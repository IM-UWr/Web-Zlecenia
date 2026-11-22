# Zlecenie 68 (23.11.2026): minione referaty na stronie seminarium według lat akademickich

**Skąd to zlecenie.** 22–23.11 czat przygotował archiwum referatów ze starej strony: **1294 referaty z lat 2014–2026** w 8 repozytoriach `Web-Sem-*`, opisane w projekcie w `claude/archiwum-seminariow.md`. Strona seminarium (`/seminaria/<id>`) pokazuje dziś wszystkie minione referaty jednym ciągiem. Po dodaniu archiwum robi się z tego bardzo długa lista:

| Seminarium | Minione na stronie | Rozmiar HTML |
|---|---|---|
| Dyskretna analiza harmoniczna | ok. 260 | ok. 880 KB |
| Geometria | ok. 240 | ok. 270 KB |
| Analiza harmoniczna | ok. 230 | ok. 215 KB |
| Topologia | ok. 157 | ok. 420 KB |
| Prawdopodobieństwo | ok. 147 | ok. 660 KB |

Kalendarz (archiwum) urósł do ok. 1,3 MB.

**Decyzja właściciela (23.11, 00:01–00:07):** przyjął propozycję czatu, czyli minione referaty w sekcjach według lat akademickich ze spisem lat w „Na tej stronie”, tak jak lista obron w zleceniu 57. Polecenie: „daj zlecenie dla code”.

## Zasady pracy
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- **Tylko Web-Core.** Repozytoriów treści nie zmieniasz.
- Raport `RAPORT-ZLECENIE-68.md`, zrzuty `raport-zrzuty/z68-*`. Bez subagentów.
- **Kolejność:** jeśli inne otwarte zlecenie zmienia `Seminarium.astro`, `widoki/seminarium.ts` albo `TytulReferatu.astro`, to zlecenie robisz po nim.
- **Numer:** czat pisał to zlecenie najpierw jako „60”. Code w międzyczasie doszedł do numeru 66 (w historii Web-Core są zlecenia 65 i 66), więc to jest **67**. Jeśli 67 jest już zajęte, weź pierwszy wolny numer i zmień nazwę pliku. **Numer 67 okazał się zajęty (67 = instrukcje dla redaktorów w PDF), więc to zlecenie ma numer 68** (Code, 23.11).

## Dane do testów
Najpierw `python3 skrypty/pobierz_tresci.py`.
- **Archiwum już jest na `main`:** po wypchnięciu przez czat strona seminarium DAH ma ok. 260 minionych referatów. Wtedy to wystarczy.
- **Archiwum jeszcze nie ma na `main`:** rozpakuj `67-tresci-archiwum.zip` z folderu zlecenia, np. do `.przekazanie\robocze\67-tresci\`. W środku jest 8 katalogów `Web-Sem-*`, każdy z `src/`, `public/` i `.pages.yml`. Nałóż je na Web-Core:
  ```
  python3 skrypty/pobierz_tresci.py --zrodlo Web-Sem-Analiza-Harmoniczna=<katalog>\Web-Sem-Analiza-Harmoniczna --zrodlo Web-Sem-Dyskretna-Analiza-Harmoniczna=<…> --zrodlo Web-Sem-Geometria=<…> --zrodlo Web-Sem-Prawdopodobienstwo=<…> --zrodlo Web-Sem-Rownania-Rozniczkowe=<…> --zrodlo Web-Sem-Statystyka=<…> --zrodlo Web-Sem-Teoria-Modeli=<…> --zrodlo Web-Sem-Topologia=<…>
  ```
  Na koniec przywróć zwykłą nakładkę (`pobierz_tresci.py` bez opcji). Katalogu z paczką nie dodawaj do gita.
- Próbna budowa z tymi treściami przeszła w czacie (959 stron, 0 błędów, 0 błędów KaTeX).

## Stan dziś (`src/views/Seminarium.astro`, `src/lib/widoki/seminarium.ts`)
- **Spis:** `spis` ma dwie pozycje: `z-nadchodzace` i `z-minione`.
- **Sekcja `#z-minione`** (po zleceniu 65, commit `629c820`, 22.11):
  - `h2#h-min` „Minione referaty” / „Past talks”;
  - pod nim jedna siatka `div.ref-dwie` z płaską listą `article.ref.maly` od najnowszego, na komputerze w dwóch kolumnach, jak minione Konferencje;
  - tytuł referatu w `h3`, streszczenie zwinięte w `<details name="streszczenie-minione">`, więc rozwinięte jest jedno naraz;
  - rozwinięte streszczenie zajmuje cały rząd, a skrypt na dole pliku (`document.querySelector('.ref-dwie')`) ustawia `order`, żeby sąsiad zszedł pod nie; kliknięty wiersz zostaje w tym samym miejscu ekranu;
  - pliki w `ul.pliki`;
  - na końcu link `p.archiwum` (pole `archiwum` seminarium).
- **Kotwice referatów:** `id={slugOf(r.id)}`. Prowadzą do nich Kalendarz i lista seminariów, więc **muszą zostać bez zmian**.
- **`daneSeminarium()`** zwraca `minione` jako płaską tablicę.

## Docelowo
1. **Lata akademickie w „Minionych”.**
   - Rok akademicki zaczyna się 1 października: referat z 15.09.2025 należy do 2024/25, a z 1.10.2025 do 2025/26.
   - Każdy rok to `h3 id="rok-RRRR-RR"` (np. `rok-2025-26`) z tekstem „2025/26”, potem `<span class="sr-only">, </span>` i `<small>` z liczbą.
   - Liczba z odmianą: PL „1 referat / 2 referaty / 5 referatów / 22 referaty”, EN „1 talk / 2 talks”.
   - Wygląd roku i liczby jak `h3`/`small` lat w Konferencjach i Obronach (zlecenie 57).
   - Lata od najnowszego, w roku referaty od najnowszego (jak dziś).
   - Pierwszy rok to bieżący rok akademicki, jeśli ma już minione referaty (dziś 2026/27).
2. **Układ ze zlecenia 65 zostaje w każdym roku.**
   - Każdy rok ma własną siatkę `div.ref-dwie` (dwie kolumny na komputerze, jedna na telefonie).
   - Skrypt `order` i „kliknięty wiersz zostaje w miejscu” mają działać w każdej siatce: `querySelectorAll` zamiast `querySelector`, nasłuch `toggle` na każdej.
   - `details name="streszczenie-minione"` zostaje wspólne dla całej strony, więc rozwinięte jest jedno streszczenie na stronie, także między latami.
3. **Tytuł referatu w minionych to `h4`** (bo stoi pod `h3` roku).
   - Wygląd wiersza ma zostać dokładnie jak dziś (po zleceniu 65): data, etykieta, tytuł Brygadą, prelegent, „Streszczenie” w `details`, pliki, przygaszenie minionych. Przejrzyj selektory CSS, które celują w `.ref h3`, i porównaj obliczone style.
   - Nadchodzące zostają bez zmian, z tytułem w `h3`.
4. **Spis „Na tej stronie”:**
   - kolejność: „Nadchodzące referaty” (`#z-nadchodzace`), „Minione referaty” (`#z-minione`), potem lata od najnowszego (`#rok-RRRR-RR`, etykieta „2025/26”);
   - lata wyliczane z danych, bez listy wpisanej na sztywno;
   - jeśli `Podstrona`/spis obsługuje wcięcie podpozycji, lata mogą być wcięte pod „Minione”; jeśli nie, zostaw płasko jak w Konferencjach;
   - nie dodawaj nowego mechanizmu tylko po to;
   - na telefonie spis zwija się jak dziś.
5. **Mało referatów:** jeśli seminarium ma minione tylko z jednego roku akademickiego, nie rób podziału ani pozycji lat w spisie (wygląd jak dziś, np. Dydaktyka).
6. **Link „archiwum”** (`p.archiwum`) zostaje na końcu sekcji „Minione”, pod ostatnim rokiem.
7. **Wersja angielska** (`/en/seminaria/<id>`): te same lata i ten sam zapis „2025/26”, liczby po angielsku.
8. **Komentarz na górze `Seminarium.astro`** opisuje nowy układ (zlecenie 68).

**Wskazówka (nie przepis):** w `daneSeminarium()` dodaj np. `lataMinionych: { rok: string, id: string, lista: … }[]`, jak `daneListyKonferencji()`. Funkcję roku akademickiego (1.10) wstaw tam, gdzie pasuje (np. `src/lib/daty.ts`), i sprawdź, czy podobnej już nie ma (Plan zajęć ma rok od 1.08, zlecenie 43, i to inna reguła).

## Poza zmianą, tylko pomiar i raport
- **Rozmiar stron seminariów** po zmianie (PL i EN). Jeśli któraś przekracza 1 MB, wypisz to i zaproponuj rozwiązanie, ale go nie wdrażaj.
- **Kalendarz → Archiwum** (ok. 1,3 MB): przewiń na telefonie (390 px, emulacja słabszego CPU ×4) i opisz, czy coś przycina. Bez zmian w kodzie.
- **Lista seminariów:** liczba „referaty w archiwum” w banerze ma się zgadzać z sumą minionych.

## Odbiór lokalny
- **Zrzuty** stron `/seminaria/dyskretna-analiza-harmoniczna`, `/seminaria/geometria` (ma kilka nadchodzących) i `/seminaria/statystyka` (mało referatów), oraz jedna strona EN:
  - 1920×1080, 1440×900, 1024 i 390 px, jasny i ciemny;
  - góra strony, przejście Nadchodzące → Minione, przejście między dwoma latami i koniec listy (2014).
- **Spis:** klik w rok przewija do `h3`, a znacznik spisu podąża za przewijaniem. Sprawdź myszą i klawiaturą.
- **Kotwice:**
  - link do referatu z Kalendarza (`/seminaria/<id>#<slug>`) dalej trafia w wiersz;
  - sprawdź 3 referaty z różnych lat, w tym jeden z 2014.
- **Wiersz:** `getComputedStyle` daty, etykiety, tytułu, prelegenta, „Streszczenie” i pliku są równe tym sprzed zmiany, na komputerze i telefonie.
- **Dwie kolumny (zlecenie 65) w kilku latach:** rozwiń streszczenie w prawej kolumnie w dwóch różnych latach. Za każdym razem zajmuje cały rząd, sąsiad schodzi pod nie, poprzednie się zwija, a kliknięty wiersz nie ucieka spod kursora. Zrzut 1440×900.
- **Kontrole:**
  - `astro check` bez nowych błędów;
  - `sprawdz_tresci.py` OK;
  - konsola czysta;
  - indeks wyszukiwarki obejmuje referaty jak dotąd.
- **Reszta `dist` bez zmian** poza `/seminaria/<id>` (PL i EN), nazwami plików CSS/JS i indeksem wyszukiwarki.
- **Stop:** raport i czekanie na „push”. Push dotyczy tylko Web-Core.

## Kryteria odbioru
- [ ] Na stronach seminariów z wieloma latami minione referaty są podzielone na lata akademickie (`h3#rok-RRRR-RR` z liczbą w poprawnej odmianie PL i EN). Kolejność: od najnowszego.
- [ ] Spis „Na tej stronie” ma Nadchodzące, Minione i lata.
- [ ] Seminarium z minionymi z jednego roku wygląda jak dziś.
- [ ] Wiersze referatów wyglądają jak przed zmianą. Układ dwóch kolumn i rozwijanie streszczeń ze zlecenia 65 działa w każdym roku. Kotwice `#<slug>` działają.
- [ ] Inne strony bez zmian. Repozytoria treści bez zmian.
- [ ] Raport zawiera rozmiary stron i ocenę płynności Kalendarza.
