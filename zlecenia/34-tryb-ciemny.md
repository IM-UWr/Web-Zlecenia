# Zlecenie 34: tryb ciemny „Granat z krawędzią” (17.11.2026)

**Decyzje właściciela (17.11, 21:56–22:28):**
- **Wybrany wariant B „Granat z krawędzią”** z artefaktu https://claude.ai/artifact/41X9sXaNLtLFwD2TQD2V5Z (zakładki „Warianty” i „Obok siebie”; zrzuty to wzorzec odbioru). Opis i diagnoza: `claude/tryb-ciemny.md`.
- **Poprawka do prototypu:** na telefonie grupy na stronach działów (Ludzie, Organizacja, Więcej…) zostają **osobnymi kafelkami**, jak dziś. W pierwszej wersji B zlewały się w jeden pas.
- **Tryb jasny bez zmian, co do piksela.**

**Decyzje domyślne (do zmiany na prośbę właściciela):**
- **Pasek przycisków (☀, EN, ☰) i „Szybki dostęp” zmieniają się tylko w trybie ciemnym**, bo jasny ma zostać bez zmian. Właściciel nie odpowiedział jeszcze, który pasek miał na myśli, więc oba wyglądają jak w prototypie.
- **Kolejność przycisków na telefonie zostaje (EN, ☀, ☰).** Gdyby zmienić ją tylko w ciemnym, przycisk pod palcem przeskakiwałby po przełączeniu motywu. Ujednolicenie z komputerem (☀, EN, ☰) wymaga zmiany także w jasnym, więc to osobna decyzja. Z tego samego powodu odstępy przycisków na okładce zostają.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- Najlepiej po zleceniu 32 (menu z hamburgera), bo oba ruszają pasek menu i `zalozyciele.css`.
- Raport `RAPORT-ZLECENIE-34.md`, zrzuty `raport-zrzuty/z34-*`. Bez subagentów.
- Numery linii poniżej pochodzą z `main` z 9.11 (`24c708e`) i mogły się przesunąć. Szukaj po selektorach.

## Jak wdrożyć
- W prototypie zmiany są nakładką na końcu stylów (załącznik niżej, tylko do porównania). **W kodzie zmieniaj reguły na miejscu, bez nakładki.**
- Każda nowa reguła stoi pod `:root[data-theme="dark"]`, więc tryb jasny się nie zmienia.
- Komentarze „Nocny granat” zamień na „Granat z krawędzią (zlecenie 34)”.

### 1. Tokeny ciemnego motywu
`src/styles/zalozyciele.css`, blok `:root[data-theme="dark"]` (ok. linii 45), który obowiązuje na komputerze i telefonie:

| token | dziś | nowa wartość |
|---|---|---|
| `--bg` | #18243b | **#172032** |
| `--surface` | #222e46 | **#202a3c** |
| `--pow-2` (nowy: powierzchnia o ton wyżej, najechanie) | — | **#2a3447** |
| `--line` | #3a465c | **#323b4b** |
| `--ink` | #e4eaf5 | **#ecf0f7** |
| `--text` | #ced5e3 | **#d1d6df** |
| `--muted` | #a5afc1 | **#a5abb7** |
| `--line-ui` | #727c8f | **#727986** |
| `--rule` | #7d8697 | **#585f6c** |
| `--panel` | #24324f | **#1d2b44** |
| `--tint`, `--tint-ink` | #222e46, #e4eaf5 | `var(--surface)`, `var(--ink)` |
| `--primary`, `--accent-ink`, `--uwr` | #ced5e3, #18243b, #e4eaf5 | `var(--text)`, `var(--bg)`, `var(--ink)` |
| `--d-a`, `--d-t` (poza działami) | #e4eaf5, #222e46 | `var(--ink)`, `var(--surface)` |

- **Dopisz do tego samego bloku:** `--photo: var(--surface); --minione-tlo: var(--surface); --minione-tekst: var(--muted); --footer-bg: #0d1830; --footer-text: var(--ink); --footer-muted: var(--muted); --footer-line: var(--line);`. Dziś te tokeny są w `global.css` (ok. linii 52). Sprawdź w przeglądarce, która definicja wygrywa, i zostaw jedną.
- **`telefon.css`** (ok. linii 158): `--znacznik: var(--pow-2); --znacznik-ink: var(--ink); --znacznik-tekst: var(--text);`. Wiersz `--tint-ink: #d3dcea` (linia 159) usuń, żeby obowiązywał `var(--ink)`.
- **`tlo.css`, linia 90** (`--kafel` #17223b): zamień na `var(--surface)` / `var(--line)` tylko wtedy, gdy któraś z klas z linii 91 (`.tile`, `.stat`, `.person`…) jest jeszcze na jakiejś stronie (sprawdź w zbudowanym HTML). Jeśli nie ma żadnej, nie ruszaj.

### 2. Kolory działów
- **Reguła `:root[data-theme="dark"] [data-dzial]:is(...)`** w `zalozyciele.css` (ok. linii 57) dostaje:
  - `--d-a: color-mix(in oklab, var(--d-j) 80%, var(--ink))`, co daje Instytut #e7b576, Nauka #82d3aa, Studia #77caf5, Popularyzacja #f0a4c7;
  - `--d-t: var(--surface)`;
  - nowy `--d-kafel: color-mix(in oklab, var(--d-j) 14%, var(--surface))` (kafelki na telefonie, punkt 4): #383b43, #293e49, #283d53, #3b384c.
- **Kolory wpisane na sztywno zamień na tokeny:**
  - `zalozyciele.css` ok. 64, `.akt-wydarzenie > *`: `--d-a: var(--ink); --d-t: var(--surface)`;
  - `src/components/zal/ListaPokaz.astro` ok. 53, `.lp-uklad`: to samo;
  - `zal-dzialy.css` ok. 36 (najechanie na stronę w pasie, komputer): `color-mix(in oklab, var(--d-a) 9%, var(--bg))` zamiast `… #18243b`;
  - `zal-dzialy.css` ok. 242 (telefon, `::before`): `color-mix(in oklab, var(--d-a) 14%, var(--d-kafel))`.

### 3. Krawędź banera (komputer i telefon)
- **`.z-nagl` w ciemnym:** `box-shadow: none`. Dziś to szara kreska `0 1px 0 var(--line)`; w jasnym zostaje.
- **Nowy `.z-nagl::after` w ciemnym:** `content: ''; position: absolute; left: 0; right: 0; bottom: 0; height: 2px; z-index: 4; pointer-events: none; background: color-mix(in srgb, var(--d-j) 80%, transparent)`.
- **Banery bez działu i granatowe** (`.z-nagl.z-granat`, `.z-nagl:not([data-dzial])`: Aktualności, wpisy, listy w ich stylu): `height: 1px; background: rgb(201 208 222 / .38)`.
- **`::after` na `.z-nagl`** nie jest dziś nigdzie używany. Sprawdź, czy nadal tak jest (np. po zleceniach 31–33).

### 4. Pas działu
- **Komputer** (`zal-dzialy.css`, `html.js .z-dz-karty`, ok. linii 159): w ciemnym `background: var(--surface); --ton: var(--pow-2); --kreska: var(--line); box-shadow: 0 1px 0 var(--line)`. Ta reguła tylko w `@media` komputera.
- **Telefon** (`zal-dzialy.css`, ok. 224 i 233):
  - w ciemnym kafelek grupy (`.z-dz-karta` bez `aria-expanded="true"`) i rozwinięte pole ze stronami (`html.js .z-dz .z-dz-rzad`) mają `background: var(--d-kafel)`;
  - odstęp 6 px między kafelkami zostaje, a kafelek otwarty wygląda jak dziś (`var(--d-a)`);
  - kontener `.z-dz-karty` na telefonie **nie ma tła**, przez co kafelki są osobne.

### 5. Szybki dostęp (`zalozyciele-strony.css`, `.z-skr`, ok. 18–23, telefon 166–169 i 239–242)
- **Kreski:** w ciemnym `border-top: 1px solid var(--line)` zamiast 2 px `var(--rule)` oraz `border-bottom: 1px solid var(--line)`.
- **Tło:** `background: var(--surface)`.
- **Nagłówek:** `h2` dostaje `padding-left: 18px`.
- **Najechanie na pole:** `var(--pow-2)`.

### 6. Pasek przycisków
- **Okładka** (`zalozyciele.css`, `.z-narz`, ok. 408–411): w ciemnym przyciski bez tła i bez rozmycia (`background: none; backdrop-filter: none`), z cieniem pod treścią:
  - dla tekstu `text-shadow: 0 1px 8px rgb(9 16 34 / .8)`;
  - dla ikon `filter: drop-shadow(0 1px 4px rgb(9 16 34 / .8))`;
  - odstępy, rozmiar i kolejność bez zmian.
- **Najechanie** na przycisk w `.z-pasek-narz`, `.z-narz` i `.hdr-tools`: `background: color-mix(in srgb, currentColor 12%, transparent); border-radius: 4px`.
- **Telefon:** w ciemnym hamburger bez kółka, czyli `background: transparent` w trzech miejscach:
  - `zal-telefon.css` ok. 52 (`.hdr .icon-btn.burger`) i ok. 57 (`.hdr.jasny …`);
  - `global.css` 158 (`.hdr.hdr-stopka … .burger`).

  Te reguły mają dziś `!important`, więc nowe muszą wygrać kolejnością albo szczegółowością, bez dokładania kolejnych `!important`, jeśli się da. Kolejność bez zmian (EN, ☀, ☰).

### 7. Plan zajęć (`zal-granty-plan.css`, linie 51 i 97)
- W ciemnym wybrany semestr i dzień: `background: color-mix(in oklab, var(--d-a) 16%, transparent); color: var(--ink); box-shadow: inset 0 -2px 0 var(--d-a)` zamiast pełnego wypełnienia kolorem działu.

## Odbiór lokalny
- **Zrzuty przed i po** (Playwright, `reducedMotion: 'reduce'`, ciekawostki ze stałym ziarnem losowania):
  - strony: `/`, drugi ekran strony głównej (Szybki dostęp), `/instytut/`, `/nauka/`, `/studia/`, `/popularyzacja/`, `/seminaria/`, `/aktualnosci/`, `/studia/plan-zajec/`, `/aktualnosci/2026-05-22-mirek-i-wrobel-frontiers-of-science-award/`;
  - ekrany 1536×864 i 390×844 (telefon z `isMobile`), u góry i po przewinięciu o 45% wysokości;
  - porównanie z artefaktem (wariant B): ma wyglądać tak samo, a kafelki działów na telefonie jak na zrzucie „B” po poprawce 22:28.
- **Tryb jasny:** te same zrzuty w jasnym przed i po zmianach są identyczne. Dopuszczalny tylko szum wygładzania (≤ 2/255) przy polu „Szukaj w aktualnościach” po przewinięciu, który pojawia się też między dwoma przebiegami bez zmian.
- **Wartości wyliczone** (`getComputedStyle`, ciemny):
  - `body` tło #172032;
  - Nauka: `--d-a` #82d3aa, `--d-kafel` #293e49;
  - kreska pod banerem Nauki: 2 px w kolorze działu;
  - pod banerem Aktualności: 1 px;
  - pole „Szybki dostęp” na #202a3c.
- **Kontrast** (ciemny, 9 stron × 2 szerokości):
  - każdy widoczny tekst poza banerami ≥ 4,5 : 1, a duży ≥ 3 : 1. W prototypie najsłabszy był „2 strony” na kafelku Popularyzacji na telefonie (5,84);
  - obrys pól `--line-ui` ≥ 3 : 1 na tle (3,72) i na powierzchni (3,29);
  - kafelek działu na telefonie odcina się od tła co najmniej jak dziś (1,44–1,46 : 1, dziś 1,40).
- **Przełączanie motywu:** na telefonie i na okładce komputera przyciski nie zmieniają położenia po kliknięciu ☀ (`getBoundingClientRect` przed i po).
- **Kontrole:** `astro check` bez nowych błędów, konsola czysta.
- **Stop:** raport ze zrzutami przed/po i czekanie na „push”.

## Kryteria odbioru
- [ ] Tokeny ciemnego motywu jak w tabeli; kolory działów i `--d-kafel` liczone z `color-mix`, bez kolorów wpisanych na sztywno w `ListaPokaz.astro`, `.akt-wydarzenie` i `zal-dzialy.css`.
- [ ] Baner kończy się kreską 2 px w kolorze działu (granatowe banery: 1 px jasna linia), bez szarej kreski; komputer i telefon.
- [ ] Pas działu na komputerze na powierzchni; na telefonie osobne kafelki z odcieniem działu, nie jeden pas.
- [ ] Szybki dostęp bez grubej kreski, na powierzchni.
- [ ] Przyciski na okładce bez kafelków, hamburger na telefonie bez kółka; nic nie przeskakuje po przełączeniu motywu.
- [ ] Plan zajęć: wybrany semestr i dzień z odcieniem i kreską zamiast jaskrawego wypełnienia.
- [ ] Wszystkie teksty ≥ AA w ciemnym; tryb jasny bez zmian (zrzuty identyczne).

## Załącznik: CSS prototypu B (nakładka użyta do zrzutów, tylko do porównania)
```css
/* ===== Wariant B „Granat z krawędzią” — tylko tryb ciemny ===== */
:root[data-theme="dark"] {
  --bg: #172032; --surface: #202a3c; --pow-2: #2a3447; --line: #323b4b;
  --ink: #ecf0f7; --text: #d1d6df; --muted: #a5abb7;
  --line-ui: #727986; --rule: #585f6c; --panel: #1d2b44;
  --tint: var(--surface); --tint-ink: var(--ink); --primary: var(--text); --accent-ink: var(--bg); --uwr: var(--ink);
  --photo: var(--surface); --minione-tlo: var(--surface); --minione-tekst: var(--muted);
  --footer-bg: #0d1830; --footer-text: var(--ink); --footer-muted: var(--muted); --footer-line: var(--line);
  --kafel: var(--surface); --kafel-ramka: var(--line);
  --znacznik: var(--pow-2); --znacznik-ink: var(--ink); --znacznik-tekst: var(--text);
  --d-a: var(--ink); --d-t: var(--surface);
}
html:root[data-theme="dark"] [data-dzial][data-dzial="instytut"] { --d-a: #e7b576; --d-t: #202a3c; }
html:root[data-theme="dark"] [data-dzial][data-dzial="nauka"] { --d-a: #82d3aa; --d-t: #202a3c; }
html:root[data-theme="dark"] [data-dzial][data-dzial="studia"] { --d-a: #77caf5; --d-t: #202a3c; }
html:root[data-theme="dark"] [data-dzial][data-dzial="popularyzacja"] { --d-a: #f0a4c7; --d-t: #202a3c; }
/* wpis o wydarzeniu i listy w stylu Aktualności: kolory poza działami z tokenów (zamiast #e4eaf5 / #222e46 na sztywno) */
:root[data-theme="dark"] .akt-wydarzenie > *, :root[data-theme="dark"] .lp-uklad { --d-a: var(--ink); --d-t: var(--surface); }
:root[data-theme="dark"] .z-dz-rzad a:is(:hover, :active, :focus-visible), :root[data-theme="dark"] .z-dz .z-dz-rzad a:is(:hover, :active, :focus-visible)::before { background-color: color-mix(in oklab, var(--d-a) 9%, var(--bg)); }
/* przejście banera w tło */
:root[data-theme="dark"] .z-nagl { box-shadow: none; }
:root[data-theme="dark"] .z-nagl::after { content: ''; position: absolute; left: 0; right: 0; bottom: 0; z-index: 4; height: 2px; pointer-events: none; background: color-mix(in srgb, var(--d-j) 80%, transparent); }
:root[data-theme="dark"] .z-nagl.z-granat::after, :root[data-theme="dark"] .z-nagl:not([data-dzial])::after { height: 1px; background: rgb(201 208 222 / .38); }
/* pas działu na komputerze: neutralna powierzchnia (pas tła pod kreską banera) */
@media (min-width: 1024px) and (min-height: 501px), (min-width: 1024px) and (pointer: fine) {
  html.js:root[data-theme="dark"] .z-dz-karty { --ton: var(--pow-2); --kreska: var(--line); background: var(--surface); box-shadow: 0 1px 0 var(--line); }
}
/* telefon: grupy działu jako osobne kafelki z odcieniem działu (jak dziś), pole ze stronami w tym samym kolorze */
html:root[data-theme="dark"] [data-dzial][data-dzial="instytut"] { --d-kafel: #383b43; }
html:root[data-theme="dark"] [data-dzial][data-dzial="nauka"] { --d-kafel: #293e49; }
html:root[data-theme="dark"] [data-dzial][data-dzial="studia"] { --d-kafel: #283d53; }
html:root[data-theme="dark"] [data-dzial][data-dzial="popularyzacja"] { --d-kafel: #3b384c; }
@media (max-width: 1023px), (max-height: 500px) and (pointer: coarse) {
  :root[data-theme="dark"] .z-dz-karta:not([aria-expanded="true"]), html.js:root[data-theme="dark"] .z-dz .z-dz-rzad { background: var(--d-kafel, var(--d-t)); }
  html.js:root[data-theme="dark"] .z-dz .z-dz-rzad a:is(:hover, :active, :focus-visible)::before { background-color: color-mix(in oklab, var(--d-a) 14%, var(--d-kafel, var(--d-t))); }
}
/* Szybki dostęp: jedna płyta na powierzchni, cienkie kreski */
:root[data-theme="dark"] .z-skr { border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); background: var(--surface); }
:root[data-theme="dark"] .z-skr h2 { padding-left: 18px; }
:root[data-theme="dark"] .z-skr a:hover { background: var(--pow-2); }
/* pasek przycisków: ten sam wygląd na pasku menu, okładce i telefonie */
:root[data-theme="dark"] .hdr .icon-btn.burger { background: transparent !important; }
/* kolejność i odstępy jak w trybie jasnym: przycisk pod palcem nie przesuwa się po przełączeniu motywu */
:root[data-theme="dark"] .z-narz :is(a, button) { background: none; -webkit-backdrop-filter: none; backdrop-filter: none; text-shadow: 0 1px 8px rgb(9 16 34 / .8); }
:root[data-theme="dark"] .z-narz svg:not(.z-flaga) { filter: drop-shadow(0 1px 4px rgb(9 16 34 / .8)); }
:root[data-theme="dark"] :is(.z-pasek-narz, .z-narz, .hdr-tools) > :is(a, button):hover { background: color-mix(in srgb, currentColor 12%, transparent) !important; border-radius: 4px; }
/* Plan zajęć: wybrany semestr i dzień bez jaskrawego wypełnienia — lekki odcień działu i kreska pod spodem */
:root[data-theme="dark"] .z-pl :is(.pl-sem, .pl-dni) button[aria-pressed="true"] { background: color-mix(in oklab, var(--d-a) 16%, transparent); color: var(--ink); box-shadow: inset 0 -2px 0 var(--d-a); }
```
