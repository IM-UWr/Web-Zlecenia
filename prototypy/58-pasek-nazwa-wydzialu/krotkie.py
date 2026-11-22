from playwright.sync_api import sync_playwright
BASE='http://localhost:8765/Web-Core'
kand=['Faculty of Mathematics and Computer Science','Faculty of Maths & CS','Faculty of Mathematics & CS','Fac. of Math. & Comp. Sci.','Faculty of Math & Computer Sci.','Mathematics & Computer Science','Faculty of Mathematics','Faculty of Mathematics and']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for w in [421,430]:
        pg=b.new_page(viewport={'width':w,'height':700}); pg.goto(BASE+'/en/instytut/'); pg.evaluate('document.fonts.ready')
        for k in kand:
            d=pg.evaluate('''(k)=>{const s=document.querySelector('.hdr .brand-sub'); s.textContent=k; const r=document.createRange(); r.selectNodeContents(s); const b=r.getBoundingClientRect(); return {r:b.right,w:b.width,t:document.querySelector('.hdr-tools').getBoundingClientRect().left}}''',k)
            print(w, f"{k:45} szer={d['w']:.0f} zapas={d['t']-d['r']:.0f}")
        pg.close()
    b.close()
