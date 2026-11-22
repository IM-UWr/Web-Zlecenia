# Zlecenie 36: okładka na dotyku — tablety i duże ekrany dotykowe (17.11.2026)

**Zgłoszenia i decyzje właściciela (17.11, wieczorem):**
- Zgłoszenie: „Duże ekrany dotykowe, tablety, tam się odpala wersja PC […], bo przy naciśnięciu na stronie głównej na patrona nie masz animacji, tylko od razu przejście.”
- Wybrany wariant A: stuknięcie powoduje szybkie dorysowanie patrona, a potem przejście. Bez wariantu „pierwsze stuknięcie pokazuje, drugie przechodzi”.
- **22:40:** „To rysowanie na PC jest spoko, zostawimy to na później. Daj to zlecenie na koniec. Twoja propozycja na tablet jest git.” Wynika z tego, że:
  - **do wdrożenia jest tylko część „Dotyk”**;
  - pomysł „patron rysuje się raz i przelatuje do banera” jest **odłożony** (sekcja na końcu, w tym zleceniu go nie wdrażaj);
  - zlecenie idzie **na koniec kolejki**, po zleceniach 31–34.

**Zakres:**
- Układ komputerowy (`MQ_KOMPUTER`: od 1024 px), czyli także tablety w poziomie i duże ekrany dotykowe.
- Mysz i klawiatura bez zmian.
- Telefon (poniżej 1024 px, w tym tablet w pionie) bez zmian.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push na `main` dopiero po „push” właściciela.
- Najlepiej po zleceniach 32 i 34, bo one też ruszają okładkę i `zalozyciele.css`. Numery linii niżej są z 17.11 i mogły się przesunąć; szukaj po selektorach.
- Raport `RAPORT-ZLECENIE-36.md`, zrzuty i nagrania `raport-zrzuty/z36-*`. Bez subagentów.

## Stan dziś

**Okładka**
- Działy: `src/components/zal/Okladka.astro`, ok. linii 163–166, `<a class="z-okl-dz" data-dzial>` ze szkicem `<Szkic … rodzaj="pelny" duch />`.
- Style: `src/styles/zalozyciele.css`, ok. linii 431–463.
- Skrypt: `src/scripts/zal/okladka.ts`. Barwi zdjęcie na `mouseenter` albo przy fokusie z klawiatury.

**Rysowanie szkicu na okładce**
- Szkic rysuje się tylko na `:hover` / `:focus-visible`: kontur (`stroke-dashoffset` od 1 do 0) i detale (`opacity`).
- Czasy w `zalozyciele.css`, ok. linii 283–288: kontur 1,5 s z odstępem `--i × 45 ms` między kreskami, detale 0,7 s po 0,55 s.
- Po najechaniu w miejscu hasła pojawia się też nazwisko patrona (`.slot .patron`).

**Dotyk**
- W kodzie nie ma `(hover: none)` ani rozpoznawania palca.
- Na tablecie w układzie komputerowym stuknięcie daje najechanie i kliknięcie w tej samej chwili, więc strona przechodzi od razu, a patron się nie rysuje.
- Nazwisko patrona na dotyku nie pojawia się nigdy.

**Wczytywanie z wyprzedzeniem**
- Reguły `speculationrules` w `src/layouts/Baza.astro`, ok. linii 120–126, `eagerness: 'moderate'`.
- Na dotyku strona działu zaczyna się przygotowywać przy naciśnięciu (Chrome i Edge).

## Do wdrożenia: okładka na dotyku (wariant A)

1. **Dotyk rozpoznawany przy każdym naciśnięciu:** `pointerType === 'touch'` w `pointerdown` na `.z-okl-dz`, nie przez media query. Dzięki temu laptop z ekranem dotykowym działa palcem jak tablet, a myszą jak komputer.
2. **Naciśnięcie palcem:**
   - Kafel dostaje klasę, np. `.z-dotyk`. Wygląda tak samo jak po najechaniu: kontur i detale, poświata `::before`, kreska i poświata nazwy, nazwisko patrona w miejscu hasła. Do tego barwienie zdjęcia (`wlacz()` z `okladka.ts`).
   - Rysowanie jest szybsze: kontur z odstępami i detale są gotowe w ok. **0,3 s**, licząc od stanu, w jakim rysunek akurat jest.
   - Czasy `.z-dotyk` mają pierwszeństwo przed `:hover`.
3. **Przewinięcie i przytrzymanie:**
   - dotyczy `pointercancel` (palec ruszył, przeglądarka przewija) i `contextmenu` (podgląd linku na iPadzie, menu na Androidzie);
   - zdejmij `.z-dotyk` i barwienie, bez przejścia do działu.
4. **Stuknięcie** (`click` po naciśnięciu palcem, lewy przycisk, bez klawiszy):
   - wywołaj `preventDefault()` i ignoruj kolejne kliknięcia;
   - po dorysowaniu przejdź: `location.href = kafel.href`. Moment przejścia to koniec przejścia ostatniej kreski i detali albo licznik 0,3 s, przy **twardym limicie 0,45 s**;
   - wczytywanie z wyprzedzeniem rusza już przy naciśnięciu, więc w Chrome i Edge strona działu przygotowuje się w czasie animacji;
   - **dalej jak dziś na komputerze:** przejście do strony działu bez zmian, a w banerze patron rysuje się od zera (część „Odłożone” niżej tego nie zmienia, bo nie jest wdrażana).
5. **Ograniczony ruch** (`prefers-reduced-motion: reduce`): bez `.z-dotyk` i bez czekania, przejście od razu, jak dziś.
6. **Zawieszone najechanie:** przeglądarki dotykowe zostawiają `:hover` na ostatnio stukniętym elemencie, więc po „wstecz” patron może zostać narysowany.
   - Reguły `:hover` okładki (`zalozyciele.css`, ok. linii 431–463) obejmij `@media (hover: hover)`. Selektory `:is(:hover, :focus-visible)` rozdziel; `:focus-visible` zostaje bez warunku.
   - W `pageshow` z `persisted` zdejmij `.z-dotyk`, barwienie i blokadę kliknięć, tak jak dziś barwienie.
7. **Bez zmian:**
   - mysz: najechanie rysuje jak dziś, kliknięcie przechodzi od razu;
   - klawiatura: fokus rysuje, Enter przechodzi od razu.

**Wartości do potwierdzenia przez właściciela przy odbiorze** (wdrażasz domyślne):
- czas dorysowania na dotyku: 0,3 s (zakres 0,25–0,35 s);
- nazwisko patrona pokazywane przy stuknięciu: tak;
- barwienie zdjęcia przy stuknięciu: tak.

## Do raportu, bez wdrażania

- Lista efektów układu komputerowego, które działają tylko pod kursorem (np. rysowanie znaku `.z-znak:hover` w `zalozyciele.css`, ok. linii 380; Szybki dostęp; menu). Przy każdym ocena, co na dotyku ginie i czy coś ważnego jest widoczne wyłącznie po najechaniu.
- Elementy, których pole dotyku jest mniejsze niż 44×44 px w układzie komputerowym przy `(pointer: coarse)`: motyw, język, hamburger, Szukaj itd.
- Tablet w pionie (np. 820×1180), który dostaje wersję telefonową: zrzut i ocena, czy układ nie jest za rzadki.

## Kod i dokumentacja

- **Pliki do zmiany:** `src/scripts/zal/okladka.ts` i `src/styles/zalozyciele.css`.
- **Znaczniki:** w `Okladka.astro` bez zmian, poza ewentualnym atrybutem `data-` potrzebnym skryptowi.
- **Dokumentacja:** zaktualizuj komentarze w nagłówkach tych plików oraz `dok/estetyka.md` (rozdział „Animacje”: zachowanie na dotyku).

## Odbiór lokalny

**Dotyk** (emulacja: Playwright `hasTouch`, `page.tap`; ekrany 1366×1024, 1180×820, 1280×800; nagranie Playwright `recordVideo` albo seria zrzutów co ok. 100 ms)
- Stuknięcie w każdego z czterech patronów: dorysowanie w ok. 0,3 s z nazwiskiem i barwieniem, potem przejście.
- Przesunięcie palca zaczęte na patronie: brak przejścia, patron gaśnie.
- Przytrzymanie: brak przejścia.
- Podwójne stuknięcie: jedno przejście.
- „Wstecz”: okładka czysta, bez narysowanego patrona i bez zabarwienia.
- Ograniczony ruch: przejście od razu.

**Komputer**
- Mysz i klawiatura bez zmian względem dziś: porównanie nagrań przed i po (najechanie, kliknięcie, Tab + Enter).

**Telefon:** 0 różnic. Porównanie pikselowe 390 px i 768 px przed i po.

**Na koniec**
- Konsola bez błędów, `astro check` bez nowych błędów.
- **Stop:** raport z nagraniami i czekanie na „push”. Właściciel sprawdza potem na prawdziwym iPadzie (Safari) i tablecie z Androidem.

## Kryteria odbioru

- [ ] Na dotyku stuknięcie w patrona daje szybkie dorysowanie (ok. 0,3 s) z nazwiskiem i barwieniem, a potem przejście.
- [ ] Przewijanie i przytrzymanie nie przechodzą; podwójne stuknięcie przechodzi raz.
- [ ] Nie ma zawieszonego najechania po „wstecz”.
- [ ] Mysz i klawiatura bez zmian. Laptop z ekranem dotykowym: palcem jak tablet, myszą jak komputer.
- [ ] Telefon: 0 różnic.
- [ ] Raport z nagraniami i listą z sekcji „Do raportu, bez wdrażania”.

---

## Odłożone (decyzja 22:40): patron z okładki rysuje się raz i przelatuje do banera — NIE WDRAŻAĆ w tym zleceniu

Zapis na później. Rysowanie na komputerze zostaje takie, jakie jest.

**Stan dziś:**
- **Zerowanie odwiedzonych działów.** Okładka przy każdym pokazaniu zeruje sessionStorage `im-wizyta-dzialy`: `ZERUJ` w `Okladka.astro`, ok. linii 62–69 (zalecenie 28 ze zlecenia 14). Dlatego każde wejście z okładki jest „pierwsze” i baner dostaje `.z-czeka` (`STAN` w `NaglowekZ.astro`, ok. linii 116–133).
- **Wyłączony przelot.** W `zal-przejscia.css` reguła `[data-z-baner-dzialu].z-czeka :is(.z-szkic-ramka, .z-podpis-ramka) { view-transition-name: none; }` wyłącza przelot szkicu.
- **Skutek:**
  - z okładki szkic nigdy nie przelatuje, leci tylko nazwa działu;
  - w banerze patron rysuje się od zera, a jeśli był już narysowany po najechaniu na okładce, to drugi raz.
- **Podpis:** `szkice.ts`, funkcja `zgrajPodpis`: pisze się w drugiej połowie rysowania szkicu, gdzie `koniec = 1,5 + (n−1)·0,045 s`.

**Pomysł (uzgodniony 17.11, 22:24–22:31):** rysowanie patrona odbywa się raz i nigdy nie zaczyna się od nowa. Baner dokańcza je od miejsca, w którym zatrzymało się na okładce. Podpis dopisuje się na końcu.

| Klik | Zachowanie |
|---|---|
| Od razu | Blady zarys leci do banera i w locie zaczyna się rysować. Kończy w banerze, potem podpis. |
| W trakcie rysowania | Patron leci w połowie narysowany. W banerze dorysowuje się tylko reszta, potem podpis. |
| Po narysowaniu | Gotowy patron leci, ląduje narysowany i od razu dopisuje się podpis. |

**Szkic techniczny:**
- **Zapis stanu w ostatniej chwili.** Przy wolnym wczytywaniu okładka zostaje na ekranie i patron rysuje się dalej, więc stan zapisuj w `pageswap` (zapas: przy kliknięciu i w `pagehide`).
  - Kafel zapamiętaj przy kliknięciu.
  - Zapis do sessionStorage, np. `im-z-okladki` = `{ dz, t, kiedy }`. `t` to równoważny czas rysowania, liczony z rzeczywistego stanu kresek (`getComputedStyle`), bo rysunek mógł się cofać, a na dotyku rysuje się szybciej.
- **Nowy stan banera, np. `.z-dalej`,** ustawiany przed pierwszym narysowaniem strony (przy prerenderze w `prerenderingchange`):
  - zapis z okładki jest jednorazowy i ważny np. 10 s;
  - rysowanie przez animację CSS z ujemnym opóźnieniem (`calc(var(--i) * 45ms - var(--z-t))`), nie przez `transition`, żeby w locie baner nie był przez chwilę pusty;
  - `data-z-start` = `performance.now() − t·1000`;
  - nazwa przejścia szkicu pozostaje włączona, więc szkic przelatuje.
- **Podpis:** tempo jak dziś, start = max(`koniec/2 − t`, 0,3 s od pokazania strony). Bez przelotu, bo na okładce podpisu nie ma.
- **Bez zmian:** wejścia spoza okładki, powrót „wstecz” i ograniczony ruch.
- **Wolne wczytywanie i Firefox:**
  - przelot zaczyna się, gdy strona działu jest gotowa;
  - przy bardzo długim wczytywaniu (Chrome: ok. 4 s) przeglądarka pomija przejście, a w Firefoksie przejść między stronami nie ma; w obu przypadkach baner dokańcza rysowanie bez przelotu.
- **Z wariantem dotykowym:** po wdrożeniu tej części patron po stuknięciu przelatuje już narysowany, a w banerze dopisuje się tylko podpis.
