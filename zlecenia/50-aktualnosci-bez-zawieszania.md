# Zlecenie 50: Aktualności bez zawieszania przy zmianie szerokości okna i niewidoczne linki w zamkniętym menu (18.11.2026)

Zakres: tylko dwie zmiany w Web-Core. Repozytoria treści bez zmian. Zasada D4 (Podstrona.astro), animacja „wejscie” i reszta — NIE w tym zleceniu (później; diagnoza w projekcie, claude/plynne-zwezanie.md). Skoki w układzie przy zwężaniu są w porządku; chodzi tylko o zacinanie.
Baza: Web-Core main = 3cde30e. Zlecenia 46–49 mogą wejść wcześniej: przed pushem git fetch i rebase na origin/main.

## 1. „… czytaj dalej” w dwóch fazach (src/scripts/zal/czytaj-dalej.ts, funkcja czytajDalej)
Stan dziś: funkcji używają ListaAktualnosci.astro (PL i EN) i ListaOfert.astro (Kariera). Wywołania: w requestAnimationFrame po każdym resize, po fonts.ready i po filtrowaniu. Pętla na przemian czyta (z.scrollHeight > z.clientHeight + 1) i zapisuje (dopisuje/usuwa span.wa-dalej), więc każdy następny odczyt wymusza przeliczenie układu całej strony. Przy 160 wpisach jedna raptowna zmiana szerokości (1536↔1076, 768↔1536) daje 120–150 przeliczeń i klatkę 1,0–1,45 s — strona stoi. Wersja dwufazowa w moim pomiarze: ok. 0,1 s.
Docelowo: najpierw pętla samych odczytów (dla widocznych pozycji z zajawką: zajawka + czy ucięta, ten sam warunek z tolerancją 1 px), potem pętla samych zapisów (ten sam span: klasa wa-dalej, aria-hidden, tekst). .wa-dalej ma position: absolute (WierszAktualnosci.astro), więc wynik jest ten sam. Podpis funkcji, wywołania i czytajDalejNaBiezaco bez zmian; nic więcej w listach.

## 2. Zamknięty panel menu bez niewidocznych linków (src/styles/zal-menu.css, blok komputera)
Stan dziś: reguła `.z-menu.zwijane section[data-dzial].rozwiniety .z-menu-grupy` ma `visibility: visible`, co przebija `visibility: hidden` zamkniętego panelu. Rozwinięty dział zostaje rozwinięty po zamknięciu, więc jego linki są niewidoczne (opacity 0), ale klikalne i dostępne Tabem. Odtworzenie: /nauka/konferencje/ przy 1536 px → otwórz hamburger, Esc → Tab trafia w niewidoczne „Seminaria”; klik w puste miejsce banera przenosi na /seminaria/. Przy przejściu telefon → komputer (przez 1024 px) grupy prześwitują na środku strony jako „duch” (przejście opacity panelu, stare --menu-x/-y).
Docelowo: w tej jednej regule `visibility: inherit` zamiast `visible`; reszta reguły bez zmian. Grupy widać tylko w otwartym panelu; rozwijanie i zwijanie w otwartym panelu jak dziś. Panel telefonu bez zmian (reguła tylko w bloku komputera). Sprawdziłem to wstrzykniętym CSS: Tab po zamknięciu idzie do „← Nauka”, klik w dawnym miejscu linku trafia w treść, ducha nie ma, rozwijanie działów działa.

## Odbiór lokalny
- Pomiar przed i po (Playwright + Chromium; CDP Performance.getMetrics, PerformanceObserver 'long-animation-frame'): /aktualnosci/, /en/aktualnosci/, /aktualnosci/kariera/; skoki przy wysokości 800: 1536→1076, 1076→1536, 1076→768, 768→1076, 1536→768, 768→1536. Do tabeli: najdłuższa klatka w 1,5 s po zmianie i LayoutCount. Cel na Aktualnościach: najdłuższa klatka co najmniej 5× krótsza, przeliczeń najwyżej ok. 25.
- Ten sam wynik „czytaj dalej”: PL, EN i Kariera przy 1920, 1536, 1366, 1076, 1024, 900, 768, 390 — zbiór wpisów z dopiskiem identyczny przed i po; także po wybraniu każdego filtra i po wpisaniu słowa w szukanie.
- Menu: /nauka/konferencje/ 1536×864 — po otwarciu i Esc Tab idzie do następnego elementu strony, elementFromPoint w miejscu „Seminaria” nie trafia w panel, klik tam nie przenosi; w otwartym panelu bieżący dział rozwinięty, rozwijanie/zwijanie innych z animacją (zrzut). Duch: /aktualnosci/ 1536 px, otwórz menu, rozwiń Naukę, zamknij, szerokość 1536→1000→1076, zrzut ok. 60 ms po zmianie — bez fragmentów menu. Telefon 390 px: panel jak dziś. Strona główna: jasny panel w trybie jasnym i ciemnym jak dziś.
- astro check bez nowych błędów, konsola czysta. Zrzuty raport-zrzuty/z50-*. Bez subagentów.
- Stop: raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Raptowna zmiana szerokości na Aktualnościach (PL, EN) i Karierze nie zawiesza strony; tabela przed/po, najdłuższa klatka ≥ 5× krótsza.
- [ ] „… czytaj dalej” przy tych samych wpisach co przed zmianą (wszystkie szerokości, filtry, szukanie).
- [ ] Zamknięty panel menu bez klikalnych i fokusowalnych linków; bez ducha przy przejściu przez 1024 px.
- [ ] Otwarty panel działa jak dziś (komputer, telefon, jasny panel głównej, tryb ciemny).
- [ ] Zmienione tylko czytaj-dalej.ts i jedna wartość w zal-menu.css.
