# Raport: zlecenie 42 — osoby w formularzach CMS wybierane ze spisu pracowników; osoby, które odeszły (19.11.2026)

**Stan: zrobione i wypchnięte** (push samodzielny według polecenia z 19.11, po spełnieniu warunków: budowa PL i EN, kontrole i testy zielone, porównanie HTML wyjaśnione, fetch i rebase z budową po rebase, pełna „Ochrona zmian redaktorów” w każdym repozytorium treści, cisza). Etap 0 nie znalazł nowych przypadków niejednoznacznych — bez STOP. Kolejność jak w zleceniu: najpierw Web-Core, potem treści (Web-Pracownicy, Web-Instytut, Web-Nauka, 9 seminariów, Web-Studia), każde repozytorium jednym commitem i osobną kontrolą, po każdym pushu przebieg Podglądu.

Gałęzie robocze `praca/42-osoby` (Web-Core i 13 klonów w `tresci-C`) zostają lokalnie. Automat katalogu czeka na klucze (sekcja „Klucze automatu”); do tego czasu katalog odświeża skrypt.

## Co zmieniono

- **Web-Core** (`608d6337`, jeden commit):
  - `src/content.config.ts`: nowe pola `kierownik_ze_spisu`, `kierownik_spoza` (granty), `karta.kierownik_ze_spisu` (zakłady), `prowadzacy_ze_spisu`, `prowadzacy_spoza` (seminaria), `pracuje`, `data_odejscia` (pracownicy). Pole „… ze spisu” zapisuje ścieżkę `_cms/pracownicy/<id>.yml`; schemat zamienia ją na `<id>`. Stare pola tekstowe zostają w schemacie i dalej działają.
  - `src/lib/osobySpisu.ts` (nowy): osoba po id, „pracuje”, ostrzeżenia w logu budowy (na GitHubie adnotacja `::warning`), kierownik zakładu i koordynatorzy seminarium jako funkcje, zbieranie funkcji bez osoby. `src/lib/brakiOsob.ts` (nowy): funkcje bez osoby na danej stronie dla plakietki stanu budowy.
  - `src/components/BrakOsoby.astro` (nowy): znacznik „nie przypisano osoby — uzupełnij w CMS” / „no person assigned — fill in the CMS” w stylu etykiety „szkic”. `src/middleware.ts`: styl etykiety także przy znaczniku, z zawijaniem w wąskich kolumnach.
  - `src/components/zal/StanBudowy.astro`: wiersz „Nie przypisano osoby: <funkcja>. Popraw w CMS →” z linkiem do formularza (tylko budowa Podglądu, `PODGLAD=1`).
  - Strona: `tresci.ts` (kierownicy grantów ze spisu albo spoza, zakład grantu z kierownika ze spisu; stare pole jak dotąd), widoki `grant`, `listaGrantow`, `zaklad`, `listaZakladow`, `seminarium`, `listaSeminariow`, `specjalnosc`, `kierunek`, `wladze`, `pracownicy` i odpowiadające im `views/*.astro`, `OsobaZ.astro`, `WladzeZ.astro`, `podglad.ts`.
  - Skrypty: `skrypty/migracja/osoby_42.py` (migracja, jednorazowa; odmawia na przerobionych plikach), `skrypty/migracja/formularze_40.mjs` (formularze zlecenia 42 w generatorze), `skrypty/synchronizuj-katalog-pracownikow.mjs` (zastępuje `synchronizuj-katalog-opiekunow.mjs`), `skrypty/sprawdz_tresci.py` (ostrzeżenia o funkcji bez osoby i o odwołaniu spoza spisu), `skrypty/test-edytora/formularz.mjs` (scenariusz 14).
  - Dokumentacja: `dok/sciagawka-edytora.md` (nowa sekcja „Osoby: wybór ze spisu pracowników”, oba zdania ze zlecenia), `dok/jawny-markdown.md` (opiekun, który odszedł; skrypt i automat katalogu). Pola do CMS: `.przekazanie\pola-do-cms.md`, sekcja „Zlecenie 42”.
- **Repozytoria treści** (każde jednym commitem z `.pages.yml` i danymi razem):

| Repozytorium | Co w commicie | Push | Godzina | Podgląd (Web-Podglad) |
|---|---|---|---|---|
| **Web-Core** | kod, skrypty, dokumentacja (wyżej) | `67ac130f..608d6337` | 13:46 | 44527092696 sukces (1 min 36 s) |
| Web-Pracownicy | `pracuje: true` w 128 plikach, `.pages.yml` (pole „Pracuje w Instytucie”, „Data odejścia”, usuwanie wyłączone), `.github/workflows/katalog-pracownikow.yml` | `ff4aec1..19c92b2` | 13:49 | 44527502592 sukces; automat katalogu: przebieg 44527436019 „skipped” (czeka na zmienną) |
| Web-Instytut | 9 zakładów, `src/data/wladze.json`, `.pages.yml`, katalog 128 plików | `e88a088..d14657e` | 13:51 | 44527865944 sukces |
| Web-Nauka | 94 granty, `.pages.yml`, katalog | `51626f2..2db3479` | 13:54 | 44528245670 sukces |
| Web-Sem-Analiza-Harmoniczna | opis seminarium, `.pages.yml`, katalog | `e25b641..f3cbe4a` | 13:56 | 44528585524 sukces |
| Web-Sem-Dydaktyka | jw. | `b3d6e7f..7d0c6db` | 13:58 | 44528916002 sukces |
| Web-Sem-Dyskretna-Analiza-Harmoniczna | jw. | `81716a7..4b9f116` | 14:00 | 44529277494 sukces |
| Web-Sem-Geometria | jw. | `1700d8a..0787017` | 14:03 | 44529691622 sukces |
| Web-Sem-Prawdopodobienstwo | jw. | `15169e5..c94a533` | 14:05 | 44530111038 anulowany przez kolejkę (nowszy push), objęty przez 44530211833 sukces |
| Web-Sem-Rownania-Rozniczkowe | jw. | `ba24c65..ac693ee` | 14:06 | 44530211833 sukces |
| Web-Sem-Statystyka | jw. | `699c086..4a5d5d3` | 14:08 | 44530582788 sukces |
| Web-Sem-Teoria-Modeli | jw. | `5a96f65..e1c73b9` | 14:10 | 44530927393 sukces |
| Web-Sem-Topologia | jw. | `1cf30da..75558dc` | 14:13 | 44531311455 sukces |
| Web-Studia | `.pages.yml` (opiekunowie na wspólnym katalogu), zdanie w `README-jawny-markdown.md`, katalog odświeżony (usunięty duplikat bez odwołań) | `e7e297e..608f1dc` | 14:16 | 44531873228 sukces |

Wszystkie pushe to zwykłe fast-forwardy, bez force-push i bez revertów. W logach przebiegów Podglądu 0 ostrzeżeń „Brak osoby” / „Osoba spoza spisu”. Na żywo sprawdzone: listy grantów zakładów z nazwiskami ze spisu, grant z przykładu z 13.11 z zakładem, lista seminariów z nową kolejnością, specjalność „matematyka nauczycielska” jak lokalnie, 0 znaczników „nie przypisano osoby”.

Katalog `_cms/pracownicy/` (128 plików) jest w każdym z 12 repozytoriów z polami osób.

## Etap 0 — inwentaryzacja (kontrola na świeżym main)

**Wynik: brak nowych przypadków niejednoznacznych albo podejrzanych → bez STOP.** Liczby zgodne z przeglądem z 18.11 co do sztuki.

| Repozytorium · pole | Rodzaj | Wpisy | Pewne (pełne / inicjał) | Niejednoznaczne / podejrzane | Brak w spisie |
|---|---|---|---|---|---|
| Web-Nauka · granty → `kierownik` | historia | 95 | 81 (34 / 47) | 0 | 14 |
| Web-Instytut · zakłady → `karta.kierownik` | funkcja | 9 | 9 | 0 | 0 |
| Web-Sem-* (9) · `prowadzacy` | funkcja | 21 | 16 | 0 | 5 |
| Web-Instytut · władze → `osoby` (dyrekcja) | funkcja | 5 | 5 | 0 | 0 |
| Web-Instytut · władze → `wydzial.osoby` | funkcja | 2 | 2 | 0 | 0 |
| Web-Instytut · władze → `sekretariat.osoby` | funkcja | 2 | 2 | 0 | 0 |
| Web-Studia · specjalności → `opiekunowie` | funkcja | 7 | 7 (już wybór) | 0 | 0 |
| Web-Nauka · granty → `wykonawcy` | historia, tekst bez zmian | 59 | 27 | 0 | 32 |
| Web-Aktualnosci · obrony → `recenzje.recenzent` | historia, tekst bez zmian | 15 | 0 | 0 | 15 |

- **Brak w spisie** (→ „spoza spisu”): granty — Kisielewicz ×3, Jasiulis-Gołdyn ×2, Palmowski, Śniady, Więsław, Iwanow, Krupski, Czarna, Kosiński, Celiński, Kotelnykova (14); seminaria — Krzysztof Stempak, Adam Nowak (IM PAN) (Analiza Harmoniczna), Paweł Krupski, Szymon Żeberski, Robert Rałowski (Topologia). Dokładnie jak w przeglądzie. Grant „Ekstrema fragmentacji…” („mgr T. Mika”) dopasowuje się sam do `tamara-mika`.
- **Nowe pola z osobami:** nie znalazłem innych pól, w których strona bierze dane ze spisu. Promotorów obron nie ma dziś w żadnym wpisie (obrony mają tylko recenzentów); prelegenci, autorzy publikacji i organizatorzy — poza zakresem (jak w zleceniu).
- **Spis pracowników:** 128 plików, wszystkie widoczne (`opublikowany: false`: 0). Grupy: nauczyciel 81, emeryt 23, doktorant 17, administracja 7. Te same imię i nazwisko w kilku plikach: brak. Odejścia nie były dotąd oznaczane polem; jedyny usunięty plik w historii Web-Pracownicy to `elzbieta-kalinowska-administracja.yml` (11.11, Pages CMS) — duplikat osoby, która zostaje jako `elzbieta-kalinowska.yml`. Do usuniętego pliku nie ma odwołań w danych; był tylko w starym katalogu Web-Studia (usunięty przy synchronizacji, w logu).
- **Pages CMS** (kod źródłowy `fields/core/reference`, `lib/schema.ts`):
  - `reference` wskazujący plik spoza katalogu: walidacja sprawdza tylko, czy wartość nie jest pusta; formularz trzyma zapisaną ścieżkę i zapisuje ją z powrotem bez zmian (symulacja: scenariusz 14, grant z kierownikiem, który „odszedł”). Lista wyboru może wtedy nie pokazać etykiety, ale wartość nie znika. Katalog i tak nie kasuje osób, do których są odwołania.
  - Kolejności pozycji na liście wyboru nie da się ustawić w konfiguracji (opcje `search` i `value`/`label`, bez sortowania). Byli pracownicy są więc w porządku alfabetycznym z dopiskiem „(były pracownik)” w etykiecie, a nie na końcu.

## Migracja (skrypt `osoby_42.py`, raport)

| Repozytorium · pole | Do spisu | Spoza spisu | Uwagi |
|---|---|---|---|
| Web-Pracownicy · `pracuje` | 128 × `pracuje: true` | — | nikogo nie oznaczono jako byłego pracownika (decyzja 18.11) |
| Web-Nauka · granty → kierownik | 81 | 14 | 95 plików; kolejność osób jak w tekście |
| Web-Instytut · zakłady → kierownik | 9 | 0 | |
| Web-Instytut · dyrekcja | 5 | 0 | rola, zakres, dyżur, zdjęcie i EN bez zmian |
| Web-Instytut · władze Wydziału | 2 | 0 | 2 e-maile `@uwr.edu.pl` przeniesione do „Inne dane niż w spisie” |
| Web-Instytut · sekretariat | 2 | 0 | |
| Web-Sem-* · koordynatorzy | 16 | 5 | AH 3+2, Dydaktyka 1, DAH 2, Geometria 1, Prawdopodobieństwo 2, Równania 3, Statystyka 1, Teoria Modeli 1, Topologia 2+3 |

Przypadki niepewne: 0. Skrypt pomija już przerobione pliki (jednorazowość) i przy powtórnym uruchomieniu na świeżym main daje ten sam wynik.

## Strona: porównanie HTML przed i po

Budowy po rebase (Core `608d6337`), wszystkie PL i EN, 5001 plików każda. Narzędzie: `tresci-C/porownaj.py`, wyniki `tresci-C/z42-*-roznice.txt`.

| Porównanie | Wynik |
|---|---|
| strona dziś (`z55-push`, publiczna) → nowy Core + stare treści, publiczna (`z42-core2-pub`) | **0 różnic** (4892 identyczne, 108 tylko znacznik czasu, kolejność w sitemap) |
| stary Core + stare treści, Podgląd (`z42-stary-podglad`) → nowy Core + stare treści, Podgląd (`z42-core2`) | **0 różnic** (jw.) |
| `z55-push` → nowy Core + treści po migracji, publiczna (`z42-po2-pub`) | 24 pliki, wszystkie wyjaśnione (niżej) |
| `z42-core2` → nowy Core + treści po migracji, Podgląd (`z42-po2`) | te same 24 pliki |

Czyli push samego Web-Core nie zmienia strony, a zmiany przychodzą dopiero z danymi po migracji:

- **Listy grantów na stronach 8 zakładów (PL i EN) i „Realizowane projekty” na stronie Nauki (PL i EN), 18 plików:** kierownik ze spisu wyświetla się z aktualnym imieniem i tytułem ze spisu zamiast tekstu wpisanego przy grancie, np. „Kierownik: dr M. Valiunas” → „dr Motiejus Valiunas”, „dr hab. Ś. Gal” → „dr hab. Światosław Gal, prof. UWr”, „mgr D. Danielski” → „dr Daniel Danielski”, EN „J. Gogolok” → „Dr Jakub Gogolok”. Strona grantu robiła tak już przed zleceniem (tytuł ze spisu); teraz tak samo listy. Zgodne z etapem 5 („aktualne imię, nazwisko i tytuł ze spisu”).
- **Seminaria Analiza Harmoniczna i Topologia (PL i EN), 4 pliki, i lista seminariów (PL i EN), 2 pliki:** koordynatorzy w kolejności „najpierw ze spisu, potem spoza” (etap 3), np. AH: Dziubański, Wróbel, … , Adam Nowak (IM PAN), Krzysztof Stempak; na liście seminariów „Jacek Dziubański, Błażej Wróbel i 3 inne osoby” zamiast „…, Adam Nowak (IM PAN) i 3…”. Teksty osób spoza spisu bez zmian.
- Brak znaczników „nie przypisano osoby” i ostrzeżeń w logach budowy (0 w czterech budowach) — po migracji każda funkcja ma osobę.
- Linki i zakłady, które dotąd brakowały: grant „Ekstrema fragmentacji…” (kierownik „mgr T. Mika”) ma teraz zakład (Zakład Analizy Funkcjonalnej) — strona grantu dopasowywała go już po 13.11 (poprawka redaktora), więc w HTML bez różnicy.

## Test osoby, która odchodzi (kopia lokalna, cofnięty)

Na klonach ustawiłem `pracuje: false` u Jacka Świątkowskiego (kierownik zakładu Geometrii, koordynator seminarium Geometrii, opiekun specjalności „matematyka nauczycielska”) i u Damiana Osajdy (kierownik grantu `2018-2017-25-b-st1-01335`), potem katalog skryptem i trzy budowy (Podgląd, Podgląd z plakietką `PODGLAD=1`, publiczna):

- Podgląd: zakład Geometrii — w karcie „Kierownik” znacznik „nie przypisano osoby — uzupełnij w CMS” (PL) / „no person assigned — fill in the CMS” (EN); lista zakładów, seminarium Geometrii i specjalność — ten sam znacznik; grant — nazwisko z tytułem jako zwykły tekst, bez linku i bez dopisku. **Spełnione.**
- Plakietka stanu budowy: wiersz „Nie przypisano osoby: Kierownik zakładu. Popraw w CMS →” z linkiem do formularza zakładu. **Spełnione.**
- Log budowy: ostrzeżenia `[Brak osoby] …` (na GitHubie jako `::warning`, od nowej linii). **Spełnione.**
- Budowa publiczna (`TYLKO_OPUBLIKOWANE=1`): zakład bez wiersza „Kierownik” (reszta karty zostaje), seminarium bez wiersza koordynatora, grant jak na Podglądzie. **Spełnione.**
- Spis pracowników: 128 → 126 osób (także wyszukiwarka i listy zakładów). Osobnych stron profilu strona nie ma, więc nie ma czego ukrywać. **Spełnione.**
- Katalog: etykieta z dopiskiem „(były pracownik)”. **Spełnione.**
- `sprawdz_tresci.py`: 3 nowe ostrzeżenia (kierownik zakładu, koordynator seminarium, opiekun specjalności). Bez testu: OK, 0 nowych ostrzeżeń.
- Po teście klony przywrócone (`git checkout`), katalog też; kontrola pole po polu potwierdza stan sprzed testu.

## Symulacja CMS (scenariusz 14, `skrypty/test-edytora/formularz.mjs`)

Wszystkie punkty OK:
- granty: „Kierownik ze spisu pracowników” (wybór, kilka osób) i zaraz pod nim „Kierownik spoza spisu” (tekst, lista);
- stary grant z kierownikiem, który „odszedł”, otwarty i zapisany bez zmian: odwołanie zostaje, dane te same;
- grant z kierownikiem spoza spisu: zapis bez zmian zachowuje tekst;
- nowy grant: lista wyboru 128 osób z katalogu Web-Nauka, bez danych kontaktowych; dwie osoby ze spisu i jedna spoza zapisują się jak oczekiwano;
- zakład, Topologia (2 ze spisu + 3 spoza), władze (dyrektor, „Inne dane” dziekana, sekretariat): zapis bez zmian bez strat;
- pozycja dyrekcji bez osoby: zapis zablokowany („This field is required”);
- pracownicy: plik bez pola `pracuje` po zapisie dostaje `pracuje: true` (domyślna), odznaczenie i data odejścia zapisują się, nowa osoba startuje z zaznaczonym polem, usuwanie wyłączone (`operations.delete: false`);
- katalog „Katalog pracowników (tylko odczyt)” w 12 repozytoriach: tylko odczyt, ta sama lista.

Zapis bez zmian wszystkich 2160 plików w nowej konfiguracji: różnice w 6 plikach, te same co przed zleceniem (pusta Treść obron i jednego grantu dostaje szablon z `default` — znane od zlecenia 54B, nie dotyczy osób).

## Automat i katalog

- `skrypty/synchronizuj-katalog-pracownikow.mjs <Web-Pracownicy> <repo…> [--na-sucho]`: zapisuje `_cms/pracownicy/<id>.yml` (`imie_nazwisko`, `id`, `etykieta`, `pracuje`) w 12 repozytoriach (Web-Instytut, Web-Nauka, Web-Studia, 9 × Web-Sem-*). Etykieta przy duplikatach nazwisk z grupą, przy `pracuje: false` z dopiskiem „(były pracownik)”. Plik usuwa tylko, gdy osoby nie ma w spisie i nikt się do niej nie odwołuje (każde usunięcie w logu). Dziś: 128 osób w każdym katalogu; jedno usunięcie (`Web-Studia/_cms/pracownicy/elzbieta-kalinowska-administracja.yml`, duplikat bez odwołań).
- Tryb „na sucho” (w teście osoby, która odchodzi): wypisuje zmienione pliki (np. `~ Web-Instytut/_cms/pracownicy/damian-osajda.yml`) i niczego nie zapisuje.
- Automat: `Web-Pracownicy/.github/workflows/katalog-pracownikow.yml` — po pushu na main ze zmianą spisu, codziennie o 3:17 UTC i ręcznie (z opcją „na sucho”). Commituje tylko `_cms/pracownicy/`, zwykły push, przy odrzuceniu `pull --rebase` i do 3 prób, nigdy force-push. **Wyłączony do czasu ustawienia kluczy** (warunek `vars.KATALOG_PRACOWNIKOW == 'wlaczony'`), więc nie daje czerwonych przebiegów.

## Rzeczy do sprawdzenia w CMS (właściciel, po pushu)

Symulator odtwarza logikę zapisu Pages CMS, ale nie jego wygląd. Do obejrzenia w prawdziwym CMS (najlepiej po odświeżeniu strony CMS, żeby wczytała nową konfigurację):
- Web-Nauka → Granty → dowolny grant: pole „Kierownik ze spisu pracowników” (lista wyboru, wpisz nazwisko) i pod nim „Kierownik spoza spisu”; czy wybrane osoby pokazują się z imieniem (etykietą), a nie ze ścieżką pliku.
- Web-Instytut → Zakłady (karta → Kierownik), Władze (osoba ze spisu, zwinięta grupa „Inne dane niż w spisie”, sekretariat).
- Dowolne seminarium → opis seminarium: „Koordynatorzy ze spisu pracowników” i „Koordynatorzy spoza spisu”.
- Web-Pracownicy → osoba: przełącznik „Pracuje w Instytucie” i „Data odejścia (opcjonalnie)”; brak usuwania.
- Widoki list (granty, zakłady): kolumna z polem „ze spisu” może pokazywać ścieżkę `_cms/pracownicy/…yml` zamiast imienia. Jeśli przeszkadza — do usunięcia z `view.fields` (jedna linia w generatorze).

## Klucze automatu: co kliknąć (właściciel)

Automat korzysta z tej samej aplikacji organizacji co `powiadom.yml` (zmienna `POWIADOM_APP_ID`, sekret `POWIADOM_KLUCZ`, ustawione dla całej organizacji). Do czasu tych kroków katalog odświeżam ręcznie skryptem (dziś zrobione dla 12 repozytoriów).

1. **Uprawnienie aplikacji** (jeśli jeszcze nie ma): GitHub → organizacja IM-UWr → Settings → Developer settings → GitHub Apps → aplikacja powiadomień (`im-uwr-strona-powiadomienia`) → Edit → Permissions & events → Repository permissions → **Contents: Read and write** → Save. Jeśli GitHub poprosi o akceptację nowych uprawnień: Settings → GitHub Apps (Installed) → ta aplikacja → **Accept new permissions**. (Wysyłanie sygnału do Web-Core w `powiadom.yml` już wymaga zapisu w Contents, więc najpewniej jest ustawione.)
2. **Dostęp do repozytoriów:** IM-UWr → Settings → GitHub Apps (Installed GitHub Apps) → ta aplikacja → Configure → Repository access → „Only select repositories” → dodaj 12 repozytoriów: **Web-Instytut, Web-Nauka, Web-Studia, Web-Sem-Analiza-Harmoniczna, Web-Sem-Dydaktyka, Web-Sem-Dyskretna-Analiza-Harmoniczna, Web-Sem-Geometria, Web-Sem-Prawdopodobienstwo, Web-Sem-Rownania-Rozniczkowe, Web-Sem-Statystyka, Web-Sem-Teoria-Modeli, Web-Sem-Topologia** (Web-Core zostaje) → Save.
3. **Włączenie automatu:** IM-UWr/Web-Pracownicy → Settings → Secrets and variables → Actions → zakładka Variables → New repository variable → nazwa **`KATALOG_PRACOWNIKOW`**, wartość **`wlaczony`** → Add variable.
4. **Próba:** Web-Pracownicy → Actions → „Katalog pracowników w CMS” → Run workflow → zaznacz „Tylko pokaż, co by się zmieniło” → Run. Oczekiwany wynik: zielony przebieg, w logu 12 linii „katalog 128 osób, zmian: 0”. Potem raz bez zaznaczenia (też „zmian: 0”, bez commitów).
5. Od tej chwili automat działa sam: po każdej zmianie spisu (zapis w CMS), codziennie o 4:17 czasu polskiego (3:17 UTC) i ręcznie. Commity w repozytoriach treści podpisuje „Katalog pracowników (automat)”.

Gdyby przebieg był czerwony z błędem klucza („Resource not accessible by integration”, „Not Found”) — brakuje kroku 1 albo 2 dla któregoś repozytorium.

## Kontrole (odbiór lokalny)

- `npx astro check`: 0 błędów, 0 ostrzeżeń, 8 podpowiedzi (jak po 53–55). `npm run test:jawne`: **84/84**.
- `sprawdz_tresci.py` (nakładka z treści po migracji): **OK**, 594 pliki i 106 ciekawostek, 0 ostrzeżeń. W teście osoby, która odchodzi: 3 nowe ostrzeżenia o funkcji bez osoby (zgodnie ze zleceniem).
- `sprawdz_pola_cms.py ../tresci-C` (klony po migracji): 2160 plików w 16 repozytoriach, **0 problemów**.
- Symulator formularzy: scenariusz 14 — wszystko OK; „zapis bez zmian” — 6 znanych różnic sprzed zlecenia (wyżej).
- Budowy PL i EN: wszystkie przechodzą (publiczna i Podgląd, przed i po migracji, test osoby, która odchodzi).
- Konsola przeglądarki przy zrzutach: 0 błędów.

## Ochrona zmian redaktorów

Bazy zanotowane rano (HEAD = `origin/main` przy starcie pracy): Web-Pracownicy `ff4aec1`, Web-Instytut `e88a088`, Web-Nauka `51626f2`, Web-Studia `e7e297e`, seminaria: AH `e25b641`, Dydaktyka `b3d6e7f`, DAH `81716a7`, Geometria `1700d8a`, Prawdopodobieństwo `15169e5`, Równania `ba24c65`, Statystyka `699c086`, Teoria Modeli `5a96f65`, Topologia `1cf30da`.

1. **Świeży main:** tuż przed każdym pushem `git fetch` i `git log <baza>..origin/main`: **0 zapisów w każdym z 13 repozytoriów**, więc migracja z rana była na aktualnych plikach (skrypt odmawia na przerobionych; na świeżym main daje ten sam wynik). Rozwiązywania konfliktów nie było.
2. **Cisza:** ostatni zapis redaktora (commit spoza zleceń) — Web-Pracownicy 16.11 20:46, Web-Instytut 18.11 23:41, Web-Nauka 13.11 12:41, Web-Studia 10.11 10:58, seminaria 09.11 00:47. Wszędzie starszy niż 20 min, bez czekania.
3. **Kontrola przed pushem** (`tresci-C/z42-kontrola.py <repo> origin/main praca/42-osoby`, wyniki `tresci-C/z42-kontrola-przed2-<repo>.txt`): dla każdego pliku danych wersja wypychana = wersja z main przerobiona regułami migracji. `.pages.yml` = wynik generatora na wersji z main, katalog = 4 pola bez kontaktów, poza tym dozwolony tylko plik automatu (Web-Pracownicy) i zdanie w README (Web-Studia). **OK w 13/13.**
4. **Kontrola po pushu** (to samo narzędzie, stary main → nowy main, wyniki `tresci-C/z42-kontrola-po-<repo>.txt`): **OK w 13/13**, różnice tylko w polach osób:
   - Web-Pracownicy: `pracuje` ×128 (+ `.pages.yml`, plik automatu);
   - Web-Instytut: `karta.kierownik` → `karta.kierownik_ze_spisu` ×9; dyrekcja `osoby[].imie_nazwisko` → `osoby[].osoba` ×5; Wydział `imie_nazwisko` → `osoba` ×2 i `email` → `inne` ×2; `sekretariat.osoby` → `sekretariat.osoby_ze_spisu`;
   - Web-Nauka: `kierownik` ×94 → `kierownik_ze_spisu` ×80 plików / `kierownik_spoza` ×14 plików;
   - seminaria: `prowadzacy` → `prowadzacy_ze_spisu` (9) i `prowadzacy_spoza` (AH, Topologia);
   - Web-Studia: brak zmian w danych (formularz, README, katalog).
   - W Web-Studia skrypt po pushu za pierwszym razem przerwał się na błędzie Windows („Filename too long” przy `git show <pełny sha>:<długa ścieżka PDF>`). Zmieniłem odczyt na `git cat-file blob` (ta sama treść) i powtórzyłem kontrolę: OK. To błąd narzędzia, nie niezgodność.
5. **Odwracalność:** każdy push to jeden commit na repozytorium. W razie potrzeby można go cofnąć `git revert` bez ruszania zapisów redaktorów. Nie było potrzeby.

## Zrzuty (`raport-zrzuty/`)

- Test osoby, która odchodzi: `z42-test-zaklad-podglad-1440.png`, `z42-test-zaklad-podglad-en-1440.png`, `z42-test-zaklad-podglad-390.png`, `z42-test-zaklad-podglad-plakietka-1440.png`, `z42-test-zaklad-publiczna-1440.png`, `z42-test-seminarium-podglad-1440.png`, `z42-test-seminarium-plakietka-390.png`, `z42-test-lista-zakladow-podglad-1440.png`, `z42-test-grant-podglad-1440.png`, `z42-test-grant-publiczna-1440.png`, `z42-test-specjalnosc-podglad-1440.png`.
- Po migracji: `z42-po-wladze-1440.png` (cała strona władz), `z42-po-wladze-ciemny-1440.png`.
- Konsola przeglądarki: 0 błędów.

## PDF-y dla redaktorów — lista zmian (do następnego generowania; nie generowałem)

- `Mapa-CMS-IM-UWr.pdf` (Web-Podglad `dla-redaktorow/`), kafelek „Pracownicy”: dopisać „Pracuje w Instytucie — po odejściu odznacz, nie usuwaj (usuwanie wyłączone)”. Przy Nauce (granty), Instytucie (zakłady, władze) i seminariach: „osoby wybierasz z listy (wpisz nazwisko); ręcznie tylko osoby spoza Instytutu”.
- `dok/mapa-redakcyjna-IM-UWr.pdf`, punkt `:::opiekun`: „Osoby wybierz w formularzu” zostaje; dopisać, że lista to wspólny katalog ze spisu pracowników, odświeżany automatycznie (albo skryptem do czasu ustawienia kluczy). Zdanie „Nie zmieniaj ID plików pracowników” zostaje.
- `Czat-AI-formatowanie-tresci.pdf`: bez zmian (przykład „Sekretariat” dotyczy formatowania tekstu).

## Osoby, które mogły odejść (do decyzji właściciela; nikogo nie odznaczyłem)

Grupa „emeryt” w spisie, 23 osoby: Agata Hoffmann, Alexander Bendikov, Andrzej Dąbrowski, Andrzej Krzywicki, Bogusław Hajduk, Bolesław Kopociński, Danuta Zaremba, Janusz Pawlikowski, Jurij Kryakin, Kazimierz Musiał, Krzysztof Tabisz, Małgorzata Romanowska-Majsnerowska, Marek Bożejko, Roman Duda, Ryszard Szekli, Ryszard Szwarc, Stanisław Miklos, Tomasz Rolski, Wiesław Krakowiak, Władysław Narkiewicz, Władysław Szczotka, Zbigniew J. Jurek, Zofia Diaków.

Uwaga: odznaczenie „Pracuje w Instytucie” usuwa osobę ze spisu pracowników także z grupy „Emeryci”. Jeśli emeryci mają zostać na liście, zostaw ich zaznaczonych; odznaczaj tylko osoby, które naprawdę nie mają już być w spisie. Byli kierownicy grantów z tej grupy (np. Bożejko, Rolski, Jurek) i tak zostaną przy grantach jako tekst.

## Kryteria odbioru

- [x] Wybór osoby z listy we wszystkich polach „wybór” z tabeli. Osoba spoza spisu wpisywana ręcznie przy grantach, seminariach i władzach Wydziału. Pola tekstowe (wykonawcy, recenzenci) bez zmian. Lista aktualizuje się skryptem; automat jest gotowy i czeka na klucze.
- [x] Osoba, która odeszła: znika ze spisu, w historii zostaje tekstem bez linku, przy funkcji Podgląd pokazuje znacznik, a strona publiczna ukrywa wiersz (test lokalny, zrzuty).
- [x] Pliku osoby nie da się usunąć w CMS (`delete: false`). Katalog nie kasuje osób, do których są odwołania.
- [x] Migracja przeniosła wszystkie wartości (115 do spisu, 19 spoza, 128 × `pracuje`). Wygląd bez zmian poza zgłoszonymi 24 plikami.
- [ ] Kontrola zmian redaktorów przed i po pushu: zrobiona (13/13 OK). **Przegląd z następnego dnia: do zrobienia 20.11** (skrypt gotowy).

## Decyzje domyślne (do zmiany na prośbę właściciela)

- Nazwy pól: `…_ze_spisu` / `…_spoza`, w władzach `osoba` + grupa `inne` (e-mail, pokój, stopień, strona), sekretariat `osoby_ze_spisu`. Wartość pola „ze spisu” = ścieżka pliku katalogu (`_cms/pracownicy/<id>.yml`), jak w Studiach.
- Stare pola tekstowe dalej czytane przez stronę (formularz otwarty przed pushem i zapisany po nim nie psuje strony).
- Kolumny widoku listy w CMS (granty, zakłady) pokazują pole „ze spisu” — Pages CMS pokaże tam ścieżkę pliku katalogu, nie imię. Jeśli to przeszkadza, usunąć je z `view.fields`.
- Brak sortowania listy wyboru (Pages CMS nie pozwala); byli pracownicy z dopiskiem w etykiecie.
- Automat wyłączony zmienną `KATALOG_PRACOWNIKOW` do czasu ustawienia kluczy.
- Usuwanie osób w CMS wyłączone (`operations.delete: false`), pole `data_odejscia` dodane (opcjonalne).
- Kierownicy grantów ze spisu wyświetlani z aktualnym tytułem i pełnym imieniem ze spisu (np. „J. Gogolok” → „Dr Jakub Gogolok”) — zgodnie z etapem 5 („aktualne imię, nazwisko i tytuł ze spisu”); historyczny tytuł z czasu grantu znika.
- Opis pola „spoza spisu” z przykładem „recenzent z innej uczelni” dokładnie jak w zleceniu, choć pole jest przy grantach i seminariach.
- Usunięty z katalogu Web-Studia nieaktualny plik duplikatu (bez odwołań).

## Przegląd zapisów redaktorów 24 h po pushu

**Do zrobienia jutro (20.11, od 14:16)**, bo dziś nie da się go zrobić (kryterium odbioru zostaje otwarte). Narzędzie: `sh ../tresci-C/przeglad-24h.sh` (Git Bash, w folderze Web-Core). Skrypt tylko czyta. Dla każdego repozytorium wypisuje zapisy redaktorów po pushu i „podejrzane” linie, czyli przywrócone stare pola (`kierownik`, `prowadzacy`, `imie_nazwisko`, `sekretariat.osoby`) albo zniknięte nowe (`…_ze_spisu`, `…_spoza`, `osoba`, `inne`, `pracuje`). Tak wygląda zapis z karty CMS otwartej przed pushem.

Stan w chwili pisania (14:20): 0 zapisów we wszystkich repozytoriach. Gdyby coś się znalazło: strona i tak to pokaże (stare pola dalej działają), a poprawka to osobny commit z wartością „ze spisu” z historii.
