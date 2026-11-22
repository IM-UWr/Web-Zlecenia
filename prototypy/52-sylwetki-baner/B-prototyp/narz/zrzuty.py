"""Zrzuty stron sylwetek: python3 zrzuty.py <baza-url> <katalog-wyj> <prefiks> [osoby,...] [szer,...] [--ciemny-tylko-steinhaus]
Adres strony: <baza>/<id>/index.html (proto) albo <baza>/<id>/ (Podgląd)."""
import sys, asyncio, os
from playwright.async_api import async_playwright

OSOBY = ['hugo-steinhaus', 'marek-bozejko', 'czeslaw-ryll-nardzewski', 'krzysztof-tabisz']
SZER = {1920: 1200, 1366: 1000, 1024: 1000, 390: 1700}

async def main():
    baza, wyj, pref = sys.argv[1], sys.argv[2], sys.argv[3]
    osoby = sys.argv[4].split(',') if len(sys.argv) > 4 and sys.argv[4] else OSOBY
    szer = [int(x) for x in sys.argv[5].split(',')] if len(sys.argv) > 5 and sys.argv[5] else list(SZER)
    sufiks = sys.argv[6] if len(sys.argv) > 6 else '/'
    os.makedirs(wyj, exist_ok=True)
    bledy = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        for motyw in ['light', 'dark']:
            for w in szer:
                ctx = await b.new_context(viewport={'width': w, 'height': SZER.get(w, 1000)}, device_scale_factor=1,
                                          is_mobile=(w < 500), has_touch=(w < 500))
                await ctx.add_init_script(f"try{{localStorage.setItem('motyw','{motyw}')}}catch(e){{}}")
                for o in osoby:
                    if motyw == 'dark' and o != 'hugo-steinhaus':
                        continue
                    pg = await ctx.new_page()
                    pg.on('console', lambda m, o=o, w=w: bledy.append(f'{o} {w} {m.type}: {m.text}') if m.type in ('error', 'warning') else None)
                    pg.on('pageerror', lambda e, o=o, w=w: bledy.append(f'{o} {w} pageerror: {e}'))
                    pg.on('requestfailed', lambda r, o=o, w=w: bledy.append(f'{o} {w} requestfailed: {r.url}'))
                    await pg.goto(f'{baza}/{o}{sufiks}', wait_until='networkidle')
                    await pg.wait_for_timeout(500)
                    nazwa = f'{pref}-{o}-{w}{"-ciemny" if motyw == "dark" else ""}.png'
                    await pg.screenshot(path=os.path.join(wyj, nazwa))
                    await pg.close()
                await ctx.close()
        await b.close()
    for l in bledy:
        print(l)
asyncio.run(main())
