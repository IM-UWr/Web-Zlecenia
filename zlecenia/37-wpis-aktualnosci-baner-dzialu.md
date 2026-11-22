# Zlecenie 37: wpis w Aktualnościach z banerem swojego działu (17.11.2026)

**Decyzje właściciela:**
- 7.11, 20:23 (kolejka, punkt 12): pojedynczy wpis w Aktualnościach ma pokazywać baner swojego działu zamiast banera Aktualności.
- 17.11, 22:44: dorzucić do kolejki zleceń dla Code. Miejsce w kolejce: po zleceniu 34 (tryb ciemny), przed 33.

**Zakres:**
- **Zmieniają się:** strony pojedynczych wpisów `/aktualnosci/<wpis>` i `/en/aktualnosci/<wpis>`, na komputerze i telefonie.
- **Bez zmian, z banerem Aktualności:** lista `/aktualnosci`, Kalendarz, Obrony doktorskie i „Warto wiedzieć”.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push na `main` dopiero po „push” właściciela.
- Najlepiej po zleceniu 32, które rusza `PasekMenu.astro` i `PanelMenu.astro`.
- Najlepiej także po zleceniu 34 (tryb ciemny), bo jego zrzuty odbioru obejmują wpis `/aktualnosci/2026-05-22-mirek-i-wrobel-frontiers-of-science-award/` jeszcze z banerem Aktualności.
- Numery linii poniżej są z 17.11 i mogły się przesunąć; szukaj po nazwach.
- Raport `RAPORT-ZLECENIE-37.md`, zrzuty `raport-zrzuty/z37-*`. Bez subagentów.

## Stan dziś

**Dział wpisu.** Liczy go już `dzialWpisu` w `src/lib/patroni.ts` (ok. linii 102–112) z pól Rodzaj, Dla kogo i Zakład:
1. sukces, obrona → Nauka;
2. kariera → Studia;
3. wydarzenie: jeśli pierwszym odbiorcą są kandydaci → Popularyzacja, w przeciwnym razie Nauka;
4. pozostałe: studenci lub kandydaci → Studia; wpisany zakład → Nauka; reszta → Instytut.

Tej samej reguły używają wiersze listy Aktualności (`WierszAktualnosci.astro`) i Szybki dostęp (`DrugiEkran.astro`). Pola „Dział” w CMS nie ma i na razie nie trzeba.

**Dział strony liczony z adresu (`dzialZeSciezki`):**
- `src/layouts/Baza.astro`:
  - ok. linii 82: `data-dzial` na `<body>`;
  - ok. linii 146: „Następna strona w dziale”.
- `src/components/NaglowekStrony.astro`, ok. linii 42: `banerAktualnosci(…) ? undefined : dzialZeSciezki(…)`.
- `src/components/zal/PasekMenu.astro`, ok. linii 24: podświetlenie działu w pasku menu.
- `src/components/zal/PanelMenu.astro`, ok. linii 46: rozwinięty dział w hamburgerze.

**Przypięcie do banera Aktualności:**
- `/aktualnosci/…` jest przypięte do banera Aktualności przez `banerAktualnosci` (`patroni.ts`, ok. linii 117).
- `NaglowekZ.astro`, ok. linii 61 (`fotoNat`): zdjęcie Aktualności w naturalnych kolorach.

**Wpis.** `src/views/Aktualnosc.astro` (ok. linii 60) przekazuje do `src/components/zal/Podstrona.astro` prop `dzial` tylko dla wydarzeń (`oWydarzeniu ? dzialWpisu(d) : undefined`). `Podstrona` używa go wyłącznie do kolorów treści (`.z-pd[data-dzial]`, ok. linii 72; zlecenie 21, punkt 6), nie do banera.

## Docelowo

1. **Baner działu na każdym wpisie** (PL i EN):
   - dział według `dzialWpisu`;
   - wariant podstrony działu: sygnet patrona, kolor i zdjęcie działu, tak jak inne podstrony działu;
   - tytuł banera: tytuł wpisu;
   - link „wstecz” bez zmian: „Wszystkie aktualności” → `/aktualnosci`.
2. **Jak to zrobić:**
   - Dodaj opcjonalny prop `dzial` w `Baza.astro`. Ma pierwszeństwo przed `dzialZeSciezki` i `banerAktualnosci`.
   - `Podstrona.astro` przekazuje go dalej do `Baza` oraz do `NaglowekStrony` → `NaglowekZ`.
   - `Aktualnosc.astro` podaje `dzialWpisu(d)` dla **każdego** wpisu.
   - **Kolory treści wpisu zostają jak dziś:** w kolorze działu tylko wpisy o wydarzeniach. Rozdziel dział banera od dotychczasowego `dzial` w `Podstrona` (kolory treści), np. osobnym propem, żeby zwykłe wpisy nie dostały kolorów działu w treści.
3. **Menu:**
   - Pasek menu i hamburger podświetlają **dział wpisu**, na komputerze i telefonie. To ustawienie domyślne; przy odbiorze właściciel może zdecydować, że ma zostać podświetlenie Aktualności.
   - `PasekMenu` i `PanelMenu` biorą dział z `Baza`, gdy jest podany, a w przeciwnym razie z adresu, jak dziś.
4. **Bez skutków ubocznych:**
   - **„Następna strona w dziale” i „Zgłoś błąd”** pod treścią: zachowanie jak dziś. Nie dokładaj ich wpisom tylko dlatego, że mają teraz dział.
   - **`data-dzial` na `<body>`:** sprawdź, co od niego zależy (tło, kolory, skrypty). Zdecyduj, czy wpis ma go dostać, tak żeby wygląd treści nie zmienił się poza banerem, i opisz decyzję w raporcie.
   - **Listy w stylu Aktualności** (lista Aktualności, Kalendarz, Obrony doktorskie, „Warto wiedzieć”): baner Aktualności bez zmian, `banerAktualnosci` zostaje dla nich.
   - **Przejścia między stronami** (lista → wpis → „wstecz”): bez skoków, baner zmienia się przez przenikanie.
   - **Ciekawostka / znak w banerze podstrony:** tak jak na innych podstronach działu. Jeśli na wpisie przeszkadza (np. długi tytuł wpisu), zaproponuj w raporcie ukrycie ze zrzutem, ale nie wdrażaj.
5. **Komentarze:** zaktualizuj je przy `banerAktualnosci` w `patroni.ts`, w nagłówku `NaglowekZ.astro` (opis zlecenia 27) i w `Podstrona.astro` (opis propów).

## Odbiór lokalny

- **Zrzuty przed/po:**
  - po jednym istniejącym wpisie z każdego działu, np. sukces → Nauka, kariera → Studia, wydarzenie dla kandydatów → Popularyzacja, ogłoszenie bez odbiorców → Instytut;
  - każdy wpis w PL i EN;
  - ekrany: komputer 1536×864 i telefon 390×844;
  - tryb jasny i ciemny.
- **Listy bez zmian:** lista Aktualności, Kalendarz, Obrony doktorskie i „Warto wiedzieć” mają 0 różnic w porównaniu pikselowym.
- **Kolory treści:** zwykły wpis ma treść w kolorach jak dziś, a wpis o wydarzeniu jak dziś w kolorze działu.
- **Menu:** na wpisie podświetlony jest dział wpisu, w pasku i w hamburgerze, na komputerze i telefonie.
- **Przejścia:** lista → wpis → „wstecz”, nagranie albo seria zrzutów, bez skoków.
- **Kontrole:** konsola bez błędów, `astro check` bez nowych błędów.
- **Stop:** raport ze zrzutami i czekanie na „push”.

## Kryteria odbioru

- [ ] Każdy wpis ma baner swojego działu według `dzialWpisu` (PL i EN, komputer i telefon).
- [ ] Lista Aktualności, Kalendarz, Obrony doktorskie i „Warto wiedzieć” bez zmian.
- [ ] Menu podświetla dział wpisu.
- [ ] Kolory treści wpisów jak dziś.
- [ ] „Następna strona w dziale” i „Zgłoś błąd” jak dziś.
- [ ] Raport ze zrzutami przed/po.
