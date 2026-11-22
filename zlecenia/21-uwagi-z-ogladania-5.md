# Zlecenie 21: uwagi z oglądania, część 5 (OTWARTE, 6.11.2026)

Stan: **otwarte** — właściciel może dopisywać kolejne punkty. Wykonuj tylko punkty oznaczone **GOTOWE**.

**Gdzie i jak** (tak samo jak w zleceniach 17–20)
- Gałąź `wyglad/zlecenie-16`, po commitach zlecenia 20. Osobny commit na każdy punkt. **Bez pushowania**, także w repozytoriach treści.
- **Nie uruchamiaj `skrypty/pobierz_tresci.py`.**
- Dziennik w `.przekazanie\dziennik.md`, raport `RAPORT-ZLECENIE-21.md`.

## 1. Lista Seminaria: podtytuł na karcie kursywą, bez zieleni — GOTOWE (decyzja 6.11, 12:14)
Właściciel: podtytuł (np. „Wielomiany i kumulanty”) „powinno być bez zielonego, jakiś inny motyw, mniej rzucający się w oczy”. Wybrana wersja: **C. Kursywa**. Zastrzeżenie właściciela: zmienia się wyłącznie ten tekst, nic więcej.

**Wzór:** artefakt https://claude.ai/artifact/RZGt6prE7qf8VdG6tiktJo, sekcja „C. Kursywa”. Źródło: `.przekazanie\prototypy\21-podtytuly-seminariow.html`.

**Zmiana:** jedna reguła w `src/styles/zal-tresc.css` (dziś linia 124).

Było:
```css
.tresc .boks .haslo { font-size: 14px; font-weight: 600; color: var(--d-a); }
```

Ma być:
```css
.tresc .boks .haslo { font-family: var(--f-display); font-style: italic; font-size: 16px; font-weight: 400; line-height: 1.3; color: var(--muted); }
```

**Czego nie zmieniać**
- Żadnego innego pliku ani reguły. HTML w `src/views/ListaSeminariow.astro` i pole `haslo` w CMS zostają bez zmian.
- Bez nowych czcionek: kursywa Brygady jest już w `@font-face`.
- Bez zmian: nazwa zakładu, tytuł, data referatu, „Brak zapowiedzianych referatów”, „Prowadzą”, zachowanie karty po najechaniu.
- Bez podobnych poprawek „przy okazji” na innych stronach. Jeśli zauważysz coś do poprawy, wpisz to do raportu.

**Odbiór**
- `/seminaria` i `/en/seminaria`: każdy podtytuł (na podglądzie 9 kart w każdym języku) ma krój Brygada, kursywę, 16 px, grubość 400 i kolor `--muted`. Sprawdź w obliczonych stylach, w jasnym i ciemnym motywie.
- Kursywa jest prawdziwa, a nie pochylona przez przeglądarkę, także dla polskich znaków. Sprawdź na podtytule z „ó” („Od danych do wniosków”) i „ś” („Jak uczyć matematyki i o niej mówić”).
- Elementy pod podtytułem nie przesuwają się o więcej niż 1 px (linia ma 20,8 px zamiast 21,7 px).
- Kontrast podtytułu na tle karty co najmniej 4,5:1 w obu motywach (w artefakcie 5,34:1 w jasnym i 6,14:1 w ciemnym).
- `git diff` tej zmiany obejmuje tylko wskazaną regułę.
- `astro check` bez nowych błędów, `npm run build` przechodzi.
- Zrzuty przed i po: PL przy 1536 px i 390 px, jasny i ciemny motyw, oraz EN przy 1536 px w jasnym → `raport-zrzuty/z21-seminaria-*`.

## 2. Telefon: kolor nagłówka według tych samych zasad co pasek na komputerze — GOTOWE (decyzja 6.11, 12:19–12:22)
Właściciel: „Na ciele strony w wersji mobilnej pasek navbar nie zmienia koloru. Powinien zmieniać podobnie jak na wersji pc”, „Przeskanuj dokładnie zasady i wprowadź je też na telefonie”. Punkt zmienia wcześniejsze ustalenie „pełny granatowy nagłówek na telefonie” (zlecenie 18, punkt 10).

**Dziś:** `.hdr` w `src/styles/zal-telefon.css` ma granat z `!important` na każdej stronie, a `src/scripts/zal/pasek.ts` działa tylko na `.z-pasek`, schowanym na telefonie.

**Zasady (≤ 760 px, `.hdr`).** Wartości są te same co w `zalozyciele.css`.

| Gdzie jest pasek | Wygląd |
|---|---|
| Strona z banerem, na górze (`scrollY` ≤ wysokość paska) | pełny granat, biały tekst. Pasek stoi tu w układzie i nie ma jeszcze pod sobą banera, więc prześwitujące tło dałoby szarość |
| Nad banerem po przewinięciu (`.przewiniety`) | `color-mix(in srgb, var(--granat) var(--pasek-krycie), transparent)`, `blur(14px) saturate(1.1)`, linia `rgb(255 255 255 / .1)`, cień `0 8px 24px rgb(0 0 0 / .18)`, biały tekst. `--pasek-krycie` na tych samych warunkach co na komputerze: 45%, `.z-nagl-pod[data-dzial]` 40%, `.z-foto-nat` 60% |
| Nad treścią (`.jasny`) | `color-mix(in srgb, var(--bg) 95%, transparent)`, `blur(8px)`, linia `var(--line)`, cień `0 6px 18px rgb(13 24 48 / .06)`. Nazwa `--ink`, podpis `--muted`, logo `--uwr`, ikony `color-mix(in srgb, var(--ink) 76%, transparent)`, burger: tło `--surface`, kolor `--ink` |
| Nad stopką | jak nad banerem po przewinięciu |
| Strona bez banera (`/powiadomienia`, `/studia/kalendarz-zajec`, także EN) | na górze pełny granat, od `scrollY` > 2 jasny, nad stopką pełny granat bez rozmycia |
| Strona główna | nad okładką pełny granat, od krawędzi Szybkiego dostępu w dół zawsze jasny, także nad stopką (jak `.z-pasek-jasny` na komputerze). Nazwa Wydziału i jej zamiana na Instytut (`po-okladce`) bez zmian |

- **Co jest pod paskiem:** linia 1 px tuż **pod** dolną krawędzią paska (h…h+1), a nie h−1…h jak na komputerze. Na telefonie pasek stoi w układzie: przy `scrollY` 0 baner zaczyna się dokładnie na h, a na krawędzi Szybkiego dostępu okładka kończy się dokładnie na h. Przy linii z komputera oba stany wyszłyby odwrotnie.
- **Panel menu ma kolor paska, jak na komputerze** (`.z-menu-jasny`): wyjmij reguły `.z-menu-jasny` z bloku komputera w `zal-menu.css`, żeby działały też na telefonie. Na telefonie tło jasnego panelu pełne, `var(--bg)`, bo przy 97% prześwituje tekst strony. `.hdr.menu-otwarte` przestaje wymuszać granat. Na głównej panel ma na stałe klasę `z-menu-jasny`: na telefonie klasę przełącza skrypt według stanu paska, a na komputerze panel zostaje jasny, także po obróceniu lub zmianie szerokości okna.
- Przejścia `var(--t-sredni) var(--rytm)`, przy `prefers-reduced-motion` bez przejść. Popraw komentarze w `zal-telefon.css`, `pasek.ts` i `zal-menu.css`.
- **Komputer (≥ 761 px) bez żadnych zmian.**

**Wzór:** `.przekazanie\prototypy\21-telefon-pasek.css` i `21-telefon-pasek.js` (próba nałożona na zbudowany podgląd, stany i wartości sprawdzone; kod do przeniesienia po swojemu, najlepiej przez rozszerzenie `pasek.ts`).

**Odbiór**
- Tabela stanów w raporcie (klasa, tło, kolor nazwy) dla: `/instytut`, `/aktualnosci`, `/seminaria`, `/`, pojedynczej aktualności, `/powiadomienia`, `/studia/kalendarz-zajec`, na górze, nad banerem, nad treścią i nad stopką (gdzie stopka dochodzi pod pasek). PL i EN, jasny i ciemny motyw.
- Bez mignięcia jasnym paskiem przy wejściu na górę strony.
- Kontrast białego tekstu paska z najjaśniejszym miejscem pod nim nad banerem co najmniej 4,5:1 (w próbie najmniej 8,95:1 na 8 stronach).
- Panel otwarty przy pasku ciemnym i jasnym, w obu motywach, przy 390 i 320 px.
- Komputer: zrzuty przed i po przy 1536 px identyczne.
- Zrzuty → `raport-zrzuty/z21-pasek-*`.

## 3. Telefon, strona główna: rozpęd zatrzymuje się na krawędzi Szybkiego dostępu — GOTOWE (decyzja 6.11, 12:20)
Właściciel: „jak jesteś na quick access to scroll na telefonie nie powinien pozwalać na przejście na główną, chyba że dojdziesz do góry quick access i wtedy jeszcze raz scroll. Żeby nie dało się z rozpędu raz i wywala na główną”. To ta sama zasada co na komputerze w `src/scripts/zal/przejazd.ts` (ruch w górę, który zaczął się poniżej, kończy się na krawędzi; na okładkę prowadzi dopiero nowy ruch po `CISZA` = 400 ms).

**Dziś:** na dotyku działa tylko `scroll-snap-type: y mandatory` (`zalozyciele-strony.css`), więc machnięcie w górę przelatuje krawędź i kończy na okładce.

**Czego nie używać (sprawdzone na emulacji Pixel 7, machnięcia palcem):**
- `scroll-snap-stop: always` na `.z-druga-obszar`: bez zmian względem stanu dzisiejszego;
- osobny punkt przyciągania z `scroll-snap-stop: always`: wynik przypadkowy, raz staje, raz przelatuje;
- zatrzymywanie rozpędu skryptem (`overflow: hidden` i `scrollTo` w zdarzeniu `scroll`): 4 z 15 prób.

**Co zadziałało (20 z 20 prób):** gdy Szybki dostęp stoi w spoczynku na krawędzi lub niżej, okładki nie ma w układzie strony, więc rozpęd kończy się na prawdziwej górze dokumentu.
- Na dotyku (`(hover: none) and (pointer: coarse)`) po uspokojeniu przewijania, gdy `scrollY` ≥ `y1()` − 1: `html.bez-okladki .z-okladka { display: none }` i w tej samej chwili `scrollTo` o `y1()` niżej (`behavior: 'instant'`), bez widocznego skoku.
- Uspokojenie: 150 ms bez zdarzeń `scroll` i bez palca na ekranie. Nigdy w trakcie rozpędu.
- `touchstart`, gdy okładka schowana, `scrollY` ≤ 1 i od ostatniego zdarzenia `scroll` minęło co najmniej `CISZA`: przywróć okładkę i w tej samej chwili przewiń o jej wysokość w dół. Ten ruch może już wejść na okładkę, a `mandatory` ją dociągnie.
- Wzór: `.przekazanie\prototypy\21-telefon-okladka.js`.

**Sprawdź przy przenoszeniu do `przejazd.ts`**
- `ResizeObserver` na okładce i `y1()` przy schowanej okładce; zmiana wysokości okna i obrót telefonu.
- Powrót „wstecz” na główną i odtworzenie pozycji (`pageshow`).
- Adres z `#okladka` lub `#szybki-dostep` oraz kliknięcie strzałki i liczb na okładce.
- Zaznaczanie tekstu i dotknięcie linku na krawędzi: link ma działać, pozycja bez skoku.
- Kolor paska z punktu 2 i obserwator `po-okladce` przy schowanej okładce.
- Mysz, gładzik i klawiatura (komputer) bez zmian.

**Odbiór**
- Tabela w raporcie, po 3 próby machnięcia w górę ze startu +30, +120, +300, +600 i +1000 px od krawędzi oraz od stopki: każda kończy na krawędzi, żadna na okładce.
- Następny ruch po chwili: okładka. Z okładki w dół, krótko i mocno: krawędź. Z krawędzi w dół: swobodnie.
- Dwa machnięcia w odstępie krótszym niż 400 ms od zatrzymania: nadal krawędź.
- Palec przesuwany powoli przez krawędź: nie wchodzi na okładkę.
- **Emulacja to tylko Chromium.** W raporcie napisz wprost, że Safari na iPhonie i prawdziwy Android sprawdza właściciel na swoim telefonie.

## 4. Telefon, strona Instytutu: „Ostatnie sukcesy” w układzie listy Aktualności — GOTOWE (decyzja 6.11, 12:26)
Właściciel: „Sukcesy w instytucie na telefonie powinny mieć strukturę podobną do aktualności. Obecny układ ciężko się czyta. Tyle samo sukcesów, ale inny sposób wyświetlania”.

**Zakres:** sekcja „Ostatnie sukcesy” w `src/views/DzialInstytut.astro`, tylko ≤ 760 px. Te same 3 wpisy. `/nauka/sukcesy` i komputer bez zmian.

**Wzór:** `src/components/WierszAktualnosci.astro` na telefonie (data i miniatura z lewej, tekst z prawej). Porównanie: `.przekazanie\prototypy\21-sukcesy-porownanie.png`, style próby: `21-sukcesy-telefon.css`. W próbie sekcja ma 686 px zamiast 1421 px.

**HTML** (jedna wersja dla obu szerokości)
- `<time>` z dwiema formami: pełna data jak dziś oraz dzień z `<small>` „mie rrrr” (`dayNum`, `monthShort`, `parse`). Komputer pokazuje pierwszą, telefon drugą; drugiej nie oznaczaj `aria-hidden`, bo ukrywa ją już `display: none`.
- `<h3>` i `<p>` w jednym elemencie, np. `.z-dz-suk-tr`; na komputerze `display: contents`.

**CSS (≤ 760 px)**
```css
.z-dz-suk { display: block; }
.z-dz-suk article { display: grid; grid-template-columns: 54px minmax(0, 1fr); grid-template-rows: auto minmax(0, 1fr); gap: 0 12px; padding: 13px 0; border-bottom: 1px solid var(--line); }
.z-dz-suk article > time { grid-column: 1; grid-row: 1; margin: 0; font-family: var(--f-display); font-weight: 500; font-size: 28px; line-height: 1; color: var(--d-a); font-variant-numeric: lining-nums; }
.z-dz-suk article > time small { display: block; margin-top: 4px; font-family: var(--f-text); font-size: 12px; font-weight: 600; color: var(--muted); }
.z-dz-suk .z-dz-fot { grid-column: 1; grid-row: 2; align-self: start; width: 54px; aspect-ratio: 1; margin-top: 10px; }
.z-dz-suk .z-dz-suk-tr { grid-column: 2; grid-row: 1 / 3; min-width: 0; }
.z-dz-suk h3 { margin: 2px 0 4px; font-size: 18.5px; line-height: 1.3; }
.z-dz-suk p { margin: 0; font-size: 15px; line-height: 1.55; }
```
- Bez etykiety „Sukces”: mówi to już tytuł sekcji.
- Zdjęcie: `sizes` z `(max-width: 760px) 54px` i małe szerokości w `srcset` (jak `SZEROKOSCI` w `WierszAktualnosci.astro`), żeby telefon nie pobierał dużych plików. Sygnet przy wpisie bez zdjęcia ma się zmieścić w polu 54 px.
- Cały wiersz klikalny (`.z-dz-klik`) i kolor tytułu po najechaniu bez zmian.

**Odbiór**
- 3 wpisy w tej samej kolejności, co na komputerze.
- Zrzuty przy 390 i 320 px, jasny i ciemny motyw, PL i EN, oraz porównanie obok listy Aktualności → `raport-zrzuty/z21-sukcesy-*`.
- Komputer przy 1536 px identyczny.
- Rozmiar pobieranych zdjęć sekcji na telefonie przed i po w raporcie.

## 5. Panel menu: jedna grubość pisma, bieżącą pozycję oznacza kolor — GOTOWE (decyzja 6.11, 12:40)
Właściciel: „Sprawdź navbar na telefonie, mam wrażenie że czcionki są różne. W szczególności aktualności”. Przegląd 758 stron (PL i EN): krój i wielkość są wszędzie te same, a różnice wychodzą z trzech reguł niżej. Pasek bez różnic.

**Co jest dziś**
- „Aktualności” mają grubość 700 na liście i na każdym wpisie (336 stron), nazwa działu ma 700 na stronie tego działu, a bieżący link w grupie też 700. Pozostałe pozycje mają 500.
- Na stronie głównej odstęp między literami nazw w panelu to −0,12 px zamiast −0,24 px, bo panel stoi tam w `main` i wygrywa `main :is(h1, h2, h3)`.

**Zmiana w `src/styles/zal-menu.css`**

Było:
```css
.z-menu ul a[aria-current='page'], .z-menu section[data-dzial] h2 a[aria-current='page'] { font-weight: 700; color: var(--d-j); }
.z-menu section.duza h2 a[aria-current='page'] { font-weight: 700; }
```

Ma być:
```css
.z-menu ul a[aria-current='page'], .z-menu section[data-dzial] h2 a[aria-current='page'] { color: var(--d-j); }
.z-menu section.duza h2 a[aria-current='page']::after { content: ''; background: currentColor; }
```
- Druga reguła daje „Aktualnościom” krótką kreskę, bo nie mają koloru działu. Wymiary bierze z `.z-menu h2 a::after`, także na telefonie. „Rekrutacja ↗” bez zmian.
- Do `.z-menu h2` dopisz `letter-spacing: -0.01em`.
- Popraw komentarz „bieżąca strona: pogrubiona, w kolorze działu”.
- W jasnym panelu (punkt 2) kolor bieżącej pozycji bez zmian (`--d-a`), kreska w `currentColor`. Punkty 2 i 5 dotykają tego samego pliku, więc sprawdź je razem.

**Dotyczy też komputera,** bo to wspólne reguły panelu. Pasek menu na komputerze („Aktualności” w górnym pasku) bez zmian.

**Odbiór**
- Na `/aktualnosci`, pojedynczym wpisie, `/nauka`, `/instytut/wladze`, `/` i ich wersjach EN wszystkie nazwy w panelu mają 500 i ten sam odstęp liter. Bieżący link w grupie ma 500 i kolor działu. W próbie telefon wyszedł −0,24 px na wszystkich tych stronach.
- Bieżące „Aktualności” mają kreskę, a na innych stronach jej nie mają.
- Panel na komputerze przy 1920×1080 i 1366×640 mieści się bez przewijania, tak jak dziś (w próbie 1366×640 bez przewijania). Na telefonie przy 390 i 320 px bez innych zmian.
- Zrzuty panelu → `raport-zrzuty/z21-menu-*`.

## 6. Wpis o wydarzeniu: kolor działu jak w wierszu listy (bez obron) — GOTOWE (decyzja 6.11, 12:40)
Właściciel pytał, czy konkretne wpisy o wydarzeniach (komputer i telefon, za wyjątkiem obron) powinny dziedziczyć motyw kolorystyczny z listy, i zatwierdził: etykieta, data (także miniona) i linki w tekście w kolorze wiersza, baner granatowy.

**Dziś:** na liście wiersz ma kolor z `dzialWpisu` (`src/lib/patroni.ts`): zielony Nauka albo różowy Popularyzacja. Po kliknięciu `Aktualnosc.astro` nie przekazuje działu do `Podstrona`, więc etykieta jest granatowa, a data granatowa albo szara.

**Zmiana**
- W `src/views/Aktualnosc.astro`, tylko gdy `d.rodzaj === 'wydarzenie'`: przekaż do `Podstrona` `dzial={dzialWpisu(d)}`, a do `klasa` dodaj `akt-wydarzenie`. Ta sama funkcja co na liście, bez kopii reguły.
- Etykieta „Wydarzenie” i data w karcie dostaną kolor same, bo używają `--d-a`. Reszta wiersza z etykietą (`Opublikowano`, `Dla:`) zostaje szara.
- **Data minionego wydarzenia:** usuń regułę `.akt-wyd-data.minione` i klasę `minione` z `.akt-wyd-data`, bo na liście miniona data też jest w kolorze. Napis „Wydarzenie się odbyło” zostaje szary.
- **Linki w tekście wpisu** (tylko `.prose`), w `src/styles/zal-tresc.css`:
```css
body .tresc.akt-wydarzenie .prose a { color: var(--d-a); text-decoration-color: currentColor; }
body .tresc.akt-wydarzenie .prose a:hover { color: var(--d-a); text-decoration-thickness: 2px; }
```
  Reguła ma stać po `body .tresc .prose a`. Załączniki, „Nowszy / Starszy wpis” i powrót w banerze zostają jak dziś.
- **„Najbliższe wydarzenia” na wpisie:** `WierszWydarzenia.astro` nie ma własnego `data-dzial`, więc po zmianie wiersze wzięłyby kolor wpisu, także obcych wydarzeń. Mają mieć własny kolor, według tej samej reguły co kolumna „Nadchodzące wydarzenia” na stronie głównej.

**Czego nie zmieniać**
- Baner zostaje granatowy, ze zdjęciem jak dziś. W pasku menu żadnej zmiany.
- Obrony (`Obrona.astro`), sukcesy, ogłoszenia i kariera bez zmian. Strona `AktualnoscZamianaDni.astro` bez zmian.
- Lista Aktualności bez zmian.

**Odbiór**
- Zrzuty przy 1536 i 390 px, jasny i ciemny motyw, PL i EN: wydarzenie Nauki i Popularyzacji, przyszłe i minione, z linkiem w tekście (np. `2026-07-14-szkola-baby-steps-beyond-the-horizon`, `2026-09-23-2-kongres-mlodych-odkrywcow`) → `raport-zrzuty/z21-wydarzenie-*`.
- Kolor etykiety i daty na wpisie taki sam jak w jego wierszu na liście, co najmniej dla 5 wydarzeń (tabela w raporcie).
- Kontrast etykiety, daty i linków z tłem co najmniej 4,5:1 w obu motywach (w jasnym w próbie 5,67:1 Nauka i 6,45:1 Popularyzacja; ciemny zmierz).
- Wpis innego rodzaju niż wydarzenie i obrona wyglądają jak przed zmianą.
- Sprawdź, że `data-dzial` na `.z-pd` nie zmienia na wpisie niczego poza punktami wyżej (np. karta, galeria, załączniki).

## 7. Ciekawostki: nazwisko patrona w każdej karcie — GOTOWE (decyzja 6.11, 12:55)
Właściciel: „W niektórych ciekawostkach zakłada się, że użytkownik domyślnie wie, że chodzi o patrona, np. wypromował doktorów, ostatni gdy miał 87 lat. […] w tekście przynajmniej raz musi pojawić się nazwisko patrona (albo tytuł, albo w tekście, nie ma znaczenia, ale unikamy stwierdzeń on itd.)”. Nowe zdania przejrzał i zatwierdził: „Wszystko jest ok” (artefakt https://claude.ai/artifact/9eGDGaQfxPKbFdyMosbJ1m).

**Zasada**
- W każdej karcie nazwisko patrona pada w `nazwa` albo w `zdanie`, a po angielsku w `nazwa_en` albo w `zdanie_en`.
- „On”, „jego” („he”, „his”) o patronie nie stoją przed jego nazwiskiem.

**Dane:** `.przekazanie\prototypy\21-ciekawostki-nazwisko.json`, układ `{ "<dział>": { "<id karty>": { pola } } }`, razem 76 kart.
- Podmień w `src/data/ciekawostki/<dział>.json` **tylko pola wymienione w tym pliku**: `zdanie`, `zdanie_en`, a w `tom-26-colloquium` także `nazwa` i `nazwa_en`. W `kontinuum-dziedzicznie-nierozkladalne` tylko `zdanie_en`.
- Bez zmian: `id`, `rok`, `sciezki`, `notka`, `stan`, `strona`, `ukryta`, `zrodla`, kolejność kart i zapis pliku (diff tylko w tych wierszach).
- Karta `praca-na-glos` dostaje nowe zdanie, ale zostaje `ukryta`.
- Teksty przenieś dosłownie, bez poprawek.

**README:** w `src/data/ciekawostki/README.md`, przy polach, dopisz zasadę i wskazówkę: `zdanie` najwyżej 115 znaków, bo tyle mają obecne karty.

**Kontrola w `skrypty/sprawdz_tresci.py`**
- Tylko przy wywołaniu bez argumentów (tak uruchamiają go `deploy.yml` i `sprawdz-galaz.yml`).
- Dla każdej karty z 4 plików: `nazwa` + `zdanie` zawiera rdzeń nazwiska (`instytut` Marczewsk, `nauka` Ślebodzińsk, `studia` Knaster, `popularyzacja` Steinhaus); to samo dla `nazwa_en` + `zdanie_en`, chyba że `zdanie_en` jest puste (wtedy `/en` pokazuje tekst polski).
- Błąd w stylu: `src/data/ciekawostki/nauka.json: jedenastu-doktorow: brak nazwiska patrona (PL)`, kod wyjścia 1.
- Zaimków nie sprawdzaj automatycznie: w `dyrektor-instytutu` „kierował nim Marczewski” jest poprawne, bo „nim” to Instytut.

**Odbiór**
- `python3 skrypty/sprawdz_tresci.py` przechodzi dla wszystkich 106 kart. Próba: po chwilowym usunięciu nazwiska z jednej karty skrypt zgłasza błąd i kończy się kodem 1 (zmiany nie commituj).
- Żadne `zdanie` nie ma więcej niż 115 znaków.
- `git diff --stat`: tylko 4 pliki JSON, `README.md` i `sprawdz_tresci.py`.
- Losowanie bez zmian, bo `id` zostają. Zestaw zapisany w `sessionStorage` działa dalej.
- Zrzuty nagłówka podstrony przy 1536 px, PL i EN: `jedenastu-doktorow`, `tom-26-colloquium` (nowy tytuł w jednej linii), `szpilrajn-porzadek`, oraz najdłuższe zdanie z każdego działu → `raport-zrzuty/z21-ciekawostki-*`.
- Weryfikacja faktów przed startem zostaje na liście właściciela. Ten punkt jej nie zastępuje.

## 8. „Na tej stronie”: bez paska przewijania — GOTOWE (decyzja 6.11, 12:56)
Właściciel: „Przy ostatniej pozycji na «Na tej stronie» pojawia się scroll. Wywalić go.” Na jego zrzucie: `/studia/matematyka`, bieżąca pozycja „Akty prawne”, pasek Windows przez całą wysokość listy.

**Prawdopodobna przyczyna:** `.z-spis` ma `overflow-y: auto` (`src/styles/zal-podstrona.css`, linia 25), a znacznik `.z-spis-znacznik` (absolute, `transform` z `scaleY`) na ostatniej pozycji wystaje poza listę: w pomiarze 366,88 px przy wysokości spisu 366,67 px. Właściciel ma skalę ekranu 125%, więc po zaokrągleniu może to wystarczyć do paska. **W emulacji na Linuksie paska nie udało się odtworzyć** (`scrollHeight` = `clientHeight` także przy skali 1,25). Najpierw odtwórz go na Windows i napisz w raporcie, czy się udało.

**Zmiana w `src/styles/zal-podstrona.css`**
```css
.z-spis-lista { overflow-y: clip; } /* dopisz do istniejącej reguły: znacznik nie powiększa obszaru przewijania; w lewo wystaje dalej, bo overflow-x zostaje visible */
.z-spis { scrollbar-width: none; }  /* dopisz do istniejącej reguły */
.z-spis::-webkit-scrollbar { display: none; }
```
- `overflow-y: auto` zostaje: przy bardzo niskim oknie długi spis dalej przewija się kółkiem, tylko bez widocznego paska.
- Telefon (spis schowany) i `.z-pd-prawa > .z-spis` bez zmian.

**Odbiór**
- Chrome na Windows, skala 1, 1,25 i 1,5, okna 1536×730 i 1920×940: `/studia/matematyka`, `/studia/isim` i co najmniej 3 inne strony z długim spisem, także w EN. Na górze strony, na dole i po kliknięciu ostatniej pozycji: `scrollHeight` ≤ `clientHeight` i `offsetWidth` = `clientWidth`. Tabela w raporcie.
- Znacznik widoczny w całości, także te 2 px w lewo od linii.
- Okno 1366×640 i strona z najdłuższym spisem: lista przewija się kółkiem, paska nie ma.
- Zrzuty → `raport-zrzuty/z21-spis-*`.

## 9. Telefon, strona główna: powrót zawsze na górę, bez białego paska — GOTOWE (decyzja 6.11, 13:54)
Właściciel: „powrót na stronę główną w widoku mobilnym powinien zawsze dawać na górę strony, bo nie daje, czasami zostawia biały pasek z quick access”. Punkt 3 tego nie załatwia.

**Powrót na górę (≤ 760 px, `src/scripts/zal/przejazd.ts`)**
- Na stronie głównej `history.scrollRestoration = 'manual'`.
- Przy `pageshow`, także z `e.persisted` (powrót z pamięci przeglądarki): gdy okładka schowana, przywróć ją, i `scrollTo({ top: 0, behavior: 'instant' })`. Bez widocznego przelotu przez Szybki dostęp.
- Dotyczy przycisku „wstecz” przeglądarki, logo, nazwy Instytutu i „← Strona główna”, PL i EN.
- Wyjątek: adres z kotwicą, np. `#szybki-dostep`, działa jak dotąd.
- Właściciel chce „zawsze”, więc „wstecz” po kliknięciu linku w Szybkim dostępie też wraca na okładkę, a nie na miejsce w liście.
- Komputer bez zmian.

**Biały pasek (`src/styles/zal-telefon.css`, `.z-okladka`)**
- Prawdopodobna przyczyna: `min-height: calc(100svh - var(--hdr-h))`. `svh` liczy okno przy wysuniętym pasku adresu. Gdy pasek adresu jest schowany, np. po przewinięciu poprzedniej strony, okno jest wyższe niż okładka i pod nią widać początek Szybkiego dostępu. **W emulacji paska adresu nie ma, więc tego nie potwierdziłem.**
- Zmiana: tuż po tej deklaracji dopisz `min-height: calc(100dvh - var(--hdr-h));`. `svh` zostaje dla starszych przeglądarek.
- Sprawdź przy zmianie wysokości okna: `ResizeObserver` i `y1()` w `przejazd.ts`, brak skoku na Szybkim dostępie, kadr zdjęcia i tytuł okładki.

**Odbiór**
- Tabela w raporcie, emulacja telefonu, PL i EN: `scrollY` = 0 i widoczna okładka po „wstecz” z krawędzi Szybkiego dostępu, z głębi strony i z pamięci przeglądarki oraz po logo, nazwie Instytutu i „← Strona główna”.
- Przy `scrollY` = 0 górna krawędź `#szybki-dostep` nie jest wyżej niż dolna krawędź okna, także po zmianie wysokości okna o 56 px w obie strony.
- `#szybki-dostep` w adresie i zachowanie z punktu 3 bez zmian.
- W raporcie napisz wprost, że prawdziwy pasek adresu właściciel sprawdza na swoim telefonie.

## 10. Okładka strony głównej: krócej rozmazane zdjęcie — GOTOWE (decyzja 6.11, 14:03)
Właściciel: po wejściu na stronę główną zdjęcie przez ułamek sekundy jest rozmazane. Zatwierdził trzy zmiany niżej. **Odrzucił zmniejszanie rozdzielczości na telefonie: zestaw plików i rozmiary zostają bez zmian.** Rozmyta wersja zastępcza z zlecenia 13 zostaje na wolniejsze łącza.

**Zmiany (tylko okładka, PL i EN; `src/components/zal/Okladka.astro`, `src/components/ZdjecieZ.astro`, nagłówek strony głównej)**
1. **Wczytywanie od razu:** w `<head>` strony głównej `<link rel="preload" as="image" type="image/avif" imagesrcset="…" imagesizes="…" fetchpriority="high">`. `imagesrcset` i `imagesizes` muszą być dokładnie takie jak w `<source type="image/avif">` zdjęcia okładki, z tych samych danych (`rozmiarOkl`, szerokości, `jakosc`), inaczej przeglądarka pobierze plik dwa razy. Przeglądarka bez AVIF pominie link i zadziała jak dziś.
2. **Pokazywanie po zdekodowaniu:** pełne zdjęcie okładki z `decoding="sync"`.
3. **Bez płynnego wejścia przy szybkim wczytaniu:** w `onload` tego zdjęcia, przed dodaniem `z-wczytane`: `if (performance.now() < 400) this.style.transition = 'none';`. Przy wolniejszym wczytaniu przejście 0,35 s i rozmyta wersja zostają.

Wzór obu ostatnich jako opcja `ZdjecieZ` używana tylko przez okładkę. Banery działów, podstron i Aktualności bez zmian, tak samo komputerowy i telefonowy układ okładki.

**Odbiór**
- Tabela przed i po, nagranie klatek (np. CDP `Page.startScreencast`), czas od początku wejścia do ostrego zdjęcia: ponowne wejście oraz pierwsze wejście przy 50 i 10 Mb/s, 1920×940 i telefon. Próba w emulacji Linux dała przy 1920×940: ponowne ok. 0,6 s → 0,3 s, 50 Mb/s ok. 1,0 s → 0,85 s, 10 Mb/s bez zysku.
- Przy każdym wejściu zdjęcie okładki pobrane raz (Network), ten sam plik co dziś przy 1920×940, 1536×730, 412×839 (2,625) i 390×664 (3). Żadna nowa wersja pliku.
- Bez JavaScriptu i przy `prefers-reduced-motion` zdjęcie widać od razu, jak dziś. Kadr z punktu 13 zlecenia 18 i układ okładki (`ULOZ`) bez zmian, bez skoku po wczytaniu.
- Wolne łącze 2 Mb/s: najpierw rozmyta wersja, potem płynne wejście.
- Pozostałe strony nie mają tego `preload`.
