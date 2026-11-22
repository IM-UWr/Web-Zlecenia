# Raport: zlecenie 36, okładka na dotyku (wariant A)

**Status:** zrobione i wypchnięte 18.11.2026 o 12:54 UTC, w trybie samodzielnym.
- Web-Core `main`: `5772282f..a0e32c28`, jeden commit, zwykły push, bez force.
- Przed pushem:
  - `fetch` pokazał dwa nowe commity drugiej sesji na `origin/main`: `fb54f3f5` (zlecenie 33) i `5772282f` (zlecenie 39);
  - rebase bez konfliktów, bo tamte zmiany nie dotykają okładki;
  - przebudowa z przebazowanego drzewa (`tresci-B/z36-po2`) i powtórzony odbiór dotyku na tej budowie (1366×1024, tablet i laptop, `raport-zrzuty/z36-dotyk-rebase/`): wynik ten sam;
  - `astro check` bez błędów i ostrzeżeń, 5 podpowiedzi, tyle samo co na `main` po zleceniu 33;
  - testy `npm run test:jawne`: 47/47.
- **Podgląd:** przebieg [44308419922](https://github.com/IM-UWr/Web-Podglad/actions/runs/44308419922) jest zielony (budowa 1 min 14 s, wdrożenie 17 s).
- Zlecenie kończy się słowami „Stop: raport z nagraniami i czekanie na push”. Wypchnąłem według zasad trybu samodzielnego, bo wszystkie kontrole przeszły.
- Część „Odłożone” (patron rysuje się raz i przelatuje do banera) zgodnie z decyzją z 22:40 **nie jest wdrożona**.

## Zmienione pliki
- **`src/scripts/zal/okladka.ts`**
  - Nagłówek, punkt 3: opis całego zachowania na dotyku.
  - Palec rozpoznawany przy każdym naciśnięciu: `pointerType === 'touch'`, a nie media query.
  - Klasa `.z-dotyk` na stukniętym kaflu i barwienie.
  - Przejście po dorysowaniu, wyzwalane zdarzeniem `transitionend` ostatniej kreski konturu i detali. Gdy rysunek był już gotowy, liczy licznik 0,3 s, a twardy limit to 0,45 s od naciśnięcia.
  - Blokada kolejnych kliknięć.
  - Przewinięcie, przytrzymanie i palec podniesiony bez kliknięcia gaszą rysunek.
  - Ograniczony ruch: przejście od razu.
  - Atrybut `[data-z-dotyk]` na okładce oznacza, że ostatnim wskaźnikiem był palec.
  - `pageshow` z `persisted` czyści `.z-dotyk`, barwienie i blokadę.
- **`src/styles/zalozyciele.css`**
  - Linia w nagłówku pliku.
  - Selektory `:is(:hover, :focus-visible)` rozdzielone:
    - `:focus-visible` i `.z-dotyk` bez warunku;
    - najechanie w `@media (hover: hover)` i tylko gdy okładka nie ma `[data-z-dotyk]` (7 reguł, plus osobno reguła, która gasi liczby nad strzałką przy środkowych działach).
  - Czasy `.z-dotyk`, które mają pierwszeństwo przed zwykłymi:
    - 18 kresek konturu po 0,2 s z odstępem 6 ms, czyli 17 × 6 ms ≈ 0,1 s;
    - detale 0,2 s po 0,1 s;
    - poświata, kreska i poświata nazwy, nazwisko patrona i barwienie zdjęcia po 0,3 s.
  - Rysunek kończy się po ok. 0,3 s od stanu, w jakim akurat był: przejście CSS rusza od bieżącej wartości.
  - `.z-okl-dz:hover { color: #fff; }` zostaje bez warunku, bo tylko chroni przed globalnym kolorem `a:hover`.
- **`src/components/zal/Okladka.astro`:** bez zmian. Atrybut `data-z-dotyk` ustawia skrypt.

## Jak to działa (dotyk, układ komputerowy od 1024 px)
1. **Naciśnięcie palcem na dziale.** Kafel dostaje `.z-dotyk` i wygląda jak po najechaniu:
   - szkic patrona;
   - poświata kafla;
   - kreska i poświata nazwy;
   - nazwisko patrona w miejscu hasła;
   - zdjęcie barwi się na kolor działu.
2. **Stuknięcie**, czyli `click` po naciśnięciu palcem, lewym przyciskiem, bez klawiszy:
   - `preventDefault()`;
   - kolejne kliknięcia, także w inne działy, są ignorowane;
   - `location.href = kafel.href` w chwili dorysowania, najpóźniej 0,45 s od naciśnięcia.
   - Strona działu ładuje się w tym czasie z wyprzedzeniem (`speculationrules`, Chrome i Edge).
   - Dalej jak z myszą: w banerze działu patron rysuje się od zera.
3. **Przewinięcie:** bez przejścia, patron gaśnie.
   - Normalny sygnał to `pointercancel`, gdy przeglądarka przejmuje palec.
   - Na okładce jest jednak `touch-action: pinch-zoom` (`przejazd.ts`), więc przeglądarka palca nie przejmuje i `pointercancel` nie przychodzi. Dlatego dodatkowo: palec ruszył o ponad 12 px.
4. **Przytrzymanie:** bez przejścia, patron gaśnie.
   - Sygnał to `contextmenu` (podgląd linku na iPadzie, menu na Androidzie) albo naciśnięcie dłuższe niż 0,5 s.
   - 0,5 s to próg długiego naciśnięcia w Chrome; nie każda przeglądarka wysyła `contextmenu`.
5. **Palec podniesiony bez kliknięcia:** po 0,4 s rysunek gaśnie, bo inaczej zostałby narysowany na stałe.
6. **Ograniczony ruch:** bez `.z-dotyk`, przejście od razu, jak dotąd.
7. **Laptop z ekranem dotykowym:** palcem jak tablet, myszą jak komputer.
   - `[data-z-dotyk]` wyłącza reguły `:hover` kafli, bo po stuknięciu przeglądarka zostawia „najechanie” w miejscu palca. Bez tego po „wstecz” patron zostawałby narysowany także na urządzeniu z kursorem.
   - Pierwszy ruch myszą zdejmuje atrybut.
8. **Mysz, klawiatura i telefon:** bez zmian.

## Narzędzia odbioru (lokalnie, `raport-zrzuty/z36-skrypt/`)
- **`dotyk36.mjs`**, w Playwright (Edge), dwa rodzaje kontekstu:
  - **tablet:** `hasTouch` i `isMobile`, czyli `hover: none` i `pointer: coarse`;
  - **laptop dotykowy:** kontekst bez `hasTouch` (`hover: hover`, `pointer: fine`), a stuknięcia jako zdarzenia dotyku CDP (`Input.dispatchTouchEvent`).

  Pomiary:
  - stan kafla w każdej klatce (rAF) od naciśnięcia;
  - zdarzenia: `pointerdown`, `click` z informacją, czy zablokowany, `pointercancel`, `contextmenu`, `beforeunload` (= start przejścia), `pagehide`;
  - klatki ekranu z `Page.startScreencast` od ostatniej klatki przed stuknięciem przez 700 ms, w arkuszach `stukniecie-nauka-<rodzaj>-<ekran>.png`.

  Ekrany: 1366×1024, 1180×820 i 1280×800. Testy: stuknięcie w każdego z czterech patronów, „wstecz”, mysz po dotyku (laptop), przesunięcie palca, przytrzymanie 1,1 s, podwójne stuknięcie, ograniczony ruch.
- **`mysz36.mjs`:** budowa przed (`main` sprzed zlecenia) i po. Porównuje:
  - najechanie i zjechanie myszą (stan co klatkę i zrzuty);
  - kliknięcie;
  - Tab + Enter;
  - telefon i tablet w pionie, piksel w piksel.
- **`cele36.mjs`:** pola dotyku mniejsze niż 44×44 px przy `pointer: coarse` w układzie komputerowym (1366×1024 i 1180×820, sześć stron) oraz zrzuty tabletu w pionie 820×1180.
- **Wyniki:**
  - `raport-zrzuty/z36-dotyk/` (`dotyk.json`, log `z36-dotyk.log`);
  - `z36-dotyk-rebase/` (po rebase);
  - `z36-mysz/` (`mysz.json`);
  - `z36-cele/` (`cele.json`, `arkusz-pion.png`).

## Wynik odbioru

### Stuknięcie w patrona (12 przebiegów na ekran: 4 działy × tablet/laptop, ekrany 1366×1024, 1180×820, 1280×800)

| Ekran | Rodzaj | Rysunek gotowy (od naciśnięcia) | Start przejścia | Nowa strona (z wczytaniem z lokalnego serwera) |
|---|---|---|---|---|
| 1366×1024 | tablet | 314–323 ms | 331–340 ms | 448–552 ms |
| 1366×1024 | laptop | 314–331 ms | 331–348 ms | 442–507 ms |
| 1180×820 | tablet | 314–315 ms | 331–332 ms | 450–501 ms |
| 1180×820 | laptop | 314–330 ms | 331–347 ms | 444–481 ms |
| 1280×800 | tablet | 314–315 ms | 331–332 ms | 463–526 ms |
| 1280×800 | laptop | 312–315 ms | 330–332 ms | 434–480 ms |

- **Każdy przebieg trafia do swojego działu:** `/instytut/`, `/nauka/`, `/studia/`, `/popularyzacja/`.
- **Stan tuż przed przejściem, za każdym razem:**
  - ostatnia kreska narysowana (`stroke-dashoffset` 0, krycie 1);
  - detale 1;
  - nazwisko patrona 1;
  - poświata 1;
  - barwienie 0,5, czyli pełne;
  - `.z-dotyk` obecne.
- **Kliknięcie** przychodzi 52–125 ms po naciśnięciu i jest zablokowane. Przejście rusza w klatce po końcu rysowania, a nie po limicie 0,45 s.
- **Arkusze klatek:** `z36-dotyk/stukniecie-nauka-{tablet,laptop}-{1366x1024,1180x820,1280x800}.png`. Na nich szkic, nazwisko i barwienie narastają od naciśnięcia do ok. 0,3 s, potem strona działu.
- **Po rebase** (`z36-dotyk-rebase/`, 1366×1024): rysunek gotowy po 314–315 ms, przejście po 331–332 ms.

### Przesunięcie, przytrzymanie, podwójne stuknięcie
- **Przesunięcie palca zaczęte na patronie** (wszystkie ekrany, tablet i laptop):
  - 0 przejść;
  - w trakcie przesuwania `.z-dotyk` było (max 1), po nim nie ma;
  - okładka niezabarwiona, nic nie narysowane.

  Zrzuty: `z36-dotyk/przesuniecie-*.png`.
- **Przytrzymanie 1,1 s:**
  - kliknięcie przychodzi po 1118–1137 ms i jest zablokowane;
  - 0 przejść;
  - patron zgaszony, okładka niezabarwiona.

  Zrzuty: `przytrzymanie-*.png`.
- **Podwójne stuknięcie:** jedno przejście, do `/popularyzacja/`. Oba kliknięcia zablokowane, przejście raz.

### „Wstecz” (pamięć przeglądarki, `persisted: true`)
- Na każdym ekranie, tablet i laptop:
  - brak `.z-dotyk`;
  - okładka niezabarwiona (barwienie 0);
  - żaden patron nie jest narysowany ani podświetlony;
  - liczby nad strzałką widoczne.

  Zrzuty: `z36-dotyk/wstecz-*.png`.
- **Laptop, mysz po dotyku:** po „wstecz” ruch myszy zdejmuje `[data-z-dotyk]`, a najechanie na Naukę rysuje patrona i barwi zdjęcie jak zwykle.

### Ograniczony ruch
- Kliknięcie nie jest blokowane, przejście rusza 0–1 ms po nim (51–69 ms po naciśnięciu).
- `.z-dotyk` ani razu się nie pojawiło.

### Mysz i klawiatura bez zmian (1366×1024 i 1920×950, przed i po)
- **Najechanie i zjechanie myszą (Nauka, Popularyzacja):** stan kafla w chwilach 0,3, 0,7, 1,2, 1,8 i 2,5 s jest identyczny przed i po.
  - W chwili 0,1 s różnice sięgają do 0,53 na pierwszej kresce. To przesunięcie o jedną klatkę między ruchem myszy a startem pomiaru; kształt krzywej jest ten sam, a w drugą stronę pojawia się w innych przebiegach.
  - Zrzuty stanu końcowego różnią się o 35–46 px, wszystkie w ramce ok. 9×7 px na środku przy dolnej krawędzi. To podskakująca strzałka „Szybki dostęp” (animacja `z-bob`), a nie kafel.
- **Kliknięcie myszą:** `mousedown` → start przejścia trwa 7–9 ms przed i po.
- **Klawiatura:**
  - 8 × Tab do Nauki, fokus rysuje patrona i barwi zdjęcie;
  - zrzut fokusu: 0 różnic pikseli;
  - Enter → start przejścia 1 ms, przed i po.

### Telefon bez zmian
- **390×844 i 768×1024:** cała strona, 0 różnic pikseli.
- **Dotyk 390×844 i tablet w pionie 820×1180:**
  - zrzuty różnią się o 56 i 46 px, wyłącznie w ramce ok. 11×8 px przy strzałce (`z-bob`);
  - stuknięcie w Naukę przechodzi od razu: 99–103 ms po, 102–127 ms przed.

### Kontrole
- **Konsola:** bez błędów we wszystkich przebiegach.
- **`astro check`:** 0 błędów, 0 ostrzeżeń, 5 podpowiedzi, jak na `main`.
- **Testy:** 47/47.

## Do raportu, bez wdrażania

### Efekty tylko pod kursorem w układzie komputerowym
- **Okładka: szkic patrona, nazwisko, poświata, barwienie.** Teraz obsłużone dotykiem (to zlecenie).
- **Znak patrona `.z-znak:hover` (rysowanie znaku od nowa):**
  - już było pod `@media (hover: hover)`;
  - na dotyku znak stoi narysowany i nic nie ginie.
- **Podpowiedzi `title`:**
  - pełna nazwa SIAD (`skrotNazwy`) w menu, na stronie działu i w Szybkim dostępie;
  - krótkie etykiety w Spisie.

  Na dotyku nie pokażą się nigdy. Pełna nazwa SIAD jest jedyną treścią widoczną wyłącznie po najechaniu.
- **Kolory i podkreślenia linków po najechaniu oraz powiększenie zdjęcia `.z-dz-suk`:**
  - kosmetyczne, na dotyku nic nie ginie;
  - po stuknięciu mogą zostać „zawieszone” na stukniętym elemencie do następnego dotknięcia, a po „wstecz” widać je na chwilę.
- **Narzędzia i loga na okładce (motyw, język, szukaj, UWr):** tylko zmiana koloru, bez treści. Zostawione.
- **Przyciemnienie przy naciśnięciu** (`:active`, zlecenie 13) działa także palcem. To istniejąca informacja zwrotna, bez zmian.

### Pola dotyku mniejsze niż 44×44 px (`pointer: coarse`, 1366×1024 i 1180×820)
Strony: okładka, drugi ekran, `/studia/`, plan zajęć, Aktualności (lista i wpis), Pracownicy. Pełna lista z liczbą elementów: `raport-zrzuty/z36-cele/cele.json`.


| Element | Wymiary | Uwagi |
|---|---|---|
| Linki paska menu | wys. 40 px | wszystkie strony |
| Motyw i hamburger | 38×38 na podstronach, 40×40 na okładce | |
| Język | 67×40 / 75×40 | |
| Linki marki (UWr, Instytut) | wys. 36–40 px | loga na okładce wys. 30 px |
| Liczby nad strzałką „Szybki dostęp” | 99–135×27 | okładka |
| Strzałka „Szybki dostęp” | 122×29 | okładka |
| Drugi ekran: „i jeszcze N · Wszystkie aktualności”, nagłówek Studiów, „Rekrutacja na studia” | wys. 27, 26, 19 px | strona główna |
| Linki i telefony w stopce | wys. 18–19 px | |
| Filtry Aktualności („Wszystkie” itd.) | 236×29 | |
| Wiersze listy Aktualności | wys. 22–28 px | |
| Strona działu: „← Strona główna”, „Wszystkie”, wiersze aktualności działu | wys. 19, 24, 24 px | |
| Spis (plan zajęć, Pracownicy) | 235×31 | |
| Plan zajęć: przyciski dni | 41–54×36 | |
| Plan zajęć: przyciski semestrów | wys. 36 px | |
| Plan zajęć: linki „N” | 17×17 | najmniejsze |
| Plan zajęć: linki przedmiotów | wys. 20–42 px | |
| „Kalendarz →” | wys. 18 px | |
| Wyszukiwarka Aktualności | 236×37 | wyszukiwarka planu 42 px, Pracownicy (pole i wybór zakładu) 40 px |
| Linki w tekście ciągłym | wysokość wiersza | zwykle się ich nie powiększa |

- **Najpilniejsze:**
  - linki „N” w planie zajęć (17×17);
  - stopka i „Kalendarz →” (18–19 px);
  - liczby i strzałka na okładce (27–29 px).
- **Prosta poprawka bez zmiany wyglądu:** pod `(pointer: coarse)` dodać niewidoczny margines pola dotyku, na przykład pseudo-element z ujemnym `inset`.

### Tablet w pionie (820×1180, układ telefonu)
Zrzuty: `raport-zrzuty/z36-cele/pion-820x1180-*.png` i zestawienie `arkusz-pion.png`.
- **Strona główna:** kafle działów stoją w lewym dolnym rogu, nad nimi dużo pustego zdjęcia. Czytelne, ale wygląda jak powiększony telefon.
- **Strona działu i podstrony:** tekst w jednej kolumnie na całą szerokość, ok. 110+ znaków w wierszu. Za długo do wygodnego czytania (zwykle 60–80).
- **Szybki dostęp:** jedna kolumna kafelków, po prawej dużo pustego miejsca.
- **Ocena:** układ za rzadki w poziomie, a wiersze tekstu za długie.
- **Propozycja, niewdrożona:** w zakresie 700–1023 px ograniczyć szerokość kolumny treści (np. `max-width` ok. 680 px, wyśrodkowana) albo dać Szybkiemu dostępowi dwie kolumny.

## Odstępstwa od zlecenia i powody
- **Nagrania:** zamiast filmów są serie klatek z `Page.startScreencast` w arkuszach. Nagranie `recordVideo` w Playwright wymaga osobno pobieranego ffmpeg, a pobieranie wymaga zgody. Zlecenie dopuszcza serię zrzutów; arkusze mają każdą klatkę ekranu przez 0,7 s od stuknięcia.
- **Dodatkowe progi dotyku**, poza `pointercancel` i `contextmenu` z punktu 3:
  - przesunięcie o 12 px, bo na okładce jest `touch-action: pinch-zoom` i przeglądarka nie wysyła `pointercancel`;
  - przytrzymanie dłuższe niż 0,5 s, bo nie każda przeglądarka (ani emulacja) wysyła `contextmenu`;
  - gaszenie po podniesieniu palca bez kliknięcia, po 0,4 s.
- **`[data-z-dotyk]` poza samym `@media (hover: hover)`:** laptop z ekranem dotykowym ma kursor (`hover: hover`), więc sam warunek medialny nie usunąłby zawieszonego najechania po stuknięciu palcem.
- **Reguła liczb nad strzałką** (gasną przy najechaniu na środkowe działy) też rozdzielona na fokus/`.z-dotyk` i najechanie pod `(hover: hover)`. Była kolejną regułą `:hover` okładki, której zlecenie nie wymienia.
- **`dok/estetyka.md` nie istnieje na `main`**, więc opis zachowania jest w komentarzach nagłówków `okladka.ts` i `zalozyciele.css`. Nie zakładałem nowego pliku dokumentacji.

## Decyzje podjęte samodzielnie (wartości domyślne zlecenia)
- **Czas dorysowania 0,3 s:** przyjąłem, bo to wartość domyślna zlecenia. Zmierzone 312–331 ms.
- **Nazwisko patrona przy stuknięciu: tak.** Przyjąłem, bo to wartość domyślna zlecenia i jedyna okazja, by na dotyku zobaczyć nazwisko.
- **Barwienie zdjęcia przy stuknięciu: tak.** Przyjąłem, bo to wartość domyślna zlecenia i tak samo wygląda najechanie myszą.

## Pytania do użytkownika
1. Czy czas dorysowania 0,3 s, nazwisko patrona i barwienie przy stuknięciu zostają (wartości domyślne)?
2. Czy powiększyć pola dotyku poniżej 44 px pod `(pointer: coarse)` (najpierw plan zajęć, stopka, liczby i strzałka na okładce)? Wygląd zostałby bez zmian.
3. Czy tablet w pionie dostaje węższą kolumnę treści lub dwie kolumny Szybkiego dostępu w zakresie 700–1023 px?
4. Pełna nazwa SIAD jest tylko w podpowiedzi `title`, której na dotyku nie widać. Czy pokazać ją inaczej, np. w tekście strony działu?
5. Czy zdjąć efekty najechania z linków na urządzeniach dotykowych (`@media (hover: hover)`), żeby po stuknięciu nie zostawały zawieszone?

## Do sprawdzenia jutro
- **Prawdziwy iPad (Safari):**
  - stuknięcie w każdego patrona: dorysowanie z nazwiskiem i barwieniem, potem przejście;
  - przewijanie zaczęte na patronie;
  - przytrzymanie (podgląd linku);
  - podwójne stuknięcie;
  - „wstecz”.
- **Tablet z Androidem (Chrome):** to samo, plus przytrzymanie z menu kontekstowym.
- **Laptop z ekranem dotykowym, jeśli jest:** palcem jak tablet, myszą jak zwykle, także zaraz po „wstecz”.
- **Na Podglądzie:** mysz i klawiatura na okładce jak dotąd.
