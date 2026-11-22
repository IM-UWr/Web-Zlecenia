// Przegląd szerokości: renderuje zbudowaną stronę (Web-Podglad, gałąź zbudowana) w kilku rozmiarach okna,
// wykrywa kolizje tekstu, tekst obcięty przez overflow, tekst wychodzący poza ramkę (kafelek/przycisk/pole)
// i poziome przewijanie strony; robi zrzuty. Wynik: wyniki.json + zrzuty/<strona>/<WxH>-*.jpg
const { chromium } = require('playwright') /* npx playwright install chromium; launch bez executablePath */;
const fs = require('fs');
const path = require('path');

// Adres strony: zmienna BAZA (np. podgląd `npm run preview` albo zbudowane dist serwowane lokalnie)
const BAZA = process.env.BAZA || 'http://localhost:4321/Web-Core';
const OUT = process.env.OUT || path.join(process.cwd(), 'raport-zrzuty', 'szerokosci');
const ZRZUTY = path.join(OUT, 'zrzuty');

// [szerokość, wysokość] w px CSS — realne okna przeglądarki (ekran / skala systemu − pasek przeglądarki)
const OKNA = [
  [800, 900],   // wąskie okno / tablet pionowo tuż nad progiem telefonu
  [860, 780],   // okno ~1075 px przy skali 125% (jak na zrzucie)
  [960, 950],   // pół ekranu Full HD
  [1024, 700],  // tablet poziomo / 1280 przy 125%
  [1180, 820],  // iPad Air poziomo
  [1280, 600],  // Full HD przy 150% (laptopy 14–15")
  [1366, 620],  // laptop 1366×768 przy 100%
  [1440, 780],  // MacBook / 1440×900
  [1536, 730],  // Full HD przy 125% (domyślne Windows na laptopach)
  [1707, 830],  // 2560×1440 przy 150%
  [1920, 950],  // Full HD przy 100% — wzorzec projektu
];
const PELNE = new Set(['960x950', '1280x600', '1536x730']); // zrzuty całej strony (do 5000 px)

const S = (id, adres, grupa, opcje = {}) => ({ id, adres, grupa, ...opcje });
const STRONY = [
  S('glowna', '/', 'glowna', { glowna: true, menu: true }),
  S('instytut', '/instytut/', 'dzial', { dzial: true }),
  S('nauka', '/nauka/', 'dzial', { dzial: true }),
  S('studia', '/studia/', 'dzial', { dzial: true, menu: true }),
  S('popularyzacja', '/popularyzacja/', 'dzial', { dzial: true }),
  S('instytut-kontakt', '/instytut/kontakt/', 'podstrona'),
  S('instytut-struktura', '/instytut/struktura/', 'podstrona'),
  S('instytut-wladze', '/instytut/wladze/', 'podstrona'),
  S('instytut-infrastruktura', '/instytut/infrastruktura-informatyczna/', 'podstrona'),
  S('instytut-infra-siec', '/instytut/infrastruktura-informatyczna/siec-studencka/', 'podstrona'),
  S('instytut-zaklady', '/instytut/zaklady/', 'lista'),
  S('instytut-zaklad', '/instytut/zaklady/analiza-funkcjonalna/', 'wpis'),
  S('nauka-granty', '/nauka/granty/', 'lista'),
  S('nauka-grant', '/nauka/granty/2009-nieliniowe-rownania-ewolucji-z-dyfuzja-typu-levy-ego/', 'wpis'),
  S('nauka-konferencje', '/nauka/konferencje/', 'lista'),
  S('nauka-publikacje', '/nauka/publikacje/', 'lista'),
  S('nauka-publikacje-rok', '/nauka/publikacje/2018/', 'lista'),
  S('nauka-sukcesy', '/nauka/sukcesy/', 'lista'),
  S('nauka-sukcesy-historia', '/nauka/sukcesy/historia/', 'podstrona'),
  S('studia-matematyka', '/studia/matematyka/', 'podstrona'),
  S('studia-siad', '/studia/siad/', 'podstrona'),
  S('studia-isim', '/studia/isim/', 'podstrona'),
  S('studia-szkola-doktorska', '/studia/szkola-doktorska/', 'podstrona'),
  S('studia-sd-rekrutacja', '/studia/szkola-doktorska/rekrutacja/', 'podstrona'),
  S('studia-podyplomowe', '/studia/podyplomowe/', 'podstrona'),
  S('studia-plan-zajec', '/studia/plan-zajec/', 'lista'),
  S('studia-rok-akademicki', '/studia/rok-akademicki/', 'lista'),
  S('studia-zajecia', '/studia/zajecia/', 'podstrona'),
  S('studia-pierwszy-rok', '/studia/pierwszy-rok/', 'podstrona'),
  S('studia-egzaminy', '/studia/egzaminy-i-dyplom/', 'podstrona'),
  S('studia-sprawy', '/studia/sprawy-studenckie/', 'podstrona'),
  S('studia-procedura', '/studia/procedura-dyplomowania/', 'podstrona'),
  S('studia-skrypty', '/studia/skrypty/', 'podstrona'),
  S('studia-most', '/studia/program-most/', 'podstrona'),
  S('studia-archiwalne', '/studia/archiwalne-programy/', 'podstrona'),
  S('popularyzacja-uczniowie', '/popularyzacja/uczniowie/', 'podstrona'),
  S('popularyzacja-nauczyciele', '/popularyzacja/nauczyciele/', 'podstrona'),
  S('popularyzacja-organizatorzy', '/popularyzacja/organizatorzy/', 'podstrona'),
  S('popularyzacja-wszyscy', '/popularyzacja/wszyscy/', 'podstrona'),
  S('aktualnosci', '/aktualnosci/', 'lista'),
  S('aktualnosc', '/aktualnosci/2026-03-01-sukces-motiejusa-valiunasa-w-konkursie-ncn/', 'wpis'),
  S('aktualnosc-wydarzenie', '/aktualnosci/test-2026-11-06-dzien-otwarty-dla-kandydatow/', 'wpis'),
  S('kalendarz', '/kalendarz/', 'lista'),
  S('seminaria', '/seminaria/', 'lista'),
  S('seminarium', '/seminaria/topologia/', 'wpis'),
  S('pracownicy', '/pracownicy/', 'lista'),
  S('obrony', '/obrony-doktorskie/', 'lista'),
  S('obrona', '/obrony-doktorskie/2026-10-27-malwina-mrowinska/', 'wpis'),
  S('warto-wiedziec', '/warto-wiedziec/', 'lista'),
  S('warto-wpis', '/warto-wiedziec/wyklad-terencea-tao/', 'wpis'),
  S('o-stronie', '/o-stronie/', 'ogolna'),
  S('dostepnosc', '/deklaracja-dostepnosci/', 'ogolna'),
  S('prywatnosc', '/polityka-prywatnosci/', 'ogolna'),
  S('szukaj', '/szukaj/', 'ogolna'),
  S('powiadomienia', '/powiadomienia/', 'ogolna'),
  S('404', '/404.html', 'ogolna'),
  S('en-glowna', '/en/', 'en', { glowna: true }),
  S('en-instytut', '/en/instytut/', 'en', { dzial: true }),
  S('en-nauka', '/en/nauka/', 'en', { dzial: true }),
  S('en-studia', '/en/studia/', 'en', { dzial: true }),
  S('en-popularyzacja', '/en/popularyzacja/', 'en', { dzial: true }),
  S('en-studia-matematyka', '/en/studia/matematyka/', 'en'),
  S('en-instytut-wladze', '/en/instytut/wladze/', 'en'),
  S('en-seminaria', '/en/seminaria/', 'en'),
  S('en-pracownicy', '/en/pracownicy/', 'en'),
];

// --- wykrywanie w przeglądarce ---
function wykryj() {
  const W = innerWidth, H = innerHeight;
  const wynik = { przewijanieX: Math.max(0, document.documentElement.scrollWidth - W), problemy: [] };
  const opis = (el) => {
    const czesci = [];
    for (let e = el; e && e !== document.body && czesci.length < 4; e = e.parentElement) {
      let s = e.tagName.toLowerCase();
      if (e.id) s += '#' + e.id;
      const kl = [...e.classList].filter((k) => !k.startsWith('astro-')).slice(0, 2);
      if (kl.length) s += '.' + kl.join('.');
      czesci.unshift(s);
    }
    return czesci.join(' > ');
  };
  const widoczny = (el) => (el.checkVisibility ? el.checkVisibility({ opacityProperty: true, visibilityProperty: true }) : true);
  const pamiecKlipu = new Map();
  const NIESK = { l: -1e9, t: -1e9, r: 1e9, b: 1e9 };
  function klip(el) {
    if (!el || el === document.documentElement) return NIESK;
    if (pamiecKlipu.has(el)) return pamiecKlipu.get(el);
    const p = klip(el.parentElement);
    const cs = getComputedStyle(el);
    let c = p;
    const ox = cs.overflowX !== 'visible', oy = cs.overflowY !== 'visible';
    if ((ox || oy) && el !== document.body && cs.display !== 'contents' && cs.display !== 'inline') {
      const r = el.getBoundingClientRect();
      c = { l: ox ? Math.max(p.l, r.left) : p.l, r: ox ? Math.min(p.r, r.right) : p.r, t: oy ? Math.max(p.t, r.top) : p.t, b: oy ? Math.min(p.b, r.bottom) : p.b };
    }
    pamiecKlipu.set(el, c);
    return c;
  }
  // ramka: najbliższy przodek z tłem, obramowaniem lub cieniem (kafelek, przycisk, pole) — poza dużymi sekcjami pełnej szerokości
  const pamiecRamki = new Map();
  function ramka(el) {
    if (!el || el === document.body || el === document.documentElement) return null;
    if (pamiecRamki.has(el)) return pamiecRamki.get(el);
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const tlo = cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'transparent';
    const kreska = ['Top', 'Right', 'Bottom', 'Left'].filter((s) => parseFloat(cs['border' + s + 'Width']) > 0).length >= 2;
    const cien = cs.boxShadow !== 'none' && /inset/.test(cs.boxShadow);
    const pelnaSzer = r.width >= W - 2;
    let w = null;
    if (cs.display === 'contents') w = ramka(el.parentElement);
    else if ((tlo || kreska || cien) && !pelnaSzer && cs.display !== 'inline' && r.width > 20 && r.height > 14) w = el;
    else w = ramka(el.parentElement);
    pamiecRamki.set(el, w);
    return w;
  }
  // linie tekstu
  const linie = [];
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (n.nodeValue.trim() ? 1 : 2) });
  let n;
  while ((n = tw.nextNode())) {
    const el = n.parentElement;
    if (!el || /^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE|TITLE)$/.test(el.tagName)) continue;
    if (!widoczny(el)) continue;
    const zakres = document.createRange();
    zakres.selectNodeContents(n);
    const c = klip(el);
    const fixed = (() => { for (let e = el; e; e = e.parentElement) { const p = getComputedStyle(e).position; if (p === 'fixed' || p === 'sticky') return true; } return false; })();
    for (const r of zakres.getClientRects()) {
      if (r.width < 2 || r.height < 4) continue;
      const v = { l: Math.max(r.left, c.l), r: Math.min(r.right, c.r), t: Math.max(r.top, c.t), b: Math.min(r.bottom, c.b) };
      if (v.r - v.l <= 1 || v.b - v.t <= 1) continue; // całkiem schowane (sr-only, zwinięte pola)
      const tekst = n.nodeValue.trim().replace(/\s+/g, ' ').slice(0, 60);
      const obcX = (r.right - r.left) - (v.r - v.l), obcY = (r.bottom - r.top) - (v.b - v.t);
      if (obcX > 4 || obcY > r.height * 0.35) {
        wynik.problemy.push({ typ: 'obciety', tekst, el: opis(el), px: Math.round(Math.max(obcX, obcY)), y: Math.round(r.top + scrollY) });
      }
      linie.push({ el, tekst, fixed, l: v.l, r: v.r, t: v.t, b: v.b, y0: r.top + scrollY });
      // wychodzenie poza ramkę
      const rm = ramka(el);
      if (rm) {
        const R = rm.getBoundingClientRect();
        const wyjX = Math.max(R.left - v.l, v.r - R.right), wyjY = Math.max(R.top - v.t, v.b - R.bottom);
        if (wyjX > 3 || wyjY > 6) wynik.problemy.push({ typ: 'poza-ramka', tekst, el: opis(el), ramka: opis(rm), px: Math.round(Math.max(wyjX, wyjY)), y: Math.round(r.top + scrollY) });
      }
      // poza oknem w poziomie
      if (v.r > W + 2 || v.l < -2) wynik.problemy.push({ typ: 'poza-oknem', tekst, el: opis(el), px: Math.round(Math.max(v.r - W, -v.l)), y: Math.round(r.top + scrollY) });
    }
  }
  // kolizje: środkowy pas wysokości linii (60%), różne elementy, żaden nie zawiera drugiego
  const pas = linie.map((x) => { const h = x.b - x.t; return { ...x, t2: x.t + h * 0.2, b2: x.b - h * 0.2, l2: x.l + 1, r2: x.r - 1 }; }).sort((a, b) => a.t2 - b.t2);
  const widziane = new Set();
  for (let i = 0; i < pas.length; i++) {
    const a = pas[i];
    for (let j = i + 1; j < pas.length && pas[j].t2 < a.b2; j++) {
      const b = pas[j];
      if (a.el === b.el || a.el.contains(b.el) || b.el.contains(a.el)) continue;
      if (a.fixed !== b.fixed) continue; // przyklejony pasek nad treścią — osobna sprawa
      const w = Math.min(a.r2, b.r2) - Math.max(a.l2, b.l2), h = Math.min(a.b2, b.b2) - Math.max(a.t2, b.t2);
      if (w > 3 && h > 2 && w * h > 30) {
        const k = opis(a.el) + '|' + opis(b.el);
        if (widziane.has(k)) continue;
        widziane.add(k);
        wynik.problemy.push({ typ: 'kolizja', tekst: a.tekst + '  ⟷  ' + b.tekst, el: opis(a.el), el2: opis(b.el), px: Math.round(w), y: Math.round(a.y0) });
      }
    }
  }
  // nagłówek: gdzie kończy się baner (jaka część pierwszego ekranu idzie na nagłówek)
  const nagl = document.querySelector('.z-nagl, .z-okladka, [class*="z-okl"]');
  wynik.banerDol = nagl ? Math.round(nagl.getBoundingClientRect().bottom + scrollY) : null;
  wynik.wysokoscStrony = document.documentElement.scrollHeight;
  // zostaw najwyżej 40 problemów każdego typu
  const ile = {};
  wynik.problemy = wynik.problemy.filter((p) => (ile[p.typ] = (ile[p.typ] || 0) + 1) <= 40);
  wynik.licznik = ile;
  return wynik;
}

async function pracownik(przegladarka, zadania, wyniki) {
  while (zadania.length) {
    const { strona, okno } = zadania.shift();
    const [w, h] = okno;
    const klucz = `${w}x${h}`;
    const kat = path.join(ZRZUTY, strona.id);
    fs.mkdirSync(kat, { recursive: true });
    const ctx = await przegladarka.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1, reducedMotion: 'reduce', colorScheme: 'light', locale: 'pl-PL' });
    const p = await ctx.newPage();
    const zapis = { strona: strona.id, adres: strona.adres, grupa: strona.grupa, okno: klucz, stany: {} };
    try {
      await p.goto(BAZA + strona.adres, { waitUntil: 'load', timeout: 45000 });
      await p.evaluate(() => document.fonts && document.fonts.ready);
      await p.waitForTimeout(500);
      zapis.stany.start = await p.evaluate(wykryj);
      await p.screenshot({ path: path.join(kat, `${klucz}-gora.jpg`), type: 'jpeg', quality: 72 });
      if (PELNE.has(klucz)) {
        const wys = Math.min(5000, await p.evaluate(() => document.documentElement.scrollHeight));
        await p.screenshot({ path: path.join(kat, `${klucz}-cala.jpg`), type: 'jpeg', quality: 60, fullPage: true, clip: { x: 0, y: 0, width: w, height: wys } });
      }
      if (strona.glowna) {
        const jest = await p.$('.z-druga');
        if (jest) {
          await p.evaluate(() => document.querySelector('.z-druga').scrollIntoView({ block: 'start' }));
          await p.waitForTimeout(400);
          zapis.stany.drugi = await p.evaluate(wykryj);
          await p.screenshot({ path: path.join(kat, `${klucz}-drugi.jpg`), type: 'jpeg', quality: 72 });
          await p.evaluate(() => scrollTo(0, 0));
        }
      }
      if (strona.dzial) {
        const karty = await p.$$('.z-dz-karta');
        for (let i = 0; i < karty.length; i++) {
          if (!(await karty[i].isVisible())) continue;
          await karty[i].click();
          await p.waitForTimeout(450);
          await p.evaluate(() => { const e = document.querySelector('.z-dz-karty'); if (e) scrollTo(0, Math.max(0, e.getBoundingClientRect().top + scrollY - 120)); });
          await p.waitForTimeout(150);
          zapis.stany[`karta${i + 1}`] = await p.evaluate(wykryj);
          await p.screenshot({ path: path.join(kat, `${klucz}-karta${i + 1}.jpg`), type: 'jpeg', quality: 72 });
          await karty[i].click();
          await p.waitForTimeout(350);
          await p.evaluate(() => scrollTo(0, 0));
        }
      }
      if (strona.menu) {
        const b = await p.$('.z-burger');
        if (b && (await b.isVisible())) {
          await b.click();
          await p.waitForTimeout(500);
          zapis.stany.menu = await p.evaluate(wykryj);
          await p.screenshot({ path: path.join(kat, `${klucz}-menu.jpg`), type: 'jpeg', quality: 72 });
        }
      }
    } catch (e) {
      zapis.blad = String(e).slice(0, 300);
    }
    wyniki.push(zapis);
    await ctx.close();
    process.stdout.write('.');
  }
}

(async () => {
  fs.mkdirSync(ZRZUTY, { recursive: true });
  const przegladarka = await chromium.launch({ args: ['--disable-gpu', '--font-render-hinting=none'] });
  const zadania = [];
  const tylko = process.env.STRONY ? process.env.STRONY.split(',') : null;
  const tylkoOkna = process.env.OKNA ? process.env.OKNA.split(',') : null;
  for (const strona of STRONY) for (const okno of OKNA) {
    if (tylko && !tylko.includes(strona.id)) continue;
    if (tylkoOkna && !tylkoOkna.includes(`${okno[0]}x${okno[1]}`)) continue;
    zadania.push({ strona, okno });
  }
  const wyniki = [];
  const t0 = Date.now();
  await Promise.all([1, 2, 3].map(() => pracownik(przegladarka, zadania, wyniki)));
  await przegladarka.close();
  wyniki.sort((a, b) => (a.strona + a.okno).localeCompare(b.strona + b.okno, 'pl', { numeric: true }));
  fs.writeFileSync(path.join(OUT, 'wyniki.json'), JSON.stringify(wyniki, null, 1));
  console.log(`\n${wyniki.length} renderów w ${Math.round((Date.now() - t0) / 1000)} s`);
})();
