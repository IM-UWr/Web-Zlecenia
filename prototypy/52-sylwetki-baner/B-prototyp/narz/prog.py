"""Zapas miejsca między tytułem a figurką (px) dla każdej sylwetki przy szerokościach 1024–1920 (z JS)."""
import sys, asyncio, json
from playwright.async_api import async_playwright
OSOBY = ['wladyslaw-slebodzinski', 'hugo-steinhaus', 'bronislaw-knaster', 'edward-marczewski', 'witold-wolibner',
         'julian-perkal', 'stanislaw-hartman', 'czeslaw-ryll-nardzewski', 'kazimierz-urbanik', 'jan-mycielski',
         'andrzej-hulanicki', 'andrzej-krzywicki', 'roman-duda', 'wladyslaw-narkiewicz', 'marek-bozejko',
         'tomasz-rolski', 'piotr-biler', 'krzysztof-tabisz']
JS = """() => {const n=document.querySelector('.z-nagl-pod'),z=n.querySelector('.z-znak'),h1=n.querySelector('h1');
 n.classList.remove('z-znak-brak'); const zr=z.getBoundingClientRect(); const q=document.createRange(); q.selectNodeContents(h1);
 const w=q.getBoundingClientRect().width, l=h1.getBoundingClientRect().left;
 return {zapas: Math.round(zr.left-(l+w+40)), fs: getComputedStyle(h1).fontSize, w: Math.round(w), em: w/parseFloat(getComputedStyle(h1).fontSize)}}"""
async def main():
    baza = sys.argv[1]; szer = list(range(1024, 1921, 8)) + [1499, 1500]
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        for o in OSOBY:
            pg = await b.new_page(viewport={'width': 1024, 'height': 800})
            await pg.goto(f'{baza}/{o}/index.html', wait_until='networkidle')
            wyn = []
            for w in sorted(set(szer)):
                await pg.set_viewport_size({'width': w, 'height': 800}); await pg.wait_for_timeout(30)
                wyn.append((w, await pg.evaluate(JS)))
            mn = min(wyn, key=lambda x: x[1]['zapas'])
            out[o] = (mn[0], mn[1]['zapas'], round(wyn[0][1]['em'], 2))
            print(f'{o:26} min zapas {mn[1]["zapas"]:5} px przy {mn[0]} px; szer. tytułu {wyn[0][1]["em"]:.2f} em; przy 1024: {wyn[0][1]["zapas"]} px')
            await pg.close()
        await b.close()
asyncio.run(main())
