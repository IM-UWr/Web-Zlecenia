# Zlecenie 25: średnie ekrany — treść, gdy brakuje miejsca (GOTOWE, 6.11.2026)

Stan: **wszystkie punkty GOTOWE** (decyzje właściciela 6.11, 22:20–22:42). Drugie z czterech zleceń „średnie ekrany”. **Po zleceniu 24** (potrzebuje nowego progu telefonu 1024 px i nowego marginesu).

**Gdzie i jak:** jak w zleceniu 24 (gałąź `wyglad/zlecenie-16`, commit na punkt, bez pushowania, bez `pobierz_tresci.py`, dziennik, `RAPORT-ZLECENIE-25.md`, zrzuty `raport-zrzuty/z25-*`, numery linii ze stanu `b4f99c2`, PL i EN). Narzędzie odbioru: `24-zalaczniki/24-pomiar-szerokosci.cjs`.

**Skąd to zlecenie.** Przy 1024–1280 px na podstronach z tabelami i kolumnami tekst wylewa się albo łamie litera po literze. Przykład: Plan zajęć — wiersz ma kolumnę nazw 220 px + 12 px i 7 kolumn zajęć, z czego 5 stałych (typ 52, grupa 40, dzień 44, godziny 92, sala 64; `zal-granty-plan.css:59–61`) + 60 px odstępów; elastyczne są tylko „prowadzący” (55%) i „uwagi”, a obok stoi pole „Na tej stronie” (236 + 56 px, `zal-podstrona.css:11`). Prowadzący ma 202 px przy 1920, 153 przy 1280, 98 przy 1180 i **11 przy 1024**, a `overflow-wrap: anywhere` (`:66`) łamie wtedy nazwiska litera po literze (`25-dzis-plan-1024.jpg`). Podobnie kontakty na kierunkach (zawsze 3 kolumny, `zal-tresc.css:129`; zgłoszenie właściciela ze zrzutem), granty (`25-dzis-granty-860.jpg`), pole kafelków działu (`25-dzis-pole-kafelkow-860.jpg`).

## 1. Zasada dla treści strony — GOTOWE (pomysł właściciela, 22:31; doprecyzowania 22:37–22:42)
Właściciel: „gdy robi się wąsko, wypada pole na stronie, to daje miejsce (w ogóle to niech będzie ogólna zasada przy zwężaniu, że pole na stronie wypada jako pierwsze, gdy brakuje miejsca). Potem pozwalamy na zwężanie kolumn i łamanie tekstu, ale tylko do max 2 linii, np. w jednej imię, w drugiej nazwisko, albo część nazwy przedmiotu / część nazwy przedmiotu. A jeśli jest na tyle wąsko, że nie możemy tego spełnić, to włączamy widok mobilny (ale tylko dla ciała strony). Baner ma ogólne zasady określone wyżej.”

Gdy w treści podstrony brakuje miejsca (nagłówek ma swoje zasady ze zlecenia 24):
1. **Najpierw ustępuje pole „Na tej stronie”: zwija się nad treścią, jak dziś na telefonie** (22:37: „zwija jak na mobilce”). Zasada wspólna dla całej strony, ale włącza się **osobno na każdej podstronie**, tylko tam, gdzie czegoś brakuje. Na stronach z samym tekstem pole zostaje aż do 1024 px.
2. **Potem kolumny mogą się zwężać, a tekst łamie się tylko między słowami** — nigdy w środku słowa. Limity linii dla „pozycji z limitem”:
   - nazwisko (imię i nazwisko jednej osoby): **2 linie**;
   - nazwa przedmiotu: **3 linie** (22:37: „dopuszczamy 3” — przy 1920 px 7 z 88 przedmiotów ma już 3 linie w kolumnie 220 px);
   - adres e-mail: **2 linie, łamanie tylko przed „@”** (`<wbr>` przed „@” wstawiane przy budowie);
   - komórka tabeli w treści: **2 linie**.
3. **Gdy i tak się nie mieści: widok telefonu dla całej treści podstrony** (22:42: „cała podstrona”) — nie dla jednego bloku. Nagłówek, pasek i stopka zostają w widoku komputera.

**Rozstrzyga pomiar w przeglądarce** (zaakceptowane 22:41). Dla każdej pozycji z limitem: ile linii zajmuje (liczba różnych górnych krawędzi prostokątów tekstu `Range.getClientRects()`, z tolerancją ok. pół wysokości linii; tekst tylko dla czytnika pominąć; osoby rozdzielone `<br>` w jednej komórce liczyć osobno) i czy któreś słowo nie wystaje z kolumny (`scrollWidth > clientWidth`). Wzór: `25-zalaczniki/25-zasada-tresci-prototyp.js`.
- Kolejność: stan pełny → mierz → jeśli źle: zwiń pole → mierz → jeśli źle: widok telefonu treści. Przy poszerzaniu okna zacznij od stanu pełnego i zejdź tylko tak nisko, jak trzeba (bez mrugania: mierz w `requestAnimationFrame`, zmiany klas dopiero po pomiarze).
- Chwile pomiaru: przed pierwszym narysowaniem (skrypt w linii na końcu treści), po `document.fonts.ready`, przy zmianie rozmiaru okna.
- Pozycje z limitem oznacz w szablonach atrybutem (np. `data-limit-linii="2"`), nie listą selektorów w skrypcie: Plan zajęć (prowadzący — każda osoba, nazwa przedmiotu = 3), kontakty (`.tresc .kontakty`: nazwisko, e-mail), Pracownicy (nazwisko, e-mail), Władze (nazwiska, e-maile), komórki tabel w treści (`.tresc table`, `.prose table`).
- Bez JavaScriptu: zapasowe, ostrożne progi w CSS — na podstronach z pozycjami z limitem pole zwinięte poniżej 1300 px; widok telefonu treści się nie włącza.
- Stan widać w atrybutach (np. `data-pole="zwiniete"`, `data-tresc="telefon"` na `.z-pd`), żeby cotygodniowe sprawdzanie (zlecenie 27) mogło wypisać, gdzie i od jakiej szerokości to następuje. Po imporcie (USOS, CMS) nic nie trzeba przestawiać.

**Widok telefonu tylko dla treści** wymaga jednorazowej przeróbki CSS: reguły telefonu treści (dziś w `@media` telefonu w `zal-podstrona.css`, `zal-tresc.css`, `zal-granty-plan.css`, widokach list i `TabelaPracownikow.tsx`) muszą dać się włączyć także klasą/atrybutem na `.z-pd`, bez kopiowania reguł (np. jedna lista selektorów z `:is()` dla `@media` telefonu i dla `[data-tresc="telefon"]`, albo zapytania kontenerowe). Sposób wybierz sam, opisz w raporcie. Spis „Na tej stronie” zwinięty nad treścią ma wygląd i zachowanie z telefonu (`SpisStrony.astro`).

**Wynik prototypu** (pole wyjęte, łamanie tylko między słowami; szczegóły w pliku prototypu): Plan zajęć — prowadzący 173 px przy 1024, 260 przy 1180, 316 przy 1280; **0 z 253 nazwisk** w więcej niż 2 liniach, nic nie wystaje, więc krok 3 przy obecnych danych nie zachodzi. Kontakty Szkoły doktorskiej i Matematyki przy 1024 i 1180 px — bez kolizji, nazwiska w 1 linii, najdłuższy e-mail w 2 liniach przed „@” (`25-kontakty-dzis-i-zasada.jpg`). Kontakty kierunków, Szkoła doktorska, Pracownicy, Granty, Konferencje, Władze — po kroku 1 0 problemów w narzędziu przy 1024–1280 px.

**Odbiór (punkt 1):** okna 1024×700, 1100×800, 1180×820, 1280×600, 1366×620, 1440×780, 1536×730, 1920×950, PL i EN:
- Plan zajęć (oba semestry): 0 osób w więcej niż 2 liniach, 0 przedmiotów w więcej niż 3, 0 słów łamanych w środku, nic nie wystaje; pole zwinięte tam, gdzie potrzeba;
- strony z kontaktami (Matematyka, SIAD, ISIM, Szkoła doktorska i jej podstrony), Pracownicy, Władze, Sprawy studenckie, Zajęcia, Pierwszy rok: narzędzie 0 K/R/O/W/X w treści, e-maile łamane tylko przed „@”;
- strony z samym tekstem (O stronie, deklaracja dostępności, polityka prywatności, Program MOST, Skrypty): pole zostaje przy każdym oknie od 1024 px;
- od 1368 px strony, które dziś nie mają problemów, bez zmian (poza zamierzonym brakiem łamania w środku słowa);
- tymczasowo dopisz w danych (lokalnie, nie commituj) bardzo długie nazwisko i e-mail w kontaktach — przy 1024 px treść przechodzi na widok telefonu, nagłówek zostaje komputerowy;
- bez JS: pole zwinięte poniżej 1300 px na stronach z pozycjami z limitem, nic nie wystaje poza okno.

## 2. Poprawki bez decyzji (mechaniczne) — GOTOWE
Każda to osobny mały commit. Numery linii ze stanu `b4f99c2`.
1. **Pole stron pod kafelkami działu** (`TrescDzialu.astro:51`, `zal-dzialy.css` ok. :190–196): nazwy linków po polsku też się zawijają (dziś `white-space: nowrap` tylko w PL, w EN `normal` — EN nie ma kolizji); w wąskim polu najwyżej 3 kolumny (zapytanie kontenerowe albo `repeat(auto-fill, minmax(200px, 1fr))`). Dziś psuje się poniżej ok. 1260 px (Studia „Dyplom”: Procedura dyplomowania ⟷ Sprawy studenckie, przy 1280 px styk 4 px), 1185 px (Popularyzacja „Partnerzy”), 912 px (Instytut „Więcej”).
2. **Kafelek „Rekrutacja RRRR/RR ↗”** (`zal-dzialy.css` ok. :159, :180, `.z-dz-kart-rekr`): napis nie wylewa się z ramki (dziś poniżej ok. 1100–1130 px, EN ok. 1135; przy 800 px poziome przewijanie) — ostatnia kolumna `minmax(max-content, …)` albo zawijanie „Rekrutacja / 2027/28 ↗” w dwóch liniach; strzałka `::after` w ramce.
3. **Kontakty** `.tresc .kontakty` (`zal-tresc.css:129`): `repeat(auto-fill, minmax(250px, 1fr))`; pary etykieta–wartość (`dl.para`, `:70`) łamią się tylko między słowami; e-mail z `<wbr>` przed „@” (punkt 1).
4. **Dane seminarium** (`Seminarium.astro:177–180`): kolumny `repeat(auto-fit, minmax(220px, 1fr))` zamiast 3 kolumn do 979 px; bez `overflow-wrap: anywhere`; e-mail przed „@”.
5. **Listy linków** `ul.linki` / `ul.dwa` (`zal-tresc.css:42`, `:194`): zapytanie kontenerowe jak przy `ul.boksy` (`:109–112`) — jedna kolumna, gdy kolumna treści jest wąska (dziś przy 800–860 px strzałka „Teoria prawdopodobieństwa ↗” wchodzi na „Statystyka”).
6. **Publikacje** (`Publikacje.astro:114`): siatka lat `repeat(auto-fill, minmax(150px, 1fr))` (dziś przy 4 kolumnach przycisk PDF zjeżdża pod rok i wiersze mają różną wysokość).
7. **Władze** (`zalozyciele-strony.css:107, 118, 130, 132`): zastępcy w `repeat(auto-fill, minmax(200px, 1fr))` zamiast 4 kolumn, kontakt w 2 kolumnach z etykietą 90 px → `auto-fill`; bez łamania w środku słowa (nazwiska i e-maile to pozycje z limitem).
8. **Projekty i granty** (`zal-granty-plan.css:14–15`): pasek czasu `clamp(160px, 40%, 380px)` zamiast stałych 380 px; dolna lista „Zakończone” (kolumna 240 px) bez ściskania tytułu do kilkudziesięciu px.
9. **Konferencje** (`ListaKonferencji.astro:102`): minione w `repeat(auto-fill, minmax(300px, 1fr))` zamiast zawsze 2 kolumn.
10. **Plan zajęć** (`zal-granty-plan.css:66`): bez `overflow-wrap: anywhere`; resztę załatwia punkt 1.
11. **Tekst działu i „W skrócie”** (`zal-dzialy.css`, `.z-dz-tresc`: `1fr 300px`, odstęp 72): kolumna „W skrócie” i odstęp przez `clamp()`, nagłówek sekcji `line-height` 1,2 zamiast 1,6.
12. **Karty projektów i „Dla kogo”** (`zal-dzialy.css` `.z-dz-kart`, `repeat(4, …)`): `repeat(auto-fill, minmax(220px, 1fr))` (2×2, gdy wąsko).
13. **Wpis aktualności ze zdjęciem bez wydarzenia** (`Aktualnosc.astro:177–181`): przy 1024–1103 px karta na całą szerokość z ok. 70% pustego beżu — podpis pod zdjęciem, karta `width: fit-content` (albo zdjęcie obok wstępu); wpis o wydarzeniu bez zmian.
14. **Lista Aktualności** (`ListaAktualnosci.astro:210`, `@container (min-width: 760px)`): dwie kolumny dopiero od ok. 880 px szerokości kontenera (dziś przy 1180–1365 px tytuły w 4–5 liniach).
15. **Długi spis „Na tej stronie” przy niskim oknie** (`zal-podstrona.css:26`, `scrollbar-width: none`): gdy spis jest dłuższy niż okno, przy dolnej krawędzi zanikanie (maska ok. 24 px), żeby było widać, że jest więcej (Pierwszy rok przy 600–730 px wysokości).

**Odbiór (punkt 2):** narzędzie przy 1024–1920 px na 4 działach (z rozwiniętymi kafelkami — narzędzie robi to samo) i na stronach z punktu 1: 0 K/R/O/W/X; zrzuty Studia „Dyplom” przy 1280 i 1180 px, Popularyzacja „Partnerzy” przy 1180 px, Rekrutacja przy 1024 px, Władze, Granty, Konferencje i Publikacje przy 1024 px w `raport-zrzuty/z25-*`.

## Raport
`RAPORT-ZLECENIE-25.md`: sposób przeróbki CSS (widok telefonu dla treści), lista pozycji z limitem i gdzie są oznaczone, tabela: strona × okno → stan (pełny / pole zwinięte / treść telefonu), macierz z narzędzia przed i po, pytania.
