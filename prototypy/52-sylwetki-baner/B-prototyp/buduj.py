#!/usr/bin/env python3
"""Prototyp nowego układu stron sylwetek „Warto wiedzieć” (IM UWr).

Buduje samodzielny folder /home/claude/ww-baner/proto/ ze zbudowanego Podglądu (pod47) i plików liczb:
  - index.html                 lista „Warto wiedzieć” (bez zmian układu, tylko linki i porządki),
  - <id>/index.html            18 stron sylwetek w nowym układzie,
  - ww-baner.css               style prototypu (opis w zmiany.md),
  - _astro/, pliki/, favicon   tylko zasoby, których te strony używają.

Uruchomienie (powtarzalne, np. gdy dojdą pliki liczb):  python3 /home/claude/ww-baner/buduj.py
Na wyjściu: tabela, skąd są liczby (JSON albo tymczasowo z „W skrócie”), figurka bez JS, rozmiar folderu.

Zmiany na stronie sylwetki:
 1. baner: klasa z-liczbami, trzy pozycje z JSON-a (ul.pt-liczby w .z-slot pod hasłem), blok „W skrócie” usunięty;
 2. baner: figurka z puli Instytutu (svg.z-znak) bez opisu, losowana skryptem w linii przy każdym wejściu;
    bez JS stała figurka wybrana po skrócie FNV-1a z id osoby;
 3. treść: .ww2-prof zamiast siatki (portret | „W skrócie”) obejmuje portret z latami (float) i wstęp, który go opływa;
    sekcje z nagłówkami h2 zaczynają się pod tym blokiem; CSS w ww-baner.css;
 4. Tabisz (TBA): baner bez liczb, figurka zostaje, ramka TBA obok portretu;
 5. komputer: imię i nazwisko zawsze w jednej linii; gdy obok figurki się nie mieści, figurka znika (wstawka do skryptu
    dopasowania nagłówka, klasa z-znak-brak; bez JS klasa z-tyt-dlugi-bez-js dla tytułów > 28 znaków).
Źródło stylów prototypu: /home/claude/ww-baner/ww-baner.css (kopiowany do proto/). Raport: /home/claude/ww-baner/raport-budowy.json.
"""
import html
import json
import os
import re
import shutil
import sys
from pathlib import Path

POD = Path('/home/claude/pod47')
OUT = Path('/home/claude/ww-baner/proto')
LICZBY = Path('/home/claude/ww-baner/liczby')
CSS_PROTO = Path('/home/claude/ww-baner/ww-baner.css')
PULA = Path('/home/claude/repo/Web-Core/src/data/ciekawostki/instytut.json')
ZEW = 'https://im-uwr.github.io/Web-Podglad/'
WW = 'instytut/warto-wiedziec'
OSOBY = ['wladyslaw-slebodzinski', 'hugo-steinhaus', 'bronislaw-knaster', 'edward-marczewski', 'witold-wolibner',
         'julian-perkal', 'stanislaw-hartman', 'czeslaw-ryll-nardzewski', 'kazimierz-urbanik', 'jan-mycielski',
         'andrzej-hulanicki', 'andrzej-krzywicki', 'roman-duda', 'wladyslaw-narkiewicz', 'marek-bozejko',
         'tomasz-rolski', 'piotr-biler', 'krzysztof-tabisz']
# rozszerzenia plików, które kopiujemy jako zasoby (reszta, np. PDF, idzie jako link do Podglądu)
ZASOBY = ('.css', '.js', '.woff2', '.woff', '.ttf', '.jpg', '.jpeg', '.png', '.webp', '.avif', '.svg', '.gif', '.ico')


def blad(msg):
    print('BŁĄD:', msg, file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------- figurki (pula Instytutu)
def liczba(m):
    s = repr(round(float(m) * 10) / 10)
    if s.endswith('.0'):
        s = s[:-2]
    if s == '-0':
        s = '0'
    return re.sub(r'^(-?)0\.', r'\1.', s)


def kompakt_d(d):
    """To samo co kompaktD w src/lib/ciekawostki.ts (liczby do 0,1, bez zbędnych spacji)."""
    d = re.sub(r'-?\d*\.?\d+(?:e[-+]?\d+)?', lambda m: liczba(m.group(0)), d, flags=re.I)
    d = re.sub(r'\s*([A-Za-z])\s*', r'\1', d)
    d = re.sub(r'\s*,\s*', ',', d)
    d = re.sub(r'\s+', ' ', d)
    d = re.sub(r' (?=-)', '', d)
    return d.strip()


def wczytaj_pule():
    karty = json.loads(PULA.read_text(encoding='utf-8'))
    pula = [c for c in karty if not c.get('ukryta') and c.get('stan') != 'odpada']
    if not pula:
        blad('pusta pula figurek')
    return [{'id': c['id'], 'waga': 3 if c.get('stan') == 'ulubiona' else 1,
             'sciezki': [(kompakt_d(k['d']), bool(k.get('gruba'))) for k in c['sciezki']]} for c in pula]


def fnv1a(s):
    h = 0x811c9dc5
    for b in s.encode('utf-8'):
        h ^= b
        h = (h * 0x01000193) & 0xffffffff
    return h


def figurka_stala(pula, osoba):
    return pula[fnv1a(osoba) % len(pula)]


def svg_znaku(karta):
    sc = ''.join(f'<path d="{d}" pathLength="1"{" class=\"gruba\"" if g else ""}></path>' for d, g in karta['sciezki'])
    return f'<svg class="z-znak" viewBox="0 0 200 240" aria-hidden="true" focusable="false">{sc}</svg>'


# Losowanie przy każdym wejściu (skrypt w linii zaraz za svg.z-znak, zanim strona się narysuje):
#  - kandydaci: cała pula bez figurki z poprzedniej sylwetki w tej wizycie (sessionStorage „im-ww-znak”) i bez ciekawostki,
#    którą w tej wizycie pokazuje lista „Warto wiedzieć” (zestaw „im-ciek-zestaw” z NaglowekZ.astro); gdy nic nie zostaje — cała pula;
#  - wybór ważony (ulubiona — waga 3, jak w ciekawostkach);
#  - do końca skryptu figurka niewidoczna (.z-ck-losuje, CSS jak na Pracownikach), więc stała z budowania nie mignie.
# D = [[id, waga, [[d, gruba?], …]], …]
ZNAK_JS = (
    "(function(n,D){var K='im-ww-znak',v=n.querySelector('.z-znak'),bez={},s=0,r,i,j,c,p,k;"
    "try{bez[sessionStorage.getItem(K)]=1;bez[((JSON.parse(sessionStorage.getItem('im-ciek-zestaw')||'{}')||{}).instytut||{})['/instytut/warto-wiedziec']]=1}catch(e){}"
    "try{k=D.filter(function(c){return!bez[c[0]]});if(!k.length)k=D;"
    "for(i=0;i<k.length;i++)s+=k[i][1];r=Math.random()*s;for(i=0;i<k.length-1;i++){r-=k[i][1];if(r<0)break}c=k[i];"
    "if(v&&c[0]!==n.getAttribute('data-ck')){while(v.firstChild)v.removeChild(v.firstChild);"
    "for(j=0;j<c[2].length;j++){p=document.createElementNS('http://www.w3.org/2000/svg','path');p.setAttribute('d',c[2][j][0]);"
    "p.setAttribute('pathLength','1');if(c[2][j][1])p.setAttribute('class','gruba');v.appendChild(p)}n.setAttribute('data-ck',c[0])}"
    "try{sessionStorage.setItem(K,c[0])}catch(e){}}catch(e){}finally{n.classList.remove('z-ck-losuje')}})"
)


# Decyzja 18.11, 23:26: na komputerze (≥ 1024 px) imię i nazwisko w jednej linii. Wstawka do skryptu dopasowania (DOPASUJ
# w NaglowekZ.astro), na początku każdego dopasowania (wczytanie, zmiana rozmiaru okna, wczytanie krojów), przed układem tytułu,
# hasła i liczb: zdejmuje klasę z-znak-brak, mierzy szerokość tytułu w jednej linii (h1 ma white-space: nowrap, pomiar
# zakresem tekstu, bez stylów z poprzedniego dopasowania) i gdy lewa krawędź tytułu + szerokość + 40 px wychodzi za lewą
# krawędź figurki, dodaje klasę z-znak-brak (figurka display: none). Dalej dopasowanie liczy granice już bez figurki.
# Zdjęcie i dodanie klasy dzieją się w jednym przebiegu skryptu, przed malowaniem — bez mignięcia. Telefon: klasa zdjęta, bez zmian.
DOPASUJ_PRZED = "if(dod)dod.classList.remove('z-brak-miejsca');var zaDlugi=uklad();"
DOPASUJ_ZNAK = (
    "var zs=n.classList.contains('z-znak-sam')&&n.querySelector('.z-znak');"
    "if(zs){n.classList.remove('z-znak-brak');if(!tel&&h1){h1.style.fontSize='';h1.style.maxWidth='';"
    "var zr=zs.getBoundingClientRect(),q=document.createRange();q.selectNodeContents(h1);"
    "if(zr.width&&h1.getBoundingClientRect().left+q.getBoundingClientRect().width+40>zr.left)n.classList.add('z-znak-brak')}}"
)


def dane_js(pula):
    d = [[c['id'], c['waga'], [[dd, 1] if g else [dd] for dd, g in c['sciezki']]] for c in pula]
    return json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')


# ---------------------------------------------------------------- liczby do banera
def tekst(h):
    return html.unescape(re.sub(r'<[^>]+>', '', h)).strip()


def utnij(s, limit=20):
    """Podpis tymczasowy: całe słowa do ok. 18–20 znaków, „…” gdy ucięty."""
    if len(s) <= limit:
        return s
    out = ''
    for w in s.split():
        if len((out + ' ' + w).strip()) > limit:
            break
        out = (out + ' ' + w).strip()
    return (out or s[:limit - 1]).rstrip(',;:') + '…'


def liczby_osoby(osoba, strona):
    """→ (lista [(n, podpis)], źródło: 'json' | 'tymczasowe' | 'brak', uwaga)"""
    plik = LICZBY / f'{osoba}.json'
    uwaga = ''
    if plik.exists():
        try:
            d = json.loads(plik.read_text(encoding='utf-8'))
            poz = [(str(x['n']).strip(), str(x['podpis']).strip()) for x in d['liczby']]
            if len(poz) == 3 and all(n and p for n, p in poz):
                return poz, 'json', ''
            uwaga = f'{plik.name}: {len(poz)} pozycji zamiast 3'
        except Exception as e:  # zły JSON — tymczasowe z „W skrócie”
            uwaga = f'{plik.name}: {e}'
    pkt = re.findall(r'<div><dt>(.*?)</dt><dd>(.*?)</dd></div>', blok_skrotu(strona) or '', re.S)
    if not pkt:
        return [], 'brak', uwaga
    return [(tekst(n), utnij(tekst(p))) for n, p in pkt[:3]], 'tymczasowe', uwaga


def blok_skrotu(strona):
    m = re.search(r'<dl class="ww2-skrot">.*?</dl>', strona, re.S)
    return m.group(0) if m else None


def twarde_spacje(s):
    """Polska zasada składu: jednoliterowe a, i, o, u, w, z nie zostają na końcu linii (twarda spacja po nich),
    np. „doktorat u Hartmana” na telefonie łamie się „doktorat / u Hartmana”."""
    return re.sub(r'(?<!\S)([aiouwzAIOUWZ]) ', '\\1\u00a0', s)


def html_liczb(poz):
    li = ''.join(f'<li><span class="n">{html.escape(n)}</span>{html.escape(twarde_spacje(p))}</li>' for n, p in poz)
    return f'<div class="z-slot"><ul class="pt-liczby" data-pagefind-ignore>{li}</ul></div>'


# ---------------------------------------------------------------- przekształcenia stron
def jedno(wzor, s, opis, flags=re.S):
    m = list(re.finditer(wzor, s, flags))
    if len(m) != 1:
        blad(f'{opis}: {len(m)} trafień wzoru {wzor[:60]!r}')
    return m[0]


def porzadki(s):
    """Wspólne dla wszystkich stron prototypu: bez plakietki stanu budowy (odpytuje API GitHuba) i bez reguł
    wczytywania z wyprzedzeniem (wzorce adresów /Web-Podglad/* nie pasują do prototypu)."""
    s = re.sub(r'<link rel="stylesheet" href="/Web-Podglad/podglad/stan-budowy\.css[^"]*">', '', s)
    s = re.sub(r'<div id="stan-budowy"[^>]*>.*?</div><script defer src="/Web-Podglad/podglad/stan-budowy\.js[^"]*"></script>', '', s,
               flags=re.S)
    s = re.sub(r'<script type="speculationrules">.*?</script>', '', s, flags=re.S)
    if 'stan-budowy' in s:
        blad('zostały ślady plakietki stanu budowy')
    return s


def przebuduj_sylwetke(osoba, s, pula, js_dane):
    raport = {'osoba': osoba}
    # --- liczby
    poz, zrodlo, uwaga = liczby_osoby(osoba, s)
    raport.update(liczby=poz, zrodlo=zrodlo, uwaga=uwaga)
    ma_haslo = '<p class="z-haslo">' in s
    z_liczbami = bool(poz) and ma_haslo
    if poz and not ma_haslo:
        raport['uwaga'] = (raport['uwaga'] + '; ' if raport['uwaga'] else '') + 'liczby bez hasła — pominięte (jak w NaglowekZ)'
    # --- baner: klasy, liczby, figurka
    karta = figurka_stala(pula, osoba)
    raport['figurka_bez_js'] = karta['id']
    m = jedno(r'<div class="z-nagl z-nagl-pod" data-dzial="instytut" data-pagefind-ignore>', s, f'{osoba}: baner')
    tytul = tekst(jedno(r'<h1 data-pagefind-meta="title">(.*?)</h1>', s, f'{osoba}: tytuł').group(1))
    # bez JS tytułu nie da się zmierzyć: długi tytuł (> 28 znaków, ok. 0,5 em na znak, granica ok. 15,6 em) — figurka chowana
    dlugi = len(tytul) > 28
    raport['tytul'] = tytul
    klasy = ('z-nagl z-nagl-pod' + (' z-liczbami' if z_liczbami else '') + ' z-ck-losuje z-znak-sam'
             + (' z-tyt-dlugi-bez-js' if dlugi else ''))
    s = s[:m.start()] + f'<div class="{klasy}" data-dzial="instytut" data-ck="{karta["id"]}" data-pagefind-ignore>' + s[m.end():]
    if z_liczbami:
        m = jedno(r'<p class="z-haslo">.*?</p>', s, f'{osoba}: hasło')
        s = s[:m.end()] + html_liczb(poz) + s[m.end():]
    # figurka i skrypt losowania: za blokiem .z-tyt, przed skryptem dopasowania (jak ciekawostka na Pracownikach)
    m = jedno(r'</div><script>\(function\(n\)\{function px\(v\)', s, f'{osoba}: koniec .z-tyt')
    znak = svg_znaku(karta) + f'<script>{ZNAK_JS}(document.currentScript.parentElement,{js_dane});</script>'
    s = s[:m.start() + 6] + znak + s[m.start() + 6:]
    # --- treść: portret z latami opływany tekstem; „W skrócie” znika
    # .ww2-prof przestaje być siatką (portret | liczby): obejmuje portret (float) i wstęp albo ramkę TBA, które go opływają
    m = jedno(r'<div class="ww2-prof"> (<div class="ww2-prof-l">.*?</div>) <div class="ww2-prof-tr">.*?</div> </div>\s*'
              r'(<div class="ww2-wstep ww2-tresc"><div class="prose">.*?</div></div>|<div class="ww2-tba">.*?</div>)', s,
              f'{osoba}: głowa sylwetki')
    if '<div' in m.group(2)[5:].replace('<div class="prose">', '', 1):
        blad(f'{osoba}: wstęp z zagnieżdżonym <div> — wzorzec do poprawy')
    s = s[:m.start()] + '<div class="ww2-prof">' + m.group(1) + m.group(2) + '</div>' + s[m.end():]
    if 'ww2-skrot' in s or 'ww2-prof-tr' in s:
        blad(f'{osoba}: został blok „W skrócie”')
    # skrypt dopasowania nagłówka: na komputerze imię i nazwisko zawsze w jednej linii; gdy obok figurki się nie mieści — figurka znika
    if s.count(DOPASUJ_PRZED) != 1:
        blad(f'{osoba}: nie znaleziono miejsca w skrypcie dopasowania nagłówka')
    s = s.replace(DOPASUJ_PRZED, DOPASUJ_ZNAK + DOPASUJ_PRZED)
    # style prototypu
    s = s.replace('</head>', '<link rel="stylesheet" href="/Web-Podglad/ww-baner.css"></head>', 1)
    return s, raport


# ---------------------------------------------------------------- adresy
ADRES = re.compile(r'(?<![\w.:/-])/Web-Podglad/([^"\'\s)<>,]*)')


def przepisz_adresy(s, glebokosc, zasoby):
    """/Web-Podglad/… → ścieżki względne (strony prototypu i skopiowane zasoby) albo pełny adres Podglądu."""
    wyzej = '../' * glebokosc

    def zamien(m):
        sciezka = m.group(1)
        sc, _, hash_ = sciezka.partition('#')
        sc, _, query = sc.partition('?')
        bez = sc.rstrip('/')
        kotwica = f'#{hash_}' if hash_ else ''
        if bez == WW:
            return f'{wyzej}index.html{kotwica}'
        if bez.startswith(WW + '/') and bez[len(WW) + 1:] in OSOBY:
            return f'{wyzej}{bez[len(WW) + 1:]}/index.html{kotwica}'
        if bez == 'ww-baner.css':
            return f'{wyzej}ww-baner.css'
        if bez.lower().endswith(ZASOBY) and (POD / bez).is_file():
            zasoby.add(bez)
            return f'{wyzej}{bez}'
        return ZEW + sciezka

    # url() w zmiennej CSS (np. style="--logo:url(...)") liczy się względem arkusza, który używa var(), czyli _astro/*.css
    def zmienna(m):
        zasoby.add(m.group(2))
        return f'{m.group(1)}../{m.group(2)})'
    s = re.sub(r'(--[\w-]+:\s*url\()/Web-Podglad/([^)\s]+)\)', zmienna, s)
    return ADRES.sub(zamien, s)


def kopiuj_zasoby(zasoby):
    """Kopiuje zasoby; CSS i JS przegląda w poszukiwaniu kolejnych (url(...), import "./x.js")."""
    zrobione = set()
    kolejka = list(zasoby)
    while kolejka:
        z = kolejka.pop()
        if z in zrobione:
            continue
        zrobione.add(z)
        src, dst = POD / z, OUT / z
        dst.parent.mkdir(parents=True, exist_ok=True)
        if z.endswith('.css'):
            t = src.read_text(encoding='utf-8')
            nowe = set()
            glebokosc = z.count('/')
            t = przepisz_adresy(t, glebokosc, nowe)
            kolejka += [n for n in nowe if n not in zrobione]
            dst.write_text(t, encoding='utf-8')
        elif z.endswith('.js'):
            t = src.read_text(encoding='utf-8')
            if '/Web-Podglad/' in t:
                blad(f'{z}: adres /Web-Podglad/ w skrypcie')
            for imp in re.findall(r'(?:from|import)\s*["\'](\./[^"\']+)["\']', t):
                kolejka.append(os.path.normpath(os.path.join(os.path.dirname(z), imp)))
            shutil.copyfile(src, dst)
        else:
            shutil.copyfile(src, dst)
    return zrobione


# ---------------------------------------------------------------- budowa
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    pula = wczytaj_pule()
    js_dane = dane_js(pula)
    zasoby = {'favicon.svg'}
    raporty = []
    for osoba in OSOBY:
        s = (POD / WW / osoba / 'index.html').read_text(encoding='utf-8')
        s = porzadki(s)
        s, r = przebuduj_sylwetke(osoba, s, pula, js_dane)
        s = przepisz_adresy(s, 1, zasoby)
        (OUT / osoba).mkdir()
        (OUT / osoba / 'index.html').write_text(s, encoding='utf-8')
        raporty.append(r)
    s = (POD / WW / 'index.html').read_text(encoding='utf-8')
    s = przepisz_adresy(porzadki(s), 0, zasoby)
    (OUT / 'index.html').write_text(s, encoding='utf-8')
    skopiowane = kopiuj_zasoby(zasoby)
    shutil.copyfile(CSS_PROTO, OUT / 'ww-baner.css')
    # kontrola: żadnego /Web-Podglad/ w stronach (poza pełnymi adresami Podglądu)
    for p in OUT.rglob('*.html'):
        t = p.read_text(encoding='utf-8')
        if ADRES.search(t):
            blad(f'{p}: został adres /Web-Podglad/')
    # raport
    print(f'{"osoba":26} {"źródło":11} {"figurka bez JS":36} liczby')
    for r in raporty:
        lic = ' · '.join(f'{n} {p}' for n, p in r['liczby']) or '—'
        print(f'{r["osoba"]:26} {r["zrodlo"]:11} {r["figurka_bez_js"]:36} {lic}' + (f'   [{r["uwaga"]}]' if r['uwaga'] else ''))
    ile = {k: sum(r['zrodlo'] == k for r in raporty) for k in ('json', 'tymczasowe', 'brak')}
    rozmiar = sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
    print(f'\nliczby z JSON: {ile["json"]}, tymczasowe z „W skrócie”: {ile["tymczasowe"]}, bez liczb: {ile["brak"]}')
    print(f'pula figurek: {len(pula)} kart; zasobów skopiowanych: {len(skopiowane)}; rozmiar folderu: {rozmiar / 1e6:.1f} MB')
    (OUT.parent / 'raport-budowy.json').write_text(json.dumps(raporty, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
