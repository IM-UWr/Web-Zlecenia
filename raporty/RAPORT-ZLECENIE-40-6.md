# Raport: zlecenie 40, etap 6 — Web-Ustawienia (18.11.2026)

## Stan
> **Aktualizacja 18.11, 17:20:** Web-Ustawienia i część 2 Web-Core wypchnięte 18.11 o 17:06 i 17:08 (przed wieczorem, na Twoje polecenie) — wynik w „Push treści i część 2 Web-Core”.

- **Web-Core, część 1/2** (ikony w stopce, skrypty): opis wypchnięcia niżej, w „Push Web-Core”.
- **Web-Ustawienia: commit gotowy, push wieczorem**, zaplanowany na **22:43** (po 33, 40.1, 40.2, 40.4 i 40.5). Skrypt: `push40_ustawienia.sh` w scratchpadzie.
  - Klon roboczy: `tresci-z40/Web-Ustawienia`, gałąź `praca/40-ustawienia`, commit `05080a9`.
  - **Baza** (świeży `main`): `f145d85` (zlecenie 33 nie ruszało Web-Ustawienia). O 15:30 brak zapisów od bazy.
- **Web-Core, część 2/2** (zdjęcia nagłówków działów z CMS, `NaglowekZ.astro`): **dopiero po pushu Web-Ustawienia**, tego samego wieczoru (skrypt `naglowek40b.sh`, łatka `naglowek40.patch`).

### Dlaczego Web-Core w dwóch częściach
Zlecenie każe pushować najpierw Web-Core, potem treści. Tu podłączenie zdjęć nagłówków **potrzebuje nowych danych**: dziś w `ustawienia.json` są stare, nieużywane kadry (`center 45%` itd.) i inne zdjęcie Aktualności. Kod czytający te pola, wypchnięty przed danymi, zmieniłby na kilka godzin kadr nagłówków na stronach działów i zdjęcie na listach Aktualności. Dlatego:
1. teraz: stopka (dane Facebook i YouTube już są) i skrypty;
2. wieczorem: dane Web-Ustawienia (stary kod ich nie czyta, porównanie: 0 różnic);
3. zaraz potem: kod nagłówków (z nowymi danymi: 0 różnic).

## Co zrobiłem

### Web-Core
- **Stopka** (`StopkaZ.astro`): ikony Facebooka i YouTube z linkami na końcu linii kontaktu, po e-mailu. Dane z pól `facebook` i `youtube`; puste pole = bez ikony. Etykiety: „Instytut na Facebooku” / „Instytut na YouTube”, po angielsku „The Institute on Facebook” / „The Institute on YouTube”. Ikony z istniejącego `Ikona.astro`, 17 px, pole kliknięcia 24 px.
- **Nagłówki działów** (część 2, `NaglowekZ.astro` i `NaglowekStrony.astro`):
  - zdjęcie i kadr działu z CMS; puste pole = zdjęcie i kadr wpisane w kodzie;
  - kadr z CMS działa na stronie działu i na listach Aktualności, Kalendarzu i „Warto wiedzieć” (tam, gdzie dotąd działał kadr z kodu); podstrony mają nadal stały kadr 50% 40%;
  - opis zdjęcia (alt, Studia i Aktualności) tylko przy zdjęciu domyślnym — inne zdjęcie z CMS jest ozdobne (`alt=""`); filtr Nauki (szarość) bez zmian.
- **Skrypty:**
  - `formularze_40.mjs`: część Web-Ustawienia; formularze w grupach; operacje `usun`, `odkryj`, `etykietyEn`, `daneJson`;
  - `kontrola_redaktorow.py`: opcja `--pomin POLE` (pole usunięte albo zmienione decyzją właściciela, pomijane po obu stronach porównania);
  - `sprawdz-jawny-markdown.mjs`: w Web-Ustawienia sprawdza formularze plików deklaracja, prywatność, „O stronie”.

### Web-Ustawienia (commit `05080a9`: `.pages.yml`, `ustawienia.json`, 3 strony)
- **Strona główna i kontakt:**
  - opis formularza: „Tylko właściciel. Okładka strony głównej (zdjęcie, tekst pod nazwą Instytutu, wydarzenia), sekcja „Studiuj matematykę” i menu „Studia”, zdjęcia w nagłówkach działów, kontakt i profile w stopce.”;
  - **usunięte** z formularza i z pliku (decyzja 18.11, lista 1a):
    - `baner.zdjecie_male`, `zdjecie_telefon`, `podpis`, `podpis_en`, `kadr`;
    - `przyciski` (3 przyciski);
  - **Facebook, YouTube:** pola widoczne, z opisem („Ikona z linkiem w stopce każdej strony…; puste = bez ikony”);
  - **Nagłówki działów:**
    - grupa widoczna (dotąd ukryta), zdjęcie i kadr dla 5 działów, z opisami; pole „Wygląd” (`wariant`) ukryte;
    - **wartości** = to, co nagłówek dziś pokazuje (z kodu): kadry `50% 42%`, `50% 30%`, `50% 40%`, `48% 52%`, `50% 40%`, a dla Aktualności zdjęcie `aktualnosci-skok.jpg` (dotąd w danych było nieużywane `aktualnosci.jpg`);
  - **ukryte** (decyzja 18.11, pytanie 3): hasło strony wyszukiwania (PL i EN); wartości zostają w pliku;
  - etykiety „EN: …” → „… EN”; opis zdjęcia okładki z przykładem.
- **„Na skróty”** (opis: pierwsze cztery kafelki w pasku „Szybki dostęp” pod okładką) i **Menu główne** (opis: menu na górze strony; kierunki w menu „Studia” są w „Strona główna i kontakt”); etykiety „… EN”.
- **Deklaracja dostępności, Polityka prywatności, O stronie → jawny Markdown:**
  - `format_tresci: jawne`, `{#id}` przy 9 nagłówkach `##` (PL) i 9 (EN), z dzisiejszymi adresami sekcji;
  - komentarz `UKŁAD JAWNY`;
  - formularz: tytuł, tytuł EN → Treść, Treść EN → reszta; ściągawka jawnego Markdownu; opis formularza „Tekst strony „…” (link w stopce).”;
  - ukryte: hasło (PL i EN), „Bloki wzorca”, `format_tresci`.

## Kontrole
- **Porównanie HTML całej strony** (925 plików): przed = kod `origin/main` + dane z bazy; po = kod obu części + dane z commitu.
  - Różnica w 791 plikach (każda strona HTML) i **tylko jedna**: blok ikon w stopce. Po jego wycięciu: **0 różnic**.
  - Strony ze stopki w jawnym Markdownie i nagłówki działów: **bez zmian**.
- **Próba zmian zdjęć nagłówków** (osobna budowa z danymi testowymi):
  - Instytut — puste zdjęcie i kadr;
  - Nauka — pusty kadr;
  - Studia — inne zdjęcie i kadr 10% 90%;
  - Popularyzacja — kadr 20% 20%.
- **Wynik próby:**
  - Nauka bez zmian;
  - Studia: nowe zdjęcie na wszystkich stronach działu, bez opisu (alt) starego zdjęcia, kadr na stronie działu;
  - Popularyzacja: kadr tylko na stronie działu;
  - Instytut: zdjęcie domyślne, ale zniknęła klasa `ph-z-foto`. Poprawione w części 2 (`NaglowekStrony.astro`: puste zdjęcie = domyślne). Klasa i tak nie zmienia wyglądu nowego nagłówka.
- `sprawdz_pola_cms.py`: **0 problemów** (724 pliki, 16 repozytoriów, Web-Ustawienia z klonu roboczego).
- `sprawdz-jawny-markdown.mjs`: **OK** (3 strony, 18 nagłówków `##`, wszystkie z `{#id}`). Kontrola ujemna: wersja z bazy — błąd „brak ukrytego pola format_tresci”, jak trzeba. Instytut, Nauka, Pracownicy po zmianie skryptu: nadal OK.
- `kontrola_redaktorow.py`:
  - `przed`: 0 zapisów od bazy;
  - `po` (`f145d85` → `05080a9`, z `--pomin` dla pól z decyzji 1a i zdjęć nagłówków): „OK, tylko zmiany z migracji”;
  - bez `--pomin` te same zmiany są wykazane, więc kontrola działa.
- `astro check`: wynik w „Push Web-Core”.

## Przyjąłem sam
- **Miejsce ikon:** koniec linii kontaktu, po e-mailu (to też kanały kontaktu); na telefonie zawijają się z resztą linii.
- **Zdjęcie Aktualności w CMS = `aktualnosci-skok.jpg`**, bo to je nagłówek pokazuje (zlecenie 27). Ogólne zdjęcie stron spoza działów (deklaracja, wyszukiwanie, 404) zostaje w kodzie: nie ma go w formularzu.
- **Kadr z CMS tylko tam, gdzie dotąd działał kadr z kodu** (strona działu, listy Aktualności); podstrony mają stały kadr, inaczej zmieniłby się ich wygląd.
- **Usunięcie pól z 1a także z pliku danych**, nie tylko z formularza (CMS i tak wyciąłby je przy pierwszym zapisie; tak jest od razu porządek, a kontrola wie o tym przez `--pomin`). **Pliki zdjęć zostają** (zlecenie nie każe ich usuwać).
- **Etykiety „… EN” we wszystkich formularzach Web-Ustawienia** (raport 40-0, sekcja 3), także w polach ukrytych.
- **`opublikowany: true` w trzech stronach ze stopki bez pola w formularzu** (tak było: pola „Opublikowany” w Ustawieniach usunięto przy migracji). Zapis w CMS wytnie tę linię; brak pola = opublikowana, więc wygląd się nie zmieni. Nie dodawałem pola. Kontrola `sprawdz-jawny-markdown` to uwzględnia.
- **Kolejność: Web-Core w dwóch częściach, treść pomiędzy** (powód w „Stan”).

## Pytania do Ciebie
1. **Lista 1c** (jak w raporcie 40-5): `partnerzy`, `baner.podpis_telefon`, `baner.podpis_telefon_en` — zostały ukryte, nie usunięte. Usunąć?
2. **Nieużywane pliki zdjęć po usunięciu pól:** `public/pliki/baner/kampus-zmierzch-1200.jpg` (Web-Ustawienia) i `instytut-telefon.jpg` (tylko w `public` Web-Core). Usunąć?
3. **Kadr nagłówka na podstronach:** dziś stały (50% 40%), kadr z CMS działa tylko na stronie działu. Czy kadr z CMS ma działać także na podstronach? To zmieni wygląd podstron Instytutu (42% zamiast 40%) i Nauki (30%).

## Push Web-Core
- **Część 1/2 wypchnięta** o 15:29: `057513dc..1ab56e50`. Przed pushem `fetch` i rebase na zlecenie 43 z drugiego okna (2 commity: plan zajęć, okładka); po rebase budowa OK i `astro check`: 0 błędów, 0 ostrzeżeń.
- **Podgląd zielony:** run 44324807301 zbudował stronę z `1ab56e50`. Na żywo ikony są w stopce PL i EN (etykiety sprawdzone w HTML).
- Wysokość stopki bez zmian przy 1024, 1280, 1366, 1920 i 2560 px oraz na telefonie (375 px), z ikonami i bez nich. Zrzuty: `raport-zrzuty/z40-stopka-komputer-pl.jpg`, `z40-stopka-komputer-en.png`, `z40-stopka-telefon-pl.jpg`.

## Push treści i część 2 Web-Core (18.11, 17:04–17:09, przed wieczorem na Twoje polecenie: „Dobra, zgadzam sie wrażamy teraz”)
- **Web-Ustawienia:** baza `f145d85` = `origin/main`, 0 zapisów od bazy; `sprawdz-jawny-markdown` OK (3 wpisy, 18 nagłówków); `sprawdz_pola_cms.py` 0 problemów; porównanie HTML (stary kod, stare i nowe dane): **0 różnic**; **wypchnięte `f145d85..05080a9`**; kontrola po (z `--pomin` dla pól z decyzji): „OK, tylko zmiany z migracji”.
- **Web-Core część 2/2** (`naglowek40b.sh`): przed budowami `fetch` i rebase na nowy commit drugiej sesji na `main` (`d436ab69`, zlecenie 43, etap 2); nakładka z danymi Web-Ustawienia z `main`; porównanie HTML (kod bez i z łatką, nowe dane): **0 różnic**; `astro check`: 0 błędów, 0 ostrzeżeń; **wypchnięte `d436ab69..5131ebf2`** (zmienia `NaglowekZ.astro` i `NaglowekStrony.astro`).
- Przed uruchomieniem poprawiłem w `naglowek40b.sh` trzy rzeczy: warunek „czysty Web-Core” liczył nieśledzony plik spoza mojej pracy (`skrypty/test-edytora/package-lock.json`) i zatrzymałby skrypt; cofanie łatki i `git add` obejmowały tylko `NaglowekZ.astro`, a łatka zmienia też `NaglowekStrony.astro`.
- Podgląd: **zielony** — przebieg 44343845368 zbudował stronę z `05080a9` i `5131ebf2`. Nagłówki działów wyglądają jak przedtem (0 różnic), teraz z danymi z CMS.

## Następnego dnia (19.11)
- **Test w CMS (Ustawienia → Strona główna i kontakt):**
  - otwarcie: widać Nagłówki działów, Facebook, YouTube; nie widać przycisków ani resztek banera;
  - zapis bez zmian: diff pusty albo tylko kosmetyka formatu JSON;
  - zmiana kadru jednego działu → strona działu po przebudowie.
- **Deklaracja / Prywatność / O stronie:** otwarcie, zapis bez zmian; oczekiwane: znika tylko linia `opublikowany: true`.
- **Podgląd:** ikony w stopce (komputer i telefon, PL i EN), nagłówki działów bez zmian.
- **Przegląd zapisów redaktorów z 24 h po pushu.**
