# Raport — zlecenie 41: szybszy Podgląd i przebudowa po pushu kodu

**Status: zrobione i wypchnięte 18.11.2026 (00:30–00:48 UTC), w trybie samodzielnym.** Spełnione były wszystkie warunki pushu. Przed każdym pushem: `fetch` i `rebase`, bez force.

## Commity

| Repozytorium | Commit | Treść |
|---|---|---|
| Web-Podglad | `51c4b95` | `podglad.yml`: pamięć npm i zdjęć, płytkie klony równolegle, nowa budowa przerywa starą; usunięty TEST telefonu i `testy/telefon-TEST.patch`; README |
| Web-Podglad | `f11ae37` | `actions/cache` v5 (Node 24) zamiast v4 |
| Web-Core | `4511613b` | `podglad-przekaznik.yml`: push na `main` wysyła „przebuduj” (filtr ścieżek) |
| Web-Instytut | `0855f0d`, `7ed4d89`, `d720e38`, `311faae` | test serii zapisów: tymczasowa strona `test-zlecenie-41`, utworzona, dwa razy zmieniona i usunięta; różnica netto zerowa |

## Etap 0. Pomiar przed zmianą
Źródło: 10 ostatnich udanych przebiegów (17.11, 20:43 – 18.11, 00:09 UTC), API `actions/runs/…/jobs` i logi.

| Krok (zadanie `build`) | Mediana [s] | Zakres [s] |
|---|---:|---:|
| Kod strony (checkout Web-Core) | 8,5 | 1–12 |
| Łatki testowe (checkout `testy/`) | 1 | 0–2 |
| Treści z 16 repozytoriów (kolejno, `--filter=blob:none`) | 15 | 8–17 |
| Instalacja zależności (`npm install`, bez pamięci) | 7 | 4–7 |
| **Budowanie strony** (`astro build` + `pagefind`) | **235** | 175–275 |
| TEST telefonu | 0 | 0 |
| Poprzednia wersja (`_astro` z `zbudowana`) | 2 | 2–4 |
| Kopia na `zbudowana` | 9 | 7–16 |
| `upload-pages-artifact` | 9 | 8–18 |
| Zadanie `deploy` | 11 | 8–17 |
| **Całe zadanie `build`** | **294,5** | 234–337 |
| Od startu budowy do końca publikacji | 314 | 250–352 |

Co dzieje się w kroku „Budowanie strony” (5 przebiegów z pełnymi logami):

| Faza | Czas |
|---|---|
| `astro build` łącznie | 173–273 s (757 stron) |
| **generating optimized images** | **156–249 s**, 3021–3060 zdjęć, wszystkie optymalizowane od nowa |
| suma czasów pojedynczych optymalizacji (`+…s` w logu, idą równolegle) | 585–932 s |
| generating static routes | 10–14 s |
| collecting / static entrypoints | 2–3 s / 5 s |
| `pagefind` | 0,9–1,1 s |

**Wniosek:** ok. 90% czasu to optymalizacja zdjęć bez pamięci podręcznej. Lokalnie, z pamięcią w `node_modules/.astro`, ta sama budowa trwa 30 s.

Krok „TEST telefonu” od 9.11 kończył się po 0 s, bo łatka się nie nakładała (`patch failed: src/components/Naglowek.astro`), a `/test-telefon/` już wcześniej zwracał 404. W praktyce nie było więc drugiej budowy.

## Etap 1. Szybsza budowa (`Web-Podglad/.github/workflows/podglad.yml`)
1. **TEST telefonu: krok i łatka usunięte.** Przyjąłem usunięcie, bo w zleceniu to wartość domyślna, a właściciel potwierdził ją w poleceniu trybu samodzielnego. Usunąłem też checkout `testy/` i kopiowanie `test-telefon/_astro`. README nie wspomina już o teście.
2. **Zależności:** `actions/setup-node@v5` z `cache: npm` oraz `npm ci`. `package-lock.json` jest zgodny z `package.json` (sprawdzone `npm ci` lokalnie) i ma pakiety linuksowe: rollup, sharp, esbuild, pagefind.
3. **Zdjęcia:** pamięć `node_modules/.astro/assets`, bo `astro.config.mjs` nie ustawia `cacheDir` (Astro 5.18.2).
   - Odtwarzam ją **po** `npm ci`, które usuwa `node_modules`. Pamięć npm (`~/.npm`) jej więc nie nadpisze.
   - Nazwa pliku w pamięci to nazwa pliku wynikowego `_astro`: zawiera skrót zdjęcia i parametrów. Sprawdziłem lokalnie: 3060 z 3060 plików pamięci jest w `dist/_astro`. Zmienione zdjęcie zawsze optymalizuje się więc od nowa.
   - **Klucz:** `zdjecia-astro-<wersja Astro>-<skrót plików zdjęć z src/>-<skrót listy plików w pamięci>`. `restore-keys` szukają najpierw tych samych zdjęć, potem tej samej wersji Astro.
   - Po budowie w pamięci zostają tylko pliki użyte w tej budowie (porządki). Zapis następuje tylko wtedy, gdy zestaw plików się zmienił.
   - *Odstępstwo:* do klucza ze zlecenia (wersja Astro + skrót zdjęć) dodałem skrót listy plików. Bez niego nowe rozmiary z kodu (te same zdjęcia, inne parametry) nie trafiałyby do pamięci, aż do zmiany jakiegoś zdjęcia.
   - Pamięć waży ok. 42 MB (3066 plików).
4. **Treści:** sprawdziłem, że budowa nie czyta historii repozytoriów treści. `pobierz_tresci.py --lokalnie` tylko kopiuje pliki, a w `src/` nie ma odwołań do gita ani do dat plików.
   - Przy `main`: klony `--depth=1`, 8 naraz (`xargs -P 8`). Log pokazuje teraz SHA każdego repozytorium.
   - Przy gałęzi podanej ręcznie: jak dotąd `--filter=blob:none`, bo scalenie z `main` potrzebuje historii.
   - Sprawdzone lokalnie:
     - 16 klonów = `main` z GitHuba (SHA zgodne z `ls-remote`), głębokość 1;
     - błąd klonu przerywa krok;
     - nieistniejąca gałąź daje „main” z pełną historią.
5. **Checkout Web-Core:** zlecenie 38 jest zrobione, `sparse-checkout` niepotrzebny. Checkout trwa teraz 1–2 s zamiast 8,5 s.
6. **Seria zapisów: wybrałem przerywanie budowy w toku.** Grupa `podglad-budowa` z `cancel-in-progress: true` dotyczy tylko zadania `build`. Publikacja ma grupę `pages` bez przerywania, a poziom całego workflow nie ma już `concurrency`.
   - Dlaczego nie wstrzymanie w przekaźniku: po zmianie budowa trwa ok. 1 min, a 60 s czekania dokładałoby minutę do *każdego* zapisu.
   - Nowe uruchomienie i tak pobiera najnowsze treści, więc nic nie przepada.
   - Przerwany przebieg ma stan `cancelled`.
   - Ograniczenie: przebieg może zostać przerwany w ostatnich ok. 20 s budowy, już po nadpisaniu `zbudowana`, ale przed publikacją. Wtedy następna budowa weźmie „poprzednie” pliki `_astro` z tej nieopublikowanej wersji. Skutek: strona zapamiętana w przeglądarce sprzed obu budów może raz wczytać się bez stylów i po odświeżeniu wraca do normy. Zdarza się to rzadko i niczego nie psuje trwale.
7. **Bez zmian:** `pagefind`, kopia na `zbudowana`, pliki `_astro` z poprzedniej wersji, publikacja.
8. **Poza zleceniem:** `actions/cache/restore|save@v5` (Node 24) zamiast v4. Przy v4 GitHub ostrzegał o wycofywanym Node 20. Pamięć zapisana przez v4 została odczytana przez v5.

## Etap 2. Przebudowa po pushu kodu (`Web-Core/.github/workflows/podglad-przekaznik.yml`)
- Dodany wyzwalacz `push` na `main` z filtrem `paths`. Kolejność wzorców ma znaczenie: `**`, `!**/*.md`, `src/**/*.md`, `!dok/**`, `!.github/**`, `.github/workflows/podglad-przekaznik.yml`.
- Filtr sprawdziłem na przykładach (picomatch, ta sama semantyka):
  - `README.md`, `dok/…`, `.github/workflows/deploy.yml`, `.github/qa/…` → bez przebudowy;
  - przekaźnik, `src/**/README.md`, `astro.config.mjs`, `skrypty/…`, `README.md` razem z `src/…` → przebudowa.
- Klucz: `POWIADOM_APP_ID` i `POWIADOM_KLUCZ` są na poziomie organizacji i widoczne dla Web-Core (API `organization-secrets`). Działają przy zdarzeniu `push`: przebieg [44209855615](https://github.com/IM-UWr/Web-Core/actions/runs/44209855615) zakończył się sukcesem i wysłał `przebuduj (IM-UWr/Web-Core)`.
- Nagłówki zaktualizowane w przekaźniku i w `podglad.yml` („Po zmianie treści, planu zajęć albo kodu…”).
- `deploy.yml` nadal wyłączony (`disabled_manually`) i nie uruchomił się po pushu.

## Odbiór

### Czas: mediana 3 przebiegów przed i po

| | Przed (3 ostatnie: 335, 239, 323 s) | Po (62, 56, 61 s) |
|---|---:|---:|
| Zadanie `build` | **323 s** | **61 s** |
| Od startu budowy do końca publikacji | 340 s | 77 s |

Dla wszystkich pomiarów: przed mediana 294,5 s z 10 przebiegów, po 58,5 s z 4 przebiegów (62, 56, 61, 47).

Pierwsza budowa po wdrożeniu, z pustą pamięcią zdjęć, trwała 317 s ([44208358961](https://github.com/IM-UWr/Web-Podglad/actions/runs/44208358961)). Tak będzie po każdej zmianie wersji Astro.

| Krok po zmianie | Mediana [s] | Zakres [s] | Przed [s] |
|---|---:|---:|---:|
| Kod strony | 1,5 | 1–2 | 8,5 |
| Treści (16 repozytoriów) | 2 | 2–3 | 15 |
| setup-node + pamięć npm | 1,5 | 1–2 | 0,5 |
| Instalacja zależności (`npm ci`) | 4,5 | 3–6 | 7 |
| Pamięć zdjęć: odtworzenie | 1 | 1–2 | — |
| **Budowanie strony** | **23** | 16–26 | **235** |
| Poprzednia wersja | 2,5 | 2–3 | 2 |
| Kopia na `zbudowana` | 8,5 | 8–9 | 9 |
| `upload-pages-artifact` | 8,5 | 6–9 | 9 |
| Publikacja (`deploy`) | 7 | 6–17 | 7 |

Faza „generating optimized images” trwa teraz 0,5–0,6 s zamiast 156–249 s.

### Pamięć podręczna działa
Przebieg [44209269623](https://github.com/IM-UWr/Web-Podglad/actions/runs/44209269623), druga budowa po wdrożeniu:
- npm: `Cache hit for: node-cache-Linux-x64-npm-6b40…`;
- zdjęcia: `Cache hit for restore-key: zdjecia-astro-5.18.2-0995f26744e93081-72232d76caac1d16`;
- komunikaty przebiegu: „z pamięci 3066, zoptymalizowane od nowa 0” oraz „Pamięć zdjęć: 3066 plików, 50M; usunięte nieużywane: 0”;
- zapis pamięci pominięty, bo zestaw plików bez zmian.

Klony treści trwają 2–3 s zamiast 15 s.

### Wynik identyczny
Porównanie gałęzi `zbudowana`: `80c6c7c` (ostatnia budowa starym workflow, 00:25) z `6c4251b` (druga nowa) i z `276f7c5` (ostatnia, po teście serii). Normalizacja w skrypcie porównującym:
- **HTML: 0 różnic.** CSS, JS i obrazy też bez różnic, także zdjęcia wzięte z pamięci (bajt w bajt).
- 110 plików `.ics`: różni się tylko `DTSTAMP`. W `seminaria/powiadomienia.json` tylko `wygenerowano`.
- `sitemap.xml`: te same wpisy, inna kolejność. Ta kolejność zmieniała się też między starymi budowami: w 40 wersjach `zbudowana` z 13–18.11 pozycja „siad/matematyka” odwróciła się 6 razy.

Pierwsza nowa budowa `e139c13` miała dodatkowo odwróconą kolejność dwóch konferencji o tej samej dacie początku (11.09.2016: „Stochastic models V” i „Mathematics of pattern formation”). Dotyczy to kalendarza i listy konferencji (PL/EN, oba `.ics`) oraz zależnego od nich indeksu pagefind. Następna nowa budowa wróciła do dawnej kolejności. Ta sama zamiana zdarzyła się 13.11 jeszcze ze starym workflow (`4935206`). To niedeterministyczne rozstrzyganie remisu w sortowaniu, niezależne od tego zlecenia (pytanie 1).

### Seria zapisów w CMS
- Trzy zapisy tymczasowej strony `src/content/strony/test-zlecenie-41.md` w Web-Instytut: 00:43:35, 00:43:59 i 00:44:23 UTC (zwykłe commity na `main`, tą samą drogą co zapis z CMS: `powiadom.yml` → przekaźnik → Podgląd).
- 3 powiadomienia i 3 przekaźniki zakończone sukcesem. **3 przebiegi Podglądu, w tym tylko jedna pełna budowa:**
  - [44210218415](https://github.com/IM-UWr/Web-Podglad/actions/runs/44210218415): budowa przerwana po 34 s (`cancelled`), publikacja pominięta;
  - [44210266959](https://github.com/IM-UWr/Web-Podglad/actions/runs/44210266959): budowa przerwana po 7 s (`cancelled`);
  - [44210315065](https://github.com/IM-UWr/Web-Podglad/actions/runs/44210315065): sukces. Strona pokazywała „Test zlecenia 41 — zapis 3 z 3” o 00:46:08, czyli **1 min 45 s po ostatnim zapisie**. Ten sam tekst był na gałęzi `zbudowana`.
- Wcześniej (np. 17.11, 20:43–20:50) seria zapisów dawała pełne budowy po ok. 5 min, jedna po drugiej. Ostatni zapis był widoczny nawet po ok. 10 min.
- Usunięcie strony (00:46:40) → przebudowa [44210645295](https://github.com/IM-UWr/Web-Podglad/actions/runs/44210645295) → `/test-zlecenie-41/` i `/en/test-zlecenie-41/` zwracają 404.
- **Ochrona zmian redaktorów:**
  - przed każdym pushem: `fetch` i `rebase`, a wypychana różnica względem `origin/main` dotyczyła tylko pliku testowego (kontrola w skrypcie, inaczej STOP);
  - po każdym pushu sprawdziłem to samo;
  - od bazy `3f9689a` na `main` Web-Instytut są tylko moje 4 commity, a różnica netto jest zerowa;
  - żaden zapis redaktora nie przyszedł w trakcie testu, więc żaden nie mógł zginąć.
  - Narzędzia `kontrola_redaktorow.py` z 31 nie uruchomiłem: wymaga PyYAML, którego tu nie ma, a dla jednego własnego pliku powyższa kontrola jest ostrzejsza.

### Push kodu
Push `4511613b` na `main` Web-Core, czyli samo to zlecenie, uruchomił przekaźnik ([44209855615](https://github.com/IM-UWr/Web-Core/actions/runs/44209855615), zdarzenie `push`). Ten wywołał budowę Podglądu [44209875462](https://github.com/IM-UWr/Web-Podglad/actions/runs/44209875462) („przebuduj IM-UWr/Web-Core”, sukces, 56 s).

## Kryteria odbioru
- [x] Budowa Podglądu wyraźnie krótsza: zadanie `build` 323 → 61 s (mediana z 3), od startu do publikacji 340 → 77 s; wynik bez zmian (wyżej).
- [x] Pamięć podręczna npm i zdjęć działa (trafienia w logu); treści klonowane w 2–3 s zamiast 15 s.
- [x] Seria zapisów nie robi kolejki pełnych budów: 3 zapisy → 2 przerwane i 1 pełna budowa. Ostatnia zmiana była widoczna.
- [x] Push kodu do `main` Web-Core sam przebudowuje Podgląd.
- [x] TEST telefonu usunięty (wartość domyślna).

## Dla zlecenia 33 (druga sesja)
- `podglad.yml` nie ma już `concurrency` na poziomie workflow:
  - zadanie `build` ma grupę `podglad-budowa` (`cancel-in-progress: true`);
  - `deploy` ma grupę `pages` (bez przerywania).
- Przerwana budowa: przebieg `cancelled`, `deploy` `skipped`.
- Zmienne `PODGLAD=1` i `PODGLAD_RUN_ID` najlepiej dodać w kroku „Budowanie strony”. Jego `run` używa teraz `npm run build | tee "$RUNNER_TEMP/budowa.log"`.

## Pytania do właściciela
1. **Stała kolejność wyników budowy.** Dwie konferencje z tą samą datą początku oraz wpisy w `sitemap.xml` mogą zmieniać kolejność między budowami. Proponuję drugi klucz sortowania (np. identyfikator wpisu) w sortowaniu konferencji i wydarzeń kalendarza oraz w `sitemap.xml.ts`. Strona przestanie się wtedy zmieniać „sama z siebie”, a porównania `zbudowana` będą czyste. Nie wdrażałem, bo to zmiana wyglądu listy poza zleceniem.
2. `actions/configure-pages@v5`, `actions/upload-pages-artifact@v4` i `actions/deploy-pages@v4` wciąż dają ostrzeżenie o Node 20. Działają, ale GitHub w końcu je wyłączy. Czy podnieść je do nowszych wersji osobnym, małym zleceniem?

## Do sprawdzenia następnego dnia
- Pierwsze zapisy redaktorów w CMS: przebieg Podglądu powinien kończyć się po ok. 1–1,5 min. Przy kilku zapisach z rzędu część przebiegów będzie `cancelled` i tak ma być.
- Przebiegi z `cron` (co godzinę) przechodzą.
- Lokalnie, w `tresci-B/Web-Podglad` i `tresci-B/Web-Instytut`, zostały gałęzie robocze `praca/41-*`. Nie są wypchnięte, a ich zmiany są na `main`.
