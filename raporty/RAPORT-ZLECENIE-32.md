# Raport — zlecenie 32: menu na komputerze jako zwarta lista; orzeł UWr prowadzi do UWr

**Status: zrobione i wypchnięte 18.11.2026, 10:29 UTC, w trybie samodzielnym.** Web-Core `main`: `0fa6731b..c2c193e0` (zwykły push, bez force).
- **Push:** przed pushem `fetch` (origin/main bez zmian, `rebase` pusty) i ponowna budowa.
- **Podgląd:** przebieg [44285963010](https://github.com/IM-UWr/Web-Podglad/actions/runs/44285963010) (`przebuduj`), build i deploy zielone, 67 s.
- **Opublikowana strona:** `z-marka-uwr` / `z-okl-uwr` → `https://uwr.edu.pl/`, `z-okl-wydzial` → `https://wmi.uwr.edu.pl/`.
- **Przerwa:** 18.11, 02:06 praca stanęła z kodem w lokalnym commicie. Po wznowieniu zrobiłem `rebase` na zlecenie 39 (`0fa6731b`, bez konfliktów), a odbiór od nowa na tej bazie.
- **Punkt 9 (dopisany 18.11, 11:36):** osobny commit `cbca5051`, wypchnięty 18.11, 10:59 UTC (`c2c193e0..cbca5051`, bez force). Podgląd: przebieg [44290545777](https://github.com/IM-UWr/Web-Podglad/actions/runs/44290545777) zielony, 72 s. Szczegóły w sekcji „Punkt 9” na końcu.

## Zrzuty (lokalnie, `raport-zrzuty/`)
- `z32-przed2/` — **przed**, budowa `main` = `0fa6731b` (z 39 i treścią z 18.11 rano). To właściwa baza porównań.
- `z32-po/` — **po**, wersja wypchnięta.
- `z32-po-pelna-skala/` — pierwsza wersja „po”, z wielkościami pełnej skali (30 / 17,5 / 14,5 / 54 / 17 px). Pokazuje, dlaczego zmniejszyłem o stopień.
- `z32-przed/` — dawne „przed” z 17.11 (`4511613b`, starsza treść). Zostawione, ale nieużywane do porównań.
- **Skrypt:** `z32-skrypt/zrzuty32.mjs`. Każdy folder ma `pomiary.json`.
- **Zawartość folderu:** 4 rozdzielczości (1536×864 przy skali 1,25, 1920×1080, 1280×720, 1024×768). W każdej podstrona (`/studia/plan-zajec/`) z rozwiniętym działem bieżącym, wszystkimi zwiniętymi i w jasnej wersji, a także okładka (zwinięta i ze Studiami) i jasny pasek drugiego ekranu. Do tego telefon 390 i 768 px.

## Wynik (pomiary z `z32-po/pomiary.json`)
| | 1536×864 | 1920×1080 | 1280×720 | 1024×768 |
|---|---|---|---|---|
| góra listy pod przyciskiem | 8 px | 8 px | 8 px | 8 px |
| prawa krawędź vs przycisk | 0 px | 0 px | 0 px | 0 px |
| zwinięte: wysokość / do dołu okna | 441 / 363 px | 441 / 579 px | 441 / 219 px | 441 / 267 px |
| rozwinięty dział: wysokość / do dołu | 692 / 113 px | 692 / 329 px | 644 / 17 px, **przewijanie w liście** | 692 / 17 px (mieści się co do piksela) |
| szerokość zwinięte = rozwinięte | 560 = 560 | 560 = 560 | 560 = 560 | 560 = 560 |
| wiersze linków działu (najwięcej) | 2 | 2 | 2 | 2 |

- **Przed:** panel na całą wysokość okna (864 px przy 1536×864), szerokość 670 px.
- **Teraz:** stałe pismo 26 px (dział), 16 px (link), sygnet 46×55 px we wszystkich rozdzielczościach.
- **Bez pustych pasów między sekcjami:** sekcje leżą jedna pod drugą (zrzuty).
- **Przy pasku** lista jest `fixed`, **na okładce** `absolute`, a położenie liczy `ustawPolozenie()`.

**Klawiatura** (1536×864, podstrona):
- Tab: × → Szukaj → działy (link, przycisk rozwijania) → linki rozwiniętego działu po kolei → Aktualności → Rekrutacja.
- **Następny Tab zamyka listę** i idzie dalej po stronie („← Studia”); bez pułapki fokusu.
- Esc zamyka listę i wraca na hamburger (`aria-expanded="false"`).
- Klik obok zamyka.
- Ponowny klik hamburgera zamyka; dawniej był niemożliwy, bo panel zasłaniał przycisk.
- Shift+Tab z pierwszej pozycji wraca na hamburger, a lista zostaje otwarta.

**Wygląd i ruch** (wartości wyliczone):
- `border-radius` 8 px, cień `0 16px 44px` dookoła;
- zamknięta lista: `opacity 0`, `translateY(-8px)`; przejście 0,18 s;
- przy `prefers-reduced-motion` bez przejść;
- na komputerze bez przyciemnienia (`.z-menu-tlo` ma `display: none`).

**Punkt 8 (PL i EN, okładka, pasek, nagłówek telefonu):**
- orzeł → `https://uwr.edu.pl/` (EN `/en/`), z `aria-label` „Uniwersytet Wrocławski — strona główna UWr (inna strona)”;
- nazwa Wydziału → `https://wmi.uwr.edu.pl/`, z `sr-only` „(inna strona)”;
- nazwa Instytutu → strona główna (`/` lub `/en/`);
- Tab trafia na każdy link osobno.
- **Wygląd znaku:**
  - położenie orła i nazwy przed i po identyczne co do 0,01 px (`getBoundingClientRect`, PL/EN, okładka i pasek);
  - porównanie pikselowe obszaru znaku: **0 różnic** przy 1280, 1536 i 1920;
  - przy 1024 porównać się nie da, bo stary panel na całą wysokość zasłaniał tam część znaku;
  - najechanie: orzeł przygasa do 75%, a napis jak dotąd, każdy link osobno.

**Telefon:**
- porównanie pikselowe 390 i 768 px (menu zwinięte i ze Studiami, strona główna i podstrona): 0 różnic;
- wyjątek to 7 pikseli o 1/255 na stronie głównej przy 390 px. To szum renderowania: dwa przebiegi tej samej wersji różnią się tak samo (2–6 kanałów), a w jednej z trzech par przed/po wyszło 0.

**Kontrole:**
- `npm run check`: 0 błędów, 0 ostrzeżeń, 3 wskazówki, przed i po tak samo;
- `npm run test:jawne`: 47/47;
- konsola po zmianie bez błędów. W „przed” był jeden `ERR_CONNECTION_REFUSED`: zasób spoza lokalnego serwera, niezwiązany ze zleceniem.

## Odstępstwa i decyzje przyjęte samodzielnie
- **Wielkości o stopień mniejsze:** 26 / 16 / 13,5 / 46 / 16 px zamiast pełnej skali 30 / 17,5 / 14,5 / 54 / 17 px.
  - Przyjąłem to, bo zlecenie każe zmniejszyć o stopień, gdy lista wychodzi za duża.
  - Przy pełnej skali na domyślnym ekranie właściciela (1536×864) lista z rozwiniętym działem bieżącym (stan po otwarciu na podstronie) kończyła się 19 px nad dołem okna. Wyglądała więc prawie jak dawny panel na całą wysokość (zrzut `z32-po-pelna-skala/1536x864-podstrona-rozwiniety.png`).
  - Teraz kończy się 113 px nad dołem.
- **Szerokość:** limit `min(560px, 100vw − 32px)` z propozycji zlecenia. Treść jest szersza, więc lista ma zawsze 560 px, a linki działu łamią się w najwyżej 2 wierszach. Szerokość nie zmienia się przy rozwijaniu.
- **Tab za ostatnią pozycją zamyka listę** zamiast pułapki fokusu. Lista nie przyciemnia strony i nie jest oknem modalnym; zlecenie dopuszcza oba warianty.
- **Położenie bez zaokrąglania do pikseli:** przy zaokrąglaniu na pasku wychodziło 9 px zamiast 8 (pasek ma ułamkową wysokość).

## Pytania do właściciela
- **Krzyżyk czy × w hamburgerze?** Krzyżyk zostaje w prawym górnym rogu listy, jak każe zlecenie, a hamburger też zamyka listę. Nie proponuję zamiany: × w liście jest blisko pola „Szukaj” i jest widocznym celem zamknięcia. Jeśli wolisz × w miejscu hamburgera, to osobna mała zmiana.

## Kryteria odbioru
- [x] Na komputerze menu otwiera się jako zwarta lista pod hamburgerem (pasek i okładka).
- [x] Wysokość i szerokość wynikają z treści; sekcje się nie rozciągają; na niskim oknie przewijanie wewnątrz (1280×720 z rozwiniętym działem).
- [x] Stałe wielkości liter i sygnetów, niezależne od wysokości okna.
- [x] Treść, zwijanie działów, wersja jasna, Esc, kliknięcie obok i fokus działają jak dotąd. Ponowny klik hamburgera teraz też zamyka.
- [x] Orzeł UWr prowadzi do uwr.edu.pl na okładce, pasku i telefonie; nazwa wydziału do strony wydziału; adres UWr w jednym miejscu kodu (`UWR_ADRES`).
- [x] Telefon: 0 różnic w menu na zrzutach (poza szumem renderowania, opisanym wyżej).
- [x] Raport ze zrzutami przed/po w czterech rozdzielczościach.
- [x] **Punkt 9:** „Aktualności” i „Rekrutacja ↗” mają tę samą wysokość wiersza co działy; separatory w równych odstępach.

## Do sprawdzenia
- Na swoim ekranie (1536×864, skala 1,25): otwarcie menu na podstronie i na okładce, czy wielkość listy jest dobra. Jeśli wolisz pełną skalę, wystarczy zmienić jeden wiersz w `zal-menu.css` (zmienne `--m-*`).

## Punkt 9: równe odstępy separatorów (dopisany 18.11, 11:36)

**Zmiana** (tylko `src/styles/zal-menu.css`, tylko blok komputera):
- Nowa zmienna `--menu-wiersz: calc(var(--m-s) * 1.2 + 12px)` = sygnet (55,2 px) i po 6 px nad i pod nim. To jedyne miejsce, gdzie wpisana jest wysokość wiersza.
- **Zwinięty dział:** pierwszy rząd siatki ma `calc(var(--menu-wiersz) - 12px)` (12 px to odstępy sekcji, które już były).
- **„Aktualności” i „Rekrutacja ↗”:** sekcja bez odstępów, a link `display: block` ma wysokość `var(--menu-wiersz)`. Cały wiersz jest więc linkiem, a tekst jest wyśrodkowany w pionie. Wcięcie i wielkość pisma bez zmian.
- **Rozwinięty dział:** bez zmian. Stała wysokość dotyczy tylko `section[data-dzial]:not(.rozwiniety)`. Pierwsza wersja miała ją także dla rozwiniętego i wtedy rozwinięty dział urósł o 15,6 px; poprawione przed commitem.
- **Wersja jasna:** te same reguły (jasna lista różni się tylko kolorami).
- **Telefon:** reguły są wewnątrz warunku komputera, więc telefon się nie zmienia.

**Zrzuty** (lokalnie, `raport-zrzuty/`):
- `z32p9-przed/`: wersja `c2c193e0`, czyli punkty 1–8;
- `z32p9-po/`: wersja wypchnięta `cbca5051`.

Każdy folder ma `pomiary.json`. Skrypt to ten sam `z32-skrypt/zrzuty32.mjs`, rozszerzony o wysokości wierszy i test kliknięcia.

**Wynik** (wysokość każdej sekcji z separatorem, px CSS):

| Stan | Przed | Po |
|---|---|---|
| zwinięte działy, każda z 4 rozdzielczości, pasek, okładka, jasny pasek | 68,19 × 4, potem **46,69** i 45,69 | **68,19 × 5** i 67,19 |
| rozwinięty dział (Studia) | 318,94 | 318,94 (bez zmian) |

- **Ostatni wiersz:** ma 1 px mniej, bo nie ma pod nim separatora (`border-bottom: 0`). Odległość od separatora do separatora to wszędzie 68,19 px, rozrzut 0,00 px (kryterium ±1 px).
- **W pikselach ekranu właściciela (skala 1,25):** 68,19 px to 85,2 px, a dawne 46,69 px to 58,4 px. Zgadza się z opisem w zleceniu (ok. 85 i ok. 58).
- **Obszar kliknięcia:** w 4 punktach wiersza (lewy brzeg, góra, dół, prawy brzeg) `elementFromPoint` trafia w link, w obu wierszach, w każdej rozdzielczości.
  - Przy 1280×720 z rozwiniętym działem dolny punkt „Aktualności” wypadał poza listę, bo lista jest tam przewijana.
  - Po przewinięciu listy do końca wszystkie 4 punkty trafiają, także przy 1024×768.
- **Położenie tekstu:** w poziomie równo z nazwami działów (62 px od lewej krawędzi sekcji). W pionie środek tekstu jest 32,75 px od góry wiersza, a wiersz ma 67,2 px.
  - Nazwa działu stoi wyżej (27,3 px), bo pod nią zawsze jest 2-pikselowa kreska działu i wyśrodkowana jest para nazwa + kreska.
- **Wysokość listy:** lista jest wyższa o 43 px (2 × 21,5 px), zgodnie z istotą zmiany. Przy 1536×864 rozwinięta lista kończy się 70 px nad dołem okna (było 113 px).
  - Przy 1024×768 z rozwiniętym działem lista jest teraz przewijana wewnątrz (733 px treści, 692 px miejsca). Dotąd mieściła się o 2 px.
  - Zlecenie przewiduje przewijanie właśnie w tym przypadku (1024×768 i 1280×720 z rozwiniętym działem).
- **Telefon:** 0 różnych pikseli we wszystkich 8 zrzutach (390 i 768 px, zwinięte i rozwinięte, strona główna i podstrona).
- **Kontrole:**
  - `npm run check`: 0 błędów, 0 ostrzeżeń, 3 wskazówki, tak samo jak przed zmianą;
  - `npm run test:jawne`: 47/47;
  - konsola bez błędów.

**Decyzja przyjęta samodzielnie:**
- Na stronie `/aktualnosci/` link „Aktualności” ma pod tekstem kreskę bieżącej strony (6 + 2 px). Tam wyśrodkowany jest tekst razem z kreską (środek tekstu 28,75 px zamiast 32,75 px).
- Przyjąłem to, bo wiersze działów też wyśrodkowują nazwę razem z kreską, a bez tego kreska wisiałaby nisko (11 px nad separatorem, przy 19 px nad tekstem).
- Wysokość wiersza się nie zmienia.
