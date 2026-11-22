import json
from playwright.sync_api import sync_playwright
BASE='http://localhost:8765/Web-Core'
OUT='/home/claude/proto/img/'
WAR={
 'obecnie':'',
 'A':'@media (max-width: 519px){ .hdr .brand-sub:lang(en){ display:none !important; } }',
 'B':'@media (min-width: 421px) and (max-width: 519px){ .hdr .brand-sub:lang(en){ white-space:normal !important; text-wrap:balance; line-height:1.15; } }',
 'C':'',
}
JS_C='''()=>{ if(innerWidth<=519){ document.querySelectorAll('.hdr .brand-sub').forEach(s=>s.textContent='Faculty of Mathematics & CS'); } }'''
POM='''()=>{ const vis=[...document.querySelectorAll('.hdr .brand-txt')].find(e=>{const c=getComputedStyle(e);return c.visibility!=='hidden'&&+c.opacity>0});
 const s=vis.querySelector('.brand-sub'); let sr=null; if(s && getComputedStyle(s).display!=='none'){const r=document.createRange(); r.selectNodeContents(s); const b=r.getBoundingClientRect(); sr={l:b.left,r:b.right,t:b.top,b:b.bottom};}
 const t=document.querySelector('.hdr .hdr-tools').getBoundingClientRect(); const h=document.querySelector('.hdr').getBoundingClientRect();
 return {sub:sr, tools:{l:t.left,r:t.right,t:t.top,b:t.bottom}, hdrH:h.height}; }'''
meta={}
widths=[412,430,440,480,520]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    def shot(war, w, path, scroll, name, h=118):
        ctx=b.new_context(viewport={'width':w,'height':760}, device_scale_factor=2, reduced_motion='reduce')
        pg=ctx.new_page(); pg.goto(BASE+path, wait_until='load'); pg.evaluate('document.fonts.ready')
        if WAR.get(war): pg.add_style_tag(content=WAR[war])
        if war=='C': pg.evaluate(JS_C)
        if scroll:
            pg.mouse.wheel(0, scroll); pg.wait_for_timeout(700)
        pg.wait_for_timeout(500)
        m=pg.evaluate(POM)
        pg.screenshot(path=OUT+name, clip={'x':0,'y':0,'width':w,'height':h})
        ctx.close(); return m
    for war in WAR:
        for w in widths:
            meta[f'{war}-{w}']=shot(war,w,'/en/instytut/',0,f'{war}-{w}.png')
            meta[f'{war}-{w}-jasny']=shot(war,w,'/en/aktualnosci/',900,f'{war}-{w}-jasny.png',h=64)
    # problem: kilka stron przy 430
    for path,nm,sc in [('/en/studia/','p-studia',0),('/en/pracownicy/','p-pracownicy',0),('/en/seminaria/','p-seminaria',0),('/en/aktualnosci/','p-aktualnosci',0)]:
        meta[nm]=shot('obecnie',430,path,sc,nm+'.png')
    b.close()
json.dump(meta,open('/home/claude/proto/meta.json','w'),indent=1)
print(json.dumps({k:v for k,v in meta.items() if k.startswith('obecnie-430') or k.startswith('B-430')},indent=1))
