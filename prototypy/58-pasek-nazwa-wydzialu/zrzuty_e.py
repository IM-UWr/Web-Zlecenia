from playwright.sync_api import sync_playwright
from PIL import Image
import io
BASE='http://localhost:8765/Web-Core'
OUT='/home/claude/proto/img/'
TXT={'E':'Faculty of Math. & Comp. Sci.'}
JS='''(k)=>{ if(innerWidth<=519){ document.querySelectorAll('.hdr .brand-sub').forEach(s=>s.textContent=k); } }'''
zadania=[('E',w) for w in [421,430,440,480]]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for war,w in zadania:
        for path,suf,scroll,h in [('/en/instytut/','',0,118),('/en/aktualnosci/','-jasny',900,64)]:
            ctx=b.new_context(viewport={'width':w,'height':760}, device_scale_factor=2, reduced_motion='reduce')
            pg=ctx.new_page(); pg.goto(BASE+path, wait_until='load'); pg.evaluate('document.fonts.ready')
            pg.evaluate(JS, TXT[war])
            if scroll: pg.mouse.wheel(0,scroll); pg.wait_for_timeout(700)
            pg.wait_for_timeout(500)
            png=pg.screenshot(clip={'x':0,'y':0,'width':w,'height':h})
            Image.open(io.BytesIO(png)).convert('RGB').save(f'{OUT}{war}-{w}{suf}.webp','WEBP',quality=84,method=6)
            ctx.close()
    b.close()
print('ok')
