# Raport: zlecenie 35, Szybki dostęp bez dziur i „Ostatnio”

**Status:** zrobione i wypchnięte 18.11.2026 o 11:49 UTC, w trybie samodzielnym.
- Web-Core `main`: `6e370e19..70e9ab73`, jeden commit, zwykły push, bez force.
- Przed pushem: `fetch` i `rebase` na `origin/main`. W międzyczasie wszedł tam kod zlecenia 33 z drugiej sesji (3 commity).
  - Jeden konflikt: wiersz `import … from '../../lib/tresci'` w `DrugiEkran.astro`. Tam doszło `widoczny`, u mnie `wydarzeniaMinione` i `referatyMinione`; połączyłem obie listy.
  - Potem ponowna budowa, `astro check`, testy i cała macierz na zbudowanej stronie po `rebase`. Wszystkie 33 pomiary są takie same jak przed `rebase`.
- **Podgląd:** przebieg [44298270197](https://github.com/IM-UWr/Web-Podglad/actions/runs/44298270197) (`przebuduj`) zielony, trwał 86 s.
- Zlecenie kończy się słowami „Stop, raport, czekanie na push”. Wypchnąłem według zasad trybu samodzielnego: wszystkie kontrole przeszły.

## Zmienione pliki
- **`src/styles/zalozyciele-strony.css`:**
  - siatka bez rozpychania rzędów: `align-content: start`, `row-gap: 0`, `grid-template-rows: auto auto 1fr`. Ostatni rząd bierze resztę wysokości, więc długa kolumna sięga do stopki;
  - odstępy jako `margin-top` Studiów (`--z-g1`) i „Warto wiedzieć” (`--z-g2`), domyślnie 22 px;
  - usunięte reguły `data-krok` i `--z-siatka-h`;
  - zapas bez JS: `nth-child` tylko przy `.z-druga:not([data-tryb])`;
  - tryb pomiaru `.z-miara`;
  - wygląd „Ostatnio”: nagłówek 12 px, 700, wersaliki, `--muted`, padding 10/6, kreska `--line`; tytuł 500 w `--text`, „dział · …” z `opacity: .8`;
  - na telefonie „Ostatnio” schowane.
- **`src/scripts/zal/drugi-ekran.ts`:**
  - `uloz()` zamiast `drabinka()`, działa przy każdym k: tryby 0–3, stałe `G0 = 22`, `GPREF = 56`, `GMAX = 88`, dokładanie pozycji do R, odstępy jak w zleceniu;
  - `pokaz()` i „Zobacz więcej (N)” liczą tylko nadchodzące;
  - `dopasujDluga()` pokazuje minione pod nadchodzącymi, tylko gdy zmieszczą się wszystkie nadchodzące;
  - `schowajZakonczone()` przenosi zakończone wydarzenia na początek „Ostatnio” i co 60 s sprawdza, czy coś się skończyło;
  - `zamien()` liczy układ od nowa przed FLIP;
  - komentarze w nagłówku opisują D3.4.
- **`src/components/zal/DrugiEkran.astro`:**
  - minione pozycje (`a.z-w.minelo.z-przeszle`, `hidden`) i nagłówek `<h3 class="z-ostatnio-h" hidden>`;
  - napisy „Ostatnio w kalendarzu” / „Ostatnie referaty”, po angielsku „Recently in the calendar” / „Recent talks”;
  - wiersze nadchodzące i minione z jednego wzoru;
  - komentarz w nagłówku.
- **`src/lib/tresci.ts`:**
  - `wydarzeniaMinione()` i `referatyMinione()` ze stałymi `OSTATNIO_DNI = 14` i `OSTATNIO_LIMIT = 6`, bez pola w CMS;
  - wspólna `referatyMiedzy()`; `referatyWTygodniu()` korzysta z niej bez zmiany wyniku.

## Narzędzia odbioru (lokalnie, `raport-zrzuty/z35-skrypt/`)
- `pomiar.js` (załącznik C, bez zmian) i `dane_odbior.py` (załącznik D) z wierszem poleceń.
  - **Odstępstwo w `dane_odbior.py`:** komunikat „W tym tygodniu nie ma referatów” w seminariach jest usuwany zamiast ukrywany. Prawdziwa budowa z referatami go nie ma, bo `DrugiEkran.astro` renderuje go tylko przy pustej liście.
  - Ukryty komunikat stał jako pierwsze dziecko `.pozycje`. Przez to zapas `nth-child` w wersji „przed” pokazywał 2 referaty zamiast 3, a wynik „przed” był zafałszowany.
- `macierz35.mjs`: 11 okien × 3 scenariusze, zrzuty całej strony, `pomiary.json`. Do tego tryb, `--z-g1`, `--z-g2`, położenie Studiów, „Warto wiedzieć” i stopki oraz liczba widocznych minionych pozycji.
  - Warunki: motyw jasny, `Math.random` z ziarnem (ta sama kolejność „Warto wiedzieć” przed i po), `reducedMotion`.
- `tabela35.mjs`: tabela jak w zleceniu.
- `zegar35.mjs`, `zamiana35.mjs`, `reszta35.mjs`: pozostałe sprawdzenia.
- **Foldery:**
  - `z35-przed2`: przed, `main` = `b7192769`;
  - `z35-po3`: po, przed `rebase`;
  - `z35-po4`: po, wersja wypchnięta;
  - `z35-po3-1711`: po, z „Warto wiedzieć” jak 17.11 (wyjaśnienie niżej);
  - `z35-testy`: zegar, zamiana, Ctrl +, ciemny, telefon, bez JS.
- **Zostawione, nieużywane:**
  - `z35-przed` i `z35-dane-przed`: scenariusze przed poprawką komunikatu;
  - `z35-po` i `z35-dane-po`: pierwsza wersja z błędem pomiaru (niżej);
  - `z35-po2`, `z35-dane-po2` i `z35-dane-1711`.

## Wynik odbioru

### Macierz: przed → po (dzisiejsze treści)
Wartości to największa dziura w px okna; „—” znaczy brak dziury. „x/y” to pozycje widoczne / nadchodzące (widoczne obejmują minione).

| okno | mało | typowo | dużo | tryb po (m/t/d) | po, mało: wyd · sem | po, typowo: wyd · sem · akt |
|---|---|---|---|---|---|---|
| 1280×590 | 241 → 166 | 246 → — | 229 → — | 3/3/3 | 2/2 · 0/0 | 2/4 · 2/5 · 9/12 |
| 1366×638 | 239 → 175 | 215 → — | 198 → — | 2/3/3 | 2/2 · 0/0 | 2/4 · 2/5 · 9/12 |
| 1536×734 | 163 → 163 | 219 → — | 219 → 121 | 1/2/2 | 2/2 · 0/0 | 4/4 · 3/5 · 10/12 |
| 1920×950 | 242 → — | 130 → 108 | 113 → 112 | 0/0/0 | 4/2 · 3/0 | 4/4 · 3/5 · 10/12 |
| 2560×1310 | 344 → 175 | 198 → 169 | 175 → 171 | 0/0/0 | 4/2 · 4/0 | 4/4 · 3/5 · 11/12 |
| 1707×830 | 190 → — | 217 → 101 | — → — | 0/2/1 | 2/2 · 1/0 | 5/4 · 4/5 · 11/12 |
| 3840×2030 | 548 → — | 325 → — | 290 → — | 0/0/0 | 5/2 · 4/0 | 5/4 · 4/5 · 11/12 |
| 1024×950 | 412 → — | 223 → 108 | 224 → 142 | 2/2/2 | 3/2 · 3/0 | 3/4 · 2/5 · 7/12 |
| 1150×950 | 219 → — | 253 → 115 | 253 → 115 | 0/2/2 | 2/2 · 1/0 | 4/4 · 3/5 · 8/12 |
| 1300×950 | 204 → — | 274 → — | 274 → — | 0/2/2 | 2/2 · 1/0 | 5/4 · 4/5 · 12/12 |
| 1100×1300 | 385 → 109 | 176 → 137 | 166 → 118 | 0/0/0 | 4/2 · 4/0 | 4/4 · 3/5 · 9/12 |

- Żadna dziura nie urosła. Największe zostały na 2560×1310 (169–175 px przy k = 1,33, czyli 127–131 px w skali Full HD).
- **„Mało” to dane z dnia budowy (18.11):**
  - 2 nadchodzące wydarzenia, 0 referatów;
  - minione: 4 wydarzenia (9–14.11) i 3 referaty (12–13.11).

  W zleceniu „mało” to dane z 17.11 (1 wydarzenie), więc kolumna „mało” nie porównuje się 1:1 (zlecenie to przewiduje).

### Dlaczego część wartości odbiega od tabeli zlecenia: „Warto wiedzieć” jest dziś o jeden wiersz wyższe
- **Różnica w treści:**
  - w budowie z 17.11, z której jest prototyp, „Warto wiedzieć” miało 3 wpisy z tytułami w 2 wierszach (ok. 92 px);
  - dziś ma 4 wpisy, w tym nowy „Medale Uniwersytetu dla profesorów Marka Bożejki i Tomasza Rolskiego” (2026), którego tytuł zajmuje 3 wiersze;
  - blok ma więc 113 px (zrzuty obok siebie sprawdzone).
- **Skutek:** wolnego miejsca jest o ok. 21 px mniej:
  - **1920×950, typowo:** odstępy 63,7 px zamiast ok. 74. Dziury mierzone `pomiar.js` mają 76 i 64 px zamiast 86 i 74;
  - **1707×830, typowo:** tryb 2 zamiast 1. Pomiar przy 3 pozycjach daje 773 px przy budżecie 764 px, czyli 9 px za dużo;
  - **2560×1310, typowo:** minione wydarzenie z nagłówkiem (ok. 88 px projektu) już się nie mieści, bo zostaje 83 px. Kolumna wydarzeń jest krótsza od seminariów i zostaje dziura 169 px (127 px w skali Full HD).
- **Sprawdzenie:** ta sama macierz na zbudowanej stronie po zmianie, z usuniętym tylko tym jednym wpisem „Warto wiedzieć” (`z35-po3-1711`):

  | okno | typowo: D w zleceniu → u mnie | dużo: D → u mnie | tryb D → u mnie (m/t/d) | typowo D → u mnie: wyd · sem · akt |
  |---|---|---|---|---|
  | 1280×590 | — → — | — → 104 | 2/3/3 → 3/3/3 | 2/4 · 2/5 · 9/12 → tak samo |
  | 1366×638 | — → — | — → — | 2/3/3 → 2/3/3 | 2/4 · 2/5 · 8/12 → 9/12 |
  | 1536×734 | — → — | 121 → 121 | 0/2/2 → 1/2/2 | 4/4 · 3/5 · 9/12 → tak samo |
  | 1920×950 | 118 → 118 | 122 → 122 | 0/0/0 → 0/0/0 | 4/4 · 3/5 · 10/12 → tak samo |
  | 2560×1310 | — → — | — → — | 0/0/0 → 0/0/0 | 5/4 · 4/5 · 10/12 → 11/12 |
  | 1707×830 | — → — | — → — | 0/1/1 → 0/1/1 | 3/4 · 3/5 · 9/12 → tak samo |
  | 3840×2030 | 209 → 217 | — → — | 0/0/0 → 0/0/0 | 5/4 · 5/5 · 11/12 → tak samo |
  | 1024×950 | 108 → 108 | 142 → 142 | 0/2/2 → 1/2/2 | 3/4 · 2/5 · 7/12 → tak samo |
  | 1150×950 | 112 → 112 | — → — | 0/2/2 → 0/2/2 | 4/4 · 3/5 · 7/12 → 8/12 |
  | 1300×950 | — → — | — → — | 0/2/2 → 0/2/2 | 5/4 · 4/5 · 11/12 → 12/12 |
  | 1100×1300 | — → 182 | 174 → 163 | 0/0/0 → 0/0/0 | 5/4 · 4/5 · 9/12 → 4/4 · 4/5 · 9/12 |

  - Na 1920×950 odstęp wynosi 73,9 px, Studia stoją na 555 px (treść na 567), „Warto wiedzieć” na 787 px, czyli dokładnie jak w prototypie.
  - Wszystko mieści się w tolerancji (±15 px albo jedna pozycja). Wyjątek to 1100×1300 typowo: dziura 182 px, bo w kolumnie wydarzeń jest o jedną minioną pozycję mniej niż w prototypie. Minione wydarzenia są inne niż 17.11 (dłuższe tytuły „TEST - …”).
  - 1280×590 dużo: 104 px, tuż nad progiem 100 px.
  - Różnice w trybie „mało” wynikają z innych danych.

### Pozostałe sprawdzenia
- **1920×950, typowo, „jak dziś”:** spełnione.
  - Studia 545 → 545 px, „Warto wiedzieć” 768 → 767 px.
  - Jedyna różnica to czwarte wydarzenie zamiast „Zobacz więcej (1)”.
  - Odstępy 74–86 px z tabeli zlecenia odpowiadają treściom z 17.11. Przy dzisiejszych treściach dzisiejsza strona też ma 63,7 px.
- **„Ostatnio”, dane z budowy:**
  - 1920×950: kolumny pełne, bez dziur (2 + 2 minione · 3 minione referaty);
  - 3840×2030: bez dziur;
  - 2560×1310: dziura 175 px (z treścią z 17.11: brak dziury);
  - w scenariuszu „dużo” „Ostatnio” nie pokazuje się w żadnym z 11 okien.
- **Zegar (`page.clock`, strefa Europe/Warsaw):** spełnione. Strona otwarta 19.11 o 14:40. O 14:46 wydarzenie z 19.11 (koniec 14:45) jest pierwsze pod „Ostatnio w kalendarzu”, a układ policzył się od nowa. Zrzuty: `z35-testy/zegar-*`.
- **Zamiana kolumn** (6 przypadków × z ruchem i bez, w trybach 0, 1 i 2):
  - fokus zawsze na nagłówku klikniętej kolumny;
  - minione zawsze pod nadchodzącymi (kolejność `N…NHP…P`);
  - konsola czysta;
  - **nowe dziury:** po zamianie Aktualności stają się krótką kolumną. Następna aktualność (ok. 69 px) nie mieści się w zapasie ponad odstęp 56 px, więc pod nią zostaje pas 101–115 px:
    - 1920×950 typowo: 108 → 102;
    - 1920×950 dużo: 112 → 101;
    - 1300×950 dużo: — → 115;
    - 1707×830 i 1300×950 typowo: bez dziur.

  To ta sama zasada co w prototypie (pytanie 2).
- **Ctrl + 125%, 150% i 200%** (okno 1920×950, `devicePixelRatio` jak przy powiększeniu): k = 1 jak dziś, nic nie zachodzi na siebie.
  - 125%: tryby 1/2/2;
  - 150%: tryby 2/3/3, czyli przewijanie;
  - 200% (960 px): układ telefonu.
- **Zmiana rozmiaru na żywo** 1920 → 1024 → 1920: stan po powrocie (tryb, style, ukryte pozycje, przyciski) taki sam jak na początku, w scenariuszach „mało” i „typowo”.
- **EN:** „Recently in the calendar” i „Recent talks”, widoczne.
- **Tryb ciemny** 1920×950 i 2560×1310: bez regresji (zrzuty przed i po). Nagłówek „Ostatnio” rgb(165 171 183) na tle #172032, kreska rgb(50 59 75).
- **Telefon 390 i 768 px:** 0 różnych pikseli w 8 z 8 porównań (okładka, `#szybki-dostep`, „typowo”, EN).
- **Bez JS:** 3 pozycje w krótkich kolumnach, jak przed zmianą, w trzech scenariuszach; minione i nagłówek niewidoczne.
- **`astro check` i testy:**
  - przed `rebase`: 0 błędów, 0 ostrzeżeń, 3 podpowiedzi, jak na bazie;
  - po `rebase`: 6 podpowiedzi. Trzy nowe są w plikach zlecenia 33 (`skrypty/test-stanu-budowy.mjs`, `src/lib/stanBudowy/klient.js`), żadna w moich;
  - testy 47/47, konsola czysta we wszystkich przebiegach.

## Błąd znaleziony w trakcie i naprawiony przed pushem
Pierwsza wersja `uloz()` usuwała `data-tryb` na czas pomiaru, jak prototyp (`delete druga.dataset.tryb`).
- Wtedy działał zapas bez JS (`.z-druga:not([data-tryb]) … nth-child(n+4)`), który chował pozycje dokładane przez pomiar.
- Skutek: kolumny dostawały wszystkie pozycje.
- Poprawka: na czas pomiaru `data-tryb="miara"`.

## Odstępstwa od zlecenia i powody
- **`data-tryb="miara"` podczas pomiaru** (wyżej). W prototypie nie było zapasu bez JS opartego na `data-tryb`.
- **Zakończone wydarzenia** przechodzą do „Ostatnio” przy każdym sprawdzeniu, co 60 s, dopóki strona jest otwarta (punkt 12). W prototypie znikały i były sprawdzane tylko na starcie.
- **`dok/estetyka.md` nie istnieje na `main`.** Był tylko w commicie `2f0db28c`, który nie należy do żadnej gałęzi. Opis D3.4 jest w komentarzach na początku `drugi-ekran.ts`, `zalozyciele-strony.css` i `DrugiEkran.astro` (pytanie 1).
- **Liczba dni i limit „Ostatnio”** to stałe w `tresci.ts`, nie w `ustawienia.json`. Zlecenie dopuszcza oba miejsca; tak nie trzeba ruszać repozytorium Web-Ustawienia. Bez pola w CMS, więc bez wpisu w `pola-do-cms.md`.

## Decyzje podjęte samodzielnie
- **„Ostatnio” pojawia się zawsze, gdy zostaje miejsce,** także przy 3 i więcej nadchodzących. Przyjąłem domyślne ustawienie ze zlecenia, bo tak opisuje je artefakt („przyjęte domyślnie w zleceniu 35”).
- **Przy trybie 3 krótkie kolumny mają po 2 pozycje,** bo tak każe D3.4 i zlecenie.
- **Nagłówek „Ostatnio” to `h3` z `hidden`, widoczny tylko razem z pierwszą widoczną minioną pozycją.** Zlecenie (punkt 9) chce osobnego elementu zamiast `::before` z prototypu. Ma padding 10/6 px jak `::before`, bez dodatkowego marginesu pod kreską.
- **Ukryte pozycje mają atrybut `hidden`, a nie styl,** bo wtedy czytnik ekranu ich nie czyta (punkt 14).
- **Scenariusze danych z poprawką komunikatu „brak referatów”** (wyżej), bo bez niej porównanie „przed” byłoby zafałszowane.

## Pytania do użytkownika
1. **`dok/estetyka.md`:** pliku nie ma na `main`. Czy odtworzyć go z `2f0db28c` i dopisać rozdział „Drugi ekran” (D3.4), czy opis ma trafić gdzie indziej? Na razie jest tylko w komentarzach w kodzie.
2. **Zamiana kolumn:** po kliknięciu „Zobacz więcej” Aktualności stają się krótką kolumną. Pod nimi bywa pas 101–115 px, bo następna aktualność nie mieści się w zapasie ponad odstęp 56 px. Czy to przyjąć (zasada jak w prototypie), czy w zamienionej kolumnie dopuścić mniejszy odstęp?
3. **Nowy wpis „Medale Uniwersytetu…” w „Warto wiedzieć”** ma tytuł w 3 wierszach. Przez niego odstępy na Full HD mają dziś 64 px zamiast 74, a 1707×830 przechodzi w tryb 2. Czy skrócić tytuł (lub `tytul_krotki`), czy tak zostawić?

## Do sprawdzenia jutro
- Podgląd na prawdziwym monitorze 2K / 4K i na 1707×830 (2560 × 1440 przy 150%): „Ostatnio” i odstępy.
- „Ostatnio” na żywo, gdy wydarzenie z 19.11 (koniec 14:45) się skończy: przy otwartej stronie przejdzie do „Ostatnio” po najwyżej minucie.
- Zamiana kolumn z ruchem w prawdziwej przeglądarce.
