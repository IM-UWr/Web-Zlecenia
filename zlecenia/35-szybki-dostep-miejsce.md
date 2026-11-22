# Zlecenie 35: Szybki dostęp bez dziur: odstępy z limitem, kolumny „ile się zmieści” i „Ostatnio” (17.11.2026)

**Decyzja właściciela (17.11, 22:37):** wariant **D („B + Ostatnio”)** z artefaktu https://claude.ai/artifact/F2tKXowSoGVvpjCGwMxjA8 („wygląda bardzo dobrze”). Zrzuty wariantu D w artefakcie to wzorzec odbioru. Opis, przyczyny i pozostałe warianty: `claude/szybki-dostep-miejsce.md`.

**Decyzje domyślne (do zmiany na prośbę właściciela, który jeszcze ich wprost nie potwierdził):**
- „Ostatnio” pojawia się zawsze, gdy nadchodzące pozycje kolumny się skończą, a zostanie miejsce. Dotyczy to także kolumny z 3 lub więcej nadchodzącymi (np. 1100×1300 i 4K przy typowych danych). Minione pozycje nigdy nie są wymuszane do minimum 3 pozycji.
- Na oknie, które i tak się przewija (tryb 3), krótkie kolumny mają po 2 pozycje, jak w kroku 4 drabinki z D3.4.
- Napisy EN: „Recently in the calendar” i „Recent talks”.

**Zakres:** drugi ekran strony głównej w układzie komputerowym (`MQ_KOMPUTER`, od 1024 px), po polsku i angielsku. **Bez zmian:** telefon (poniżej 1024 px), okładka, skala k z D3.2, ręczne powiększanie (Ctrl +) i progi szerokości.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push na `main` dopiero po „push” właściciela.
- Raport `RAPORT-ZLECENIE-35.md`, zrzuty `raport-zrzuty/z35-*`. Bez subagentów.
- Najlepiej po zleceniu 34 (tryb ciemny zmienia wygląd Szybkiego dostępu), nie równolegle z nim.
- Numery linii poniżej pochodzą z `main` z 9.11 (`24c708e`) i mogły się przesunąć. Szukaj po selektorach i nazwach funkcji.

## Stan dziś (skąd biorą się dziury)
- `src/styles/zalozyciele-strony.css`:
  - l. 9: `.z-druga` ma `min-height` równe wysokości okna / k minus pasek minus 47 px;
  - l. 30: `.z-siatka` rośnie do tej wysokości (`flex: 1 0 auto`), a `align-content: space-between` oddaje całą nadwyżkę dwóm przerwom: kolumny → Studia i Studia → „Warto wiedzieć”, **bez górnej granicy**. Przy danych z 17.11 (1 wydarzenie, 0 referatów) przerwa ma 223 px na 1920×950, 320 px na 2560×1310 i 511 px na 3840×2030 (px okna);
  - l. 44 i 186: krótkie kolumny pokazują na sztywno 3 pozycje (z wyróżnionym wpisem 2), bez względu na wysokość okna;
  - l. 192–196: drabinka (`data-krok`). W krokach 2–4 Studia stoją przypięte do dołu pierwszego ekranu (`align-self: end`), a długa kolumna ma `grid-row: 1 / span 2` i wysokość okna. Skutek: dziura nad Studiami (1300×950 przy typowych danych: 239 px) i druga obok „Warto wiedzieć”, bo długa kolumna kończy się przed nim.
- `src/scripts/zal/drugi-ekran.ts`: `drabinka()` (l. 66) działa tylko przy k ≤ 1 (l. 81). Pozostałe funkcje: `liczWiecej()` (l. 35), `dopasujDluga()` (l. 106), `zamien()` (l. 140), `schowajZakonczone()` (l. 22).
- `src/components/zal/DrugiEkran.astro`: wydarzenia z `wydarzeniaNaTelefon(10, lang, 30)` (l. 54), referaty z `referatyWTygodniu` (l. 71: od dziś do dziś + 6 dni), 12 aktualności (l. 77).

## Część A. Układ: odstępy z limitem i kolumny „ile się zmieści”

1. **Siatka nie rozpycha rzędów.**
   - `.z-siatka`: `align-content: start`, `row-gap: 0`, `grid-template-rows: auto auto 1fr`; dalej `flex: 1 0 auto` w `.z-druga`.
   - Odstępy jako `margin-top` Studiów (`--z-g1`) i „Warto wiedzieć” (`--z-g2`), domyślnie 22 px. `.z-warto { align-self: start; }`.
   - Ostatni rząd bierze resztę wysokości, więc długa kolumna (rzędy 1–3) sięga do stopki i pokazuje więcej aktualności.
2. **Liczbę pozycji krótkich kolumn ustawia skrypt** atrybutem `hidden`.
   - Reguły `nth-child` z l. 44 i 186 zostają jako zapas bez JS, ale tylko dopóki skrypt nie ustawi trybu, np. `.z-druga:not([data-tryb]) .z-kolumna:not([data-slot="2"]) .z-w:nth-child(n+4) { display: none; }`. Ukryte pozycje: `.z-druga .z-w[hidden] { display: none !important; }`.
   - Telefon bez zmian.
3. **Stałe** na górze skryptu, z komentarzem, w px projektu (przed skalą k):
   - `G0 = 22`: odstęp nominalny;
   - `GPREF = 56`: krótkie kolumny dostają kolejne pozycje, dopóki odstępy między rzędami nie spadłyby poniżej tej wartości;
   - `GMAX = 88`: odstęp nigdy nie jest większy, nadwyżka zostaje pod „Warto wiedzieć”.
4. **`uloz()` zastępuje `drabinka()` i działa przy każdym k**, także k > 1 (2K, 4K).
   - **Pomiar** w trybie „miara” (klasa na `.z-druga`): bez `min-height`, siatka `flex: none`, krótkie kolumny `align-self: start`, żeby ich wysokość była wysokością treści. Wartości z `getBoundingClientRect` są w px okna, więc przy przeliczaniu na px CSS dziel przez k (jak dziś w `zamien()`).
   - **Tryby.** Wybierz pierwszy, który się mieści, najpierw przy minimum 3 nadchodzących pozycji na kolumnę (albo tylu, ile ich jest), potem przy 2:
     - 0: pasek, drugi ekran i stopka w oknie;
     - 1: stopka pod ekranem;
     - 2: „Warto wiedzieć” pod ekranem. W oknie mieszczą się pasek, Szybki dostęp, kolumny i Studia (do dołu Studiów plus dolny padding `.z-druga`). **Studia nie są przypinane do dołu ekranu;**
     - 3: nic się nie mieści: po 2 pozycje i zwykłe przewijanie.
   - **Dokładanie pozycji** w wybranym trybie. Każda krótka kolumna osobno dostaje kolejne pozycje, dopóki jej wysokość ≤ R:
     - R = wysokość wyższej krótkiej kolumny + (budżet − wysokość całości − rezerwa);
     - rezerwa = liczba odstępów (2 w trybach 0 i 1, 1 w trybie 2) × (GPREF − G0) × k.

     Krótsza kolumna dopełnia się więc do wysokości sąsiedniej bez kosztu.
   - **Odstępy:**
     - tryby 0 i 1: g1 = g2 = G0 + min(GMAX − G0, wolne / 2). `--z-druga-h` = (okno − pasek − stopka) / k w trybie 0, a (okno − pasek) / k w trybie 1;
     - tryb 2: g1 = G0 + min(GMAX − G0, wolne), g2 = G0 + reszta wolnego (więc „Warto wiedzieć” zaczyna się tuż pod dolną krawędzią okna), `--z-druga-h` = 0;
     - tryb 3: oba G0, `--z-druga-h` = 0.
   - **Zapis stanu:** `data-tryb` na `.z-druga` (zamiast `data-krok`) oraz zmienne `--z-g1`, `--z-g2` i `--z-druga-h`. Usuń reguły `data-krok` (l. 192–196) i `--z-siatka-h`.
5. **Kiedy liczyć:** jak dziś, czyli na starcie, po wczytaniu czcionek, przy `resize` i przy zmianie wysokości paska Szybkiego dostępu (kolor dnia). Do tego w `zamien()` po zamianie slotów, przed FLIP.
6. **„Zobacz więcej (N)”:** N to liczba ukrytych **nadchodzących** pozycji (minione się nie liczą). Przy N = 0 przycisk znika. W prototypie liczy to `pokaz(kolumna, n)`.
7. **Długa kolumna:** `dopasujDluga()` bez zmian dla nadchodzących. Minione (część B) pokazuje pod nimi, jeśli zostało miejsce (razem z nagłówkiem), a w przeciwnym razie ukrywa.

## Część B. „Ostatnio”: minione pozycje w wolnym miejscu krótkiej kolumny

8. **Dane z budowy** (`src/lib/tresci.ts`, nowe funkcje obok `wydarzeniaNaTelefon` i `referatyWTygodniu`):
   - `wydarzeniaMinione(lang, dni = 14, limit = 6)`: z `wszystkieWydarzenia()` bez rodzajów `referat` i `termin`. Zakończone w chwili budowy (`koniecIcs`, a gdy go brak `koniec` albo `poczatek`), z początkiem nie wcześniej niż dziś − 14 dni. Od najnowszego.
   - `referatyMinione(lang, dni = 14, limit = 6)`: referaty seminariów z listy (filtr jak w `referatyWTygodniu`), z datą od dziś − 14 do dziś − 1. Od najnowszego. Pola jak w `ReferatWLiscie`.
   - Liczbę dni i limit trzymaj jako stałe, ewentualnie w `ustawienia.json` obok `wydarzenia_dni_telefon`, bez pola w CMS.
9. **HTML** (`DrugiEkran.astro`). W `.pozycje` kolumn „wyd” i „sem”, po nadchodzących i po komunikacie `.z-pusto`:
   - nagłówek `<h3 class="z-ostatnio-h">`: „Ostatnio w kalendarzu” (wydarzenia) i „Ostatnie referaty” (seminaria); EN „Recently in the calendar” i „Recent talks”;
   - pod nim minione pozycje w tym samym wzorze wiersza (`a.z-w.minelo.z-przeszle`): data przygaszona, dział i kolor jak w nadchodzących, przy referatach prelegent;
   - wszystkie minione są w HTML z atrybutem `hidden` (bez JS ich nie widać). Nagłówek jest widoczny tylko razem z pierwszą widoczną minioną pozycją.
10. **Zasada:** minione pozycje pokazują się **tylko w wolnym miejscu**, po wszystkich nadchodzących danej kolumny, w ramach R z punktu 4. W kolejce stoją za nadchodzącymi, a nagłówek liczy się do wysokości. Nigdy nie zastępują nadchodzących i nie wchodzą do minimum 3 pozycji.
11. **Wygląd** (jak w prototypie):
    - nagłówek: 12 px, grubość 700, wersaliki, odstęp liter .04em, kolor `--muted`, padding 10 px 0 6 px, kreska `--line` pod spodem;
    - minione pozycje: tytuł w grubości 500 i kolorze `--text`, „dział · …” lekko przygaszony (opacity .8);
    - tryb ciemny przez tokeny.
12. **Wydarzenia, które skończą się w przeglądarce** (`schowajZakonczone()`): nie znikają, tylko przechodzą na początek „Ostatnio” (klasy `minelo z-przeszle`), po czym układ liczy się od nowa. Komunikat „Brak wydarzeń…” jak dziś, gdy nie zostało żadne nadchodzące.
13. **Telefon** (poniżej 1024 px): minione pozycje i nagłówek schowane. Telefon bez zmian.
14. **Dostępność:** nagłówek h3 w kolumnie; ukryte pozycje mają `hidden`, więc czytnik ich nie czyta; fokus i FLIP przy zamianie jak dziś.

## Kod i dokumentacja
- **Pliki:** `DrugiEkran.astro`, `drugi-ekran.ts`, `zalozyciele-strony.css`, `src/lib/tresci.ts`, ewentualnie `ustawienia.json`.
- **Prototyp** (załączniki A i B) to nakładka na zbudowaną stronę i podmieniony moduł. W kodzie zmieniaj reguły na miejscu, bez nakładki. W prototypie nagłówek „Ostatnio…” to `::before` pierwszej minionej pozycji, a w kodzie ma być osobnym elementem (punkt 9).
- **Dokumentacja:** komentarze w nagłówkach plików i `dok/estetyka.md` (rozdział „Drugi ekran”). Opisz zmianę D3.4: drabinka bez przypinania Studiów, kolumny dopełniane pozycjami.

## Odbiór lokalny
**Narzędzia**
- Playwright, strona zbudowana i serwowana lokalnie, adres z `#szybki-dostep` (bez okładki).
- Pomiar pustych miejsc: załącznik C (`pomiar.js`, `page.evaluate`). „Dziura” to pusty pas wyższy niż 100 px × k, bez pasa pod „Warto wiedzieć”.
- Scenariusze danych: załącznik D (`dane-odbior.py`). Przekształca zbudowany `index.html` (podmieniany przez `page.route`) i zostawia minione pozycje z budowy. „Mało” to dane z budowy.

**Okna** (px CSS): 1280×590, 1366×638, 1536×734, 1920×950, 2560×1310 (to także 3840×2160 przy 150%), 1707×830, 3840×2030, 1024×950, 1150×950, 1300×950, 1100×1300.

**Macierz przed i po:** 11 okien × 3 scenariusze, zrzuty całej strony i tabela największych dziur. Wzorzec to prototyp D:

| okno (px CSS) | mało: dziś → D | typowo: dziś → D | dużo: dziś → D | tryb D (mało/typowo/dużo) | D, mało: wyd · sem | D, typowo: wyd · sem · akt |
|---|---|---|---|---|---|---|
| 1280×590 | 226 → 127 | 236 → — | 219 → — | 2/3/3 | 1/1 · 0/0 | 2/4 · 2/5 · 9/12 |
| 1366×638 | 215 → 161 | 212 → — | 195 → — | 2/3/3 | 1/1 · 0/0 | 2/4 · 2/5 · 8/12 |
| 1536×734 | 102 → 102 | 222 → — | 222 → 121 | 0/2/2 | 1/1 · 0/0 | 4/4 · 3/5 · 9/12 |
| 1920×950 | 223 → 112 | 140 → 118 | 123 → 122 | 0/0/0 | 4/1 · 2/0 | 4/4 · 3/5 · 10/12 |
| 2560×1310 | 320 → — | 212 → — | 188 → — | 0/0/0 | 5/1 · 3/0 | 5/4 · 4/5 · 10/12 |
| 1707×830 | 172 → — | — → — | — → — | 0/1/1 | 2/1 · 1/0 | 3/4 · 3/5 · 9/12 |
| 3840×2030 | 511 → — | 345 → 209 | 310 → — | 0/0/0 | 5/1 · 3/0 | 5/4 · 5/5 · 11/12 |
| 1024×950 | 151 → 151 | 278 → 108 | 264 → 142 | 0/2/2 | 1/1 · 0/0 | 3/4 · 2/5 · 7/12 |
| 1150×950 | 181 → 181 | 192 → 112 | 192 → — | 0/2/2 | 1/1 · 0/0 | 4/4 · 3/5 · 7/12 |
| 1300×950 | 176 → 161 | 239 → — | 239 → — | 0/2/2 | 1/1 · 0/0 | 5/4 · 4/5 · 11/12 |
| 1100×1300 | 358 → 156 | 194 → — | 184 → 174 | 0/0/0 | 5/1 · 3/0 | 5/4 · 4/5 · 9/12 |

Wartości to px okna; „—” znaczy brak dziury. „x/y” to pozycje widoczne / nadchodzące w kolumnie (widoczne obejmują minione). Tolerancja: ±15 px albo jedna pozycja. Wartości „mało” zależą od dnia budowy: minione pozycje z 14 dni i wydarzenia, które się skończyły.

**Pozostałe sprawdzenia**
- **1920×950, typowo:** Studia i „Warto wiedzieć” w tym samym miejscu co dziś (±2 px), odstępy 74–86 px. Jedyna różnica to czwarte wydarzenie zamiast „Zobacz więcej (1)”.
- **„Ostatnio”:**
  - przy danych z 17.11 na 1920×950, 2560×1310 i 3840×2030 kolumny są pełne jak w artefakcie;
  - w scenariuszu „dużo” „Ostatnio” się nie pokazuje;
  - test z zegarem Playwright (`page.clock`): wydarzenie kończy się przy otwartej stronie i przechodzi do „Ostatnio”.
- **Zamiana kolumn „Zobacz więcej”** w trybach 0, 1 i 2 (np. 1920×950, 1707×830, 1300×950), z ruchem i bez:
  - fokus na nagłówku;
  - po zamianie nie ma nowych dziur;
  - minione pozycje w długiej kolumnie stoją pod nadchodzącymi.
- **Ctrl + 125%, 150% i 200%** na 1920×950: działa jak dziś (skala wyłączona), nic na siebie nie zachodzi. Przy dużym powiększeniu tryb 3 (przewijanie).
- **Zmiana rozmiaru okna na żywo** (1920 → 1024 → 1920): układ wraca do tego samego stanu.
- **EN** (`/en/#szybki-dostep`): napisy „Recently in the calendar” i „Recent talks”.
- **Tryb ciemny:** zrzuty 1920×950 i 2560×1310 bez regresji.
- **Telefon** 390 i 768 px: 0 różnic (porównanie pikselowe).
- **Bez JS:** krótkie kolumny po 3 pozycje jak dziś, minione schowane.
- **Na koniec:** `astro check` bez nowych błędów, konsola czysta. **Stop**, raport, czekanie na „push”.

## Kryteria odbioru
- [ ] Odstępy między rzędami (`--z-g1`, `--z-g2`) nie przekraczają 88 px projektu (× k na ekranie), poza trybem 2, w którym „Warto wiedzieć” zaczyna się pod dolną krawędzią okna. Nadwyżka wysokości jest pod „Warto wiedzieć”, a długa kolumna sięga do stopki.
- [ ] Krótkie kolumny pokazują tyle pozycji, ile się zmieści (co najmniej 3 nadchodzące, na niskim oknie 2). „Zobacz więcej (N)” liczy tylko nadchodzące.
- [ ] Studia nigdy nie są przypinane do dołu ekranu. Kolejność ustępowania: stopka, „Warto wiedzieć”, 2 pozycje, przewijanie.
- [ ] „Ostatnio” pojawia się tylko w wolnym miejscu, po polsku i angielsku, z nagłówkiem. Zakończone wydarzenia przechodzą do „Ostatnio”.
- [ ] 1920×950 wygląda jak dziś (poza czwartym wydarzeniem), a macierz mieści się w tolerancji wobec tabeli.
- [ ] Telefon: 0 różnic. Ctrl + działa, tryb ciemny bez regresji.

## Załączniki (tylko do porównania i odbioru)

### A. CSS prototypu (nakładka na zbudowaną stronę)
Selektory z `html[data-wariant]` działały tylko w prototypie. W kodzie reguły trafiają na miejsce w `zalozyciele-strony.css`.

```css
/* ===== Warianty „Szybkiego dostępu” — wspólna podstawa (prototyp, nakładany na zbudowaną stronę) =====
   Siatka już nie rozpycha rzędów: rzędy stoją od góry, odstępy między nimi (--z-g1: kolumny → Studia, --z-g2: Studia → Warto wiedzieć)
   liczy skrypt wariantu (z górnym limitem), liczbę pozycji krótkich kolumn też. Drabinka ze strony (data-krok) nie działa, bo skrypt
   wariantu zastępuje moduł drugiego ekranu. Telefon (< 1024 px) bez zmian. */
@media (min-width: 1024px) and (min-height: 501px), (min-width: 1024px) and (pointer: fine) {
  html[data-wariant] .z-druga { min-height: var(--z-druga-h, calc(100svh / var(--z-k, 1) - var(--gora) - 47px)); }
  html[data-wariant] .z-siatka { align-content: start; row-gap: 0; grid-template-rows: auto auto auto; }
  html[data-wariant] .z-studia { margin-top: var(--z-g1, 22px); }
  html[data-wariant] .z-warto { margin-top: var(--z-g2, 22px); }
  /* liczbę widocznych pozycji krótkich kolumn ustawia skrypt (atrybut hidden), nie CSS */
  html[data-wariant] .z-kolumna:not([data-slot="2"]) .z-w:nth-child(n+4),
  html[data-wariant] .z-kolumna:not([data-slot="2"]) .pozycje:has(> .z-w.wyr) > .z-w:nth-child(n+3) { display: grid; }
  html[data-wariant] .z-druga .z-w[hidden] { display: none !important; }
  /* pomiar (skrypt): bez rozciągania */
  html[data-wariant] .z-druga.z-miara { min-height: 0 !important; }
  html[data-wariant] .z-druga.z-miara .z-siatka { flex: none; }
  html[data-wariant] .z-druga.z-miara .z-kolumna:not([data-slot="2"]) { align-self: start; }
  /* „Ostatnio” (wariant D): minione pozycje pod nadchodzącymi, przygaszone, z podpisem nad pierwszą */
  html[data-wariant] .z-w.z-przeszle .t { font-weight: 500; color: var(--text); }
  html[data-wariant] .z-w.z-przeszle .gdzie { opacity: .8; }
  html[data-wariant] .z-w.z-przeszle.z-pierwsza-przeszla { border-top: 0; }
  html[data-wariant] .z-w.z-przeszle.z-pierwsza-przeszla::before { content: attr(data-podpis); grid-column: 1 / -1; padding: 10px 0 6px; margin-bottom: 4px;
    border-bottom: 1px solid var(--line); font-size: 12px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; color: var(--muted); }
  html[data-wariant] .z-kolumna:not(.z-ostatnio-wl) .z-w.z-przeszle { display: none !important; }
}

/* B: ostatni rząd (Warto wiedzieć) bierze resztę wysokości, więc długa kolumna sięga do stopki i pokazuje więcej aktualności */
@media (min-width: 1024px) and (min-height: 501px), (min-width: 1024px) and (pointer: fine) {
  html[data-wariant] .z-siatka { grid-template-rows: auto auto 1fr; }
  html[data-wariant] .z-warto { align-self: start; }
}
```

### B. Skrypt prototypu D (zamiast modułu drugiego ekranu)
Importy wskazują pliki zbudowanej strony z 17.11 (`daty`, `media`). W kodzie zasady trafiają do `src/scripts/zal/drugi-ekran.ts`.

```js
// Prototyp wariantu D (B + „Ostatnio”) — moduł drugiego ekranu użyty w artefakcie „Odstępy w Szybkim dostępie” zamiast
// src/scripts/zal/drugi-ekran.ts (podmieniony w zbudowanej stronie). Tylko do porównania: w kodzie przenieś zasady do drugi-ekran.ts.
import { n as now, t as today, h as hasTime } from './daty.uoFrWalC.js';
import { M as MQ_TELEFON } from './media.BXCVDSPC.js';

const siatka = document.querySelector('[data-z-siatka]');
const druga = siatka?.closest('.z-druga') ?? null;
const TELEFON = matchMedia(MQ_TELEFON);
const RYTM = 'cubic-bezier(.22, .8, .2, 1)';
const rt = document.documentElement;
// odstępy w px projektu (przed skalą k): nominalny, najmniejszy przy dokładaniu pozycji, największy
const G0 = 22, GPREF = 56, GMAX = 88;

const kolumny = () => Array.from(siatka.querySelectorAll('.z-kolumna'));
const krotkie = () => kolumny().filter((k) => k.dataset.slot !== '2');
const wys = (e) => (e ? e.getBoundingClientRect().height : 0);
const zoomK = () => parseFloat(getComputedStyle(rt).getPropertyValue('--z-k')) || 1;

function schowajZakonczone() {
  const kol = siatka?.querySelector('.z-kolumna[data-key="wyd"]');
  if (!kol) return;
  const n = now(), d = today();
  kol.querySelectorAll('[data-koniec]').forEach((w) => {
    const koniec = w.dataset.koniec || '';
    if (koniec && (hasTime(koniec) ? koniec < n : koniec < d)) w.remove();
  });
  if (!kol.querySelector('.z-w:not(.z-przeszle)')) kol.querySelector('.z-pusto')?.removeAttribute('hidden');
}

// pozycje kolumny: nadchodzące, potem minione („Ostatnio”, klasa z-przeszle)
const nadch = (k) => Array.from(k.querySelectorAll('.z-w:not(.z-przeszle)'));
const pozycje = (k) => Array.from(k.querySelectorAll(k.classList.contains('z-ostatnio-wl') ? '.z-w' : '.z-w:not(.z-przeszle)'));
const widac = (k) => pozycje(k).filter((w) => !w.hidden).length;
function pokaz(k, n) {
  pozycje(k).forEach((w, i) => { w.hidden = i >= n; });
  const b = k.querySelector('.z-wiecej');
  if (b) {
    // N liczy tylko nadchodzące
    const ukryte = nadch(k).filter((w) => w.hidden).length;
    const ik = b.querySelector('.z-ile-k');
    if (ik) ik.textContent = String(ukryte);
    b.hidden = !ukryte;
  }
}

function wyrownajKreski() {
  const h = Array.from(siatka.querySelectorAll('.z-kolumna > .z-h'));
  h.forEach((e) => { e.style.minHeight = ''; });
  if (TELEFON.matches) return;
  const ws = h.map((e) => e.getBoundingClientRect().height), max = Math.max(...ws);
  if (ws.some((x) => x < max - 0.5)) h.forEach((e) => { e.style.minHeight = `${max}px`; });
}

// Tryby: 0 — wszystko ze stopką w oknie; 1 — stopka pod ekranem; 2 — „Warto wiedzieć” pod ekranem (Studia NIE są przypinane);
// 3 — nie mieści się nawet z 2 pozycjami: zwykłe przewijanie z 2 pozycjami (jak krok 4 drabinki).
function uloz() {
  if (!siatka || !druga) return;
  const pasek = document.querySelector('.z-pasek-jasny'), stopka = document.querySelector('.z-stopka');
  const studia = siatka.querySelector('.z-studia');
  const kk = krotkie();
  druga.style.removeProperty('--z-druga-h'); druga.style.removeProperty('--z-g1'); druga.style.removeProperty('--z-g2');
  delete druga.dataset.tryb;
  wyrownajKreski();
  if (TELEFON.matches) { kk.forEach((k) => pozycje(k).forEach((w) => { w.hidden = false; })); return; }
  kk.forEach((k) => {
    k.classList.toggle('z-ostatnio-wl', !!k.querySelector('.z-przeszle'));
    // w prototypie podpis „Ostatnio…” to ::before pierwszej minionej pozycji; w kodzie osobny element (zlecenie, punkt 9)
    k.querySelectorAll('.z-przeszle').forEach((w, i) => { w.classList.toggle('z-pierwsza-przeszla', i === 0); w.dataset.podpis = k.dataset.key === 'sem' ? 'Ostatnie referaty' : 'Ostatnio w kalendarzu'; });
  });
  const k = zoomK();
  const H = rt.clientHeight, P = wys(pasek), F = wys(stopka);
  const pad = parseFloat(getComputedStyle(druga).paddingBottom) * k;
  druga.classList.add('z-miara');
  const dt = () => druga.getBoundingClientRect().top;
  const naturalna = () => wys(druga);
  const doStudiow = () => studia.getBoundingClientRect().bottom - dt() + pad;
  const TRYBY = [
    { id: 0, budzet: H - P - F, miara: naturalna, odstepy: 2 },
    { id: 1, budzet: H - P, miara: naturalna, odstepy: 2 },
    { id: 2, budzet: H - P, miara: doStudiow, odstepy: 1 },
  ];
  const rezerwa = (t) => t.odstepy * (GPREF - G0) * k;
  let wybor = null;
  for (const minimum of [3, 2]) {
    for (const t of TRYBY) {
      // minimum liczy tylko nadchodzące: minione („Ostatnio”) nigdy nie są wymuszane
      kk.forEach((c) => pokaz(c, Math.min(nadch(c).length, minimum)));
      if (t.miara() > t.budzet + 1) continue;
      // kolumny obok siebie: każda niezależnie dostaje tyle pozycji, ile zmieści się w wysokości rzędu R
      // (rząd może urosnąć o wolne miejsce ponad rezerwę na odstępy GPREF)
      const R = Math.max(...kk.map(wys)) + (t.budzet - t.miara() - rezerwa(t));
      for (const c of kk) {
        for (let n = widac(c); n < pozycje(c).length; n++) {
          pokaz(c, n + 1);
          if (wys(c) > R + 0.5) { pokaz(c, n); break; }
        }
      }
      wybor = t; break;
    }
    if (wybor) break;
  }
  if (!wybor) { kk.forEach((c) => pokaz(c, Math.min(nadch(c).length, 2))); wybor = { id: 3, budzet: 0, miara: naturalna, odstepy: 0 }; }
  const luz = Math.max(0, (wybor.budzet - wybor.miara()) / k);
  druga.classList.remove('z-miara');
  druga.dataset.tryb = String(wybor.id);
  if (wybor.id <= 1) {
    // odstępy rosną z wolnym miejscem, najwyżej do GMAX; reszta zostaje pod „Warto wiedzieć” (długa kolumna sięga do stopki)
    const g = G0 + Math.min(GMAX - G0, luz / 2);
    druga.style.setProperty('--z-g1', `${g}px`); druga.style.setProperty('--z-g2', `${g}px`);
    druga.style.setProperty('--z-druga-h', `${(wybor.id === 0 ? H - P - F : H - P) / k}px`);
  } else if (wybor.id === 2) {
    // pierwszy ekran: odstęp kolumny → Studia do GMAX, reszta przed „Warto wiedzieć”, które zaczyna się pod dolną krawędzią okna
    const g1 = G0 + Math.min(GMAX - G0, luz);
    druga.style.setProperty('--z-g1', `${g1}px`); druga.style.setProperty('--z-g2', `${G0 + luz - (g1 - G0)}px`);
    druga.style.setProperty('--z-druga-h', '0px');
  } else {
    druga.style.setProperty('--z-druga-h', '0px');
  }
}

function dopasujDluga() {
  if (!siatka || !siatka.offsetHeight || TELEFON.matches) return;
  const kol = siatka.querySelector('.z-kolumna[data-slot="2"]');
  if (!kol) return;
  const box = kol.querySelector('.pozycje'), link = kol.querySelector('.reszta');
  if (!box || !link) return;
  const wiersze = Array.from(box.querySelectorAll('.z-w:not(.z-przeszle)'));
  wiersze.forEach((w) => { w.hidden = false; });
  const limit = box.clientHeight;
  let ukryte = 0;
  wiersze.forEach((w) => { if (ukryte || w.offsetTop - box.offsetTop + w.offsetHeight > limit + 1) { w.hidden = true; ukryte++; } });
  link.textContent = ukryte ? `${(link.dataset.wiecej || '{n}').replace('{n}', String(ukryte))} · ${link.dataset.wsz}` : link.dataset.wsz || '';
}

function dalej() {
  siatka?.querySelectorAll('.z-w.wyr .zaj').forEach((z) => {
    const d = z.querySelector('.dalej');
    const ucieta = !TELEFON.matches && z.scrollHeight > z.clientHeight + 1;
    if (ucieta && !d) { const s = document.createElement('span'); s.className = 'dalej'; s.setAttribute('aria-hidden', 'true'); s.textContent = siatka.dataset.dalej ?? ''; z.append(s); }
    else if (!ucieta && d) d.remove();
  });
}

function zamien(key) {
  if (TELEFON.matches) {
    const kol = siatka.querySelector(`.z-kolumna[data-key="${key}"]`);
    kol?.classList.add('z-rozwin');
    kol?.querySelector('.z-h h2')?.focus({ preventScroll: true });
    return;
  }
  const kliknieta = siatka.querySelector(`.z-kolumna[data-key="${key}"]`), dluga = siatka.querySelector('.z-kolumna[data-slot="2"]');
  if (!kliknieta || !dluga || kliknieta === dluga) return;
  const stare = new Map(kolumny().map((el) => [el, el.getBoundingClientRect()]));
  const slot = kliknieta.dataset.slot;
  kliknieta.dataset.slot = '2'; dluga.dataset.slot = slot;
  kliknieta.querySelectorAll('.z-w').forEach((w) => { w.hidden = false; });
  uloz(); dopasujDluga();
  kliknieta.querySelector('.z-h h2')?.focus({ preventScroll: true });
  const bezRuchu = matchMedia('(prefers-reduced-motion: reduce)').matches, k = zoomK();
  for (const el of [kliknieta, dluga]) {
    const o = stare.get(el), n = el.getBoundingClientRect();
    if (bezRuchu) { el.animate([{ opacity: 0.55 }, { opacity: 1 }], { duration: 150, easing: RYTM }); continue; }
    el.animate([{ transform: `translate(${(o.left - n.left) / k}px, ${(o.top - n.top) / k}px)` }, { transform: 'none' }], { duration: 350, easing: RYTM });
  }
}

function wszystko() { uloz(); dopasujDluga(); dalej(); }

if (siatka) {
  schowajZakonczone();
  wszystko();
  siatka.querySelectorAll('.z-wiecej').forEach((b) => b.addEventListener('click', () => zamien(b.dataset.key || '')));
  new ResizeObserver(() => { dopasujDluga(); dalej(); }).observe(siatka);
  addEventListener('resize', () => requestAnimationFrame(wszystko));
  document.fonts?.ready.then(() => requestAnimationFrame(wszystko));
}
```

### C. pomiar.js (puste miejsca; `page.evaluate`)
Zwraca przerwy (`przerwy`: l, t, w, h, czy na dole, element nad i pod), skalę k, tryb, liczbę ekranów i widoczne pozycje. Dziura to przerwa wyższa niż 100 px × k, z wyjątkiem pasa pod „Warto wiedzieć” albo Studiami (`dol` i `nad` = `warto`/`studia`).

```js
() => {
  // Puste miejsca: w każdym pionowym pasie (krawędzie kolumn, Studiów, Warto wiedzieć) szukamy pionowych przerw między treścią
  // większych niż próg (44 px przy skali 1), od dołu paska „Szybki dostęp” do górnej krawędzi stopki.
  const k = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--z-k')) || 1;
  const sy = scrollY;
  const R = (e) => { const b = e.getBoundingClientRect(); return { l: b.left, t: b.top + sy, r: b.right, b: b.bottom + sy }; };
  const SEK = (e) => { const k = e.closest('.z-kolumna'); if (k) return (k.dataset.slot === '2' ? 'dluga:' : 'krotka:') + k.dataset.key; if (e.closest('.z-studia')) return 'studia'; if (e.closest('.z-warto')) return 'warto'; if (e.closest('.z-skr')) return 'pasek'; return '?'; };
  const vis = (e) => e.getClientRects().length > 0 && e.getBoundingClientRect().height > 0 && getComputedStyle(e).visibility !== 'hidden';
  const druga = document.querySelector('.z-druga'), stopka = document.querySelector('.z-stopka'), skr = document.querySelector('.z-skr');
  const LISC = '.z-skr, .z-kolumna > .z-h, .z-w, .z-wiecej, .reszta, .z-pusto, .z-studia > div, .z-studia > .z-kier, .z-warto > .z-h, .z-warto .rzad, .z-blok';
  const liscie = [...druga.querySelectorAll(LISC)].filter(vis).map((e) => ({ ...R(e), s: SEK(e) }));
  const pojemniki = [...druga.querySelectorAll('.z-kolumna, .z-studia, .z-warto')].filter(vis).map(R);
  const gora = R(skr).b, dol = stopka && vis(stopka) ? R(stopka).t : R(druga).b;
  const xs = [...new Set(pojemniki.flatMap((p) => [Math.round(p.l), Math.round(p.r)]))].sort((a, b) => a - b);
  const T = 44 * k, przerwy = [];
  for (let i = 0; i + 1 < xs.length; i++) {
    const x0 = xs[i], x1 = xs[i + 1];
    if (x1 - x0 < 100 * k) continue;
    if (!pojemniki.some((p) => p.l <= x0 + 2 && p.r >= x1 - 2)) continue;
    const el = liscie.filter((e) => Math.min(e.r, x1) - Math.max(e.l, x0) > 20).sort((a, b) => a.t - b.t);
    let cur = gora, nad = 'pasek';
    for (const e of el) { if (e.t - cur > T) przerwy.push({ l: x0, r: x1, t: cur, b: e.t, nad, pod: e.s }); if (e.b >= cur) nad = e.s; cur = Math.max(cur, e.b); }
    if (dol - cur > T) przerwy.push({ l: x0, r: x1, t: cur, b: dol, dol: true, nad, pod: 'stopka' });
  }
  // sklejanie sąsiednich pasów o tej samej wysokości
  przerwy.sort((a, b) => a.t - b.t || a.l - b.l);
  const scal = [];
  for (const p of przerwy) {
    const q = scal.find((q) => Math.abs(q.t - p.t) < 3 && Math.abs(q.b - p.b) < 3 && p.l - q.r < 60);
    if (q) { q.r = Math.max(q.r, p.r); q.l = Math.min(q.l, p.l); } else scal.push({ ...p });
  }
  const obszar = (dol - gora) * (R(druga).r - R(druga).l - 2 * 48 * k);
  const pole = scal.reduce((s, p) => s + (p.r - p.l) * (p.b - p.t), 0);
  const kol = {};
  druga.querySelectorAll('.z-kolumna').forEach((c) => { kol[c.dataset.key] = [...c.querySelectorAll('.z-w')].filter(vis).length + '/' + c.querySelectorAll('.z-w:not(.z-przeszle)').length; });
  const r = (v) => Math.round(v);
  return {
    k, krok: druga.dataset.krok || druga.dataset.tryb || null, okno: [innerWidth, innerHeight], wys: document.documentElement.scrollHeight,
    stron: Math.round(document.documentElement.scrollHeight / innerHeight * 100) / 100,
    przerwy: scal.map((p) => ({ l: r(p.l), t: r(p.t), w: r(p.r - p.l), h: r(p.b - p.t), dol: !!p.dol, nad: p.nad, pod: p.pod })),
    bloki: Object.fromEntries([...druga.querySelectorAll('.z-kolumna, .z-studia, .z-warto, .z-skr')].filter(vis).map((e) => [e.dataset.key || e.className.split(' ')[0], (({ l, t, r: rr, b }) => [r(l), r(t), r(rr - l), r(b - t)])(R(e))])),
    sk: r(sy),
    puste_proc: Math.round(pole / obszar * 1000) / 10,
    max_przerwa: r(Math.max(0, ...scal.filter((p) => !p.dol).map((p) => p.b - p.t))),
    dol_przerwa: r(Math.max(0, ...scal.filter((p) => p.dol).map((p) => p.b - p.t))),
    widac: kol,
    stopka_t: stopka ? r(R(stopka).t) : null,
  };
}
```

### D. dane-odbior.py (scenariusze danych)
Python 3 z BeautifulSoup. Użycie: `html = przeksztalc(open('index.html').read(), 'typowo')`, potem `page.route(...)` z tym HTML-em.

```python
"""Scenariusze danych do odbioru zlecenia 35: przekształcenie zbudowanego index.html (Python 3, BeautifulSoup).

przeksztalc(html, 'malo')   – bez zmian (dane z budowy);
przeksztalc(html, 'typowo') – 4 wydarzenia, 5 referatów, 12 aktualności;
przeksztalc(html, 'duzo')   – 10 wydarzeń, 14 referatów, 20 aktualności (13–20 to kopie starszych wpisów).
Dodane wiersze to prawdziwe pozycje z archiwum kalendarza z przesuniętymi datami (tydzień 17–23 listopada 2026).
Minione pozycje („Ostatnio”) z budowy zostają na swoim miejscu, pod nadchodzącymi.
"""
import copy
from bs4 import BeautifulSoup

PULE = {'sem': [
 {
  "t": "Dimension dependence and dimension-free $\\ell^2$ estimates for variation seminorms of spherical means on the hypercube",
  "kto": "Rafał Łyżwa",
  "sem": "Analiza harmoniczna i rozwinięcia ortogonalne",
  "godz": "1015",
  "sala": "sala 601"
 },
 {
  "t": "Multilinear singular integral operators with rough kernels",
  "kto": "Lenka Slavíková",
  "sem": "Analiza harmoniczna i rozwinięcia ortogonalne",
  "godz": "1015",
  "sala": "sala 601"
 },
 {
  "t": "Crystallization and K-theoretical aspects of the quantum twistor bundle",
  "kto": "Suvrajit Bhattacharjee",
  "sem": "Dyskretna analiza harmoniczna i niekomutatywna probabilistyka",
  "godz": "1015",
  "sala": "sala 604"
 },
 {
  "t": "Kwantowe grafy Knesera",
  "kto": "Igor Chełstowski",
  "sem": "Dyskretna analiza harmoniczna i niekomutatywna probabilistyka",
  "godz": "1015",
  "sala": "sala 604"
 },
 {
  "t": "Local functional equations for polynomials and related topics",
  "kto": "Takeyoshi Kogiso",
  "sem": "Dyskretna analiza harmoniczna i niekomutatywna probabilistyka",
  "godz": "0900",
  "sala": "D1.2, budynek C-16, Politechnika Wrocławska"
 },
 {
  "t": "Flexible Multivariate Skew Distributions via Coordinate-wise and Spectral Gaussian Mixtures",
  "kto": "Tomasz J. Kozubowski",
  "sem": "Teoria prawdopodobieństwa i modelowanie stochastyczne",
  "godz": "1315",
  "sala": "sala 603"
 },
 {
  "t": "From Atmospheric Rivers to Flood Risk: A Multivariate Model for Extreme Precipitation",
  "kto": "Anna K. Panorska",
  "sem": "Teoria prawdopodobieństwa i modelowanie stochastyczne",
  "godz": "1215",
  "sala": "sala 603"
 },
 {
  "t": "PDE models of diffusion: linear and nonlinear, local and nonlocal",
  "kto": "Juan Luis Vázquez",
  "sem": "Równania różniczkowe",
  "godz": "1515",
  "sala": "sala HS"
 },
 {
  "t": "Rozwiązania automorficzne (self-similar) równań konwekcji-dyfuzji",
  "kto": "Grzegorz Karch",
  "sem": "Równania różniczkowe",
  "godz": "1515",
  "sala": "sala 603"
 },
 {
  "t": "Rozwiązania automorficzne (self-similar) równań konwekcji-dyfuzji",
  "kto": "Grzegorz Karch",
  "sem": "Równania różniczkowe",
  "godz": "1515",
  "sala": "sala 605"
 },
 {
  "t": "A Schauder regularity theory for nonlocal viscous Hamilton–Jacobi equations",
  "kto": "Robin Østern Lien",
  "sem": "Równania różniczkowe",
  "godz": "1515",
  "sala": "sala 605"
 },
 {
  "t": "Long time behaviour of mean field games with fractional diffusion",
  "kto": "Espen Jakobsen",
  "sem": "Równania różniczkowe",
  "godz": "1515",
  "sala": "sala 605"
 },
 {
  "t": "From Structured Sparsity to Causal Effects: GSLOPE, PCGLASSO, and SLOPE-Based Doubly Robust Inference",
  "kto": "Małgorzata Bogdan",
  "sem": "Statystyka",
  "godz": "1115",
  "sala": "sala 602"
 },
 {
  "t": "Evaluating Imputation Methods",
  "kto": "Krystyna Grzesiak",
  "sem": "Statystyka",
  "godz": "1130",
  "sala": "sala 602"
 },
 {
  "t": "FDR Control via Sorted L-One Penalized Estimator (SLOPE) Method",
  "kto": "Michał Kos",
  "sem": "Statystyka",
  "godz": "1100",
  "sala": "sala 602"
 },
 {
  "t": "missKnockoffs: A Model-X Knockoff Framework for Variable Selection with Missing Data",
  "kto": "Dominik Nowakowski",
  "sem": "Statystyka",
  "godz": "1145",
  "sala": "sala 602"
 },
 {
  "t": "Network flow methods for alignment and deconvolution of multidimensional spectra",
  "kto": "Maria Bochenek",
  "sem": "Statystyka",
  "godz": "1115",
  "sala": "sala 605"
 },
 {
  "t": "What Counts as Significant? Lessons from Applied Proteomics",
  "kto": "Vanessa Linke",
  "sem": "Statystyka",
  "godz": "1200",
  "sala": "sala 605"
 },
 {
  "t": "Adaptive Bayesian SLOPE",
  "kto": "Joanna Pokora",
  "sem": "Statystyka",
  "godz": "1100",
  "sala": "sala 605"
 },
 {
  "t": "Modeling Hydrogen-Deuterium Exchange Mass Spectrometry data via convolutions of exchange probabilities",
  "kto": "Mateusz Staniak",
  "sem": "Statystyka",
  "godz": "1130",
  "sala": "sala 605"
 },
 {
  "t": "Challenges of AP-MS data interpretation in biological relevance driven studies",
  "kto": "Michał Tracz",
  "sem": "Statystyka",
  "godz": "1145",
  "sala": "sala 605"
 },
 {
  "t": "Beyond Average Treatment Effects: Variable Importance for Treatment Effect Heterogeneity",
  "kto": "Paweł Morzywołek",
  "sem": "Statystyka",
  "godz": "1415",
  "sala": "sala 603"
 }
]}

# (dzień, „lis · czw.”, dział, rodzaj, godzina, miejsce, tytuł)
WYDARZENIA = [
    ('20', 'lis · pt.', 'nauka', 'obrona doktorska', '14:00', 's. WS', 'Analysis and simulations of the non-linear models with non-local dispersal of species considered in ecology'),
    ('24', 'lis · wt.', 'instytut', '', '12:30', 'sala 119, Instytut Informatyki UWr', 'Seminarium wydziałowe: prof. Olga Vitek'),
    ('26', 'lis · czw.', 'popularyzacja', '', '13:00', 's. WS', 'Wykład prof. Uwe Franza „Who was Seki Takakazu?”'),
    ('27', 'lis · pt.', 'nauka', 'obrona doktorska', '13:15', 's. WS', 'Estimation of a block-structured covariance matrix'),
    ('28', 'lis · sob.', 'studia', '', '10:00', 'TEST - miejsce przykładowe', 'TEST: Dzień otwarty matematyki dla kandydatów'),
    ('2', 'gru · śr.', 'popularyzacja', 'termin', '', '', 'Zgłoszenia szkół na 3. Kongres Młodych Odkrywców'),
    ('4', 'gru · pt.', 'nauka', 'konferencja', '', 'Będlewo', 'Discrete Random Structures II'),
    ('8', 'gru · wt.', 'nauka', 'obrona doktorska', '16:30', 's. WS', 'On isomorphic and geometric properties of Banach spaces of continuous functions'),
    ('10', 'gru · czw.', 'nauka', 'obrona doktorska', '15:30', 's. WS', 'Rational approximation of surface group representations'),
]
NAZWY = {'instytut': 'Instytut', 'nauka': 'Nauka', 'studia': 'Studia', 'popularyzacja': 'Popularyzacja'}
# dni tygodnia seminariów 17–23 listopada
DNI_SEM = [('17', 'lis · wt.'), ('18', 'lis · śr.'), ('19', 'lis · czw.'), ('20', 'lis · pt.'), ('23', 'lis · pon.')]
SCEN = {'malo': (None, None, None), 'typowo': (4, 5, 12), 'duzo': (10, 14, 20)}


def _wiersz(soup, d, m, dzial, gdzie, co, tytul, kto=None):
    a = soup.new_tag('a', attrs={'class': 'z-w', 'href': '#', 'data-dzial': dzial, 'data-koniec': '2026-12-31'})
    k = soup.new_tag('span', attrs={'class': 'kiedy'}); b = soup.new_tag('b'); b.string = d; k.append(b); k.append(m)
    tr = soup.new_tag('span', attrs={'class': 'tr'})
    g = soup.new_tag('span', attrs={'class': 'gdzie'}); g.append(gdzie)
    if co:
        i = soup.new_tag('i'); i.string = ' · ' + co; g.append(i)
    t = soup.new_tag('span', attrs={'class': 't'}); t.append(tytul)
    if kto:
        t.append(' '); s = soup.new_tag('span', attrs={'class': 'kto'}); s.string = '– ' + kto; t.append(s)
    tr.append(g); tr.append(t); a.append(k); a.append(tr)
    return a


def _przycisk(soup, key, n, ile_widac):
    b = soup.new_tag('button', attrs={'type': 'button', 'class': 'z-wiecej', 'data-key': key})
    if n <= ile_widac:
        b['hidden'] = ''
    s1 = soup.new_tag('span', attrs={'class': 'kropki3', 'aria-hidden': 'true'}); s1.string = '•••'
    s2 = soup.new_tag('span'); s2.append('Zobacz więcej (')
    k = soup.new_tag('span', attrs={'class': 'z-ile-k'}); k.string = str(max(0, n - ile_widac))
    t = soup.new_tag('span', attrs={'class': 'z-ile-t'}); t.string = str(max(0, n - 3))
    s2.append(k); s2.append(t); s2.append(')')
    b.append(s1); b.append(s2)
    return b


def przeksztalc(html: str, scen: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    # zrzut całej strony: bez leniwego wczytywania obrazów
    for img in soup.select('.z-druga img'):
        img['loading'] = 'eager'
    nw, ns, na = SCEN[scen]
    if nw is None:
        return str(soup)
    kol = {k['data-key']: k for k in soup.select('.z-kolumna')}
    # wydarzenia: pierwsze prawdziwe + kolejne z puli
    poz = kol['wyd'].select_one('.pozycje')
    stare = poz.select('.z-w:not(.z-przeszle)')
    for w in stare[1:]:
        w.decompose()
    # nowe wiersze przed komunikatem „brak” i przed „Ostatnio” (minione pozycje z budowy zostają)
    kotwica = poz.select_one('.z-pusto') or poz.select_one('.z-ostatnio-h, .z-przeszle')
    for (d, m, dz, rodz, godz, miejsce, tyt) in WYDARZENIA[: nw - len(stare[:1])]:
        co = ' · '.join(x for x in (rodz, godz, miejsce) if x)
        w = _wiersz(soup, d, m, dz, NAZWY[dz], co, tyt)
        kotwica.insert_before(w) if kotwica else poz.append(w)
    for b in kol['wyd'].select('.z-wiecej'):
        b.decompose()
    kol['wyd'].append(_przycisk(soup, 'wyd', nw, 3))
    # seminaria
    poz = kol['sem'].select_one('.pozycje')
    for x in poz.select('.z-w:not(.z-przeszle)'):
        x.decompose()
    pusto = poz.select_one('.z-pusto')
    if pusto and ns:
        pusto['hidden'] = ''
    kotwica = poz.select_one('.z-ostatnio-h, .z-przeszle')
    sem = PULE['sem']
    for i in range(ns):
        r = sem[(i * 7) % len(sem)] if ns > len(sem) else sem[i * len(sem) // ns]
        d, m = DNI_SEM[min(4, i * 5 // ns)]
        godz = r['godz'][:2].lstrip('0') + ':' + r['godz'][2:]
        sala = r['sala'].replace('sala ', 's. ') if r['sala'].startswith('sala ') else r['sala']
        w = _wiersz(soup, d, m, 'nauka', r['sem'], f'{godz} · {sala}', r['t'].replace('$\\ell^2$', 'ℓ²'), r['kto'])
        kotwica.insert_before(w) if kotwica else poz.append(w)
    for b in kol['sem'].select('.z-wiecej'):
        b.decompose()
    kol['sem'].append(_przycisk(soup, 'sem', ns, 3))
    # pasek: liczba referatów
    for s in soup.select('.z-skr a small'):
        if 'referat' in s.get_text():
            s.string = f'{ns} referatów w tym tygodniu'
    # aktualności: 12 z budowy, więcej = kopie (bez wyróżnienia)
    poz = kol['akt'].select_one('.pozycje')
    w = poz.select('.z-w')
    for x in w[na:]:
        x.decompose()
    i = 0
    while len(poz.select('.z-w')) < na:
        c = copy.copy(w[1 + i % (len(w) - 1)])
        poz.append(c); i += 1
    return str(soup)
```
