from playwright.sync_api import sync_playwright
BASE='http://localhost:8765/Web-Core'
CSS='.hdr .brand-sub{ white-space:normal !important; text-wrap:balance; }'
JS='''()=>{const vis=[...document.querySelectorAll('.hdr .brand-txt')].find(e=>{const c=getComputedStyle(e);return c.visibility!=='hidden'&&+c.opacity>0});
const s=vis.querySelector('.brand-sub'); if(getComputedStyle(s).display==='none') return 'ukryta';
const r=document.createRange(); r.selectNodeContents(s); const rs=[...r.getClientRects()]; const b=r.getBoundingClientRect();
const t=document.querySelector('.hdr-tools').getBoundingClientRect().left; return `linie=${new Set(rs.map(x=>Math.round(x.top))).size} zapas=${Math.round(t-b.right)}`}'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for path in ['/en/instytut/','/instytut/']:
        for w in [421,430,433,440,480,503,520,560,600,800]:
            for war in ['obecnie','B']:
                pg=b.new_page(viewport={'width':w,'height':600}); pg.goto(BASE+path); pg.evaluate('document.fonts.ready')
                if war=='B': pg.add_style_tag(content=CSS)
                print(path,w,war,pg.evaluate(JS)); pg.close()
    b.close()
