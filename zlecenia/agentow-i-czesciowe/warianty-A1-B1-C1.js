// Raport „Propozycje: telefon” (31.10.2026) — CSS wszystkich makiet.
// Makiety: kopia Web-Core (HEAD 4a9f0be3, bez niezakończonych zmian), `astro build`, ten CSS wstrzyknięty do gotowych stron
// (<style> na końcu <head>), Chromium 390 × 844, 2×, ograniczony ruch; ciemny motyw przez localStorage 'motyw' = 'dark'.
// To szkic do makiet, nie gotowy kod: dużo !important, bo style z komponentów Astro (scoped) mają wyższą specyficzność.
// Zestawy: A1/A2/A3 (ciemny motyw), B0 („teraz” + „+N”), B1/B2/B3 (etykiety) + B_JS (adresaci → .dla, zwijanie do „+N”),
// C1/C2/C3 (kafelki). W makietach B i C w ciemnym motywie dołożony jest A1.
// C2 wskazuje plik maski fal po nazwie z kompilacji (_astro/fale-linie-pion.*.webp) — w kodzie trzeba użyć importu z src/assets/tlo.

// CSS makiet (wstrzykiwany do zbudowanych stron). Telefon = @media (max-width: 760px).
const TEL = (css) => `@media (max-width: 760px) {\n${css}\n}`;

// ---------- A. Ciemny tryb: znaczniki bez bursztynu ----------
// wspólny szkielet: token „znacznik” zamiast --primary w czterech elementach (+ mały kafelek daty .pt-dbox)
const A_BAZA = `
:root { --znacznik: #1b2d52; --znacznik-ink: #ffffff; --znacznik-tekst: #1b2d52; }
.datebox:not(.minione), .pt-dbox:not(.minione), .badge-wydarzenie,
.chip[aria-pressed='true'], .chip[role='tab'][aria-selected='true'],
.burger, .burger:hover { background: var(--znacznik); border-color: var(--znacznik); color: var(--znacznik-ink); }
:root[data-theme='dark'] { --tint-ink: #d3dcea; }
:root[data-theme='dark'] :is(.pt-k, .pt-all, .pt-all:hover, .link-arrow, .event .k, .sem-row .sem, .talk summary, .more summary) { color: var(--znacznik-tekst); }
`;
const A1 = TEL(`
${A_BAZA}
:root[data-theme='dark'] { --znacznik: #2b4170; --znacznik-ink: #f1f4fa; --znacznik-tekst: #a9c0e8; }
.ph-granat { --znacznik: #ffffff; --znacznik-ink: #1b2d52; }
:root[data-theme='dark'] :is(.datebox, .pt-dbox):not(.minione) .m { color: #f2a33a; }
`);
const A2 = TEL(`
${A_BAZA}
:root[data-theme='dark'] { --znacznik: #d3ddec; --znacznik-ink: #0f1a30; --znacznik-tekst: #c3d0e4; }
.ph-granat { --znacznik: #ffffff; --znacznik-ink: #1b2d52; }
`);
const A3 = TEL(`
${A_BAZA}
:root[data-theme='dark'] { --znacznik: transparent; --znacznik-ink: #ecf0f7; --znacznik-tekst: #c6d3e8; --znacznik-kontur: rgb(217 230 242 / .42); }
:root[data-theme='dark'] :is(.datebox, .pt-dbox):not(.minione), :root[data-theme='dark'] .badge-wydarzenie, :root[data-theme='dark'] .burger { box-shadow: inset 0 0 0 1.5px var(--znacznik-kontur); }
:root[data-theme='dark'] :is(.datebox, .pt-dbox):not(.minione) .m { color: #f2a33a; }
:root[data-theme='dark'] .chip[aria-pressed='true'] { background: #1c2740; border-color: #ecf0f7; color: #ffffff; }
.ph-granat .chip[aria-pressed='true'] { background: rgb(255 255 255 / .14) !important; border-color: #ffffff !important; color: #ffffff !important; }
`);

// ---------- B. Jedna rodzina etykiet ----------
const B_DLA = `
.wa-meta .badge.dla, .wa-meta .badge.dla-plus { background: none; box-shadow: none; padding: 0 !important; border-radius: 0; font-size: 13.5px !important; font-weight: 500; letter-spacing: 0; text-transform: lowercase; color: var(--et-dla); }
.wa-meta .badge.dla-plus { font-weight: 700; text-transform: none; font-variant-numeric: tabular-nums; }
.wa-meta .badge.dla:has(~ .badge.dla:not([data-zwin]))::after { content: ','; }
`;
const B_TOKENY = `
:root { --et-granat-tlo: #dce6f7; --et-granat: #18305f; --et-burs-tlo: #fcebd2; --et-burs: #6b3f05; --et-szary-tlo: #eceef2; --et-szary: #4a5466; --et-kontur: rgb(17 26 46 / .42); --et-dla: #5b6577;
  --et2-granat: #05649c; --et2-burs: #9a5a07; --et2-szary: #5b6577; --et3-granat: #1b2d52; --et3-szary: #9aa6b8; }
:root[data-theme='dark'] { --et-granat-tlo: rgb(110 150 230 / .26); --et-granat: #d3e1fb; --et-burs-tlo: rgb(242 163 58 / .16); --et-burs: #f6c47a; --et-szary-tlo: rgb(255 255 255 / .065); --et-szary: #aab5c7; --et-kontur: rgb(217 230 242 / .42); --et-dla: #9da9be;
  --et2-granat: #9cc4ea; --et2-burs: #f2a33a; --et2-szary: #9da9be; --et3-granat: #8fb0e6; --et3-szary: #66738a; }
`;
const B1 = TEL(`
${B_TOKENY}
:is(.news-meta, .wa-meta) .badge { padding: 1px 8px !important; border-radius: 6px; font-size: 12.5px !important; font-weight: 700; line-height: 1.5; letter-spacing: 0; background: var(--et-szary-tlo); color: var(--et-szary); box-shadow: none; }
:is(.news-meta, .wa-meta) .badge-wydarzenie { background: var(--et-granat-tlo); color: var(--et-granat); }
:is(.news-meta, .wa-meta) :is(.badge-sukces, .badge-konferencja) { background: var(--et-burs-tlo); color: var(--et-burs); }
:is(.news-meta, .wa-meta) .badge-obrona { background: transparent; box-shadow: inset 0 0 0 1px var(--et-kontur); color: var(--ink); }
.wa-meta time { margin-right: 4px !important; }
${B_DLA}
`);
const B2 = TEL(`
${B_TOKENY}
:is(.news-meta, .wa-meta) .badge { background: none; box-shadow: none; padding: 0 !important; border-radius: 0; font-size: 11.5px !important; font-weight: 800; letter-spacing: .07em; text-transform: uppercase; line-height: 1.6; color: var(--et2-szary); }
:is(.news-meta, .wa-meta) .badge-wydarzenie { color: var(--et2-granat); }
:is(.news-meta, .wa-meta) :is(.badge-sukces, .badge-konferencja) { color: var(--et2-burs); }
:is(.news-meta, .wa-meta) .badge-obrona { color: var(--ink); }
.news-meta:not(.wa-meta) > .badge + span:not(.badge)::before { content: '·'; margin-right: 6px; color: var(--muted); }
.wa-meta { column-gap: 7px !important; }
.wa-meta time { margin-right: 0 !important; }
.wa-meta > .badge:not(.dla):not(.dla-plus)::before, .wa-meta > .badge:not(.dla):not(.dla-plus) + .badge.dla::before { content: '·'; margin-right: 7px; color: var(--muted); font-weight: 400; letter-spacing: 0; text-transform: none; }
${B_DLA}
`);
const B3 = TEL(`
${B_TOKENY}
:is(.news-meta, .wa-meta) .badge { gap: 6px; background: none; box-shadow: none; padding: 0 !important; border-radius: 0; font-size: 13.5px !important; font-weight: 700; letter-spacing: 0; line-height: 1.5; color: var(--ink); }
:is(.news-meta, .wa-meta) .badge:not(.dla):not(.dla-plus)::before { content: ''; flex: none; width: 8px; height: 8px; border-radius: 50%; background: var(--et3-szary); }
:is(.news-meta, .wa-meta) .badge-wydarzenie::before { background: var(--et3-granat) !important; }
:is(.news-meta, .wa-meta) :is(.badge-sukces, .badge-konferencja)::before { background: #f2a33a !important; }
:is(.news-meta, .wa-meta) .badge-obrona::before { background: transparent !important; box-shadow: inset 0 0 0 1.5px var(--ink); }
.wa-meta { column-gap: 7px !important; }
.wa-meta time { margin-right: 3px !important; }
.wa-meta > .badge:not(.dla):not(.dla-plus) + .badge.dla::before { content: '·'; margin-right: 7px; color: var(--muted); font-weight: 400; }
${B_DLA}
`);
// „Teraz” z „+N” w obecnym stylu (zachowanie zmiany drugiego agenta: plakietka „+N” jak pozostałe)
const B0 = TEL(`.wa-meta .badge.dla-plus { font-variant-numeric: tabular-nums; }`);

// skrypt: adresaci dostają klasę .dla; linijka plakietek bez zawijania; nadmiarowi adresaci zwinięci od końca do „+N”
const B_JS = `(() => {
  document.querySelectorAll('.wa-meta').forEach((m) => {
    const dla = [...m.querySelectorAll('.badge')].filter((b) => ![...b.classList].some((c) => c.startsWith('badge-')));
    if (!dla.length) return;
    dla.forEach((b) => b.classList.add('dla'));
    const plus = document.createElement('span');
    plus.className = 'badge dla-plus'; plus.hidden = true;
    dla[dla.length - 1].after(plus);
    m.style.flexWrap = 'nowrap';
    [...m.children].forEach((c) => { c.style.flexShrink = '0'; c.style.whiteSpace = 'nowrap'; });
    let k = 0;
    while (m.scrollWidth > m.clientWidth + 0.5 && k < dla.length) {
      k++; const b = dla[dla.length - k]; b.style.display = 'none'; b.dataset.zwin = '1';
      plus.hidden = false; plus.textContent = '+' + k;
    }
  });
})()`;

// ---------- C. Kafelki czy brak kafelków ----------
const C_PLASKO = `
.dz-groups { border: 0 !important; background: transparent !important; padding: 0 !important; border-radius: 0 !important; box-shadow: none !important; }
.dz-g h3 { margin-top: 14px !important; }
.dz-g:first-child h3 { margin-top: 4px !important; }
.dz-tile + .dz-tile { border-top-color: var(--c-kreska) !important; }
.dz-tile { padding-inline: 0 !important; }
.pt-box { border: 0 !important; background: transparent !important; padding: 0 !important; border-radius: 0 !important; box-shadow: none !important; }
.pt-list > li + li, .pt-links li { border-color: var(--c-kreska) !important; }
.pt-item { padding-inline: 0 !important; }
.zsec.dz-ramka-sek { padding: 16px 0 6px !important; }
.zsec.dz-ramka-sek::after { display: none !important; }
.dz-granty { gap: 0 !important; }
.dz-ramka-sek .spec { background: transparent !important; border: 0 !important; border-top: 1px solid var(--c-kreska) !important; border-radius: 0 !important; padding: 12px 0 !important; box-shadow: none !important; }
.dz-ramka-sek .dz-granty .spec:first-child { border-top: 0 !important; }
.karty-lista > .row-item { border-top-color: var(--c-kreska) !important; }
.dz-tel { gap: 0 !important; }
`;
const C_KRESKA = `
:root { --c-kreska: rgb(17 26 46 / .13); }
:root[data-theme='dark'] { --c-kreska: rgb(217 230 242 / .14); }
`;
const C1 = TEL(`
body[data-tlo='fale']::before { opacity: .45; }
:root[data-theme='dark'] body[data-tlo='fale']::after { opacity: .45; }
/* listy (Aktualności) w osobnych białych kartach, jak na komputerze */
.karty-lista { display: flex; flex-direction: column; gap: 8px; }
.karty-lista > .row-item { padding: 12px 14px !important; border: 1px solid var(--kafel-ramka, var(--line)) !important; border-radius: 14px; background: var(--kafel, var(--bg)); box-shadow: var(--kafel-cien, none); }
.lista-miesiac > .month { margin-bottom: 8px; }
/* bez karty w karcie: projekty w ramce Nauki jako wiersze z kreską */
.dz-granty { gap: 0 !important; }
.dz-ramka-sek .spec { background: transparent !important; border: 0 !important; border-top: 1px solid var(--line) !important; border-radius: 0 !important; padding: 12px 0 !important; box-shadow: none !important; }
.dz-ramka-sek .dz-granty .spec:first-child { border-top: 0 !important; padding-top: 4px !important; }
`);
const C2 = TEL(`
${C_KRESKA}
${C_PLASKO}
body[data-tlo='fale']::before { filter: saturate(1.35); }
body[data-tlo='fale']::after { background: rgb(27 45 82 / .17); -webkit-mask: url('/Web-Core/_astro/fale-linie-pion.CzxHzQCV.webp') center / cover no-repeat; mask: url('/Web-Core/_astro/fale-linie-pion.CzxHzQCV.webp') center / cover no-repeat; }
:root[data-theme='dark'] body[data-tlo='fale'] { --tlo-linie: rgb(214 228 245 / .40); }
`);
const C3 = TEL(`
${C_KRESKA}
${C_PLASKO}
body[data-tlo]::before, body[data-tlo]::after { display: none !important; }
`);

module.exports = { A1, A2, A3, B0, B1, B2, B3, B_JS, C1, C2, C3 };
