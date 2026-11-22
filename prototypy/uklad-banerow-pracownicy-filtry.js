const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  await p.goto('http://localhost:8765/Web-Core/aktualnosci/', { waitUntil: 'networkidle' });
  const wiersz = await p.evaluate(() => { const f = document.querySelector('.filters'); f.querySelectorAll('.tylko-komputer').forEach(e => e.remove()); return f.outerHTML; });
  await p.goto('http://localhost:8765/Web-Core/pracownicy/', { waitUntil: 'networkidle' }); await p.waitForTimeout(600);
  await p.evaluate((wiersz) => {
    // baner jak w propozycji
    const w = document.querySelector('.page-head .wrap');
    w.querySelectorAll('.lead, .ph-haslo, .pt-liczby').forEach(e => e.remove());
    const h1 = w.querySelector('h1');
    const hp = document.createElement('p'); hp.className = 'ph-haslo tylko-telefon'; hp.textContent = 'Kontakt do każdego z nas'; h1.after(hp);
    const ul = document.createElement('ul'); ul.className = 'pt-liczby tylko-telefon';
    ul.innerHTML = '<li><span class="n">129</span>osób</li><li><span class="n">8</span>zakładów</li><li><span class="n">17</span>doktorantów</li>'; hp.after(ul);
    const m = w.querySelector('.ph-m'); if (m) { m.style.filter = 'grayscale(1) brightness(2.4)'; m.style.opacity = '.5'; }
    // jeden wiersz filtrów jak w Aktualnościach
    const t = document.querySelector('.staff-tools');
    const box = document.createElement('div'); box.innerHTML = wiersz; const f = box.firstElementChild;
    t.replaceWith(f);
    const sel = f.querySelector('select');
    const zak = ['Algebra i teoria modeli','Analiza funkcjonalna','Analiza matematyczna','Geometria','Równania różniczkowe','Teoria mnogości i topologia','Teoria prawdopodobieństwa','Statystyka matematyczna'];
    sel.innerHTML = '<option selected>Wszyscy</option><optgroup label="Kto"><option>Nauczyciele akademiccy</option><option>Doktoranci</option><option>Administracja</option><option>Emerytowani</option></optgroup><optgroup label="Zakład">' + zak.map(z => '<option>' + z + '</option>').join('') + '</optgroup>';
    const inp = f.querySelector('input'); if (inp) inp.placeholder = 'Szukaj';
    const c = document.querySelector('.staff-count'); if (c) c.remove();
  }, wiersz);
  await p.waitForTimeout(300);
  await p.screenshot({ path: 'pracownicy-propozycja-a.jpg', type: 'jpeg', quality: 78, clip: { x: 0, y: 0, width: 390, height: 760 } });
  console.log(await p.evaluate(() => Math.round(document.querySelector('.page-head').getBoundingClientRect().height)));
  await b.close();
})();
