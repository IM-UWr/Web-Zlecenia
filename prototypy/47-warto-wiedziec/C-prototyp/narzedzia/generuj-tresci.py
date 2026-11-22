# Generuje załącznik A zlecenia 47: pliki treści „Warto wiedzieć” dla Web-Instytut (stan docelowy).
import os, re, sys, json, shutil, yaml
sys.path.insert(0, '/home/claude/proto-src')
import dane
OUT = '/home/claude/z46/zalaczniki/A-tresci/Web-Instytut/src/content'
REPO = '/home/claude/repo/Web-Instytut/src/content/warto_wiedziec'
SYL = '/home/claude/sylwetki'
shutil.rmtree('/home/claude/z46/zalaczniki/A-tresci', ignore_errors=True)
WW = '/instytut/warto-wiedziec/'
UKLAD = '<!-- UKŁAD JAWNY: ## rozpoczyna sekcję w spisie. Nazwę można zmieniać; {#id} zachowuje adres. Bloki :::nazwa … ::: sterują wyglądem; komentarze są tylko instrukcjami dla redaktora. -->'
K_SKROT = '<!-- W SKRÓCIE: Każdy punkt: **liczba lub rok** — krótki podpis (może mieć link). 3–5 punktów. Lat życia tu nie wpisuj: są w polu „Lata”. -->'
K_TEKST = '<!-- TEKST: Zwykły Markdown. Wzmiankę o publikacji, która jest w „Źródłach”, zrób linkiem do niej. -->'
K_PLIKI = '<!-- PLIKI: Jeden dokument na punkt. Plik wgraj w „Media” i wklej link; po — można dopisać opis. -->'
K_ZRODLA = '<!-- ŹRÓDŁA: Jeden punkt = jedno źródło: [tytuł](link) — co z niego wzięto. Na stronie sekcja jest zwinięta; zostaw {#zrodla}. -->'
K_LAUR = '<!-- LAUREACI: Każdy punkt: **rok** imię i nazwisko — [aktualność](/aktualnosci/…). Nazwisko jako link do sylwetki dostaje portret. Nowych dopisuj na górze. -->'
K_TBA = '<!-- TBA: Pusta Treść = sylwetka „TBA” (imię, lata i znaczek TBA). Tekst pisz według innych sylwetek: :::w-skrocie, sekcje ## z {#id}, „## Źródła {#zrodla}”. -->'

ZYJACY = {'marek-bozejko', 'tomasz-rolski', 'piotr-biler', 'roman-duda', 'wladyslaw-narkiewicz', 'andrzej-krzywicki'}
ULUBIONE = {'hugo-steinhaus', 'edward-marczewski', 'bronislaw-knaster', 'wladyslaw-slebodzinski'}
NOWE = {'marek-bozejko', 'tomasz-rolski', 'piotr-biler'}
MAPA_ID = {'annals': 'artykul-w-annals-of-mathematics', 'wyklad-tao': 'wyklad-terencea-tao', 'pka': 'wyrozniajaca-ocena-pka',
           'trzech-rektorow': 'czterech-rektorow'}

def q(v):
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, (int, float)): return str(v)
    return json.dumps(v, ensure_ascii=False)

def front(pola):
    out = ['---']
    for k, v in pola:
        if isinstance(v, dict):
            out.append(f'{k}:')
            for k2, v2 in v.items():
                out.append(f'  {k2}: {q(v2)}')
        elif isinstance(v, list):
            if not v: out.append(f'{k}: []'); continue
            out.append(f'{k}:')
            out += [f'  - {q(x)}' for x in v]
        elif isinstance(v, str) and '\n' in v:
            out.append(f'{k}: |')
            out += [('  ' + l) if l else '' for l in v.rstrip('\n').split('\n')]
        else:
            out.append(f'{k}: {q(v)}')
    out.append('---')
    return '\n'.join(out) + '\n'

def linki(t):
    t = t.replace('https://im-uwr.github.io/Web-Podglad', '')
    t = re.sub(r'\(w-([a-z0-9-]+)\.html\)', lambda m: f'({WW}{MAPA_ID.get(m.group(1), m.group(1))})', t)
    for a, b in MAPA_ID.items():
        t = t.replace(f'{WW}{a})', f'{WW}{b})').replace(f'{WW}{a}#', f'{WW}{b}#')
    return t

def zapisz(sciezka, tekst):
    p = os.path.join(OUT, sciezka)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tekst = re.sub(r'\n{3,}', '\n\n', tekst).rstrip() + '\n'
    open(p, 'w', encoding='utf-8').write(tekst)

def czytaj_repo(nazwa):
    t = open(os.path.join(REPO, nazwa + '.md'), encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    return yaml.safe_load(m.group(1)), t[m.end():].strip()

# ------------------------------------------------------------ sylwetki
def sylwetka(_id):
    p = os.path.join(SYL, _id + '.md')
    tba = not os.path.exists(p)
    if tba:
        p = os.path.join(SYL, _id + '-szkic.md')
    t = open(p, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    f = yaml.safe_load(m.group(1))
    body = t[m.end():]
    if tba:
        f['lata'] = ''
        f['podpis'] = ''
        f['zajawka'] = ''
        tresc = UKLAD + '\n\n' + K_TBA + '\n'
    else:
        body = linki(body)
        # poprawki rektorów (18:40): czterech, z Łukaszewiczem
        body = body.replace('Edward Marczewski i [Kazimierz Urbanik](/instytut/warto-wiedziec/kazimierz-urbanik) (zob. wpis [Trzech rektorów](/instytut/warto-wiedziec/czterech-rektorow))',
                            'Edward Marczewski, [Kazimierz Urbanik](/instytut/warto-wiedziec/kazimierz-urbanik) i Józef Łukaszewicz (zob. wpis [Czterech rektorów-matematyków](/instytut/warto-wiedziec/czterech-rektorow))')
        body = body.replace('[trzech matematyków-rektorów]', '[czterech matematyków-rektorów]')
        # W skrócie: standardowy komentarz, bez lat życia
        body = re.sub(r'<!--\s*W SKRÓCIE:.*?-->\s*\n', '', body, flags=re.S)
        def skr(mm):
            wiersze = [l for l in mm.group(1).split('\n') if not re.match(r'\s*-\s*\*\*[^*]+\*\*\s*[—–-]\s*(lata życia|rok urodzenia)\s*$', l)]
            return K_SKROT + '\n:::w-skrocie\n' + '\n'.join(wiersze) + '\n:::\n\n' + K_TEKST + '\n'
        body = re.sub(r':::w-skrocie\n(.*?)\n:::\n', skr, body, count=1, flags=re.S)
        body = re.sub(r'<!--\s*PLIKI:.*?-->', K_PLIKI, body, flags=re.S)
        body = re.sub(r'(?m)^(## Źródła \{#zrodla\})\s*\n', r'\1\n\n' + K_ZRODLA + '\n', body)
        assert ':::w-skrocie' in body and K_ZRODLA in body, _id
        tresc = UKLAD + '\n\n' + body.strip() + '\n'
    pola = [
        ('tytul', f['tytul']),
        ('opublikowany', _id not in ZYJACY),
        ('lata', f.get('lata', '')),
        ('podpis', f.get('podpis', '')),
        ('podpis_en', ''),
        ('rocznica_urodzin', f.get('rocznica_urodzin', '')),
        ('karta', {'zajawka': f.get('zajawka', ''), 'zajawka_en': '', 'obraz': '', 'obraz_zrodlo': ''}),
        ('na_glownej', True),
        ('ulubione', _id in ULUBIONE),
        ('zawsze', False),
        ('dodano', ''),
        ('format_tresci', 'jawne'),
        ('tresc_en', ''),
    ]
    zapisz(f'warto_wiedziec/sylwetki/{_id}.md', front(pola) + tresc)

for _id, _ur, _por in dane.OSOBY:
    sylwetka(_id)

# ------------------------------------------------------------ nagrody i historie z prototypu
po_id = {w['id']: w for w in dane.WPISY}
OBRAZ = {'aplus': ('/pliki/aktualnosci/decyzja_5_704_2026_matematyka.jpg'), 'bogdan': '/pliki/aktualnosci/mbogdan2.jpg',
         'sierpinski': '/pliki/aktualnosci/tjan_sierpinski.jpg', 'ceremonia': '/pliki/warto-wiedziec/ceremonia.png'}

def laureaci_md(w):
    wiersze = []
    for l in w['laureaci']:
        rok, kto, akt = l[0], l[1], l[2]
        os_ = l[4] if len(l) > 4 else None
        if os_:
            pref = 'prof. ' if kto.startswith('prof. ') else ''
            kto = f'{pref}[{kto[len(pref):]}]({WW}{os_})'
        wiersze.append(f'- **{rok}** {kto} — [aktualność](/aktualnosci/{akt})')
    return f'## {w["lista_tytul"]} {{#laureaci}}\n\n{K_LAUR}\n:::laureaci\n\n' + '\n'.join(wiersze) + '\n\n:::\n'

def nowy_wpis(w, grupa):
    _id = MAPA_ID.get(w['id'], w['id'])
    tresc = linki(w['tresc'])
    if w['id'] == 'medal-uniwersytetu':
        tresc = re.sub(r'\n\n- \[Nota biograficzna profesora Marka.*', '', tresc, flags=re.S)
    karta = {}
    if grupa == 'historie':
        karta['rok'] = str(w['rok'])
    karta.update({'zajawka': w['zajawka'], 'zajawka_en': ''})
    if w.get('obraz') in OBRAZ:
        karta.update({'obraz': OBRAZ[w['obraz']], 'obraz_opis': w.get('obraz_opis', ''), 'obraz_opis_en': ''})
    body = UKLAD + '\n\n<!-- TEKST: Zwykły Markdown. Specjalny układ wymaga jawnego znacznika bloku. -->\n\n' + tresc.strip() + '\n'
    if w['id'] == 'medal-uniwersytetu':
        body += ('\n## Noty biograficzne laureatów {#noty}\n\n' + K_PLIKI + '\n:::pliki\n\n'
                 '- [Nota biograficzna prof. Marka Bożejki](/pliki/aktualnosci/marekbozejkonotabiograficzna.pdf) — przygotowana na wręczenie medalu (2026)\n'
                 '- [Nota biograficzna prof. Tomasza Rolskiego](/pliki/aktualnosci/tomaszrolskinotabiograficzna.pdf) — przygotowana na wręczenie medalu (2026)\n\n:::\n')
    if w.get('laureaci'):
        body += '\n' + laureaci_md(w)
    pola = [('tytul', w['tytul']), ('tytul_en', ''), ('opublikowany', True)]
    if grupa == 'nagrody':
        pola.append(('kolejnosc', w['kolejnosc']))
    else:
        pola.append(('rocznica', w.get('rocznica', '')))
    pola += [('karta', karta), ('na_glownej', not w.get('laureaci')), ('ulubione', w.get('stan') == 'ulubiona'),
             ('zawsze', False), ('dodano', ''), ('format_tresci', 'jawne'), ('tresc_en', ''), ('zrodla', [])]
    return _id, pola, body

ISTN = {'annals': 'artykul-w-annals-of-mathematics', 'wyklad-tao': 'wyklad-terencea-tao', 'pka': 'wyrozniajaca-ocena-pka'}

def istniejacy(w, grupa):
    nazwa = ISTN[w['id']]
    f, body = czytaj_repo(nazwa)
    k = f.get('karta', {}) or {}
    body = linki(body)
    if w['id'] == 'pka':
        body = re.sub(r'\n\n(- \[Pismo.*)', lambda m: '\n\n## Dokumenty {#dokumenty}\n\n' + K_PLIKI + '\n:::pliki\n\n' + m.group(1).strip() + '\n\n:::', body, flags=re.S)
    body = UKLAD + '\n\n<!-- TEKST: Zwykły Markdown. Specjalny układ wymaga jawnego znacznika bloku. -->\n\n' + body.strip() + '\n'
    karta = {}
    if grupa == 'historie':
        karta['rok'] = str(k.get('rok', w['rok']))
    for kk in ('zajawka', 'zajawka_en', 'obraz', 'obraz_opis', 'obraz_opis_en', 'link', 'link_etykieta', 'link_etykieta_en'):
        if k.get(kk): karta[kk] = k[kk]
    if w['id'] == 'pka':
        karta['zajawka'] = w['zajawka']   # nowa zajawka z prototypu (bez roku na karcie)
        karta['zajawka_en'] = 'For well over a decade, the Mathematics programme has held a distinction rating from the Polish Accreditation Committee and its Certificate of Quality of Education.'
    pola = [('tytul', f['tytul']), ('tytul_en', f.get('tytul_en', '')), ('opublikowany', f.get('opublikowany', True))]
    if grupa == 'nagrody':
        pola.append(('kolejnosc', w['kolejnosc']))
    else:
        pola.append(('rocznica', w.get('rocznica', '')))
    tresc_en = f.get('tresc_en', '') or ''
    if w['id'] == 'pka' and '- [' in tresc_en:
        tresc_en = re.sub(r'\n\n(- \[.*)', lambda m: '\n\n## Documents {#dokumenty}\n\n:::pliki\n\n' + m.group(1).strip() + '\n\n:::', tresc_en.strip(), flags=re.S)
    pola += [('karta', karta), ('na_glownej', f.get('na_glownej', True)), ('ulubione', w.get('stan') == 'ulubiona'),
             ('zawsze', bool(f.get('zawsze', False))), ('dodano', ''), ('format_tresci', 'jawne'),
             ('tresc_en', tresc_en.strip() + '\n' if tresc_en.strip() else ''), ('zrodla', f.get('zrodla', []) or [])]
    return nazwa, pola, body

for w in dane.WPISY:
    if w['grupa'] not in ('historie', 'nagrody'):
        continue
    g = w['grupa']
    _id, pola, body = istniejacy(w, g) if w['id'] in ISTN else nowy_wpis(w, g)
    zapisz(f'warto_wiedziec/{g}/{_id}.md', front(pola) + body)

# medal: EN ze starego wpisu (żeby strona EN nie straciła tekstu)
f_old, _ = czytaj_repo('medale-uniwersytetu-dla-profesorow-marka-bozejki-i-tomasza-rolskiego')
p = os.path.join(OUT, 'warto_wiedziec/nagrody/medal-uniwersytetu.md')
t = open(p, encoding='utf-8').read()
en = (f_old['tresc_en'].split('\n\n')[0].strip() + '\n\n'
      '## Biographical notes {#noty}\n\n:::pliki\n\n'
      '- [Biographical note of Prof. Marek Bożejko (in Polish)](/pliki/aktualnosci/marekbozejkonotabiograficzna.pdf)\n'
      '- [Biographical note of Prof. Tomasz Rolski (in Polish)](/pliki/aktualnosci/tomaszrolskinotabiograficzna.pdf)\n\n:::\n\n'
      '## Recipients from the Institute {#laureaci}\n\n:::laureaci\n\n'
      f'- **2026** Prof. [Marek Bożejko]({WW}marek-bozejko) — [news](/aktualnosci/2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego)\n'
      f'- **2026** Prof. [Tomasz Rolski]({WW}tomasz-rolski) — [news](/aktualnosci/2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego)\n\n:::\n')

t = t.replace('tytul_en: ""', 'tytul_en: "University of Wrocław Medal"', 1)
t = t.replace('tresc_en: ""', 'tresc_en: |\n' + '\n'.join(('  ' + l) if l else '' for l in en.rstrip('\n').split('\n')), 1)
t = t.replace('  zajawka_en: ""', '  zajawka_en: "Awarded by the University Senate in recognition of exceptional contributions to the University. Its recipients include Professors Marek Bożejko and Tomasz Rolski."', 1)
t = t.replace('  obraz_opis_en: ""', '  obraz_opis_en: "University of Wrocław Medal ceremony, 13 November 2026"', 1)
open(p, 'w', encoding='utf-8').write(t)

# ------------------------------------------------------------ tekst strony listy (Strony → instytut/warto-wiedziec.md)
f, body = (lambda t: (yaml.safe_load(re.match(r'---\n(.*?)\n---\n', t, re.S).group(1)), t[re.match(r'---\n(.*?)\n---\n', t, re.S).end():]))(
    open('/home/claude/repo/Web-Instytut/src/content/strony/warto-wiedziec.md', encoding='utf-8').read())
pola = [('tytul', f['tytul']), ('opublikowany', True), ('tytul_en', f.get('tytul_en', '')),
        ('opis', 'Ludzie i historie, z których wyrosła wrocławska matematyka: założyciele i profesorowie, ważne odkrycia i wyróżnienia, z których jesteśmy dumni. Bieżące sukcesy znajdziesz w Aktualnościach.'),
        ('opis_en', ''),
        ('haslo', 'Ludzie i historie wrocławskiej matematyki'), ('haslo_en', 'People and stories of Wrocław mathematics'),
        ('format_tresci', 'jawne')]
zapisz('strony/instytut/warto-wiedziec.md', front(pola) + body.strip() + '\n')
print('OK')
