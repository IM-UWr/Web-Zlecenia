"""Kontrola prototypu: wszystkie sylwetki × szerokości. python3 sprawdz.py <baza-url>"""
import sys, asyncio, json
from playwright.async_api import async_playwright
OSOBY = ['wladyslaw-slebodzinski', 'hugo-steinhaus', 'bronislaw-knaster', 'edward-marczewski', 'witold-wolibner',
         'julian-perkal', 'stanislaw-hartman', 'czeslaw-ryll-nardzewski', 'kazimierz-urbanik', 'jan-mycielski',
         'andrzej-hulanicki', 'andrzej-krzywicki', 'roman-duda', 'wladyslaw-narkiewicz', 'marek-bozejko',
         'tomasz-rolski', 'piotr-biler', 'krzysztof-tabisz']
SZER = [1920, 1600, 1440, 1366, 1280, 1180, 1100, 1024, 900, 768, 560, 430, 390, 360]
JS = """() => {
 const n=document.querySelector('.z-nagl-pod'), z=n.querySelector('.z-znak'), h1=n.querySelector('h1'), hs=n.querySelector('.z-haslo'), ul=n.querySelector('.pt-liczby');
 const r=e=>e?e.getBoundingClientRect():null; const zr=r(z);
 function linie(e){const w=document.createTreeWalker(e,4);let t,rs=[];while(t=w.nextNode()){if(!t.nodeValue.trim())continue;const g=document.createRange();g.selectNodeContents(t);rs.push(...g.getClientRects())}return rs.filter(q=>q.width&&q.height)}
 const nach=(a,b)=>a.left<b.right&&b.left<a.right&&a.top<b.bottom&&b.top<a.bottom;
 const tel=matchMedia('(max-width: 1023px)').matches;
 const kol=e=>e?linie(e).some(q=>nach(q,zr)):false;
 const lis=ul?[...ul.children]:[];
 const pr=document.querySelector('.ww2-prof-l'), wst=document.querySelector('.ww2-wstep p, .ww2-tba');
 return {tel, brak:n.classList.contains('z-znak-brak'), ck:n.getAttribute('data-ck'), losuje:n.classList.contains('z-ck-losuje'), sciezek:z.children.length,
   znak:zr&&[Math.round(zr.left),Math.round(zr.top),Math.round(zr.width),Math.round(zr.height)],
   h1_znak:kol(h1), haslo_znak:kol(hs), liczby_znak:ul?linie(ul).some(q=>nach(q,zr)):false,
   h1_px:getComputedStyle(h1).fontSize, h1_linie:Math.round(h1.offsetHeight/parseFloat(getComputedStyle(h1).lineHeight)),
   ukryte:lis.filter(l=>l.getAttribute('aria-hidden')).length, bez_liczb:ul?ul.classList.contains('z-bez-liczb'):null,
   etykiety_linie: tel? lis.map(l=>{const t=[...l.childNodes].filter(x=>x.nodeType===3).map(x=>{const g=document.createRange();g.selectNodeContents(x);return new Set([...g.getClientRects()].map(q=>Math.round(q.top))).size});return t.reduce((a,b)=>a+b,0)}):null,
   portret: pr&&[Math.round(r(pr).width), Math.round(r(pr.querySelector('.ww2-portret')).top)], tekst_gora: wst&&Math.round(r(wst).top),
   przewija: document.documentElement.scrollWidth>innerWidth };
}"""
async def main():
    baza = sys.argv[1]
    wyniki, bledy = [], []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        for w in SZER:
            ctx = await b.new_context(viewport={'width': w, 'height': 900}, is_mobile=w < 500, has_touch=w < 500)
            for o in OSOBY:
                pg = await ctx.new_page()
                pg.on('console', lambda m, o=o, w=w: bledy.append(f'{o} {w} {m.type}: {m.text}') if m.type in ('error', 'warning') else None)
                pg.on('pageerror', lambda e, o=o, w=w: bledy.append(f'{o} {w} pageerror: {e}'))
                pg.on('requestfailed', lambda r, o=o, w=w: bledy.append(f'{o} {w} requestfailed: {r.url}'))
                pg.on('response', lambda r, o=o, w=w: bledy.append(f'{o} {w} HTTP {r.status}: {r.url}') if r.status >= 400 else None)
                await pg.goto(f'{baza}/{o}/index.html', wait_until='networkidle')
                await pg.wait_for_timeout(150)
                d = await pg.evaluate(JS); d.update(osoba=o, w=w); wyniki.append(d)
                await pg.close()
            await ctx.close()
        await b.close()
    zle = [d for d in wyniki if (not d['tel'] and (d['h1_znak'] or d['haslo_znak'] or d['liczby_znak'] or d['ukryte'] or d['bez_liczb'])) or d['losuje'] or d['przewija']]
    print('problemy (komputer: nachodzenie na figurkę, ukryte liczby; wszędzie: przewijanie w poziomie):')
    for d in zle: print(' ', json.dumps(d, ensure_ascii=False))
    print('telefon/tablet — tekst nad figurką (figurka w tle, jak na innych podstronach):')
    for d in wyniki:
        if d['tel'] and (d['h1_znak'] or d['haslo_znak']): print('  ', d['w'], d['osoba'], 'h1' if d['h1_znak'] else '', 'hasło' if d['haslo_znak'] else '')
    print('komputer: figurka schowana (z-znak-brak):', [(d['osoba'], d['w']) for d in wyniki if not d['tel'] and d['brak']])
    print('komputer: tytuł w więcej niż 1 linii:', [(d['osoba'], d['w'], d['h1_linie']) for d in wyniki if not d['tel'] and d['h1_linie'] != 1])
    print('komputer: stopnie tytułu:', sorted({(d['w'], d['h1_px']) for d in wyniki if not d['tel']}))
    print('h1 zmniejszony (komputer):', sorted({(d['osoba'], d['w'], d['h1_px'], d['h1_linie']) for d in wyniki if not d['tel'] and d['h1_px'] != max(x['h1_px'] for x in wyniki if x['w']==d['w'])}))
    print('etykiety na telefonie, linie:', {d['osoba']: d['etykiety_linie'] for d in wyniki if d['w']==390})
    print('portret/tekst (szer., góra portretu, góra tekstu) przy 1366/768/390:', {(d['osoba'][:10], d['w']): (d['portret'], d['tekst_gora']) for d in wyniki if d['w'] in (1366, 768, 390) and d['osoba'] in ('hugo-steinhaus','krzysztof-tabisz')})
    print('figurki (data-ck):', len({d['ck'] for d in wyniki}), 'różnych na', len(wyniki), 'wejść')
    print('błędy konsoli/sieci:', len(bledy)); [print('  ', l) for l in bledy[:20]]
asyncio.run(main())
