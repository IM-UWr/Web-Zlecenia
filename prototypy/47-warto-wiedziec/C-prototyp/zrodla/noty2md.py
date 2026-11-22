import re, sys
def czysc(path):
    L = open(path, encoding='utf-8').read().split('\n')
    out = []
    for l in L:
        if re.search(r'N OTA B I O G|M A R E K B O|Nota biograficzna\s+\d|^\s*Profesor Tomasz Rolski \|', l):
            continue
        out.append(l.rstrip())
    return out

def akapity(lines, naglowki, szer):
    paras, cur = [], []
    def flush():
        if cur:
            t = ''
            for x in cur:
                x = x.strip()
                if t.endswith('‐') or t.endswith('-') and re.search(r'[a-ząćęłńóśźż]-$', t) and False:
                    t = t[:-1] + x
                elif t.endswith('‐'):
                    t = t[:-1] + x
                else:
                    t = (t + ' ' + x).strip()
            paras.append(('p', t)); cur.clear()
    for i, l in enumerate(lines):
        s = l.strip()
        if not s:
            flush(); continue
        if s in naglowki:
            flush(); paras.append(('h', s)); continue
        cur.append(l)
        # koniec akapitu: krótka linia zakończona kropką (układ PDF bez pustych linii)
        if szer and s.endswith(('.', '.”')) and len(l.rstrip()) < szer:
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
            if nxt and (nxt[0].isupper() or nxt[0] in '„'):
                flush()
    flush()
    return paras
