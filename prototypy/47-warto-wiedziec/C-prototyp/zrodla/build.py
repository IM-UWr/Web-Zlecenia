#!/usr/bin/env python3
"""Prototyp „Warto wiedzieć” w Instytucie (18.11.2026).
Bierze zbudowane strony Web-Podglad (gałąź zbudowana) i podmienia treść:
  index.html  — lista Warto wiedzieć na szablonie podstrony Instytutu (wzór: /instytut/wladze)
  w-<id>.html — wpisy (wzór: /warto-wiedziec/wyklad-terencea-tao)
  glowna.html — strona główna z nowym losowaniem rzędu „Warto wiedzieć”
"""
import html, os, re, shutil, sys, json
from datetime import date
import markdown
from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from dane import WPISY, GRUPY, LIVE

ZB = '/home/claude/repo/zb'
CIEK = '/home/claude/repo/Web-Core/src/data/ciekawostki'
OUT = os.environ.get('OUT', '/home/claude/proto2')
DZIS = date(2026, 11, 18)
GRUPA = dict(GRUPY)
PO_ID = {w['id']: w for w in WPISY}
assets = set()
styl_url = set()  # adresy z url() w atrybutach style — kopia także pod _astro/, bo zmienne CSS liczą adres od pliku stylów

def czytaj(p):
    return open(os.path.join(ZB, p), encoding='utf-8').read()

def strona_wpisu(i):
    return f'w-{i}.html'

# ------------------------------------------------------------------ portrety
def _svg(dzial, klasa, nowa):
    h = czytaj(f'{dzial}/index.html')
    m = re.search(r'<svg class="' + klasa + r'"[\s\S]*?</svg>', h)
    t = m.group(0)
    t = re.sub(r'^<svg class="[^"]*"', f'<svg class="{nowa}"', t)
    t = t.replace(' data-dzial-szkic="' + dzial + '"', '')
    return t

SZKICE, PODPISY = {}, {}
def szkic(dzial):
    if dzial not in SZKICE:
        SZKICE[dzial] = _svg(dzial, 'z-szkic', 'ww2-sz')
    return SZKICE[dzial]
def podpis_svg(dzial):
    if dzial not in PODPISY:
        PODPISY[dzial] = _svg(dzial, 'z-podpis pisze', 'ww2-podpis')
    return PODPISY[dzial]

# 18.11 (14:56): na razie w miejscu każdego zdjęcia placeholder — także u patronów (szkice) i Bożejki
ZDJECIA = False
SYLWETKA_SVG = ('<svg viewBox="0 0 80 100" aria-hidden="true"><circle cx="40" cy="36" r="15"/>'
                '<path d="M12 96c0-17 12.5-30 28-30s28 13 28 30"/></svg>')

def portret(w, klasa=''):
    if not ZDJECIA:
        return f'<span class="ww2-portret ww2-ph {klasa}" aria-hidden="true">{SYLWETKA_SVG}<small>Zdjęcie</small></span>'
    if w.get('szkic'):
        return f'<span class="ww2-portret ww2-szkic {klasa}" aria-hidden="true">{szkic(w["szkic"])}</span>'
    if w.get('portret'):
        return f'<span class="ww2-portret ww2-foto {klasa}"><img src="./pliki/ww/{w["portret"]}.jpg" alt="" decoding="async"></span>'
    return f'<span class="ww2-portret ww2-mono {klasa}" aria-hidden="true"><span>{w.get("monogram", "")}</span></span>'

# 18.11 (17:48): „Inne sylwetki” na stronie osoby = 4 losowe inne sylwetki (bez TBA).
# Bez JS widać 4 wybrane stałym ziarnem (inne na każdej stronie); skrypt losuje przy każdym wejściu.
import random as _random
def inne_sylwetki(w, ile=4):
    pula = sorted([x for x in WPISY if x.get('typ') == 'osoba' and x is not w and not x.get('tba')], key=lambda x: x.get('sort', 0))
    start = set(o['id'] for o in _random.Random(w['id']).sample(pula, min(ile, len(pula))))
    li = ''.join(
        f'<li{"" if o["id"] in start else " hidden"}><a href="{strona_wpisu(o["id"])}">{portret(o)}<b>{esc(o["tytul"])}</b><small>{esc(o["lata"])}</small></a></li>'
        for o in pula)
    skrypt = ('<script>(function(){var u=document.currentScript.previousElementSibling.previousElementSibling,'
              'l=[].slice.call(u.children),n=+u.dataset.ww2Losuj;'
              'for(var i=l.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),x=l[i];l[i]=l[j];l[j]=x;}'
              'l.forEach(function(e,k){e.hidden=k>=n;if(k<n)u.appendChild(e);});})();</script>')
    return (f'<ul class="ww2-siatka ww2-siatka-mala ww2-inne" data-ww2-losuj="{ile}">{li}</ul>'
            f'<p class="ww2-inne-wszystkie"><a href="index.html#sylwetki">Wszystkie sylwetki →</a></p>{skrypt}')

# 18.11 (17:52): pole „Lata” z CMS — jedna data = rok urodzenia, dwie = lata życia.
# Redaktor może wpisać „1956”, „ur. 1956”, „1956-2020”, „1956 - 2020”, „1956–2020”.
def parsuj_lata(s):
    s = (s or '').strip()
    m = re.fullmatch(r'(?:ur\.?\s*)?(\d{4})\s*(?:[-–—]\s*(\d{4}))?', s)
    if not m:
        return None
    if m.group(2):
        return (f'{m.group(1)}–{m.group(2)}', f'{m.group(1)}–{m.group(2)}', 'lata życia')
    return (f'ur. {m.group(1)}', m.group(1), 'rok urodzenia')

for _w in WPISY:
    if _w.get('typ') == 'osoba':
        _p = parsuj_lata(_w.get('lata'))
        _w['lata_stat'] = (_p[1], _p[2]) if _p else None
        if _p:
            _w['lata'] = _p[0]
        # W skrócie: bez dublowania lat życia (pokazujemy je raz, jako pierwszą liczbę)
        if _w.get('skrot'):
            _w['skrot'] = [(x, y) for x, y in _w['skrot']
                           if y.strip().lower() not in ('lata życia', 'rok urodzenia') and not (_p and x.strip() == _p[1])]

def zrodla_licz(n):
    if n == 1: return '1 źródło'
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14): return f'{n} źródła'
    return f'{n} źródeł'

def osoba(i):
    return PO_ID.get(i)

def linkuje(w, i):
    t = (w.get('tresc') or '') + (w.get('tresc_md') or '')
    return f'/instytut/warto-wiedziec/{i}' in t or f'w-{i}.html' in t

def wpisy_z_osoba(i, z_osobami=False):
    # wpisy „Warto wiedzieć”, które wskazują tę osobę: link w treści, pole osoby albo laureat
    out = []
    for w in WPISY:
        if w['id'] == i or (w.get('typ') == 'osoba' and not z_osobami):
            continue
        if linkuje(w, i) or i in (w.get('osoby') or []) or any(len(l) > 4 and l[4] == i for l in (w.get('laureaci') or [])):
            out.append(w)
    return out

# ------------------------------------------------------------------ wspólne przeróbki HTML
def mapuj(url):
    if not url.startswith('/Web-Podglad/'):
        return url
    rest = url[len('/Web-Podglad/'):]
    if rest.startswith(('_astro/', 'pliki/', 'favicon.svg', 'grafiki/')):
        assets.add(rest.split('#')[0].split('?')[0])
        return './' + rest
    base = rest.split('#')[0].rstrip('/')
    hash_ = ('#' + rest.split('#', 1)[1]) if '#' in rest else ''
    if base == '':
        return 'glowna.html' + hash_
    if base == 'warto-wiedziec':
        return 'index.html' + hash_
    return LIVE + '/' + rest

def przerob(h):
    h = re.sub(r'<script type="speculationrules">[\s\S]*?</script>', '', h)
    # prototyp: bez wariantów zdjęć (avif/webp/rozmiary) — zostaje samo src
    h = re.sub(r'<source [^>]*>', '', h)
    h = re.sub(r'\s(srcset|sizes)="[^"]*"', '', h)
    # srcset: wiele adresów
    def srcset(m):
        czesci = []
        for c in m.group(2).split(','):
            c = c.strip()
            if not c:
                continue
            u, *reszta = c.split(' ')
            czesci.append(' '.join([mapuj(u)] + reszta))
        return f'{m.group(1)}="{", ".join(czesci)}"'
    h = re.sub(r'(srcset)="([^"]*)"', srcset, h)
    h = re.sub(r'(href|src)="(/Web-Podglad/[^"]*)"', lambda m: f'{m.group(1)}="{mapuj(m.group(2))}"', h)
    def url_styl(m):
        u = mapuj(m.group(1))
        if u.startswith('./pliki/'):
            styl_url.add(u[2:])
        return f'url({u})'
    h = re.sub(r'url\((/Web-Podglad/[^)]*)\)', url_styl, h)
    h = re.sub(r'(?<!github\.io)/Web-Podglad/', LIVE + '/', h)  # resztki (np. w JSON-ach) — na żywą stronę
    # Menu Instytutu: „Warto wiedzieć” w grupie „Więcej”
    h = re.sub(r'(<h3>Więcej</h3>\s*<ul>)(<li><a href="' + re.escape(LIVE) + r'/instytut/infrastruktura-informatyczna">)',
               r'\1<li><a href="index.html">Warto wiedzieć</a></li>\2', h)
    # dodatki prototypu
    h = h.replace('</head>', PROTO_HEAD + '</head>', 1)
    h = h.replace('</body>', PROTO_BAR + '</body>', 1)
    return h

PROTO_HEAD = '''<link rel="stylesheet" href="./ww2.css">'''
PROTO_BAR = '''<nav class="ww2-proto" aria-label="Prototyp"><b>Prototyp · Warto wiedzieć</b>
<a href="index.html" data-p="lista">Lista</a><a href="w-stypendium-steinhausa.html" data-p="wpis">Wpis z laureatami</a><a href="w-nowa-ksiega-szkocka.html" data-p="wpis2">Zwykły wpis</a><a href="glowna.html#szybki-dostep" data-p="glowna">Strona główna</a>
<button type="button" data-ww2-losuj hidden>Losuj ponownie ↻</button><button type="button" class="ww2-x" aria-label="Schowaj pasek prototypu" data-ww2-x>✕</button></nav>
<script>(function(){var b=document.querySelector('[data-ww2-losuj]');if(window.ww2Losuj){b.hidden=false;b.onclick=window.ww2Losuj}document.querySelector('[data-ww2-x]').onclick=function(){this.parentNode.hidden=true};var p=location.pathname.split('/').pop()||'index.html';document.querySelectorAll('.ww2-proto a').forEach(function(a){if(a.getAttribute('href').split('#')[0]===p)a.setAttribute('aria-current','page')});})();</script>'''

# ------------------------------------------------------------------ markdown
# 18:29: blok :::pliki (jawny Markdown, jak w Studiach) w treści sylwetki, np. sekcja „Do pobrania”
IKONA_PLIKU = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ikona_pdf.svg')).read()
def bloki_pliki(tekst):
    def zamien(m):
        lis = []
        for l in m.group(1).splitlines():
            mm = re.match(r'\s*-\s*\[([^\]]+)\]\(([^)\s]+)\)\s*(?:[—–-]\s*(.+))?$', l)
            if not mm:
                continue
            tyt, url, opis = mm.group(1), mm.group(2), (mm.group(3) or '').strip()
            if url.startswith('/'):
                url = LIVE + url
            typ = (url.rsplit('.', 1)[-1].split('?')[0].upper() if '.' in url.rsplit('/', 1)[-1] else 'LINK')
            lis.append(f'<li><a href="{url}">{IKONA_PLIKU}<span><span class="ww2-pl-t">{esc(tyt)}</span>' + (f'<small>{esc(opis)}</small>' if opis else '')
                       + f'</span><span class="typ">{esc(typ)}</span></a></li>')
        return '\n\n<ul class="pliki">' + ''.join(lis) + '</ul>\n\n'
    return re.sub(r'(?m)^:::pliki\s*\n(.*?)\n:::\s*$', zamien, tekst, flags=re.S)

def md_inline(tekst):
    # 18:01: w podpisach „W skrócie” wolno linkować (np. Mathematics Genealogy Project)
    return re.sub(r'^<p>|</p>$', '', md(tekst).strip())

def md(tekst):
    out = markdown.markdown(tekst, extensions=['extra'])
    def link(m):
        u = m.group(1)
        mm = re.match(r'/instytut/warto-wiedziec/([a-z0-9-]+)/?(#.*)?$', u)
        if mm:
            return f'<a href="{strona_wpisu(mm.group(1))}{mm.group(2) or ""}">'
        if u.startswith('/'):
            u = LIVE + u
        zew = u.startswith('http') and not u.startswith(LIVE)
        return f'<a href="{u}"' + (' class="zew"' if zew else '') + '>'
    out = re.sub(r'<a href="([^"]*)">', link, out)
    out = re.sub(r'(<a [^>]*class="zew"[^>]*>)(.*?)</a>', r'\1\2<span class="sr-only"> (inna strona)</span></a>', out)
    return out

def esc(s):
    return html.escape(s, quote=True)

def rok_napis(w):
    return str(w['rok']) if w['rok'] else '—'

def obraz_min(w):
    if w.get('typ') == 'osoba':
        return f'<span class="ww-min ww2-min-os" aria-hidden="true" data-astro-cid-kbldtwja>{portret(w)}</span>'
    if not w.get('obraz'):
        return ''
    return (f'<span class="ww-min" aria-hidden="true" data-astro-cid-kbldtwja><img src="./pliki/ww/{w["obraz"]}-min.jpg" alt="" '
            f'width="160" height="120" decoding="async"></span>')

def nowy(w):
    d = w.get('dodano') or (max(l[3] for l in w['laureaci']) if w.get('laureaci') else None)
    if w.get('dodano') and w.get('laureaci'):
        d = max(w['dodano'], max(l[3] for l in w['laureaci']))
    if not d:
        return None
    dd = date.fromisoformat(d)
    return d if (DZIS - dd).days <= 30 else None

def rocznica_teraz(w):
    r = w.get('rocznica')
    rok = w.get('rocznica_rok') or w['rok']
    if not r or not rok:
        return None
    m, d = map(int, r.split('-'))
    dz = date(DZIS.year, m, d)
    if abs((dz - DZIS).days) <= 7:
        return DZIS.year - rok
    return None

MIES = ['', 'stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia']

def oznaczenia(w, z_grupa=False):
    o = []
    if z_grupa:
        o.append(f'<span class="ww2-gr">{GRUPA[w["grupa"]]}</span>')
    if w.get('typ') == 'osoba' and z_grupa:
        o.append(f'<span>{esc(w["lata"])}</span>')
    if w.get('laureaci') and w.get('lista_tytul', '').startswith('Laureaci'):
        n = len(w['laureaci'])
        o.append(f'<span>{n} {"laureat" if n == 1 else ("laureaci" if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else "laureatów")} z Instytutu</span>')
    if nowy(w):
        o.append('<span class="ww2-nowe">' + ('Nowy laureat' if not w.get('dodano') and w.get('laureaci') else 'Nowe') + '</span>')
    lat = rocznica_teraz(w)
    if lat:
        m, d = map(int, w['rocznica'].split('-'))
        o.append(f'<span class="ww2-roczn">{lat}. {"urodziny" if w.get("rocznica_typ") == "urodziny" else "rocznica"} · {d} {MIES[m]}</span>')
    return ('<p class="ww2-oz">' + ''.join(o) + '</p>') if o else ''

def pozycja(w, z_grupa=False):
    klasy = 'ww-w ww-klik' + (' ww-z-min' if (w.get('obraz') or w.get('typ') == 'osoba') else '') + (' ww2-bez-roku' if w['grupa'] == 'nagrody' else '')
    return (f'<li class="{klasy}" data-ww-poz data-grupa="{w["grupa"]}" data-szukaj="{esc((w["tytul"] + " " + w["zajawka"]).lower())}" data-astro-cid-kbldtwja>'
            + (f'<span class="ww-rok" data-astro-cid-kbldtwja>{rok_napis(w)}</span>' if w['grupa'] != 'nagrody' else '') +
            f'<div class="ww-tr" data-astro-cid-kbldtwja><p class="t" data-astro-cid-kbldtwja><a href="{strona_wpisu(w["id"])}" data-astro-cid-kbldtwja="true">{esc(w["tytul"])}</a></p>'
            f'<p class="x" data-astro-cid-kbldtwja>{esc(w["zajawka"])}</p>{oznaczenia(w, z_grupa)}</div>{obraz_min(w)}</li>')

def sortuj(lista):
    return sorted(lista, key=lambda w: (w['rok'] is None, w['rok'] or 0, w.get('kolejnosc', 0), w.get('sort', 0), w['tytul']))

# ------------------------------------------------------------------ lista
# 18.11 (18:20): „Historie” jako pozioma oś czasu. Najechanie, fokus albo stuknięcie punktu
# pokazuje wydarzenie w panelu pod osią; kliknięcie punktu (albo „Czytaj”) otwiera wpis.
def os_historii(g, n):
    ws = sorted([w for w in WPISY if w['grupa'] == g and w['rok']], key=lambda w: (w['rok'], w['tytul']))
    if not ws:
        return ''
    od = ws[0]['rok'] // 10 * 10
    do = (ws[-1]['rok'] // 10 + 1) * 10
    poz = lambda r: 3 + (r - od) / (do - od) * 94
    dek = ''.join(f'<span class="ww2-ol-dek{" ww2-ol-dek-n" if (d // 10) % 2 else ""}" style="left:{poz(d):.2f}%">{d}</span>'
                  for d in range(od, do + 1, 10))
    pkt, karty = [], []
    for i, w in enumerate(ws):
        url = strona_wpisu(w['id'])
        roc = w.get('rocznica') or ''
        pkt.append(f'<a class="ww2-ol-pkt" href="{url}" style="left:{poz(w["rok"]):.2f}%" data-i="{i}" data-rok="{w["rok"]}"'
                   f'{f" data-rocznica={chr(34)}{roc}{chr(34)}" if roc else ""} aria-label="{w["rok"]}: {esc(w["tytul"])}">'
                   f'<span class="ww2-ol-r">{w["rok"]}</span></a>')
        karty.append(f'<article class="ww2-ol-karta" data-i="{i}"><p class="ww2-ol-rok">{w["rok"]}</p><div>'
                     f'<h3><a href="{url}">{esc(w["tytul"])}</a></h3><p>{esc(w["zajawka"])}</p>'
                     f'<a class="ww2-ol-czytaj" href="{url}">Czytaj <span aria-hidden="true">→</span></a></div></article>')
    return (f'<section id="{g}" aria-labelledby="{g}-h" data-ww2-sekcja><h2 id="{g}-h">{n}</h2>'
            f'<p class="ww2-sek-opis">Wydarzenia i odkrycia od {ws[0]["rok"]} roku. Najedź na punkt na osi albo go wybierz.</p>'
            f'<div class="ww2-ol" data-ww2-ol><div class="ww2-ol-tor"><div class="ww2-ol-linia" aria-hidden="true"></div>'
            f'<div aria-hidden="true">{dek}</div>{"".join(pkt)}</div>'
            f'<div class="ww2-ol-panel"><div class="ww2-ol-karty" aria-live="polite">{"".join(karty)}</div>'
            f'<div class="ww2-ol-nav"><button type="button" data-ww2-ol-kier="-1" aria-label="Poprzednie wydarzenie">‹</button>'
            f'<span data-ww2-ol-licz>1 / {len(ws)}</span>'
            f'<button type="button" data-ww2-ol-kier="1" aria-label="Następne wydarzenie">›</button></div></div></div>'
            f'<script>{OS_JS}</script></section>')

OS_JS = r"""(function(){var o=document.currentScript.parentNode.querySelector('[data-ww2-ol]');if(!o)return;o.classList.add('js');
var tor=o.querySelector('.ww2-ol-tor'),P=[].slice.call(o.querySelectorAll('.ww2-ol-pkt')),K=[].slice.call(o.querySelectorAll('.ww2-ol-karta')),L=o.querySelector('[data-ww2-ol-licz]'),cur=-1,typ='mouse';
function uloz(){var W=tor.clientWidth,pad=W*0.03,gap=Math.min(W<560?24:30,W/(P.length+1)),od=+P[0].dataset.rok,dek=Math.floor(od/10)*10,
 last=+P[P.length-1].dataset.rok,dk=(Math.floor(last/10)+1)*10,x=P.map(function(p){return pad+(+p.dataset.rok-dek)/(dk-dek)*(W-2*pad)});
 for(var it=0;it<80;it++){var ok=true;for(var i=1;i<x.length;i++){var d=gap-(x[i]-x[i-1]);if(d>0.5){ok=false;x[i-1]-=d/2;x[i]+=d/2}}
  x[0]=Math.max(x[0],pad);x[x.length-1]=Math.min(x[x.length-1],W-pad);if(ok)break;}
 P.forEach(function(p,i){p.style.left=x[i]+'px'});}
function pokaz(i){if(i<0)i=P.length-1;if(i>=P.length)i=0;cur=i;P.forEach(function(p,j){p.classList.toggle('on',j===i);p.setAttribute('aria-current',j===i?'true':'false')});
 K.forEach(function(k,j){k.classList.toggle('on',j===i)});L.textContent=(i+1)+' / '+P.length;}
P.forEach(function(p,i){p.addEventListener('pointerenter',function(e){if(e.pointerType==='mouse')pokaz(i)});
 p.addEventListener('pointerdown',function(e){typ=e.pointerType});
 p.addEventListener('focus',function(){pokaz(i)});
 p.addEventListener('click',function(e){if(typ!=='mouse'&&cur!==i){e.preventDefault();pokaz(i)}typ='mouse'});
 p.addEventListener('keydown',function(e){var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(d){e.preventDefault();var n=(i+d+P.length)%P.length;P[n].focus()}});});
o.querySelectorAll('[data-ww2-ol-kier]').forEach(function(b){b.addEventListener('click',function(){pokaz(cur+ +b.dataset.ww2OlKier)})});
var d=new Date(),start=0;P.forEach(function(p,i){var r=p.dataset.rocznica;if(!r)return;var t=new Date(d.getFullYear(),+r.slice(0,2)-1,+r.slice(3));if(Math.abs(t-d)<=7*864e5)start=i});
uloz();pokaz(start);addEventListener('resize',uloz);})();"""

def lista():
    h = czytaj('instytut/wladze/index.html')
    h = re.sub(r'<title>[^<]*</title>', '<title>Warto wiedzieć — Instytut Matematyczny UWr</title>', h, count=1)
    h = h.replace('<h1 data-pagefind-meta="title">Władze Instytutu</h1>', '<h1 data-pagefind-meta="title">Warto wiedzieć</h1>', 1)
    # 18:07: hasło i liczby w banerze, jak na stronach działów; liczby liczą się same z treści
    def odm(n, f1, f2, f5):
        return f1 if n == 1 else (f2 if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14) else f5)
    n_sylw = sum(1 for w in WPISY if w['grupa'] == 'sylwetki' and not w.get('tba'))
    # 18:12: zamiast liczby wyróżnień — doktorzy wypromowani przez bohaterów sylwetek,
    # suma liczb z punktów „W skrócie” o doktorach; zaokrąglona w dół do dziesiątek z „+”
    n_dr = 0
    for w in WPISY:
        if w.get('typ') == 'osoba' and not w.get('tba'):
            for x, y in (w.get('skrot') or []):
                if re.match(r'(wypromowanych )?doktorów', y.strip()) and x.strip().isdigit():
                    n_dr += int(x)
    n_dr_txt = f'{n_dr // 10 * 10}+' if n_dr >= 20 else str(n_dr)
    n_lat = date.today().year - 1945 - (0 if (date.today().month, date.today().day) >= (11, 15) else 1)
    liczby = (f'<div class="z-slot"><ul class="pt-liczby"> '
              f'<li><span class="n">{n_lat}</span>{odm(n_lat, "rok", "lata", "lat")} od pierwszego wykładu</li>'
              f'<li><span class="n">{n_sylw}</span>{odm(n_sylw, "sylwetka", "sylwetki", "sylwetek")}</li>'
              # 18:16: trzecia liczba stała — Colloquium Mathematicum (1947), Zastosowania Matematyki (1953),
              # Probability and Mathematical Statistics (1980)
              # 18:40: trzecia liczba: 4 rektorów UWr z Instytutu (Marczewski, Urbanik, Łukaszewicz, Duda)
              f'<li><span class="n">4</span>rektorów UWr</li> </ul></div>')
    i_h1 = h.index('<h1 data-pagefind-meta="title">')
    i_div = h.index('</div>', i_h1) + len('</div>')
    h = h[:i_div] + '<p class="z-haslo">Ludzie i historie wrocławskiej matematyki</p>' + liczby + h[i_div:]
    h = h.replace('<link rel="stylesheet" href="/Web-Podglad/_astro/index.B-NAW2Gn.css">', '<link rel="stylesheet" href="/Web-Podglad/_astro/index.B-NAW2Gn.css"><link rel="stylesheet" href="/Web-Podglad/_astro/index.kLbBXUOF.css">', 1)
    a = h.index('<div class="z-pd z-wladze" data-dzial="instytut">')
    b = h.index('</main>', a)
    spis_t = ''.join(f'<li><a href="#{g}">{n}</a></li>' for g, n in GRUPY)
    dekady = sorted({(w['rok'] // 10) * 10 for w in WPISY if w['rok'] and w['grupa'] != 'sylwetki'})
    bez = [w for w in WPISY if not w['rok'] and w['grupa'] not in ('nagrody', 'sylwetki')]
    nagr = sortuj([w for w in WPISY if w['grupa'] == 'nagrody'])
    spis_o = '<li><a href="#lata-sylwetki">Sylwetki</a></li>' + ''.join(f'<li><a href="#lata-{d}">{d}–{d + 9}</a></li>' for d in dekady) + ('<li><a href="#lata-bez">Bez daty</a></li>' if bez else '') + ('<li><a href="#lata-nagrody">Nagrody i wyróżnienia</a></li>' if nagr else '')
    def sekcja(g, n):
        lista = sortuj([w for w in WPISY if w['grupa'] == g])
        if g == 'historie':
            return os_historii(g, n)
        if g == 'sylwetki':
            lista = sorted(lista, key=lambda w: w.get('sort', 0))
            karty = ''.join(
                f'<li data-ww-poz data-szukaj="{esc((w["tytul"] + " " + w["zajawka"]).lower())}"><a href="{strona_wpisu(w["id"])}">{portret(w)}'
                f'<b>{esc(w["tytul"])}</b><small>{esc(w["lata"])}</small><span>{esc(w["podpis"])}</span>'
                + ('<i class="ww2-nowe-k">Nowe</i>' if nowy(w) else '') + ('<i class="ww2-tba-k">TBA</i>' if w.get('tba') else '') + '</a></li>' for w in lista)
            return (f'<section id="{g}" aria-labelledby="{g}-h" data-ww2-sekcja><h2 id="{g}-h">{n}</h2>'
                    f'<p class="ww2-sek-opis">Ludzie, którzy zbudowali Instytut i jego pozycję. Każda sylwetka łączy się z historiami i wyróżnieniami z tej strony.</p>'
                    f'<ul class="ww2-siatka">{karty}</ul></section>')
        return (f'<section id="{g}" aria-labelledby="{g}-h" data-ww2-sekcja><h2 id="{g}-h">{n}</h2><ul class="ww-lista" data-astro-cid-kbldtwja>'
                + ''.join(pozycja(w) for w in lista) + '</ul></section>')
    tematy = ''.join(sekcja(g, n) for g, n in GRUPY)
    sylw_os = sekcja('sylwetki', 'Sylwetki').replace('id="sylwetki"', 'id="lata-sylwetki"').replace('id="sylwetki-h"', 'id="lata-sylwetki-h"').replace('aria-labelledby="sylwetki-h"', 'aria-labelledby="lata-sylwetki-h"')
    os_czasu = sylw_os + ''.join(
        f'<section id="lata-{d}" aria-labelledby="lata-{d}-h" data-ww2-sekcja><h2 id="lata-{d}-h">{d}–{d + 9}</h2><ul class="ww-lista" data-astro-cid-kbldtwja>'
        + ''.join(pozycja(w, True) for w in sortuj([w for w in WPISY if w['rok'] and w['grupa'] != 'sylwetki' and w['rok'] // 10 * 10 == d])) + '</ul></section>'
        for d in dekady)
    if nagr:
        os_czasu += ('<section id="lata-nagrody" aria-labelledby="lata-nagrody-h" data-ww2-sekcja><h2 id="lata-nagrody-h">Nagrody i wyróżnienia</h2><ul class="ww-lista" data-astro-cid-kbldtwja>'
                     + ''.join(pozycja(w) for w in nagr) + '</ul></section>')
    if bez:
        os_czasu += ('<section id="lata-bez" aria-labelledby="lata-bez-h" data-ww2-sekcja><h2 id="lata-bez-h">Bez daty</h2><ul class="ww-lista" data-astro-cid-kbldtwja>'
                     + ''.join(pozycja(w, True) for w in sortuj(bez)) + '</ul></section>')
    tresc = f'''<div class="z-pd z-ww2" data-dzial="instytut"> <nav class="z-spis" aria-labelledby="z-spis-h" data-pagefind-ignore data-z-spis><p class="z-spis-h" id="z-spis-h">Na tej stronie</p><button type="button" class="z-spis-przelacz" aria-expanded="false" aria-controls="z-spis-lista">Na tej stronie<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2"/></svg></button><ul class="z-spis-lista" id="z-spis-lista">{spis_t}<li class="z-spis-znacznik" aria-hidden="true"></li></ul></nav><script type="module" src="/Web-Podglad/_astro/SpisStrony.astro_astro_type_script_index_0_lang.BhkDecS6.js"></script>
<div class="z-pd-tresc">
<p class="wst ww2-wst">Ludzie i historie, z których wyrosła wrocławska matematyka: założyciele i profesorowie, ważne odkrycia i wyróżnienia, z których jesteśmy dumni. Bieżące sukcesy znajdziesz w <a href="{LIVE}/aktualnosci">Aktualnościach</a>.</p>
{tematy}
</div>
</div> '''
    h = h[:a] + tresc + h[b:]
    # „Następna strona w dziale” — po Warto wiedzieć: Infrastruktura informatyczna
    h = re.sub(r'<div class="z-nast"[\s\S]*?</div>', '', h, 1)
    return przerob(h)

LISTA_JS = r'''(function(){
var panele=document.querySelectorAll('[data-ww2-panel]'),przyc=document.querySelectorAll('[data-ww2-widok]'),q=document.querySelector('[data-ww2-szukaj]'),pusto=document.querySelector('[data-ww2-pusto]');
var W='tematy';try{W=sessionStorage.getItem('ww2-widok')||W}catch(e){}
if(location.hash.indexOf('#lata-')===0)W='os';
function filtr(){var t=(q.value||'').trim().toLowerCase(),ile=0;
 panele.forEach(function(p){if(p.hidden)return;p.querySelectorAll('[data-ww2-sekcja]').forEach(function(s){var n=0;s.querySelectorAll('[data-ww-poz]').forEach(function(li){var ok=!t||li.dataset.szukaj.indexOf(t)>=0;li.hidden=!ok;if(ok)n++});s.hidden=!n;ile+=n})});
 pusto.hidden=ile>0;document.dispatchEvent(new Event('z-spis'));}
function pokaz(w){W=w;panele.forEach(function(p){p.hidden=p.dataset.ww2Panel!==w});przyc.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.ww2Widok===w))});try{sessionStorage.setItem('ww2-widok',w)}catch(e){}filtr();}
przyc.forEach(function(b){b.addEventListener('click',function(){pokaz(b.dataset.ww2Widok)})});
q.addEventListener('input',filtr);pokaz(W);
})();'''

# ------------------------------------------------------------------ wpis
def wpis(w, kolejne):
    h = czytaj('warto-wiedziec/wyklad-terencea-tao/index.html')
    h = re.sub(r'<title>[^<]*</title>', f'<title>{esc(w["tytul"])} — Warto wiedzieć — Instytut Matematyczny UWr</title>', h, 1)
    h = re.sub(r'<h1 data-pagefind-meta="title">[^<]*</h1>', f'<h1 data-pagefind-meta="title">{esc(w["tytul"])}</h1>', h, 1)
    a = h.index('<div class="z-pd-tresc tresc">')
    b = h.index('</section> </div>', h.index('id="zobacz-tez"')) + len('</section> </div>')
    meta = f'{rok_napis(w) + " · " if w["rok"] else ""}<a href="index.html#{w["grupa"]}" data-astro-cid-asq2klna>{GRUPA[w["grupa"]]}</a>'
    fig = ''
    if w.get('obraz'):
        p = os.path.join(OUT, 'pliki/ww', w['obraz'] + '.jpg')
        sz = Image.open(p).size
        if sz[0] >= 560:
            fig = (f'<figure class="ww-foto" data-astro-cid-asq2klna><img src="./pliki/ww/{w["obraz"]}.jpg" alt="{esc(w.get("obraz_opis", ""))}" width="{sz[0]}" height="{sz[1]}">'
                   f'<figcaption data-astro-cid-asq2klna>{esc(w.get("obraz_opis", ""))}</figcaption></figure>')
    lista_l = ''
    ludzie = [osoba(i) for i in (w.get('osoby') or [])] + [osoba(l[4]) for l in (w.get('laureaci') or []) if len(l) > 4 and l[4]]
    ludzie = [o for o in ludzie if o]
    blok_ludzie = ''
    if ludzie:
        tyt_l = 'Sylwetki laureatów' if w.get('laureaci') else 'Ludzie w tej historii'
        blok_ludzie = (f'<section id="ludzie" aria-labelledby="ludzie-h" class="ww2-ludzie-sek" data-astro-cid-asq2klna><h2 id="ludzie-h" data-astro-cid-asq2klna>{tyt_l}</h2><ul class="ww2-ludzie">'
                       + ''.join(f'<li><a href="{strona_wpisu(o["id"])}">{portret(o)}<span><b>{esc(o["tytul"])}</b><small>{esc(o["lata"])}</small><i>Sylwetka →</i></span></a></li>' for o in ludzie)
                       + '</ul></section>')
    if w.get('laureaci'):
        def kto_html(l):
            o = osoba(l[4]) if len(l) > 4 and l[4] else None
            if o:
                return f'<span class="ww2-l-kto"><a href="{strona_wpisu(o["id"])}" class="ww2-l-os">{portret(o, "ww2-mini")}{esc(l[1])}</a></span>'
            return f'<span class="ww2-l-kto">{esc(l[1])}</span>'
        wiersze = ''.join(
            f'<li><span class="ww2-l-rok">{l[0]}</span>{kto_html(l)}<a href="{LIVE}/aktualnosci/{l[2]}">aktualność<span class="sr-only">: {esc(l[1])}</span> →</a></li>'
            for l in w['laureaci'])
        lista_l = (f'<section id="laureaci" aria-labelledby="laureaci-h" class="ww2-laur" data-astro-cid-asq2klna><h2 id="laureaci-h" data-astro-cid-asq2klna>{w["lista_tytul"]}</h2>'
                   f'<ul class="ww2-l">{wiersze}</ul>'
                   '<p class="ww2-uwaga"><b>Prototyp:</b> lista to blok <code>:::laureaci</code> w Markdownie tego wpisu — redaktor po nowej aktualności dopisuje na górze jedną linijkę, np. <code>- 2026 Dominik Gdesz</code>. Nazwisko jako link do sylwetki dostaje portret, a licznik „N laureatów” na liście strona liczy sama.</p></section>')
    akcja = ''
    if w.get('link'):
        akcja = f'<p class="akcja glowny" data-astro-cid-asq2klna><a href="{w["link"]}" class="przycisk glowny zew" data-astro-cid-asq2klna="true">{esc(w["link_etykieta"])}<span class="sr-only"> (inna strona)</span></a></p>'
    zob = ''.join(f'<li data-astro-cid-kbldtwja><a href="{strona_wpisu(k["id"])}" data-astro-cid-kbldtwja="true">{esc(k["tytul"])}</a></li>' for k in kolejne)
    tresc = (f'<div class="z-pd-tresc tresc"> <section data-astro-cid-asq2klna> <p class="etyk ww-meta" data-astro-cid-asq2klna>{meta}</p>'
             f'<p class="wst" data-astro-cid-asq2klna>{esc(w["zajawka"])}</p>{fig}<div class="ww-tresc" data-astro-cid-asq2klna>{md(w["tresc"])}</div>{akcja}</section>'
             f'{blok_ludzie}{lista_l}<section id="zobacz-tez" aria-labelledby="zobacz-tez-h" data-pagefind-ignore data-astro-cid-asq2klna> <h2 id="zobacz-tez-h" data-astro-cid-asq2klna>Zobacz też w „{GRUPA[w["grupa"]]}”</h2> <ul class="linki" data-astro-cid-kbldtwja>{zob}</ul> </section> </div>')
    h = h[:a] + tresc + h[b:]
    return przerob(h)

# ------------------------------------------------------------------ sylwetka
def rok_liczba(r):
    m = re.search(r'\d{4}', r or '')
    return int(m.group(0)) if m else (1950 if '50' in (r or '') else 9999)

def ciekawostki(dzial):
    d = json.load(open(os.path.join(CIEK, dzial + '.json'), encoding='utf-8'))
    d = [c for c in d if not c.get('ukryta') and c.get('stan') != 'odpada']
    return sorted(d, key=lambda c: rok_liczba(c.get('rok')))

def strona_osoby_md(w):
    h = czytaj('instytut/wladze/index.html')
    h = re.sub(r'<title>[^<]*</title>', f'<title>{esc(w["tytul"])} — Sylwetki — Instytut Matematyczny UWr</title>', h, count=1)
    h = h.replace('<a href="/Web-Podglad/instytut">← Instytut</a>', '<a href="index.html#sylwetki">← Warto wiedzieć</a>', 1)
    h = h.replace('<h1 data-pagefind-meta="title">Władze Instytutu</h1>', f'<h1 data-pagefind-meta="title">{esc(w["tytul"])}</h1>', 1)
    i_h1 = h.index('<h1 data-pagefind-meta="title">')
    i_div = h.index('</div>', i_h1) + len('</div>')
    h = h[:i_div] + f'<p class="z-haslo">{esc(w["podpis"])}</p>' + h[i_div:]
    a = h.index('<div class="z-pd z-wladze" data-dzial="instytut">')
    b = h.index('</main>', a)
    # 17:56: lata życia pod zdjęciem (jak na karcie w siatce), nie jako liczba obok
    _sk = list(w['skrot'] or [])
    lata_html = f'<p class="ww2-prof-lata">{esc(w["lata"])}</p>' if w.get('lata') else ''
    skrot_html = ('<dl class="ww2-skrot">' + ''.join(f'<div><dt>{esc(x)}</dt><dd>{md_inline(y)}</dd></div>' for x, y in _sk) + '</dl>') if _sk else ''
    podp = ''  # 18:27: bez odręcznych podpisów patronów przy zdjęciu
    czesci = re.split(r'(?m)^## ', w['tresc_md'])
    wstep = czesci[0].strip()
    glowa = (f'<div class="ww2-prof"><div class="ww2-prof-l">{portret(w, "ww2-duzy")}{lata_html}{podp}</div><div class="ww2-prof-tr">'
             f'{skrot_html}</div></div>')
    sekcje, spis = [], []
    if w.get('tba'):
        sekcje.append('<div class="ww2-tba"><p class="ww2-tba-h">TBA</p><p>Sylwetka w przygotowaniu. Tekst dopisze redakcja.</p>'
                      '<p class="ww2-tba-proto"><b>Prototyp:</b> w CMS to sylwetka z pustą „Treścią” (Warto wiedzieć → Sylwetki). '
                      'Strona pokazuje wtedy imię, lata i portret albo monogram, a w spisie i na karcie znaczek „TBA”. '
                      'Taka sylwetka nie losuje się na stronie głównej. Wystarczy wpisać tekst i zapisać.</p></div>')
    if wstep:
        sekcje.append(f'<div class="z-proza tresc ww2-wstep"><div class="prose">{md(wstep)}</div></div>')
    def sek(id_, tyt, html_, klasa=''):
        spis.append(f'<li><a href="#{id_}">{tyt}</a></li>')
        sekcje.append(f'<section id="{id_}" aria-labelledby="{id_}-h" class="{klasa}"><h2 id="{id_}-h">{tyt}</h2>{html_}</section>')
    zrodla = ''
    for blok in czesci[1:]:
        linia, _, body = blok.partition('\n')
        mm = re.match(r'(.*?)\s*\{#([a-z0-9-]+)\}\s*$', linia.strip())
        tyt, id_ = (mm.group(1), mm.group(2)) if mm else (linia.strip(), re.sub(r'[^a-z0-9]+', '-', linia.lower()).strip('-'))
        if id_ == 'zrodla':
            zrodla = body
            continue
        sek(id_, esc(tyt), f'<div class="z-proza tresc"><div class="prose">{md(bloki_pliki(body))}</div></div>')
    pow_ = wpisy_z_osoba(w['id'])
    if pow_:
        sek('w-warto-wiedziec', 'W „Warto wiedzieć”', f'<ul class="ww-lista" data-astro-cid-kbldtwja>{"".join(pozycja(p, True) for p in sortuj(pow_))}</ul>')
    if w.get('zalozyciel'):
        dz = {'instytut': 'Instytut', 'nauka': 'Nauka', 'studia': 'Studia', 'popularyzacja': 'Popularyzacja'}[w['dzial']]
        zrodla_dz = f'<p class="ww2-patron">Patron działu <a href="{LIVE}/{w["dzial"]}">{dz}</a> na tej stronie.</p>'
    else:
        zrodla_dz = ''
    if zrodla:
        n = len(re.findall(r'(?m)^\s*(?:[-*]|\d+\.)\s+', zrodla))
        spis.append('<li><a href="#zrodla">Źródła</a></li>')
        sekcje.append(
            f'<section id="zrodla" aria-labelledby="zrodla-h" class="ww2-zrodla-sek"><details class="ww2-zrodla-d">'
            f'<summary><h2 id="zrodla-h">Źródła</h2><span class="ww2-zrodla-n">{zrodla_licz(n)} · rozwiń</span></summary>'
            f'{zrodla_dz}<div class="z-proza tresc ww2-zrodla"><div class="prose">{md(zrodla)}</div></div></details></section>'
            '<script>(function(){var d=document.querySelector(".ww2-zrodla-d");if(!d)return;'
            'function o(){if(location.hash==="#zrodla")d.open=true;}o();addEventListener("hashchange",o);'
            'document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest(\'a[href="#zrodla"]\');if(a)d.open=true;});'
            'd.addEventListener("toggle",function(){var s=d.querySelector(".ww2-zrodla-n");if(s)s.textContent=s.textContent.replace(/ · (rozwiń|zwiń)$/,d.open?" · zwiń":" · rozwiń");});})();</script>')
    sek('inne-sylwetki', 'Inne sylwetki', inne_sylwetki(w))
    tresc = (f'<div class="z-pd z-ww2 z-ww2-os" data-dzial="instytut"> <nav class="z-spis" aria-labelledby="z-spis-h" data-pagefind-ignore data-z-spis><p class="z-spis-h" id="z-spis-h">Na tej stronie</p>'
             f'<button type="button" class="z-spis-przelacz" aria-expanded="false" aria-controls="z-spis-lista">Na tej stronie</button><ul class="z-spis-lista" id="z-spis-lista">{"".join(spis)}<li class="z-spis-znacznik" aria-hidden="true"></li></ul></nav>'
             f'<script type="module" src="/Web-Podglad/_astro/SpisStrony.astro_astro_type_script_index_0_lang.BhkDecS6.js"></script>'
             f'<div class="z-pd-tresc">{glowa}{"".join(sekcje)}</div></div> ')
    h = h[:a] + tresc + h[b:]
    h = re.sub(r'<div class="z-nast"[\s\S]*?</div>', '', h, count=1)
    h = h.replace('<link rel="stylesheet" href="/Web-Podglad/_astro/index.B-NAW2Gn.css">', '<link rel="stylesheet" href="/Web-Podglad/_astro/index.B-NAW2Gn.css"><link rel="stylesheet" href="/Web-Podglad/_astro/index.kLbBXUOF.css">', 1)
    return przerob(h)

def strona_osoby(w):
    if w.get('md'):
        return strona_osoby_md(w)
    h = czytaj('instytut/wladze/index.html')
    h = re.sub(r'<title>[^<]*</title>', f'<title>{esc(w["tytul"])} — Sylwetki — Instytut Matematyczny UWr</title>', h, count=1)
    h = h.replace('<a href="/Web-Podglad/instytut">← Instytut</a>', '<a href="index.html#sylwetki">← Warto wiedzieć</a>', 1)
    h = h.replace('<h1 data-pagefind-meta="title">Władze Instytutu</h1>', f'<h1 data-pagefind-meta="title">{esc(w["tytul"])}</h1>', 1)
    i_h1 = h.index('<h1 data-pagefind-meta="title">')
    i_div = h.index('</div>', i_h1) + len('</div>')
    h = h[:i_div] + f'<p class="z-haslo">{esc(w["podpis"])}</p>' + h[i_div:]
    a = h.index('<div class="z-pd z-wladze" data-dzial="instytut">')
    b = h.index('</main>', a)
    zal = w.get('zalozyciel')
    # W skrócie
    if zal:
        skrot = [(w['lata'], 'lata życia')] + ([('Sala ' + w['sala'], 'sala wykładowa jego imienia')] if w['sala'] != 'B' else []) \
                + [('Patron', f'działu {w["dzial_nazwa"]} na tej stronie')] + w['skrot_extra']
    else:
        skrot = w['skrot']
    skrot_html = '<dl class="ww2-skrot">' + ''.join(f'<div><dt>{esc(x)}</dt><dd>{esc(y)}</dd></div>' for x, y in skrot) + '</dl>'
    podp = f'<span class="ww2-podpis-r" aria-hidden="true">{podpis_svg(w["dzial"])}</span>' if zal else ''
    glowa = (f'<div class="ww2-prof"><div class="ww2-prof-l">{portret(w, "ww2-duzy")}{podp}</div><div class="ww2-prof-tr">'
             f'<p class="etyk ww-meta"><a href="index.html#sylwetki">Sylwetki</a> · {esc(w["lata"])}</p>'
             f'<p class="wst">{esc(w["zajawka"])}</p>{skrot_html}</div></div>')
    sekcje, spis = [], []
    def sek(id_, tyt, html_):
        spis.append(f'<li><a href="#{id_}">{tyt}</a></li>')
        sekcje.append(f'<section id="{id_}" aria-labelledby="{id_}-h"><h2 id="{id_}-h">{tyt}</h2>{html_}</section>')
    if zal:
        cs = ciekawostki(w['dzial'])
        pierwsze, reszta = cs[:8], cs[8:]
        def oc(c):
            return f'<li><span class="etyk">{esc(c.get("rok", ""))}</span><p class="t">{esc(c["nazwa"])}</p><p>{esc(c["zdanie"])}</p></li>'
        html_ = '<div class="tresc"><ol class="etapy ww2-os">' + ''.join(oc(c) for c in pierwsze) + '</ol></div>'
        if reszta:
            html_ += (f'<details class="ww2-wiecej"><summary>Pokaż wszystkie ({len(cs)})</summary><div class="tresc"><ol class="etapy ww2-os">'
                      + ''.join(oc(c) for c in reszta) + '</ol></div></details>')
        html_ += f'<p class="ww2-uwaga"><b>Prototyp:</b> oś składa się sama z ciekawostek patrona (te same, które losują się w banerach działu {esc(w["dzial_nazwa"])}). Redaktor nic tu nie wpisuje.</p>'
        if w.get('tresc'):
            sek('o-nim', 'We Wrocławiu', f'<div class="z-proza tresc"><div class="prose">{md(w["tresc"])}</div></div>')
        sek('w-ciekawostkach', 'Życie w ciekawostkach', html_)
    else:
        os_html = '<div class="tresc"><ol class="etapy ww2-os">' + ''.join(
            f'<li><span class="etyk">{esc(r)}</span><p class="t">{esc(t)}</p>' + (f'<p>{esc(o)}</p>' if o else '') + '</li>' for r, t, o in w['os']) + '</ol></div>'
        sek('droga', 'Droga naukowa', os_html + '<p class="ww2-uwaga"><b>Prototyp:</b> oś to istniejący blok <code>:::etapy</code> (<code>1. **1973: doktorat w IM PAN** — opis</code>), a „W skrócie” u góry to nowy blok <code>:::w-skrocie</code> (<code>- **72** — publikacje naukowe</code>). Wszystko w jednym polu Treść.</p>')
        # sekcje z Markdownu (## …)
        for blok in re.split(r'(?m)^## ', w['tresc'])[1:]:
            tyt, _, body = blok.partition('\n')
            id_ = re.sub(r'[^a-z0-9]+', '-', tyt.lower().translate(str.maketrans('ąćęłńóśźż', 'acelnoszz'))).strip('-')
            sek(id_, tyt.strip(), f'<div class="z-proza tresc"><div class="prose">{md(body)}</div></div>')
    # powiązane wpisy (wyróżnienia i historie)
    pow_ = wpisy_z_osoba(w['id'])
    if pow_:
        lis = ''.join(pozycja(p) for p in sortuj(pow_))
        sek('w-warto-wiedziec', 'W „Warto wiedzieć”', f'<ul class="ww-lista" data-astro-cid-kbldtwja>{lis}</ul><p class="ww2-uwaga"><b>Prototyp:</b> lista składa się sama z wpisów, które w treści linkują do tej sylwetki. Bez dodatkowych pól w CMS.</p>')
    # materiały
    mat = []
    if w.get('nota'):
        mat.append(f'<li><a href="{w["nota"]}" class="zew">Nota biograficzna (PDF)<span class="sr-only"> (inna strona)</span></a></li>')
    if w.get('pracownik'):
        mat.append(f'<li><a href="{w["pracownik"]}" class="zew">Strona domowa<span class="sr-only"> (inna strona)</span></a></li>')
        mat.append(f'<li><a href="{LIVE}/pracownicy">Spis pracowników — {esc(w["zaklad"])}</a></li>')
    if zal:
        mat.append(f'<li><a href="{LIVE}/{w["dzial"]}">Dział {esc(w["dzial_nazwa"])} — patron {esc(w["tytul"].split()[-1].rstrip("i") if False else w["tytul"])}</a></li>')
    if mat:
        sek('materialy', 'Materiały', '<ul class="z-zob">' + ''.join(mat) + '</ul>')
    sek('inne-sylwetki', 'Inne sylwetki', inne_sylwetki(w))
    tresc = (f'<div class="z-pd z-ww2 z-ww2-os" data-dzial="instytut"> <nav class="z-spis" aria-labelledby="z-spis-h" data-pagefind-ignore data-z-spis><p class="z-spis-h" id="z-spis-h">Na tej stronie</p>'
             f'<button type="button" class="z-spis-przelacz" aria-expanded="false" aria-controls="z-spis-lista">Na tej stronie</button><ul class="z-spis-lista" id="z-spis-lista">{"".join(spis)}<li class="z-spis-znacznik" aria-hidden="true"></li></ul></nav>'
             f'<script type="module" src="/Web-Podglad/_astro/SpisStrony.astro_astro_type_script_index_0_lang.BhkDecS6.js"></script>'
             f'<div class="z-pd-tresc">{glowa}{"".join(sekcje)}</div></div> ')
    h = h[:a] + tresc + h[b:]
    h = re.sub(r'<div class="z-nast"[\s\S]*?</div>', '', h, count=1)
    h = h.replace('<link rel="stylesheet" href="/Web-Podglad/_astro/index.B-NAW2Gn.css">', '<link rel="stylesheet" href="/Web-Podglad/_astro/index.B-NAW2Gn.css"><link rel="stylesheet" href="/Web-Podglad/_astro/index.kLbBXUOF.css">', 1)
    return przerob(h)

# ------------------------------------------------------------------ strona główna
def glowna():
    h = czytaj('index.html')
    a = h.index('<div class="rzad" data-losuj="4">')
    b = h.index('</script>', a) + len('</script>')
    pozycje = []
    for w in sortuj(WPISY):
        # zasady z 18.11 (02:24): wpisy z listą laureatów nie losują się na głównej; bez miejsca „Nowy laureat”
        if w.get('laureaci') or w.get('tba'):
            continue
        attrs = [f'data-waga="{3 if w.get("stan") == "ulubiona" else 1}"']
        if w.get('stan') == 'zawsze':
            attrs.append('data-zawsze')
        rr = w.get('rocznica_rok') or w['rok']
        if w.get('rocznica') and rr:
            attrs.append(f'data-rocznica="{w["rocznica"]}" data-rok="{rr}" data-roczn-typ="{w.get("rocznica_typ", "")}"')
        if w.get('dodano') and (DZIS - date.fromisoformat(w['dodano'])).days <= 30:
            attrs.append(f'data-nowe="{w["dodano"]}" data-nowe-napis="Nowa sylwetka" ' if w.get('typ') == 'osoba' else f'data-nowe="{w["dodano"]}" data-nowe-napis="Nowe"')
        if w.get('typ') == 'osoba':
            lewa = f'<span class="ww2-twarz">{portret(w)}</span>'
            tyt = esc(w['tytul'])
        else:
            lewa = f'<span>{rok_napis(w) if w["rok"] else ""}</span>'
            tyt = esc(w['tytul'])
        pozycje.append(f'<a href="{strona_wpisu(w["id"])}" {" ".join(attrs)}>{lewa}<b class="t">{tyt}</b></a>')
    nowe = f'''<div class="rzad" data-losuj="4" data-ww2-rzad>{"".join(pozycje)}</div><script>{GLOWNA_JS}</script>'''
    h = h[:a] + nowe + h[b:]
    h = h.replace('<a href="/Web-Podglad/warto-wiedziec">Wszystkie →</a>', '<a href="index.html">Wszystkie →</a>')
    return przerob(h)

GLOWNA_JS = r'''(function(box){
var MIES=['','stycznia','lutego','marca','kwietnia','maja','czerwca','lipca','sierpnia','września','października','listopada','grudnia'];
function dzis(){var p=new Intl.DateTimeFormat('en-CA',{timeZone:'Europe/Warsaw'}).format(new Date());return new Date(p+'T12:00:00')}
function losuj(){
 var D=dzis(),el=[].slice.call(box.children),n=matchMedia('(min-width: 1024px)').matches?+box.dataset.losuj:3;
 el.forEach(function(e){var o=e.querySelector('.ww2-ozn');if(o)o.remove();e.hidden=true});
 var wyb=[],uzyte=new Set();
 function dodaj(e,napis){if(!e||uzyte.has(e)||wyb.length>=n)return;uzyte.add(e);wyb.push(e);if(napis){var i=document.createElement('i');i.className='ww2-ozn';i.textContent=napis;e.querySelector('.t').prepend(i)}}
 // 1. rocznica w tym tygodniu (±7 dni)
 el.filter(function(e){return e.dataset.rocznica}).forEach(function(e){var m=+e.dataset.rocznica.slice(0,2),d=+e.dataset.rocznica.slice(3),r=new Date(D.getFullYear(),m-1,d,12),roz=Math.round((r-D)/864e5);
  if(Math.abs(roz)<=7)dodaj(e,e.dataset.rocznTyp==='urodziny'?(D.getFullYear()-e.dataset.rok)+'. urodziny · '+d+' '+MIES[m]:(D.getFullYear()-e.dataset.rok)+' lat temu · '+d+' '+MIES[m])});
 // 2. zawsze
 el.filter(function(e){return e.hasAttribute('data-zawsze')}).forEach(function(e){dodaj(e)});
 // 3. najnowsza pozycja z ostatnich 30 dni
 var nowe=el.filter(function(e){return e.dataset.nowe&&(D-new Date(e.dataset.nowe+'T12:00:00'))/864e5<=30}).sort(function(a,b){return a.dataset.nowe<b.dataset.nowe?1:-1});
 if(nowe[0])dodaj(nowe[0],nowe[0].dataset.noweNapis);
 // 4. reszta: losowanie z wagami (ulubione ×3), bez powtórzeń
 var pula=el.filter(function(e){return !uzyte.has(e)});
 while(wyb.length<n&&pula.length){var s=pula.reduce(function(a,e){return a+ +e.dataset.waga},0),r=Math.random()*s,k=0;for(;k<pula.length-1;k++){r-=+pula[k].dataset.waga;if(r<0)break}
  var e=pula.splice(k,1)[0];dodaj(e,e.dataset.nowe?e.dataset.noweNapis:'')}
 wyb.forEach(function(e){e.hidden=false;box.appendChild(e)});
}
losuj();
window.ww2Losuj=losuj;
})(document.currentScript.previousElementSibling);'''

# ------------------------------------------------------------------ zasoby
def kopiuj_zasoby():
    kolejka = list(assets)
    widziane = set()
    while kolejka:
        r = kolejka.pop()
        if r in widziane:
            continue
        widziane.add(r)
        src = os.path.join(ZB, r)
        if not os.path.isfile(src):
            print('BRAK', r)
            continue
        dst = os.path.join(OUT, r)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if r.endswith('.js'):
            t = open(src, encoding='utf-8').read()
            for imp in re.findall(r'from"\./([^"]+)"|import"\./([^"]+)"', t):
                kolejka.append('_astro/' + (imp[0] or imp[1]))
            open(dst, 'w', encoding='utf-8').write(t)
        elif r.endswith('.css'):
            t = open(src, encoding='utf-8').read()
            t = t.replace('/Web-Podglad/_astro/', './').replace('/Web-Podglad/', '../')
            open(dst, 'w', encoding='utf-8').write(t)
        else:
            shutil.copyfile(src, dst)
    return widziane

def main():
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(lista())
    for g, _ in GRUPY:
        wg = sortuj([w for w in WPISY if w['grupa'] == g])
        for w in wg:
            if w.get('typ') == 'osoba':
                open(os.path.join(OUT, strona_wpisu(w['id'])), 'w', encoding='utf-8').write(strona_osoby(w))
                continue
            inne = [k for k in wg if k is not w][:4]
            open(os.path.join(OUT, strona_wpisu(w['id'])), 'w', encoding='utf-8').write(wpis(w, inne))
    open(os.path.join(OUT, 'glowna.html'), 'w', encoding='utf-8').write(glowna())
    shutil.copyfile(os.path.join(os.path.dirname(__file__), 'ww2.css'), os.path.join(OUT, 'ww2.css'))
    z = kopiuj_zasoby()
    for r in styl_url:
        d = os.path.join(OUT, '_astro', r); os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copyfile(os.path.join(OUT, r), d)
    print('url() w style:', sorted(styl_url))
    # serwer artefaktów rezerwuje nazwy zaczynające się od „_” — katalog _astro jako astro
    os.rename(os.path.join(OUT, '_astro'), os.path.join(OUT, 'astro'))
    for f in os.listdir(OUT):
        if f.endswith('.html'):
            p = os.path.join(OUT, f); t = open(p, encoding='utf-8').read().replace('./_astro/', './astro/')
            open(p, 'w', encoding='utf-8').write(t)
    print('stron:', 2 + len(WPISY), 'zasobów:', len(z))

main()
