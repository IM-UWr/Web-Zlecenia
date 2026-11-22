# Zlecenie 41: szybsza budowa Podglądu i przebudowa po pushu kodu (punkty 8 i 9 kolejki) (17.11.2026)

**Decyzje właściciela:**
- Kolejka, punkty 8 i 9 (7.11).
- 17.11, 22:45: „to jest ważne”.

**Do potwierdzenia przez właściciela przed pushem:** usunięcie podglądu „TEST telefonu” (`/test-telefon/`), punkt 1 etapu 1. Domyślnie: usuwamy.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`.
- Zmiany w workflowach Web-Podglad i Web-Core tylko po „push”.
- Najlepiej po zleceniu 38 (porządki): bez `raport-zrzuty/` katalog roboczy Web-Core jest o 164 MB mniejszy.
- **Przed zleceniem 33** (część B, plakietka stanu budowy), bo oba zmieniają `podglad.yml`:
  - budowa anulowana ma stan `cancelled`, a plakietka z 33 ma go pokazywać spokojnie;
  - zmienne `PODGLAD=1` i `PODGLAD_RUN_ID` doda zlecenie 33.
- Raport `RAPORT-ZLECENIE-41.md`. Bez subagentów.

## Stan dziś (`Web-Podglad/.github/workflows/podglad.yml`, 152 linie)

**Kroki budowy:**
1. Checkout Web-Core (cały katalog roboczy).
2. Klon 16 repozytoriów treści z `tresci.json` (`--filter=blob:none`, po kolei), potem `pobierz_tresci.py --lokalnie`.
3. `npm install` bez pamięci podręcznej.
4. `npm run build`, czyli `astro build` + `pagefind`.
5. **Druga pełna budowa „TEST telefonu”:** łatka `testy/telefon-TEST.patch`, wynik pod `/test-telefon/`, `continue-on-error`. Opis w pliku: „próbna wersja na telefon, NIE WZOROWAĆ SIĘ”.
6. Kopia na gałąź `zbudowana`, pliki `_astro` z poprzedniej wersji, publikacja (`deploy-pages`).

**Czas:** ok. 5,5 min (pomiar z 7.11).

**Wyzwalacze:**
- ręcznie;
- `repository_dispatch` (`tresc-zmieniona`, `przebuduj`) przez `Web-Core/.github/workflows/podglad-przekaznik.yml` (klucz aplikacji `POWIADOM_APP_ID` / `POWIADOM_KLUCZ`);
- `cron` co godzinę o :23 (w praktyce GitHub uruchamia go rzadziej);
- push w Web-Podglad.

**Push kodu do `main` Web-Core nie przebudowuje Podglądu.** Dziś trzeba ręcznie: Actions → „Przekaźnik do Web-Podglad” → Run workflow.

**Kolejka:** `concurrency: pages`, `cancel-in-progress: false`. Seria zapisów w CMS daje serię pełnych budów, jedna po drugiej.

## Etap 0. Pomiar
- Czasy kroków z 5–10 ostatnich udanych przebiegów (`gh run view --log` albo API z tokenem właściciela na jego komputerze).
- Tabela w raporcie: ile trwa każdy krok, w tym osobno `astro build` (zdjęcia) i `pagefind`.
- Jeśli `astro build` wypisuje czasy optymalizacji zdjęć, podaj ich sumę.

## Etap 1. Szybsza budowa
1. **TEST telefonu** (do potwierdzenia):
   - usuń krok i łatkę `testy/telefon-TEST.patch`; `/test-telefon/` zniknie;
   - wersja telefonowa jest od dawna na głównym Podglądzie, a ten krok to druga pełna budowa;
   - jeśli właściciel chce zachować podgląd: budowa tylko ręcznie (wejście `workflow_dispatch` „z testem telefonu”).
2. **Zależności:** `actions/setup-node` z `cache: npm` oraz `npm ci`.
3. **Zdjęcia:** pamięć podręczna optymalizacji zdjęć Astro między budowami.
   - `actions/cache` na katalog pamięci Astro. Domyślnie to `node_modules/.astro`, bo `astro.config.mjs` nie ustawia `cacheDir`; sprawdź.
   - Klucz z wersji Astro i skrótu plików zdjęć; `restore-keys` na częściowe trafienie.
   - Pamięć `node_modules` z kroku 2 nie może nadpisać tego katalogu. Ustaw kolejność albo osobny `cacheDir` poza `node_modules`.
4. **Treści:**
   - klonowanie `--depth 1` zamiast `--filter=blob:none`, jeśli budowa nie korzysta z historii repozytoriów treści. Sprawdź `pobierz_tresci.py` i kod, np. czy nie czyta dat z gita;
   - klonowanie równoległe (np. `xargs -P 8`), z tym samym wynikiem i obsługą gałęzi podanej ręcznie.
5. **Checkout Web-Core:** jeśli zlecenie 38 nie jest jeszcze zrobione, `sparse-checkout` bez `raport-zrzuty/`.
6. **Seria zapisów w CMS.** Zaproponuj (na podstawie pomiaru) i wdroż jedno z dwóch:
   - nowe zdarzenie treści anuluje budowę w toku (`cancel-in-progress` tylko dla zadania `build`, publikacja nigdy nie jest przerywana);
   - albo krótkie wstrzymanie w przekaźniku (np. 60 s), żeby kilka zapisów dało jedną budowę.

   Wynik ma być taki, że ostatni zapis redaktora jest widoczny jak najszybciej, a żadna zmiana nie przepada.
7. Bez zmian: `pagefind`, kopia na `zbudowana`, pliki `_astro` z poprzedniej wersji, publikacja.

## Etap 2. Przebudowa po pushu kodu (punkt 9)
- W `Web-Core/.github/workflows/podglad-przekaznik.yml` dodaj wyzwalacz `push` na `main`.
  - Pomijaj zmiany tylko w `**/*.md` poza `src/`, w `dok/**` i w `.github/**` poza samym przekaźnikiem.
  - Przekaźnik wysyła `przebuduj` z tym samym kluczem aplikacji.
- Sprawdź, że klucz (`secrets.POWIADOM_KLUCZ`) jest dostępny przy zdarzeniu `push`.
- Opis w nagłówku przekaźnika i w `podglad.yml` (komentarz „Po zmianie treści…”).
- Uwaga: `deploy.yml` też reaguje na push do `main`, ale jest wyłączony i **zostaje wyłączony**.

## Odbiór
- **Czas:** mediana 3 przebiegów przed i po, tabela kroków.
- **Wynik identyczny:** zawartość gałęzi `zbudowana` przed i po bez różnic w HTML, poza znacznikami czasu i nazwami plików `_astro`.
- **Druga budowa z rzędu:** szybsza dzięki pamięci podręcznej. W logu widać trafienie w cache npm i zdjęć.
- **Seria zapisów:** 3 zapisy w CMS w ciągu minuty (testowy wpis, potem usunięty) kończą się stroną z ostatnią zmianą. Opisz, ile było budów.
- **Push kodu:** pierwszy push po wdrożeniu (np. samo to zlecenie) uruchamia przebudowę Podglądu.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Budowa Podglądu wyraźnie krótsza (pomiar przed i po w raporcie), wynik bez zmian.
- [ ] Pamięć podręczna npm i zdjęć działa; treści klonowane szybciej.
- [ ] Seria zapisów nie robi kolejki pełnych budów, a ostatnia zmiana jest zawsze widoczna.
- [ ] Push kodu do `main` Web-Core sam przebudowuje Podgląd.
- [ ] TEST telefonu usunięty albo tylko na żądanie, według decyzji właściciela.
