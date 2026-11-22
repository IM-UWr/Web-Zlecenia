# Zlecenie 43: plan zajęć pokazuje cały rok akademicki (zmiana 1 sierpnia); harmonogramy GitHub bez wyłączania po 60 dniach; logo UWr prowadzi na uwr.edu.pl (18.11.2026)

**Decyzje właściciela (18.11.2026):**
- **02:04:** „Zróbmy, żeby na początku sierpnia zmieniały się oba. Nowy zimowy i nowy letni.”
  - Plan zajęć ma zawsze dwie zakładki: semestr zimowy i letni **tego samego roku akademickiego**.
  - 1 sierpnia obie zakładki przechodzą na następny rok akademicki.
- **02:07:** dołączyć ochronę przed wyłączaniem harmonogramów przez GitHub po 60 dniach (etap 2).
- **02:08–02:09:** logo UWr („orzełki”) w pasku na stronie głównej i na podstronach ma prowadzić na stronę główną UWr (etap 3).

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`.
- Praca na lokalnej gałęzi roboczej, push dopiero po „push”.
- Raport w `RAPORT-ZLECENIE-43.md`. Bez subagentów.
- **Kolejność (18.11, 12:04):** okno 2, na końcu, po zleceniu 44. Etap 2 zmienia `podglad.yml` w Web-Podglad, tak jak zlecenie 33 (okno 1): przed pushem `git fetch` i rebase na `origin/main` Web-Podglad, zmiany zlecenia 33 zostają.
- Etapy są niezależne; każdy ma osobny commit.

# Etap 1. Plan zajęć: rok akademicki od 1 sierpnia

## Stan dziś
- `skrypty/plan/pobierz_plan.py`, funkcja `wybierz_semestry()`:
  - bez `--semestr` bierze z USOS (`terms/terms_index`) ostatni rozpoczęty semestr i najbliższy przyszły (`rozpoczete[-1:] + przyszle[:1]`);
  - gdy API nie odpowiada, `semestry_z_kalendarza()` liczy to samo z kalendarza (zimowy X–I, letni od 20 lutego).
- Skutek, którego właściciel nie chce:
  - od startu letniego (24.02.2027) zakładki to Letni 2026/27 i Zimowy 2027/28;
  - od października 2027: Zimowy 2027/28 i Letni 2027/28.
- Strona:
  - zakładki to semestry z `src/data/plan/plan.json`;
  - aktywną zakładkę wybiera `wybierzSemestr()` (`src/components/wyborSemestru.ts`): trwający semestr, w przerwie najbliższy następny, a gdy takiego nie ma, ten, który kończy się najpóźniej.

## Zmiana
1. **Rok akademicki zamiast pary „bieżący + następny”.** Bez `--semestr` skrypt wybiera `R/RR-Z` i `R/RR-L` jednego roku akademickiego:
   - od 1 sierpnia roku R włącznie (czas `Europe/Warsaw`, czyli `STREFA`) jest to rok R/(R+1);
   - przed 1 sierpnia jest to rok (R−1)/R;
   - dzień zmiany jest jedną stałą na górze pliku z komentarzem, np. `ZMIANA_ROKU = (8, 1)  # miesiąc, dzień`.
2. **Nazwy i daty** obu semestrów pochodzą z `terms/terms_index`, jak dziś.
   - Jeśli semestru jeszcze nie ma w USOS, skrypt nie zgłasza błędu. Zapisuje wpis z nazwą z `nazwa_semestru()` i pustymi datami.
   - Strona pokaże wtedy zakładkę z napisem „Plan na ten semestr nie jest jeszcze dostępny w USOS”.
3. **Ta sama reguła w trybie awaryjnym** (`semestry_z_kalendarza()`, gdy API nie odpowiada). W pliku najpierw zimowy, potem letni.
4. **`--semestr` bez zmian:** ręczne wskazanie wygrywa.
5. **Opisy do poprawienia:**
   - nagłówek skryptu („Domyślnie pobierany jest…”);
   - `--help`;
   - komentarze w `.github/workflows/plan-zajec.yml`, jeśli o tym wspominają.
6. **Bez zmian:**
   - `wybierzSemestr()`; w raporcie tylko potwierdź tabelą niżej, że przy parze z jednego roku wybiera dobrze;
   - zachowywanie poprzednich danych, gdy USOS nie odpowiada. Dotyczy tylko semestrów z wybranej pary; semestr spoza pary znika z `plan.json`.

## Odbiór etapu 1
**Test bez sieci.** Wywołaj wybór semestrów dla dat z tabeli w dwóch wariantach:
- na zapisanej odpowiedzi `terms_index` (zrzut do pliku testowego);
- w trybie awaryjnym (kalendarz).

Wynik wpisz do raportu. Kolumna „Aktywna” to wynik `wybierzSemestr()` na datach z USOS.

| Dzień | Zakładki | Aktywna |
|---|---|---|
| 18.11.2026 | Zimowy 2026/27, Letni 2026/27 | Zimowy 2026/27 |
| 10.02.2027 (przerwa) | Zimowy 2026/27, Letni 2026/27 | Letni 2026/27 |
| 24.02.2027 | Zimowy 2026/27, Letni 2026/27 | Letni 2026/27 |
| 15.07.2027 (po zajęciach) | Zimowy 2026/27, Letni 2026/27 | Letni 2026/27 |
| 31.07.2027 | Zimowy 2026/27, Letni 2026/27 | Letni 2026/27 |
| 01.08.2027 | Zimowy 2027/28, Letni 2027/28 | Zimowy 2027/28 |
| 01.10.2027 | Zimowy 2027/28, Letni 2027/28 | Zimowy 2027/28 |

**Pozostałe sprawdzenia:**
- Prawdziwe pobranie dziś (`python3 skrypty/plan/pobierz_plan.py`): treść `plan.json` bez zmian, bo dziś para to i tak Zimowy i Letni 2026/27.
- `astro check` bez nowych błędów.
- Strona Plan zajęć i kafelek „Plan zajęć” na stronie głównej wyglądają jak dziś.

# Etap 2. Harmonogramy GitHub nie wyłączają się po 60 dniach

## Problem
GitHub w repozytoriach publicznych automatycznie wyłącza zaplanowane workflowy (`on: schedule`), gdy w repozytorium przez 60 dni nie było aktywności. Przy wyłączeniu nic się nie psuje widocznie, tylko po cichu staje.
- **Web-Core, `plan-zajec.yml`** (3 razy dziennie):
  - commituje tylko wtedy, gdy plan w USOS się zmienił;
  - latem albo po zakończeniu prac nad kodem łatwo o 60 dni ciszy;
  - wtedy plan przestaje się pobierać, a 1 sierpnia nie przejdzie na nowy rok.
- **Web-Podglad, `podglad.yml`** (cron co godzinę):
  - przebudowa codzienna odświeża wszystko, co zależy od daty: „Dziś”, nadchodzące wydarzenia, zakończone wydarzenia, kolor dnia;
  - po wyłączeniu strona odświeżałaby się tylko po zapisach w CMS.
- **Web-Core, `deploy.yml`:** wyłączony i **zostaje wyłączony**. Nie podtrzymuj go.
- Na początku etapu sprawdź, czy inne repozytoria IM-UWr nie mają `schedule`. Repozytoria treści mają dziś tylko `powiadom.yml`, uruchamiany przy zapisie, bez harmonogramu.

## Zmiana
1. **Podtrzymanie przez API, bez pustych commitów** (historia i repozytoria treści zostają czyste):
   - raz w tygodniu wywołaj `gh api -X PUT repos/<właściciel>/<repo>/actions/workflows/<plik>/enable` dla każdego zaplanowanego workflowu tego repozytorium;
   - może to być osobny krok w tym samym workflowie z warunkiem na dzień tygodnia albo osobny cron w tym samym pliku;
   - `permissions: actions: write`; `GITHUB_TOKEN` powinien wystarczyć, bez nowych sekretów.
2. **Przed wdrożeniem sprawdź w dokumentacji GitHub** (oraz np. jak robi to `keepalive-workflow` w trybie API), że takie wywołanie zeruje licznik 60 dni.
   - Jeśli nie zeruje albo wymaga innego tokenu, nie wdrażaj zgadywanego obejścia.
   - Opisz wtedy w raporcie możliwe rozwiązania i czekaj na decyzję.
3. **Ostrzeżenie zapasowe:**
   - jeśli krok podtrzymania się nie uda, przebieg kończy się widocznym błędem w Actions (nie `continue-on-error`);
   - zwykłe powiadomienie GitHub o nieudanym przebiegu trafi wtedy do właściciela.
4. **Krótki opis** w komentarzu na górze każdego zmienionego workflowu: po co jest podtrzymanie i co się stanie bez niego.

## Odbiór etapu 2
- Ręczne uruchomienie kroku podtrzymania w Web-Core i Web-Podglad kończy się sukcesem; w logu jest odpowiedź API (204).
- W raporcie:
  - lista wszystkich zaplanowanych workflowów IM-UWr z informacją, które są podtrzymywane;
  - termin następnego podtrzymania;
  - link do fragmentu dokumentacji, który potwierdza zerowanie licznika.
- Pozostałe kroki workflowów działają jak przedtem (porównanie logów przed i po).

# Etap 3. Logo UWr prowadzi na stronę główną UWr

**Uwaga (dopisane 18.11, 12:04):** to samo robi punkt 8 zlecenia 32 (okno 2, przed tym zleceniem). Najpierw sprawdź na świeżym `main`, czy logo już prowadzi na uwr.edu.pl w pasku i na okładce (PL i EN). Jeśli tak, nie zmieniaj kodu: zrób tylko odbiór etapu 3 i wpisz wynik do raportu. Popraw wyłącznie to, czego punkt 8 zlecenia 32 nie objął, a ten etap wymaga.

## Stan dziś (sprawdzone na Web-Podglad, gałąź `zbudowana`, 18.11, przez `elementFromPoint` na środku logo)
| Gdzie | Szerokość | Element | Kliknięcie w logo prowadzi do |
|---|---|---|---|
| Pasek menu na komputerze (drugi ekran strony głównej i wszystkie podstrony) | ≥ 1024 px | `a.z-marka` w `src/components/zal/PasekMenu.astro`: logo `.z-logo` i napis „Instytut Matematyczny / Wydział Matematyki i Informatyki” w jednym linku | strony głównej Instytutu ❌ |
| Okładka strony głównej, lewy górny róg | ≥ 1024 px | `a.z-okl-marka` w `src/components/zal/Okladka.astro`: logo `.z-okl-logo` i napis „Wydział Matematyki i Informatyki” w jednym linku | wmi.uwr.edu.pl ❌ |
| Nagłówek na telefonie | < 1024 px | `a.brand-uwr` | uwr.edu.pl ✅ (wzór) |

## Zmiana
1. **Pasek menu (`PasekMenu.astro`):** rozdziel `a.z-marka` na dwa linki obok siebie.
   - Logo prowadzi na `https://uwr.edu.pl/`, z `aria-label="Uniwersytet Wrocławski — strona główna UWr"`, tak jak `.brand-uwr` na telefonie.
   - Napis „Instytut Matematyczny / Wydział Matematyki i Informatyki” prowadzi na stronę główną Instytutu, jak dziś.
2. **Okładka (`Okladka.astro`):** rozdziel `a.z-okl-marka` w ten sam sposób.
   - Logo prowadzi na `https://uwr.edu.pl/`.
   - Napis „Wydział Matematyki i Informatyki” prowadzi na `https://wmi.uwr.edu.pl/`, jak dziś.
   - `sr-only` „(inna strona)” przy obu linkach na swoim miejscu (po nazwie, nie przed).
3. **Wygląd bez zmian:**
   - te same położenia, odstępy i kreska między logo a napisem;
   - zachowanie przy przewijaniu i na skalach 1024–1367 px (D1) bez zmian.
4. **Najechanie i fokus:** każdy link ma własne podświetlenie i własny widoczny fokus; Tab przechodzi najpierw przez logo, potem przez napis.
5. **Strzałka „↗” linku zewnętrznego:** przy logo jej nie ma (jak na telefonie).
6. **Wersja EN:** to samo. `aria-label` po angielsku, np. „University of Wrocław — UWr home page”.
7. **Telefon (`.brand-uwr`) bez zmian.**

## Odbiór etapu 3
- `elementFromPoint` na środku logo i na środku napisu: tabela jak wyżej, przed i po.
  - Strony: główna 1920×950 (okładka i drugi ekran po przewinięciu), `/instytut/wladze`, `/en/`, 1366×768, 1024×768 i 390×844.
- Zrzuty przed i po (te same okna): bez różnic pikselowych poza stanami najechania i fokusu.
- Tab od początku strony: kolejność fokusu w raporcie.

**Stop:** raport ze wszystkich trzech etapów i czekanie na „push”.

## Kryteria odbioru
- [ ] Zakładki planu to zawsze zimowy i letni jednego roku akademickiego; zmiana na następny rok 1 sierpnia.
- [ ] Ta sama reguła działa przy awarii USOS API.
- [ ] Brak semestru w USOS nie psuje pobrania (pusta zakładka z komunikatem).
- [ ] Dzień zmiany ustawia się w jednym miejscu.
- [ ] `--semestr` działa jak dziś.
- [ ] `plan-zajec.yml` i `podglad.yml` są podtrzymywane co tydzień przez API, bez pustych commitów; `deploy.yml` zostaje wyłączony.
- [ ] Nieudane podtrzymanie widać jako błąd przebiegu w Actions.
- [ ] Logo UWr na każdej szerokości (pasek, okładka, telefon) prowadzi na uwr.edu.pl; napisy obok prowadzą tam gdzie dziś.
- [ ] Wygląd bez zmian, osobny fokus dla logo i napisu.
