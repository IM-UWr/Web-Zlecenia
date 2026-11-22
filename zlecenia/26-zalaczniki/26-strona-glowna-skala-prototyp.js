// Zlecenie 26 — PROTOTYP (wstrzyknięty w zbudowany podgląd; wzór zachowania, nie kod do skopiowania 1:1).

/* PUNKT 1. Okładka jako jedna kompozycja: s = min(W/1920, H/950). Wartości przy 1920×950 = dzisiejsze.
   W prototypie: CSS poniżej + w skrypcie ULOZ (Okladka.astro) podmiana stałej  ODSTEP=58  na
   ODSTEP=58*Math.min(innerWidth/1920,innerHeight/950)  (tytuł i łuk liczy dalej ten sam skrypt).
   Przy wdrożeniu s licz raz (w ULOZ), ustaw jako zmienną CSS i z niej buduj rozmiary; Math.min z progami jak niżej. */
const CSS_OKLADKI = `@media (min-width: 1024px) {
 .z-okl-marka { top: min(0.9375vw, 1.895vh) !important; left: max(24px, min(2.5vw, 5.05vh)) !important; gap: min(0.729vw, 1.474vh) !important; }
 .z-okl-marka .z-okl-logo { height: max(30px, min(2.083vw, 4.211vh)) !important; }
 .z-okl-marka > span:last-child { font-size: max(12px, min(0.729vw, 1.474vh)) !important; padding-left: min(0.729vw, 1.474vh) !important; }
 .z-okl-tytul { left: max(24px, min(2.5vw, 5.05vh)) !important; }
}`;
// (18 px = 0,9375vw przy 1920 / 1,895vh przy 950; 48 px = 2,5vw / 5,05vh; 14 px = 0,729vw / 1,474vh; 40 px = 2,083vw / 4,211vh)
// NIE objęte prototypem, do zrobienia: rząd czterech działów (.z-okl-dzialy, .z-okl-szkic, .z-okl-nazwa, .z-okl-dz .slot,
// .z-okl-liczby, .z-strzalka) — dziś clamp() od --h z górnymi limitami; przejść na tę samą skalę s, drobny tekst ≥ 13 px.

/* Wynik prototypu — miejsce łuku na wysokości środka pierwszej linii tytułu (% szerokości okna):
   okno        dziś   po zmianie   rozmiar „Instytut” po zmianie
   1024×700     45%      34%        81 px
   1180×820     40%      31%        85 px
   1280×600     34%      27%        78 px
   1536×730     30%      25%        84 px
   1920×950     25%      25%       105 px (bez zmian)
   2048×1040     —       25%       112 px
   2560×1300    20%      25%       140 px
   3440×1300     —       19%       143 px (ultrawide: ogranicza wysokość)
   3840×2000     —       25%       212 px */

/* PUNKT 2. Drugi ekran („Szybki dostęp”), pasek menu i stopka powiększone tą samą skalą, tylko gdy s > 1. */
const SKALA_DRUGIEGO_EKRANU = () => {
  function ustaw() {
    const k = Math.min(innerWidth / 1920, innerHeight / 950);
    document.querySelectorAll('.z-druga, .z-stopka, .z-pasek').forEach((e) => { e.style.zoom = k > 1 ? k : ''; });
    // min-height drugiego ekranu liczony od wysokości okna: przy zoom trzeba go podzielić przez k (inaczej podwaja się)
    const d = document.querySelector('.z-druga');
    if (d) d.style.minHeight = k > 1 ? `calc((100svh - 113px) / ${k})` : '';   // 113 px = --gora 66 + 47 z zalozyciele-strony.css:8
  }
  ustaw(); addEventListener('resize', ustaw);
};
// Wynik: 2560×1300 → zoom 1,33, dół stopki 1330 px (okno 1300); 3840×2000 → zoom 2, dół stopki 2061 px; bez przewijania w poziomie.
// DO DOŁOŻENIA: wyłączenie skali przy ręcznym powiększeniu strony (Ctrl +) — punkt 2 zlecenia; sprawdzenie animacji „Zobacz więcej”.

/* PUNKT 3. Pomiar wysokości drugiego ekranu (dziś, bez zmian): o ile dół stopki wychodzi poza okno (minus pasek 61 px):
   1280×600 +395 · 1366×620 +303 · 1440×780 +122 · 1536×730 +140 · 1707×830 −4 · 1920×950 −4.
   Części do odzyskania: stopka 71 px; „Warto wiedzieć” 113–137 px + odstęp 22; ostatnia pozycja krótkich kolumn ok. 71–96 px
   (wysokość krótkiej kolumny = wyższa z dwóch). Długa kolumna aktualności wypełnia wysokość lewej części sama. */
