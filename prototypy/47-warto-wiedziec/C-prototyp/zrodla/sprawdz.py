import re, sys, glob, os
IDS = {'wladyslaw-slebodzinski','hugo-steinhaus','bronislaw-knaster','edward-marczewski','witold-wolibner','stanislaw-hartman','czeslaw-ryll-nardzewski','kazimierz-urbanik','andrzej-hulanicki','andrzej-krzywicki','marek-bozejko','tomasz-rolski','jan-mycielski','wladyslaw-narkiewicz','roman-duda','julian-perkal','piotr-biler','krzysztof-tabisz',
 'pierwsze-wyklady','nowa-ksiega-szkocka','taksonomia-wroclawska','aksjomat-determinacji','trzech-rektorow','zywa-ges','probability-and-mathematical-statistics','wyklad-tao','annals','kategoria-a-plus','pka','medal-uniwersytetu','medal-sierpinskiego','nagroda-ptm-steinhausa','stypendium-steinhausa'}
for f in sorted(glob.glob('/home/claude/sylwetki/*.md')):
    b=os.path.basename(f)
    if b.endswith('-weryfikacja.md') or b=='BRIEF.md': continue
    t=open(f).read()
    m=re.match(r'---\n(.*?)\n---\n',t,re.S)
    fm=dict(re.findall(r'^(\w+):\s*"?(.*?)"?\s*$',m.group(1),re.M)) if m else {}
    body=t[m.end():] if m else t
    sk=re.search(r':::w-skrocie\n(.*?)\n:::',body,re.S)
    items=re.findall(r'^- \*\*(.+?)\*\* — (.+)$',sk.group(1),re.M) if sk else []
    secs=re.findall(r'^## (.+?)(?: \{#([\w-]+)\})?$',body,re.M)
    links=re.findall(r'\]\(/instytut/warto-wiedziec/([\w-]+)\)',body)
    bad=[l for l in links if l not in IDS]
    prose=re.sub(r':::w-skrocie.*?:::','',body,flags=re.S)
    prose=prose.split('## Źródła')[0]
    words=len(re.sub(r'<!--.*?-->','',prose,flags=re.S).split())
    noid=[s for s,i in secs if not i]
    print(f"{b[:-3]:28} w={words:4} skrot={len(items)} sek={len(secs)} linki={len(links)} zle={bad} bez_id={noid} lata={fm.get('lata')} rocz={fm.get('rocznica_urodzin','-')} zaj={len(fm.get('zajawka',''))} pod={len(fm.get('podpis',''))}")
