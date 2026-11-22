# Nowe pola danych do `.pages.yml` (Pages CMS)

Pola dopisane lokalnie w nakładce treści (`src/data`, `src/content`; pliki w `.gitignore`). Przy „push” trzeba:
1. zapisać te pliki w repozytoriach treści (kolumna „Repozytorium”, przypisanie sprawdzone na klonach w `.tresci/`);
2. dopisać pola do `.pages.yml` odpowiednich repozytoriów (etykiety i opisy pól po polsku).

Schematy kolekcji w Web-Core są już gotowe (`src/content.config.ts`). Wszystkie pola są opcjonalne. Puste hasło oznacza, że baner pokazuje opis jak dotąd, albo działa reguła widoku: seminarium pokazuje wtedy nazwę zakładu.
Po angielsku strona bierze tylko pole `_en`, bez zastępowania go polskim.

## Zlecenie 01 (31.10.2026): hasło i liczby w banerze na telefonie

### Pola w plikach JSON i Markdown z danymi
| Plik | Repozytorium | Pole | Przykład |
|---|---|---|---|
| `src/data/dzialy/nauka.json` | Web-Ustawienia | `seminaria_haslo`, `seminaria_haslo_en` | „Otwarte dla wszystkich” / „Open to everyone” |
| ″ | ″ | `konferencje_haslo`, `konferencje_haslo_en` | „Spotkania, które współtworzymy” |
| ″ | ″ | `obrony_haslo`, `obrony_haslo_en` | „Publiczne obrony rozpraw” |
| ″ | ″ | `obrona_haslo`, `obrona_haslo_en` (strona pojedynczej obrony) | „Publiczna obrona doktoratu” |
| ″ | ″ | `granty_haslo`, `granty_haslo_en` | „Projekty NCN, unijne i inne” |
| ″ | ″ | `publikacje_haslo`, `publikacje_haslo_en` | „Nasze wyniki, rok po roku” |
| ″ | ″ | `rocznik_haslo`, `rocznik_haslo_en` (strona rocznika publikacji) | „Rocznik prac Instytutu” |
| ″ | ″ | `sukcesy_haslo`, `sukcesy_haslo_en` | „Nagrody, granty, stypendia” |
| `src/data/dzialy/instytut.json` | Web-Ustawienia | `pracownicy_haslo`, `pracownicy_haslo_en` | „Kontakt do każdego z nas” |
| ″ | ″ | `struktura_haslo`, `struktura_haslo_en` | „Osiem zakładów i pracownia” |
| ″ | ″ | `warto_wiedziec_haslo`, `warto_wiedziec_haslo_en` | „Czym chwalimy się od lat” |
| `src/data/dzialy/studia.json` | Web-Ustawienia | `plan_haslo`, `plan_haslo_en` (Plan zajęć) | „Zawsze aktualny, prosto z USOS” |
| `src/data/ustawienia.json` | Web-Ustawienia | `szukaj_haslo`, `szukaj_haslo_en` | „Osoby, referaty i ogłoszenia” |
| `src/data/wladze.json` | Web-Instytut | `haslo`, `haslo_en` | „Dyrekcja i sekretariat” |
| `src/data/rok-akademicki.md` (front matter) | Web-Studia | `haslo`, `haslo_en` | „Semestry, sesje, kolory dni” |

### Pola w kolekcjach treści (front matter)
| Kolekcja / pliki | Repozytorium | Pole | Przykład |
|---|---|---|---|
| seminaria: `src/content/seminaria/<id>.md` | Web-Sem-<nazwa> (9 repozytoriów) | `haslo`, `haslo_en`; puste daje nazwę zakładu | „Operatory, mnożniki, rozwinięcia” |
| zakłady: `src/content/zaklady/*.md` | Web-Instytut | `haslo`, `haslo_en` | „Geometryczna teoria grup” |
| kierunki: `src/content/kierunki/*.md` | Web-Studia | `haslo`, `haslo_en` | „Od teorii do zastosowań” |
| ″ | ″ | w każdej pozycji `fakty`: `etykieta_krotka`, `etykieta_krotka_en`, czyli krótsza etykieta do liczb w banerze | „punktów ECTS” / „ECTS credits” |
| specjalności: `src/content/specjalnosci/*.md` | Web-Spec-<nazwa> (5 repozytoriów) | `haslo`, `haslo_en` | „Od danych do wniosków” |
| strony: `src/content/strony/**/*.md` | Web-Studia (strony/studia), Web-Instytut (strony/instytut), Web-Nauka (strony/nauka), Web-Ustawienia (deklaracja-dostepnosci, polityka-prywatnosci) | `haslo`, `haslo_en` | „Droga do dyplomu” |
| ″ | ″ | `liczby`: lista stałych liczb do banera, gdzie nie da się ich policzyć z danych. Każda pozycja to `n` (tekst, np. „8” albo „3 lata”), `n_en` (opcjonalnie), `etykieta`, `etykieta_en`. | `- n: "81"`, `etykieta: "zestawów licencjackich"`, `etykieta_en: "bachelor's exam papers"` |

Hasła i liczby są dziś wpisane w tych plikach:
- **seminaria:** wszystkie 9;
- **zakłady:** wszystkie 9;
- **kierunki:** matematyka, siad, isim, szkola-doktorska;
- **specjalności:** wszystkie 5;
- **strony:** studia/* (bez `egzaminy-i-dyplom/zadania`), szkola-doktorska/* (4), instytut/kontakt, instytut/infrastruktura-informatyczna, nauka/sukcesy/historia, deklaracja-dostepnosci, polityka-prywatnosci;
- **stałe `liczby`:** egzaminy-i-dyplom, skrypty, podyplomowe, szkola-doktorska/dokumenty, nauka/sukcesy/historia.

## Zlecenie 06 (01.11.2026): strona główna B2 na telefonie

Wszystkie pola są w pliku `src/data/ustawienia.json`, w repozytorium Web-Ustawienia (formularz „Ustawienia”, w `.pages.yml` grupy `baner` i pola główne). Zdjęcie trzeba dodać do tego samego repozytorium, obok `kampus-zmierzch.jpg`.

| Pole | Przykład / wartość | Uwagi |
|---|---|---|
| `haslo`, `haslo_en` | „Badania, studia i popularyzacja” / „Research, education and outreach” | Bursztynowe hasło pod tytułem i w zwiniętym pasie (telefon). Hasła robocze. Puste pole daje te same teksty zapasowe z kodu. |
| `baner.zdjecie_telefon` | `/pliki/baner/instytut-telefon.jpg` | Zdjęcie banera na telefon (884×1779, ≤ 300 KB). Telefon pobiera tylko je. Puste pole: telefon dostaje zdjęcie komputera przycięte do kadru. Pole obrazka jak `zdjecie` (`path: public/pliki/baner`). |
| `baner.podpis_telefon`, `baner.podpis_telefon_en` | puste (np. „Fot. Corvus, fotopolska.eu”) | Podpis w prawym górnym rogu zdjęcia na telefonie. Puste pole: bez podpisu. Podpis komputera (`podpis`) zostaje osobno. |
| `wydarzenia_dni_telefon` | `30` | Ile dni kalendarzowych naprzód obejmuje lista „Nadchodzące wydarzenia” na telefonie (najwyżej 10 pozycji, widać 3). Komputer dalej używa `wydarzenia_dni_robocze`. |
| `baner.opis`, `baner.opis_en` (pole już było, **zmieniona wartość**) | „Kampus przy placu Grunwaldzkim o zmierzchu: budynek Instytutu Matematycznego wśród drzew, nad Odrą” / „The campus at plac Grunwaldzki at dusk: the Mathematical Institute building among trees, by the Oder” | Tekst alternatywny, wspólny dla zdjęcia komputera i telefonu. |

Nowy plik: `public/pliki/baner/instytut-telefon.jpg` (Web-Ustawienia). Przed pushem trzeba ustalić prawa do zdjęcia (pytanie w dzienniku, sekcja 06).

## Zlecenie 11 (05.11.2026): ciekawostki patronów w nagłówkach podstron (zalecenie 19)

Dane są na razie w repozytorium kodu (Web-Core), w `src/data/ciekawostki/<dział>.json` — po jednym pliku na dział (instytut, nauka, studia, popularyzacja). Opis pól: `src/data/ciekawostki/README.md`. Jeśli ciekawostki mają być edytowane w CMS, pliki można przenieść do repozytorium treści (np. Web-Ustawienia) i dodać formularz w `.pages.yml`; kod czyta je z tej samej ścieżki.

| Pole | Przykład / wartość | Uwagi |
|---|---|---|
| `nazwa`, `nazwa_en` | „Twierdzenie Szpilrajna” / „Szpilrajn’s theorem” | tytuł ciekawostki; na stronie „nazwa, rok”, zawsze w jednej linii |
| `rok`, `rok_en` | „1930”; „lata 30.” / „1930s” | `rok_en` tylko, gdy rok ma słowa |
| `zdanie`, `zdanie_en` | jedno zdanie (do ok. 130 znaków) | pod tytułem, kolumna 300 px |
| `sciezki` | `[{ "d": "M…", "gruba": true }]` | rysunek 200×240; edycja raczej w narzędziu niż w formularzu |
| `stan` (nowe, opcjonalne) | `przypieta` / `ulubiona` / `odpada` | do uzupełnienia po przeglądzie kart z właścicielem; dziś wszystkie bez stanu |
| `strona` (nowe, dla przypiętej) | `/instytut/wladze` | adres podstrony bez `/en` |
| `ukryta` (nowe, opcjonalne) | `true` | dziś: `praca-na-glos`, `seminarium-w-salonie`, `twierdzenie-knastera-reichbacha` |

Tłumaczenia EN wszystkich 106 ciekawostek do przejrzenia: `dok/en/TLUMACZENIA.md`, sekcja 6.

## Zlecenie 14 (05.11.2026): strona „O stronie” (zalecenie 27)

Nowy plik w Web-Ustawienia: `src/content/strony/o-stronie.md` (obok `deklaracja-dostepnosci.md` i `polityka-prywatnosci.md`) i nowy formularz `o-stronie` w `.pages.yml` — oba w łatce `dok/latki/zlecenie-14/Web-Ustawienia.patch` (Web-Core). Pola jak w „Polityce prywatności”, plus hasło na banerze:

| Pole | Przykład / wartość | Uwagi |
|---|---|---|
| `tytul`, `tytul_en` | „O stronie” / „About this site” | link w stopce ma osobny napis w kodzie (`oStronie` w `src/lib/i18n.ts`) |
| `opis`, `opis_en` | „Patroni działów, źródła ilustracji, zgłaszanie błędów i jak zrobiona jest ta strona.” | pod tytułem i w Google |
| `haslo`, `haslo_en` (nowe w tym formularzu) | „Patroni, źródła i kulisy” / „Patrons, sources and how it was made” | hasło na banerze (telefon) |
| `pasek_boczny` | `spis` | spis „Na tej stronie” |
| `body`, `tresc_en` | pięć sekcji: patroni, źródła ilustracji, błąd na stronie, jak zrobiona jest strona, poprzednia strona | **adres redakcji do wpisania** w sekcji „Błąd na stronie?” (dziś „(adres do uzupełnienia)”) |

## Zlecenie 15 (05.11.2026): Popularyzacja

Formularz w `.pages.yml` jest już w łatce `dok/latki/zlecenie-15/Web-Popularyzacja.patch`. Tu tylko spis pól.

**Dział (`src/data/popularyzacja.json`):**

| Pole | Przykład / wartość | Uwagi |
|---|---|---|
| `haslo`, `haslo_en` | „Matematyka dla wszystkich ciekawych” / „Mathematics for the curious” | okładka, baner działu, menu telefonu |
| `o_popularyzacji`, `o_popularyzacji_en` | pięć akapitów | akapity oddzielone pustą linią |
| `o_popularyzacji_fakty` | `wartosc`, `wartosc_en`, `opis`, `opis_en` | „W skrócie”, ten sam kształt co `o_studiach_fakty` |
| `tradycja` | `rok`, `nazwa`, `nazwa_en` | 1989, „Zimowych Szkół”, „Winter Schools”; liczba lat liczona przy budowie strony; nazwa w dopełniaczu |
| `grupy` | usunięte | dawne puste grupy „To be announced” |

**Strony (nowy formularz „Strony Popularyzacji”, `src/content/strony/popularyzacja/`):** `tytul` (nazwa nad kartą „Dla kogo”), `haslo` (tytuł karty), `opis` (zdanie na karcie), `pasek_boczny`, `bloki`, `body`, `tytul_en`, `haslo_en`, `opis_en`, `tresc_en`. Każda strona z katalogu sama dostaje kartę; menu to osobny plik w Web-Ustawienia.

**Nowe pole `bloki` (tak/nie), kolekcja `strony`:** listy Markdown stają się blokami wzorca treści, bez HTML:

| Budowa w treści | Blok |
|---|---|
| lista: `**Tytuł**`, opis, wiersze `Klucz: wartość`, link w osobnym akapicie | dwie kolumny (`ul.dwa`) z parami i linkiem |
| lista: `*etykieta*`, `**Nazwa**`, opis, link | kontakty (`.kontakty`) |
| lista z samych linków albo akapit z samym linkiem | lista linków (`ul.linki`) |
| lista numerowana: `**Tytuł**`, opis, link | ścieżka etapów z „Krok N” / „Step N” (`ol.etapy`) |
| cytat `>` zaczynający się od `**Etykieta**` | ramka uwagi z etykietą |
| pierwszy akapit po pierwszym `##` | akapit w kolorze nagłówków (`.wst`) |

Tabela kalendarza to zwykła tabela Markdown „Kiedy | Co | Dla kogo”. Strzałka ↗ przy linkach poza stronę dochodzi sama.

## Zlecenie 16 (5.11.2026): język referatu

Pole dodane w łatkach `dok/latki/zlecenie-16/Web-Sem-*.patch`, razem z wpisem w `.pages.yml` dziewięciu repozytoriów.

| Plik | Repozytorium | Pole | Przykład |
|---|---|---|---|
| `src/content/referaty/<seminarium>/<plik>.md` | Web-Sem-<nazwa> (9 repozytoriów) | `jezyk` (`pl` / `en`, opcjonalne): przy `pl` na `/en` po tytule jest „(talk in Polish)”, tytuł zostaje w oryginale | `jezyk: pl` |

## Zlecenie 16 (5.11.2026): tekst obrony z danych

Istniejące pola, nowe znaczenie; opis pola `body` w `.pages.yml` zmienia łatka `dok/latki/zlecenie-16/Web-Aktualnosci.patch`. Nowych pól nie ma.

| Plik | Repozytorium | Pole | Znaczenie |
|---|---|---|---|
| `src/content/obrony/<plik>.md` | Web-Aktualnosci | `body` (opcjonalne) | puste: przed terminem zaproszenie, po terminie informacja o odbytej obronie, złożone z danych. Wpisany tekst wygrywa i nie zmieni się sam po terminie |
| ″ | ″ | `tresc_en` (opcjonalne) | to samo dla `/en` |

## Zlecenie 20 (6.11.2026): opisy w pasie działu

Nowe pola, wszystkie opcjonalne. Formularze zmieniają łatki `dok/latki/zlecenie-20/`.

| Plik | Repozytorium | Pole | Znaczenie |
|---|---|---|---|
| `src/data/nawigacja.json` | Web-Ustawienia | `menu[].grupy[].opis`, `opis_en` | krótki opis grupy na kafelku strony działu (komputer). Puste: bez opisu |
| ″ | ″ | `menu[].grupy[].linki[].opis`, `opis_en` | krótki opis strony pod jej nazwą w polu ze stronami. Puste: bez opisu |
| `src/content/kierunki/<plik>.md` | Web-Studia | `menu_opis`, `menu_opis_en` | to samo dla kierunku. Puste: przy krótkiej nazwie w menu (SIAD, ISIM) pełna nazwa kierunku, inaczej bez opisu |

## Zlecenie 22 (6.11.2026): formularze kompletne

Pola opisane wyżej są już w `.pages.yml` na gałęzi `wyglad/zlecenie-16`, wypchniętej w etapie 8. Stan pilnuje `skrypty/sprawdz_pola_cms.py`: 0 problemów. Nowego pola danych dopisuj odtąd od razu do formularza, bo Pages CMS przy zapisie zostawia tylko pola z formularza.

**Dopisane, widoczne (104 pola):**

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Instytut | `zaklady`, `wladze` | `haslo`, `haslo_en` |
| Web-Instytut, Web-Nauka, Web-Studia | `strony` | `haslo`, `haslo_en`, `liczby` (`n`, `n_en`, `etykieta`, `etykieta_en`) |
| Web-Studia | `kierunki` | `haslo`, `haslo_en`; w `fakty`: `etykieta_krotka`, `etykieta_krotka_en`; w `dlaczego.ikona`: wartość `pinezka` |
| Web-Studia | `rok-akademicki` | `haslo`, `haslo_en` |
| Web-Studia | `spec-matematyka-w-ekonomii` | `haslo`, `haslo_en`; w `opiekunowie`: `rola_en` |
| Web-Spec-* (5) | `specjalnosc` | `haslo`, `haslo_en`; w `opiekunowie`: `rola_en` |
| Web-Sem-* (9) | `seminarium` | `haslo`, `haslo_en` |
| Web-Ustawienia | `ustawienia` | `szukaj_haslo`, `szukaj_haslo_en`, `wydarzenia_dni_telefon` |
| Web-Ustawienia | `dzial-instytut` | `haslo`, `pracownicy_haslo`, `struktura_haslo`, `warto_wiedziec_haslo`, każde z `_en` |
| Web-Ustawienia | `dzial-nauka` | `haslo`, `granty_haslo`, `konferencje_haslo`, `obrona_haslo`, `obrony_haslo`, `publikacje_haslo`, `rocznik_haslo`, `seminaria_haslo`, `sukcesy_haslo`, każde z `_en` |
| Web-Ustawienia | `dzial-studia` | `haslo`, `plan_haslo`, każde z `_en` |
| Web-Ustawienia | `deklaracja`, `prywatnosc` | `haslo`, `haslo_en` |

**Ukryte (`hidden: true`, dane zostają w plikach):**

| Repozytorium / formularz | Pola |
|---|---|
| Web-Nauka / `publikacje` | `zrodla`, `do_uzupelnienia` |
| Web-Nauka / `publikacje-wykazy` | `zrodla` |
| Web-Ustawienia / `ustawienia` | `tlo_strony`, `sekcje`, cały `naglowki_podstron`, `haslo`, `haslo_en` (nowa okładka ich nie czyta, decyzja właściciela), `facebook`, `youtube`, `partnerzy`, `przyciski`; w `baner`: `zdjecie_male`, `zdjecie_telefon`, `podpis`, `podpis_en`, `podpis_telefon`, `podpis_telefon_en`, `kadr` |
| Web-Ustawienia / `dzial-studia` | `sekretariat_zakres`, `sekretariat_zakres_en` |

**Widoczne wbrew zleceniu, bo zmienia wygląd (powód w `RAPORT-ZLECENIE-22.md`):** Web-Nauka / `publikacje-wykazy` / `pochodzenie`: lista wyboru `pdf` / `strona`, wybiera zdanie nad wykazem.

**Usunięty formularz:** Web-Ustawienia / `stopka`. Plik `src/data/stopka.json` zostaje, nowa stopka go nie czyta.

**Etykieta:** Web-Studia / `kierunki` / `przyciski` mówi, że wyświetlają się tylko przy Szkole doktorskiej.

## Zlecenie 28 (7.11.2026): kierunki jako jeden Markdown

Formularze są już w `.pages.yml` klonów (gałąź `wyglad/zlecenie-16`, commity lokalne do „push”); pliki danych przerobił `skrypty/migracja/kierunki.py`.

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Studia | grupa „Kierunki” → `kierunki` („Treść”) | tylko `nazwa`, `body` (rich-text, Markdown), `nazwa_en`, `tresc_en` (teraz rich-text, cała strona EN); dawne ok. 100 pól usunięte |
| Web-Studia | grupa „Kierunki” → `kierunki-baner` („Baner”, nowy; `src/content/kierunki-baner/<kierunek>.json`) | `kierunek` (nazwa pliku), `podtytul`, `opis`, `haslo`, `liczby[]` (`wartosc`, `etykieta`, `etykieta_krotka`, każde z `_en`), `podtytul_en`, `opis_en`, `haslo_en` |
| Web-Studia | `przypomnienia` („Przypomnienia o terminach”, nowy; `src/data/przypomnienia.json`) | `przypomnienia[]`: `sprawa`, `podpis`, `data`, `co_roku` (domyślnie tak), `dni_przed` (domyślnie 14), `adres`, `sprawa_en`, `podpis_en`, `uid` (ukryte) |
| Web-Ustawienia | `ustawienia` → `studia.kierunki` (zamiast „Dodatkowych kafelków”) | `adres` (wymagane), `nazwa`, `poziom`, `opis`, `opis_menu`, `w_menu`, `na_stronie_glownej`, `nazwa_en`, `poziom_en`, `opis_en`, `opis_menu_en` |

Pole `podpis` / `podpis_en` przypomnienia jest spoza zlecenia: trzyma dawny podtytuł wydarzenia („1. semestr studiów II stopnia · formularz C3”).

## Zlecenie 29 (7.11.2026): specjalności i strona działu Popularyzacja jako Markdown

Formularze są już w `.pages.yml` klonów (gałąź `wyglad/zlecenie-16`, commity lokalne do „push”); pliki danych przerobiły `skrypty/migracja/specjalnosci.py` i `skrypty/migracja/popularyzacja.py`. Formularz specjalności ma jeden szablon: `skrypty/migracja/specjalnosc.pages.yml` (wstawia go `skrypty/migracja/formularze_specjalnosci.py`).

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Spec-* (5) | grupa „Specjalność: <nazwa>” → `specjalnosc-tresc` („Treść”; `src/content/specjalnosci/<id>.md`) | tylko `nazwa`, `body` (rich-text, Markdown, cała strona), `nazwa_en`, `tresc_en` (rich-text, cała strona EN); dawne listy (`dlaczego`, `etapy`, `przedmioty`, `umiejetnosci`, `tematy_prac`, `dokumenty`, `linki`, `faq`, `dla_kogo`, `kariera` i ich `_en`) są w tekście |
| Web-Spec-* (5) | grupa „Specjalność: <nazwa>” → `specjalnosc-baner` („Baner i kafelek”, nowy; `src/content/specjalnosci-baner/<id>.json`) | `kierunek` (stała lista), `kolejnosc`, `na_stronie_kierunku`, `bez_podstrony`, `kafelek_dla_kogo`, `kafelek_kariera`, `skrot`, `poziom`, `opis`, `haslo`, `zaklad` (stała lista), `opiekunowie[]` (`imie_nazwisko`, `rola`, `rola_en`), `seminaria` (stała lista), `wygaszana`, `poziom_en`, `opis_en`, `haslo_en`, `kafelek_dla_kogo_en`, `kafelek_kariera_en`; ukryte: `do_uzupelnienia`, `zrodla` |
| Web-Studia | grupa „Specjalność wygaszana: Matematyka w ekonomii” (zamiast pozycji `spec-matematyka-w-ekonomii`) | jak wyżej; `kierunek` zostaje odnośnikiem do kolekcji kierunków |
| Web-Popularyzacja | `popularyzacja` → „Strona działu Popularyzacja” (`src/data/popularyzacja.md` zamiast `popularyzacja.json`) | `tytul`, `body` (rich-text, tekst „O popularyzacji”, dawne `o_popularyzacji`), `tytul_en`, `tresc_en` (rich-text, dawne `o_popularyzacji_en`), `wstep`, `haslo`, `o_popularyzacji_fakty[]`, `tradycja[]`, `wstep_en`, `haslo_en`; ukryte: `linki[]` (strona ich nie wyświetla — grupy linków są z menu działu) |

Usunięte z formularza specjalności bez przeniesienia: `ikona` kafelków „Dlaczego warto” (szablon jej nie wyświetlał) i `opublikowany` (zawsze prawda). Wartości są w historii repozytoriów.

## Zlecenie 30 (7.11.2026): teksty działów i stron z listą w repozytoriach działów, porządek formularzy

Formularze są w `.pages.yml` klonów (gałąź `wyglad/zlecenie-16`); pliki danych przerobiły `skrypty/migracja/dzialy.py` (teksty stron), `wpisy.py` (grupa „Karta”, bez `wyroznij_do`) i `formularze.py` (formularze, etapy 1–3).

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Instytut, Web-Nauka, Web-Studia | „Strona działu Instytut / Nauka / Studia” (nowy, pierwszy na liście; `src/data/<dział>.md`) | `tytul` (wymagane), `body` (rich-text, tekst strony działu; u Instytutu z sekcją `## Ostatnie sukcesy`), `tytul_en`, `tresc_en` (rich-text), `wstep`, `wstep_en`, `haslo`, `haslo_en`, liczby „W skrócie” (`o_instytucie_fakty[]` / `badania_fakty[]` / `o_studiach_fakty[]`), Instytut: `kontakt_godziny(_en)`, Studia: `sekretariat_zakres(_en)` — dawne formularze `dzial-*` z Web-Ustawienia (usunięte) |
| Web-Instytut, Web-Nauka, Web-Studia, Web-Aktualnosci (nowa), Web-Pracownicy (nowa) | „Strony” (`src/content/strony`; w Web-Instytut i Web-Nauka dotąd `src/content/strony/<dział>`) — wpis pod adresem strony z listą: `instytut/struktura`, `warto-wiedziec`, `pracownicy`, `seminaria`, `nauka/konferencje`, `nauka/granty`, `nauka/sukcesy`, `nauka/publikacje`, `obrony-doktorskie`, `aktualnosci`, `studia/plan-zajec` | `tytul`, `body` (rich-text, tekst nad listą; sekcja `## Czasopisma redagowane w Instytucie` idzie na miejsce swojej listy), `tytul_en`, `tresc_en` (rich-text), `opis`, `opis_en`, `haslo`, `haslo_en`, `haslo_podstron(_en)` (nowe, Web-Nauka i Web-Aktualnosci: hasło podstron wpisów), `liczby[]`, `pasek_boczny`, `bloki` |
| wszystkie „Strony” i strony prawne Web-Ustawienia (`deklaracja`, `prywatnosc`, `o-stronie`) | kolejność pól | `tytul`, `body`, `tytul_en` („Tytuł EN”), `tresc_en` (teraz rich-text), pod spodem reszta; `bloki` (boolean, domyślnie nie) widoczne: „Kafelki, oś i kontakty z list — zob. ściągawka” |
| Web-Studia | „Rok akademicki” | `tytul`, `body`, `tytul_en`, `tresc_en`, `dalej` („Koniec strony”), `dalej_en` — cztery pola rich-text; potem `opis(_en)`, `haslo(_en)`, `bloki` |
| Web-Aktualnosci | aktualności, obrony | pola wymagane, potem `body` i `tresc_en` (rich-text), reszta; `wyroznij_do` usunięte (z formularza i z 2 plików) |
| Web-Nauka | konferencje, granty | pola wymagane, `body`, reszta; konferencje: `organizatorzy` ukryte |
| Web-Instytut | zakłady, „Warto wiedzieć” | pola wymagane, `body`, `tresc_en`, grupa „Karta” (`karta:` w pliku: zakład — `nazwa_krotka(_en)`, `kierownik`, `telefon`, `opis(_en)`, `haslo(_en)`, `obszary(_en)`, `strona`, `zdjecie`, `zdjecie_opis(_en)`; „Warto wiedzieć” — `rok`, `zajawka(_en)`, `obraz`, `obraz_opis(_en)`, `link`, `link_etykieta(_en)`), reszta pod grupą |
| Web-Nauka | „Publikacje” (`src/data/publikacje.json`) | bez `wstep(_en)`, `czasopisma_naglowek(_en)` (tekst w „Strony” → `nauka/publikacje`) |

Strona bez wpisu w „Strony” nie psuje się: ma tytuł, opis i hasło z kodu (`src/lib/tekstyStron.ts`), bez tekstu nad listą. Treść wszystkich pól Markdown przechodzi przez `remark-wzory-edytora` (ukośniki dopisane przez edytor we wzorach).

## Zlecenie 31 (18.11.2026): termin wydarzenia na kliknięcie, wymagane pola w pozycjach list, nazwy plików z tytułu

Formularze są w `.pages.yml` klonów roboczych (gałąź lokalna `praca/31-galeria-daty-nazwy`, worktree `tresci-z31`); zmiany zrobił `skrypty/migracja/formularze_31.py`, dane aktualności przeniósł `skrypty/migracja/termin.py`. Schemat w Web-Core czyta stary i nowy zapis.

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Aktualnosci | aktualności | `termin` (nowe, lista obiektów, `max: 1`, pod `rodzaj`, z opisem): `dzien` (date, wymagane, `default: ""`), `godzina` (string, wzorzec GG:MM lub G.MM, komunikat „Wpisz godzinę w formacie 13:00”), `dzien_konca` (date, `default: ""`), `godzina_konca` (string, wzorzec), `miejsce` (string), `pozycja`; usunięte `wydarzenie_poczatek`, `wydarzenie_koniec`, `wydarzenie_miejsce` (strona wylicza je z terminu; stary zapis działa przejściowo z ostrzeżeniem w logu budowy) |
| Web-Aktualnosci | aktualności: `galeria`, `zalaczniki` | `plik` wymagany, z opisem „Wymagane. Jeśli nie chcesz …, usuń tę pozycję ikoną kosza.”; `pozycja` |
| Web-Aktualnosci | aktualności, obrony | bez `filename.field: create` (nazwa pliku z tytułu przy zapisie) |
| Web-Nauka, Web-Sem-* (9) | konferencje, granty; referaty | bez `filename.field: create`, jak wyżej (decyzja właściciela 18.11) |
| Web-Aktualnosci | obrony | `data_ogloszenia` z `default: ""`; `recenzje`: `recenzent` i `plik` wymagane, `pozycja` |
| Web-Aktualnosci, Web-Pracownicy, Web-Instytut, Web-Nauka, Web-Studia | „Strony” → `liczby` | `pozycja` |
| Web-Instytut | `o_instytucie_fakty` (`wartosc` wymagana), `wladze/osoby`, `wladze/wydzial/osoby`, `wladze/linki` | `pozycja` |
| Web-Nauka | `badania_fakty` (`wartosc` wymagana), `publikacje/lata`, `czasopisma` | `pozycja`; konferencje: `koniec` z `default: ""` |
| Web-Studia | `o_studiach_fakty` (`wartosc` wymagana), kierunki `baner/liczby` (`wartosc`, `etykieta` wymagane), specjalności `opiekunowie`, `baner/liczby` | `pozycja` |
| Web-Studia | „Kolory dni” | 7 dat semestru z `default: ""`; `przerwy` (`od` wymagane), `zamiany` (`data`, `jak_dzien` wymagane), `wyjatki` (`data`, `kolor` wymagane): daty z `default: ""`, `pozycja` |
| Web-Popularyzacja | `fakty`, `tradycja`, `linki` | `pozycja` |
| Web-Ustawienia | `przyciski` (`etykieta`, `adres`), `partnerzy` (`nazwa`), `skroty/kafelki` (`etykieta`, `adres`), `nawigacja/menu/grupy/linki` (`etykieta`, `adres`) | wymagane jak w nawiasach, `pozycja` |
| Web-Sem-* (9) | referaty → `pliki` | `plik` wymagany (z opisem), `pozycja` |

`pozycja` to ukryte pole tak/nie (`type: boolean`, `hidden: true`): dzięki niemu Pages CMS sprawdza także całkiem pustą pozycję listy (czerwony komunikat i blokada zapisu zamiast `- {}` w pliku). W pliku pojawia się `pozycja: false`; strona i skrypty to pole pomijają.

## Zlecenie 39 (18.11.2026): kierunki w menu i kafelkach tylko z listy, studia podyplomowe jako kierunek

| Repozytorium | Formularz / kolekcja | Pola |
|---|---|---|
| Web-Ustawienia | `ustawienia` → `studia.kierunki` („Kierunki w menu „Studia” i kafelki na stronie głównej”) | nowe: `nazwa_menu` (wymagane), `nazwa_menu_en`, `pozycja`; wymagane teraz: `adres`, `nazwa_menu`, `opis_menu`, `nazwa`; kolejność: adres, nazwa i opis w menu, nazwa, napis i zdanie na kafelku, „pokaż w menu”, „pokaż na stronie głównej” (oba `default: true`), wersje EN; każde pole z opisem i przykładem |
| Web-Ustawienia | `nawigacja` → menu „Studia” → grupa „Kierunki” | ręczny link do studiów podyplomowych usunięty (`linki: []`); kierunki w grupie dalej z listy |
| Web-Studia | `kierunki` | nowy plik `kierunki/podyplomowe.md` (przeniesiony ze „Stron”, `strony/studia/podyplomowe.md` nie ma); baner w tym samym wpisie (`baner.opis`, `haslo`, `liczby`, PL/EN) |

Strona pokazuje pola listy dokładnie tak, jak są wpisane: bez wartości zastępczych (pełna nazwa kierunku, „Kierunek”, zdanie z banera) i bez kierunków spoza listy. Kierunek spoza listy ma stronę `/studia/<plik>`, ale do menu i kafelków trafia dopiero po dopisaniu na listę; budowa wypisuje wtedy ostrzeżenie.

## Zlecenie 33 (18.11.2026): przełącznik „Opublikowane”

Formularze w klonach roboczych `tresci-z33/<repozytorium>` (gałąź lokalna `praca/33-opublikowane`); zmiany zrobił `skrypty/migracja/opublikowany_33.py`. Do repozytoriów treści trafiają w oknie pusha (wieczorem).

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Instytut, Web-Nauka, Web-Studia | strona działu (`strona-dzialu`) | `opublikowany` |
| Web-Popularyzacja | strona działu (`popularyzacja`) | `opublikowany` |
| Web-Aktualnosci, Web-Instytut, Web-Nauka, Web-Popularyzacja, Web-Pracownicy, Web-Studia | „Strony” (`strony`) | `opublikowany` |
| Web-Studia | `kierunki`, `specjalnosci` | `opublikowany` zamiast dawnego „Uwzględniaj w zestawieniach” |

`opublikowany`: `type: boolean`, `default: true`, etykieta „Opublikowane — widoczne na stronie publicznej (na Podglądzie widać zawsze)”, opis „Odznacz, żeby przygotować stronę bez pokazywania jej na stronie publicznej (szkic)”. Miejsce: zaraz pod tytułem (pod parą tytuł / tytuł EN). W 28 plikach danych dopisane `opublikowany: true` (pliki, które pole już miały, bez zmian).

Bez przełącznika: seminaria, referaty, aktualności, obrony, pracownicy, konferencje, granty, zakłady i „Warto wiedzieć” (zakłady i „Warto wiedzieć”: pytanie do właściciela w raporcie). Strona działu ze szkicem zostaje w budowie publicznej, ale bez tekstu z pliku (prowadzi do niej menu); szkic Strony ukrywa też jej podstrony, szkic kierunku jego specjalności.

### Zlecenie 33, uzupełnienie (decyzja właściciela 18.11, ok. 13:05): przełącznik w zakładach i „Warto wiedzieć”

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Instytut | `zaklady` | `opublikowany` (pod „Pełna nazwa”) |
| Web-Instytut | `warto_wiedziec` | `opublikowany` (pod „Tytuł”) |

Ustawienia pola jak wyżej. Dane: 12 z 13 plików miało już `opublikowany: true`; dopisane w 1 pliku (`warto_wiedziec/medale-uniwersytetu-dla-profesorow-marka-bozejki-i-tomasza-rolskiego.md`, wpis z CMS bez pola). Ten sam commit w Web-Instytut co reszta zlecenia 33 (push wieczorem).

## Zlecenie 40, etap 1 (18.11.2026): Web-Instytut — jawny Markdown i formularze jak w Studiach

Zmiany zrobiły `skrypty/jawny-markdown-repo.mjs` (dane) i `skrypty/migracja/formularze_40.mjs` (formularze). Klon roboczy `tresci-z40/Web-Instytut`; do repozytorium treści trafia w oknie pusha (wieczorem, po zleceniu 33).

| Formularz | Pole | Zmiana |
|---|---|---|
| `strona-dzialu`, `strony` | `format_tresci` | **nowe**: `type: string`, `hidden: true`, `default: jawne` (za Treścią EN); w 13 plikach `format_tresci: jawne` |
| `strony` | `bloki` | ukryte (`hidden: true`); w jawnym formacie strona go nie czyta, wartości zostają |
| `zaklady` | `body` | `default`: `<!-- TEKST: Czym zajmuje się zakład. Skład i seminaria strona dopisze sama. -->` |
| `warto_wiedziec` | `body` | `default`: `<!-- TEKST: Pusta Treść = sama zajawka bez własnej strony. -->` |
| `wladze` | `haslo`, `haslo_en`, `do_uzupelnienia` | ukryte (decyzje właściciela 18.11) |

Kolejność pól: tytuł/nazwa, wersja EN, „Opublikowane” → Treść, Treść EN → reszta; w karcie zakładu pola EN pod polskimi. Opisy: ściągawka jawnego Markdownu przy Treści Stron i strony działu, ściągawka zwykłego Markdownu w zakładach i „Warto wiedzieć”.

## Zlecenie 40, etap 2 (18.11.2026): Web-Nauka — jawny Markdown, formularze, strony konferencji

Zmiany zrobiły te same skrypty co w etapie 1. Klon roboczy `tresci-z40/Web-Nauka`; do repozytorium treści trafia w oknie pusha (wieczorem, po zleceniach 33 i 40.1).

| Formularz | Pole | Zmiana |
|---|---|---|
| `strona-dzialu`, `strony` | `format_tresci` | **nowe**: `type: string`, `hidden: true`, `default: jawne` (za Treścią EN); w 7 plikach `format_tresci: jawne` |
| `strony` | `bloki` | ukryte (`hidden: true`); żadna Strona Nauki nie miała ich włączonych |
| `strona-dzialu` | `wstep`, `wstep_en` | etykieta „Opis strony dla Google” (pole nie wyświetla się na stronie) |
| `konferencje` | `body` | etykieta „Opis (opcjonalnie; konferencja z opisem ma własną stronę)”; `default`: szablon Aktualności + `<!-- Program, rejestracja, opłaty: każda informacja w osobnym akapicie. -->` |
| `granty` | `body` | `default`: `<!-- OPIS PROJEKTU: Cel i wyniki projektu. Pusta Treść = strona projektu pokaże same dane. -->` |

Kolejność pól: tytuł, tytuł EN (konferencje i granty: dotąd pod Treścią) → daty, rodzaj → Treść → reszta. Opisy formularzy Konferencje i Projekty i granty (raport 40-0, sekcja 3). Web-Core: konferencja z niepustą Treścią (`maTresc`) ma stronę `/nauka/konferencje/<slug>`.

## Zlecenie 40, etap 4 (18.11.2026): Web-Pracownicy — jawny Markdown i formularze

Te same skrypty co w etapach 1–2. Klon roboczy `tresci-z40/Web-Pracownicy`; do repozytorium treści trafia w oknie pusha (wieczorem, po zleceniu 33). Etap 3 (Web-Aktualnosci) odłożony, bo druga sesja ma niezatwierdzone zmiany jego `.pages.yml` (zlecenie 44).

| Formularz | Pole | Zmiana |
|---|---|---|
| `strony` | `format_tresci` | **nowe**: `type: string`, `hidden: true`, `default: jawne` (za Treścią EN); w `pracownicy.md` `format_tresci: jawne` |
| `strony` | `bloki` | ukryte (`hidden: true`); strona go nie miała włączonego |
| `pracownicy` | — | opis formularza „co to i gdzie widać”; pola bez zmian |

## Zlecenie 44 (18.11.2026): termin zgłoszeń ofert i strona Kariera

Klon roboczy `tresci-B/Web-Aktualnosci`, lokalna gałąź `praca/44-kariera`, commit `e2b51a5` (`.pages.yml` i nowa Strona w jednym commicie); push wieczorem albo po wiadomości właściciela do redaktorów. Web-Core (`23050dd2`) czyta stary i nowy zapis: bez tej zmiany strona Kariera działa z domyślnymi tekstami, a oferty nie mają terminu. Bez migracji danych.

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Aktualnosci | aktualności | `zgloszenia` (**nowe**, „Termin zgłoszeń (tylko oferty: Rodzaj „Kariera”)”, lista obiektów, `max: 1`, zaraz pod `termin`, z opisem): `do_dnia` (date, wymagane, `default: ""`), `pozycja` (ukryte). Strona czyta termin tylko przy `rodzaj: kariera`; przy innym rodzaju albo więcej niż 1 pozycji — ostrzeżenie w logu budowy i w `sprawdz_tresci.py` |
| Web-Aktualnosci | aktualności | `rodzaj`: opis „„Kariera” (oferty pracy, staży i stypendiów) trafia na stronę Kariera (link w Aktualnościach), a nie na listę Aktualności i stronę główną.”; opcje bez zmian |
| Web-Aktualnosci | Strony | nowy plik `src/content/strony/kariera.md` (`tytul`, `tytul_en`, `opis`, `opis_en`, `haslo`, `haslo_en`; adres `/aktualnosci/kariera`, wyjątek od „adres = ścieżka pliku”); opis kolekcji wymienia `kariera.md`. Wpis aktualności o nazwie `kariera.md` jest pomijany (ostrzeżenie), bo zająłby adres strony |

## Zlecenie 40, etap 5 (18.11.2026): 9 repozytoriów Web-Sem-* — jeden wzór formularzy

Skrypt `skrypty/migracja/formularze_40.mjs` (ten sam opis dla 9 repozytoriów). Klony robocze `tresci-z40/Web-Sem-*`; push w oknie wieczornym. Dane bez zmian.

| Formularz | Pole | Zmiana |
|---|---|---|
| `seminarium` | — | opis formularza „co to i gdzie widać”; Opis i Opis EN pod nazwą |
| `seminarium` | `do_uzupelnienia` | ukryte (`hidden: true`, decyzja 18.11); wartości zostają |
| `referaty` | `body` | `default`: `<!-- STRESZCZENIE: Zwykły tekst; wzory w $…$. Slajdy: dodaj w „Pliki” niżej. -->`; Streszczenie i Streszczenie EN przed plikami |

## Zlecenie 40, etap 6 (18.11.2026): Web-Ustawienia — formularze, decyzje 1a, strony ze stopki w jawnym Markdownie

Skrypty `skrypty/migracja/formularze_40.mjs` (formularze i `src/data/ustawienia.json`) i `skrypty/jawny-markdown-repo.mjs --formularze deklaracja,prywatnosc,o-stronie`. Klon roboczy `tresci-z40/Web-Ustawienia`, commit `05080a9`; push w oknie wieczornym. Web-Core: ikony w stopce (`1ab56e50`); zdjęcia nagłówków z CMS osobnym commitem po pushu treści.

| Formularz | Pole | Zmiana |
|---|---|---|
| `ustawienia` | `baner.zdjecie_male`, `baner.zdjecie_telefon`, `baner.podpis`, `baner.podpis_en`, `baner.kadr` | **usunięte** z formularza i z pliku (decyzja 18.11, lista 1a); pliki zdjęć zostają |
| `ustawienia` | `przyciski` | **usunięte** z formularza i z pliku (decyzja 18.11, lista 1a) |
| `ustawienia` | `facebook`, `youtube` | **widoczne** (dotąd ukryte), z opisem; strona: ikony z linkami w stopce, puste = bez ikony |
| `ustawienia` | `naglowki_podstron` | **widoczne** jako „Nagłówki działów”; `zdjecia.*.zdjecie` i `zdjecia.*.kadr` z opisami, wartości = dotychczasowy wygląd (kadry z kodu, Aktualności `aktualnosci-skok.jpg`); `wariant` ukryte. Strona czyta je po części 2 Web-Core (puste = domyślne z kodu) |
| `ustawienia` | `szukaj_haslo`, `szukaj_haslo_en` | ukryte (decyzja 18.11, pytanie 3); wartości zostają |
| `ustawienia`, `skroty`, `nawigacja` | etykiety „EN: …” | → „… EN”; opisy formularzy „Tylko właściciel. …” |
| `deklaracja`, `prywatnosc`, `o-stronie` | `format_tresci` | **nowe**: `type: string`, `hidden: true`, `default: jawne`; w 3 plikach `format_tresci: jawne`, `{#id}` przy 18 nagłówkach `##` |
| `deklaracja`, `prywatnosc`, `o-stronie` | `haslo`, `haslo_en`, `bloki` | ukryte; wartości zostają |
| `deklaracja`, `prywatnosc`, `o-stronie` | kolejność | tytuł, tytuł EN → Treść, Treść EN → reszta |

## Zlecenie 40, etap 7 (18.11.2026): Web-Studia i Web-Popularyzacja — porządek pól

Skrypt `skrypty/migracja/formularze_40.mjs`. Klony robocze `tresci-z40/Web-Studia` i `tresci-z40/Web-Popularyzacja`; push w oknie wieczornym. Format treści był już jawny.

| Repozytorium | Formularz | Pole | Zmiana |
|---|---|---|---|
| Web-Studia | `kierunki` | `baner.liczby.etykieta_krotka`, `baner.liczby.etykieta_krotka_en` | **usunięte** z formularza i z 4 plików kierunków (decyzja 18.11, lista 1a; strona ich nie czyta) |
| Web-Studia | `kierunki` | `baner.*`, `baner.liczby.*` | kolejność: pola EN pod polskimi (nadtytuł, zdanie, hasło; wartość, podpis) |
| Web-Studia | `kierunki` | `baner.podtytul`, `baner.podtytul_en` | opis „Na stronie się nie wyświetla…” (pytanie do właściciela w raporcie 40-7) |
| Web-Studia | `strona-dzialu` | `wstep`, `wstep_en` | etykieta „Opis strony dla Google (1–2 zdania)”, opis z przykładem (nowy nagłówek działu go nie pokazuje) |
| Web-Studia | `strony` | `opis`, `opis_en` | etykieta „Krótki opis (Google i podgląd linku)”, opis „Na samej stronie się nie wyświetla” |
| Web-Studia | `strony` | `haslo` | etykieta „Hasło na banerze (jedna linia)”, opis: hasło i liczby pokazują się tylko razem |
| Web-Studia | `przypomnienia`, `kolory-dni` | pola EN | pod polskimi |
| Web-Popularyzacja | `popularyzacja`, `strony` | kolejność | tytuł, tytuł EN → Treść, Treść EN → reszta; pola EN pod polskimi |
| Web-Popularyzacja | `popularyzacja` | `wstep`, `wstep_en` | etykieta „Opis strony dla Google (1–2 zdania)”, opis z przykładem |
| Web-Popularyzacja | `strony` | `opis`, `haslo` | etykiety „Opis (zdanie na karcie „Dla kogo”)”, „Hasło (tytuł karty „Dla kogo”)”, opisy (nowy baner strony ich nie pokazuje) |
| oba | wszystkie | etykiety „EN: …” | → „… EN” |

## Zlecenie 40, etap 3 (18.11.2026): Web-Aktualnosci

Skrypt `skrypty/migracja/formularze_40.mjs` (funkcja `aktualnosci()`, zgodna z `.pages.yml` sprzed zlecenia 44 i po nim) i `skrypty/jawny-markdown-repo.mjs`. Klon roboczy `tresci-z40/Web-Aktualnosci`; push zaraz po pushu zlecenia 44 (decyzja właściciela 18.11), migracja od nowa na `main` z 44.

| Formularz | Pole | Zmiana |
|---|---|---|
| `aktualnosci` | opis formularza | **nowy**: „Ogłoszenia, wydarzenia, sukcesy i oferty pracy, staży i stypendiów. …; Oferty (rodzaj „Kariera”) są na stronie Kariera i na stronie Studiów.” |
| `aktualnosci` | kolejność | tytuł, tytuł EN → data, rodzaj, termin (po 44: zgłoszenia) → Treść, Treść EN → zajawka, zajawka EN → dla, zdjęcie…, galeria, album, załączniki, zakład |
| `aktualnosci` | `body` | opis: ściągawka zwykłego Markdownu; **`default`**: szablon `<!-- TEKST: … -->` + `<!-- Rejestracja, program, plakat: … -->` (nowe wpisy; istniejące mają Treść) |
| `obrony` | opis formularza | **nowy**: „Publiczne obrony rozpraw doktorskich. Lista w Nauce → Obrony doktorskie. Pusta Treść = strona sama napisze zaproszenie.” |
| `obrony` | `body` | opis: ściągawka; **`default`**: `<!-- Zostaw puste, a strona sama napisze zaproszenie. … -->` (CMS wstawi go też przy otwarciu 5 istniejących obron bez Treści; strona liczy to jak pustą Treść) |
| `obrony` | `tresc_en` | opis poprawiony: pusta Treść EN = zaproszenie z danych, nigdy polski opis |
| `strony` | `format_tresci` | **nowe**: `type: string`, `hidden: true`, `default: jawne`; w plikach Stron `format_tresci: jawne` i komentarz `UKŁAD JAWNY` |
| `strony` | kolejność | tytuł, tytuł EN, Opublikowane → Treść, Treść EN → opis, hasła, liczby, prawy pasek |
| `strony` | `body`, `tresc_en`, `opis` | ściągawka jawnego Markdownu; „Krótki opis (Google i podgląd linku)” z opisem |
| `strony` | `bloki` | ukryte; wartości zostają |
| wszystkie trzy | etykiety „EN: …” | → „… EN” |

## Zlecenie 45 (18.11.2026): Tutornia — link w „W skrócie”, grafik dyżurów, piąty kafelek

Klony robocze `tresci-B/*`, lokalne gałęzie `praca/45-tutornia`; push po „push” właściciela, najpierw Web-Core. Pole `adres` jest opcjonalne, więc kod Web-Core działa też ze starymi formularzami.

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Studia | strona działu (`src/data/studia.md`) | „W skrócie” (`o_studiach_fakty`): **nowe** `adres` („Link (opcjonalnie)”, `string`, po `opis_en`, przed ukrytym `pozycja`), opis z przykładem `/studia/tutornia`; pozycja „Tutornia” ma `adres: /studia/tutornia` |
| Web-Instytut | strona działu (`src/data/instytut.md`) | „W skrócie”: **nowe** `adres`, jw. (przykład `/instytut/zaklady`) |
| Web-Nauka | strona działu (`src/data/nauka.md`) | „W skrócie”: **nowe** `adres`, jw. (przykład `/nauka/granty`) |
| Web-Popularyzacja | strona działu (`src/data/popularyzacja.md`) | „W skrócie”: **nowe** `adres`, jw. (przykład `/popularyzacja/uczniowie`) |
| Web-Studia | Strony studiów | `body`, `tresc_en`: opis wymienia `:::pary (- **Etykieta:** treść)` i `:::grafik` (PL: `Sala:`, `Od:`, `Do:`, jeden dyżur na linię; EN: pusty blok bierze grafik z wersji polskiej); nowy plik `src/content/strony/studia/tutornia.md` (bez nowych pól) |
| Web-Ustawienia | `skroty` | opis kolekcji: pierwsze pięć kafelków na stronie głównej; kafelki z adresem `/studia/rok-akademicki` i `/studia/tutornia` mają podpis na żywo; piąty kafelek „Tutornia” |
| Web-Ustawienia | `nawigacja` | bez nowych pól: piąty link „Tutornia” w grupie „Na co dzień”, `opis` „zajęcia, kalendarz, pierwszy rok, tutornia” / „classes, calendar, first year, tutoring” |

## Zlecenie 47 (18.11.2026): „Warto wiedzieć” pod Instytutem — grupa trzech kolekcji

Skrypty `skrypty/migracja/formularze_40.mjs` (stała `WARTO_WIEDZIEC_47`, funkcja `instytut()`) i `skrypty/migracja/warto_wiedziec_47.py` (treści, menu, `--dodano`). Klony robocze `tresci-B/Web-Instytut`, `tresci-B/Web-Ustawienia`, lokalne gałęzie `praca/47-warto-wiedziec`; push po „push” właściciela, najpierw Web-Core.

| Repozytorium | Formularz | Pola |
|---|---|---|
| Web-Instytut | `warto_wiedziec` | **zmiana**: dawna kolekcja → `type: group` „Warto wiedzieć” z trzema kolekcjami (niżej); stare pliki przeniesione `git mv` do podkatalogów |
| Web-Instytut | `ww_sylwetki` „Sylwetki” (`src/content/warto_wiedziec/sylwetki`, `filename: {primary}.md`, widok: tytuł, lata, Opublikowane, Dodano) | `tytul`* („Imię i nazwisko”), `opublikowany`, `body`, `tresc_en` (jawny Markdown, `code`), `format_tresci` (ukryte, `jawne`), **nowe** `lata`, `podpis`, `podpis_en`, `rocznica_urodzin` (MM-DD, wzorzec), `karta{zajawka, zajawka_en, obraz, obraz_zrodlo}` (**nowe** `obraz_zrodlo`), **nowe** `dodano` (`date`, `default: ""`), `na_glownej`, **nowe** `ulubione`, `zawsze` |
| Web-Instytut | `ww_nagrody` „Nagrody i wyróżnienia” (`…/nagrody`, sortowanie po `kolejnosc`) | `tytul`*, `tytul_en`, `opublikowany`, `body` (szablon z sekcją `## Laureaci z Instytutu {#laureaci}` i `:::laureaci`), `tresc_en`, `format_tresci` (ukryte), **nowe** `kolejnosc` (`number`, `default: 100`), `karta{zajawka(_en), obraz, obraz_opis(_en), link, link_etykieta(_en)}`, `dodano`, `na_glownej`, `ulubione`, `zawsze`, `zrodla` |
| Web-Instytut | `ww_historie` „Historie” (`…/historie`, sortowanie po `karta.rok`) | `tytul`*, `tytul_en`, `opublikowany`, `body`, `tresc_en`, `format_tresci` (ukryte), `karta{rok* (wzorzec ^\d{4}$), zajawka(_en), obraz, obraz_opis(_en), link, link_etykieta(_en)}` (**grupa „Karta” wymagana**, `required: true`: Pages CMS nie sprawdza pól całkiem pustej, niewymaganej grupy, więc bez tego historia bez roku przeszłaby zapis), **nowe** `rocznica` (MM-DD), `dodano`, `na_glownej`, `ulubione`, `zawsze`, `zrodla` |
| Web-Instytut | `strony` | opis: tekst nad listą „Warto wiedzieć” to `instytut/warto-wiedziec.md` (dawniej `warto-wiedziec.md`, plik przeniesiony) |
| Web-Instytut | `strona-dzialu` (`src/data/instytut.md`) | bez nowych pól: „W skrócie” „4 rektorów” (PL i EN, opis z Łukaszewiczem) |
| Web-Ustawienia | `nawigacja` | bez nowych pól: Instytut → grupa „Więcej”, pierwsza pozycja „Warto wiedzieć” / „Highlights” (`/instytut/warto-wiedziec`, opis „sylwetki, nagrody, historie” / „people, awards, stories”); opis grupy „ludzie i historia, informatyka, biblioteka” / „people and history, IT, library” |

Usunięte z formularza „Warto wiedzieć” bez przeniesienia: `dzial` (dziś tylko kolor wiersza; wszystko ma kolor Instytutu) i rok przy PKA (nagrody są bez lat). Pola „Osoby” nie ma: powiązania biorą się z linków w Treści.

## Zlecenie 48 (18.11.2026): przełącznik „Opublikowane” w aktualnościach, opisach seminariów i referatach

Formularze w klonach roboczych `tresci-B/<repozytorium>` (gałąź lokalna `praca/48-opublikowane`); pole dodaje wspólny wzór formularzy `skrypty/migracja/formularze_40.mjs` (Web-Aktualnosci: etap 3; Web-Sem-*: etap 5, jeden wzór dla 9 repozytoriów, zmiana identyczna), wartości w plikach — `skrypty/migracja/opublikowany_48.py`. Do repozytoriów treści trafiają po „push” (wieczorem albo po wiadomości do redaktorów, także redaktorów 9 seminariów).

| Repozytorium | Formularz | Pole i opis |
|---|---|---|
| Web-Aktualnosci | „Aktualności” (`aktualnosci`, także „Rodzaj: Kariera”) | `opublikowany` pod parą tytuł / tytuł EN: „Odznacz, żeby przygotować wpis bez pokazywania go na stronie publicznej (szkic).” |
| Web-Sem-* (9) | „Seminarium: … (opis)” (`seminarium`, formularz jednego pliku) | `opublikowany` pod parą nazwa / nazwa EN: „Odznacz, żeby przygotować seminarium bez pokazywania go na stronie publicznej (szkic). Razem z nim znikną wszystkie jego referaty.” |
| Web-Sem-* (9) | „Referaty” (`referaty`) | `opublikowany` zaraz pod tytułem (bez tytułu EN): „Odznacz, żeby przygotować referat bez pokazywania go na stronie publicznej (szkic).” |

`opublikowany`: `type: boolean`, `default: true`, etykieta jak w zleceniu 33 („Opublikowane — widoczne na stronie publicznej (na Podglądzie widać zawsze)”). Nagłówek `.pages.yml` dostaje linię komentarza „Zlecenie 48: …”. Dane: `opublikowany: true` dopisane tylko w plikach bez pola — Web-Aktualnosci 4 pliki (z 167; pozostałe 163 miały pole od migracji z Avean), Web-Sem-* 0 plików (wszystkie 9 opisów i 31 referatów miało pole). Żaden wpis nie ma `false`.

## Zlecenie 49 (18.11.2026): rodzaj „Seminarium wydziałowe” w Aktualnościach; menu „Warto wiedzieć”

Bez nowych pól. Web-Core zna nową wartość (`z.enum` w `src/content.config.ts`) przed formularzem (push Web-Core → Web-Aktualnosci).

| Repozytorium | Formularz | Zmiana |
|---|---|---|
| Web-Aktualnosci | „Aktualności” (`aktualnosci`), pole `rodzaj` (select) | **nowa opcja** `seminarium-wydzialowe` „Seminarium wydziałowe” pod „Wydarzenie”; opis pola: „„Seminarium wydziałowe” działa jak „Wydarzenie”: dodaj „Termin wydarzenia”. W tytule wpisz prelegenta, np. „Prof. Jan Kowalski”, bez „Seminarium wydziałowe”, bo pokazuje to plakietka. Tytuł wykładu wpisz w zajawce.” + dotychczasowe zdanie o „Karierze” |
| Web-Aktualnosci | kolekcja `aktualnosci` (opis) | „Ogłoszenia, wydarzenia, seminaria wydziałowe, sukcesy i oferty… wpis z terminem trafia też do kalendarza…” (też w `skrypty/migracja/formularze_40.mjs`) |
| Web-Ustawienia | `nawigacja` (dane `src/data/nawigacja.json`) | bez nowych pól: Instytut → grupa „Ludzie” (opis „władze, pracownicy, historia” / „management, staff, history”) ma trzeci link „Warto wiedzieć” / „Highlights” z opisem „profesorowie, odkrycia, nagrody” / „professors, discoveries, awards”; grupa „Więcej” znów „informatyka i biblioteka” / „IT and library” (decyzja właściciela 18.11) |

## Zlecenie 52 (19.11.2026): sylwetki „Warto wiedzieć” — liczby w banerze

Skrypty `skrypty/migracja/formularze_40.mjs` (stałe `LICZBY_SYLWETKI`, `OPIS_TRESCI_SYLWETKI`, funkcja `wstawZa`, blok zlecenia 52 w `instytut()`) i `skrypty/migracja/sylwetki_52.py` (wartości z `.przekazanie/prototypy/52-sylwetki-baner/A-liczby/`, usunięcie bloków `:::w-skrocie`, porządek w sylwetce Tabisza). Klon roboczy `tresci-B/Web-Instytut`, lokalna gałąź `praca/52-sylwetki-baner`; push najpierw Web-Core (zna pole `liczby`), potem Web-Instytut.

| Repozytorium | Formularz | Pole |
|---|---|---|
| Web-Instytut | `ww_sylwetki` „Sylwetki” | **nowe** `liczby` „Liczby w banerze (3 pozycje)”, tuż pod „Podpis EN”: `type: object`, `list` zwinięta (`collapsed: true`, `summary: "{n} {etykieta}"`), pola `n`* „Liczba (np. 1945 albo 20)”, `n_en` „Liczba EN (puste = jak po polsku)”, `etykieta`* „Podpis (np. pierwszy dziekan)”, `etykieta_en` „Podpis EN (puste = podpis polski)”, ukryte `pozycja` (boolean) — jak `liczby` Stron. Opis: „Trzy krótkie pozycje pod podpisem na banerze, np. „1945 · pierwszy dziekan”, „20 · doktorów”. Liczba: same cyfry (rok, liczba, 1800+). Podpis: najwyżej ok. 20 znaków, małą literą, bez linków. Pokazują się pierwsze trzy. Puste = baner bez liczb.” |
| Web-Instytut | `ww_sylwetki`, pole `body` (opis i `default`) | bez `:::w-skrocie`: opis „Sylwetka: wstęp (obok portretu), sekcje ## z {#id}, … Liczby do banera wpisuje się w polu „Liczby”. …”; szablon nowej sylwetki: komentarz TBA ze zdaniem „Liczby do banera wpisuje się w polu „Liczby”.”, szkielet bez bloku `:::w-skrocie` |

Dane: 18 sylwetek dostały `liczby` (3 pozycje, `n_en: ""`); 17 straciło blok `:::w-skrocie` z komentarzem `<!-- W SKRÓCIE: … -->`. Web-Core (`src/content.config.ts`, `WYMAGANE_W_LISTACH.ww_sylwetki`) czyta `liczby` i — gdy pole jest puste — pierwsze 3 punkty starego bloku (z ostrzeżeniem w logu). Nagłówek `.pages.yml` dostaje linię komentarza „Zlecenie 52: …”. Cudzysłowy »…« ze zlecenia w formularzu jako „…” (jak w pozostałych opisach `.pages.yml`).

## Zlecenie 42 (19.11.2026): osoby wybierane ze spisu pracowników; osoby, które odeszły

Wzór formularzy: `skrypty/migracja/formularze_40.mjs` (sekcja „Zlecenie 42”: `KATALOG_42`, `wyborOsoby`, `osobySpoza`, `INNE_42`, funkcje `instytut42`, `nauka42`, `seminaria42`, `studia42`, `pracownicy42`; API `zamienPole`, `dodajFormularz`, `wezel`). Dane: `skrypty/migracja/osoby_42.py migruj`; katalog: `skrypty/synchronizuj-katalog-pracownikow.mjs` (zastępuje `synchronizuj-katalog-opiekunow.mjs`). Pole „… ze spisu”: `type: reference`, `options: {collection: katalog-pracownikow, value: "{path}", label: "{etykieta}", search: "etykieta,name"}` (+ `multiple: true` przy listach); wartość = `_cms/pracownicy/<id>.yml`, strona bierze z niej id osoby (`optId` / `idList` w `src/content.config.ts`).

| Repozytorium | Formularz | Pole |
|---|---|---|
| Web-Pracownicy | `pracownicy` | **nowe** `pracuje` „Pracuje w Instytucie” (boolean, `default: true`, pod „Grupa”; opis „Po odejściu odznacz. Nie usuwaj osoby — jej nazwisko zostaje przy dawnych grantach i obronach.”), **nowe** `data_odejscia` „Data odejścia (opcjonalnie)” (date, `default: ""`); `operations: {delete: false}`; opis kolekcji z „Usuwanie wyłączone: po odejściu odznacz „Pracuje w Instytucie”.”; kolumna `pracuje` w widoku listy |
| Web-Nauka | `granty` | `kierownik` → **`kierownik_ze_spisu`** „Kierownik ze spisu pracowników” (reference, `multiple`) + **`kierownik_spoza`** „Kierownik spoza spisu” (string, list); widok listy: `kierownik_ze_spisu` |
| Web-Instytut | `zaklady`, grupa `karta` | `kierownik` → **`kierownik_ze_spisu`** „Kierownik” (reference, jedna osoba); widok listy: `karta.kierownik_ze_spisu` |
| Web-Instytut | `wladze`, lista `osoby` (dyrekcja) | `imie_nazwisko` → **`osoba`** „Osoba ze spisu” (reference, `required`); `stopien`, `email`, `pokoj`, `strona` → grupa **`inne`** „Inne dane niż w spisie (zwykle puste)” (nad ukrytym `pozycja`); podsumowanie pozycji `{rola}`; nowy opis formularza |
| Web-Instytut | `wladze`, `wydzial.osoby` | **nowe** `osoba` „Osoba ze spisu” (reference); `imie_nazwisko` → „Osoba spoza spisu (z tytułem)”; `email`, `pokoj` → grupa **`inne`** (opis z „Pokój spisu Wydział nie bierze: wpisz go tutaj.”); podsumowanie `{rola}` |
| Web-Instytut | `wladze`, `sekretariat` | `osoby` (tekst, lista) → **`osoby_ze_spisu`** „Osoby (ze spisu pracowników)” (reference, `multiple`) |
| Web-Sem-* (9) | `seminarium` | `prowadzacy` → **`prowadzacy_ze_spisu`** „Koordynatorzy ze spisu pracowników” (reference, `multiple`) + **`prowadzacy_spoza`** „Koordynatorzy spoza spisu” (string, list) |
| Web-Studia | `specjalnosci`, `opiekunowie` → `osoba` | `search: "etykieta,name"`; nowy opis listy opiekunów |
| Web-Instytut, Web-Nauka, Web-Studia, Web-Sem-* (9) | **nowa kolekcja** `katalog-pracownikow` „Katalog pracowników (tylko odczyt)” (`_cms/pracownicy`, w Web-Studia zastępuje „Katalog opiekunów”) | pola `imie_nazwisko`, `id`, `etykieta`, `pracuje` (wszystkie `readonly`), `operations: {create: false, rename: false, delete: false}`; etykieta z grupą przy duplikatach i z „(były pracownik)” przy `pracuje: false` |

Opisy: „… ze spisu” — „Wybierz z listy (wpisz nazwisko). Tytuł, link i zakład strona weźmie ze spisu pracowników.”; „… spoza spisu” — „Tylko osoby, których nie ma w spisie (np. recenzent z innej uczelni). Wpisz z tytułem: prof. dr hab. Jan Kowalski.”; grupa `inne` — „Wypełnij tylko, jeśli na tej stronie ma być coś innego niż w spisie pracowników (np. e-mail dziekanatu).”. Nagłówek `.pages.yml` dostaje linię „Zlecenie 42: …”. Stare pola (`kierownik`, `prowadzacy`, `imie_nazwisko` dyrekcji, `sekretariat.osoby`) strona czyta dalej, gdy nowych nie ma (zgodność wsteczna na czas pushy).

Automat: `Web-Pracownicy/.github/workflows/katalog-pracownikow.yml` (push na `main` w `src/content/pracownicy/**`, codziennie 03:17 UTC, ręcznie z opcją „na sucho”); działa dopiero po ustawieniu zmiennej `KATALOG_PRACOWNIKOW = wlaczony` i dostępu aplikacji (raport zlecenia 42).

## Zlecenie 59 (22.11.2026): uzupełnienie wersji angielskiej — nowe pola EN

Pola weszły do `.pages.yml` razem z łatkami przeglądu EN (`.przekazanie/zlecenia/59-zalaczniki/`); schemat: `src/content.config.ts` w Web-Core. Puste pole = na stronie angielskiej wersja polska (z `lang="pl"`, gdy wygląda na polską).

| Repozytorium | Formularz | Pole |
|---|---|---|
| Web-Aktualnosci | `aktualnosci`, lista `galeria` | **nowe** `podpis_en` „Podpis EN” (string), zaraz pod „Podpis”; strona: podpis zdjęcia w galerii na `/en` |
| Web-Nauka | `konferencje` | **nowe** `tresc_en` „Opis EN” (code, Markdown), zaraz pod opisem (`body`); opis pola: „Opis po angielsku, w tym samym układzie co opis polski (te same linki i pliki). Puste = na stronie angielskiej pokaże się opis polski.” |
| Web-Instytut | `ww_sylwetki`, grupa `karta` | **nowe** `obraz_zrodlo_en` „Źródło zdjęcia EN” (string, `default: ""`), pod „Źródłem zdjęcia”; opis: „Po angielsku, bez „Photo:” (strona dopisuje je sama), np. „University of Wrocław Archives”. Puste = jak po polsku (nazwiska, licencje i „Wikimedia Commons” nie wymagają tłumaczenia).” |
