# Zlecenie 52: sylwetki „Warto wiedzieć”: liczby w banerze, figurka bez opisu, portret opływany tekstem; porządek w sylwetce Tabisza (18.11.2026)

**Decyzje właściciela (18.11):**
- **23:02 i 23:06 (nowy układ sylwetek):**
  - liczby „W skrócie” przechodzą do banera, ze skróconymi podpisami, tak żeby się mieściły;
  - baner ma styl zwykłych podstron, ale **bez ciekawostek o Marczewskim**: losuje się sama figurka z puli Instytutu, bez tytułu i opisu;
  - tekst zaczyna się **na równi z portretem** i opływa go z prawej strony.
- **23:26 (tytuł w jednej linii):** na komputerze imię i nazwisko zawsze mieści się w jednej linii. Jeśli nie mieści się razem z figurką, **figurka znika**. Nie łamiemy tytułu, żeby ją utrzymać.
- **23:51:** zlecenie ma wdrożyć nowy styl i uporządkować tekst sylwetki Tabisza.
- **23:55:** filtr na portretach listy (znika po najechaniu) zostaje, ale na stronie sylwetki zdjęcie jest od razu bez filtra (punkt 4a).
- **23:58:** zlecenie 51 (automatyczna poprawka nagłówków) można pominąć. Tego zlecenia nie trzeba robić po 51.
- **Prototyp:**
  - https://claude.ai/artifact/21WhYPy23xSc8wznNUdFxF (18 sylwetek na Podglądzie z 18.11, 22:42);
  - źródła i opis zmian w `.przekazanie\prototypy\52-sylwetki-baner\` (opis plików na końcu);
  - **`B-prototyp\zmiany.md` to szczegółowa specyfikacja tego zlecenia:** DOM, CSS, wstawka do `DOPASUJ`, losowanie i pomiary.

**Decyzje domyślne** (pytania bez odpowiedzi; zmiana na prośbę właściciela):
- **Źródło liczb:** pole **„Liczby”**, takie samo jak na innych stronach (`liczby: [{n, n_en, etykieta, etykieta_en, pozycja}]`), a nie blok w Treści. Bloki `:::w-skrocie` znikają z plików sylwetek po przeniesieniu liczb (punkt 1).
- **Obok portretu płynie tylko wstęp** (albo ramka TBA). Sekcje z nagłówkiem `##` zaczynają się pod portretem, na pełnej szerokości. Przy krótkim wstępie nagłówek obok dolnej części portretu wyglądał źle: `B-prototyp\zrzuty\wariant-odrzucony-h2-obok-portretu-bozejko-1366.png`.
- **Telefon:**
  - portret 110 px, opływany;
  - figurka w tle za tytułem i hasłem, jak na innych podstronach (np. Struktura i zakłady).
- **Losowanie figurki:**
  - przy każdym wejściu, z wagą „ulubiona” ×3;
  - bez figurki z poprzedniej sylwetki i bez ciekawostki pokazanej w tej wizycie na liście „Warto wiedzieć”;
  - bez JS figurka stała, z FNV-1a od nazwy pliku osoby;
  - dane puli wpisane w stronę, jak na Pracownikach.
- **Figurka znika dopiero wtedy, gdy tytuł nie mieści się w pełnym stopniu.** Tytułu nie zmniejszamy, żeby ją zatrzymać.
- **Krzywicki: „1962 twierdzenie AKS”** zostaje roboczo. Skrótu AKS nie ma w tekście; do decyzji właściciela przy odbiorze.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela. Raport `RAPORT-ZLECENIE-52.md`, zrzuty `raport-zrzuty/z52-*`. Bez subagentów.
- **Niezależne od zlecenia 51** (decyzja 23:58: 51 można pominąć). Jeśli 51 jest już na `main`, pracuj na nim, bo oba zmieniają `src/lib/wartoWiedziec.ts` (`trescWW`) i `SylwetkaWW.astro`. Jeśli go nie ma, nie czekaj na nie.
- **Repozytoria:** Web-Core i **Web-Instytut** (pliki 18 sylwetek i `.pages.yml`).
- **Ochrona zmian redaktorów (jak w zleceniach 31, 40 i 47).** Redaktorzy właśnie edytują sylwetki: Grzegorz Karch i właściciel zmieniali Tabisza 18.11, 23:19–23:41.
  - Zawsze od świeżego `main`, zwykły commit, bez force-push. Baza = HEAD zanotowany na początku pracy.
  - **Migracja skryptem**, nie kopiowaniem plików:
    - dopisanie pola `liczby`;
    - usunięcie bloku `:::w-skrocie` z komentarzem;
    - poprawki Tabisza (punkt 6).

    Tuż przed pushem `git fetch` i `git log <baza>..origin/main`. Jeśli redaktor zmienił któryś plik, uruchom skrypt jeszcze raz na świeżym `main`.
  - Kontrola pole po polu przed pushem i po nim, wynik w raporcie.
  - Push wieczorem albo po wiadomości właściciela do redaktorów („zapiszcie i zamknijcie CMS na 15 minut”).
  - Następnego dnia przegląd zapisów redaktorów z 24 godzin.
- **Kolejność pushy:**
  1. **Web-Core.** Czyta `liczby`, a gdy pole jest puste, pierwsze 3 punkty `:::w-skrocie`, więc nie psuje się bez zmian w treści.
  2. **Web-Instytut.**

## Stan dziś (18.11, ok. 23:55)
- **Web-Core:** zlecenie 47 jest wdrożone. Pliki:
  - `src/views/SylwetkaWW.astro`;
  - `src/lib/wartoWiedziec.ts` (`trescWW`, `portretHtml`, `parsujLata`);
  - `src/lib/markdown.ts` (tryb `ww`, bloki `:::w-skrocie` i `:::laureaci`);
  - `src/styles/warto-wiedziec.css` (`.ww2-prof`, `.ww2-skrot`);
  - baner: `src/components/zal/NaglowekZ.astro` (ciekawostka, `DOPASUJ`), `LiczbyBanera`;
  - ciekawostki: `src/lib/ciekawostki.ts`, `src/data/ciekawostki/instytut.json` (25 kart).

  Zlecenia 51 (automatyczna poprawka nagłówków) nie robimy, decyzja 23:58.
- **Web-Instytut** `2328a0d`: 18 sylwetek w `src/content/warto_wiedziec/sylwetki/`.
  - 17 ma blok `:::w-skrocie` (3–5 punktów, długie podpisy, linki do MGP) z komentarzem `<!-- W SKRÓCIE: … -->`.
  - Tabisz bloku nie ma. Jego Treść wpisał redaktor: `# Dr Krzysztof Tabisz`, trzy `###`, `{#id}` bez spacji i komentarze szablonu TBA na końcu pliku.
- **Strona sylwetki dziś:**
  - baner bez liczb i bez figurki (`z-nagl z-nagl-pod`);
  - w treści siatka: portret 200 px | „W skrócie”;
  - wstęp zaczyna się pod portretem.
- **Pole `liczby` na innych stronach** (wzór): `.pages.yml` Web-Instytut, ok. linii 249: `n`, `n_en`, `etykieta`, `etykieta_en` i ukryte `pozycja`. Pracownicy pokazują liczby przez `LiczbyBanera` (`Napis {n, pl, en}`).

## Docelowo

### 1. Liczby w polu „Liczby” (Web-Instytut, migracja skryptem)
- **Wartości:** dla każdej z 18 sylwetek 3 pozycje z `A-liczby\<plik>.json` (`liczby[].n`, `podpis` → `etykieta`, `podpis_en` → `etykieta_en`, `n_en` puste). Tabela: `A-liczby\liczby-sylwetek.md`.
- **Kolejność pozycji jak w JSON.** Pole `z` w JSON mówi, skąd wzięto pozycję; nie trafia do pliku.
- **Usunięcie bloku:** z Treści PL usuń blok `:::w-skrocie … :::` razem z komentarzem `<!-- W SKRÓCIE: … -->` przed nim. Komentarz `<!-- TEKST: … -->` i reszta Treści zostają bez zmian. Treść EN nie ma bloków (sprawdź).
- **Kontrola:** porównanie tekstu Treści przed i po. Różnica tylko w usuniętym bloku z komentarzem; prozy nie ruszamy.

### 2. Formularz „Sylwetki” (Web-Instytut `.pages.yml`, wzór zleceń 40 i 31)
- **Nowe pole `liczby`**, tuż pod „Podpis EN”, w formacie jak na innych stronach (lista obiektów, zwinięta, `summary: "{n} {etykieta}"`, ukryte `pozycja`). Etykieta i opis:
  - **etykieta:** „Liczby w banerze (3 pozycje)”;
  - **opis:** „Trzy krótkie pozycje pod podpisem na banerze, np. »1945 · pierwszy dziekan«, »20 · doktorów«. Liczba: same cyfry (rok, liczba, 1800+). Podpis: najwyżej ok. 20 znaków, małą literą, bez linków. Pokazują się pierwsze trzy. Puste = baner bez liczb.”
- **Opis pola „Treść”** i **szablon nowej sylwetki:** usuń `:::w-skrocie` (z komentarza W SKRÓCIE i ze szkieletu). Dopisz zdanie: „Liczby do banera wpisuje się w polu »Liczby«”.
- **`sprawdz_pola_cms.py`** i `formularze_40.mjs` bez problemów. Nowe pole dopisz do `.przekazanie\pola-do-cms.md`.

### 3. Baner sylwetki (Web-Core)
Szczegóły: `B-prototyp\zmiany.md`, punkty 1, 2 i 5.

- **Liczby:**
  - `SylwetkaWW.astro` podaje `liczby` do `LiczbyBanera` jak Pracownicy (pierwsze 3 niepuste pozycje);
  - na stronie EN `etykieta_en`, a gdy jest pusta, polski podpis;
  - **zapas:** pole puste, a w Treści jest blok `:::w-skrocie`, to pierwsze 3 punkty bloku (bez linków) idą do banera, a w logu jest ostrzeżenie „przenieś do pola Liczby”;
  - więcej niż 3 pozycje: pokazują się pierwsze 3, w logu ostrzeżenie;
  - blok `:::w-skrocie` **nigdy nie pokazuje się w treści sylwetki**.
- **Figurka bez opisu:** nowy prop w `NaglowekZ` (np. `znakSam`), przekazywany z `SylwetkaWW` (sylwetka nie jest w menu działu, więc nie idzie przez `zMenuDzialuZ`). Działa tak:
  - pula Instytutu, czyli `pulaDzialu('instytut')`: bez `ukryta` i bez `odpada`, waga „ulubiona” ×3;
  - svg `.z-znak` bez `p.z-znak-opis`, klasa `z-znak-sam`, wygląd jak na Pracownikach;
  - losowanie w skrypcie w linii przed narysowaniem strony. Klasa `z-ck-losuje` chowa figurkę do końca losowania, więc nic nie miga;
  - wykluczenia: figurka z poprzedniej sylwetki (`sessionStorage["im-ww-znak"]`) i ciekawostka z zestawu listy „Warto wiedzieć” w tej wizycie. Bez `sessionStorage` losowanie bez wykluczeń;
  - bez JS stała figurka po `fnv1a(nazwa pliku) % długość puli`.
- **Tytuł w jednej linii (komputer, media query komputera):**
  - `h1` z `white-space: nowrap`;
  - wstawka do `DOPASUJ` (`zmiany.md`, pkt 5) mierzy szerokość tytułu przy wczytaniu, przy zmianie rozmiaru okna i po wczytaniu krojów. Gdy tytuł + 40 px wchodzi na figurkę, dodaje `z-znak-brak` i figurka znika, w tym samym przebiegu, bez skakania;
  - bez JS: tytuł dłuższy niż 28 znaków dostaje przy budowie klasę `z-tyt-dlugi-bez-js` i figurka znika na komputerze;
  - na telefonie bez zmian.
- **Lista „Warto wiedzieć”** bez zmian (jej baner ma zwykłą ciekawostkę).

### 4. Treść sylwetki: portret opływany tekstem (Web-Core)
Szczegóły: `zmiany.md`, punkty 3 i 4.

- **DOM:** w `SylwetkaWW.astro` `div.ww2-prof` obejmuje portret (`.ww2-prof-l`: portret, lata, źródło zdjęcia), ramki (`RamkiWW`: błędy, TBA, „Translation in preparation”) i wstęp. `div.ww2-prof-tr` z `dl.ww2-skrot` znika.
- **CSS** (`warto-wiedziec.css`, w miejsce siatki):
  - `.ww2-prof { display: flow-root; margin: 0 0 40px }`;
  - `.ww2-prof-l`:
    - `float: left`, bez sticky;
    - **szerokość portretu i marginesy:**

      | Szerokość okna | Portret | Margines (góra, prawy, dół) |
      |---|---|---|
      | ≥ 1024 px | 200 px | `7px 28px 16px 0` |
      | 561–1023 px | 160 px | `7px 24px 14px 0` |
      | ≤ 560 px | 110 px | `7px 14px 12px 0` |

    - 7 px u góry wyrównuje górę portretu z górą liter pierwszej linii;
  - wstęp `margin: 0`, akapity `text-wrap: pretty`;
  - listy, cytaty i rysunki we wstępie `display: flow-root`;
  - `.ww2-tba` w `.ww2-prof` z `flow-root` i `margin-top: 7px`.

  Usuń reguły siatki `.ww2-prof` z media queries i style `dl.ww2-skrot`, jeśli nic ich już nie używa.
- Sekcje `##` zaczynają się pod `.ww2-prof`, na pełnej szerokości.
- Lata (złote, pod portretem) i placeholder („Zdjęcie” tylko na Podglądzie) bez zmian.

### 4a. Zdjęcie na stronie sylwetki bez filtra (decyzja 18.11, 23:55)
- **Na liście** (siatka sylwetek) i wszędzie, gdzie portret jest linkiem (np. „Inne sylwetki”, mini portrety w `:::laureaci`), filtr zostaje: szarość i nakładka w kolorze działu (`warto-wiedziec.css`, linie ok. 8–12), znikają po najechaniu. Bez zmian.
- **Na stronie sylwetki** duży portret (`.ww2-prof .ww2-portret.ww2-foto`, klasa `ww2-duzy`) pokazuje zdjęcie **od razu w kolorze, bez filtra**:
  - `img`: `filter: none; mix-blend-mode: normal`;
  - nakładka `::after`: niewidoczna;
  - bez przejścia (`transition`), żeby po wejściu na stronę nic się nie „wywoływało”.
- Placeholder (bez zdjęcia) bez zmian.
- Sprawdź na Tabiszu (jedyne prawdziwe zdjęcie): siatka listy z filtrem, a po najechaniu bez niego; strona sylwetki bez filtra od razu, w trybie jasnym i ciemnym.

### 5. Strona EN
- Liczby z `etykieta_en` (zapas: PL).
- Układ jak PL. Ramka „Translation in preparation” stoi w `.ww2-prof` obok portretu, jak ramka TBA.

### 6. Sylwetka Tabisza: porządek w pliku (Web-Instytut, skryptem, na świeżym `main`)
Strona nie poprawia sama nagłówków wpisanych inaczej niż `## Tytuł {#id}` (zlecenie 51 pominięte), więc porządkujemy sam plik (prośba właściciela, 23:51). Po zmianie Tabisz ma sekcje z kreskami, czarne nagłówki i spis „Na tej stronie”, jak inne sylwetki.

- **Treść PL:**
  - usuń pierwszą linię `# Dr Krzysztof Tabisz` (pusta linia po niej też znika);
  - trzy śródtytuły zamień na:
    - `## Działalność naukowa i akademicka {#dzialalnosc-naukowa}`;
    - `## Działalność społeczna i opozycyjna {#dzialalnosc-spoleczna}`;
    - `## Odznaczenia i wyróżnienia {#odznaczenia}`;
  - na początek Treści wstaw standardowe komentarze jak w innych sylwetkach: `<!-- UKŁAD JAWNY: … -->` i `<!-- TEKST: … -->` (dosłownie z `hugo-steinhaus.md`);
  - usuń oba komentarze z końca pliku: powtórzony `<!-- UKŁAD JAWNY … -->` i nieaktualny `<!-- TBA: … -->`.
- **Treść EN:**
  - usuń `# Dr Krzysztof Tabisz`;
  - `### Academic and Scientific Career` → `## Academic and Scientific Career {#dzialalnosc-naukowa}`;
  - `### Social Activism and Democratic Opposition` → `## … {#dzialalnosc-spoleczna}`;
  - `### Honours and Distinctions` → `## … {#odznaczenia}`.

  Te same `{#id}` co w PL.
- **Pola:**
  - `podpis_en` bez kropki na końcu: „Mathematician and distinguished democratic opposition activist”;
  - `liczby` z `A-liczby\krzysztof-tabisz.json`: 1973 w Instytucie · 1991 zastępca dyrektora · 2026 Wrocławska Wolność.
- **Bez zmian:** cała proza PL i EN, `lata`, `podpis`, zajawki, zdjęcie, `dodano`, `opublikowany`.
- **Kontrola:** porównanie tekstu przed i po. Proza identyczna, zmiany tylko w opisanych liniach. Wynik w raporcie.
- **Do raportu, bez zmian:**
  - zdjęcie `tabisz-1.jpg` ma 240×240 px (na ekranach o wysokiej rozdzielczości będzie rozmyte);
  - pole „Źródło zdjęcia” jest puste;
  - sylwetka nie ma sekcji „Źródła”.

  Do decyzji właściciela i redaktora.

### 7. Dokumentacja
- `dok/sciagawka-edytora.md` (część „Warto wiedzieć”):
  - liczby do banera w polu „Liczby” (3 pozycje, krótkie podpisy);
  - figurka w banerze losuje się sama;
  - `:::w-skrocie` w sylwetkach już się nie używa.
- `dok/jawny-markdown.md`: przy `:::w-skrocie` dopisz, że w sylwetkach jest tylko zapasem dla starych plików.
- `dok/dla-redaktorow/mapa-cms.html`: nowe pole.

## Odbiór lokalny
- **Porównanie HTML przed i po** (PL i EN, te same klony treści, po migracji z punktów 1 i 6). Dozwolone różnice:
  - 18 stron sylwetek PL i EN: baner (liczby, figurka), głowa strony (portret i wstęp), brak „W skrócie”;
  - u Tabisza sekcje i `id` z punktu 6.

  Pozostałe strony, w tym lista „Warto wiedzieć”, nagrody, historie i strona główna, bez różnic.
- **Zgodność z prototypem:** zrzuty przy 1920, 1366, 1024 i 390 px, porównane z `B-prototyp\zrzuty\po-*.png`:
  - Steinhaus (także tryb ciemny);
  - Bożejko (szkic);
  - Ryll-Nardzewski (najdłuższe nazwisko);
  - Tabisz (PL i EN);
  - Biler przy 1024.

  Różnice opisz.
- **Automatycznie, na 18 stronach przy 14 szerokościach** (wzór: `B-prototyp\narz\sprawdz.py`):
  - trzy liczby w rzędzie od 1024 px, bez nachodzenia na figurkę;
  - tytuł w jednej linii;
  - konsola czysta.
- **Figurka:**
  - 50 wejść na sylwetki w jednej wizycie: figurki się zmieniają i nie powtarza się ta z poprzedniej strony;
  - bez JS figurka stała;
  - test sztucznie długiego tytułu (kopia testowa, np. 48 znaków): figurka znika przy 1024, 1366 i 1920 px.
- **Zapas `:::w-skrocie`:** kopia testowa sylwetki z blokiem i pustym polem „Liczby” daje liczby w banerze i ostrzeżenie w logu. Bloku nie ma w treści.
- **Edytor:** symulacja zapisu jak w zleceniu 28 (etap 6a). Sylwetka z polem `liczby` po wczytaniu i zapisie daje pusty diff albo opisaną kosmetykę.
- **Kontrole:**
  - `astro check` bez nowych błędów;
  - testy wtyczek zielone;
  - `sprawdz_pola_cms.py` 0;
  - `sprawdz_tresci.py` i `sprawdz-jawny-markdown.mjs` bez problemów.
- **Test w CMS z właścicielem** (po pushu): w Sylwetkach widać pole „Liczby”; zmiana jednej liczby i podgląd po przebudowie.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Na 18 sylwetkach (PL i EN) w banerze są trzy liczby z pola „Liczby” w stylu Pracowników, a po prawej figurka z puli Instytutu bez opisu, losowana przy każdym wejściu.
- [ ] Na komputerze tytuł nigdy się nie łamie. Gdy nie mieści się z figurką, figurka znika (sprawdzone na sztucznie długim tytule).
- [ ] Wstęp zaczyna się na wysokości portretu i opływa go z prawej (telefon: portret 110 px). Sekcje zaczynają się pod nim. „W skrócie” w treści nie ma.
- [ ] Zdjęcie na stronie sylwetki bez filtra od razu, a na liście z filtrem znikającym po najechaniu (Tabisz).
- [ ] Pole „Liczby” w formularzu Sylwetek z opisem. `:::w-skrocie` usunięty z 17 plików i z szablonu, a w kodzie zostaje jako zapas z ostrzeżeniem.
- [ ] Tabisz:
  - `##` z `{#id}`, bez `#` i bez komentarzy TBA, PL i EN;
  - `podpis_en` bez kropki;
  - liczby w banerze;
  - proza nietknięta.
- [ ] Lista, nagrody, historie i strona główna bez zmian w HTML.
- [ ] Zapisy redaktorów w Web-Instytut zachowane (kontrola przed pushem i po nim, przegląd następnego dnia).

## Załączniki (`.przekazanie\prototypy\52-sylwetki-baner\`)
- **A. `A-liczby\`:**
  - 18 plików `<plik>.json` (`liczby[]: n, podpis, podpis_en, z`, do tego `pominiete` i `uwagi`);
  - `liczby-sylwetek.md` (tabela PL i EN);
  - pliki przygotowali agenci z obecnych bloków `:::w-skrocie` i z tekstów, a przy scalaniu zostały poprawione: Hartman, Mycielski, Perkal, Duda, Hulanicki, Biler i Tabisz.
- **B. `B-prototyp\`:**
  - `zmiany.md`: **specyfikacja** (DOM, CSS, `DOPASUJ`, losowanie, pomiary, pytania);
  - `ww-baner.css`: style prototypu;
  - `buduj.py`: budowa prototypu z Podglądu;
  - `narz\`: `zrzuty.py`, `sprawdz.py`, `prog.py`;
  - `zrzuty\`: przed i po, warianty odrzucone, bez JS, test długiego nazwiska;
  - `strona\`: zbudowany prototyp, otwierany przez serwer HTTP, np. `python -m http.server`, wejście przez `index.html`.
