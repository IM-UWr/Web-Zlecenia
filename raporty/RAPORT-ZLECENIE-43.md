# Raport: zlecenie 43, plan zajęć na cały rok akademicki, podtrzymanie harmonogramów, logo UWr

**Status:** wszystkie etapy zrobione.
- Etapy 1 i 3: wypchnięte 18.11.2026 o 14:24 UTC (15:24 czasu lokalnego), w trybie samodzielnym.
- Etap 2: wdrożony po decyzji właściciela, wypchnięty 18.11 o 15:57 UTC (Web-Core `d436ab69`, Web-Podglad `6abb1bb6`).
- **Zostaje jedno kliknięcie właściciela:** uprawnienie Actions: Read and write dla aplikacji „IM-UWr strona powiadomienia” (instrukcja w etapie 2). Do tego czasu przekaźnik przy każdym przebiegu zostawia ostrzeżenie.
- **Web-Core `main`:** `0b239768..057513dc`, dwa commity, zwykły push, bez force:
  - `ee446fee` — etap 1;
  - `057513dc` — etap 3.
- **Przed pushem:**
  - `fetch` pokazał nowy commit drugiej sesji `0b239768` (zlecenie 40, etap 5, tylko skrypt migracji); rebase bez konfliktów;
  - budowa z przebazowanego drzewa;
  - `astro check` 0 błędów, 0 ostrzeżeń, 5 podpowiedzi (jak na `main`); `npm run test:jawne` 47/47.
- **Podgląd:**
  - przebieg [44323847367](https://github.com/IM-UWr/Web-Podglad/actions/runs/44323847367) jest zielony (1 min 30 s);
  - gałąź `zbudowana` ma już nowy znacznik okładki;
  - strona na żywo pokazywała jeszcze starą wersję z pamięci podręcznej GitHub Pages (do 10 minut).
- Zlecenie kończy się słowami „Stop: raport ze wszystkich trzech etapów i czekanie na push”. Etapy 1 i 3 wypchnąłem według zasad trybu samodzielnego, bo kontrole przeszły i etapy są niezależne.

## Etap 1. Plan zajęć: rok akademicki od 1 sierpnia (`ee446fee`)

### Zmiana (`skrypty/plan/pobierz_plan.py`)

- **`ZMIANA_ROKU = (8, 1)  # miesiąc, dzień`** na górze pliku, z komentarzem. To jedyne miejsce, w którym ustawia się dzień zmiany.
- **`rok_akademicki(dzis)` i `para_semestrow(dzis)`:** od 1 sierpnia roku R (data w strefie `STREFA` = Europe/Warsaw) para to `R/RR-Z` i `R/RR-L`, wcześniej `(R−1)/R`.
- **`wybierz_semestry()` bez `--semestr`** bierze tę parę z `terms/terms_index`, z nazwami i datami z USOS jak dotąd.
  - Semestr, którego USOS jeszcze nie zna, dostaje znacznik `brak_w_usos`.
  - Skrypt nie pyta wtedy ani eksportu, ani API o jego plan: dla nieistniejącego semestru tryb awaryjny API robiłby do 2500 zapytań.
  - Do pliku trafia wpis z nazwą z `nazwa_semestru()`, bez dat i bez planu. W logu jest zwykła informacja, nie ostrzeżenie ani błąd.
- **Tryb awaryjny** (`semestry_z_kalendarza()`, gdy API nie odpowiada): ta sama para, najpierw zimowy, potem letni.
- **`--semestr` bez zmian:** ręczne wskazanie wygrywa, także przy awarii API.
- **Opisy:**
  - nagłówek skryptu (para, dzień zmiany, brak semestru w USOS, semestr spoza pary znika z pliku);
  - `--help`;
  - `plan-zajec.yml` nie wspominał o wyborze semestrów, więc go nie ruszałem.
- **Bez zmian:** `wybierzSemestr()` i zachowywanie poprzednich danych przy awarii USOS.

### Test bez sieci (`raport-zrzuty/z43-skrypt/`)

- **Pliki:**
  - `test_wybor.py` wywołuje `wybierz_semestry()` z zablokowaną siecią;
  - `test_aktywna.mjs` liczy aktywną zakładkę prawdziwą funkcją `wybierzSemestr()` (Node 26 czyta plik `.ts` bez kompilacji);
  - odpowiedź `terms/terms_index` zapisana 18.11 w `terms_index-2026-11-18.json`. USOS zna już semestry do 2031/32.
- **Wyniki:** `wynik-tabela.md`, `wynik-wyboru.json`.

**Na zapisanej odpowiedzi `terms_index`** (zgodne z tabelą zlecenia w każdym wierszu):

| Dzień | Zakładki | Daty z USOS | Aktywna |
|---|---|---|---|
| 18.11.2026 | Zimowy 2026/27, Letni 2026/27 | 01.10.2026–05.02.2027; 24.02–17.06.2027 | Zimowy 2026/27 |
| 10.02.2027 (przerwa) | Zimowy 2026/27, Letni 2026/27 | jw. | Letni 2026/27 |
| 24.02.2027 | Zimowy 2026/27, Letni 2026/27 | jw. | Letni 2026/27 |
| 15.07.2027 (po zajęciach) | Zimowy 2026/27, Letni 2026/27 | jw. | Letni 2026/27 |
| 31.07.2027 | Zimowy 2026/27, Letni 2026/27 | jw. | Letni 2026/27 |
| 01.08.2027 | Zimowy 2027/28, Letni 2027/28 | 01.10.2027–26.01.2028; 20.02–16.06.2028 | Zimowy 2027/28 |
| 01.10.2027 | Zimowy 2027/28, Letni 2027/28 | jw. | Zimowy 2027/28 |

**Tryb awaryjny (kalendarz):**
- zakładki takie same jak wyżej w każdym wierszu, w kolejności zimowy, letni;
- dat brak, więc `wybierzSemestr()` daje pierwszą zakładkę (zapas).

**Dodatkowo:**
- **Granica dnia zmiany w dwóch latach:**
  - 31.07.2027 → 2026/27 (aktywny letni), 01.08.2027 → 2027/28 (aktywny zimowy);
  - 31.07.2028 → 2027/28, 01.08.2028 → 2028/29.
- **Brak letniego 2027/28 w USOS (01.08.2027):** zimowy z datami, letni bez dat z dopiskiem „brak w USOS (bez pobierania)”; aktywny zimowy.
- **`--semestr 2025/26-L --semestr 2026/27-Z`:** dokładnie te dwa, z datami z USOS. Przy awarii API: `2025/26-L` z nazwą z identyfikatora.
- **Cały przebieg `main()` bez sieci, 01.08.2027, letniego nie ma w USOS** (`test_brak_w_usos.py`, wynik `wynik-brak-w-usos.txt`):
  - kod 0;
  - w pliku `2027/28-Z` (z danymi z podstawionego eksportu) i `2027/28-L` bez dat, bez przedmiotów, `zrodlo: null`;
  - eksportu dla letniego skrypt nie pytał.

### Pozostałe sprawdzenia

- **Prawdziwe pobranie dziś**, stary skrypt (z `main`) i nowy, każdy na kopii `plan.json`:
  - oba: 8 zapytań do USOS API, 2026/27-Z: 88 przedmiotów, 300 zajęć; 2026/27-L: 100 przedmiotów, 304 zajęcia;
  - oba piszą „Plik bez zmian”; wynik obu identyczny i równy `plan.json` w repozytorium.
- **Strona z pustym semestrem:** budowa z opróżnionym letnim 2026/27 (kopia robocza `plan.json`, potem przywrócona; `tresci-B/z43-brakL`):
  - zakładka letnia pokazuje „Plan na ten semestr nie jest jeszcze dostępny w USOS.”;
  - EN: „The timetable for this semester is not available in USOS yet.”
- **Strona Plan zajęć i kafelek na stronie głównej:** bez zmian. Zmiana dotyczy tylko skryptu, a `plan.json` jest ten sam; porównanie HTML budów przed i po etapie 3 pokazuje różnice tylko na stronie głównej (etap 3).
- **`astro check`:** bez nowych błędów.
- **Nowy skrypt w Actions (kontrola 18.11, 16:13 UTC):**
  - ~~Przebieg z harmonogramu po pushu (14:24 UTC): jeszcze go nie ma.~~ **Kontrola 18.11, 19:03 UTC (20:03 lokalnie): ✓.** Pierwszy przebieg z harmonogramu z nowym skryptem to [44368917211](https://github.com/IM-UWr/Web-Core/actions/runs/44368917211). Ruszył o 18:22 UTC (cron z 15:47 opóźniony przez GitHub) na kodzie `02a2e8aa`, który zawiera `ee446fee`, i jest zielony. Log, ten sam filtr:
    - „2026/27-Z: źródło usosweb-eksport, przedmiotów 88, zajęć 300, bez zmian”;
    - „2026/27-L: źródło usosweb-eksport, przedmiotów 100, zajęć 304, bez zmian”;
    - „Zapytania do USOS API: 8”, „Plik bez zmian”;
    - adnotacja „Bez zmian w USOS — nic do zapisania”, bez commita i bez błędu;
    - trafienia „warning” to tylko podpowiedź gita przy checkout i wypisany tekst skryptu kroku „Zapis zmian” (linia `|| echo "::warning …"`, która się nie wykonała). Adnotacji ostrzeżeń z przebiegu brak.

    Wniosek: nowy skrypt działa w Actions z harmonogramu, nic nie trzeba poprawiać ani cofać.
  - **Ręczny przebieg [44341565229](https://github.com/IM-UWr/Web-Core/actions/runs/44341565229)** (15:57 UTC, z odbiorem etapu 2, kod `d436ab69`, czyli z nowym skryptem): zielony. Log, filtr `2026/27|Plik|Zapytania|UWAGA|warning|Error`:
    - „2026/27-Z: źródło usosweb-eksport, przedmiotów 88, zajęć 300, bez zmian”;
    - „2026/27-L: źródło usosweb-eksport, przedmiotów 100, zajęć 304, bez zmian”;
    - „Zapytania do USOS API: 8”, „Plik bez zmian”;
    - jedyne trafienie „warning” to podpowiedź gita przy checkout („hint: … suppress this warning”), nie błąd skryptu;
    - wiersz w wiersz to samo co przebieg z harmonogramu 09:14 UTC ze starym skryptem (44274032995).

## Etap 2. Harmonogramy GitHub — wdrożony po decyzji właściciela (`d436ab69`, Web-Podglad `6abb1bb6`)

**Decyzja właściciela (18.11, ok. 16:50 czasu lokalnego):** w pełni automatycznie, bez ręcznych kliknięć później, bez osobistych tokenów i bez commitów.
1. Przekaźnik `podglad-przekaznik.yml` (uruchamiany zdarzeniami; takich GitHub nie wyłącza) przy każdym przebiegu sprawdza `plan-zajec.yml` (Web-Core) i `podglad.yml` (Web-Podglad). Nieaktywny włącza (`PUT …/enable`) i zostawia `::warning`.
   - W Web-Core: `GITHUB_TOKEN` z `actions: write`.
   - Do Web-Podglad: token tej samej aplikacji (`POWIADOM_APP_ID` / `POWIADOM_KLUCZ`). Dopóki aplikacja nie ma uprawnienia, krok dla Web-Podglad nie wywraca przekaźnika, tylko ostrzega.
2. Do tego A + B jako ostatni zapas: cotygodniowe `enable` i czerwony przebieg z jasnym komunikatem.

**Wypchnięte 18.11 o 15:57 UTC (16:57 czasu lokalnego), zwykły push, bez force:**
- Web-Podglad `main`: `f2fe4af0..6abb1bb6`. Ten push był pierwszy, bo kontrola z Web-Core sprawdza nowy plik.
- Web-Core `main`: `b43b0aa8..d436ab69`.
- **Przed pushem:**
  - fetch w obu repozytoriach, bez nowych commitów;
  - budowa OK;
  - `astro check` 0 błędów, 0 ostrzeżeń, 5 podpowiedzi;
  - `npm run test:jawne` 47/47.
- **Porównania HTML nie robiłem:** zmiana nie dotyka plików strony (`git diff --stat`: dwa workflowy i README).

### Co działa

| Gdzie | Kiedy | Co robi | Gdy coś nie tak |
|---|---|---|---|
| Web-Core, `podglad-przekaznik.yml`: nowy krok „Harmonogramy”, przed sygnałem | każdy przebieg przekaźnika: zapis w CMS, push na main, ręcznie | sprawdza stan i wywołuje `PUT …/enable` dla `plan-zajec.yml` (`GITHUB_TOKEN`) i dla `podglad.yml` w Web-Podglad (klucz aplikacji) | wyłączony przez GitHub: włącza i zostawia ostrzeżenie „włączony ponownie”. Nie da się włączyć: ostrzeżenie ze skutkiem i linkiem. Nigdy nie zatrzymuje przekaźnika (`continue-on-error`, zawsze kod 0) |
| Web-Core, `plan-zajec.yml`: nowe zadanie „podtrzymanie” | poniedziałek 04:13 UTC i ręczne uruchomienie | `enable` dla `plan-zajec.yml`; kontrola `podglad.yml` i `podtrzymanie.yml` w Web-Podglad | czerwony przebieg, `::error`: stan, przyczyna, skutek, link „Enable workflow” |
| Web-Podglad, `podtrzymanie.yml` (nowy) | poniedziałek 04:43 UTC i ręczne uruchomienie | `enable` dla `podglad.yml` i dla siebie; kontrola `plan-zajec.yml` w Web-Core | jak wyżej |

- **Zadanie „plan”** nie rusza przy cotygodniowym cronie. Ręczne uruchomienie `plan-zajec.yml` robi oba zadania.
- **Krok w przekaźniku stoi przed sygnałem.** Jeśli GitHub wyłączył `podglad.yml`, zapis w CMS najpierw go włącza, a potem uruchamia budowę.
- **`deploy.yml` nietknięty**, dalej `disabled_manually`.
- **Opisy:**
  - na górze każdego zmienionego workflowu;
  - w README Web-Core nowa sekcja „Harmonogramy GitHub (podtrzymanie)” z instrukcją dla właściciela;
  - w `podglad.yml` tylko dwa wiersze komentarza.

### Jednorazowe ustawienie dla właściciela: Actions: Read and write dla aplikacji

Aplikacja to **„IM-UWr strona powiadomienia”** (`im-uwr-strona-powiadomienia`, należy do organizacji IM-UWr, instalacja 176681935).
- Dziś ma tylko Contents: read & write i Metadata: read.
- Dlatego przekaźnik przy każdym przebiegu zostawia ostrzeżenie „Harmonogram IM-UWr/Web-Podglad/podglad.yml — nie można włączać … (HTTP 403)”.
- Uprawnienie ustawia się dla całej aplikacji, nie dla jednego repozytorium.

1. Otwórz https://github.com/organizations/IM-UWr/settings/apps/im-uwr-strona-powiadomienia/permissions
   - inaczej: IM-UWr → **Settings** → na dole lewego menu **Developer settings** → **GitHub Apps** → „IM-UWr strona powiadomienia” → **Edit** → zakładka **Permissions & events**.
2. **Repository permissions** → **Actions** → z listy **Read and write** → na dole strony **Save changes**.
3. Otwórz https://github.com/organizations/IM-UWr/settings/installations/176681935
   - inaczej: IM-UWr → **Settings** → **GitHub Apps** → „IM-UWr strona powiadomienia” → **Configure**.
   - Na górze pojawi się prośba o nowe uprawnienia: **Review request** → **Accept new permissions**. Jeśli jej nie ma, uprawnienie już obowiązuje.
   - Na tej samej stronie, w **Repository access**, musi być zaznaczone Web-Podglad. Powinno być, skoro przekaźnik wysyła tam sygnały.
4. **Sprawdzenie:** Web-Core → **Actions** → „Przekaźnik do Web-Podglad” → **Run workflow** (zleca też zwykłą przebudowę Podglądu) albo dowolny zapis w CMS.
   - W przebiegu nie ma ostrzeżenia „nie można włączać”.
   - W logu kroku „Harmonogramy” jest `IM-UWr/Web-Podglad/podglad.yml: active; PUT enable → HTTP/2.0 204 No Content`.

Skąd adresy i nazwy:
- adres instalacji podało API organizacji;
- adres strony uprawnień jest ułożony według wzoru GitHuba;
- nazwy przycisków są według GitHuba; tych stron nie otwierałem, bo wymagają konta właściciela.

Co daje to uprawnienie:
- obejmuje wszystkie repozytoria instalacji;
- pozwala m.in. włączać i wyłączać workflowy oraz uruchamiać, anulować, ponawiać i usuwać przebiegi;
- nie pozwala zmieniać plików workflowów.

Klucz aplikacji jest sekretem organizacji dostępnym w publicznych repozytoriach IM-UWr i już dziś daje zapis treści, więc ryzyko rośnie niewiele.

### Sprawdzenie

**Lokalnie, przed pushem.**
- Skrypty z workflowów wyjęte z YAML i uruchomione z atrapą `gh` w 21 scenariuszach, w `bash -e` i w `bash -e -o pipefail`; oba tryby dały ten sam wynik.
- Narzędzia: `raport-zrzuty/z43e2-skrypt/` (`wyciagnij.py`, `bin/gh`, `scenariusze.sh`); pełny wynik: `raport-zrzuty/z43e2-scenariusze.txt`.

| Skrypt | Scenariusze | Wynik |
|---|---|---|
| przekaźnik | oba aktywne, aplikacja bez uprawnienia (403) | 204 dla Web-Core; dla Web-Podglad ostrzeżenie z wyjaśnieniem o uprawnieniu; kod 0 |
| przekaźnik | oba aktywne, uprawnienie jest | dwa wiersze 204, bez ostrzeżeń |
| przekaźnik | GitHub wyłączył oba (`disabled_inactivity`), aplikacja bez uprawnienia | Web-Core włączony ponownie (ostrzeżenie); Web-Podglad: ostrzeżenie „WYŁĄCZONY” ze skutkiem i linkiem; kod 0 |
| przekaźnik | GitHub wyłączył `podglad.yml`, uprawnienie jest | włączony ponownie (ostrzeżenie) |
| przekaźnik | oba wyłączone ręcznie | ostrzeżenia, bez `PUT` |
| przekaźnik | brak klucza aplikacji; błąd odczytu stanu; błąd 500 przy `PUT`; 403 dla `GITHUB_TOKEN` | ostrzeżenia, kod 0 |
| `plan-zajec.yml`, „podtrzymanie” | `enable` 204 / 403 | notatka z datą następnego / `::error`, kod 1 |
| `plan-zajec.yml`, kontrola | oba aktywne; `disabled_inactivity` + plik nieznaleziony (404); `disabled_manually` | kod 0 / `::error` dla każdego, kod 1 |
| `podtrzymanie.yml` | oba aktywne; `podglad.yml` wyłączony przez GitHub; wyłączony ręcznie; 500 przy `PUT` | 204 dwa razy / włączony ponownie (ostrzeżenie), kod 0 / `::error` bez `PUT` / `::error` |
| `podtrzymanie.yml`, kontrola Web-Core | aktywny; `disabled_inactivity`; `disabled_manually`; błąd odczytu | kod 0 / `::error` z opisem / kod 1 |

Przy pierwszej próbie testy znalazły błąd: przy odmowie API komunikat cytował wiersz statusu zamiast komunikatu GitHuba i gubił wskazówkę o uprawnieniu aplikacji. Poprawione przed commitem.

**Na GitHubie (18.11), wszystkie zielone:**

| Przebieg | W logu |
|---|---|
| Przekaźnik [44341507520](https://github.com/IM-UWr/Web-Core/actions/runs/44341507520) (push `d436ab69`) | `IM-UWr/Web-Core/plan-zajec.yml: active; PUT enable → HTTP/2.0 204 No Content`; ostrzeżenie 403 dla Web-Podglad (oczekiwane do czasu uprawnienia); sygnał wysłany |
| Przekaźnik [44341705470](https://github.com/IM-UWr/Web-Core/actions/runs/44341705470) (zapis w CMS, `tresc-zmieniona`) | jak wyżej |
| `plan-zajec.yml` [44341565229](https://github.com/IM-UWr/Web-Core/actions/runs/44341565229) (ręcznie) | „plan”: 2026/27-Z i 2026/27-L „bez zmian” (pierwszy przebieg nowego skryptu etapu 1 w Actions). „podtrzymanie”: `PUT …/plan-zajec.yml/enable → HTTP/2.0 204 No Content`, `podglad.yml: active`, `podtrzymanie.yml: active`, „Następne: 2026-11-23 04:13 UTC” |
| Web-Podglad `podtrzymanie.yml` [44341558338](https://github.com/IM-UWr/Web-Podglad/actions/runs/44341558338) (ręcznie) | 204 dla `podglad.yml` i `podtrzymanie.yml`; `IM-UWr/Web-Core/plan-zajec.yml: active`; „Następne: 2026-11-23 04:43 UTC” |
| Podgląd [44341742516](https://github.com/IM-UWr/Web-Podglad/actions/runs/44341742516) | budowa i publikacja. Dwa wcześniejsze przebiegi (push, sygnał) przerwał nowszy sygnał, jak zwykle od zlecenia 41 |

**Przed i po** (lista kroków i wyników; `raport-zrzuty/z43e2-przed.txt`, `raport-zrzuty/z43e2-po.txt`):
- zadanie „plan”: te same kroki i wyniki co w przebiegu z harmonogramu 44274032995;
- Podgląd: te same kroki i wyniki co w 44340761376;
- przekaźnik: nowy krok 3 „Harmonogramy”, reszta bez zmian;
- plakietka stanu budowy czyta tylko przebiegi `podglad.yml`, więc przebiegi `podtrzymanie.yml` jej nie zmieniają.

**Następne podtrzymanie:**
- przekaźnik: przy każdym zapisie w CMS i pushu na main;
- co tydzień: poniedziałek 23.11.2026, 04:13 UTC (Web-Core) i 04:43 UTC (Web-Podglad).

**Dokumentacja potwierdzająca, że `enable` zeruje licznik 60 dni: nie ma** (analiza niżej). Dlatego głównym mechanizmem jest przekaźnik: włącza z powrotem niezależnie od tego, czy `enable` zeruje licznik.

**Kto dostanie powiadomienie o czerwonym przebiegu z harmonogramu.** GitHub wysyła je osobie, która ostatnio zmieniła składnię `cron` w pliku. Dla obu plików to teraz commity `d436ab69` i `6abb1bb6`, wypchnięte z konta Avean. Jeśli powiadomienia mają trafiać do właściciela, musi on sam zmienić linię `cron` w obu plikach (np. minutę).

**Co zostaje niezabezpieczone:**
- Gdy przez długi czas nie ma zapisów w CMS ani pushy, a `enable` nie zeruje licznika, GitHub może wyłączyć `plan-zajec.yml`. Wtedy jego cotygodniowe zadanie też stoi. Wykryje to kontrola z Web-Podglad (czerwony przebieg, powiadomienie), a włączy pierwszy zapis w CMS.
- Gdy oba repozytoria wyłączą się naraz, nikt tego nie zgłosi. To mało prawdopodobne, bo Web-Podglad buduje co godzinę.

### Zaplanowane workflowy IM-UWr (stan po wdrożeniu, 18.11, przez API; 24 repozytoria)

| Repozytorium | Workflow | Harmonogram | Stan | Podtrzymywany |
|---|---|---|---|---|
| Web-Core | `plan-zajec.yml` | 3 razy dziennie; podtrzymanie w poniedziałek 04:13 UTC | `active` | tak: przekaźnik przy każdym przebiegu, co tydzień `enable`, kontrola z Web-Podglad |
| Web-Podglad | `podglad.yml` | co godzinę (`23 * * * *`) | `active` | tak: co tydzień `enable` (`podtrzymanie.yml`), kontrola z Web-Core. Przekaźnik dopiero po nadaniu uprawnienia aplikacji, do tego czasu tylko ostrzega |
| Web-Podglad | `podtrzymanie.yml` (nowy) | poniedziałek 04:43 UTC | `active` | tak: co tydzień `enable` sam dla siebie, kontrola z Web-Core |
| Web-Core | `deploy.yml` | ma `schedule` | `disabled_manually` | nie; zostaje wyłączony |

Pozostałe workflowy nie mają `schedule`:
- Web-Core: `podglad-przekaznik.yml`;
- Web-Podglad: `cms-reorganizacja-test.yml`, `markdown-jawne-test.yml`;
- `powiadom.yml` w 21 repozytoriach treści.

### Analiza sprzed decyzji: dlaczego najpierw nie wdrożyłem

Zlecenie każe przed wdrożeniem sprawdzić w dokumentacji GitHub, że `PUT …/actions/workflows/<plik>/enable` zeruje licznik 60 dni. Gdy to się nie potwierdzi: „nie wdrażaj zgadywanego obejścia; opisz możliwe rozwiązania i czekaj na decyzję”. Wynik sprawdzenia:

- **Dokumentacja GitHub nie mówi, że `enable` zeruje licznik.** Mówi tylko:
  - [Disable and enable workflows](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows): w repozytorium publicznym harmonogramy wyłączają się, gdy przez 60 dni nie było „repository activity”;
  - workflow można włączyć z powrotem (także przez REST API);
  - nie mówi, co liczy się jako aktywność, ani czy `enable` na włączonym workflowie coś zmienia.
- **`liskin/gh-workflow-keepalive`** ([repozytorium](https://github.com/liskin/gh-workflow-keepalive)):
  - wywołuje dokładnie `gh api -X PUT repos/$GITHUB_REPOSITORY/actions/workflows/<plik>/enable`, z `actions: write` i `GITHUB_TOKEN`;
  - README tylko twierdzi, że to zapobiega wyłączeniu, bez źródła u GitHuba.
- **`gautamkrishnar/keepalive-workflow`** (wspomniany w zleceniu) ma dziś stronę „Access to this repository has been disabled by GitHub Staff due to a violation of GitHub's terms of service”. README nie da się przeczytać.
- **Relacja przeciwna:** w [mikmorg/lcsas#462](https://github.com/mikmorg/lcsas/issues/462) jest relacja z drugiej ręki: projekt z podtrzymaniem przez API i tak zastał swoje workflowy w stanie `disabled_inactivity`.
- **Inni:** w kilku projektach to samo rozwiązanie wprowadzono z adnotacją, że GitHub tego nie dokumentuje, np. [yiisoft/yii2-docker#187](https://github.com/yiisoft/yii2-docker/pull/187).

Wniosek: wywołanie jest powszechne i nie wymaga innego tokenu, ale działania nie potwierdza żadne źródło GitHuba, a jest jedna relacja przeciwna. Według zlecenia to „zgadywane obejście”, więc czekam na decyzję.

### Dwie rzeczy ważne dla decyzji

1. **Wyłączony workflow nie uruchamia się od żadnego zdarzenia**, nie tylko od harmonogramu. Dokumentacja: wyłączenie pozwala „stop a workflow from being triggered”.
   - Gdyby GitHub wyłączył `podglad.yml`, Podgląd nie przebudowałby się także po zapisach w CMS (`repository_dispatch`).
   - Zlecenie zakłada, że wtedy odświeżałby się „tylko po zapisach w CMS”; tak nie będzie.
2. **Web-Podglad ma już ruch:**
   - każda budowa (co godzinę i po każdym zapisie) wypycha (`push -f`) gałąź `zbudowana` tokenem `GITHUB_TOKEN`; `pushed_at` repozytorium zmienia się co godzinę;
   - nie wiadomo (GitHub nie dokumentuje), czy push bota na gałąź inną niż domyślna liczy się jako „aktywność”;
   - Web-Core ma ruch tylko przy commitach kodu i przy zmianie planu w USOS. W lecie łatwo o 60 dni ciszy.

### Możliwe rozwiązania

| Wariant | Co robi | Za | Przeciw |
|---|---|---|---|
| **A. `enable` co tydzień** (jak w zleceniu) | Osobny cron w tym samym pliku (np. `13 4 * * 1`) i osobne zadanie z `permissions: actions: write`, które woła `enable` dla zaplanowanych workflowów repozytorium. Błąd wywołania = czerwony przebieg | tanie, bez sekretów i bez commitów | działanie niepotwierdzone przez GitHub; jedna relacja, że nie pomogło |
| **B. Wzajemna kontrola** (dodatek do A albo samodzielnie) | `plan-zajec.yml` sprawdza stan `podglad.yml` w Web-Podglad, a `podglad.yml` stan `plan-zajec.yml` w Web-Core (`gh api …/workflows/<plik> --jq .state`, odczyt publiczny). Stan inny niż `active` = czerwony przebieg | wykrywa wyłączenie niezależnie od tego, czy A działa | nie włączy workflowu w drugim repozytorium (`GITHUB_TOKEN` działa tylko we własnym); nie zadziała, gdy oba wyłączą się naraz (Web-Podglad ma ruch co godzinę, więc mało prawdopodobne) |
| **C. Token właściciela (PAT albo aplikacja GitHub) jako sekret** | Wzajemna kontrola z B może wtedy od razu włączyć wyłączony workflow w drugim repozytorium | samonaprawa | nowy sekret i jego odnawianie; ustawienia repozytorium zmienia właściciel |
| **D. Commit z danymi** | np. plik stanu w Web-Core aktualizowany co kilka tygodni przez `plan-zajec.yml` | push na gałąź domyślną to jedyny sygnał, który relacje zgodnie uznają za skuteczny | zlecenie wyklucza puste commity („historia zostaje czysta”) |
| **E. Przypomnienie** | Kalendarz właściciela co 50 dni: `gh workflow list --all -R IM-UWr/Web-Core` i `-R IM-UWr/Web-Podglad`, w razie potrzeby `gh workflow enable` | zero kodu | ręczne |

**Rekomendacja: A + B.**
- A nic nie kosztuje, a jeśli działa, wyłączeń nie będzie.
- B wykrywa wyłączenie niezależnie od A i daje widoczny błąd. Powiadomienie o nieudanym przebiegu harmonogramu GitHub wysyła do osoby, która ostatnio zmieniła składnię `cron` w pliku ([events-that-trigger-workflows, schedule](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)), czyli do właściciela, jeśli to jego commit zmieni `cron`.
- Szkic zadania A w `plan-zajec.yml` (do wdrożenia po decyzji; tak samo w `podglad.yml`, z dodaniem `podglad.yml` do listy):

```yaml
  # nowy wpis w on.schedule:  - cron: '13 4 * * 1'   # podtrzymanie (poniedziałek)
  podtrzymanie:
    if: github.event.schedule == '13 4 * * 1' || github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    permissions:
      actions: write
    steps:
      - name: Podtrzymanie harmonogramu (enable przez API)
        env:
          GH_TOKEN: ${{ github.token }}
        run: gh api -X PUT -i "repos/${{ github.repository }}/actions/workflows/plan-zajec.yml/enable" | head -1
  # zadanie „plan” dostaje: if: github.event.schedule != '13 4 * * 1'
```

## Etap 3. Logo UWr prowadzi na stronę główną UWr (`057513dc`)

**Stan na świeżym `main`:** zrobione w zleceniu 32, punkt 8 (`c2c193e0`):
- pasek: `a.z-marka-uwr` i `a.z-marka-im`;
- okładka: `a.z-okl-uwr` i `a.z-okl-wydzial`;
- telefon: `a.brand-uwr` bez zmian.

**Poprawione tylko to, czego punkt 8 nie objął.** W linku Wydziału na okładce komputera dopisek dla czytników ekranu stał przed nazwą: nazwa dostępna „(inna strona) Wydział Matematyki i Informatyki”. Zlecenie wymaga „po nazwie, nie przed”. Teraz:
- PL: „Wydział Matematyki i Informatyki (inna strona)”;
- EN: „Faculty of Mathematics and Computer Science (external site)” (drzewo dostępności Edge, `raport-zrzuty/z43-nazwy-dostepne.txt`).

Nazwa dostała klasę `z-okl-wydzial-nazwa`. Wcześniej style (kreska, kolor po najechaniu) i skrypt układu tytułu okładki szukały jej jako `span:last-child`, a po przeniesieniu dopisku ostatni byłby dopisek. Specyficzność selektorów stylów bez zmian.

### `elementFromPoint` na środku logo i napisu (budowa `tresci-B/z43-po2`, Edge; `raport-zrzuty/z43-logo/logo43.json`)

| Gdzie | Szerokości | Logo → | Napis → |
|---|---|---|---|
| Okładka strony głównej (PL) | 1920×950, 1366×768, 1024×768 | `a.z-okl-uwr` → `https://uwr.edu.pl/` ✅ | `a.z-okl-wydzial` → `https://wmi.uwr.edu.pl/` ✅ |
| Okładka `/en/` | jw. | `https://uwr.edu.pl/en/` ✅ | `https://wmi.uwr.edu.pl/` ✅ |
| Pasek: drugi ekran głównej i `/instytut/wladze` (PL) | jw. | `a.z-marka-uwr` → `https://uwr.edu.pl/` ✅ | `a.z-marka-im` → `/` (strona główna Instytutu) ✅ |
| Pasek `/en/` (drugi ekran) | jw. | `https://uwr.edu.pl/en/` ✅ | `/en/` ✅ |
| Telefon: główna (okładka) | 390×844 | `a.brand-uwr` → `https://uwr.edu.pl/` ✅ | `a.brand-txt.z-wydzial` → `https://wmi.uwr.edu.pl/` |
| Telefon: po przewinięciu, `/instytut/wladze` | 390×844 | `a.brand-uwr` → `https://uwr.edu.pl/` ✅ | `a.brand-txt` → `/` |
| Telefon `/en/` | 390×844 | `https://uwr.edu.pl/en/` ✅ | jak PL, wersje EN |

- **`aria-label` logo:**
  - pasek i okładka: „Uniwersytet Wrocławski — strona główna UWr (inna strona)” / „University of Wrocław — main website (external site)”;
  - telefon: bez dopisku, jak dotąd.
- **Strzałka ↗:** przy logo jej nie ma (sprawdzone w treści linków).

### Kolejność Tab od początku strony (`raport-zrzuty/z43-tab.txt`, `z43-logo.txt`)

- **Strona główna 1920×950 i 1024×768:**
  1. „Przejdź do treści”;
  2. logo UWr;
  3. „Wydział Matematyki i Informatyki”;
  4. przełącznik trybu;
  5. „English version”;
  6. menu;
  7. kafelki działów.

  Fokus cały czas na okładce: `scrollY` 0, element w oknie, krycie 1.
- **Podstrona `/instytut/wladze` (1366×768; tak samo 1920 i 1024):**
  1. „Przejdź do treści”;
  2. logo UWr;
  3. „Instytut Matematyczny / Wydział…”;
  4. pozycje menu.

  Logo i napis mają obwódkę 3 px, menu 2 px.
- **Podstrona `/instytut/wladze` na telefonie (390×844):**
  1. „Przejdź do treści”;
  2. logo;
  3. „Instytut Matematyczny…”;
  4. wersja językowa;
  5. tryb.
- **Telefon 390×844 (główna PL i EN):**
  1. „Przejdź do treści”;
  2. logo;
  3. nazwa Wydziału;
  4. wersja językowa;
  5. tryb;
  6. menu;
  7. kafelki.
- **Każdy link ma własny widoczny fokus** (obwódka) **i własne podświetlenie:**
  - po najechaniu na logo krycie logo 0,75, a kolor nazwy obok się nie zmienia;
  - po najechaniu na nazwę kolor nazwy `#fff`, a logo się nie zmienia;
  - przed i po poprawce identycznie.

### Zrzuty przed/po (`raport-zrzuty/z43-piksele/`, kontrola `z43-piksele-kontrola/`)

- **Zakres:** 18 par (strona główna: okładka i drugi ekran; `/en/`; `/instytut/wladze`; 1920×950, 1366×768, 1024×768, 390×844).
- **13 par:** 0 różnic pikselowych.
- **5 par z różnicą:**
  - dół drugiego ekranu przy 1920 (PL i EN);
  - rysunek w banerze `/instytut/wladze` przy 1024, 1366 i 390.

  Te same miejsca różnią się między dwoma wczytaniami tej samej budowy (kontrola), więc to treść zmienna, nie poprawka.
- **Obszar logo i napisu:** we wszystkich parach bez różnic.

### Porównanie HTML (budowa przed i po poprawce)

- Różnią się tylko `index.html` i `en/index.html`: kolejność dopisku i nazwy, klasa nazwy, selektor w skrypcie okładki.
- Poza tym tylko znaczniki czasu (`.ics`, `seminaria/powiadomienia.json`) i nazwy plików `_astro` (zmieniony CSS).

## Odstępstwa od zlecenia i powody

- **Etap 2 najpierw niewdrożony.** Dokumentacja GitHub nie potwierdza, że `enable` zeruje licznik, i jest relacja przeciwna; zlecenie każe wtedy opisać możliwości i czekać. Wdrożony po decyzji właściciela z 18.11, inaczej niż w zleceniu: główny mechanizm to przekaźnik, cotygodniowe `enable` jest tylko zapasem.
- **Brak linku do dokumentacji potwierdzającej zerowanie licznika** (punkt odbioru etapu 2): takiej dokumentacji nie ma. Decyzja właściciela tego nie wymaga, bo przekaźnik włącza z powrotem niezależnie od licznika.
- **W Web-Podglad osobny plik `podtrzymanie.yml`**, nie zadanie w `podglad.yml`, jak szkicowałem w propozycji. Powód w decyzjach niżej.
- **Etap 3 to nie tylko odbiór.** Poprawiłem kolejność dopisku „(inna strona)” w linku Wydziału na okładce, bo punkt 2 etapu tego wymaga, a zlecenie 32 tego nie objęło. Wygląd bez zmian (zrzuty).
- **Semestr nieznany w USOS jest pomijany przy pobieraniu**, choć zlecenie mówi tylko o zapisie pustego wpisu. Powód: dla nieistniejącego semestru tryb awaryjny API zrobiłby do 2500 zapytań przy każdym z trzech dziennych przebiegów.

## Decyzje podjęte samodzielnie (wartości domyślne zlecenia)

- **Brak semestru w USOS jest zwykłą informacją w logu, nie ostrzeżeniem.** Przyjąłem tak, bo zlecenie mówi „nie zgłasza błędu”, a ostrzeżenie pojawiałoby się 3 razy dziennie do czasu dodania semestru w USOS.
- **Test etapu 1 zostaje lokalnie** (`raport-zrzuty/z43-skrypt/`), nie w repozytorium. Przyjąłem tak, bo zlecenie każe tylko wpisać wynik do raportu.
- **Bez ręcznego uruchamiania `plan-zajec.yml` po pushu etapu 1**, bo najbliższy zaplanowany przebieg (15:47 UTC) sprawdzi nowy skrypt w Actions sam. Ręczne uruchomienie przyszło i tak z odbiorem etapu 2 (przebieg 44341565229, „bez zmian”).

Etap 2:
- **Przekaźnik wywołuje `enable` także na włączonym workflowie.** Przyjąłem tak, bo bez tego ostrzeżenie o braku uprawnienia aplikacji pojawiłoby się dopiero po wyłączeniu. Właściciel nie zobaczyłby, czy ustawienie zadziałało. `enable` na włączonym nic nie zmienia, a może podtrzymywać licznik.
- **Workflowu wyłączonego ręcznie (`disabled_manually`) nie włącza ani przekaźnik, ani cotygodniowe podtrzymanie;** zostaje ostrzeżenie albo czerwony przebieg. Przyjąłem tak, bo ręczne wyłączenie to czyjaś decyzja, jak przy `deploy.yml`. Inaczej celowe wyłączenie Podglądu cofałby pierwszy zapis w CMS. Wyłączenie przez GitHub (`disabled_inactivity`) jest włączane zawsze. Pytanie 1 niżej.
- **W Web-Podglad osobny plik `podtrzymanie.yml`.** Przyjąłem tak, bo plakietka stanu budowy na stronie czyta przebiegi `podglad.yml`:
  - udany przebieg bez budowy wyglądałby jak „nowa wersja”;
  - czerwony wyglądałby jak „budowa nieudana”.

  Nowy plik sam ma harmonogram, więc podtrzymuje sam siebie i jest sprawdzany z Web-Core.
- **Token do Web-Podglad: ten sam co do sygnału, bez zawężania do Actions.** Przyjąłem tak, bo żądanie tokenu z `permission-actions: write` nie udałoby się do czasu kliknięcia właściciela i zatrzymałoby sygnał.
- **Godziny: poniedziałek 04:13 i 04:43 UTC.** Przyjąłem je, bo są poza godzinami trzech pobrań planu i z dala od pełnej godziny.
- **README:** opis aplikacji poprawiony z „zainstalowana tylko na Web-Core” na Web-Core i Web-Podglad, bo przekaźnik od zlecenia 41 używa jej w Web-Podglad.

## Pytania do użytkownika

1. **Etap 2, workflow wyłączony ręcznie:** przekaźnik i podtrzymanie go nie włączają, tylko ostrzegają (przekaźnik) albo dają czerwony przebieg (co tydzień). Zostawić tak, czy włączać każdy nieaktywny, jak dosłownie w decyzji? Zmiana to jeden warunek w trzech plikach.

**Do zrobienia przez właściciela (nie pytanie):** uprawnienie Actions: Read and write dla aplikacji „IM-UWr strona powiadomienia”, instrukcja w etapie 2.
2. **Telefon:** w linku Wydziału na okładce telefonu (`Naglowek.astro`, `a.brand-txt.z-wydzial`) dopisek „(inna strona)” też stoi przed nazwą. Zlecenie każe zostawić telefon bez zmian, więc go nie ruszałem. Poprawić tak samo jak na komputerze?
3. **Tryb awaryjny etapu 1:** gdy API nie odpowiada, a eksport działa, nowe dane semestru nie mają dat, więc strona do następnego udanego przebiegu otwiera pierwszą zakładkę (zimową). Tak było też przed zmianą. Brać wtedy daty z poprzedniego pliku?

## Do sprawdzenia jutro

- **Przebiegi `plan-zajec.yml` z 18.11 (15:47 UTC) i 19.11:** zielone, „Bez zmian w USOS”, w podsumowaniu 2026/27-Z i 2026/27-L.
  - 16:13 UTC: z harmonogramu jeszcze żadnego (opóźnienie GitHuba); ręczny 44341565229 z nowym skryptem zielony, wynik jak wyżej. Ponowna kontrola o 20:03.
- **Podgląd na żywo:** link Wydziału na okładce ma dopisek po nazwie, wygląd bez zmian.
- **Etap 2, po kliknięciu właściciela:** najbliższy przebieg przekaźnika bez ostrzeżenia „nie można włączać”, w logu `IM-UWr/Web-Podglad/podglad.yml: active; PUT enable → HTTP/2.0 204 No Content`.
- **Etap 2, 23.11:**
  - pierwsze cotygodniowe przebiegi zielone: Web-Core 04:13 UTC (tylko zadanie „podtrzymanie”, „plan” pominięte), Web-Podglad 04:43 UTC;
  - plakietka Podglądu bez zmian.
