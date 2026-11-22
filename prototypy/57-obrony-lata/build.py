#!/usr/bin/env python3
"""Prototyp: lista Obron doktorskich w układzie Konferencji/Sukcesów (lata jako sekcje, spis „Na tej stronie”),
z 4 przykładowymi nadchodzącymi obronami. Bazą jest zbudowana strona Podglądu (Web-Podglad, gałąź zbudowana)."""
import os, re, subprocess, shutil, html as H
from collections import OrderedDict

GIT = '/home/claude/im-uwr/web-podglad'
REF = 'FETCH_HEAD'
OUT = '/home/claude/proto-obrony/out'
SITE = 'https://im-uwr.github.io/Web-Podglad/'

def git_show(path):
    return subprocess.run(['git', '-C', GIT, 'show', f'{REF}:{path}'], capture_output=True).stdout

TREE = set(subprocess.run(['git', '-C', GIT, 'ls-tree', '-r', '--name-only', REF], capture_output=True, text=True).stdout.split())

s = git_show('obrony-doktorskie/index.html').decode()
k = git_show('nauka/konferencje/index.html').decode()

# ---------- wiersze obron z obecnej strony ----------
rows = re.findall(r'<article class="ww [^"]*" data-ww data-rodzaj="obrona".*?</article>', s, re.S)
lata = OrderedDict()
for r in rows:
    rok = re.search(r'datetime="(\d{4})', r).group(1)
    r = r.replace('<h3 class="ww-t"', '<h4 class="ww-t"').replace('</h3>', '</h4>')
    lata.setdefault(rok, []).append(r)

CID = 'data-astro-cid-765psfln'
def przyklad(dzien, mies, rok, dt, kiedy, kto, tytul, lang, prom):
    a = f' {CID}'
    return (f'<article class="ww ww-klik ww-zwarty" data-ww data-rodzaj="obrona" data-dzial="nauka"{a}> '
            f'<time class="ww-data" datetime="{dt}"{a}>{dzien}<small{a}>{mies} {rok}</small></time> '
            f'<div class="ww-tresc"{a}> <div class="ww-rodz"{a}>{kiedy}</div> '
            f'<h4 class="ww-t"{a}="true"><a href="#z-nadchodzace"{a}="true">{H.escape(kto)}</a></h4> '
            f'<p lang="{lang}"{a}>{H.escape(tytul)}</p> '
            f'<p class="ob-prom" data-astro-cid-3vkp6zug><strong data-astro-cid-3vkp6zug>Promotor:</strong> {H.escape(prom)}</p> </div> </article>')

nadchodzace_przyklady = [
    przyklad(3, 'gru', 2026, '2026-12-03', 'czw. 12:15 · sala WS, Instytut Matematyczny UWr', 'Anna Przykładowa',
             'Asymptotic behaviour of random walks in random environment', 'en', 'prof. dr hab. Jan Kowalski'),
    przyklad(15, 'gru', 2026, '2026-12-15', 'wt. 14:15 · sala HS, Instytut Matematyczny UWr', 'Piotr Testowy',
             'Przestrzenie Banacha funkcji ciągłych i ich własności izomorficzne', 'pl', 'dr hab. Maria Nowak'),
    przyklad(20, 'sty', 2027, '2027-01-20', 'śr. 10:15 · sala WS, Instytut Matematyczny UWr', 'Katarzyna Wzorcowa',
             'Nonlocal reaction–diffusion equations and pattern formation', 'en', 'prof. dr hab. Adam Zieliński'),
    przyklad(10, 'lut', 2027, '2027-02-10', 'śr. 13:00 · sala A, Instytut Matematyczny UWr', 'Tomasz Próbny',
             'Model theory of fields with operators and definable groups', 'en', 'prof. dr hab. Ewa Wiśniewska'),
]

nadchodzace = []  # przykłady usunięte 22.11 (decyzja właściciela)

def ile(n):
    if n == 1: w = 'obrona'
    elif n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14): w = 'obrony'
    else: w = 'obron'
    return f'{n} {w}'

C = 'data-astro-cid-r4mi3tpp'
spis = ''.join([f'<li><a href="#z-nadchodzace">Nadchodzące</a></li>'] + [f'<li><a href="#rok-{r}">{r}</a></li>' for r in lata]) + \
    '<li class="z-spis-znacznik" aria-hidden="true"></li>'
nav = re.search(r'<nav class="z-spis".*?</nav>', k, re.S).group(0)
nav = re.sub(r'<ul class="z-spis-lista" id="z-spis-lista">.*?</ul>', f'<ul class="z-spis-lista" id="z-spis-lista">{spis}</ul>', nav, flags=re.S)

wstep = re.search(r'<div class="lp-wstep"[^>]*>(.*?)</div>', s, re.S).group(1)
wstep = wstep.replace('<p>', '<p class="wst">', 1)

tresc = [f'<section>{wstep}</section>',
         f'<section id="z-nadchodzace" aria-labelledby="h-z-nadchodzace" class="ob-sek"> <h2 id="h-z-nadchodzace">Nadchodzące</h2>'
         + (''.join(nadchodzace) if nadchodzace else '<p class="pusto">Nie zapowiedziano jeszcze kolejnych obron.</p>') + '</section>',
         '<section id="z-odbyte" aria-labelledby="h-z-odbyte" class="ob-sek"> <h2 id="h-z-odbyte">Odbyte</h2>' +
         ''.join(f'<h3 id="rok-{r}" class="ob-rok">{r}<span class="sr-only">, </span> <small>{ile(len(l))}</small></h3>' + ''.join(l) for r, l in lata.items()) +
         '</section>']

spis_js = re.search(r'<script type="module" src="[^"]*SpisStrony[^"]*"></script>', s).group(0)
uklad_js = re.search(r'<script>\(function\(pd\)\{var tel=.*?</script>', k, re.S).group(0)
nowy = (f'<div class="z-pd" data-dzial="nauka"> {spis_js} {nav} <div class="z-pd-tresc tresc z-ob">' + ''.join(tresc) +
        f'</div> {uklad_js} </div>')

a = s.index('<div class="z-pd z-pd-pelna">')
b = s.index('</main>', a)
s = s[:a] + nowy + '  ' + s[b:]

# style prototypu: rok jak w Konferencjach (liczba obok roku), wiersze bez stylów .tresc
extra = '''<style>
  .z-ob .ob-sek h2 { margin-bottom: 0; }
  .z-ob h3.ob-rok small { margin-left: 8px; font-family: var(--f-text); font-size: 13px; font-weight: 600; color: var(--muted); }
  .z-ob h3.ob-rok { margin-bottom: 0; padding-bottom: 6px; border-bottom: 1px solid var(--line); }
  .z-ob .ww p { max-width: none; }
  .z-ob .pusto { margin: 10px 0 0; font-style: italic; color: var(--muted); }
  .z-ob .ob-przyklad { margin: 6px 0 0; font-size: 13px; font-style: italic; color: var(--muted); }
  .z-ob .ob-prom { margin: 2px 0 0; max-width: none; font-size: 13px; line-height: 1.5; color: var(--muted); }
  .z-ob .ob-prom strong { font-weight: 700; color: var(--ink); }
  .ww-t { font-size: 21px; }
</style>'''
s = s.replace('</head>', extra + '\n</head>', 1)

# bez nakładki Podglądu (stan budowy)
s = re.sub(r'<link rel="stylesheet" href="/Web-Podglad/podglad/[^"]*">', '', s)
s = re.sub(r'<script[^>]*src="/Web-Podglad/podglad/[^"]*"[^>]*></script>', '', s)
s = re.sub(r'<script type="module" src="/Web-Podglad/_astro/ListaObron[^"]*"></script>', '', s)

# ---------- zasoby: kopiowanie z drzewa i przepisanie adresów ----------
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
potrzebne = set()
ASSET = re.compile(r'/Web-Podglad/([^"\'\s),?#]+)')

def rel_html(m):
    p = m.group(1)
    if p in TREE and re.search(r'\.(css|js|jpg|jpeg|png|webp|avif|svg|woff2?|ttf|ico)$', p):
        potrzebne.add(p); return p
    return SITE + p
s = ASSET.sub(rel_html, s)
s = s.replace('href="/Web-Podglad/"', f'href="{SITE}"')
# srcset z wieloma plikami: zostaw jeden obraz (mniej plików)
open(os.path.join(OUT, 'index.html'), 'w').write(s)

done = set()
while potrzebne - done:
    p = sorted(potrzebne - done)[0]; done.add(p)
    data = git_show(p)
    dst = os.path.join(OUT, p); os.makedirs(os.path.dirname(dst), exist_ok=True)
    if p.endswith('.css'):
        t = data.decode()
        def rel_css(m):
            q = m.group(1)
            if 'KaTeX' in q: return 'data:,'
            if q in TREE:
                potrzebne.add(q); return os.path.relpath(q, os.path.dirname(p))
            return SITE + q
        t = re.sub(r'/Web-Podglad/([^"\'\s),?#]+)', rel_css, t)
        data = t.encode()
    elif p.endswith('.js'):
        t = data.decode()
        for q in re.findall(r'["\'](\./[^"\']+\.js)["\']', t):
            potrzebne.add(os.path.normpath(os.path.join(os.path.dirname(p), q)))
        t = re.sub(r'/Web-Podglad/([^"\'\s),?#]+)', lambda m: SITE + m.group(1), t)
        data = t.encode()
    open(dst, 'wb').write(data)

n = sum(len(f) for _, _, f in os.walk(OUT))
mb = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(OUT) for f in fs) / 1e6
print(f'{n} plików, {mb:.1f} MB; lata: {list(lata)}; wierszy: {sum(len(v) for v in lata.values())}')

# logo w zmiennej CSS (url() w style="--…") przeglądarka rozwiązuje względem arkusza w _astro/
if os.path.exists(os.path.join(OUT, 'pliki/uwr-logo.png')):
    os.makedirs(os.path.join(OUT, '_astro/pliki'), exist_ok=True)
    shutil.copy(os.path.join(OUT, 'pliki/uwr-logo.png'), os.path.join(OUT, '_astro/pliki/uwr-logo.png'))

# serwer artefaktów rezerwuje nazwy z „_” na początku: _astro → astro
os.rename(os.path.join(OUT, '_astro'), os.path.join(OUT, 'astro'))
for d, _, fs in os.walk(OUT):
    for f in fs:
        if f.endswith(('.html', '.css', '.js')):
            p = os.path.join(d, f); t = open(p, encoding='utf-8').read()
            t2 = t.replace('"_astro/', '"astro/').replace("'_astro/", "'astro/").replace('(_astro/', '(astro/').replace(' _astro/', ' astro/').replace(',_astro/', ',astro/')
            if t2 != t: open(p, 'w', encoding='utf-8').write(t2)
print('po zmianie nazwy:', sum(len(f) for _, _, f in os.walk(OUT)), 'plików')
