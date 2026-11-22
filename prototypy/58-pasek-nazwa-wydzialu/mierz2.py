from playwright.sync_api import sync_playwright
BASE='http://localhost:8765/Web-Core'
pages=['/en/instytut/','/instytut/','/en/']
widths=[360,390,412,421,430,440,480,520,560,600,640,700,768,900,1023]
JS='''() => {
 const tr = e => { if(!e) return null; const cs=getComputedStyle(e); if(cs.display==='none') return {vis:false}; const rg=document.createRange(); rg.selectNodeContents(e); const b=rg.getBoundingClientRect(); return {vis: cs.visibility!=='hidden' && +cs.opacity>0, l:b.left, r:b.right, h:b.height, fs:cs.fontSize}; };
 const vis = [...document.querySelectorAll('.hdr .brand-txt')].find(e=>{const cs=getComputedStyle(e); return cs.visibility!=='hidden' && +cs.opacity>0});
 const sub=tr(vis?.querySelector('.brand-sub')), name=tr(vis?.querySelector('.brand-name, .z-wydzial-nazwa'));
 const t=document.querySelector('.hdr .hdr-tools').getBoundingClientRect();
 return {sub, name, toolsL:t.left, cls: vis?.className};
}'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for path in pages:
      for w in widths:
        ctx=b.new_context(viewport={'width':w,'height':800}); pg=ctx.new_page()
        pg.goto(BASE+path, wait_until='load'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(100)
        d=pg.evaluate(JS)
        s=d['sub']; n=d['name']
        f=lambda x: (f"{'vis' if x['vis'] else 'ukr'} prawa={x.get('r',0):.0f} wys={x.get('h',0):.0f} {x.get('fs','')}") if x else '-'
        print(f"{path:14} {w:5}  narzędzia od {d['toolsL']:.0f}  | nazwa: {f(n)} | sub: {f(s)}  {'NACHODZI o %.0f px'%(s['r']-d['toolsL']) if s and s['vis'] and s['r']>d['toolsL'] else ''}")
        ctx.close()
    b.close()
