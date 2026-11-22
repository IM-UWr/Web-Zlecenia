# Raport: zlecenie 31 — termin wydarzenia „na kliknięcie”, czerwony komunikat przy pozycji bez pliku, strona odporna na puste pozycje, nazwy plików z tytułu (18.11.2026)

## W skrócie

**Wypchnięte 18.11 (etap 5, ok. 01:15–01:23): Web-Core i 16 repozytoriów treści.** Szczegóły: „Etap 5. Push” na końcu. Zostało: test w CMS (właściciel) i przegląd zapisów redaktorów z 24 godzin po pushu.
- **Termin wydarzenia.** „Termin wydarzenia” to grupa dodawana przyciskiem „Add an item”, najwyżej jedna, pod „Rodzaj”, z opisem.
  - Dzień jest wymagany, godziny są sprawdzane wzorcem.
  - CMS nie wpisuje już sam żadnej daty wydarzenia, ani w nowym, ani w starym wpisie.
- **Pozycje list bez pliku.** Pozycja galerii lub załącznika bez pliku dostaje czerwone „This field is required”, a zapis jest zablokowany. Dotyczy to także całkiem pustej pozycji (ukryte pole `pozycja`).
  - Razem `pozycja` jest w 40 listach w 16 repozytoriach (każde Web-Sem-* liczone osobno), a 32 podpola stały się wymagane.
- **Strona.** Pomija puste pozycje list i wypisuje ostrzeżenie w logu budowy (plik, pole, numer pozycji).
  - Czyta stary i nowy zapis terminu, więc Web-Core można wypchnąć przed danymi.
- **Migracja.** 13 wpisów przeszło z `wydarzenie_*` do `termin`. Kalendarz i .ics są bez zmian poza trzema wpisami z 16.11.
- **Daty.** 17 pól dat dostało `default: ""`: 12 opcjonalnych i 5 wymaganych w pozycjach list.
- **Nazwy plików.** Nazwa pliku nowej aktualności i obrony powstaje z tytułu.
- **Kontrole:**
  - `sprawdz_pola_cms.py` 0 problemów;
  - `sprawdz_tresci.py` OK, bez ostrzeżeń (po decyzji o „Medalach”);
  - `astro check` 0 błędów;
  - symulacja formularza, punkty 1–6 i nazwy plików w konferencjach, grantach i referatach (7): OK;
  - zapis bez zmian 724 plików: 0 różnic;
  - kontrola zmian redaktorów: OK.

**Czeka na właściciela.**
1. Wszystkie pytania z raportu mają odpowiedź (16.11: „Akceptuję”; „Medale”: „sukces”; nazwy plików: „Tak, przemianuj”; `field: create`: „Tak, usuń”).
2. Test w CMS, punkty 1–6 z etapu 4 (i nazwa pliku nowego referatu lub konferencji), na wpisie testowym; potem usunięcie wpisu.
3. Poprawka PDF-u `Mapa-CMS-IM-UWr.pdf` w Web-Podglad (sekcja „Dla redaktorów”).

## Commity (wypchnięte na `main` 18.11)

| Repozytorium | Zakres na `main` | Commity |
|---|---|---|
| Web-Core | `6bf211e6..e3625870` | `f339be95` schemat, siatka, termin<br>`d7e2275c` kontrole<br>`2c2caa79` skrypty migracji i kontroli redaktorów<br>`adc16bf4` symulacja formularza, ściągawka<br>`6851dc9b` decyzja o „Medalach” (`termin.py --decyzje`)<br>`b38f511b` przemianowanie (`termin.py --przemianuj`)<br>`e3625870` bez `field: create` w konferencjach, grantach i referatach |
| Web-Aktualnosci | `cc6a7b0..7f0bd01` | `2736871` `.pages.yml`<br>`78ccea4` migracja danych (osobny commit, jak w 2c)<br>`f47aa0a` decyzja właściciela: „Medale” jako sukces<br>`7f0bd01` decyzja właściciela: nowe nazwy trzech plików z 16.11 |
| Web-Nauka, 9 × Web-Sem-* | po 1 commicie | `.pages.yml`: `pozycja`, wymagane pola, bez `field: create` (Nauka `498bc8d`; Sem: `59c6e32`, `a760623`, `b8f2028`, `2fcae0f`, `a9610b1`, `db08446`, `a654c55`, `29148ab`, `f0ff458`) |
| Web-Instytut, Web-Popularyzacja, Web-Pracownicy, Web-Studia, Web-Ustawienia | po 1 commicie | `.pages.yml` (`3f9689a`, `0f76f88`, `5bcaf22`, `b76a2c6`, `3f6bca2`) |

Stan lokalny przed pushem (dla porównania, niewypchnięty): Web-Core `0244f17b` na `222d5e47`, klony robocze z commitami opisanymi niżej.

- Klony treści robocze są w `C:\Users\Szymek\Documents\GitHub\tresci-z31` (git worktree).
- Wspólne klony `tresci` (gałąź `main`) nie są ruszone.
- Przeniesienie na `222d5e47` nastąpiło po pushu drugiej sesji (zlecenie 38, etap 1).
  - Jej zmiany to workflowy, `dok/` i `skrypty/porzadki`; z tym zleceniem nie mają wspólnych plików, rebase przeszedł bez konfliktów.
  - Gałęzie robocze tego zlecenia są lokalne, więc porządki gałęzi na GitHubie ich nie dotyczą. Wszystkie 16 jest na miejscu.

## Etap 0. Stan

**Bazy.** HEAD origin/main przy starcie. Fetch 18.11 o 00:40 nie przyniósł nowych zapisów.

| Repozytorium | Baza | | Repozytorium | Baza |
|---|---|---|---|---|
| Web-Aktualnosci | `f8126af` | | Web-Sem-Geometria | `d23e406` |
| Web-Instytut | `dcdebe8` | | Web-Sem-Prawdopodobienstwo | `8a52232` |
| Web-Nauka | `40ae8a0` | | Web-Sem-Rownania-Rozniczkowe | `d24e794` |
| Web-Popularyzacja | `45045d1` | | Web-Sem-Statystyka | `9b4d7e6` |
| Web-Pracownicy | `d646aa7` | | Web-Sem-Teoria-Modeli | `38755e5` |
| Web-Sem-Analiza-Harmoniczna | `bfa6f70` | | Web-Sem-Topologia | `178a8d3` |
| Web-Sem-Dydaktyka | `deda520` | | Web-Studia | `9a5d3e5` |
| Web-Sem-Dyskretna-Analiza-Harmoniczna | `6009695` | | Web-Ustawienia | `c02dc1c` |

**Zapisy od 16.11** (`git log --since=2026-11-16`):

- **Web-Aktualnosci: 29 zapisów.**
  - Grzegorz Karch (konta grzegorz.karch@…, `grzegorzkarch-blip`, gkarch@…):
    - trzy nowe wpisy `2026-11-16-*.md` i ich edycje;
    - 9 plików w Media;
    - usunięcie `test-2026-11-08-…`;
    - utworzenie i usunięcie `2026-11-17-.md` i `--1.md`.
  - Właściciel: 3 zapisy, 17.11 o 14:50, 20:53 i 20:58.
- **Web-Instytut: 6 zapisów.** Grzegorz Karch, 17.11 22:36–23:03: nowy wpis „Warto wiedzieć” o Medalach ze zdjęciem.
- **Web-Pracownicy: 2 zapisy.** Grzegorz Karch, 16.11: zakłady Hechta i Krawczyka (sprawa z „Do wiadomości” w zleceniu).
- **Pozostałe 13 repozytoriów:** brak zapisów.

**Budowa na `main` nie przechodzi.** To był STOP etapu 0.
- Przebiegi Podglądu 44187719353, 44190972181 i 44195234883 (17.11, 23:12–23:59) kończą się błędem.
- Przyczyna: zapis `78e5044` (17.11 23:12) zostawił pustą pozycję `- {}` w `zalaczniki` wpisu `2026-11-16-.md`. Schemat wymaga pola `plik`, więc budowa się przerywa. To dokładnie błąd z etapu 1 tego zlecenia.
- W klonie `tresci/Web-Aktualnosci` leży lokalny, niewypchnięty commit `b7a307a` (18.11 00:00, „usunięty pusty załącznik”). Nie pochodzi z tej sesji.
- Decyzja właściciela: pracować dalej lokalnie, `b7a307a` i `main` bez zmian.
- Po wypchnięciu Web-Core z tego zlecenia Podgląd zbuduje się także bez `b7a307a`: strona pominie pustą pozycję z ostrzeżeniem.
- Migracja danych też usuwa tę pozycję. Jeśli `b7a307a` zostanie wypchnięty wcześniej, ponowne uruchomienie migracji po prostu jej nie znajdzie.

**Ręczne poprawki właściciela przed zleceniem: nie było ich.**
- Brak `default: ""` przy `wydarzenie_*`. Stara konfiguracja w symulacji wpisuje daty „teraz”.
- Daty w trzech wpisach z 16.11 są nadal wartościami z CMS, więc wyjątki z tabeli 2c zastosowane bez zmian.

**Przegląd zapisów po 17.11, 15:05.**
- Zapisy dotyczyły tylko `2026-11-16-.md`, `2026-11-16--2.md` oraz `2026-11-17-.md` i `--1.md`. Dwa ostatnie zostały utworzone i usunięte tego samego wieczoru.
- **Żaden starszy wpis nie dostał dat wydarzenia.**

**Budowa „przed”.**
- Kod: `24c708ea`.
- Dane: z klonów `tresci`, czyli Web-Aktualnosci z `b7a307a`. Z samym origin/main budowa nie przechodzi, jak w Podglądzie.

## Etap 1. Pozycje list

### 1a. Czerwony komunikat w CMS

Mechanizm ukrytego pola `pozycja` potwierdzają kod Pages CMS i symulacja (scenariusz 4).
- Pole tak/nie ma domyślnie `false`. `isEffectivelyEmpty` traktuje je jako wartość, więc nowa pozycja nie jest „pusta” i jest sprawdzana w całości.
- W pliku pojawia się `pozycja: false`. Strona i skrypty to pole pomijają.

**Widoczność błędu w zwiniętej pozycji.** `collapsed: true` zostaje, bo błąd widać w każdym przypadku:
- nowa pozycja otwiera się sama;
- zwinięta pozycja z błędem ma czerwony nagłówek;
- próba zapisu kończy się komunikatem „Please fix the errors before saving.”.

**Przegląd wszystkich list obiektów.** „Nowe” oznacza, że pole stało się wymagane w tym zleceniu.

| Repozytorium | Lista (wymagane podpola) | Decyzja |
|---|---|---|
| Web-Aktualnosci | `galeria` (`plik`, nowe), `zalaczniki` (`plik`, nowe) | `pozycja` i opis: „Wymagane. Jeśli nie chcesz zdjęcia/załącznika, usuń tę pozycję ikoną kosza.” |
| ″ | `termin` (`dzien`) | `pozycja` |
| ″ | obrony `recenzje` (`recenzent`, `plik`, nowe) | `pozycja` |
| Web-Aktualnosci, Web-Instytut, Web-Nauka, Web-Pracownicy, Web-Studia | „Strony” → `liczby` (`n`, `etykieta`) | `pozycja` |
| Web-Instytut | `o_instytucie_fakty` (`wartosc`, nowe), `wladze/osoby`, `wladze/wydzial/osoby` (`rola`, `imie_nazwisko`), `wladze/linki` (`etykieta`, `adres`) | `pozycja` |
| Web-Nauka | `badania_fakty` (`wartosc`, nowe), `publikacje/lata` (`rok`), `czasopisma` (`nazwa`) | `pozycja` |
| Web-Nauka | `publikacje-wykazy/grupy`, `grupy/prace` | **bez zmian.** Żadne pole nie jest niezbędne: nagłówek jest pusty w 21 z 35 grup, praca ma albo tytuł, albo opis. |
| Web-Popularyzacja | `o_popularyzacji_fakty` (`wartosc`), `tradycja` (`rok`, `nazwa`), `linki` (`nazwa`, `adres`) | `pozycja` |
| Web-Studia | `o_studiach_fakty` (`wartosc`, nowe), kierunki `baner/liczby` (`wartosc`, `etykieta`, nowe), specjalności `opiekunowie` (`osoba`), `baner/liczby` (`n`, `etykieta`) | `pozycja` |
| Web-Studia | „Kolory dni”: `przerwy` (`od`), `wolne` (`od`), `zamiany` (`data`, `jak_dzien`), `wyjatki` (`data`, `kolor`), wszystkie nowe | `pozycja`; daty bez „teraz” (2d) |
| Web-Studia | `przypomnienia` (`sprawa`, `data`), `kolory-dni/semestry` (`nazwa`, `poczatek`, `koniec`) | **bez `pozycja`.** Wymagana data z wartością „teraz” sprawia, że nowa pozycja nigdy nie jest pusta i CMS ją sprawdza. |
| Web-Ustawienia | `przyciski` (`etykieta`, `adres`), `partnerzy` (`nazwa`), `skroty/kafelki` (`etykieta`, `adres`), `nawigacja/menu/grupy/linki` (`etykieta`, `adres`), wszystkie nowe | `pozycja` |
| Web-Ustawienia | `studia/kierunki` (`adres`) | **bez `pozycja`.** Pola tak/nie z `default: true` sprawiają, że pozycja nigdy nie jest pusta. |
| Web-Ustawienia | `nawigacja/menu`, `menu/grupy` | **bez zmian** (brak pól wymaganych) |
| Web-Sem-* (9) | referaty `pliki` (`plik`, nowe) | `pozycja` i opis |
| Web-Spec-* (5) | `specjalnosc-baner/opiekunowie` | **bez zmian.** Tych repozytoriów nie ma w `tresci.json`, strona ich nie czyta. |

Lista zmienionych pól jest też w `.przekazanie/pola-do-cms.md`.

### 1b. Strona pomija puste pozycje

- **`src/content.config.ts`.**
  - Jedna tabela `WYMAGANE_W_LISTACH` i jedna funkcja `bezPustychPozycji` dla wszystkich list z wymaganym podpolem:
    - aktualności: galeria, załączniki, termin;
    - liczby stron;
    - pliki referatów;
    - recenzje obron;
    - liczby banerów kierunków i specjalności.
  - Działa przed walidacją, w opakowaniu loadera `glob` (`zKontrola`).
- **Test budowy:** 5 plików próbnych `zz-test-z31-*`, po teście usunięte. Strony zbudowane, w logu na przykład:
  ```
  [WARN] [glob-loader] src/content/aktualnosci/zz-test-z31-galeria-pusta.md: galeria, pozycja 1 pominięta — brak pola „plik”
  [WARN] [glob-loader] src/content/aktualnosci/zz-test-z31-pusty-termin.md: termin, pozycja 1 pominięta — brak pola „dzien”
  [WARN] [glob-loader] src/content/aktualnosci/zz-test-z31-godziny.md: termin.godzina_konca „25:00” to nie godzina (GG:MM) — pominięta
  ```
- **`sprawdz_tresci.py`.**
  - Te same ostrzeżenia.
  - Dodatkowo przegląd całkiem pustych pozycji we wszystkich plikach `src/data` i banerach.
  - Ostrzeżenia nie zmieniają kodu wyjścia.

## Etap 2. Termin wydarzenia

### 2a. Formularz (Web-Aktualnosci)

- **Miejsce w formularzu.** `termin` stoi pod „Rodzaj”: lista obiektów, `max: 1`.
- **Opis pola:** „Tylko jeśli wpis zapowiada wydarzenie (kliknij „Add an item”). Termin trafia do Kalendarza, do „Nadchodzących wydarzeń” i do Szybkiego dostępu na stronie głównej, a po jego końcu wpis znika z Aktualności na stronie głównej. Dzień, którego dotyczy zwykła informacja (np. dzień wręczenia medalu), wpisz w polu „Data”, nie tutaj.”
- **Pola:**
  - Dzień (wymagany, `default: ""`);
  - Godzina rozpoczęcia (puste = cały dzień);
  - Dzień zakończenia (tylko wydarzenia wielodniowe);
  - Godzina zakończenia (puste = 2 godziny po rozpoczęciu);
  - Miejsce;
  - `pozycja`.
- **Godziny** to pola tekstowe ze wzorcem `^(|([01]?[0-9]|2[0-3])[:.][0-5][0-9])$`. Pages CMS nie ma pola samej godziny. Komunikat błędu: „Wpisz godzinę w formacie 13:00” (przy końcu: „14:30”).
- **Usunięte pola:** `wydarzenie_poczatek`, `wydarzenie_koniec`, `wydarzenie_miejsce`.

### 2b. Kod strony

- **`.transform()` w schemacie aktualności.** Z pierwszej pozycji `termin` wylicza `wydarzenie_poczatek`, `wydarzenie_koniec` i `wydarzenie_miejsce` według reguły ze zlecenia.
  - `src/lib/tresci.ts` i `src/lib/widoki/aktualnosc.ts` są bez zmian.
  - Astro przyjął transformację, `astro check` 0 błędów.
- **Godziny.** Normalizacja do `GG:MM`: „9.30” → „09:30”. Błędna godzina jest pomijana z ostrzeżeniem.
- **Okres przejściowy.** Wpis bez `termin` ze starymi `wydarzenie_*` działa jak dotąd. W logu jest ostrzeżenie: „stary zapis terminu … przenieś do pola „termin””.
- **`formularze.py`.** Kolejność pól aktualności ma `termin` po `rodzaj`.
- **`sprawdz_tresci.py` ostrzega o:**
  - rodzaju „wydarzenie” bez terminu;
  - terminie przy „sukces” i „kariera”;
  - więcej niż jednym terminie;
  - starym zapisie;
  - błędnej godzinie.

### 2c. Migracja

Migrację zrobił `skrypty/migracja/termin.py`.
- Dla każdego wpisu sprawdza, że z nowego zapisu strona wyliczy dokładnie te same daty co ze starego.
- Zmienia tylko linie `wydarzenie_*`; styl wartości zostaje taki, jak w danym pliku.
- Usuwa całkiem puste pozycje list `- {}`.
- Wyjątki z 16.11 stosuje tylko wtedy, gdy wartości są nadal te z etapu 0. Inaczej zatrzymuje się.

| Plik | Przed | `termin` po |
|---|---|---|
| `2026-06-16-seminarium-wydzialowe.md` | 23.06 12:30–14:00, sala 119, Instytut Informatyki UWr | dzień 23.06, 12:30, koniec 14:00, miejsce jw. |
| `2026-06-19-seminarium-ze-statystyki.md` | 22.06 11:00 – 24.06 13:00, sale 602 i 605… | 22.06, 11:00, koniec 24.06 13:00, miejsce jw. |
| `2026-07-14-szkola-baby-steps-beyond-the-horizon.md` | 30.08 – 5.09, Będlewo | 30.08, bez godziny, koniec 5.09, Będlewo |
| `2026-09-10-wyklad-prof-uwe-franza.md` | 15.09 13:00–14:30, sala WS… | 15.09, 13:00, koniec 14:30, miejsce jw. |
| `2026-09-20-kurs-dla-studentow-pierwszego-roku.md` (ogłoszenie) | 25.09, Wydział… | 25.09, bez godziny, miejsce jw. |
| `2026-09-23-2-kongres-mlodych-odkrywcow.md` | 21–22.09, Wydział… | 21.09, koniec 22.09, miejsce jw. |
| 4 × `test-2026-11-0*` | — | 1:1 |
| **`2026-11-16-.md`** „Seminarium wydziałowe” | 10.11 21:28 – 16.11 21:28, Instytut Informatyki sala 119 | **10.11, 13:00, bez końca, Instytut Informatyki sala 119**; usunięta pusta pozycja załącznika |
| **`2026-11-16--1.md`** „Stypendium…” (sukces) | 11.11 21:35 – 16.11 21:35 | **bez terminu** |
| **`2026-11-16--2.md`** „Medale…” | 13.11 22:02–22:02, Aula Leopoldina | **bez terminu**; miejsce „Aula Leopoldina” przepada |

**Zmiany do akceptacji przed pushem:** trzy pogrubione wiersze, według decyzji w zleceniu. **Właściciel zaakceptował je 18.11.**

„Medale” miały rodzaj **„wydarzenie”**, a nie „sukces”, jak zakładało zlecenie: redaktor zmienił rodzaj 17.11 o 22:27. Bez terminu `sprawdz_tresci.py` ostrzegał, a na stronie głównej wpis miał etykietę „wydarzenie”.

**Decyzja właściciela (18.11, pytanie 2): rodzaj „sukces”.**
- Osobny commit `b36d9af`, zrobiony przez `termin.py --decyzje`.
- Zmiana nastąpi tylko wtedy, gdy rodzaj jest nadal „wydarzenie”. Inna wartość zatrzymuje skrypt.
- Na stronie głównej „Medale” mają teraz etykietę „sukces”. Zrzuty i porównanie przed/po zrobiono przed tą decyzją, więc pokazują „wydarzenie”.

### 2d. Pola dat

Przejrzane wszystkie pola `type: date` we wszystkich `.pages.yml`.

**Opcjonalne, teraz z `default: ""` (12):**

| Repozytorium | Pole |
|---|---|
| Web-Aktualnosci | `termin/dzien_konca` (nowe), obrony `data_ogloszenia` |
| Web-Nauka | konferencje `koniec` |
| Web-Studia | „Kolory dni”: `semestr_od`, `semestr_do`, `inauguracja`, `sesja_od`, `sesja_do`, `poprawkowa_od`, `poprawkowa_do`, `przerwy/do`, `wolne/do` |

**Wymagane, zostają z „teraz”:**

| Repozytorium | Pole |
|---|---|
| Web-Aktualnosci | aktualności `data`, obrony `termin` |
| Web-Nauka | konferencje `poczatek` |
| Web-Sem-* (9) | referaty `termin` |
| Web-Studia | przypomnienia `data`, semestry `poczatek` i `koniec` |

**Wymagane w pozycjach list, z `default: ""` (5):** `termin/dzien`, `przerwy/od`, `wolne/od`, `zamiany/data`, `wyjatki/data`.
- To odstępstwo od zasady „wymagane zostają z »teraz«”.
- W nowej pozycji listy data „teraz” zapisałaby się niezauważona. Z pustą datą CMS pokazuje czerwone „Invalid date”.
- Dla `termin/dzien` wynika to wprost ze scenariusza 2.

**Znalezione przy okazji: ukryty błąd w „Kolorach dni” (Web-Studia).**
- Pages CMS przy otwarciu formularza usuwa puste wartości, a potem wstawia domyślne.
- Stara konfiguracja przy pierwszym zapisie formularza zamieniłaby więc puste daty na dzisiejszą datę:
  - `do` czterech dni wolnych (12.11, 13.11, 7.05, 28.05);
  - `inauguracja` semestru letniego.
- Dzień wolny 12.11 stałby się przedziałem 12–18.11.
- Nowa konfiguracja tego nie robi, co potwierdza symulacja: stara konfiguracja daje różnicę w `kolory-dni.json`, nowa nie.

### 2e. Dla redaktorów

**Ściągawka.** `dok/sciagawka-edytora.md` ma nową sekcję „Aktualności: termin wydarzenia, zdjęcia i załączniki”:
- reguła: „Wydarzenie = kliknij »Add an item« pod »Termin wydarzenia«; zwykła informacja = nic nie klikaj, dzień w polu »Data«”;
- godziny, pusta pozycja i ikona kosza;
- nazwa pliku z tytułu;
- wiersz w tabeli „Gdzie co jest”.

**PDF-y w Web-Podglad `dla-redaktorow/`:**

| PDF | Poprawka |
|---|---|
| **`Mapa-CMS-IM-UWr.pdf`** | **Trzeba poprawić.** Na pierwszej stronie jest wiersz „Aktualności: ogłoszenia i wydarzenia (data, miejsce, zdjęcie)”. Proponowany tekst: „Aktualności: ogłoszenia i wydarzenia. Wydarzenie = »Add an item« pod »Termin wydarzenia« (dzień, godzina, miejsce); zwykła informacja = tylko »Data«. Pustą pozycję galerii lub załącznika usuń ikoną kosza.” Przydałaby się też ramka „Jak dodać wydarzenie”, obok ramek „Jak dodać plik” i „Jak dodać nowy kierunek”. Źródła PDF-u nie ma w repozytoriach, więc go nie poprawiałem. |
| `Czat-AI-formatowanie-tresci.pdf` | Bez zmian. „Termin” to tam para w treści, nie pole formularza. |
| `dok/mapa-redakcyjna-IM-UWr.pdf` (Web-Core) | Bez zmian. Opisuje repozytoria, nie pola. |

## Etap 3. Nazwy plików

**Przyczyna potwierdzona.**
- Kod `components/entry/entry.tsx`: przy `field: create` nazwa liczy się przy otwarciu formularza, gdy tytuł jest pusty.
- Symulacja, scenariusz 6:
  - stara konfiguracja daje `2026-11-18-.md`;
  - nowa daje `2026-11-18-medale-uniwersytetu-dla-profesorow-test.md`, z polskimi literami zamienionymi tak jak w Pages CMS.

**Zmiana.** `field: create` usunięte w Web-Aktualnosci, w aktualnościach i obronach.

**Trzy pliki z 16.11 przemianowane** (decyzja właściciela 18.11, pytanie 3).
- Osobny commit `d0e763f`, zrobiony przez `termin.py --przemianuj`. Treść plików jest bez zmian.
- Nazwy jak w reszcie wpisów: data wpisu + opis z tytułu.

| Było | Jest |
|---|---|
| `2026-11-16-.md` | `2026-11-10-seminarium-wydzialowe-problem-milenijny.md` |
| `2026-11-16--1.md` | `2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza.md` |
| `2026-11-16--2.md` | `2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego.md` |

- Nic nie linkuje do starych adresów (sprawdzone w 16 repozytoriach treści i w Web-Core).
- Stare adresy `/aktualnosci/2026-11-16-…/` przestaną działać. Dziś dotyczy to tylko Podglądu.
- Seminarium dostaje w .ics nowy UID i adres, bo oba biorą się z nazwy pliku. Kto już subskrybuje kalendarz, zobaczy to wydarzenie jako nowe.

**Inne kolekcje z `field: create`: usunięte** (decyzja właściciela 18.11, pytanie 4). Dawały ten sam błąd: nazwa przy otwarciu, gdy tytuł jest pusty.

| Repozytorium | Kolekcja | Szablon nazwy |
|---|---|---|
| Web-Nauka | konferencje, granty | `{year}-{primary}.md` |
| Web-Sem-* (9) | referaty | `{year}-{month}-{day}-{primary}.md` |

- Zmiana to jedna linia na kolekcję, w `formularze_31.py` (operacja `bez_field_create`). Lokalnie osobny commit w każdym z 10 repozytoriów.
- Istniejące pliki mają poprawne nazwy (żaden nie ma pustej części z tytułu), więc nic nie przemianowuję.
- Symulacja, scenariusz 7: stara konfiguracja daje `2026-.md` (konferencje, granty) i `2026-11-18-.md` (referaty), nowa daje nazwy z tytułu we wszystkich 11 kolekcjach.
- Kontrola: `formularze_31.py` uruchomiony od zera na bazie każdego z 16 repozytoriów daje dokładnie `.pages.yml` z worktree.
- Ściągawka: zdanie o nazwie pliku dotyczy teraz także obron, konferencji, grantów i referatów.

## Etap 4. Odbiór lokalny

### Porównanie przed/po

**Budowy.** „Po” przechodzi: 757 stron.

**Zakres porównania.** Widoczny tekst 885 plików (HTML PL i EN, .ics, XML, JSON). Różnią się 18 plików, wszystkie w dozwolonym zakresie.

| Plik | Różnica |
|---|---|
| `aktualnosci/2026-11-16--1/`, `--2/` (PL i EN) | „Stypendium” i „Medale” nie mają już bloku „Kiedy / Gdzie / Wydarzenie się odbyło” |
| `aktualnosci/2026-11-16-/` (PL i EN) | „wtorek, 10 listopada 2026, 13:00” zamiast „10–16 listopada 2026” |
| `aktualnosci/` (PL i EN) | wiersze „Kiedy:” znikają przy „Medalach” i „Stypendium”; Seminarium: „10 listopada 2026, 13:00” |
| `kalendarz/` (PL i EN, zakładka Archiwum) | „Medale” i „Stypendium” znikają; Seminarium: „wt. 13:00 · Instytut Informatyki sala 119” |
| `kalendarz/akt-2026-11-16-.ics` | 10.11 13:00–15:00, było 10.11 21:28 – 16.11 21:28 |
| `kalendarz/akt-2026-11-16--1.ics`, `--2.ics` | pliki znikają |
| `wszystko.ics`, `wydarzenia.ics` | te same trzy zmiany |
| strona główna (PL i EN) | „Medale” i „Stypendium” wracają na górę kolumny „Aktualności”; dwie najstarsze pozycje spadają z listy („Ankiety ewaluacyjne”, „Lvzhou Chen…”); wpis TEST nie jest już pierwszy, więc traci zajawkę; w pasku pod okładką pojawia się „1 nowa aktualność” |
| `sitemap.xml` | ta sama lista adresów, inna kolejność |
| `seminaria/powiadomienia.json` | tylko znacznik czasu `wygenerowano` |
| `collections/aktualnosci.schema.json` | schemat Astro z polem `termin` |

Pliki obecne tylko w budowie „przed” to dwa pliki .ics (wyżej) i dwa stare pliki pamięci podręcznej Astro. Nie są stronami.

Tabela pokazuje stan sprzed decyzji właściciela, ze starymi nazwami plików. Zmiany po decyzjach są w części „Po decyzjach właściciela (18.11)”.

**Zrzuty** (`raport-zrzuty/z31-*`, PL, 1440 i 390 px, „przed” z dopiskiem `-przed`):
- `z31-glowna-aktualnosci-*`: kolumna „Aktualności” na stronie głównej;
- `z31-kalendarz-archiwum-*`: Kalendarz → Archiwum, listopad;
- `z31-seminarium-wydzialowe-*`: wpis z 16.11 z terminem 10.11, 13:00;
- `z31-medale-*`: wpis bez bloku terminu.

Zrzuty robione w Edge przez Playwright na statycznych budowach.

### Kontrole

| Kontrola | Wynik |
|---|---|
| `sprawdz_pola_cms.py` na klonach po migracji | 724 pliki w 16 repozytoriach, **0 problemów**. Skrypt zna wzorce pól. „13:00” czyta jako tekst. |
| `sprawdz_tresci.py` | **OK**, 565 plików, **bez ostrzeżeń**. Przed decyzją o „Medalach” było 1 ostrzeżenie: rodzaj „wydarzenie” bez terminu. |
| `astro check` | **0 błędów**, 0 ostrzeżeń, 3 wskazówki (231 plików). |

**Uwaga o YAML.**
- Pages CMS (YAML 1.2) zapisuje `godzina: 13:00` bez cudzysłowu. Astro czyta to jako tekst.
- PyYAML (YAML 1.1) czytał to jako liczbę 780. Oba skrypty Pythona dostały wczytywacz zgodny z YAML 1.2.

### Symulacja zapisu w CMS

**Narzędzie.** `skrypty/test-edytora/formularz.mjs` przenosi logikę formularza Pages CMS (MIT) bez przeglądarki:
- otwarcie (`initializeState` z `sanitizeObject`);
- schemat walidacji (`generateZodSchema`);
- sprawdzenie w przeglądarce i na serwerze;
- zapis YAML i JSON;
- nazwę pliku.

Uruchomienie:
```
node skrypty/test-edytora/formularz.mjs <tresci-z31> <tresci>
```

| Scenariusz | Stara konfiguracja | Nowa konfiguracja |
|---|---|---|
| 1. nowy wpis bez terminu | w pliku `wydarzenie_poczatek` i `wydarzenie_koniec` = chwila otwarcia | **bez terminu i dat wydarzenia** |
| 2. „Add an item” w terminie, bez wypełnienia | — | **zapis zablokowany: `termin.0.dzien: Invalid date`** |
| 3a. sam dzień | — | zapisane `termin: - dzien: 2026-12-02` (całodniowe) |
| 3b. godzina „9.30” | — | **przyjęta** (`godzina: "9.30"`); budowa testowa pokazuje 09:30 |
| 3c. godzina „25:00” | — | **zablokowany: „Wpisz godzinę w formacie 13:00”** |
| 3d. drugi termin (przycisk i tak znika) | — | zablokowany: najwyżej 1 pozycja |
| 4a. galeria: „Add an item” bez zdjęcia | zapisane `galeria: - {}` (to wywraca budowę) | **zablokowany: `galeria.0.plik: This field is required`** |
| 4b. galeria: sam podpis | zapisane `- podpis: Sam podpis` | **zablokowany**, jw. |
| 4c. galeria ze zdjęciem | — | zapisane, w pliku `pozycja: false` |
| 4d. załączniki: „Add an item” bez pliku | zapisane `zalaczniki: - {}` | **zablokowany: `zalaczniki.0.plik: This field is required`** |
| 5. `2026-10-17-rusza-tutornia.md` otwarty i zapisany bez zmian | **dostaje daty wydarzenia = chwila zapisu** | **bez terminu i dat** |
| 6. nazwa pliku nowego wpisu | `2026-11-18-.md` | **`2026-11-18-medale-uniwersytetu-dla-profesorow-test.md`** |
| 7. nazwa pliku w konferencjach, grantach i 9 × referatach | `2026-.md`, `2026-11-18-.md` | **nazwa z tytułu we wszystkich 11** |

**Zapis bez zmian** każdego pliku każdego formularza w 16 repozytoriach (724 pliki):
- **Nowa konfiguracja: 0 różnic w danych.** Za równe uznane są: puste i brak wartości; pole tak/nie i jego wartość domyślna (np. `pozycja: false`); końcowe puste znaki treści.
- **Stara konfiguracja: 161 różnic.** Wszystkie to błędy usuwane tym zleceniem:
  - 156 aktualności dostałoby daty wydarzenia „teraz”;
  - 4 obrony dostałyby `data_ogloszenia` = dziś;
  - „Kolory dni” dostałyby dzisiejsze daty (2d).

### Po decyzjach właściciela (18.11)

Po decyzjach o „Medalach” i nazwach plików zbudowałem stronę jeszcze raz (757 stron) i porównałem z budową „po”. Różnice są w 16 plikach, wszystkie zamierzone:
- **przemianowane strony** (PL i EN) mają ten sam tekst co przed przemianowaniem; „Medale” mają tylko etykietę „Sukces” zamiast „Wydarzenie”;
- **etykieta „Medali”** na stronie głównej, w „Aktualnościach” i na stronie działu Studia: „sukces” zamiast „wydarzenie”;
- **„Sukcesy”** (Nauka, PL i EN): „Medale” dochodzą do listy, licznik 139 → 140;
- **„Ostatnie sukcesy”** na stronie działu Instytut: „Medale” (13.11) zastępują „Nagrodę im. Andrzeja Hulanickiego” (16.06);
- **`wszystko.ics`, `wydarzenia.ics`, `rss.xml`, `sitemap.xml`**: nowe adresy i UID; w `powiadomienia.json` znacznik czasu.

Kontrole po decyzjach:
- `sprawdz_tresci.py`: OK, bez ostrzeżeń;
- `sprawdz_pola_cms.py`: 0 problemów;
- kontrola redaktorów przed pushem i po nim: OK.

Nakładka Web-Core (`src/content`, poza gitem) i manifest `.tresci/nalozone.json` mają nowe nazwy, żeby lokalne budowy zgadzały się z klonami.

## Ochrona zmian redaktorów

**Skrypt:** `skrypty/migracja/kontrola_redaktorow.py`.

```
kontrola_redaktorow.py przed <repo> [--wynik REF] [--baza REF]
```

Tryb `przed`:
- każdy zapis na origin/main od bazy i każdy zmieniony przez niego plik;
- porównanie pole po polu wersji z origin/main z wersją wypychaną;
- dozwolone tylko przeniesienia z migracji:
  - `wydarzenie_*` → `termin`, porównywane przez daty wyliczone dla strony;
  - usunięte `- {}`;
  - dopisane `pozycja: false`;
  - trzy wyjątki z 16.11, decyzja o rodzaju „Medali” i nowe nazwy plików (`termin.py`: `WYJATKI`, `DECYZJE`, `PRZEMIANOWANIA`);
  - zapis redaktora w starym pliku porównywany jest z plikiem pod nową nazwą;
- STOP (kod wyjścia 1), gdy:
  - wynik nie zawiera najświeższego origin/main, czyli migrację trzeba uruchomić jeszcze raz;
  - zginęła lub zmieniła się wartość;
  - redaktor zmienił `.pages.yml`.

```
kontrola_redaktorow.py po <repo> --przed <HEAD sprzed pusha> [--po REF]
```

Tryb `po`:
- całe repozytorium pole po polu;
- lista zmienionych pól z liczbą plików;
- zmiana spoza migracji daje kod wyjścia 1.

**Wynik teraz (próba przed pushem).**
- Od baz nie ma nowych zapisów, wszystkie 16 repozytoriów: **OK**.
- Tryb `po` na Web-Aktualnosci (origin/main → wynik):
  - `.pages.yml`;
  - 13 plików danych: `termin` 11, `wydarzenie_poczatek` 13, `wydarzenie_koniec` 12, `wydarzenie_miejsce` 12, `zalaczniki` 1, `rodzaj` 1 (decyzja o „Medalach”), nazwa pliku 3 (przemianowanie);
  - wynik: „tylko zmiany z migracji”.
- Pozostałe repozytoria: 0 zmian danych.

**Próby negatywne:**
- **Zapisy redaktora z 17.11:** baza cofnięta o trzy zapisy. Wyjątek `2026-11-16-.md` przechodzi, pusty zapis `f8126af` jest rozpoznany.
- **Wynik z utraconym miejscem i zmienioną godziną** (tymczasowy commit bez gałęzi): **STOP** z listą pól.
- **Wynik zbudowany na starszym `main`:** **STOP** „uruchom migrację jeszcze raz”.

## Push — plan etapu 5 (po słowie „push”)

**Okno pusha.** Wieczorem albo po wiadomości do redaktorów: „zapiszcie i zamknijcie CMS na 15 minut, potem odświeżcie stronę”.

1. **Web-Core.**
   - `git fetch`, rebase `praca/31-galeria-daty-nazwy` na origin/main (druga sesja też wypycha).
   - `astro check` i budowa.
   - Push na `main` bez force.
   - Strona czyta stary i nowy zapis, a pusta pozycja nie wywraca budowy.
2. **Zielona budowa Podglądu.**
   - Na starych danych: 13 ostrzeżeń „stary zapis terminu”.
   - Pusty załącznik pominięty z ostrzeżeniem, chyba że `b7a307a` zostanie wypchnięty wcześniej.
3. **Repozytoria treści, każde od świeżego `main`.**
   - Web-Aktualnosci: worktree przełączony na świeży origin/main. Potem jeszcze raz `formularze_31.py`, `termin.py`, `termin.py --decyzje` i `termin.py --przemianuj`, każde w osobnym commicie. Nie doklejam starego wyniku.
   - Pozostałe repozytoria: `formularze_31.py` na świeżym `main` (w Web-Nauka i Web-Sem-* razem z usunięciem `field: create`).
   - `kontrola_redaktorow.py przed`, push, `kontrola_redaktorow.py po`. Wyniki do raportu.
4. **Sprawdzenie po pushu:** zielona budowa, Kalendarz, kolumna „Aktualności” na stronie głównej.
5. **Test w CMS (właściciel).** Punkty 1–6 na wpisie testowym, potem usunięcie wpisu.
6. **Następnego dnia:**
   - przegląd zapisów z 24 godzin po pushu: czy nikt z otwartym starym formularzem nie przywrócił `wydarzenie_*`;
   - poprawki osobnymi commitami.

## Kryteria odbioru

- [x] **Pozycja galerii lub załącznika bez pliku.**
  - W CMS: czerwony komunikat i blokada zapisu, także dla całkiem pustej pozycji (symulacja).
  - Strona pomija puste pozycje z ostrzeżeniem w logu.
- [x] **„Termin wydarzenia”.**
  - Grupa na kliknięcie, najwyżej jedna, pod „Rodzaj”, z opisem.
  - Bez terminu wpis nie jest wydarzeniem.
  - Dzień obowiązkowy, godziny sprawdzane.
- [x] **CMS nie wpisuje sam daty wydarzenia**, ani w nowym, ani w starym wpisie (scenariusze 1 i 5).
- [x] **13 wpisów przeniesionych** — tak, lokalnie (wypchnięcie w etapie 5).
  - Kalendarz i .ics bez zmian poza trzema wpisami z 16.11.
  - Te trzy zaakceptowane przez właściciela 18.11.
- [x] **Opcjonalne pola dat z `default: ""`**, lista w 2d.
- [x] **Nazwa pliku z tytułu.** Trzy pliki z 16.11 przemianowane, ale na polecenie właściciela, po pytaniu w raporcie. Na polecenie właściciela także w konferencjach, grantach i referatach.
- [x] **Ściągawka uaktualniona**, lista PDF-ów do poprawy w 2e.
- [ ] **Kontrole 0 / OK / bez nowych błędów** — tak.
  - Push bez force od świeżego `main`: po słowie „push”.
- [ ] **Kontrola zmian redaktorów przed pushem i po nim** — skrypt gotowy, próba OK.
  - Właściwa kontrola i przegląd następnego dnia: w etapie 5.

## Odstępstwa i uwagi

1. **5 wymaganych dat w pozycjach list ma `default: ""`** zamiast „teraz” (2d). Powód: data „teraz” w nowej pozycji zapisałaby się niezauważona.
2. **Lista przejrzanych list jest szersza niż w zleceniu** (1a): `pozycja` jest w 40 listach (każde Web-Sem-* osobno), a 32 podpola stały się wymagane. Każda decyzja jest w tabeli 1a.
3. **Obrony.** W tym samym repozytorium recenzja wymaga recenzenta i pliku, `data_ogloszenia` nie wpisuje „dziś”, nazwa pliku powstaje z tytułu.
4. **Web-Spec-* pominięte**: nie ma ich w `tresci.json`.
5. **Rekomendacja spoza zakresu.** `src/lib/menu.ts:49` wywołuje `g.linki.filter(...)`. Grupa menu z kierunkami i bez linków (CMS usuwa pustą listę) wywróci budowę. Wystarczy `(g.linki ?? [])`. Nie zmieniałem tego, bo plik nie należy do tego zlecenia.
6. **`.przekazanie/`** jest wspólne z drugą sesją (nieśledzone). W `dziennik.md` i `pola-do-cms.md` tylko dopisałem na końcu.

## Pytania

1. **Trzy wpisy z 16.11** (tabela 2c). Czy akceptujesz zmiany? — **Odpowiedź: „Akceptuję” (18.11).**
   - „Seminarium wydziałowe”: 10.11, 13:00, jednodniowe, termin z treści wpisu.
   - „Stypendium”: bez terminu.
   - „Medale”: bez terminu; miejsce „Aula Leopoldina” przepada.
2. **„Medale”** mają rodzaj „wydarzenie” (redaktor, 17.11 22:27), ale bez terminu nie są wydarzeniem. — **Odpowiedź: „Sukces” (18.11), zrobione w `b36d9af`.** Opcje:
   - (a) zostawić, z ostrzeżeniem w kontroli;
   - (b) rodzaj „sukces”, jak zakładało zlecenie;
   - (c) termin 13.11, cały dzień, Aula Leopoldina; wpis wróci do Kalendarza (Archiwum).

   Proponuję (b).
3. **Przemianować trzy pliki z 16.11** (`2026-11-16-.md`, `--1`, `--2`) na nazwy z tytułu? — **Odpowiedź: „Tak, przemianuj” (18.11), zrobione w `d0e763f` (etap 3).**
   - Adresy `/aktualnosci/2026-11-16--2/` itd. się zmienią, a stare przestaną działać.
   - Strona jeszcze nie wystartowała, więc proponuję tak, w osobnym commicie po migracji.
4. **Usunąć `field: create`** także w Web-Nauka (konferencje, granty) i 9 × Web-Sem-* (referaty)? To po jednej linii w `.pages.yml`. Mogę dołączyć do pusha tego zlecenia. — **Odpowiedź: „Tak, usuń” (18.11), zrobione (etap 3), wejdzie z pushem.**

## Etap 5. Push (18.11, ok. 01:10–01:25)

**Tryb.** Właściciel: „push”, a w trakcie etapu zmiana trybu na samodzielną pracę z pushami według warunków (kontrole, ochrona zmian redaktorów, fetch i rebase tuż przed pushem z ponowną budową).

**Nowa reguła z `zasady.md` (zlecenie 38): raporty i zrzuty tylko lokalnie.**
- Druga sesja wypchnęła `6bf211e6`: z `main` zniknęły `RAPORT-*.md`, `PYTANIA.md` i `raport-zrzuty/`, a `.gitignore` je pomija.
- Moje commity przeniosłem na `6bf211e6` bez raportu i zrzutów. Trzy commity z samym raportem odpadły (`8c103f76`, `1acbc468`, `04016c5c`); z dwóch zniknęło słowo „raport” w opisie.
- Zmiany w kodzie po przeniesieniu są identyczne jak przed (porównanie diffów). Stary HEAD lokalny: `0244f17b`.
- Raport i zrzuty `z31-*` leżą lokalnie w `Web-Core`, nieśledzone. Stare raporty i zrzuty (24 pliki .md, 634 zrzuty) też zostały na dysku, choć przy przeniesieniu git je usunął: przywróciłem je z kopii.

**1. Web-Core** (`6bf211e6..e3625870`, 7 commitów, bez force):
- fetch tuż przed pushem: origin/main `6bf211e6`, gałąź go zawiera;
- `astro check`: 0 błędów, 0 ostrzeżeń;
- budowa po przeniesieniu: 757 stron, wynik identyczny z budową przed przeniesieniem (różni się tylko znacznik czasu w `powiadomienia.json`).

**2. Podgląd po kodzie: zielony.**
- Budowa `44206196180` (uruchomiona ręcznie `gh workflow run podglad.yml` w Web-Podglad, bo push kodu jej nie uruchamia) zbudowała Web-Core `e3625870`: **success**, 13 ostrzeżeń „stary zapis terminu”, jak przewidziano.
- Wcześniej zielona była już budowa `44205492784` po zapisie `cc6a7b0`.

**Nowy zapis na `main` Web-Aktualnosci przed pushem treści:** `cc6a7b0` (Szymon, 18.11 01:09), „usuń pusty załącznik, który przerywał budowę”, czyli usunięta pozycja `- {}` w `2026-11-16-.md`. To ta sama zmiana co w niewypchniętym `b7a307a` z etapu 0.

**3. Repozytoria treści, każde od świeżego `main`.**
- Wszystkie 16 przełączone na świeży origin/main, skrypty uruchomione jeszcze raz (Web-Aktualnosci: `formularze_31.py`, `termin.py`, `--decyzje`, `--przemianuj`, każdy w osobnym commicie; pozostałe: `formularze_31.py`).
- Wynik w każdym repozytorium ma dokładnie te same pliki co stary lokalny wynik (`git diff` stary HEAD → nowy: pusty). W Web-Aktualnosci migracja nie musiała już usuwać `- {}`, bo zrobił to `cc6a7b0`.
- **Kontrola przed pushem:** 16 × OK. W Web-Aktualnosci od bazy z etapu 0 (`f8126af`): zapis `cc6a7b0` sprawdzony, plik w wyniku pod nową nazwą, „wszystkie wartości redaktorów są w wyniku”.
- **Push:** 16 × przyjęty, bez odrzuceń (zakresy w tabeli „Commity”).
- **Kontrola po pushu:** 16 × „OK, tylko zmiany z migracji”.
  - Web-Aktualnosci: `.pages.yml`; 13 plików danych: `termin` 11, `wydarzenie_poczatek` 13, `wydarzenie_koniec` 12, `wydarzenie_miejsce` 12, `rodzaj` 1, nazwa pliku 3.
  - Pozostałe 15: tylko `.pages.yml`, 0 zmian danych.

**4. Podgląd po treściach: zielony.**
- Budowy `44207194283` (po pierwszym pushu treści) i `44207342352` (po ostatnim): **success**, 757 stron, 0 ostrzeżeń „stary zapis terminu”.
- Na stronie (im-uwr.github.io/Web-Podglad):
  - wpis Seminarium pod nowym adresem `/aktualnosci/2026-11-10-seminarium-wydzialowe-problem-milenijny/`, „Kiedy: wtorek, 10 listopada 2026, 13:00”;
  - Kalendarz: Seminarium jest (link pod nowy adres), „Medali” i „Stypendium” nie ma;
  - strona główna, kolumna „Aktualności”: „Medale…” (13.11) i „Stypendium…” (11.11), oba „Nauka · sukces”, wpis TEST niżej.

**Do zrobienia przez właściciela i następnego dnia:**
- **Test w CMS** (Web-Aktualnosci, jedno podejście): punkty 1–6 z etapu 4 na wpisie testowym, potem usunięcie wpisu. Dodatkowo nazwa pliku nowego referatu lub konferencji (punkt 7).
- **Przegląd zapisów redaktorów z 24 godzin po pushu** (do 19.11, ok. 01:25), we wszystkich 16 repozytoriach: czy nikt ze starym formularzem nie przywrócił `wydarzenie_*` ani nie wpisał „teraz” w daty; czy w Web-Aktualnosci nie powstały z powrotem pliki `2026-11-16-*.md`. Narzędzie: `kontrola_redaktorow.py po <repo> --przed <HEAD po pushu>` i `git log`.
- **Wspólne klony `tresci`** (gałąź `main`) są za origin/main i mają w Web-Aktualnosci niewypchnięty `b7a307a` (to samo co `cc6a7b0`). Nie ruszałem ich, zgodnie z decyzją z etapu 0. Przed następnym `git pull` w tym klonie `b7a307a` trzeba porzucić (zmiana jest już na `main`).
- Worktree `GitHub/tresci-z31` i lokalne gałęzie `praca/31-galeria-daty-nazwy` zostają na dysku (nie usuwam folderów).

## Przegląd zapisów redaktorów po pushu (18.11, 11:20, częściowy; okno 24 h kończy się 19.11 ok. 01:25)
- Od pushu (01:23) przybyły zapisy tylko w Web-Aktualnosci, wszystkie od pborod:
  - `9acf852` (08:23): nowa aktualność `2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu.md`;
  - `5035a82` (08:28): zdjęcie do niej;
  - `e4c9c62` (08:28): poprawka tej aktualności.
- Zapisy są zgodne z nowymi formularzami:
  - termin zapisany jako `termin` (dzień 27.11, 12:15, miejsce, `pozycja: false`), bez `wydarzenie_*`;
  - nazwa pliku powstała z tytułu;
  - nikt nie usunął nowych pól ani nie przywrócił starych.
- Podgląd po tych zapisach był zielony (run 44266561212 i 44267389555). Strona wpisu pokazuje „27 listopada 2026, 12:15”.
- Web-Instytut `3f9689a..311faae`: testy zlecenia 41 z drugiego okna, różnica netto zerowa.
- W pozostałych 14 repozytoriach treści nie było zapisów.
- Do powtórzenia po 01:25 19.11: ten sam przegląd za resztę doby.
