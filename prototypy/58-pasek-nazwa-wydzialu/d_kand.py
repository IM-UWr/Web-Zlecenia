from playwright.sync_api import sync_playwright
BASE='http://localhost:8765/Web-Core'
kand=['Faculty of Mathematics & CS','Faculty of Math. & Comp. Science','Faculty of Math. & Comp. Sci.','Faculty of Math. and Comp. Science','Faculty of Math & Comp. Science']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for w in [421,430,440]:
        pg=b.new_page(viewport={'width':w,'height':700}); pg.goto(BASE+'/en/instytut/'); pg.evaluate('document.fonts.ready')
        for k in kand:
            d=pg.evaluate('''(k)=>{const s=document.querySelector('.hdr .brand-sub'); s.textContent=k; const r=document.createRange(); r.selectNodeContents(s); const b=r.getBoundingClientRect(); return {w:b.width,z:document.querySelector('.hdr-tools').getBoundingClientRect().left-b.right}}''',k)
            print(w, f"{k:36} szer={d['w']:.0f} zapas do flagi={d['z']:.0f}")
        pg.close()
    b.close()
