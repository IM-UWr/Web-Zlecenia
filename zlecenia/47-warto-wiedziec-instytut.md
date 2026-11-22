# Zlecenie 47: „Warto wiedzieć” pod Instytutem: Sylwetki, Nagrody i wyróżnienia, Historie na osi czasu, edytowalne w CMS (18.11.2026)

**Decyzje właściciela (18.11, 01:57–18:52):**
- **Pomysł:** rozbudować „Warto wiedzieć”, podpiąć pod Instytut i przestawić na **ludzi**. Ważne historie mają być rozdzielone, np. przy medalach osobne sylwetki Bożejki i Rolskiego.
- **Prototyp przyjęty, „daj zlecenie” (18:52).** Prototyp v4.15: https://claude.ai/artifact/6UFLT6a1RyznwApt9H2vuL. Kopia do otwarcia lokalnie i źródła są w załącznikach: `.przekazanie\prototypy\47-warto-wiedziec\` (opis na końcu).
- **Menu (02:21):** „Warto wiedzieć” to pierwsza pozycja grupy „Więcej” w menu Instytutu.
- **Trzy grupy (18:20):** Sylwetki → Nagrody i wyróżnienia → Historie. Historie łączą dawne „Historia” i „Odkrycia i publikacje” i są pokazane jako interaktywna pozioma oś czasu.
- **CMS (14:14, 18:29, 18:45):**
  - edytowalny CMS: w menu Pages CMS jeden folder „Warto wiedzieć” z trzema w środku, a na dysku trzy podkatalogi;
  - **wszystkie dotychczasowe zasady CMS obowiązują** (zlecenia 40 i 31 oraz ochrona zmian redaktorów).
- **Sylwetki:**
  - tekst jest prozą (13:59);
  - **mało informacji = TBA**, czyli pusta Treść (14:22);
  - **zamiast każdego zdjęcia placeholder**, także u patronów (14:56);
  - **bez odręcznych podpisów** (18:27).
- **Strona sylwetki (17:48–18:29):**
  - „Inne sylwetki” to 4 losowe;
  - „W »Warto wiedzieć«” bez innych sylwetek;
  - źródła zwijane;
  - lata raz, pod zdjęciem;
  - pole „Lata”: jedna data = rok urodzenia, dwie = lata życia, inny tekst bez zmian (np. „xxxx” u Rolskiego, 18:38);
  - wzmianki o publikacjach linkują do źródła (17:54), także w „W skrócie” (18:01);
  - redaktor może dodać PDF w „Do pobrania” (18:29).
- **Lista (18:03–18:43):**
  - bez przełącznika „Tematycznie / Oś czasu” i bez wyszukiwarki;
  - baner z hasłem i liczbami: „81 lat od pierwszego wykładu · 17 sylwetek · 4 rektorów UWr”.
- **„Nowe” (18:25–18:26):** pole „Dodano”, znaczek przez 30 dni; na start mają go Bożejko, Rolski i Biler.
- **Laureaci (02:45):** wpisywani ręcznie w bloku, a licznik liczy się sam.
- **Losowanie na stronie głównej (02:24):**
  - bez wpisów z listą laureatów;
  - rocznica ±7 dni;
  - „Nowe” / „Nowa sylwetka” przez 30 dni;
  - ulubione ×3;
  - przy sylwetce mała twarz zamiast roku.
- **EN = pełne tłumaczenie (18:34).** Same tłumaczenia to osobny krok, po weryfikacji tekstów PL (punkt 12).
- **Poprawki (18:40):** czterech rektorów-matematyków (z Łukaszewiczem); rektorat Marczewskiego trwał w latach 1953–1957.

**Decyzje domyślne** (pytania bez odpowiedzi; zmiana na prośbę właściciela):
- **Adres:** `/instytut/warto-wiedziec` i `/instytut/warto-wiedziec/<plik>` (EN z `/en/` z przodu). Stare adresy `/warto-wiedziec/…` przekierowują na nowe.
- **Osoby żyjące jako szkic** (`opublikowany: false`, widać je tylko na Podglądzie) do czasu akceptacji tekstu przez nie. Dotyczy to Bożejki, Rolskiego, Bilera, Dudy, Narkiewicza i Krzywickiego (u dwóch ostatnich do potwierdzenia, czy żyją). Tabisz (TBA) jest opublikowany.
- **„Dodano”** dla Bożejki, Rolskiego i Bilera = dzień pusha Web-Instytut.
- **Powiązania** z ludźmi biorą się z linków w Treści, bez pola „Osoby”.
- **Źródło zdjęcia** to pole sylwetki, a na stronie drobny podpis pod portretem. Bez automatycznej listy w „O stronie”.
- **Hasło** w banerze („Ludzie i historie wrocławskiej matematyki”) i **wstęp** na stronie zostają oba, jak w prototypie.
- **Pole `dzial`** (dziś tylko kolor wiersza na liście) znika: wszystko ma kolor Instytutu. **Rok PKA** znika, bo nagrody są bez lat.
- **Pusta Treść EN:** ramka „Translation in preparation” z linkiem do PL (punkt 12).

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela. Raport `RAPORT-ZLECENIE-47.md`, zrzuty `raport-zrzuty/z47-*`. Bez subagentów.
- **Korzysta z gotowych zleceń:**
  - 33: `widoczny()`, przełącznik „Opublikowane”, plakietka B4;
  - 31: daty `default: ""`, nazwa pliku `{primary}`, „strona bezobsługowa”;
  - 40: jawny Markdown, wzór Studiów;
  - 45, jeśli jest zrobione: blok `:::pary` nie jest tu potrzebny.
- **Repozytoria:** Web-Core, **Web-Instytut** (treści i `.pages.yml`) i **Web-Ustawienia** (`nawigacja.json`).
- **Ochrona zmian redaktorów:** jak w zleceniach 31 i 40, w skrócie:
  - zawsze od świeżego `main`, zwykły commit, bez force-push;
  - baza = HEAD zanotowany na początku pracy;
  - tuż przed pushem `git fetch` i `git log <baza>..origin/main`. Jeśli redaktor zmienił któryś z czterech dzisiejszych wpisów „Warto wiedzieć”, `strony/warto-wiedziec.md` albo `src/data/instytut.md`, **nanieś migrację jeszcze raz na jego wersję**, skryptem albo listą zmian z punktu 1. Nie kopiuj starych plików;
  - kontrola pole po polu przed pushem i po nim, wynik w raporcie;
  - push wieczorem albo po wiadomości właściciela do redaktorów („zapiszcie i zamknijcie CMS na 15 minut”);
  - następnego dnia przegląd zapisów redaktorów z 24 godzin.
- **Kolejność pushy:**
  1. **Web-Core.** Nowe bloki, kolekcje i adresy. Web-Core toleruje też stary układ: plik leżący bezpośrednio w `warto_wiedziec/` traktuje jak historię, z ostrzeżeniem w logu. Dzięki temu Podgląd nie padnie między pushami.
  2. **Web-Instytut.**
  3. **Web-Ustawienia** (menu).

## Stan dziś (sprawdzone 18.11, ok. 19:00, na `main`)
- **Web-Core** `02a2e8aa`, **Web-Instytut** `88d8f50` (po zleceniu 40, etap 1), **Web-Ustawienia** `05080a9`, **Web-Podglad** `5b4e8f2`.
- **Treść (Web-Instytut):**
  - `src/content/warto_wiedziec/`: 4 pliki:
    - `artykul-w-annals-of-mathematics.md`;
    - `wyklad-terencea-tao.md`;
    - `wyrozniajaca-ocena-pka.md`;
    - `medale-uniwersytetu-dla-profesorow-marka-bozejki-i-tomasza-rolskiego.md`.
  - Pola: `tytul`, `tytul_en`, `opublikowany`, `body`, `tresc_en`, `karta{rok, zajawka(+en), obraz, obraz_opis(+en), link, link_etykieta(+en)}`, `dzial`, `na_glownej`, `zawsze`, `kolejnosc`, `zrodla`.
  - Tekst listy: `src/content/strony/warto-wiedziec.md` (tytuł, opis, hasło).
  - `src/data/instytut.md`: w „W skrócie” pozycja „3 rektorów” (Marczewski, Urbanik, Duda).
- **`.pages.yml` Web-Instytut:** kolekcja `warto_wiedziec` (ok. linii 288) z jednym formularzem; zdjęcia w `public/pliki/warto-wiedziec`.
- **Web-Core:**
  - schemat: `src/content.config.ts` (`warto_wiedziec`, `zKarta`, ok. linii 460);
  - lista: `src/pages/warto-wiedziec/index.astro`, `src/views/ListaWartoWiedziec.astro`, `src/lib/widoki/listaWartoWiedziec.ts`;
  - wpis: `[slug].astro`, `src/views/WartoWiedziecWpis.astro`, `src/lib/widoki/wartoWiedziecWpis.ts`;
  - wiersze: `src/components/WartoWiedziec.astro`;
  - strona główna: `src/components/zal/DrugiEkran.astro` (rząd 4 pozycji, `WARTO_ILE`, `zawsze` najpierw, losowanie); na telefonie osobna lista w stronie głównej;
  - wersje EN w `src/pages/en/warto-wiedziec/`;
  - adres `/warto-wiedziec` wpisany też w:
    - `NaglowekStrony.astro` i `patroni.ts` (dział Instytut; `banerAktualnosci`);
    - `motywyBanerow.ts` (`trzy-odleglosci/warto`);
    - `tekstyStron.ts` (`'warto-wiedziec'`);
    - `sitemap.xml.ts`, `szkice.ts`, `podglad.ts` (`KOLEKCJE`);
    - `skrypty/sprawdz_tresci.py`, `skrypty/migracja/formularze_40.mjs`, `dok/dla-redaktorow/mapa-cms.html`, `dok/sciagawka-edytora.md`.
- **Jawne bloki:** `src/plugins/remark-jawne-bloki.mjs` (`BLOKI`: m.in. `pliki`; **nie ma `w-skrocie` ani `laureaci`**) i `rehype-bloki.mjs`.
- **Przekierowania:** wzór w `src/views/Przekierowanie.astro` i `src/lib/widoki/przekierowanie.ts` (np. `/instytut/zaklady`).
- **Menu (Web-Ustawienia `nawigacja.json`):** Instytut → grupa „Więcej” (Infrastruktura informatyczna, Biblioteka; opis „informatyka i biblioteka”). „Warto wiedzieć” nie ma w menu.
- **Błąd:** `src/lib/patroni.ts` (notka Marczewskiego PL i EN) i `dok/en/TLUMACZENIA.md` podają rektorat w latach 1957–1962. Prawidłowo: 1953–1957 (lista rektorów UWr).

## Docelowo

### 1. Treści i katalogi (Web-Instytut)
- **Podkatalogi** `src/content/warto_wiedziec/`:
  - `sylwetki/`: 18 plików;
  - `nagrody/`: 6;
  - `historie/`: 9.

  Wszystkie **dosłownie z załącznika A** (`A-tresci\Web-Instytut\src\content\warto_wiedziec\`). Grupa wpisu wynika z podkatalogu, nie z pola.
- **Cztery dzisiejsze pliki: przenieść (`git mv`) i zmienić w miejscu, nie nadpisywać.** Wynik ma być równy plikom z załącznika A. Jeśli redaktor coś w nich zmienił, jego zmiana zostaje.
  - `artykul-w-annals-of-mathematics.md` i `wyklad-terencea-tao.md` → `historie/`:
    - `karta.rok` zostaje;
    - usunąć `dzial` i `kolejnosc`;
    - dodać `rocznica` (Tao: `09-06`), `ulubione: true`, `dodano: ""`, `format_tresci: jawne`;
    - na początku Treści komentarze UKŁAD JAWNY i TEKST.
  - `wyrozniajaca-ocena-pka.md` → `nagrody/`:
    - usunąć `karta.rok` i `dzial`;
    - `kolejnosc: 20`;
    - nowa zajawka PL i EN z załącznika;
    - dwa linki do dokumentów → sekcja `## Dokumenty {#dokumenty}` z `:::pliki` (PL i EN).
  - `medale-uniwersytetu-…md` **zastępuje** nowy ogólny wpis `nagrody/medal-uniwersytetu.md`:
    - z `:::laureaci` i notami w `:::pliki`;
    - EN z dawnego `tresc_en`, bez zdania o załącznikach.

    Stary plik usunąć (`git rm`), a stary adres przekierować na nowy (punkt 2).
- **Nazwy plików** muszą być unikalne we wszystkich trzech podkatalogach, bo adres jest płaski. Duplikat to ostrzeżenie w `sprawdz_tresci.py`, a budowa bierze pierwszy plik (w kolejności sylwetki, nagrody, historie) i pomija drugi z ostrzeżeniem.
- **Tekst listy:** `src/content/strony/warto-wiedziec.md` → `src/content/strony/instytut/warto-wiedziec.md` (`git mv`):
  - nowe `opis` (wstęp), `haslo` i `haslo_en` z załącznika A;
  - `tytul_en` „Highlights” zostaje;
  - `opis_en` puste do tłumaczenia.

  W opisie kolekcji „Strony” (`.pages.yml`) popraw ścieżkę „warto-wiedziec.md” na „instytut/warto-wiedziec.md”.
- **`src/data/instytut.md`** („W skrócie” strony Instytutu):
  - „3 rektorów” → „4 rektorów”, EN „4 rectors”;
  - opis: „matematycy Marczewski, Urbanik, Łukaszewicz i Duda kierowali Uniwersytetem Wrocławskim jako rektorzy”, EN „the mathematicians Marczewski, Urbanik, Łukaszewicz and Duda led the University of Wrocław”.

  Pozycji „pas startowy” nie ruszaj, bo czeka na decyzję.

### 2. Kolekcje, adresy i przekierowania (Web-Core)
- **Trzy kolekcje Astro** (np. `ww_sylwetki`, `ww_nagrody`, `ww_historie`) z `glob` na podkatalogach. Wspólne pola schematu przez funkcję pomocniczą, jak `zKarta`.
- **Pola:**
  - **wspólne** (wszystkie trzy):
    - `tytul`;
    - `opublikowany` (`published`);
    - `karta.zajawka` i `karta.zajawka_en`;
    - `karta.obraz`;
    - `na_glownej` (domyślnie tak);
    - `ulubione` (domyślnie nie; ×3 w losowaniu);
    - `zawsze` (domyślnie nie);
    - `dodano` (`""` albo data `RRRR-MM-DD`; zła data = ostrzeżenie i pole puste);
    - `format_tresci: jawne`;
    - `tresc_en`.
  - **sylwetka:**
    - `lata` (tekst);
    - `podpis` i `podpis_en`;
    - `rocznica_urodzin` (`MM-DD` albo puste);
    - `karta.obraz_zrodlo`.
  - **nagroda:**
    - `tytul_en`;
    - `kolejnosc` (liczba, domyślnie 100);
    - `karta.obraz_opis` (+ EN), `karta.link`, `karta.link_etykieta` (+ EN);
    - `zrodla`.
  - **historia:**
    - `tytul_en`;
    - **`karta.rok` wymagany** (4 cyfry; brak albo zły rok = wpis pominięty na osi z ostrzeżeniem, nie błąd budowy);
    - `rocznica` (`MM-DD`);
    - pola obrazu i linku jak w nagrodzie;
    - `zrodla`.
- **Adresy:**
  - lista `/instytut/warto-wiedziec` i `/en/instytut/warto-wiedziec`;
  - wpis `/instytut/warto-wiedziec/<plik>` i `/en/instytut/warto-wiedziec/<plik>`.
- **Przekierowania (wzór `Przekierowanie.astro`):**
  - `/warto-wiedziec` → `/instytut/warto-wiedziec` (i EN);
  - `/warto-wiedziec/<plik>` → `/instytut/warto-wiedziec/<plik>` dla każdego dzisiejszego wpisu;
  - `/warto-wiedziec/medale-uniwersytetu-dla-profesorow-marka-bozejki-i-tomasza-rolskiego` → `/instytut/warto-wiedziec/medal-uniwersytetu`.

  Przekierowań nie ma w `sitemap.xml`.
- **Wszystkie miejsca z `/warto-wiedziec` (lista „Stan dziś”)** przechodzą na nowy adres:
  - dział Instytut i baner listy;
  - motyw banera `trzy-odleglosci/warto` dla listy i dla `/instytut/warto-wiedziec/*`;
  - `tekstyStron` (klucz `instytut/warto-wiedziec`, a `[...slug]` nie robi z tego pliku zwykłej strony);
  - mapa strony, szkice, `podglad.ts` (link „Popraw w CMS” do właściwej kolekcji i pliku), link „Wszystkie →” na stronie głównej.

  Ścieżka „← Instytut” nad tytułem listy; nad tytułem wpisu „← Warto wiedzieć”.

### 3. Jawne bloki (Web-Core)
- **`:::w-skrocie`** (sylwetki; ogólny, klasa wspólna):
  - punkt to `- **wartość** — podpis`;
  - podpis jest Markdownem w jednej linii (linki, kursywa);
  - punkt „lata życia” / „rok urodzenia” jest pomijany, bo lata są w polu;
  - wygląd jak `.ww2-skrot` w prototypie: duża liczba Brygadą, pod nią podpis; siatka obok portretu.
- **`:::laureaci`** (nagrody):
  - punkt to `- **rok** kto — [aktualność](/aktualnosci/…)`;
  - „kto” może być linkiem do sylwetki (`/instytut/warto-wiedziec/<plik>`) i wtedy dostaje mini portret;
  - część po ` — ` jest opcjonalna;
  - kolejność taka jak wpisana;
  - nagłówek sekcji to zwykłe `## Laureaci z Instytutu {#laureaci}` nad blokiem;
  - wygląd jak `.ww2-laur` / `.ww2-l` w prototypie: rok, osoba, „aktualność →” z tekstem dla czytnika;
  - **licznik** to liczba punktów, a na liście „N laureatów z Instytutu” (1 laureat);
  - na stronie publicznej link do sylwetki-szkicu zamienia się w zwykły tekst bez portretu (`widoczny()`).
- **`:::pliki`:** bez zmian (jest), działa w każdej sekcji. W `.prose` bez punktorów i podkreśleń, jak w prototypie (`.z-ww2-os .prose ul.pliki`, `ww2-pl-t`).
- **Walidacja:**
  - jak w innych blokach: nieznany blok, niezamknięty blok i powtórzone `{#id}` to błąd budowy;
  - **zła linia `:::laureaci` / `:::w-skrocie` to ostrzeżenie i pominięcie linii**, nie błąd, bo bloki zmieniają redaktorzy („strona bezobsługowa”, zlecenie 31);
  - na Podglądzie czerwona ramka z linią i wzorem, jak w zleceniu 45 (`:::grafik`), jeśli jest już zrobione; w przeciwnym razie tylko ostrzeżenie w logu.
- Dopisz oba bloki do:
  - `BLOKI`;
  - testów (`jawne-bloki.test.mjs`, `rehype-bloki.test.mjs`);
  - `dok/jawny-markdown.md` (z komentarzami wzorcowymi W SKRÓCIE, LAUREACI, PLIKI, ŹRÓDŁA, TBA z załącznika A);
  - `dok/sciagawka-edytora.md`, `dok/zasady-parsera.md`, `sprawdz-jawny-markdown.mjs`.

### 4. Lista `/instytut/warto-wiedziec`
Wygląd jak `C-prototyp\strona\index.html`.

- **Baner** (jak strony działów: `z-haslo` + `pt-liczby`):
  - hasło z pola;
  - trzy liczby:
    - **N lat od pierwszego wykładu:** liczone przy budowie od 15.11.1945 (18.11.2026 → 81); odmiana rok/lata/lat;
    - **N sylwetek:** sylwetki widoczne (`widoczny()`) z niepustą Treścią, bez TBA; odmiana sylwetka/sylwetki/sylwetek; na Podglądzie dziś 17;
    - **„4 rektorów UWr”:** stała w kodzie (EN „University rectors”), bez pola w CMS.
- **Wstęp** z pola `opis` (`p.wst`), z linkiem „Aktualnościach” (`/aktualnosci`).
- **Spis „Na tej stronie”:** Sylwetki, Nagrody i wyróżnienia, Historie.
- **Bez** przełącznika widoków, wyszukiwarki i „Następnej strony w dziale”.
- **Sylwetki:**
  - pod nagłówkiem zdanie „Ludzie, którzy zbudowali Instytut i jego pozycję. Każda sylwetka łączy się z historiami i wyróżnieniami z tej strony.” (EN do `TLUMACZENIA.md`);
  - siatka kart: portret albo placeholder, imię i nazwisko, lata (złoty drobny tekst, punkt 5), podpis;
  - znaczki: „Nowe”, „TBA”, na Podglądzie także „szkic” (zlecenie 33);
  - **kolejność:** rok urodzenia z pola „Lata” (pierwsza liczba 4-cyfrowa). Bez roku: na końcu, alfabetycznie.
- **Nagrody i wyróżnienia:**
  - wiersze jak dziś (`WartoWiedziec.astro`, układ „lista”), **bez roku**;
  - tytuł, zajawka, miniatura i „N laureatów z Instytutu”, gdy jest blok;
  - kolejność z pola `kolejnosc`.
- **Historie: pozioma oś czasu** (prototyp `os_historii`, `OS_JS`, style `.ww2-ol*`):
  - linia z podziałką co 10 lat, punkty w miejscu roku;
  - **punkty, które wypadają za blisko siebie, rozsuwają się symetrycznie** (minimum 30 px, na telefonie 24 px);
  - pod osią panel z jednym wydarzeniem: duży rok, tytuł, zajawka, „Czytaj →” (do wpisu albo do linku, gdy Treść pusta); strzałki ‹ › i licznik „3 / 9”;
  - **stała wysokość panelu** (wszystkie karty w jednej komórce siatki), więc nic nie skacze;
  - **sterowanie:**
    - mysz: najechanie pokazuje, kliknięcie otwiera;
    - dotyk: pierwsze stuknięcie pokazuje, drugie otwiera;
    - klawiatura: Tab po punktach, ← → między nimi;
  - **start:** wydarzenie z rocznicą w ±7 dni od dziś (Europe/Warsaw), a bez takiego najstarsze;
  - **bez JS:** wszystkie wydarzenia jako lista pod osią;
  - `prefers-reduced-motion` bez animacji przejść.

### 5. Strona sylwetki
Wygląd jak `C-prototyp\strona\w-hugo-steinhaus.html`, `w-marek-bozejko.html` (Do pobrania) i `w-krzysztof-tabisz.html` (TBA).

- **Baner:** imię i nazwisko jako tytuł, `podpis` w miejscu hasła, „← Warto wiedzieć”. Bez linii „Sylwetki · lata”.
- **Głowa strony** (`.ww2-prof`):
  - z lewej portret albo placeholder (sylwetka SVG jak w prototypie; drobny napis „Zdjęcie” tylko na Podglądzie), pod nim **lata** złotym drobnym tekstem;
  - z prawej liczby z `:::w-skrocie`, ciaśniej: mniejszy portret i 2–3 kolumny liczb przy 1023, 700 i 560 px (`ww2.css`).
  - Podpis źródła zdjęcia (`karta.obraz_zrodlo`) drobno pod latami, tylko gdy jest zdjęcie.
- **Pole „Lata”:**

  | Wpis | Wynik |
  |---|---|
  | jedna data (`1956`, `ur. 1956`) | „ur. 1956” (EN „b. 1956”) |
  | dwie daty z dowolną kreską i spacjami (`1956-2020`, `1956 - 2020`, `1956–2020`) | „1956–2020” |
  | inny tekst (np. `xxxx`) | tak, jak wpisany, plus ostrzeżenie w logu „Lata: nie data” |
  | pusto | nic |

  Wzór: `parsuj_lata` w `build.py`.
- **Kolejność:**
  1. wstęp;
  2. sekcje z Treści w kolejności wpisania (także „Do pobrania” z `:::pliki`);
  3. **„W »Warto wiedzieć«”**: nagrody i historie, które w Treści linkują do tej osoby, bez innych sylwetek; bez takich wpisów sekcji nie ma;
  4. **„Źródła”**: zawsze na końcu Treści, **zwinięte** (`<details>`); w nagłówku liczba, np. „22 źródła · rozwiń” z odmianą (`zrodla_licz`); link „Źródła” w spisie i adres `#zrodla` je rozwijają;
  5. **„Inne sylwetki”**:
     - 4 losowe sylwetki widoczne, bez TBA i bez bieżącej;
     - bez JS 4 wybrane stałym ziarnem (różne na różnych stronach), a skrypt losuje przy każdym wejściu;
     - link „Wszystkie sylwetki →” do `#sylwetki` na liście.
- **Spis „Na tej stronie”** zawiera wszystkie te sekcje.
- **TBA:**
  - kiedy: Treść pusta albo z samymi komentarzami (`maTresc()`);
  - co widać: imię, lata, placeholder i ramka „TBA: sylwetka w przygotowaniu”;
  - na Podglądzie dodatkowo zdanie dla redaktora „Wpisz tekst w CMS (Warto wiedzieć → Sylwetki) i zapisz”;
  - TBA nie losuje się na stronie głównej ani w „Innych sylwetkach”.

### 6. Strona nagrody i historii
Wygląd jak `w-medal-uniwersytetu.html` i `w-pierwsze-wyklady.html`. Na bazie dzisiejszej `WartoWiedziecWpis.astro`.

- **Linia meta:** historia „1945 · Historie”, nagroda „Nagrody i wyróżnienia” (link do sekcji listy).
- Wstęp (zajawka), zdjęcie z opisem (jak dziś), Treść, przycisk linku (jak dziś).
- **„Ludzie w tej historii”** (przy nagrodzie z laureatami „Sylwetki laureatów”): karty sylwetek, do których Treść linkuje, z portretem i latami. Bez linków sekcji nie ma.
- **„Zobacz też w »Historie«”** (albo „w »Nagrody i wyróżnienia«”): pozostałe wpisy tej grupy, jak dziś.
- **Wpis bez Treści** nie ma własnej strony, a karta prowadzi do `karta.link` (jak dziś).

### 7. Strona główna (rząd „Warto wiedzieć”)
Prototyp: `glowna.html`, funkcja `GLOWNA_JS`.

- **Pula:**
  - wpisy ze wszystkich trzech grup z `na_glownej` i `widoczny()`;
  - **bez wpisów z blokiem `:::laureaci`** i bez TBA;
  - **na stronie EN** bez wpisów z pustą Treścią EN, jeśli mają polską Treść.
- **Wybór** (komputer 4 miejsca, telefon 3; obie wersje z tej samej funkcji, z listą telefonu na stronie głównej), w tej kolejności:
  1. **rocznica w ±7 dni** (`rocznica_urodzin` / `rocznica`, Europe/Warsaw) z podpisem:
     - „140. urodziny · 14 stycznia” (Steinhaus w 2027 r.);
     - „81 lat temu · 15 listopada” (rok z `karta.rok`).
  2. **„Zawsze pokazuj”.**
  3. **Najnowszy wpis z „Dodano” w ostatnich 30 dniach** z napisem „Nowa sylwetka” (sylwetka) albo „Nowe”.
  4. **Reszta:** losowanie z wagami, ulubione ×3, bez powtórzeń.
- **Pozycja:**
  - sylwetka: z lewej mała twarz (portret albo placeholder) zamiast roku;
  - historia: rok;
  - nagroda: bez roku.
- **Bez JS:** pierwsze pozycje według zasad 1–3, potem według kolejności.

### 8. „Nowe”
- Decyduje tylko pole „Dodano”: data `RRRR-MM-DD`, w CMS kalendarz z `default: ""`.
- Znaczek trwa **30 dni** i znika sam. Sprawdza to przeglądarka (`data-dodano` + skrypt, Europe/Warsaw), bez przebudowy.
- **TBA nigdy nie jest „Nowe”.** Poprawki tekstu nie włączają „Nowe”.
- **Gdzie widać:**
  - znaczek na karcie w siatce sylwetek;
  - napis w rzędzie na stronie głównej (punkt 7.3).
- **Na start** „Dodano” = dzień pusha Web-Instytut u Bożejki, Rolskiego i Bilera (w załączniku A puste, uzupełnij tuż przed pushem). Pozostałe puste.
- Ściągawka: „Opublikowanie szkicu po akceptacji: odznacz »szkic« (włącz »Opublikowane«) i ustaw »Dodano« na ten dzień”.

### 9. CMS (Web-Instytut `.pages.yml`), według zleceń 40 i 31
- **Jedna pozycja menu „Warto wiedzieć” jako grupa** (`type: group`, `items`; porządkuje tylko menu, pliki zostają na miejscu). W środku trzy kolekcje, zamiast dzisiejszej `warto_wiedziec`. Kolejność w menu CMS bez zmian: po „Strony Instytutu”, przed „Władze Instytutu”.

  ```yaml
  - name: warto_wiedziec
    label: Warto wiedzieć
    type: group
    items:
      - name: ww_sylwetki
        label: Sylwetki
        type: collection
        path: src/content/warto_wiedziec/sylwetki
        format: yaml-frontmatter
        filename: '{primary}.md'
        description: …
        view: { fields: [tytul, lata, opublikowany, dodano], primary: tytul, sort: tytul }
        fields: [ … ]
      - name: ww_nagrody      # path: …/nagrody, sort: kolejnosc
      - name: ww_historie     # path: …/historie, sort: karta.rok (jeśli Pages CMS nie sortuje po polu zagnieżdżonym: tytul)
  ```

  **Sprawdź na app.pagescms.org**, że nasza wersja obsługuje `type: group`. Jeśli nie: trzy pozycje obok siebie „Warto wiedzieć: Sylwetki”, „Warto wiedzieć: Nagrody i wyróżnienia”, „Warto wiedzieć: Historie”. Opisz to w raporcie.
- **Opisy kolekcji** (co to jest i gdzie widać):
  - **Sylwetki:** „Ludzie Instytutu: siatka portretów na stronie Warto wiedzieć (/instytut/warto-wiedziec) i strona każdej osoby. Pusta Treść = sylwetka »TBA«. Sylwetka osoby żyjącej: odznacz »Opublikowane«, dopóki osoba nie zaakceptuje tekstu. Nazwa pliku (adres) powstaje z imienia i nazwiska.”
  - **Nagrody i wyróżnienia:** „Nagrody i wyróżnienia Instytutu i jego ludzi, w kolejności z pola »Kolejność« (10, 20, 30…). Laureatów dopisuj w Treści w bloku :::laureaci; licznik na liście liczy się sam.”
  - **Historie:** „Wydarzenia i odkrycia na osi czasu na stronie Warto wiedzieć. Rok jest wymagany: stawia punkt na osi. Zajawka pokazuje się w panelu osi, więc najlepiej 1–2 zdania.”
- **Formularze: wzór Studiów:**
  - Tytuł, Opublikowane (zaraz pod tytułem, etykieta ze zlecenia 33), **Treść**, **Treść EN**, potem drobne pola; pola EN pod polskimi z dopiskiem „EN”;
  - `format_tresci` ukryte (`hidden: true`, `default: jawne`);
  - **każde drobne pole ma opis z przykładem i z tym, co się stanie, gdy zostanie puste.** Przykłady:
    - **Lata:** „np. 1887–1972 albo 1956 (= ur. 1956). Inny tekst pokaże się tak, jak wpisany. Puste = bez lat.”
    - **Rocznica urodzin:** „MM-DD, np. 01-14. Przez 7 dni przed i po tej dacie sylwetka ma pierwszeństwo na stronie głównej. Puste = bez rocznicy.”
    - **Dodano:** „Dzień dodania sylwetki: przez 30 dni znaczek »Nowe«. Ustaw tylko przy nowej sylwetce albo przy publikacji szkicu, nie przy poprawkach. Puste = bez »Nowe«.”
    - **Zdjęcie:** „Tylko z prawem do publikacji. Puste = sylwetka zastępcza.”
    - **Źródło zdjęcia:** „Autor, licencja, link, np. »Fot. Jan Kowalski, CC BY-SA 4.0«. Pokazuje się drobno pod portretem.”
    - **Ulubione:** „Na stronie głównej losuje się 3× częściej.”
    - **Zawsze pokazuj:** jak dziś.
    - **Kolejność:** „Mniejsza = wyżej; zostaw odstępy 10, 20, 30, żeby wstawiać pomiędzy.”
    - **Rok (historie):** „Rok wydarzenia, np. 1946. Wymagany.”
- **Pola z zasadami zlecenia 31:**
  - **`dodano` z `default: ""`**, bo bez tego CMS wpisałby dzisiejszą datę przy otwarciu starej sylwetki i dałby jej fałszywe „Nowe”;
  - pozostałe daty i opcjonalne teksty też z `default: ""`;
  - `filename: '{primary}.md'` bez `field: create`. Sprawdź, jak Pages CMS zamienia polskie znaki (np. „Władysław Ślebodziński”); wynik w raporcie.
- **Szablony Treści nowych wpisów** (`default`; sam komentarz = pusta Treść, `maTresc()`):
  - **sylwetka:** UKŁAD JAWNY + komentarz TBA z załącznika A, a w osobnym komentarzu szkielet do skopiowania (`:::w-skrocie` z jednym punktem, wstęp, `## Droga naukowa {#droga}`, `## Źródła {#zrodla}` z jednym punktem);
  - **nagroda:** UKŁAD JAWNY + TEKST + komentarz z szkieletem `## Laureaci z Instytutu {#laureaci}` i `:::laureaci`;
  - **historia:** UKŁAD JAWNY + TEKST.
- **Media:** `public/pliki/warto-wiedziec` bez zmian (portrety też tam).
- **`sprawdz_pola_cms.py`** i **`formularze_40.mjs`**: nowe kolekcje; 0 problemów.

### 10. Menu (Web-Ustawienia `nawigacja.json`)
- **Instytut → grupa „Więcej”, pierwsza pozycja:**

  ```json
  { "etykieta": "Warto wiedzieć", "etykieta_en": "Highlights", "opis": "sylwetki, nagrody, historie", "opis_en": "people, awards, stories", "adres": "/instytut/warto-wiedziec" }
  ```
- **Opis grupy:** „ludzie i historia, informatyka, biblioteka” / EN „people and history, IT, library”. Sprawdź, czy nie łamie się na 2 linie na karcie grupy. Jeśli się łamie, „historia, informatyka, biblioteka”.
- Na stronie Instytutu karta grupy pokazuje „3 strony”. Sprawdź, że liczy się samo.

### 11. Poprawki przy okazji
- `src/lib/patroni.ts` (notka Marczewskiego PL i EN) i `dok/en/TLUMACZENIA.md`: rektorat **1953–1957**.
- Web-Instytut `src/data/instytut.md`: „4 rektorów” (punkt 1).

### 12. Wersja angielska
- **Strony EN** dla listy i wszystkich wpisów; nazwy i lata wspólne.
- **Pusta Treść EN przy wypełnionej PL:**
  - strona EN pokazuje imię i nazwisko (albo tytuł), lata i portret oraz ramkę „Translation in preparation”, z linkiem „Read in Polish →”;
  - karta na liście EN ma znaczek „PL”;
  - wpis nie losuje się na stronie głównej EN.
- **Pusta zajawka EN, podpis EN albo tytuł EN:** pokazuje się polski tekst (jak dziś).
- **Teksty interfejsu** (do `dok/en/TLUMACZENIA.md`):

  | PL | EN |
  |---|---|
  | W skrócie | At a glance |
  | Do pobrania | Downloads |
  | Źródła, „N źródeł · rozwiń” | Sources, „N sources · show” |
  | Inne sylwetki | Other profiles |
  | Wszystkie sylwetki → | All profiles → |
  | W »Warto wiedzieć« | In Highlights (nazwa z `tytul_en` strony listy) |
  | Ludzie w tej historii | People in this story |
  | Sylwetki laureatów | Recipients’ profiles |
  | Nowe | New |
  | Nowa sylwetka | New profile |
  | TBA | TBA |
  | ur. 1956 | b. 1956 |
  | N lat od pierwszego wykładu | N years since the first lecture |
  | N sylwetek | N profiles |
  | 4 rektorów UWr | 4 University rectors |
  | N laureatów z Instytutu | N recipients from the Institute |
  | Czytaj → | Read → |
  | Poprzednie / następne wydarzenie | Previous / next event |
  | „140. urodziny · 14 stycznia” | „140th birthday · 14 January” |
  | „81 lat temu · 15 listopada” | „81 years ago · 15 November” |

- **Tłumaczenia treści:** poza tym zleceniem. Puste pola EN w załączniku A zostają puste. Wyjątek: dzisiejsze tłumaczenia (Annals, Tao, PKA i medal) są przeniesione.

### 13. Dokumentacja
- `dok/sciagawka-edytora.md`:
  - jak dodać sylwetkę, nagrodę i historię;
  - TBA;
  - „Lata”;
  - „Dodano” i „Nowe”;
  - `:::w-skrocie`, `:::laureaci`, „Do pobrania” z `:::pliki`;
  - szkic osoby żyjącej;
  - linki do sylwetek dają powiązania.
- `dok/jawny-markdown.md`: zakres „Warto wiedzieć” i nowe bloki.
- `dok/dla-redaktorow/mapa-cms.html`: nowa grupa w CMS.

## Odbiór lokalny
- **Porównanie HTML przed i po** (PL i EN, te same klony treści). Dozwolone różnice:
  - nowe strony `/instytut/warto-wiedziec…` i przekierowania ze starych adresów;
  - menu: pozycja „Warto wiedzieć” na wszystkich stronach;
  - strona Instytutu: „4 rektorów”, karta grupy „Więcej”, notka Marczewskiego;
  - strona główna: rząd „Warto wiedzieć”;
  - mapa strony.

  Pozostałe strony bez różnic.
- **Testy jednostkowe:**
  - `parsuj_lata`: przykłady z punktu 5, w tym `xxxx` i puste;
  - `:::w-skrocie`: link w podpisie, pominięcie „lata życia”, zła linia;
  - `:::laureaci`: z linkiem do sylwetki, bez, bez części po ` — `, zła linia, licznik, link do szkicu przy `TYLKO_OPUBLIKOWANE=1`;
  - powiązania z linków;
  - duplikat nazwy pliku.
- **Oś czasu** (Playwright): 9 punktów bez nakładania przy 1920, 1366, 1024 i 390 px; mysz, dotyk i klawiatura; start 15.11 (rocznica pierwszych wykładów) i 1.03 (najstarsze, bo bez rocznicy); bez JS lista.
- **Strona główna** (`page.clock.setFixedTime`, Europe/Warsaw):
  - 18.11.2026: „Nowa sylwetka” jako jedna z pozycji; 1945 „81 lat temu · 15 listopada” w ±7 dni;
  - 14.01.2027: Steinhaus „140. urodziny · 14 stycznia”;
  - 20.12.2026: brak „Nowe”, bo minęło 30 dni;
  - 100 losowań: ulubione wypadają ok. 3× częściej; nigdy laureaci ani TBA.
- **Budowa z `TYLKO_OPUBLIKOWANE=1`:**
  - 6 szkiców osób żyjących znika z siatki, liczby („11 sylwetek”), „Innych sylwetek”, strony głównej, mapy strony i wyszukiwarki;
  - linki do nich w laureatach i w tekstach innych sylwetek stają się zwykłym tekstem.
- **Zrzuty** (tryb jasny i ciemny; 1920×1080, 1366×768, 1024×768, 390 px):
  - lista;
  - sylwetka pełna (Steinhaus);
  - sylwetka z „Do pobrania” (Bożejko, z „szkicem” na Podglądzie);
  - Rolski („xxxx” i ostrzeżenie w logu);
  - TBA (Tabisz);
  - nagroda z laureatami (Stypendium im. Steinhausa, Medal UWr);
  - historia (Pierwsze wykłady);
  - strony EN (Annals z tłumaczeniem, Steinhaus z ramką „Translation in preparation”);
  - strona główna i menu Instytutu.
- **Edytor:** symulacja zapisu jak w zleceniu 28 (etap 6a). Każdy plik z załącznika A po wczytaniu i zapisie edytorem daje pusty diff albo opisaną kosmetykę; bloki przeżywają zapis bez zmian.
- **Kontrole:**
  - `astro check` bez nowych błędów;
  - testy wtyczek zielone;
  - `sprawdz_pola_cms.py`, `sprawdz_tresci.py` i `sprawdz-jawny-markdown.mjs` bez problemów (poza ostrzeżeniem „Lata: nie data” u Rolskiego);
  - konsola czysta;
  - `lychee` bez nowych martwych linków (w tym noty PDF `/pliki/aktualnosci/…notabiograficzna.pdf`).
- **Test w CMS z właścicielem** (jak w zleceniu 40, krok 8):
  - grupa „Warto wiedzieć” z trzema kolekcjami;
  - otwarcie i zapis sylwetki bez zmian;
  - nowa sylwetka z szablonu: TBA na Podglądzie, nazwa pliku z imienia i nazwiska, „Dodano” puste;
  - dopisanie laureata.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] `/instytut/warto-wiedziec` (PL i EN) z banerem (hasło + 81 lat · 17 sylwetek · 4 rektorów UWr), wstępem i trzema grupami: siatka sylwetek, lista nagród, oś czasu historii. Bez przełącznika widoków i wyszukiwarki.
- [ ] 18 sylwetek, 6 nagród i 9 historii z załącznika A. Cztery dzisiejsze wpisy przeniesione z zachowaniem zmian redaktorów i tłumaczeń EN. Stare adresy przekierowują.
- [ ] Strona sylwetki:
  - placeholder;
  - lata raz, pod portretem, według reguł pola „Lata”;
  - liczby „W skrócie” z linkami;
  - sekcje z Treści i „Do pobrania”;
  - „W »Warto wiedzieć«” tylko z nagrodami i historiami;
  - zwinięte „Źródła”;
  - 4 losowe „Inne sylwetki”;
  - TBA dla pustej Treści.
- [ ] `:::w-skrocie` i `:::laureaci` działają, z licznikiem laureatów i portretami; błędne linie nie zatrzymują budowy.
- [ ] Oś czasu: rozsuwanie punktów, panel stałej wysokości, mysz, dotyk i klawiatura, start od rocznicy, wersja bez JS.
- [ ] Strona główna: losowanie według punktu 7 (rocznica, zawsze, „Nowa sylwetka”, ulubione ×3); bez laureatów i TBA; twarz przy sylwetce.
- [ ] „Nowe” przez 30 dni z pola „Dodano” (Bożejko, Rolski, Biler), znika samo.
- [ ] Osoby żyjące są szkicami: widać je na Podglądzie, a w budowie publicznej nie ma ich nigdzie.
- [ ] CMS:
  - grupa „Warto wiedzieć” z trzema kolekcjami (albo zapas z przedrostkiem, opisany);
  - formularze według wzoru Studiów, z opisami i przykładami;
  - `dodano` z `default: ""`;
  - nazwa pliku z tytułu;
  - szablony Treści.
- [ ] Menu Instytutu: „Warto wiedzieć” pierwsza w „Więcej”.
- [ ] Poprawki: Marczewski 1953–1957 (`patroni.ts`, `TLUMACZENIA.md`), „4 rektorów” na stronie Instytutu.
- [ ] EN: interfejs przetłumaczony; pusta Treść EN daje ramkę „Translation in preparation”.
- [ ] Dokumentacja (ściągawka, jawny Markdown, mapa CMS) aktualna.
- [ ] Zapisy redaktorów w Web-Instytut i Web-Ustawienia zachowane (kontrola przed pushem i po nim, przegląd następnego dnia).

## Załączniki (`.przekazanie\prototypy\47-warto-wiedziec\`)
- **A. `A-tresci\Web-Instytut\src\content\`**: gotowe pliki treści w docelowym układzie:
  - `warto_wiedziec\{sylwetki,nagrody,historie}\*.md` (33 pliki);
  - `strony\instytut\warto-wiedziec.md`.

  Teksty PL, komentarze dla redaktora według wzoru Studiów, linki między wpisami na nowych adresach. Wygenerowane skryptem `C-prototyp\narzedzia\generuj-tresci.py` z prototypu i z plików Web-Instytut z 18.11 (`88d8f50`).
- **B. `B-weryfikacja\`**: materiał dla redakcji, nie trafia na stronę:
  - pliki `<osoba>-weryfikacja.md` (fakt → źródło, rozbieżności, pytania do Instytutu);
  - `sylwetki-do-sprawdzenia.md` (zbiorcza lista spraw do sprawdzenia);
  - `BRIEF.md` (jak powstały teksty);
  - `krzysztof-tabisz-szkic.md` (szkic, który nie trafił na stronę);
  - noty biograficzne Bożejki i Rolskiego jako tekst.
- **C. `C-prototyp\`**:
  - `strona\`: zbudowany prototyp v4.15, do otwarcia lokalnie (`index.html`, `w-*.html`, `glowna.html`);
  - `zrodla\`:
    - `dane.py` (dane prototypu);
    - `build.py`: wzory logiki: `parsuj_lata`, `inne_sylwetki`, `os_historii` + `OS_JS`, `GLOWNA_JS`, `bloki_pliki`, `zrodla_licz`; to wzór, nie kod do skopiowania;
    - `ww2.css` (wygląd: `.ww2-prof`, `.ww2-skrot`, `.ww2-siatka`, `.ww2-ol*`, `.ww2-laur`, `.ww2-zrodla-d`, placeholder `.ww2-ph`);
    - `ikona_pdf.svg`;
    - `sprawdz.py` (kontrola plików sylwetek);
  - `narzedzia\`:
    - `linkuj2.py` (linkowanie wzmianek o źródłach w tekstach);
    - `generuj-tresci.py`.
