"""Podsumowanie wyniki.json: macierz strona × okno (liczba różnych problemów) i lista problemów per grupa."""
import json, os, sys
from collections import defaultdict

KAT = os.path.dirname(os.path.abspath(__file__))
wyniki = json.load(open(os.path.join(KAT, 'wyniki.json')))
OKNA = ['800x900', '860x780', '960x950', '1024x700', '1180x820', '1280x600', '1366x620', '1440x780', '1536x730', '1707x830', '1920x950']
SKROT = {'kolizja': 'K', 'poza-ramka': 'R', 'obciety': 'O', 'poza-oknem': 'W'}

dane = defaultdict(dict)  # strona -> okno -> {problemy: {(typ, tekst): {...}}, przewX, banerDol}
grupy = {}
for z in wyniki:
    s, o = z['strona'], z['okno']
    grupy[s] = z['grupa']
    wpis = {'problemy': {}, 'przewX': 0, 'banerDol': None, 'blad': z.get('blad'), 'adres': z['adres']}
    for stan, d in z.get('stany', {}).items():
        wpis['przewX'] = max(wpis['przewX'], d['przewijanieX'])
        if stan == 'start':
            wpis['banerDol'] = d.get('banerDol')
        for p in d['problemy']:
            k = (p['typ'], p['tekst'])
            if k not in wpis['problemy']:
                wpis['problemy'][k] = {**p, 'stany': [stan]}
            elif stan not in wpis['problemy'][k]['stany']:
                wpis['problemy'][k]['stany'].append(stan)
    dane[s][o] = wpis

def komorka(w):
    if w is None:
        return '—'
    if w.get('blad'):
        return 'BŁĄD'
    c = defaultdict(int)
    for (typ, _), _p in w['problemy'].items():
        c[SKROT[typ]] += 1
    t = ''.join(f'{k}{c[k]}' for k in 'KROW' if c[k])
    if w['przewX'] > 1:
        t += f' X{w["przewX"]}'
    return t or 'ok'

def macierz(strony):
    wiersze = ['| strona | ' + ' | '.join(OKNA) + ' |', '|' + '---|' * (len(OKNA) + 1)]
    for s in strony:
        wiersze.append(f'| {s} | ' + ' | '.join(komorka(dane[s].get(o)) for o in OKNA) + ' |')
    return '\n'.join(wiersze)

def lista(strony):
    out = []
    for s in strony:
        out.append(f'\n### {s}  ({next(iter(dane[s].values()))["adres"]})')
        # zgrupuj ten sam problem z różnych okien
        zebrane = defaultdict(list)
        for o in OKNA:
            w = dane[s].get(o)
            if not w:
                continue
            for (typ, tekst), p in w['problemy'].items():
                zebrane[(typ, tekst, p['el'][-70:], (p.get('ramka') or p.get('el2') or '')[-70:])].append((o, p['px'], ','.join(p['stany'])))
        if not zebrane:
            out.append('brak wykrytych problemów')
        for (typ, tekst, el, el2), okna in sorted(zebrane.items(), key=lambda x: (x[0][0], -len(x[1]))):
            okna_t = ', '.join(f'{o}({px}px{"" if st == "start" else " " + st})' for o, px, st in okna)
            out.append(f'- **{typ}** „{tekst}” — {el}' + (f' ⟷ {el2}' if el2 else '') + f'\n  okna: {okna_t}')
        bd = {o: dane[s][o]['banerDol'] for o in OKNA if o in dane[s]}
        out.append(f'- nagłówek kończy się na y=' + ', '.join(f'{o}:{v}' for o, v in bd.items()))
    return '\n'.join(out)

if __name__ == '__main__':
    grupy_raportu = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {'wszystko': sorted(dane)}
    os.makedirs(os.path.join(KAT, 'podsumowania'), exist_ok=True)
    for nazwa, strony in grupy_raportu.items():
        strony = [s for s in strony if s in dane]
        tekst = f'# Pomiar automatyczny — {nazwa}\n\nLegenda komórek: K = kolizje tekstu, R = tekst poza ramką (kafelek/pole/przycisk), O = tekst obcięty przez overflow, W = tekst poza oknem, X = poziome przewijanie strony (px), ok = nic nie wykryto. Liczby to różne problemy (łącznie ze stanami: rozwinięte kafelki, menu, drugi ekran).\n\n' + macierz(strony) + '\n\n## Szczegóły\n' + lista(strony)
        open(os.path.join(KAT, 'podsumowania', f'{nazwa}.md'), 'w').write(tekst)
        print(nazwa, len(strony), 'stron')
