const { chromium } = require('playwright');
const BASE = 'http://localhost:8765/Web-Core/';
const odm = (n, f) => { const a = Math.abs(n) % 100, b = a % 10; return n === 1 ? f[0] : (b >= 2 && b <= 4 && !(a >= 12 && a <= 14)) ? f[1] : f[2]; };

// wspólna zmiana banera w przeglądarce
const USTAW = (cfg) => {
  const w = document.querySelector('.page-head .wrap');
  w.querySelectorAll('.lead, .ph-haslo, .pt-liczby').forEach(e => e.remove());
  const h1 = w.querySelector('h1');
  const p = document.createElement('p'); p.className = 'ph-haslo tylko-telefon'; p.textContent = cfg.haslo; h1.after(p);
  if (cfg.liczby && cfg.liczby.length) {
    const ul = document.createElement('ul'); ul.className = 'pt-liczby tylko-telefon';
    ul.innerHTML = cfg.liczby.map(([n, t]) => `<li><span class="n">${n}</span>${t}</li>`).join('');
    p.after(ul);
  } else { p.style.paddingBottom = '4px'; }
  // rysunek szary (jak animacje na telefonie)
  const m = w.querySelector('.ph-m'); if (m) { m.style.filter = 'grayscale(1) brightness(2.4)'; m.style.opacity = '.5'; }
  if (cfg.usun) cfg.usun.forEach(s => document.querySelectorAll(s).forEach(e => e.remove()));
};

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  const go = async s => { await p.goto(BASE + s, { waitUntil: 'networkidle' }); await p.waitForTimeout(700); };
  const shot = async (nazwa) => { await p.evaluate(() => window.scrollTo(0, 0)); await p.waitForTimeout(200); await p.screenshot({ path: nazwa + '.jpg', type: 'jpeg', quality: 78, clip: { x: 0, y: 0, width: 390, height: 760 } }); };
  const wysBanera = () => p.evaluate(() => Math.round(document.querySelector('.page-head').getBoundingClientRect().height));
  const raport = [];

  // ---- dane do liczb ----
  await go('kalendarz/');
  const kal = await p.evaluate(() => {
    const MIES = { sty: 0, lut: 1, mar: 2, kwi: 3, maj: 4, cze: 5, lip: 6, sie: 7, wrz: 8, 'paź': 9, paz: 9, lis: 10, gru: 11 };
    const dzis = new Date(2026, 9, 31);
    const r = { referat: 0, inne: 0, dzis: 0, d7: 0, d30: 0 };
    document.querySelectorAll('[data-widok="nadchodzace"] section').forEach(sec => {
      const rok = +(sec.querySelector('h2')?.textContent.match(/\d{4}/) || [2026])[0];
      sec.querySelectorAll('[data-rodzaj]').forEach(a => {
        if (a.dataset.rodzaj === 'referat') r.referat++; else r.inne++;
        const d = +a.querySelector('.datebox .d').textContent, m = MIES[a.querySelector('.datebox .m').textContent.trim().toLowerCase()];
        const dt = new Date(rok, m, d), roz = Math.round((dt - dzis) / 864e5);
        if (roz === 0) r.dzis++; if (roz >= 0 && roz < 7) r.d7++; if (roz >= 0 && roz < 30) r.d30++;
      });
    });
    return r;
  });
  await go('aktualnosci/');
  const ogl = await p.evaluate(() => +document.querySelector('.pt-liczby li .n').textContent);
  const semy = ['analiza-harmoniczna', 'dydaktyka', 'dyskretna-analiza-harmoniczna', 'geometria', 'prawdopodobienstwo', 'rownania-rozniczkowe', 'statystyka', 'teoria-modeli', 'topologia'];
  let arch = 0;
  for (const s of semy) { await go('seminaria/' + s + '/'); arch += await p.evaluate(() => { const h = [...document.querySelectorAll('main h2')].find(x => /Minione/.test(x.textContent)); return h ? h.closest('section').querySelectorAll('article').length : 0; }); }
  await go('pracownicy/');
  const dokt = await p.evaluate(() => { const h = [...document.querySelectorAll('main h2')].find(x => x.textContent.trim() === 'Doktoranci'); return h.parentElement.querySelectorAll('.staff-list > li').length; });
  console.log({ kal, ogl, arch, dokt });

  const T = (n, f) => [String(n), odm(n, f)];
  const strony = [
    { id: 'studia', s: 'studia/', nazwa: 'Dział: Studia (wzorzec)', wzorzec: true },
    { id: 'matematyka', s: 'studia/matematyka/', nazwa: 'Kierunek: Matematyka', cfg: { haslo: 'Od teorii do zastosowań', liczby: [['3 lata', 'studia I stopnia'], ['2 lata', 'studia II stopnia'], ['5', 'specjalności']], usun: ['.kh-btns.tylko-telefon', '.kh-fakty'] }, po: () => { const r = document.querySelector('.kh-btns-pod'); r.classList.remove('tylko-komputer'); r.querySelectorAll('a').forEach(a => { if (/Rekrutacja/.test(a.textContent)) a.remove(); }); r.style.margin = '0 0 22px'; } },
    { id: 'siad', s: 'studia/siad/', nazwa: 'Kierunek z długim tytułem: SIAD', cfg: { haslo: 'Matematyka, informatyka i AI', liczby: [['6', 'semestrów'], ['180', 'punktów ECTS'], ['70', 'ECTS do wyboru']], usun: ['.kh-btns.tylko-telefon', '.kh-fakty'] }, po: () => { const r = document.querySelector('.kh-btns-pod'); if (r) { r.classList.remove('tylko-komputer'); r.querySelectorAll('a').forEach(a => { if (/Rekrutacja/.test(a.textContent)) a.remove(); }); r.style.margin = '0 0 22px'; } } },
    { id: 'seminarium', s: 'seminaria/analiza-harmoniczna/', nazwa: 'Seminarium (długi tytuł)', cfg: { haslo: 'Operatory, mnożniki, rozwinięcia', liczby: [T(1, ['zapowiedziany referat', 'zapowiedziane referaty', 'zapowiedzianych referatów']), T(2, ['referat w archiwum', 'referaty w archiwum', 'referatów w archiwum']), T(5, ['koordynator', 'koordynatorów', 'koordynatorów'])] }, przed: () => {
        const k = document.querySelector('.sem-koord'); const osoby = k.querySelector('.sem-koord-n').innerHTML; const meta = [...k.querySelectorAll('.sem-meta a')].map(a => a.outerHTML).join(' · ');
        k.remove(); const d = document.createElement('div');
        d.style.cssText = 'font-size:15px;line-height:1.5;color:var(--muted);margin:0 0 18px;padding:0 0 16px;border-bottom:1px solid var(--line, #e3e7ef)';
        d.innerHTML = `<div style="font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:4px">Koordynatorzy</div><div style="color:var(--ink)">${osoby}</div><div style="margin-top:6px">${meta}</div>`;
        d.querySelectorAll('a').forEach(a => { a.style.color = 'var(--ink)'; });
        document.querySelector('.layout .main').prepend(d); } },
    { id: 'seminaria', s: 'seminaria/', nazwa: 'Lista: Seminaria', cfg: { haslo: 'Otwarte dla wszystkich', liczby: [T(semy.length, ['seminarium', 'seminaria', 'seminariów']), T(kal.referat, ['zapowiedziany referat', 'zapowiedziane referaty', 'zapowiedzianych referatów']), T(arch, ['referat w archiwum', 'referaty w archiwum', 'referatów w archiwum'])] } },
    { id: 'granty', s: 'nauka/granty/', nazwa: 'Lista: Projekty i granty', cfg: { haslo: 'Projekty NCN, unijne i inne', liczby: [T(5, ['realizowany projekt', 'realizowane projekty', 'realizowanych projektów']), T(87, ['zakończony', 'zakończone', 'zakończonych']), T(94, ['projekt łącznie', 'projekty łącznie', 'projektów łącznie'])] } },
    { id: 'obrony', s: 'obrony-doktorskie/', nazwa: 'Lista: Obrony doktorskie (2 liczby)', cfg: { haslo: 'Publiczne obrony rozpraw', liczby: [T(2, ['nadchodząca obrona', 'nadchodzące obrony', 'nadchodzących obron']), T(6, ['odbyta obrona', 'odbyte obrony', 'odbytych obron'])] } },
    { id: 'pracownicy', s: 'pracownicy/', nazwa: 'Lista: Pracownicy', cfg: { haslo: 'Kontakt do każdego z nas', liczby: [T(129, ['osoba', 'osoby', 'osób']), T(8, ['zakład', 'zakłady', 'zakładów']), T(dokt, ['doktorant', 'doktorantów', 'doktorantów'])] } },
    { id: 'wladze', s: 'instytut/wladze/', nazwa: 'Bez liczb: Władze Instytutu', cfg: { haslo: 'Dyrekcja i sekretariat', liczby: null } },
    { id: 'plan', s: 'studia/plan-zajec/', nazwa: 'Bez liczb: Plan zajęć', cfg: { haslo: 'Zawsze aktualny, prosto z USOS', liczby: null } },
    { id: 'aktualnosci', s: 'aktualnosci/', nazwa: 'Dział: Aktualności — nowe liczby', cfg: { haslo: 'Co słychać w Instytucie', liczby: [T(ogl, ['nowe ogłoszenie', 'nowe ogłoszenia', 'nowych ogłoszeń']), T(kal.inne, ['nadchodzące wydarzenie', 'nadchodzące wydarzenia', 'nadchodzących wydarzeń']), T(kal.referat, ['zapowiedziany referat', 'zapowiedziane referaty', 'zapowiedzianych referatów'])] } },
    { id: 'kalendarz', s: 'kalendarz/', nazwa: 'Dział: Kalendarz — liczby czasowe', cfg: { haslo: 'Co, gdzie i kiedy', liczby: [[String(kal.dzis), odm(kal.dzis, ['termin dziś', 'terminy dziś', 'terminów dziś'])], [String(kal.d7), 'w ciągu 7 dni'], [String(kal.d30), 'w ciągu 30 dni']] } },
  ];
  for (const st of strony) {
    await go(st.s); const przed = await wysBanera(); await shot(st.id + '-obecnie');
    let po = przed;
    if (!st.wzorzec) {
      if (st.przed) await p.evaluate(st.przed);
      await p.evaluate(USTAW, st.cfg);
      if (st.po) await p.evaluate(st.po);
      await p.waitForTimeout(300); po = await wysBanera(); await shot(st.id + '-propozycja');
    }
    raport.push({ id: st.id, nazwa: st.nazwa, s: st.s, przed, po, haslo: st.cfg?.haslo, liczby: st.cfg?.liczby });
    console.log(st.id, przed, '→', po);
  }
  require('fs').writeFileSync('raport.json', JSON.stringify({ raport, kal, ogl, arch, dokt }, null, 1));
  await b.close();
})();
