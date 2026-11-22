# Raport: zlecenie 49, rodzaj „Seminarium wydziałowe” w Aktualnościach i link do Tutorni we wpisie (18.11.2026)

**Status:** zrobione i sprawdzone lokalnie. Push automatyczny, bez zatrzymania (polecenie właściciela 18.11: „Po zrobieniu 49 zrób pusha automatycznie”), w kolejności Web-Core → Web-Aktualnosci → Web-Ustawienia (menu, niżej). Warunek startu spełniony: 48 i 46 były na `origin/main` (Web-Core `4e1d4c62`, Web-Aktualnosci `73569b8` + 2 zapisy redaktorów).

| Repozytorium | Gałąź lokalna | Commity | Baza (HEAD na starcie) |
|---|---|---|---|
| Web-Core (worktree `Web-Core-B`) | `praca/49-seminarium-wydzialowe` | `a5779a75` (kod), `5dd156f5` (scenariusz 12 symulatora) | `4e1d4c62` |
| Web-Aktualnosci (`tresci-B`) | `praca/49-seminarium-wydzialowe` | `a6892d4` (`.pages.yml` + 3 wpisy, jeden commit) | `945f2de` |
| Web-Ustawienia (`tresci-B`) | `praca/49-menu-warto-wiedziec` | `1fb08e6` (menu „Warto wiedzieć”, decyzja właściciela w trakcie 49) | `50d5cde` |

## Co jest zrobione
1. **Wartość i nazwy:** `seminarium-wydzialowe` w `z.enum` (`src/content.config.ts`, domyślnie dalej `ogloszenie`); `RODZAJE` „Seminarium wydziałowe” / „Faculty seminar”, `RODZAJE_FILTRY` „Seminaria wydziałowe” / „Faculty seminars” (`src/lib/i18n.ts`).
2. **Formularz** (Web-Aktualnosci `.pages.yml`): opcja „Seminarium wydziałowe” zaraz pod „Wydarzenie” (Ogłoszenie, Wydarzenie, Seminarium wydziałowe, Sukces, Kariera); opis pola „Rodzaj” zaczyna się zdaniami ze zlecenia (cudzysłowy „…” jak w reszcie formularza; cały opis w cudzysłowie YAML, bo ma „: ”); opis kolekcji jak w zleceniu; ten sam opis kolekcji w `skrypty/migracja/formularze_40.mjs`. Żadnych nowych pól. Plik się parsuje, `sprawdz_pola_cms.py`: 757 plików, 0 problemów.
3. **Jak „Wydarzenie”:** `jakWydarzenie(rodzaj)` w `src/lib/tresci.ts`, użyta w `Aktualnosc.astro` (`oWydarzeniu`: `.akt-wydarzenie`, kolory działu) i w `aktualnosc.ts` (kolory wierszy „Najbliższych wydarzeń”). Pozycja Kalendarza zostaje rodzajem `wydarzenie`; nowe pole `rodzajWpisu` w `Wydarzenie` ustawiane w `wszystkieWydarzenia()` (i w bloku wydarzenia na stronie wpisu). `dzialWpisu()`: seminarium wydziałowe zawsze Nauka; komentarz poprawiony.
4. **Podpisy:** `WierszWydarzenia.astro` — etykieta „Seminarium wydziałowe · …” / „Faculty seminar · …” i pod prelegentem zajawka (tytuł wykładu) w `.ww-opis`, jak przy referacie; `DrugiEkran.astro` — podpis „seminarium wydziałowe · 13:00 · s. 119” / „faculty seminar · …”, zwykłe wydarzenia dalej bez podpisu rodzaju. Wspólna funkcja `rodzajWiersza()` w `tresci.ts`. Lista Aktualności, kolumna Aktualności na stronie głównej, metryczka wpisu i strona Studiów biorą nazwę z `RODZAJE` — sprawdzone w HTML.
5. **Filtr:** `listaAktualnosci.ts` — `seminarium-wydzialowe` zaraz po `wydarzenie`; `?rodzaj=seminarium-wydzialowe` wybiera filtr (PL i EN).
6. **Bez zmian:** kolumna „Seminaria”, lista i strony seminariów, filtr „Seminaria” w Kalendarzu, wygląd strony wpisu poza plakietką; RSS, mapa strony i wyszukiwarka działają jak dotąd.
7. **Kontrole i ściągawka:** `sprawdz_tresci.py` — „rodzaj „Seminarium wydziałowe” bez terminu — wpis nie trafi do Kalendarza (dodaj „Termin wydarzenia”)”. Symulator formularza i `sprawdz_pola_cms.py` nie mają własnej listy wartości (czytają `.pages.yml`); do symulatora dopisałem scenariusz 12. Ściągawka (`dok/sciagawka-edytora.md`, przy „Termin wydarzenia”): zdanie ze zlecenia + jedno zdanie, gdzie wpis się pokazuje.
8. **Dwa wpisy** (Web-Aktualnosci): Karch — `rodzaj: seminarium-wydzialowe`, tytuł i tytuł EN „Prof. Grzegorz Karch”, nowe `zajawka` / `zajawka_en` po `tresc_en`, przed `dla` (kolejność pól formularza), styl bez cudzysłowów; Vitek — rodzaj, „Prof. Olga Vitek”, zajawki PL i EN = tytuł wykładu, styl w cudzysłowach. Reszta plików bajt w bajt (diff: tylko te linie). `2026-06-19-seminarium-ze-statystyki.md` nietknięty.
9. **„Rusza tutornia”:** bez pola `zalaczniki`; PL „Aktualny plan dyżurów tutorów jest na stronie [Tutornia](/studia/tutornia).”, EN „The current tutors' schedule is on the [Tutoring room](/en/studia/tutornia) page.”; plik `public/pliki/aktualnosci/plan_tutorni_2026_z.png` zostaje.

**Menu „Warto wiedzieć” (polecenie właściciela w trakcie zlecenia, 18.11 ok. 22:55):** Web-Ustawienia `src/data/nawigacja.json` — „Warto wiedzieć” przeniesione z grupy „Więcej” do grupy „Ludzie”, obok „Władz” i „Pracowników”, z opisem „profesorowie, odkrycia, nagrody” / „professors, discoveries, awards”. Opis grupy „Ludzie”: „władze, pracownicy, historia” / „management, staff, history”; „Więcej” wróciło do stanu sprzed 47: „informatyka i biblioteka” / „IT and library” (zgodnie z wiadomością właściciela). Działa w pasku działu Instytutu i w panelu menu (hamburger) na komputerze i telefonie.

## Odstępstwa od zlecenia i powody
1. Oprócz `rodzajWpisu` pozycja Kalendarza z aktualności ma `opisLang` (język zajawki): na `/en` bez „Zajawki EN” tytuł wykładu jest po polsku i dostaje `lang="pl"`. Przy referatach bez zmian.
2. Podpis rodzaju na stronie głównej i etykieta wiersza korzystają z jednej funkcji `rodzajWiersza()` (zamiast dwóch porównań).
3. Komunikat `sprawdz_tresci.py` w cudzysłowach „…” jak pozostałe komunikaty skryptu (zlecenie pisze »…«, bo cytuje w cytacie).
4. Miejsce w podpisie na stronie głównej skraca się tylko dla „sala X, Instytut Matematyczny UWr” (jak dotąd), więc wpis prof. Karcha ma „seminarium wydziałowe · 13:00 · Instytut Informatyki sala 119”, a wpis testowy „… · s. 119”.
5. Poza zakresem 49: zmiana menu „Warto wiedzieć” (wyżej) — osobny commit w Web-Ustawienia.

## Pytanie do właściciela (nie blokuje)
Zlecenie 46 ukrywa zajawkę na stronie wpisu, a w seminarium wydziałowym zajawka to tytuł wykładu. Oba dzisiejsze wpisy mają tytuł wykładu także w treści, więc ich strony go pokazują. Wpis, w którym redaktor wpisze tytuł wykładu tylko w zajawkę, będzie miał na swojej stronie samego prelegenta. Czy (a) zostawić tak i dopisać w ściągawce „tytuł wykładu także w treści”, czy (b) przy seminarium wydziałowym pokazywać zajawkę na stronie wpisu pod plakietką (wyjątek od 46)?

## Odbiór lokalny
Budowy (`tresci-B/z49-budowy.sh`, `z49-menu.sh`): „przed” = Web-Core `4e1d4c62` + Web-Aktualnosci `945f2de` (22:49), „po” = gałęzie 49 (22:50, zaraz potem), te same klony pozostałych repozytoriów; „test” = „po” + 2 wpisy testowe; „menu” = „po” + Web-Ustawienia z nowym menu; „podgląd” = „menu” z `BASE_PATH=/Web-Podglad`.

**Porównanie HTML przed i po** (`raport-zrzuty/z49-skrypt/porownaj49.py`, log `tresci-B/z49-porownaj.log`, pełna lista różnic `tresci-B/z49-roznice.txt`): **0 problemów**.
- Te same pliki w obu budowach (5079 bez Pagefind). 108 plików różni się tylko znacznikiem czasu (`DTSTAMP`, `wygenerowano`). `sitemap.xml`: te same 840 adresów, inna kolejność (kolejność wczytania stron po synchronizacji nakładki; treść identyczna).
- Zmienione 30 plików, każdy blok zmian przy tytule, zajawce albo rodzaju dwóch wpisów, przy Tutorni albo przy filtrze:
  - strony wpisów Karcha i Vitek (PL, EN): tytuł, `<title>`, og:title, plakietka, u Karcha nowe meta description i og:description (wcześniej ogólny opis serwisu, bo nie było zajawki), bez klasy `ph-dlugi` (krótszy tytuł w banerze);
  - „Rusza tutornia” (PL, EN): bez sekcji „Załączniki”, link `/Web-Core/studia/tutornia` i `/Web-Core/en/studia/tutornia` w treści;
  - lista Aktualności (PL, EN): przycisk i opcja „Seminaria wydziałowe”, `data-rodzaj`, plakietki, tytuły i zajawki dwóch wpisów;
  - Kalendarz (PL, EN): „Seminarium wydziałowe · …”, prelegent w tytule, tytuł wykładu w `.ww-opis`;
  - strona główna (PL, EN): „Ostatnio w kalendarzu” — wiersz prof. Karcha z podpisem „seminarium wydziałowe · 13:00 · …”;
  - strona Studiów (PL, EN), zakład Równań Różniczkowych (PL, EN), „Nowszy / Starszy wpis” u sąsiadów (Gdesz, Hulanicki, oferta Jaskółka, test dnia otwartego; PL, EN): tytuły i rodzaj;
  - `rss.xml` (PL, EN), `wydarzenia.ics`, `wszystko.ics`, `.ics` dwóch wpisów: tytuły i zajawki.
- **Liczby w banerach i na okładce bez zmian** (134 strony z liczbami). Pagefind: inny indeks (nowe tytuły i zajawki), dozwolone.

**Wpis testowy** (kopia lokalna; `raport-zrzuty/z49-skrypt/sprawdz49.py`, log `tresci-B/z49-sprawdz.log`): **0 problemów**. Seminarium wydziałowe „Prof. Jan Testowy”, 21.11.2026 13:00, „sala 119”:
- Kalendarz PL i EN: `data-rodzaj="wydarzenie"` (filtr „Wydarzenia”), „Seminarium wydziałowe · sob. 13:00 · sala 119” / „Faculty seminar · Sat 13:00 · room 119”, pod prelegentem tytuł wykładu;
- „Nadchodzące wydarzenia”: „Nauka · seminarium wydziałowe · 13:00 · s. 119” (EN „Research · faculty seminar · 13:00 · room 119”), kolor Nauki; kolumna „Seminaria” bez niego;
- okładka: „1 wydarzenie” → „2 wydarzenia” (EN 1 → 2 events). Liczba „nadchodzące wydarzenia” w banerach: dziś żaden baner jej nie pokazuje (na żadnej stronie nie ma tej etykiety); liczy ją `liczbyTerminow()` z rodzaju `wydarzenie`, więc wpis wliczy się sam;
- `wydarzenia.ics`: jest; `referaty.ics`: nie ma;
- strona wpisu: karta „Kiedy / Gdzie”, `.akt-wydarzenie`, plakietka „Seminarium wydziałowe” / „Faculty seminar”.
- Ten sam wpis bez terminu: ostrzeżenie `sprawdz_tresci.py` (wyżej), w Kalendarzu i w `.ics` go nie ma.

**Podgląd:** w budowie z `BASE_PATH=/Web-Podglad` link we wpisie o Tutorni prowadzi do `/Web-Podglad/studia/tutornia` i `/Web-Podglad/en/studia/tutornia` (strony istnieją), sekcji „Załączniki” nie ma.

**Formularz** (`skrypty/test-edytora/formularz.mjs ../tresci-B`, log `tresci-B/z49-formularz.log`): scenariusz 12 — opcje w kolejności ze zlecenia, domyślnie „Ogłoszenie”, opisy pola i kolekcji, nowy wpis z nową opcją zapisuje `rodzaj: seminarium-wydzialowe`, oba poprawione wpisy otwarte i zapisane bez zmian. „Zapis bez zmian” 757 plików: ten sam wynik co w 48 (6 znanych różnic: 5 obron i 1 grant z pustą treścią dostają komentarz-szablon), w Aktualnościach 0 różnic.

**Zrzuty** (`raport-zrzuty/z49-zrzuty/`, 31 + 4 poprawione kolumny, skrypty `zrzuty49.mjs`, `zrzuty49-nadchodzace.mjs`): wpis prof. Karcha 1536×864, 1920×1080, 390, ciemny 1920, EN 1920; „Rusza tutornia” PL i EN, 1920 i 390; lista z filtrem „Seminaria wydziałowe” PL i EN 1536, 1920, 390, ciemny 1920; wiersz Kalendarza jasny, ciemny, 390, EN; „Nadchodzące wydarzenia” z wpisem testowym jasny, ciemny, 390, EN; strona wpisu testowego; menu: pas działu Instytutu PL i EN, panel 1536 jasny i ciemny, 390, EN.
- Filtr mieści się: 1536 i 1920 px — „Seminaria wydziałowe” / „Faculty seminars” w jednej linii, nic nie wystaje; 390 px — lista wyboru 356 px, tekst się mieści, bez poziomego paska. Po `?rodzaj=seminarium-wydzialowe` widać tylko wpisy tego rodzaju (4 w budowie testowej).
- Konsola czysta (pierwszy przebieg miał przejściowe „connection refused” lokalnego serwera testowego; powtórzony na serwerze z dłuższą kolejką połączeń — bez błędów).

**Kontrole:** `astro check` 0 błędów, 0 ostrzeżeń (4 podpowiedzi jak przed); `npm run test:jawne` 76/76; `sprawdz_tresci.py` OK, 598 plików, 1 ostrzeżenie (Rolski „xxxx”, ze zlecenia 47); `sprawdz_pola_cms.py` 0 problemów.

**PDF-y dla redaktorów** (Web-Podglad `dla-redaktorow/`, `pdftotext`): `Mapa-CMS-IM-UWr.pdf` ma linię „Aktualności: ogłoszenia, wydarzenia (data, miejsce, zdjęcie) i oferty pracy (rodzaj „Kariera”)” — przy następnym generowaniu warto dopisać „seminaria wydziałowe”. Listy opcji „Rodzaju” PDF-y nie mają. `Czat-AI-formatowanie-tresci.pdf`: bez zmian. Nie generowałem.

## Kryteria odbioru
- Formularz: opcja pod „Wydarzenie”, opisy pola i kolekcji, „prelegent w tytule, tytuł wykładu w zajawce”, bez nowych pól, plik się parsuje — spełnione (otwarcie w Pages CMS: krok dla właściciela po pushu).
- Plakietka na liście, stronie głównej, stronie wpisu i stronie Studiów; filtr i `?rodzaj=` — spełnione.
- Wpis z terminem jak „Wydarzenie” (Kalendarz, „Nadchodzące wydarzenia”, `.ics`, liczby, Nauka, kolory) — spełnione.
- „Seminaria” bez zmian — spełnione.
- Dwa wpisy: rodzaj, prelegent w tytule, tytuł wykładu w zajawce, reszta i adresy bez zmian — spełnione.
- Tytuł wykładu pod prelegentem w Kalendarzu i „Najbliższych wydarzeniach” — spełnione.
- „Rusza tutornia”: bez załącznika, link PL i EN, działa z przedrostkiem Podglądu, PNG zostaje — spełnione.
- Ostrzeżenie `sprawdz_tresci.py`, ściągawka — spełnione.
- Push Web-Core → Web-Aktualnosci z kontrolą zapisów redaktorów — sekcja „Push” niżej; przegląd zapisów z 24 h — jutro.

## Test w Pages CMS (po pushu, z właścicielem)
1. Web-Aktualnosci → Aktualności → dowolny wpis: pole „Rodzaj” ma 5 opcji, „Seminarium wydziałowe” trzecia; opis pola zaczyna się od „„Seminarium wydziałowe” działa jak „Wydarzenie”…”.
2. Otworzyć wpis prof. Karcha i zapisać bez zmian: brak commita albo commit bez zmian w pliku.
3. Nowy wpis testowy z „Seminarium wydziałowe” i terminem → po budowie Podglądu: Kalendarz, „Nadchodzące wydarzenia”; potem usunąć.
4. Web-Ustawienia → Nawigacja: Instytut → „Ludzie” ma trzy linki, „Warto wiedzieć” z opisem „profesorowie, odkrycia, nagrody”.

## Push (18.11.2026, automatycznie po odbiorze — polecenie właściciela)
- **Web-Core** `4e1d4c62..5dd156f5` (przewinięcie; `origin/main` bez zmian od bazy).
- **Web-Aktualnosci** `945f2de..a6892d4`, 23:02. Tuż przed pushem `git log 945f2de..origin/main`: 0 nowych zapisów redaktorów. Kontrola pole po polu po pushu (`945f2de` → `origin/main`): Karch i Vitek — zmienione tylko `rodzaj`, `tytul`, `tytul_en`, `zajawka`, `zajawka_en`, treść PL bez zmian; „Rusza tutornia” — `tresc_en`, `zalaczniki` (usunięte) i ostatnie zdanie treści PL.
- **Web-Ustawienia** `50d5cde..1fb08e6`, 23:02 (menu „Warto wiedzieć”); 0 nowych zapisów od bazy.
- Jutro: przegląd zapisów redaktorów z 24 h (Web-Aktualnosci, Web-Ustawienia) i test w Pages CMS z właścicielem (kroki wyżej).
