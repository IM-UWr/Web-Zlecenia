# Zlecenie 38 — porządki: gałęzie (etap 1) — raport

Raport lokalny (nie trafia na `main`). Praca w worktree `Web-Core-B`, lokalna gałąź `praca/38-porzadki`.
Klony repozytoriów: `C:\Users\Szymek\Documents\GitHub\tresci-B`. Plan zrobiony 18.11.2026, ok. 00:30.

## Etap 1 — STOP: czekam na „push”

**Na GitHubie nic jeszcze nie zmieniłem.** Brak nowych znaczników, nic nie usunięte, nic nie wypchnięte.

### Podsumowanie
- **23 repozytoria organizacji** (bez `.github`, które jest puste). Tylko `main` mają już: Web-Aktualnosci, Web-Instytut, Web-Nauka, Web-Popularyzacja i Web-Studia. Pozostałe **18 repozytoriów ma razem 92 gałęzie** do archiwizacji (w Web-Podglad nie liczę `zbudowana`).
- Ocena gałęzi:
  - **47: cała historia jest w `main`** (0 commitów spoza `main`);
  - **1: zmiany są w `main` pod innym SHA** (`agent-naglowek-podglad` w Web-Core; `git cherry` pokazuje „−”);
  - **44: mają COMMITY SPOZA MAIN**, w tabelach pogrubione. Zgodnie z zasadą z 13.11 ich nie scalam, tylko archiwizuję. Co to za gałęzie, opisuję niżej.
- **Znaczniki:**
  - 91 do utworzenia;
  - 1 już istnieje i wskazuje ten sam commit: `archiwum/wyglad/zlecenie-16` w Web-Sem-Rownania-Rozniczkowe. Tam wystarczy usunąć gałąź.
  - **Żadna nazwa nie koliduje** ze znacznikiem wskazującym inny commit, więc przyrostek `-2` nie jest nigdzie potrzebny.
- **18 otwartych PR** (gałęzie `cms-reorganizacja-2026-11`: #2 w Web-Core, #1 w 17 pozostałych repozytoriach). Po usunięciu gałęzi GitHub sam je zamknie. Tak ma być według decyzji z 13.11, ale piszę o tym, żeby nie było zaskoczenia.
- Uwaga do opisu stanu w zleceniu: znaczniki `archiwum/kopia/2026-11-06` i `archiwum/wyglad/zlecenie-16` mają już Aktualnosci, Instytut, Nauka, Popularyzacja i 6 seminariów. Topologia, Teoria Modeli i Statystyka **jeszcze ich nie mają**, więc dostaną je teraz.

### Gałęzie z commitami spoza `main` — co to jest
- **Web-Core (24):**
  - Warianty pierwszej wersji (archiwizowane zgodnie z decyzją z 7.11):
    - `wariant-portal`, `wariant-redakcyjna` i `wariant-zwarta` wskazują **te same commity** co `agent-naglowek-portal-podglad`, `-redakcyjna-podglad` i `-zwarta-podglad` (2–4 commity). Ten sam commit dostanie więc dwa znaczniki.
    - `agent-wariant-{portal,redakcyjna,zwarta}-podglad`: 1–3 commity.
  - `podglad-agent-*` (12): gałęzie bez wspólnej historii z `main`. Każda ma 1 commit bota z gotową, zbudowaną stroną (z 29–31.10).
  - `kopia/2026-11-01-estetyka-prototypy`: osobna historia, 140 commitów. Są w niej prototypy, notatki estetyki i plan wdrożenia z 1–6.11; m.in. `dok/en/RAPORT-EN.md`, na który wskazuje `dok/en/POSTEP.md`.
  - `kopia/2026-11-06-nakladka-i-niezacommitowane`: osobna historia, 1 commit z kopią nakładki treści (`tar.gz`) i łatką niezacommitowanych zmian z 6.11.
  - `cms-reorganizacja-2026-11`: 2 commity z raportem; otwarty PR #2.
- **Pozostałe repozytoria (20):**
  - `cms-reorganizacja-2026-11` w 17 repozytoriach: po 1 commicie z 8.11 i otwartym PR #1;
  - `test-cms` w Web-Sem-Topologia i Web-Spec-Aktuarialno-Finansowa: po 1 zapisie z Pages CMS z 6.11;
  - `kopia/test-cms-zlecenie-22` w Web-Ustawienia: 2 zapisy z Pages CMS (`nawigacja.json`, 6.11).

Znaczniki zachowują wszystkie te commity. **Po usunięciu gałęzi nic nie znika z repozytoriów.**

### Przygotowane lokalnie (gałąź `praca/38-porzadki`, 2 commity, niewypchnięte)
1. `74781d1` — `skrypty/porzadki/galezie.py`.
   - **Plan** (domyślnie): czyta stan z GitHuba przez `git ls-remote`. Dla każdej gałęzi podaje: ostatni commit, liczbę commitów spoza `main`, wynik `git cherry`, czy pliki zmienione na gałęzi mają w `main` tę samą treść, otwarte PR i stan znacznika.
   - **`--wykonaj plan.json`** (po „push”): pomija gałąź, jeśli od planu zmienił się jej commit. Tworzy znacznik z opisem, wypycha go i sprawdza na GitHubie. Dopiero potem usuwa gałąź (`git push origin :refs/heads/<nazwa>`). Używa pełnych nazw ref, bo znacznik `archiwum/2026-11-09-silnik-banerow` ma tę samą nazwę co gałąź.
   - Na końcu robi **kontrolę** (`--kontrola`): w każdym repozytorium mają zostać tylko `main` (i `zbudowana`), a każda usunięta gałąź ma mieć swój znacznik.
2. `222d5e4` — usunięcie z `main` plików `sprawdz-galaz.yml`, `qa.yml` i `proza-domyslna-test.yml`. Zostają `deploy.yml`, `podglad-przekaznik.yml` i `plan-zajec.yml`. W tym samym commicie:
   - `dok/archiwum-silnika-banerow.md`: gałąź zamieniona na znacznik o tej samej nazwie, `git fetch origin tag …`;
   - `dok/en/POSTEP.md`: odwołania do gałęzi zamienione na znaczniki;
   - opis w `skrypty/pobierz_tresci.py`: bez nazw usuniętych workflowów.

   Commit nie zmienia budowy strony.

Plan w JSON (wejście dla `--wykonaj`) i ta sama tabela osobno: `raport-zrzuty/z38-plan-galezi.json` i `.md`. Dopisałem je do `.git/info/exclude` razem z `RAPORT-ZLECENIE-38*`, żeby nie trafiły przypadkiem do commita w żadnym worktree.

### Po „push” zrobię, w tej kolejności
1. `git fetch`, a potem `rebase` `praca/38-porzadki` na `origin/main`.
2. **Nowy plan i porównanie z tym raportem.** Jeśli jakaś gałąź zmieniła commit albo pojawiła się nowa, zatrzymam się i o tym napiszę.
3. `galezie.py --wykonaj`: najpierw znacznik, potem usunięcie gałęzi; po kolei we wszystkich 18 repozytoriach. `archiwum/2026-11-09-silnik-banerow` zamieni się tu w znacznik.
4. Ponownie `fetch` i `rebase`, potem push dwóch commitów na `main` Web-Core (zwykły push, bez force).
5. Kontrola przez `git ls-remote` we wszystkich repozytoriach. Lista trafi do raportu.

### Pytania
1. **`Web-Podglad/.github/workflows/markdown-jawne-test.yml`**: izolowany test jawnego Markdownu, uruchamiany ręcznie. Ostatnio działał 8.11 (3 przebiegi, wszystkie udane). Zostawiam go, zgodnie ze zleceniem. **Czy jest jeszcze potrzebny?**
2. Po usunięciu `qa.yml` nic już nie używa `.github/qa/` (`qa.py`, `kontrast.cjs`) ani `skrypty/szerokosci/`. W etapie 2 wpiszę je na listę kandydatów do usunięcia. **Czy narzędzie kontroli jakości ma zostać na później?**
3. `deploy.yml` (wyłączony) ma krok „Warianty wyglądu (gałęzie `wariant-*`)” i wywołuje `skrypty/warianty.py`. Po usunięciu gałęzi `wariant-*` ten krok sam się pomija. W etapie 2 chcę go usunąć razem z `warianty.py`; reszta `deploy.yml` zostaje. **Zgoda?**
4. `Avean/IM-Website-test` (poza organizacją IM-UWr) ma na GitHubie 55 gałęzi. Zlecenie go nie obejmuje, więc go nie ruszam.

### Tabela gałęzi (stan GitHuba z 18.11, ok. 00:30)
Kolumny:
- **Spoza main**: `git rev-list --count origin/main..gałąź`;
- **`cherry` +/−**: commity, których zmian nie ma w `main` / które są w `main` pod innym SHA;
- **Pliki jak w main**: czy pliki zmienione na gałęzi mają dziś w `main` tę samą treść.

#### Web-Aktualnosci — 0 gałęzi poza main

Tylko `main`.


#### Web-Core — 47 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `agent-instytut-baza-podglad` | 2026-10-30 `b6c4e38` | Claude | Wygląd podstron: strona główna — wariant „Obecna”, bez przełącznika… | 0 | 0/0 | — | w main (cała historia) | `archiwum/agent-instytut-baza-podglad` (brak) | — |
| `agent-instytut-podglad` | 2026-10-30 `d6015ae` | Claude | Instytut na komputerze: baner jak w „Portal” (liczby w banerze), re… | 0 | 0/0 | — | w main (cała historia) | `archiwum/agent-instytut-podglad` (brak) | — |
| `agent-naglowek-podglad` | 2026-10-30 `a1a167a` | Claude | Nagłówek: logo UWr prowadzi na uwr.edu.pl, nazwa instytutu na stron… | 1 | 0/1 | nie | zmiany w main (inne SHA) | `archiwum/agent-naglowek-podglad` (brak) | — |
| `agent-naglowek-portal-podglad` | 2026-10-30 `b568f76` | Claude | Nagłówek: logo UWr prowadzi na uwr.edu.pl, nazwa instytutu na stron… | 4 | 3/1 | nie | **COMMITY SPOZA MAIN** | `archiwum/agent-naglowek-portal-podglad` (brak) | — |
| `agent-naglowek-redakcyjna-podglad` | 2026-10-30 `d1e4a47` | Claude | Nagłówek: logo UWr prowadzi na uwr.edu.pl, nazwa instytutu na stron… | 2 | 2/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/agent-naglowek-redakcyjna-podglad` (brak) | — |
| `agent-naglowek-v2-podglad` | 2026-10-30 `52e3e70` | Claude | Nagłówek: logo UWr prowadzi na uwr.edu.pl, nazwa instytutu na stron… | 0 | 0/0 | — | w main (cała historia) | `archiwum/agent-naglowek-v2-podglad` (brak) | — |
| `agent-naglowek-zwarta-podglad` | 2026-10-30 `7ccebb2` | Claude | Nagłówek: logo UWr prowadzi na uwr.edu.pl, nazwa instytutu na stron… | 2 | 1/1 | nie | **COMMITY SPOZA MAIN** | `archiwum/agent-naglowek-zwarta-podglad` (brak) | — |
| `agent-nauka-podglad` | 2026-10-30 `5cb2b46` | Claude | Telefon (na próbę): płynne przejścia między stronami, łagodne wejśc… | 0 | 0/0 | — | w main (cała historia) | `archiwum/agent-nauka-podglad` (brak) | — |
| `agent-podglad-migracja` | 2026-10-29 `6caf543` | Claude | Kod strony przeniesiony z Avean/IM-Website-test (stan 4e8fce8), tre… | 0 | 0/0 | — | w main (cała historia) | `archiwum/agent-podglad-migracja` (brak) | — |
| `agent-wariant-portal-podglad` | 2026-10-29 `224ff6a` | Claude | Wariant „Portal”: opis telefon.css zgodny z tą gałęzią (bloki .tylk… | 3 | 3/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/agent-wariant-portal-podglad` (brak) | — |
| `agent-wariant-redakcyjna-podglad` | 2026-10-29 `43ab670` | Claude | Wariant „Redakcyjna” na komputerze (≥ 761 px), telefon bez zmian | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/agent-wariant-redakcyjna-podglad` (brak) | — |
| `agent-wariant-zwarta-podglad` | 2026-10-29 `60f1101` | Claude | Wariant „Zwarta” na komputerze (≥ 761 px), telefon bez zmian | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/agent-wariant-zwarta-podglad` (brak) | — |
| `archiwum/2026-11-09-silnik-banerow` | 2026-11-09 `ec63774` | Szymon | Mapa redakcyjna: jawny Markdown także w Popularyzacji | 0 | 0/0 | — | w main (cała historia) | `archiwum/2026-11-09-silnik-banerow` (brak) | — |
| `cms-reorganizacja-2026-11` | 2026-11-08 `97cab1e` | Szymon Cygan | Raport: zapisane branche, draft PR-y i udane testy GitHub Actions | 2 | 2/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #2 Reorganizacja CMS: scalone specjalności, ręczne menu i integracja strony |
| `kopia/2026-11-01-agent-nauka-podglad` | 2026-11-01 `ae6d5d9` | Szymon | Telefon: atraktor Lorenza przy prawej krawędzi, fala Fouriera od ko… | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-01-agent-nauka-podglad` (brak) | — |
| `kopia/2026-11-01-estetyka-prototypy` | 2026-11-06 `c9d3f0a` | Claude | Lista przed wdrożeniem: strona bezobsługowa (specjalności, seminari… | 140 | 140/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/kopia/2026-11-01-estetyka-prototypy` (brak) | — |
| `kopia/2026-11-06-nakladka-i-niezacommitowane` | 2026-11-06 `d0147cb` | Claude | Kopia bezpieczeństwa 6.11.2026: nakładka treści i niezacommitowane … | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/kopia/2026-11-06-nakladka-i-niezacommitowane` (brak) | — |
| `kopia/2026-11-06-wyglad-zlecenie-16` | 2026-11-06 `70c3c6f` | Szymon | Zlecenie 18, punkt 5: USOSweb poza menu, filtr jestUsos usunięty | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06-wyglad-zlecenie-16` (brak) | — |
| `markdown-domyslna-proza-2026-11` | 2026-11-09 `64d21fc` | Szymon | Jawny Markdown dla Popularyzacji z zachowaniem układu | 0 | 0/0 | — | w main (cała historia) | `archiwum/markdown-domyslna-proza-2026-11` (brak) | — |
| `markdown-jawne-bloki-2026-11` | 2026-11-08 `b83cde0` | Szymon | Instrukcja redaktorów dla wdrożenia na main | 0 | 0/0 | — | w main (cała historia) | `archiwum/markdown-jawne-bloki-2026-11` (brak) | — |
| `podglad-agent-instytut-baza-podglad` | 2026-10-29 `55e35f3` | github-actions[bot] | Podgląd agent-instytut-baza-podglad @ b6c4e38 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-instytut-baza-podglad` (brak) | — |
| `podglad-agent-instytut-podglad` | 2026-10-29 `5015543` | github-actions[bot] | Podgląd agent-instytut-podglad @ d6015ae | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-instytut-podglad` (brak) | — |
| `podglad-agent-naglowek-podglad` | 2026-10-29 `ff3a223` | github-actions[bot] | Podgląd agent-naglowek-podglad @ a1a167a | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-naglowek-podglad` (brak) | — |
| `podglad-agent-naglowek-portal-podglad` | 2026-10-29 `dbb47dd` | github-actions[bot] | Podgląd agent-naglowek-portal-podglad @ b568f76 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-naglowek-portal-podglad` (brak) | — |
| `podglad-agent-naglowek-redakcyjna-podglad` | 2026-10-29 `7b0078d` | github-actions[bot] | Podgląd agent-naglowek-redakcyjna-podglad @ d1e4a47 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-naglowek-redakcyjna-podglad` (brak) | — |
| `podglad-agent-naglowek-v2-podglad` | 2026-10-29 `01995d7` | github-actions[bot] | Podgląd agent-naglowek-v2-podglad @ 52e3e70 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-naglowek-v2-podglad` (brak) | — |
| `podglad-agent-naglowek-zwarta-podglad` | 2026-10-29 `65c526a` | github-actions[bot] | Podgląd agent-naglowek-zwarta-podglad @ 7ccebb2 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-naglowek-zwarta-podglad` (brak) | — |
| `podglad-agent-nauka-podglad` | 2026-10-31 `ff76086` | github-actions[bot] | Podgląd agent-nauka-podglad @ 5cb2b46 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-nauka-podglad` (brak) | — |
| `podglad-agent-podglad-migracja` | 2026-10-29 `160449e` | github-actions[bot] | Podgląd agent-podglad-migracja @ 6caf543 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-podglad-migracja` (brak) | — |
| `podglad-agent-wariant-portal-podglad` | 2026-10-29 `988612d` | github-actions[bot] | Podgląd agent-wariant-portal-podglad @ 224ff6a | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-wariant-portal-podglad` (brak) | — |
| `podglad-agent-wariant-redakcyjna-podglad` | 2026-10-29 `bfaf743` | github-actions[bot] | Podgląd agent-wariant-redakcyjna-podglad @ 43ab670 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-wariant-redakcyjna-podglad` (brak) | — |
| `podglad-agent-wariant-zwarta-podglad` | 2026-10-29 `652adee` | github-actions[bot] | Podgląd agent-wariant-zwarta-podglad @ 60f1101 | 1 | 1/0 | nie | **COMMITY SPOZA MAIN (bez wspólnej historii z main)** | `archiwum/podglad-agent-wariant-zwarta-podglad` (brak) | — |
| `robocza-aktualnosci` | 2026-10-30 `d4ba6ac` | Claude | Aktualność na komputerze: wygląd „Zwarta”, treść wpisu w białej ramce | 0 | 0/0 | — | w main (cała historia) | `archiwum/robocza-aktualnosci` (brak) | — |
| `robocza-instytut` | 2026-10-30 `9bbe19e` | Claude | Podstrony Instytutu na komputerze: baner jak w „Portal”, reszta jak… | 0 | 0/0 | — | w main (cała historia) | `archiwum/robocza-instytut` (brak) | — |
| `robocza-nauka-podstrony` | 2026-10-30 `5396fca` | Claude | Merge remote-tracking branch 'origin/agent-nauka-podglad' into robo… | 0 | 0/0 | — | w main (cała historia) | `archiwum/robocza-nauka-podstrony` (brak) | — |
| `robocza-nauka-tekst` | 2026-10-30 `f201a98` | Claude | Nauka: tekst „Badania w Instytucie” z ramką „W skrócie” zamiast „Ob… | 0 | 0/0 | — | w main (cała historia) | `archiwum/robocza-nauka-tekst` (brak) | — |
| `robocza-studia` | 2026-10-30 `4c087f3` | Claude | Studia: „W tym dziale” i „O studiach” zamiast kierunków, ścieżek i … | 0 | 0/0 | — | w main (cała historia) | `archiwum/robocza-studia` (brak) | — |
| `wariant-portal` | 2026-10-30 `b568f76` | Claude | Nagłówek: logo UWr prowadzi na uwr.edu.pl, nazwa instytutu na stron… | 4 | 3/1 | nie | **COMMITY SPOZA MAIN** | `archiwum/wariant-portal` (brak) | — |
| `wariant-redakcyjna` | 2026-10-30 `d1e4a47` | Claude | Nagłówek: logo UWr prowadzi na uwr.edu.pl, nazwa instytutu na stron… | 2 | 2/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/wariant-redakcyjna` (brak) | — |
| `wariant-zwarta` | 2026-10-30 `7ccebb2` | Claude | Nagłówek: logo UWr prowadzi na uwr.edu.pl, nazwa instytutu na stron… | 2 | 1/1 | nie | **COMMITY SPOZA MAIN** | `archiwum/wariant-zwarta` (brak) | — |
| `wyglad/en` | 2026-11-05 `9223b2a` | Claude | POSTEP: dokładny opis porównania zrzutów | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/en` (brak) | — |
| `wyglad/porzadki` | 2026-11-05 `f315100` | Claude | Raport: commity poprawek po przeglądzie | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/porzadki` (brak) | — |
| `wyglad/porzadki-01-telefon` | 2026-11-04 `94733c7` | Claude | Etap 1: Plan zajęć, Projekty i granty i strony tekstowe w jednej we… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/porzadki-01-telefon` (brak) | — |
| `wyglad/porzadki-02-szablon` | 2026-11-04 `7684cde` | Claude | Etap 2: wspólny szablon podstrony, „Na tej stronie” z prawej (kresk… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/porzadki-02-szablon` (brak) | — |
| `wyglad/porzadki-03-podstrony` | 2026-11-04 `d706728` | Claude | Raport: etap 3 (podstrony według wzorca treści); PYTANIA: sekcja „Z… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/porzadki-03-podstrony` (brak) | — |
| `wyglad/zalozyciele` | 2026-11-02 `d12c994` | Claude | PYTANIA: próbna wersja na telefon trzymana poza Web-Core (łatka w W… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zalozyciele` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-07 `c6b39f5` | Szymon | Zlecenie 30, pytanie 1: poprawka opisu — kotwicy #konsultacje używa… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Instytut — 0 gałęzi poza main

Tylko `main`.


#### Web-Nauka — 0 gałęzi poza main

Tylko `main`.


#### Web-Podglad — 2 gałęzi poza main, zbudowana

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `80016d7` | Szymon Cygan | Test pełnych branchy reorganizacji CMS bez publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Izolowany test pełnych branchy reorganizacji CMS bez publikacji |
| `markdown-jawne-bloki-2026-11` | 2026-11-08 `f7bd03a` | Szymon | Testuj main lub wskazaną wspólną gałąź po wdrożeniu | 0 | 0/0 | — | w main (cała historia) | `archiwum/markdown-jawne-bloki-2026-11` (brak) | — |

#### Web-Popularyzacja — 0 gałęzi poza main

Tylko `main`.


#### Web-Pracownicy — 1 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `630500d` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |

#### Web-Sem-Analiza-Harmoniczna — 1 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `5be3f23` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |

#### Web-Sem-Dydaktyka — 1 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `14b60a9` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |

#### Web-Sem-Dyskretna-Analiza-Harmoniczna — 1 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `161b401` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |

#### Web-Sem-Geometria — 1 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `b565d2f` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |

#### Web-Sem-Prawdopodobienstwo — 1 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `c545855` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |

#### Web-Sem-Rownania-Rozniczkowe — 2 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `91f1506` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |
| `wyglad/zlecenie-16` | 2026-11-06 `4ff405e` | Szymon | Wpisy testowe na 9–19 listopada: 1 referat (prośba właściciela) | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (jest, ten sam commit) | — |

#### Web-Sem-Statystyka — 3 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `6fc8b1e` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |
| `kopia/2026-11-06` | 2026-11-05 `a8faf44` | Szymon | Wersja angielska: tłumaczenia (zlecenie 16) | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-06 `d92bebc` | Szymon | Wpisy testowe na 9–19 listopada: 1 referat (prośba właściciela) | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Sem-Teoria-Modeli — 3 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `146d607` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |
| `kopia/2026-11-06` | 2026-11-05 `9dc5e28` | Szymon | Wersja angielska: tłumaczenia (zlecenie 16) | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-06 `311a148` | Szymon | Formularze: hasła, liczby i pozostałe pola danych (zlecenie 22, eta… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Sem-Topologia — 4 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `0c4fd73` | Szymon Cygan | Porządki CMS: aktualne pola, opisy i statusy publikacji | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Pages CMS: używane pola, aktualne opisy i status publikacji |
| `kopia/2026-11-06` | 2026-11-05 `df00da7` | Szymon | Wersja angielska: tłumaczenia (zlecenie 16) | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `test-cms` | 2026-11-06 `287338a` | Symon Cygan | Update src/content/seminaria/topologia.md (via Pages CMS) | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/test-cms` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-06 `2d5387c` | Szymon | Formularze: hasła, liczby i pozostałe pola danych (zlecenie 22, eta… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Spec-Aktuarialno-Finansowa — 4 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `51ecece` | Szymon Cygan | Archiwum specjalności: przeniesienie edycji do Web-Studia | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Archiwum specjalności: przeniesienie edycji do Web-Studia |
| `kopia/2026-11-06` | 2026-11-05 `e11ed6c` | Szymon | Wersja angielska: tłumaczenia (zlecenie 16) | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `test-cms` | 2026-11-06 `fddf23f` | Symon Cygan | Update src/content/specjalnosci/matematyka-aktuarialno-finansowa.md… | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/test-cms` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-07 `72bc53e` | Szymon | Zlecenie 29, etap 3: formularze specjalności „Treść” oraz „Baner i … | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Spec-Analiza-Danych — 3 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `d0b4dc5` | Szymon Cygan | Archiwum specjalności: przeniesienie edycji do Web-Studia | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Archiwum specjalności: przeniesienie edycji do Web-Studia |
| `kopia/2026-11-06` | 2026-11-05 `c4c03ad` | Szymon | Wersja angielska: tłumaczenia (zlecenie 16) | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-07 `eb14354` | Szymon | Zlecenie 29: pogrubione „No.” na początku 2 odpowiedzi EN (FAQ), że… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Spec-Nauczycielska — 3 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `32a25e6` | Szymon Cygan | Archiwum specjalności: przeniesienie edycji do Web-Studia | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Archiwum specjalności: przeniesienie edycji do Web-Studia |
| `kopia/2026-11-06` | 2026-11-05 `fc9844a` | Szymon | Wersja angielska: tłumaczenia (zlecenie 16) | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-07 `891742b` | Szymon | Zlecenie 29: pogrubione „No.” na początku 2 odpowiedzi EN (FAQ), że… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Spec-Stosowana — 4 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `1f68411` | Szymon Cygan | Archiwum specjalności: przeniesienie edycji do Web-Studia | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Archiwum specjalności: przeniesienie edycji do Web-Studia |
| `kopia/2026-11-06` | 2026-11-05 `0ec9422` | Szymon | Wersja angielska: tłumaczenia (zlecenie 16) | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `test-cms` | 2026-11-07 `4806331` | Szymon | Zlecenie 29, etap 3: formularze specjalności „Treść” oraz „Baner i … | 0 | 0/0 | — | w main (cała historia) | `archiwum/test-cms` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-07 `4806331` | Szymon | Zlecenie 29, etap 3: formularze specjalności „Treść” oraz „Baner i … | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Spec-Teoretyczna — 3 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `cms-reorganizacja-2026-11` | 2026-11-08 `22ea14e` | Szymon Cygan | Archiwum specjalności: przeniesienie edycji do Web-Studia | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Archiwum specjalności: przeniesienie edycji do Web-Studia |
| `kopia/2026-11-06` | 2026-11-05 `ed7f374` | Szymon | Wersja angielska: tłumaczenia (zlecenie 16) | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-07 `4f89fa8` | Szymon | Zlecenie 29, etap 3: formularze specjalności „Treść” oraz „Baner i … | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

#### Web-Studia — 0 gałęzi poza main

Tylko `main`.


#### Web-Ustawienia — 8 gałęzi poza main

| Gałąź | Ostatni commit | Autor | Temat | Spoza main | `cherry` +/− | Pliki jak w main | Ocena | Znacznik archiwum | PR |
|---|---|---|---|---:|---:|---|---|---|---|
| `agent-nauka-podglad` | 2026-10-30 `07455a8` | Claude | W skrócie: angielskie etykiety (wartosc_en) w Instytucie, Nauce i S… | 0 | 0/0 | — | w main (cała historia) | `archiwum/agent-nauka-podglad` (brak) | — |
| `cms-reorganizacja-2026-11` | 2026-11-08 `7f72b82` | Szymon Cygan | Połącz ręczne menu i kafelki oraz usuń stare ustawienia | 1 | 1/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/cms-reorganizacja-2026-11` (brak) | #1 Jedno ręczne menu i kafelki w Pages CMS; usunięcie starych opcji |
| `kopia/2026-11-06` | 2026-11-06 `e3d250a` | Szymon | Nagłówki: zdjęcie banera Aktualności aktualnosci-skok.jpg (zlecenie… | 0 | 0/0 | — | w main (cała historia) | `archiwum/kopia/2026-11-06` (brak) | — |
| `kopia/test-cms-zlecenie-22` | 2026-11-06 `f181206` | Symon Cygan | Update src/data/nawigacja.json (via Pages CMS) | 2 | 2/0 | nie | **COMMITY SPOZA MAIN** | `archiwum/kopia/test-cms-zlecenie-22` (brak) | — |
| `robocza-nauka-tekst` | 2026-10-30 `b1b35ae` | Claude | Nauka: tekst „Badania w Instytucie” (PL/EN) i ramka „W skrócie” zam… | 0 | 0/0 | — | w main (cała historia) | `archiwum/robocza-nauka-tekst` (brak) | — |
| `robocza-studia` | 2026-10-30 `3066437` | Claude | Studia: tekst „O studiach” z ramką „W skrócie” zamiast opisów ścieżek | 0 | 0/0 | — | w main (cała historia) | `archiwum/robocza-studia` (brak) | — |
| `test-cms` | 2026-11-07 `217a9bf` | Szymon | Zlecenie 30, etap 3: formularze stron prawnych — Tytuł, Treść, Tytu… | 0 | 0/0 | — | w main (cała historia) | `archiwum/test-cms` (brak) | — |
| `wyglad/zlecenie-16` | 2026-11-07 `217a9bf` | Szymon | Zlecenie 30, etap 3: formularze stron prawnych — Tytuł, Treść, Tytu… | 0 | 0/0 | — | w main (cała historia) | `archiwum/wyglad/zlecenie-16` (brak) | — |

## Stare foldery (przegląd; nic nie usunąłem)

**Jak sprawdzałem.** Dla każdego zmienionego albo nieśledzonego pliku porównałem jego treść z GitHubem: z `origin/main` Web-Core i z `main` wszystkich 21 repozytoriów treści. Końce wierszy CRLF/LF uznaję za równe. Kategorie:
- **TIP**: identyczny z dzisiejszym `main`;
- **HIST**: ta sama treść jest w historii `main` (starsza wersja);
- **INNE**: treść jest tylko w innych gałęziach (po etapie 1 będzie w znacznikach);
- **BRAK**: tej treści nie ma nigdzie na GitHubie.

Wynik w skrócie: **unikalny materiał jest tylko w `IM-Website-test`** (ok. 330 MB). Wszystko inne jest na GitHubie, jest starszą wersją albo da się to odtworzyć. Można zwolnić **ok. 6 GB**.

| Folder | Co to jest | Rozmiar | Niezacommitowane | Bez odpowiednika na GitHubie | Propozycja |
|---|---|---:|---|---|---|
| `source\Web-Core` | Pusty katalog `.git` (17.11, 23:49), pozostałość po przenosinach. To nie jest repozytorium. | 20 KB | — | nic | usunąć |
| `source\Web-Core-porzadki` | Zarejestrowany worktree Web-Core: odłączony HEAD `f315100` (= `wyglad/porzadki`, jest w `main`), 5.11. | 612 MB | 74 nieśledzone: kopia nakładki treści z 30–31.10 pod zdublowanymi ścieżkami (`src/content/referaty/referaty/…`) i `package-lock.json` | 9 plików bez dokładnej kopii (5 specjalności, 4 strony Studiów z 31.10) | usunąć: `git worktree remove --force` (z Web-Core) |
| `source\wc28` | Zarejestrowany worktree Web-Core: odłączony HEAD `900b034` (zlecenia 28 i 29, 7.11; jest w `main`). | 852 MB | 51 zmienionych i 5 nieśledzonych | nic | usunąć: `git worktree remove --force` |
| `source\wc28-przed`, `-po`, `-po2`, `-po3`, `-edytor`, `wc29-przed`, `-po`, `-po2`, `-edytor`, `wc30-przed`, `-po` | 11 zbudowanych stron (`dist`) do porównań przed/po w zleceniach 28–30 | 11 × 255 MB ≈ 2,8 GB | — | nic (da się zbudować ponownie) | usunąć |
| `source\wc28-check` | `node_modules`, `pomiar.mjs` i `zrzuty.mjs` (pomiary szerokości i zrzuty, 7.11) | 79 MB | — | 2 skrypty, razem 7 KB | usunąć (skrypty można zachować, jeśli się przydadzą) |
| `source\wc28-venv` | Środowisko Pythona | 17 MB | — | nic | usunąć |
| `source\wc29-proba`, `wc29-proba-pop` | Wyniki próbnej migracji specjalności i Popularyzacji (7.11) | 0,3 MB | — | nic: 13 plików, wszystkie w historii repozytoriów treści | usunąć |
| `source\kopie-2026-11-17\nakladka` | Kopia 5 plików nakładki (17.11, 23:26) | 0,4 MB | — | nic: 2 pliki jak w `main`, 3 w historii | usunąć |
| `source\wc31\tresci` | Klony Web-Aktualnosci, Web-Pracownicy, Web-Studia i Web-Instytut (17.11, 23:32; zlecenie 31) | 256 MB | Aktualności, Pracownicy i Studia: czyste, na `main`. **Web-Instytut jest uszkodzony**: wskazuje obiekty w nieistniejącym `source\tresci\Web-Instytut` | — | **na razie nie ruszać**, bo może go używać druga sesja (zlecenie 31). Usunąć po zamknięciu 31 |
| `source\repos\Solution1` | Projekt Visual Studio ze stycznia 2024, niezwiązany ze stroną | 13 KB | — | — | zostawić, nie dotyczy projektu |
| `source\*.log`, `*.txt` (24 pliki) | Logi budowy, pobierania i porównań ze zleceń 28–30 | 6,6 MB | — | — | usunąć |
| `GitHub\_stare\Web-Core-2026-11-17` | Osobny pełny klon Web-Core (własny `.git`). Gałąź `main` na `6eddb9f` (7.11, jest w `origin/main`). Bez innych gałęzi i bez stash. | ok. 1 GB | 1 nieśledzony `package-lock.json` (plik generowany, ta wersja nigdzie nie występuje) | nic wartościowego | usunąć |
| `GitHub\IM-Website-test` | Poprzednie repozytorium strony (`Avean/IM-Website-test`, sprzed migracji 29.10). Lokalny `main` `2fdb4e2` (24.10) jest 128 commitów za GitHubem i nie ma własnych commitów. | ok. 940 MB (`output` 305, `node_modules` 204, `dist` 160, `.git` 125) | 5 zmienionych i 777 nieśledzonych | **tak, ok. 330 MB** (opis niżej) | zachować materiały, resztę usunąć |

**Szczegóły:**
- **`Web-Core-porzadki`**:
  - 32 pliki nakładki są identyczne z dzisiejszym `main` repozytoriów treści, 32 są w ich historii.
  - 9 plików bez dokładnej kopii to wersje z 31.10, 23:28–23:32. Różnią się od importu z 29.10 tylko 1 wierszem. Później te teksty przerabiano w Web-Studia (7–9.11), więc te wersje są nieaktualne. Nie ma ich też w kopii nakładki z 6.11 (gałąź `kopia/2026-11-06-nakladka-i-niezacommitowane`).
- **`wc28`**:
  - 46 plików jest identycznych z dzisiejszym `main`.
  - 9 to wersje robocze zlecenia 30 (7.11, 15:16–16:06; m.in. `tekstyStron.ts`, `markdown.ts`, `rehype-bloki.mjs`). Wszystkie są w historii `main`, czyli zostały zacommitowane.
  - `package-lock.json` jest w innej gałęzi.
- **`IM-Website-test`: treść, której nie ma nigdzie na GitHubie:**
  - `output\` (717 plików, 305 MB): autografy (214 MB), `banery-2026-11-01` (79 MB), `imagegen` (13 MB), `export-patronow`, `portrety-animacja`. To prace nad patronami i banerami z 31.10–2.11.
  - `public\pliki\portrety\proba-01\` (25 plików: portrety, kontury podpisów, prompty, referencje) i `public\pliki\szkice-patronow.zip`.
  - 3 nieśledzone pliki kodu: `src\components\MotywDzialu.astro`, `src\lib\motywyDzialow.ts`, `src\styles\charakter.css`.
  - Zmiany w `README.md`, `package.json`, `NaglowekStrony.astro` i `Baza.astro` (+17 wierszy).
  - 4 obrazy banerów (`Waves.png`, `kampus-zmierzch-*`). Są tylko w lokalnym punkcie kontrolnym Codex (`refs/codex/…`).
  - 13 plików podpisów jest w gałęziach Web-Core (po etapie 1 będą w znacznikach), a 13 innych w `main` Web-Core pod inną ścieżką.

  **Propozycja:** przenieść `output\`, `public\pliki\portrety\`, `szkice-patronow.zip`, 3 pliki kodu i 4 obrazy do `_stare\IM-Website-test-materialy\` albo je spakować. Resztę usunąć: `node_modules` i `dist` da się odtworzyć, a historia jest na GitHubie.
- **Przy okazji (repozytorium Web-Core, którego używa druga sesja; nic nie ruszałem):**
  - Wspólny stash ma 3 wpisy: 17.11 (`package-lock.json` i pusty wiersz w `zalozyciele.css`), 31.10 i 30.10. Opis wpisu z 31.10 mówi, że to pliki wgrane ręcznie przez Claude i że odpowiadają `origin/agent-nauka-podglad 0a9eff5`; nie porównywałem tego. Wpis z 30.10 to kopia zapasowa plików wgranych ręcznie przez Claude 29–30.10. Do decyzji, czy je skasować (`git stash drop`).
  - 7 lokalnych gałęzi (`agent-nauka-podglad`, `wyglad/zalozyciele`, `wyglad/zlecenie-11`, `-13`, `-14`, `-15`, `-16`) jest w całości w `origin/main`. Można je usunąć bezpiecznie przez `git branch -d`.

## Etap 1 — wykonany po „push” (18.11.2026, 00:47)

- Przed wykonaniem: `fetch`, nowy plan i porównanie z planem z raportu. Wynik: te same 92 gałęzie i te same commity, `main` bez zmian we wszystkich repozytoriach.
- `galezie.py --wykonaj`: w każdym repozytorium kolejno znacznik z opisem, push znacznika, sprawdzenie na GitHubie (`ls-remote`), dopiero potem usunięcie gałęzi. **92 gałęzie: 91 nowych znaczników i 1 istniejący** (Web-Sem-Rownania-Rozniczkowe, `archiwum/wyglad/zlecenie-16`). Żadna gałąź nie została pominięta, nie było błędów.
- `archiwum/2026-11-09-silnik-banerow` w Web-Core jest teraz **znacznikiem** wskazującym ten sam commit `ec637746`.
- Push na `main` Web-Core: `24c708e..222d5e4`. Był to zwykły push z przewinięciem (fast-forward), bez force. Przed nim zrobiłem `fetch` i `rebase`, `origin/main` się nie zmienił. Workflowy na `main`: `deploy.yml`, `plan-zajec.yml`, `podglad-przekaznik.yml`.
- Otwarte PR z `cms-reorganizacja-2026-11` GitHub zamknął razem z gałęziami.

### Kontrola (`git ls-remote`, niezależnie od skryptu)

| Repozytorium | Gałęzie | Znaczniki `archiwum/*` |
|---|---|---:|
| Web-Aktualnosci | `main` | 4 |
| Web-Core | `main` | 48 |
| Web-Instytut | `main` | 3 |
| Web-Nauka | `main` | 5 |
| Web-Podglad | `main` `zbudowana` | 2 |
| Web-Popularyzacja | `main` | 5 |
| Web-Pracownicy | `main` | 3 |
| Web-Sem-Analiza-Harmoniczna | `main` | 4 |
| Web-Sem-Dydaktyka | `main` | 4 |
| Web-Sem-Dyskretna-Analiza-Harmoniczna | `main` | 4 |
| Web-Sem-Geometria | `main` | 4 |
| Web-Sem-Prawdopodobienstwo | `main` | 4 |
| Web-Sem-Rownania-Rozniczkowe | `main` | 4 |
| Web-Sem-Statystyka | `main` | 4 |
| Web-Sem-Teoria-Modeli | `main` | 4 |
| Web-Sem-Topologia | `main` | 5 |
| Web-Spec-Aktuarialno-Finansowa | `main` | 5 |
| Web-Spec-Analiza-Danych | `main` | 4 |
| Web-Spec-Nauczycielska | `main` | 4 |
| Web-Spec-Stosowana | `main` | 5 |
| Web-Spec-Teoretyczna | `main` | 4 |
| Web-Studia | `main` | 1 |
| Web-Ustawienia | `main` | 9 |

### Usunięte gałęzie i ich znaczniki (92)

- Web-Core: `agent-instytut-baza-podglad` → `archiwum/agent-instytut-baza-podglad`
- Web-Core: `agent-instytut-podglad` → `archiwum/agent-instytut-podglad`
- Web-Core: `agent-naglowek-podglad` → `archiwum/agent-naglowek-podglad`
- Web-Core: `agent-naglowek-portal-podglad` → `archiwum/agent-naglowek-portal-podglad`
- Web-Core: `agent-naglowek-redakcyjna-podglad` → `archiwum/agent-naglowek-redakcyjna-podglad`
- Web-Core: `agent-naglowek-v2-podglad` → `archiwum/agent-naglowek-v2-podglad`
- Web-Core: `agent-naglowek-zwarta-podglad` → `archiwum/agent-naglowek-zwarta-podglad`
- Web-Core: `agent-nauka-podglad` → `archiwum/agent-nauka-podglad`
- Web-Core: `agent-podglad-migracja` → `archiwum/agent-podglad-migracja`
- Web-Core: `agent-wariant-portal-podglad` → `archiwum/agent-wariant-portal-podglad`
- Web-Core: `agent-wariant-redakcyjna-podglad` → `archiwum/agent-wariant-redakcyjna-podglad`
- Web-Core: `agent-wariant-zwarta-podglad` → `archiwum/agent-wariant-zwarta-podglad`
- Web-Core: `archiwum/2026-11-09-silnik-banerow` → `archiwum/2026-11-09-silnik-banerow`
- Web-Core: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Core: `kopia/2026-11-01-agent-nauka-podglad` → `archiwum/kopia/2026-11-01-agent-nauka-podglad`
- Web-Core: `kopia/2026-11-01-estetyka-prototypy` → `archiwum/kopia/2026-11-01-estetyka-prototypy`
- Web-Core: `kopia/2026-11-06-nakladka-i-niezacommitowane` → `archiwum/kopia/2026-11-06-nakladka-i-niezacommitowane`
- Web-Core: `kopia/2026-11-06-wyglad-zlecenie-16` → `archiwum/kopia/2026-11-06-wyglad-zlecenie-16`
- Web-Core: `markdown-domyslna-proza-2026-11` → `archiwum/markdown-domyslna-proza-2026-11`
- Web-Core: `markdown-jawne-bloki-2026-11` → `archiwum/markdown-jawne-bloki-2026-11`
- Web-Core: `podglad-agent-instytut-baza-podglad` → `archiwum/podglad-agent-instytut-baza-podglad`
- Web-Core: `podglad-agent-instytut-podglad` → `archiwum/podglad-agent-instytut-podglad`
- Web-Core: `podglad-agent-naglowek-podglad` → `archiwum/podglad-agent-naglowek-podglad`
- Web-Core: `podglad-agent-naglowek-portal-podglad` → `archiwum/podglad-agent-naglowek-portal-podglad`
- Web-Core: `podglad-agent-naglowek-redakcyjna-podglad` → `archiwum/podglad-agent-naglowek-redakcyjna-podglad`
- Web-Core: `podglad-agent-naglowek-v2-podglad` → `archiwum/podglad-agent-naglowek-v2-podglad`
- Web-Core: `podglad-agent-naglowek-zwarta-podglad` → `archiwum/podglad-agent-naglowek-zwarta-podglad`
- Web-Core: `podglad-agent-nauka-podglad` → `archiwum/podglad-agent-nauka-podglad`
- Web-Core: `podglad-agent-podglad-migracja` → `archiwum/podglad-agent-podglad-migracja`
- Web-Core: `podglad-agent-wariant-portal-podglad` → `archiwum/podglad-agent-wariant-portal-podglad`
- Web-Core: `podglad-agent-wariant-redakcyjna-podglad` → `archiwum/podglad-agent-wariant-redakcyjna-podglad`
- Web-Core: `podglad-agent-wariant-zwarta-podglad` → `archiwum/podglad-agent-wariant-zwarta-podglad`
- Web-Core: `robocza-aktualnosci` → `archiwum/robocza-aktualnosci`
- Web-Core: `robocza-instytut` → `archiwum/robocza-instytut`
- Web-Core: `robocza-nauka-podstrony` → `archiwum/robocza-nauka-podstrony`
- Web-Core: `robocza-nauka-tekst` → `archiwum/robocza-nauka-tekst`
- Web-Core: `robocza-studia` → `archiwum/robocza-studia`
- Web-Core: `wariant-portal` → `archiwum/wariant-portal`
- Web-Core: `wariant-redakcyjna` → `archiwum/wariant-redakcyjna`
- Web-Core: `wariant-zwarta` → `archiwum/wariant-zwarta`
- Web-Core: `wyglad/en` → `archiwum/wyglad/en`
- Web-Core: `wyglad/porzadki` → `archiwum/wyglad/porzadki`
- Web-Core: `wyglad/porzadki-01-telefon` → `archiwum/wyglad/porzadki-01-telefon`
- Web-Core: `wyglad/porzadki-02-szablon` → `archiwum/wyglad/porzadki-02-szablon`
- Web-Core: `wyglad/porzadki-03-podstrony` → `archiwum/wyglad/porzadki-03-podstrony`
- Web-Core: `wyglad/zalozyciele` → `archiwum/wyglad/zalozyciele`
- Web-Core: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Podglad: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Podglad: `markdown-jawne-bloki-2026-11` → `archiwum/markdown-jawne-bloki-2026-11`
- Web-Pracownicy: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Analiza-Harmoniczna: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Dydaktyka: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Dyskretna-Analiza-Harmoniczna: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Geometria: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Prawdopodobienstwo: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Rownania-Rozniczkowe: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Rownania-Rozniczkowe: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Sem-Statystyka: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Statystyka: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Sem-Statystyka: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Sem-Teoria-Modeli: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Teoria-Modeli: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Sem-Teoria-Modeli: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Sem-Topologia: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Sem-Topologia: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Sem-Topologia: `test-cms` → `archiwum/test-cms`
- Web-Sem-Topologia: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Spec-Aktuarialno-Finansowa: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Spec-Aktuarialno-Finansowa: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Spec-Aktuarialno-Finansowa: `test-cms` → `archiwum/test-cms`
- Web-Spec-Aktuarialno-Finansowa: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Spec-Analiza-Danych: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Spec-Analiza-Danych: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Spec-Analiza-Danych: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Spec-Nauczycielska: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Spec-Nauczycielska: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Spec-Nauczycielska: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Spec-Stosowana: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Spec-Stosowana: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Spec-Stosowana: `test-cms` → `archiwum/test-cms`
- Web-Spec-Stosowana: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Spec-Teoretyczna: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Spec-Teoretyczna: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Spec-Teoretyczna: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`
- Web-Ustawienia: `agent-nauka-podglad` → `archiwum/agent-nauka-podglad`
- Web-Ustawienia: `cms-reorganizacja-2026-11` → `archiwum/cms-reorganizacja-2026-11`
- Web-Ustawienia: `kopia/2026-11-06` → `archiwum/kopia/2026-11-06`
- Web-Ustawienia: `kopia/test-cms-zlecenie-22` → `archiwum/kopia/test-cms-zlecenie-22`
- Web-Ustawienia: `robocza-nauka-tekst` → `archiwum/robocza-nauka-tekst`
- Web-Ustawienia: `robocza-studia` → `archiwum/robocza-studia`
- Web-Ustawienia: `test-cms` → `archiwum/test-cms`
- Web-Ustawienia: `wyglad/zlecenie-16` → `archiwum/wyglad/zlecenie-16`

## Etap 2 — STOP: czekam na „push”

**Na GitHubie nic jeszcze nie zmieniłem.** Lokalnie, na gałęzi `praca/38-porzadki`, czeka 1 commit: `6bf211e`. Archiwum pierwszej wersji wskazuje `222d5e4`, czyli obecny `main` z raportami, zrzutami i całą historią (także ze starym silnikiem).

### Jak szukałem nieużywanych plików
1. **Budowa z zapisem modułów.** Do zwykłej konfiguracji dołożyłem tymczasową wtyczkę Vite (plik `astro.config.z38.mjs`, już usunięty). Zapisywała każdy moduł, który Vite wczytał przy budowie: strony, komponenty, style, skrypty klienta i wyniki `import.meta.glob`. Wynik: **244 z 280 śledzonych plików w `src/` jest używanych.**
2. **Kontrola renderowania.** W tej samej budowie oznaczyłem każdy komponent `.astro` i zapisywałem, które z nich faktycznie wyrenderowały się na jakiejś stronie. Wynik: **wszystkie 135 komponentów, stron i widoków `.astro` renderuje się co najmniej na jednej z 757 stron.** Pozostałości pierwszej wersji wymienione w zleceniu (14 komponentów poza `zal/`, 33 widoki) są dziś wszystkie używane przez „Założycieli”. Style `portal.css`, `uklad-portal.css` i `uklad-zwarta.css` wchodzą do arkuszy wynikowych. Ich usunięcie zmieniłoby CSS, więc zostają.
3. **Analiza statyczna** modułów ładowanych przez Node: importy z `astro.config.mjs`, `content.config.ts`, testów wtyczek i skryptów. Dodatkowo `url()` w CSS: `tlo.css` używa wszystkich plików z `src/assets/tlo/` i `src/assets/naglowki/`, których zapis modułów nie widzi. Oprócz tego odwołania w workflowach Web-Core i Web-Podglad, w `dok/` i README.

### Usunięte z `main` (640 plików)

| Folder | Pliki |
|---|---|
| `/` | `raport-zrzuty/` (613 plików, 164 MB), 21 plików `RAPORT-*.md`, `PYTANIA.md`, `wyglad-podstron.json` |
| `src/dev/` | `panel-wariantow.ts` (cały folder) |
| `src/plugins/` | `panel-wariantow.mjs` |
| `src/styles/` | `test-warianty.css` |
| `skrypty/` | `warianty.py` |

Zmienione:
- `astro.config.mjs`: bez importu panelu i przełącznika `PANEL_WARIANTOW`;
- `.github/workflows/deploy.yml`: bez kroku „Warianty wyglądu (gałęzie `wariant-*`)”, który wywoływał `warianty.py`. Budowanie, publikacja i pozostałe kroki bez zmian; YAML sprawdzony parserem.
- `.gitignore`: `/raport-zrzuty/`, `/RAPORT-*.md`, `/PYTANIA.md`;
- `README.md`: nowa sekcja „Archiwa” (pierwsza wersja, raporty, znaczniki gałęzi);
- `dok/start-strony.md`: odwołanie do raportu 22 kieruje do archiwum;
- lokalnie `.przekazanie\zlecenia\zasady.md`: nowa sekcja „Raporty i zrzuty tylko lokalnie”.

Odwołania do `RAPORT-…md` w komentarzach kodu (np. `Fonty.astro`, `zalozyciele.css`) zostawiłem bez zmian. README wyjaśnia, że dotyczą wersji w archiwum.

### Poza grafem, ale zostają (do decyzji)
- `.github/qa/` (2 pliki) i `skrypty/szerokosci/` (3 pliki): po usunięciu `qa.yml` nic ich nie używa. To pytanie 2 z etapu 1; domyślnie zostają.
- `skrypty/migracja/` (8 plików): zlecenie 31 jeszcze nie jest na `main`, a druga sesja ma lokalnie zmieniony `formularze.py`. Zgodnie ze zleceniem usuniemy ten folder później, osobnym commitem.
- `src/assets/szkice/*.svg` i `ZRODLA.md` (13 plików): źródła `szkice.json`, którego używają animacje patronów. Budowa ich nie czyta, ale to materiał źródłowy obecnego wyglądu, więc zostawiłem.
- `src/data/ciekawostki/README.md`: opis danych dla redaktorów.
- `dok/latki/` (22 pliki) i `dok/en/` (`POSTEP.md`, `TLUMACZENIA.md`, 17 łatek): to łatki do repozytoriów treści ze zleceń 11–20 (już nałożone) i opis tamtej pracy. Odwołują się tylko do siebie nawzajem i do raportów. Zlecenie każe `dok/` aktualizować, nie usuwać, więc zostały. **Czy usunąć je razem z raportami?**

### Kontrola: identyczny wynik budowy
- **Te same klony treści:** `tresci-B`, 16 repozytoriów z `tresci.json` na `main` (SHA w `raport-zrzuty/z38-tresci-sha.txt`), nałożone w `Web-Core-B` przez `pobierz_tresci.py --lokalnie ../tresci-B`. W `Web-Core` nie uruchamiałem niczego.
- **Budowy:** `npm run build` (Astro i `pagefind`) jedna po drugiej: przed (`222d5e4`) o 00:56, po o 00:57.

| | Przed | Po |
|---|---:|---:|
| Pliki w `dist/` | 5585 | 5585 |
| Strony | 757 | 757 |
| Czas `npm run build` | 30 s | 29 s |

Wynik porównania `dist/`:
- **HTML: 757 plików identycznych bajt w bajt**, normalizacja nie była potrzebna;
- **CSS (15) i JS (33): identyczne**; tak samo `sitemap.xml`, `rss.xml`, `robots.txt` i cały `pagefind` (779 plików);
- 112 plików `.ics` i `seminaria/powiadomienia.json` różnią się **wyłącznie znacznikiem czasu budowy**: `DTSTAMP` (`new Date()` w `src/lib/kalendarz.ts`) i polem `wygenerowano`. Po pominięciu tych pól: **0 różnic**;
- pozostałe pliki (obrazy, PDF, fonty): identyczne.

Inne kontrole:
- `astro check`: przed 0 błędów, 0 ostrzeżeń, 3 podpowiedzi (231 plików); po 0 błędów, 0 ostrzeżeń, 3 podpowiedzi (229 plików).
- Testy wtyczek (`npm run test:jawne`, 3 pliki `*.test.mjs`): przed i po 47/47.
- Po porównaniu zmieniłem w commicie tylko opis znacznika w `README.md`, `.gitignore` i `dok/start-strony.md`. `src/`, `astro.config.mjs` i `package.json` są identyczne z wersją, którą budowałem.

### Rozmiar

| | Przed (`222d5e4`) | Po (`6bf211e`) |
|---|---:|---:|
| Śledzone pliki | 1006 | 366 |
| Ich rozmiar | 38,1 MB | 3,9 MB |
| Płytki klon (`--depth 1`): `.git` + pliki | 328 MB (159 + 169) | **6,3 MB** (1,8 + 4,6) |

Pełny klon dalej waży ok. 159 MB, bo historia zostaje (bez przepisywania). Rozmiar pierwszego wiersza (1006 plików) to stan już po commitach z etapu 1; zlecenie podawało 1008.

### Ważne poza zleceniem: Podgląd się nie buduje od 17.11, 22:12
Od 17.11, 22:12 zakończyły się błędem 3 przebiegi „Podgląd nowego wyglądu” w Web-Podglad. Przyczyna to treść, nie kod. Wpis `Web-Aktualnosci/src/content/aktualnosci/2026-11-16-.md`, zapisany przez Pages CMS, ma w `zalaczniki` pustą pozycję `- {}`. Schemat wymaga pola `plik`, więc budowa kończy się błędem `InvalidContentEntryDataError`. Dodatkowo nazwa pliku `2026-11-16-.md` jest bez tytułu, a obok są `-1` i `-2`.

Do porównania przed/po usunąłem tę pustą pozycję **tylko w moim klonie** `tresci-B` (bez commita i bez pushu). Obie budowy miały więc tę samą treść. Naprawa nie należy do tego zlecenia. Możliwości:
- (a) usunąć pustą pozycję w CMS;
- (b) w `content.config.ts` pomijać puste załączniki;
- (c) jedno i drugie.

Możliwe, że dotyczy tego linia CMS drugiej sesji.

### Po „push” zrobię, w tej kolejności
1. `git fetch`. Jeśli `main` się zmienił (np. zlecenie 31 drugiej sesji), robię `rebase` i **powtarzam budowę przed/po i porównanie na nowej bazie**. Ewentualne konflikty z plikami drugiej sesji rozwiązuję bez usuwania jej zmian.
2. Wypycham `archiwum/pierwsza-wersja` jako **znacznik** wskazujący `222d5e4`, tak jak pozostałe archiwa. Jeśli wolisz gałąź, zgodnie z dosłownym punktem 2.1 zlecenia, napisz to przy „push”. Gałąź jednak łamie kryterium „tylko `main`”.
3. Zwykły push `6bf211e` na `main`, bez force. Kontrola `ls-remote`: dalej tylko `main`, znacznik ma wskazywać `222d5e4`.
4. Cofam lokalną łatkę w `tresci-B/Web-Aktualnosci`.

**Uwaga dla drugiej sesji i dla `Web-Core`:** po przejściu `Web-Core` na nowy `main` git usunie z niego śledzone dotąd raporty i zrzuty. Kopie lokalne można potem odtworzyć jako pliki ignorowane. Polecenie sprawdziłem na kopii; uruchamia się w `C:\Users\Szymek\Documents\GitHub\Web-Core`:

```bash
git archive archiwum/pierwsza-wersja raport-zrzuty PYTANIA.md $(git ls-tree --name-only archiwum/pierwsza-wersja | grep '^RAPORT-') | tar -x
```

Druga sesja nie powinna commitować nowych `RAPORT-*.md`. Po pushu `.gitignore` je pominie, a zasady już to mówią.

**Raport 31 w gałęzi drugiej sesji.** W `Web-Core` gałąź `praca/31-galeria-daty-nazwy` ma zacommitowany `RAPORT-ZLECENIE-31.md`. Na `origin/main` go nie ma. Jeśli 31 trafi na `main` przed moim pushem, raport też tam wejdzie. Wtedy przy `rebase` dołożę jego usunięcie z `main`: plik zostanie w historii, a kopia lokalna w `Web-Core`. Lepiej, żeby druga sesja wypchnęła 31 już bez raportu.

## Etap 2 — wykonany po „push” (18.11.2026)
- `git fetch` przed pushem: `origin/main` = `222d5e4`, bez zmian od porównania. Nie trzeba było robić `rebase` ani powtarzać budowy.
- **Znacznik `archiwum/pierwsza-wersja`** (z opisem) wskazuje `222d5e4`. Wypchnięty i sprawdzony przez `ls-remote`. Zawiera 635 plików raportów i zrzutów: `raport-zrzuty/` (613), 21 plików `RAPORT-*.md` i `PYTANIA.md`. Lokalną gałąź o tej nazwie usunąłem, żeby nie myliła się ze znacznikiem.
- **`main` Web-Core: `222d5e4..6bf211e`**. Zwykły push z przewinięciem (fast-forward), bez force. Na `main` jest teraz 366 plików, bez żadnego raportu ani zrzutu. Workflowy: `deploy.yml`, `plan-zajec.yml`, `podglad-przekaznik.yml`.
- **Kontrola `ls-remote` we wszystkich 23 repozytoriach:** wszędzie tylko `main`, w Web-Podglad także `zbudowana`.
- Lokalna łatka w `tresci-B/Web-Aktualnosci` (pusta pozycja załącznika) jest cofnięta; klon jest czysty.

### Kryteria odbioru
- [x] We wszystkich repozytoriach IM-UWr tylko `main` (oraz `zbudowana` w Web-Podglad); każda usunięta gałąź ma znacznik `archiwum/…`. Sprawdzone przez `ls-remote`.
- [x] `archiwum/pierwsza-wersja` zawiera dawny `main` w całości. To **znacznik** na `222d5e4`, nie gałąź, zgodnie z kryterium „tylko `main`”.
- [x] Na `main` Web-Core nie ma raportów, zrzutów ani plików, których budowa nie używa; `.gitignore` je pomija. Wyjątki są opisane wyżej w „Poza grafem, ale zostają (do decyzji)”.
- [x] Budowa przed i po daje identyczny wynik: 0 różnic w HTML, CSS i JS. W `.ics` i `powiadomienia.json` różni się tylko znacznik czasu budowy.
- [x] Usunięte workflowy gałęzi roboczych; `deploy.yml`, przekaźnik i plan zajęć zostają.
- [x] Bez force-push i bez przepisywania historii.

### Co zostało
- Odpowiedzi na pytania:
  - `markdown-jawne-test.yml` w Web-Podglad;
  - `.github/qa/` i `skrypty/szerokosci/`;
  - `dok/latki/` i `dok/en/`.
- Usunięcie `skrypty/migracja/`, gdy zlecenie 31 będzie na `main` (osobny commit).
- **Podgląd nie buduje się od 17.11, 22:12**: pusty załącznik w `Web-Aktualnosci/2026-11-16-.md`. To poza zleceniem 38.
- Gdy `Web-Core` przejdzie na nowy `main`, odtworzyć lokalne kopie raportów poleceniem `git archive` (wyżej).
- Lokalnie do skasowania, gdy będzie wygodnie: w `tresci-B` są `z38-dist-przed` i `z38-dist-po` (po ok. 255 MB) oraz logi `z38-*`.
- Propozycje dotyczące starych folderów (etap 1) bez zmian. Niczego tam nie usunąłem.

## Po zleceniu: naprawa Podglądu (18.11.2026, za zgodą właściciela)
- `Web-Aktualnosci` `cc6a7b0`: w `src/content/aktualnosci/2026-11-16-.md` usunięta pusta pozycja `- {}` w `zalaczniki` (zapis z Pages CMS bez pola `plik`). Załącznik ze slajdami został.
- Lokalna budowa z poprawioną treścią na `main` Web-Core `6bf211e`: 757 stron, bez błędów.
- Podgląd: przebieg [44205492784](https://github.com/IM-UWr/Web-Podglad/actions/runs/44205492784) `build` i `deploy` zakończone sukcesem (00:09–00:15 UTC). Strona wpisu na `https://im-uwr.github.io/Web-Podglad/aktualnosci/2026-11-16-/` odpowiada 200 i ma link do PDF.

## Dopisek (18.11.2026, tryb samodzielny)
- **Gałęzie:** zgodnie z decyzją właściciela wszystkie są zarchiwizowane jako znaczniki `archiwum/…`. `archiwum/pierwsza-wersja` też jest znacznikiem. Przyjąłem znacznik, bo kryterium odbioru mówi „tylko `main`”.
- **`skrypty/migracja/` zostaje na razie na `main`, choć zlecenie 31 jest już wypchnięte.** Zlecenie 31 dodało tam `kontrola_redaktorow.py`, `termin.py` i `formularze_31.py`. To narzędzia kontroli „Ochrona zmian redaktorów”, z których druga sesja korzysta w kolejnych zleceniach CMS (39, 33, 40). Usunięcie ich teraz utrudniłoby jej pracę.
  - **Pytanie:** czy usunąć cały folder po zleceniu 40, czy przenieść kontrolę redaktorów do `skrypty/` jako narzędzie stałe, a resztę usunąć?
