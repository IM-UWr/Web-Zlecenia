import re, glob, os, sys
# Linkowanie wzmianek o źródłach w prozie sylwetek (18.11, 17:54).
# Reguły: (A) tytuł w cudzysłowie = tytuł z linku w Źródłach; (B) czasopismo + wspólny numer/rok w zdaniu;
# (C) nazwane serwisy (MGP, MacTutor, Encyklopedia Solidarności) przy pierwszej wzmiance;
# (E) fraza z linku (≥3 słowa, bez cudzysłowów) odmieniona w prozie. Jeden link na URL w pliku, bez linków w :::bloki.
CZASOPISMA = ['colloquium mathematicum','studia mathematica','wiadomości matematyczne','fundamenta mathematicae','zastosowania matematyki',
 'probability and mathematical statistics','przegląd uniwersytecki','przegląd antropologiczny','acta arithmetica','mathematica applicanda',
 'annales polonici mathematici','applicationes mathematicae','arkiv för matematik','rocznik pau','biuletyn ptm','dissertationes mathematicae']
POMIN_URL = ('ersearch2.cvtisr.sk', 'encysol.pl/es/encyklopedia/hasla-rzeczowe')
Q = re.compile(r'([„"])([^”"]{2,160})([”"])')
W = re.compile(r'[A-Za-zÀ-žĄĆĘŁŃÓŚŹŻąćęłńóśźż’\']+')
def norm(s): return re.sub(r'\s+', ' ', s.strip().lower().rstrip('.,'))
def stem(w): w = w.lower(); return w[:5] if len(w) > 5 else w
def ten_sam_tekst(a, b):
    wa, wb = W.findall(a), W.findall(b)
    return len(wa) == len(wb) and len(wa) > 0 and all(stem(x) == stem(y) for x, y in zip(wa, wb))
def czasopismo(q):
    return any(ten_sam_tekst(q, c) for c in CZASOPISMA)
def liczby(s): return set(re.findall(r'\b\d{2,4}\b', s))

tryb = sys.argv[1] if len(sys.argv) > 1 else 'pokaz'
FAZA = 'A'
for f in sorted(glob.glob('/home/claude/sylwetki/*.md')):
    b = os.path.basename(f)
    if b.endswith(('-weryfikacja.md', '-szkic.md')) or b == 'BRIEF.md': continue
    t = open(f).read(); i = t.find('\n## Źródła')
    if i < 0: continue
    proza, zr = t[:i], t[i:]
    fm = proza.find('\n---', 4) + 4
    head, body = proza[:fm], proza[fm:]
    TYTUL = re.search(r'^tytul:\s*"?([^"\n]+)', head, re.M).group(1)
    zrodla = [(tx, u) for tx, u in re.findall(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', zr) if not any(p in u for p in POMIN_URL)]
    uzyte_url = set(re.findall(r'\]\((https?://[^)\s]+)\)', body))
    zmiany = []
    # tnij treść: linki i bloki ::: zostają nietknięte
    kaw = re.split(r'(\[[^\]]*\]\([^)]*\)|\n:::[\s\S]*?\n:::|\n## [^\n]*)', body)
    for k in range(0, len(kaw), 2):
        seg = kaw[k]
        _ochr = re.sub(r'„[^”]*”', lambda m: m.group(0).replace('. ', '.\x01'), seg)
        zdania = [z.replace('.\x01', '. ') for z in re.split(r'(?<=[.!?])(\s+)', _ochr)]
        for zi in range(0, len(zdania), 2):
            s = zdania[zi]
            # (A) i (B): cudzysłowy
            def sub_q(m):
                q = m.group(2)
                for tx, u in zrodla:
                    if u in uzyte_url: continue
                    tyt = [y for _, y, _ in Q.findall(tx)]
                    if not czasopismo(q) and FAZA == 'A':
                        _a = norm(q)
                        if len(_a) >= 20 and _a[:25] in norm(re.sub(r'[„”"]', '', tx)) and not any(norm(y) == _a for y in tyt if czasopismo(y)):
                            uzyte_url.add(u); zmiany.append(('A*', q, u)); return f'[{m.group(0)}]({u})'
                        for y in tyt:
                            if czasopismo(y): continue
                            a, c = norm(q), norm(y)
                            if len(a) >= 4 and (a == c or ten_sam_tekst(a, c) or (len(c) >= 12 and a.startswith(c)) or (len(a) >= 12 and c.startswith(a))):
                                uzyte_url.add(u); zmiany.append(('A', q, u)); return f'[{m.group(0)}]({u})'
                    elif czasopismo(q) and FAZA == 'B':
                        txn = tx
                        if any(ten_sam_tekst(q, y) for y in tyt) or any(ten_sam_tekst(q, ' '.join(W.findall(txn)[j:j+len(W.findall(q))])) for j in range(len(W.findall(txn)))):
                            wspolne = (liczby(s) & liczby(tx)) - {'19', '20'}
                            if wspolne:
                                uzyte_url.add(u); zmiany.append(('B', q + ' ' + '/'.join(sorted(wspolne)), u)); return f'[{m.group(0)}]({u})'
                return m.group(0)
            FAZA = 'A'; s2 = Q.sub(sub_q, s)
            FAZA = 'B'; s2 = re.sub(r'(?<!\[)' + Q.pattern, sub_q, s2)
            # (C) nazwane serwisy
            for nazwa in ['Mathematics Genealogy Project', 'MacTutor', 'Encyklopedi[a-zęi]* Solidarności']:
                mm = re.search(r'(?<!\[)\b(' + nazwa + r')\b(?![^\[]*\]\()', s2)
                if not mm: continue
                for tx, u in zrodla:
                    if u in uzyte_url: continue
                    if re.search(nazwa.split('[')[0][:8], tx, re.I) and ('genealogy' in u or 'mactutor' in u or 'encysol' in u):
                        s2 = s2[:mm.start(1)] + f'[{mm.group(1)}]({u})' + s2[mm.end(1):]
                        uzyte_url.add(u); zmiany.append(('C', mm.group(1), u)); break
            # (E) frazy bez cudzysłowów (≥3 słowa) z tekstu linku
            for tx, u in zrodla:
                if u in uzyte_url or Q.search(tx): continue
                fr = re.split(r'\s+[—–-]\s+|,\s*', tx)[0]
                wf = W.findall(fr)
                if ten_sam_tekst(fr, TYTUL) or all(stem(x) in {stem(y) for y in W.findall(TYTUL + ' Rylla Nardzewskiego')} for x in wf): continue
                if not (3 <= len(wf) <= 8): continue
                slowa = list(W.finditer(s2))
                for j in range(len(slowa) - len(wf) + 1):
                    okno = slowa[j:j+len(wf)]
                    if all(stem(x.group(0)) == stem(y) for x, y in zip(okno, wf)):
                        a_, b_ = okno[0].start(), okno[-1].end()
                        if '[' in s2[max(0,a_-1):a_] or '](' in s2[b_:b_+2]: break
                        s2 = s2[:a_] + f'[{s2[a_:b_]}]({u})' + s2[b_:]
                        uzyte_url.add(u); zmiany.append(('E', s2[a_+1:a_+1+(b_-a_)], u)); break
            zdania[zi] = s2
        kaw[k] = ''.join(zdania)
    nowy = head + ''.join(kaw) + zr
    print('==', b)
    for r, q, u in zmiany: print(f'   {r} {q[:70]:72} -> {u[:70]}')
    if tryb == 'zastosuj' and nowy != t:
        open(f, 'w').write(nowy)
