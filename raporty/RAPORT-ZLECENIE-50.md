# Raport: zlecenie 50, Aktualności bez zawieszania przy zmianie szerokości okna i niewidoczne linki w zamkniętym menu (18.11.2026)

**Status:** zrobione, sprawdzone lokalnie i wypchnięte (`0c07b56e`). Push automatyczny po odbiorze (polecenie właściciela 18.11: „50 tez z pushem”), zamiast „Stop: raport i czekanie na push” ze zlecenia.

| Repozytorium | Gałąź lokalna | Commit | Baza (HEAD na starcie) |
|---|---|---|---|
| Web-Core (worktree `Web-Core-B`) | `praca/50-aktualnosci-bez-zawieszania` | `0c07b56e` | `5dd156f5` = `origin/main` po zleceniu 49 |

Repozytoria treści bez zmian.

## Co jest zrobione
1. **`src/scripts/zal/czytaj-dalej.ts`, `czytajDalej`:** dwie fazy. Najpierw pętla samych odczytów: dla widocznych pozycji z zajawką para (zajawka, „ucięta”) z tym samym warunkiem `z.scrollHeight > z.clientHeight + 1`. Potem pętla samych zapisów: ten sam `span.wa-dalej` (`aria-hidden`, tekst dopisku) dopisany albo usunięty. Podpis funkcji, wywołania w `ListaAktualnosci.astro` i `ListaOfert.astro` oraz `czytajDalejNaBiezaco` bez zmian. Komentarz w pliku mówi, czemu dwie fazy i czemu wynik się nie zmienia (`.wa-dalej` ma `position: absolute`).
2. **`src/styles/zal-menu.css`, blok komputera:** w regule `.z-menu.zwijane section[data-dzial].rozwiniety .z-menu-grupy` jest `visibility: inherit` zamiast `visible`; reszta reguły bez zmian. Zamknięty panel (`visibility: hidden`) chowa teraz także rozwinięty dział.

`git diff --stat`: `czytaj-dalej.ts` +7 −1, `zal-menu.css` +1 −1. Nic więcej.

## Odstępstwa od zlecenia i powody
1. **Baza:** zlecenie podaje `3cde30e`, a gałąź wyszła z `5dd156f5` (main po zleceniach 46–49, które weszły wcześniej, tak jak przewiduje zlecenie). Przed pushem `git fetch`: `origin/main` = `5dd156f5`, więc rebase nie był potrzebny.
2. **Skoki 1076↔768:** najdłuższa klatka spadła 2,2–3× (z 0,16–0,25 s do 69–87 ms), a nie 5×. Przy tych skokach „przed” nie było zawieszenia; zostaje zwykłe przeliczenie strony na nowej szerokości. Ślad przeglądarki (niżej) nie pokazuje po zmianie ani jednego przeliczenia wymuszonego przez `czytaj-dalej`. Cel 5× dotyczy dużych skoków (1536↔1076, 1536↔768, 768↔1536) i tam jest 13,6–18,9×.
3. **LayoutCount przy skokach do 768 px:** 28 (przed 39–159), czyli trochę ponad „ok. 25”. Ślad: 14 zwykłych klatek bez stosu JS (razem ok. 35 ms) i 4 drobne odczyty z `PasekMenu` i `uloz` (strona Aktualności), po 0,2–0,4 ms. `czytaj-dalej`: 0. W pozostałych skokach 7–9.
4. **Pomiar powtórzony:** pierwsza wersja `pomiar50.mjs` czytała wyniki 1,5 s po zmianie i gubiła klatki „przed” dłuższe niż 1,5 s (np. 768→1536: 0 ms przy 135 przeliczeniach). Diagnoza (`diagnoza50.mjs`) pokazała, że długa klatka jest zawsze (1,45–1,75 s). Poprawiona wersja czeka 4 s i liczy klatki *zaczęte* w 1,5 s po zmianie. W tabeli są wyniki poprawionej wersji (`tresci-B/z50-pomiar2.*`); pierwszy przebieg (`z50-pomiar.*`) zostaje do wglądu.

## Odbiór lokalny
**Budowy** (`tresci-B/z50-budowa.sh`, te same klony treści w `tresci-B`): „przed” = czysty `5dd156f5` (23:03), „po” = ta sama gałąź z dwoma zmienionymi plikami (23:05). Serwowane `tresci-B/z49-serwer.py` na portach 4389 (przed) i 4390 (po). Przeglądarka: Edge (Chromium) 157.0.4341.60 przez Playwright.

### 1. Zmiana szerokości okna (`raport-zrzuty/z50-skrypt/pomiar50.mjs`, wynik `tresci-B/z50-pomiar2.json`)
Wysokość 800, każdy skok w świeżym kontekście, 3 powtórzenia. Klatka = najdłuższa klatka zaczęta w 1,5 s po zmianie (PerformanceObserver `long-animation-frame`), mediana i w nawiasie najgorsza próba; rAF = najdłuższa przerwa między `requestAnimationFrame` (mediana); LayoutCount = przyrost z CDP `Performance.getMetrics` (mediana).

| Strona | Skok | Klatka przed [ms] | Klatka po [ms] | Krócej | rAF przed | rAF po | LayoutCount przed | LayoutCount po |
|---|---|---|---|---|---|---|---|---|
| /aktualnosci/ | 1536→1076 | 1437 (1447) | 78 (92) | 18,4× | 1418 | 67 | 129 | 8 |
| /aktualnosci/ | 1076→1536 | 1459 (1514) | 82 (83) | 17,8× | 1435 | 67 | 128 | 7 |
| /aktualnosci/ | 1076→768 | 159 (160) | 71 (76) | 2,2× | 150 | 50 | 39 | 28 |
| /aktualnosci/ | 768→1076 | 219 (219) | 87 (91) | 2,5× | 200 | 67 | 20 | 9 |
| /aktualnosci/ | 1536→768 | 1032 (1040) | 76 (77) | 13,6× | 1017 | 67 | 159 | 28 |
| /aktualnosci/ | 768→1536 | 1560 (1579) | 103 (106) | 15,1× | 1551 | 83 | 139 | 7 |
| /en/aktualnosci/ | 1536→1076 | 1359 (1443) | 72 (83) | 18,9× | 1334 | 50 | 125 | 8 |
| /en/aktualnosci/ | 1076→1536 | 1420 (1459) | 83 (85) | 17,1× | 1401 | 67 | 124 | 7 |
| /en/aktualnosci/ | 1076→768 | 181 (184) | 69 (72) | 2,6× | 167 | 50 | 42 | 28 |
| /en/aktualnosci/ | 768→1076 | 254 (255) | 85 (92) | 3,0× | 234 | 67 | 23 | 9 |
| /en/aktualnosci/ | 1536→768 | 1066 (1089) | 73 (74) | 14,6× | 1051 | 50 | 158 | 28 |
| /en/aktualnosci/ | 768→1536 | 1653 (1794) | 98 (107) | 16,9× | 1635 | 83 | 138 | 7 |
| /aktualnosci/kariera/ | 1536→1076 | < 50 | < 50 | — | 17 | 17 | 15 | 8 |
| /aktualnosci/kariera/ | 1076→1536 | < 50 | < 50 | — | 17 | 17 | 13 | 6 |
| /aktualnosci/kariera/ | 1076→768 | < 50 | < 50 | — | 17 | 17 | 5 | 5 |
| /aktualnosci/kariera/ | 768→1076 | < 50 | < 50 | — | 17 | 33 | 6 | 6 |
| /aktualnosci/kariera/ | 1536→768 | < 50 | < 50 | — | 17 | 17 | 13 | 6 |
| /aktualnosci/kariera/ | 768→1536 | 53 (60) | < 50 | — | 33 | 17 | 12 | 5 |

(„< 50” = żadnej klatki ≥ 50 ms, od tylu zaczyna się `long-animation-frame`; Kariera ma 11 wpisów, więc nie zawieszała się i przed zmianą.)

**Ślad przeglądarki** (`slad50.mjs`: CDP Tracing, zdarzenia „Layout” według funkcji, która je wymusiła), /aktualnosci/:
- 1536→1076 przed: 122 przeliczenia z `czytaj-dalej` (razem 1145 ms) + 4 drobne z `dopasuj` (strona) + 2 zwykłe klatki; po: 0 z `czytaj-dalej`, 4 drobne z `dopasuj` + 3 zwykłe klatki (razem ok. 51 ms).
- 1536→768 przed: 132 z `czytaj-dalej` + 12 zwykłych klatek + 3 drobne; po: 0 z `czytaj-dalej`, 14 zwykłych klatek (ok. 35 ms) + 4 drobne (`PasekMenu`, `uloz`).

### 2. „… czytaj dalej” przy tych samych wpisach (`dalej50.mjs`, wynik `tresci-B/z50-dalej.json`, log `z50-dalej.log`)
Zbiór = adresy widocznych wpisów z dopiskiem `.wa-dalej`. PL, EN i Kariera przy 1920, 1536, 1366, 1076, 1024, 900, 768 i 390 px: po wczytaniu, po wybraniu każdego filtra (6 przycisków na komputerze, lista wyboru na telefonie), po wpisaniu słowa w szukanie (PL „nagroda”, EN „award”, Kariera „matematyk”) i po wyczyszczeniu pola; do tego zmiana szerokości w tej samej karcie 1536 → 1076 → 768 → 1536. **177 porównań, 0 różnic**, konsola czysta. Przykładowo /aktualnosci/: 132 wpisy z dopiskiem przy 1920 i 1536, 134 przy 1366, 12 przy 1076, 20 przy 1024, 0 od 900 w dół; EN: 131 / 131 / 131 / 15 / 31 / 0; Kariera: 8 / 8 / 8 / 0 / 1 / 0.

### 3. Menu (`menu50.mjs`, log `tresci-B/z50-menu.log`; `anim50.mjs`)
| Sprawdzenie (/nauka/konferencje/, 1536×864) | Przed | Po |
|---|---|---|
| Po otwarciu rozwinięty dział | Nauka | Nauka |
| Po Esc fokus | „Otwórz menu” | „Otwórz menu” |
| Widoczne linki w zamkniętym panelu | 8 (Seminaria … Rada Dyscypliny) | 0 |
| Następny Tab | „Seminaria” w panelu | „← Nauka” (`/nauka`), poza panelem |
| `elementFromPoint` w miejscu „Seminaria” | link „Seminaria” w panelu | `div.z-slot` banera (liczby konferencji) |
| Klik w tym miejscu | przenosi na `/seminaria/` | zostaje na `/nauka/konferencje/` |
| Rozwinięcie „Instytutu” w otwartym panelu | 178 px, 7 linków widocznych, Nauka zwinięta | to samo |
| Zwinięcie | 0 px, nic nie rozwinięte | to samo |

- **Animacja:** wysokość grupy „Instytut” w kolejnych klatkach przy rozwijaniu (4 → 34 → 68 → 98 → 121 → 137 … 178 px w ok. 310 ms) i zwijaniu (174 → 140 → 107 → 78 … 0 px, linki chowają się po ok. 320 ms) jest taka sama przed i po, klatka w klatkę (różnice 1 px / kilka ms z taktowania). Zrzuty 80 ms i 140 ms po kliknięciu oraz po końcu.
- **Duch** (/aktualnosci/ 1536 px: otwórz, rozwiń Naukę, Esc, szerokość 1536 → 1000 → 1076, zrzut ok. 60 ms po zmianie): przed — grupy Nauki („Wydarzenia naukowe”, „Seminaria”, „Konferencje”…) prześwitują na środku strony, 8 linków z `visibility: visible`; po — nic, 0 linków (`z50-duch-1076-60ms-*`).
- **Telefon 390 px** (panel otwarty i z rozwiniętą Nauką): zrzuty przed i po identyczne bajt w bajt.
- **Strona główna 1536 px, jasny panel:** tryb ciemny — zrzuty identyczne bajt w bajt; tryb jasny — 26 pikseli różnicy, tylko przy animowanej strzałce „Szybki dostęp” (718–726 × 830–835, różnica 1/255).
- **Otwarty panel na /nauka/konferencje/:** w obszarze panelu różnice najwyżej 2/255 na kanał, bo przez panel lekko prześwituje losowy rysunek banera (przed: okręgi, po: krzywa Hilberta). Poza panelem różni się tylko ten rysunek. Panel ten sam.

### 4. Pozostałe
- `npx astro check` (269 plików): 0 błędów, 0 ostrzeżeń, 4 podpowiedzi (jak po zleceniu 49).
- Konsola czysta we wszystkich skryptach (dalej50, menu50, anim50).

**Zrzuty:** `raport-zrzuty/z50-zrzuty/` (18 plików `z50-*`, każdy w parze przed/po): `z50-menu-otwarty-konferencje-1536`, `z50-menu-rozwijanie-80ms-1536`, `z50-menu-rozwijanie-w-trakcie-1536` (140 ms), `z50-menu-rozwiniety-instytut-1536`, `z50-duch-1076-60ms`, `z50-menu-telefon-390`, `z50-menu-telefon-390-nauka`, `z50-menu-glowna-1536-jasny`, `z50-menu-glowna-1536-ciemny`. **Skrypty:** `raport-zrzuty/z50-skrypt/` (`pomiar50`, `diagnoza50`, `slad50`, `dalej50`, `menu50`, `anim50`, `roznica50` — porównanie zrzutów piksel po pikselu). Uruchamiane z katalogu `Web-Core-B` (Playwright stamtąd); w Git Bash adresy stron jako argumenty tylko z `MSYS2_ARG_CONV_EXCL='*'` (inaczej `/aktualnosci/` zamienia się w ścieżkę Windows).

## Kryteria odbioru
- [x] Raptowna zmiana szerokości na Aktualnościach (PL, EN) i Karierze nie zawiesza strony; tabela przed/po; najdłuższa klatka przy dużych skokach 13,6–18,9× krótsza (najgorsza próba po: 107 ms). Skoki 1076↔768: 2,2–3× (odstępstwo 2).
- [x] „… czytaj dalej” przy tych samych wpisach co przed zmianą: 8 szerokości, wszystkie filtry, szukanie, zmiana szerokości w karcie — 177 porównań, 0 różnic.
- [x] Zamknięty panel menu bez klikalnych i fokusowalnych linków; bez ducha przy przejściu przez 1024 px.
- [x] Otwarty panel działa jak dziś: komputer (bieżący dział rozwinięty, ta sama animacja), telefon (zrzuty identyczne), jasny panel głównej w trybie jasnym i ciemnym.
- [x] Zmienione tylko `czytaj-dalej.ts` i jedna wartość w `zal-menu.css`.

## Push (18.11.2026 ok. 23:37, automatycznie po odbiorze — polecenie właściciela „50 tez z pushem”)
- Tuż przed pushem `git fetch`: `origin/main` = `5dd156f5` (nic nowego), gałąź jest jego potomkiem, więc bez rebase.
- `git push origin praca/50-aktualnosci-bez-zawieszania:main`: Web-Core `5dd156f5..0c07b56e` (fast-forward, bez force). Gałąź robocza nie wypchnięta.
- Przekaźnik do Web-Podglad: przebieg `44413357888`; budowa Podglądu `44413386616` (`przebuduj`) — sukces, 1 min 40 s.
- Na opublikowanym Podglądzie: CSS ma `grid-template-rows:1fr;visibility:inherit`, skrypt `czytaj-dalej` ma dwie pętle (odczyty, potem zapisy); /Web-Podglad/aktualnosci/ ma 162 wpisy.
- Budowa Web-Core (workflow) dalej wyłączona; `TYLKO_OPUBLIKOWANE` nigdzie nie ustawione.
