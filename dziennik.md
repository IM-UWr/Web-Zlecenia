# Dziennik zleceń (Claude Code, komputer użytkownika)

Przed zleceniami (31.10, ok. 22:30): 8 lokalnych commitów z `web-core-lokalne-commity.bundle` przywrócone jako historia gałęzi `agent-nauka-podglad` (`git fetch` z bundla + `git reset --mixed 235ac2c1`, pliki bez zmian, drzewo robocze było identyczne z `235ac2c1`). Uwaga: zasady.md mówią „nie commituj”, ale użytkownik w rozmowie pozwolił na lokalne commity (bez pushy) i prosi o numer commita w dzienniku.

## 02-animacje-dzialow — 2026-10-31 23:08
Status: zrobione (zlecenie 01 jeszcze niezrobione — za zgodą użytkownika 02 przed 01, zob. odstępstwa)
Commit: `b1fbd328` (lokalny, gałąź `agent-nauka-podglad`, bez pushu)

Zmienione pliki:
- `src/scripts/baner/silnik.ts` (nowy) — silnik: pomiar banera, maska „obrys linii”, płótna, pętla, pauzy, reduced-motion, nowy układ
- `src/scripts/baner/typy.ts` (nowy) — interfejs motywu i geometrii
- `src/scripts/baner/wspolne.ts` (nowy) — smoothstep, generator losowy
- `src/scripts/baner/motywy/lorenz.ts` (nowy) — Nauka
- `src/scripts/baner/motywy/fourier.ts` (nowy) — Aktualności
- `src/scripts/baner/motywy/dendryt.ts` (nowy) — Instytut
- `src/scripts/baner/motywy/riemann.ts` (nowy) — Studia
- `src/scripts/baner/motywy/zloty-podzial.ts` (nowy) — Popularyzacja
- `src/lib/motywyBanerow.ts` (nowy) — mapa strona → motyw
- `src/components/NaglowekStrony.astro` — atrybut `data-animacja`, skrypt silnika (tylko na stronach z motywem), usunięta stara fala na requestAnimationFrame
- `src/styles/telefon.css` — płótna `.ph-anim`, token koloru `--ph-rysunek`, gaśnięcie `.ph-m`, szary akcent statycznego rysunku (wszystko w `@media (max-width: 760px)`)

Kryteria odbioru:
1. Build i konsola — spełnione. `npm run build` bez błędów i ostrzeżeń; na zbudowanej stronie (astro preview) Nauka, Instytut, Studia, Aktualności, Popularyzacja i /en/nauka/ bez komunikatów w konsoli.
2. Animacje zgodne z prototypami (390 px) — spełnione; parametry przeniesione 1:1 z ustawień „telefon” prototypów (krycie, tempo, liczba wyrazów/punktów, ziarno 1951, obrót 5°, start komety w niewidocznej części, `podHaslem` 70 we Fourierze, złoty podział nad hasłem od paska menu + 6 px do hasła − 6 px). Kolor: biały z niskim kryciem z tokenu `--ph-rysunek`. Sprawdzone zrzutami w przeglądarce. Wyjątek: Riemann losowo, nie w kółko (odstępstwa).
3. Klatki (pomiar: licznik nałożeń maski na płótna, okno 15–40 s; z wymuszonym ruchem — w przeglądarce testowej system ma „ogranicz ruch”):
   - Nauka (Lorenz): atraktor 0 kl./s; kometa średnio 15,3 kl./s, odstępy 42–112 ms (10–24 kl./s zależnie od prędkości, jak w prototypie) — wyjątek przewidziany w zleceniu;
   - Aktualności (Fourier): budowanie 4,3 kl./s (21 s), spoczynek 3,6 kl./s (oddychanie + losowe rozkłady);
   - Instytut (dendryt): 4,3 kl./s;
   - Studia (Riemann): 2,3 kl./s;
   - Popularyzacja (złoty podział): budowanie ok. 8 kl./s (jednorazowe, ok. 30 s), spoczynek 3,2 kl./s (40 s; przed zmniejszeniem kroku gaśnięcia elementu z 40 do 20 stopni krycia było 4,1).
   - Poza ekranem i w karcie w tle: pętla zatrzymana (IntersectionObserver + visibilitychange; czas motywu stoi). Sprawdzone w kodzie, nie pomiarem.
4. prefers-reduced-motion — spełnione: na wszystkich 5 stronach gotowy rysunek, 0 klatek w 5 s (przeglądarka testowa ma to ustawienie w systemie).
5. Brak requestAnimationFrame — spełnione: stary skrypt fali usunięty; w `NaglowekStrony.astro` i `src/scripts/` słowo występuje tylko w komentarzach.
6. Długi tytuł — spełnione: w przeglądarce tymczasowo „Popularyzacja matematyki we Wrocławiu” (2 linie) na Popularyzacji i na Nauce. Silnik przeliczył układ (baner 254 → 282 px). Maska po liniach: w pasie pierwszej linii (koniec ok. 347 px z 390) rysunek znika, obok krótszej drugiej linii i przy „← Strona główna” jest widoczny; nigdzie nie wchodzi pod tekst. Lorenz wygląda dobrze; złoty podział jest wtedy przecięty pasem pierwszej linii (zob. pytania).
7. Komputer bez zmian — spełnione: przy 1280 px brak płótna, brak wczytanego motywu, `.ph-m` jak dziś. Porównanie zbudowanego HTML z wersją sprzed zmian (build `235ac2c1` w osobnym katalogu): różnice tylko na 5 stronach działów (PL i EN) — atrybut `data-animacja` i `<script type="module">` silnika; na Aktualnościach dodatkowo usunięty stary skrypt fali. Inne strony (granty, władze, kalendarz, plan zajęć, seminaria, seminarium) — HTML identyczny. CSS: wszystkie zmiany w `@media (max-width: 760px)`. Jedyna różnica widoczna na komputerze: bursztynowa fala Aktualności stoi (wcześniej skrypt rAF ją animował) — wynika z kryterium 5.
8. Tryb ciemny na telefonie — spełnione: kolor rysunku 210, 222, 240 (lekko przygaszony), rysunek słaby, ale widoczny; hasło jedynym bursztynem (zrzut Instytutu).
9. Silnik gotowy na kolejne motywy (dla zleceń 03–05): nowy motyw to plik `src/scripts/baner/motywy/<nazwa>.ts`, który eksportuje domyślnie fabrykę `(G, t0) => Motyw` i opcjonalnie `ustawienia` maski (`granica`, `podHaslem`, `przejscie`), plus wpis `'<adres strony>': '<nazwa>'` w `src/lib/motywyBanerow.ts` (adres bez bazy, bez /en, bez ukośników na końcach). Silnik znajduje plik sam (`import.meta.glob`) i ładuje tylko jego kod. Motyw rysuje we współrzędnych banera; `G` daje pole (`y0`/`y1` — od linku „←” do kreski nad liczbami − 12 px), `widac(x, y)`, `granica(y)`, linie tytułu, hasło, dół paska menu i `rgba(krycie)` w kolorze z tokenu. `krok(t)` zwraca, które warstwy przerysować (`a` — stała, `b` — ruchoma, może zwrócić pudło do częściowego czyszczenia) i za ile sekund obudzić pętlę; `gotowy()` daje rysunek dla reduced-motion. Można też podać motyw wprost propem `motyw` w `NaglowekStrony`.
10. Rozmiary (build, bez kompresji): silnik 8,8 KB (wspólny dla wszystkich), lorenz 4,0 KB, fourier 2,0 KB, dendryt 2,5 KB, riemann 2,3 KB, zloty-podzial 6,4 KB — każdy ≤ 15 KB. Strona wczytuje tylko swój motyw (sprawdzone w zakładce sieci).
11. Ten wpis — spełnione.

Odstępstwa od zlecenia i powody:
- Kolejność: 02 przed 01 (decyzja użytkownika). Działy miały już na telefonie hasło, kreskę i liczby, a tabela 01 przewiduje dla nich „bez zmian”. Silnik mierzy `.wstecz`, `h1`, `.ph-haslo`, `.pt-liczby`, więc po 01 zadziała też na podstronach.
- Atrybut `data-animacja` zamiast `data-motyw` (przykład ze zlecenia): `data-motyw` oznacza w `Naglowek.astro` przycisk trybu jasny/ciemny i jego skrypt podpina kliknięcie pod każdy taki element — kliknięcie w baner przełączałoby motyw. Wyłapane porównaniem HTML przed commitem.
- Riemann: w prototypie poziom podziału szedł w kółko (cykl 40 s), co łamie zasadę „losowo, nie w kółko” (zauważył to też agent prototypów). Teraz co losową przerwę (średnio 6 s, ±60%) podział przechodzi do losowego innego poziomu (5/10/20/40 przedziałów) w tempie prototypu; między zmianami rysunek stoi.
- Dendryt: przejścia gałęzi 8 kl./s zamiast 12 (inaczej średnia ok. 6 kl./s, ponad limit 5); zmiana krycia na klatkę < 1%, schodków nie widać.
- Maska pod hasłem: granica przy linii hasła nie wychodzi dalej w prawo niż przy ostatniej linii tytułu (minus `podHaslem` motywu). Daje to dokładnie zachowanie prototypów działów (rysunek może zachodzić pod hasło za końcem krótkiego tytułu), a przy długim tytule hasło jest objęte jak każda linia.
- Pole rysunku wspólne (link „←” + 2 px do kreski − 12 px) także dla Fouriera (prototyp: − 6 px) i Riemanna (prototyp: od dołu linku „←”) — różnica kilku pikseli wysokości.
- Statyczny rysunek `.ph-m` na telefonie: bursztynowy akcent (`::after`) teraz szary na wszystkich stronach (zlecenie 02: „szary na telefonie”; to samo wymaga kryterium 5 zlecenia 01).
- Aktualności na komputerze: fala już się nie porusza (zob. kryterium 7).

Pytania do użytkownika:
- Złoty podział przy długim, dwuliniowym tytule jest przecięty pasem pierwszej linii (widać górę i dół konstrukcji). Dzisiejszy tytuł „Popularyzacja” jest krótki, więc problem nie występuje. Czy dla długich tytułów zmniejszać konstrukcję i przesuwać ją obok ostatniej linii?
- Na komputerze bursztynowa fala Aktualności stoi. Zostawić tak do decyzji o animacjach na komputerze?
- W systemie tego komputera (Windows) najwyraźniej jest wyłączony ruch („Efekty animacji” albo podobne): przeglądarka zgłasza `prefers-reduced-motion: reduce`. Wtedy strona pokazuje gotowe, nieruchome rysunki. Żeby zobaczyć ruch, trzeba włączyć animacje w systemie albo oglądać na telefonie.

Co sprawdzić:
- Telefon (390 px), strony: /nauka/, /aktualnosci/, /instytut/, /studia/, /popularyzacja/ i wersje /en/ — ruch, tempo, zanik przy tekście, kolor; Fourier buduje się 20 s, złoty podział ok. 30 s.
- Tryb ciemny (przycisk księżyca) — rysunek słaby, ale widoczny.
- Komputer (1280 px) — bez płótna, rysunki jak dotąd (fala Aktualności nieruchoma).
- `npm run build`; w konsoli brak błędów.

## 01-uklad-banerow — 2026-10-31 23:55
Status: zrobione (po zleceniu 02, za zgodą użytkownika)
Commit: `2c590dfe` (lokalny, gałąź `agent-nauka-podglad`, bez pushu). Zmiany w danych (nakładka `src/data`, `src/content`) są poza gitem — lista w `pola-do-cms.md`.
Wykonanie: część wspólną zrobił koordynator, a widoki czterech grup stron czterej podagenci, każdy na swoich plikach. Wynik przejrzał i poprawił koordynator, a build i sprawdzenia poniżej zrobił sam.

Zmienione pliki (kod):
- wspólne:
  - `src/content.config.ts`: pola `haslo`/`haslo_en` (strony, seminaria, zakłady, kierunki, specjalności), `strony.liczby`, `kierunki.fakty[].etykieta_krotka(_en)`;
  - `src/components/LiczbyBanera.astro`: przyjmuje też gotowe napisy;
  - `src/components/NaglowekStrony.astro`: `nadtytulTelefon`, `wstecz.telefon`;
  - `src/components/Wstecz.astro`: krótsza etykieta tylko na telefonie;
  - `src/views/Strona.astro`: hasło i liczby z front matter;
  - `src/styles/telefon.css`: 4 px pod hasłem w banerze bez liczb;
  - `src/lib/liczbyTerminow.ts` (nowy): jedne definicje wydarzeń, referatów, obron i nowych ogłoszeń.
- wydarzenia: `ListaAktualnosci`, `Kalendarz`, `ListaSeminariow`, `Seminarium`, `ListaObron`, `Obrona`, `ListaKonferencji` (`src/views/*.astro`).
- badania: `ListaGrantow`, `Grant`, `Publikacje`, `PublikacjeRok`, `ListaSukcesow`, `publikacjeDane.ts`.
- studia: `Kierunek`, `Specjalnosc`, `PlanZajec`, `RokAkademicki`.
- instytut i ogólne: `Zaklad`, `ListaZakladow`, `Pracownicy`, `src/components/TabelaPracownikow.tsx`, `Wladze`, `ListaWartoWiedziec`, `WartoWiedziecWpis`, `Szukaj`, `src/pages/404.astro`, `src/layouts/Baza.astro` (prop `pozaIndeksem` tylko dla 404).
- dane (poza gitem): zob. `pola-do-cms.md`.

Kryteria odbioru:
1. Build — spełnione: `npm run build` bez błędów i ostrzeżeń, 748 stron.
2. Baner na telefonie (390 px; zbudowana strona, pomiar w przeglądarce, PL i EN) — spełnione. Wartości:
   - Aktualności 2·4·5, Kalendarz 2·5·4 (bez „z 30 dni”), Seminaria 9·5·22.
   - Seminarium AH 1·2·5. Seminaria bez referatów w danych mają tylko liczbę koordynatorów, bo zera się pomija (np. Geometria: 1 koordynator).
   - Obrony: 2 nadchodzące · 6 odbytych. Obrona: „21 wrz / poniedziałek, 2026” · „17:00 / sala WS” · „3 recenzje”.
   - Konferencje: 2 w 2026 roku · 52 od 2013 roku · 15 we Wrocławiu (bez odwołanych).
   - Granty 5·87·94. Grant: hasło „UE i międzynarodowe · 2005–2009”, bez liczb.
   - Publikacje 2165·23 (2003–2025)·3, rocznik 2010: 113·53·68, Sukcesy 138·8·12.
   - Historia sukcesów 32·100·1946 (stałe w danych, policzone raz z treści).
   - Kierunki: Matematyka 3 lata·2 lata·5, SIAD 6·180·70, ISIM 3 lata·210·2, szkoła doktorska 17·8·270.
   - Specjalności: I i II · 4. sem. · 17 (AD), 14, 32 (1. sem.), 22, 15 — z danych specjalności.
   - Rok akademicki 75·40·35.
   - Egzaminy 81·65·25, Skrypty 30·7·25 (prototyp miał 33, ale wliczał 3 linki z „Innych źródeł”), Podyplomowe 3·380·90, SD Dokumenty 29·15·4 — stałe w danych.
   - Pracownicy 129·8·17, Struktura 18·16·43, zakłady jak w prototypach (np. Geometria 14·8·2).
3. Bez długiego opisu, przycisków i koordynatorów w banerze — spełnione: na wszystkich sprawdzonych stronach w banerze nie ma nic klikalnego poza „←” ani widocznego opisu. Kierunki nie mają przycisków ani kafelków faktów.
4. Wysokość 200–330 px — spełniona z wyjątkami:
   - tytuły w 3 liniach: ISIM 372 px, Archiwalne programy 261 px;
   - tytuły w 4 liniach (ponad wyjątek ze zlecenia): Dyskretna analiza harmoniczna 371 px, Teoria prawdopodobieństwa i modelowanie stochastyczne 371 px;
   - tytuł w 2 liniach i dwulinijkowe etykiety: Matematyka aktuarialno-finansowa 344 px.
   Pozostałe strony 204–328 px (SIAD 328).
5. Rysunek szary, jeden bursztyn — spełnione: akcent statycznego rysunku jest szary od zlecenia 02. Sprawdzone automatycznie: poza hasłem nie ma w banerze bursztynowego tekstu.
6. Pracownicy — spełnione na zbudowanej stronie: lista „Wszyscy ▾” (grupy Kto: 4, Zakład: 9) + „Szukaj”, bez pastylek. Po wybraniu „Doktoranci” jest „Znaleziono 17 osób” (17 wierszy), po wpisaniu „karch” — „Znaleziono 1 osobę”. Komunikat jest w `aria-live`.
7. Linki powrotu — spełnione: na telefonie „← Seminaria” / „← Obrony doktorskie” (EN „Seminars”, „PhD defences”). Na komputerze zostaje dawny napis (osobna etykieta w `Wstecz`).
8. 404 — spełnione: brak paska, `noindex, nofollow`, brak canonical, brak `data-pagefind-body`, poza indeksem pagefind.
9. EN — spełnione: hasła i etykiety po angielsku (sprawdzone m.in. seminaria, obrona, SIAD, granty, pracownicy, struktura, AD, egzaminy, aktualności, kalendarz). Na stronach EN brane są tylko pola `_en`.
10. Komputer bez zmian — spełnione:
    - HTML wszystkich 748 stron porównany z buildem sprzed zlecenia (stan po 02), po usunięciu bloków `.tylko-telefon` i klasy `tylko-komputer`: identyczny poza 404 (zamierzone) i losowym `uid` wyspy React na Pracownikach.
    - Przy 1280 px na 44 stronach (wszystkie typy z tabeli, PL i EN) położenie, wymiary, kolory, kroje i teksty każdego widocznego elementu są identyczne.
11. Tryb ciemny — spełnione: hasło, liczby, nadtytuł i filtry czytelne (zrzut specjalności AD, Pracownicy sprawdzeni przez podagenta).
12. `pola-do-cms.md` uzupełniony (z repozytoriami ustalonymi na klonach `.tresci`). Ten wpis.

Odstępstwa od zlecenia i powody:
- Kolejność 02 → 01 (decyzja użytkownika).
- Kafelki liczb `.stats` pod banerem (tylko telefon) usunięte w Grantach, Publikacjach, Sukcesach i Strukturze. Te kafelki zastępowały na telefonie liczby z banera komputerowego, więc po zmianie dublowały liczby z banera. Z telefonu znikają przez to m.in. „73 z NCN”, „11 z UE” i liczba doktorantów w Strukturze. Łatwo przywrócić.
- Grant: plakietki i tytuł w drugim języku na telefonie są pod banerem. Rocznik: przycisk „Wykaz w PDF” też jest pod banerem.
- Seminarium: koordynatorzy, e-mail i zakład w zwartym bloku pod banerem. Obrona: tytuł rozprawy na telefonie pod banerem, bo w banerze zostaje imię i nazwisko.
- Wpis Warto wiedzieć: zajawka i link do działu są pod banerem. Zakład: obszary badań są pod banerem.
- Specjalność: nadtytuł na telefonie to „Specjalność · skrót” (jak w prototypie), a nie samo „Specjalność”. Skrót i poziom zniknęły z banera.
- Szkoła doktorska (widok kierunku): na telefonie nadtytuł skrócony do „Kolegium Doktorskie Matematyki”.
- Liczby kierunków: z pola `fakty` — pierwsze trzy fakty z wartością od cyfry, z krótszą etykietą `etykieta_krotka` (nowe pole). Szkoła doktorska: liczba doktorantów liczona ze spisu pracowników.
- Stałe liczby (pole `liczby` w danych) na 5 stronach Studiów i w historii sukcesów: te wartości to fakty z treści albo wymagałyby parsowania Markdownu.
- Obrona: etykieta daty to „dzień tygodnia, rok” (jak w prototypie animacji). Etykieta godziny to sala, a bez niej „godzina”.
- Konferencje: etykiety „w 2026 roku · od 2013 roku · we Wrocławiu”.
- Hasło Zakładu Teorii Prawdopodobieństwa („Procesy gaussowskie i teoria ryzyka”) jest nowe: brak go w prototypach.
- Odmiana rzeczowników męskoosobowych po 2–4: dopełniacz („2 koordynatorów”, „43 doktorów”).

Pytania do użytkownika:
- Kafelki `.stats` pod banerem na telefonie (Granty, Publikacje, Sukcesy, Struktura): usunąć jak teraz czy przywrócić?
- Bardzo długie tytuły seminariów (4 linie, 371 px) i ISIM (3 linie, 372 px): mniejszy krój tytułu na telefonie, krótsza nazwa do banera, czy zostawić?
- Hasła robocze: m.in. Teoria prawdopodobieństwa (zakład), „Nonlinear PDEs” (EN, skrócone), EN dydaktyki „Teaching and talking mathematics” (skrócone, żeby było w 1 linii).
- „Archiwalne programy studiów”: link „←” prowadzi do strony głównej, bo strony nie ma w menu. Poprawka (np. „← Studia”) zmieniłaby też komputer — zrobić?
- Strona „Zadania z egzaminów” (`studia/egzaminy-i-dyplom/zadania`) nie ma hasła (nie było jej w tabeli). Propozycja: „Archiwum zadań od 2002 r.”.

Co sprawdzić:
- Telefon (390 px): strony z tabeli zlecenia, PL i /en/, także tryb ciemny.
- Pracownicy: lista „Wszyscy ▾” i „Szukaj”.
- 404: brak paska „Podgląd”.
- Komputer (1280 px): wygląd bez zmian.
- **Serwer `npm run dev` trzeba uruchomić od nowa** (`npm run dev -- --force`). Pomocniczy build starej wersji w scratchpadzie (porównanie przy zleceniu 02) nadpisał `node_modules/.vite/deps`, więc w działającym serwerze dev komponenty React (np. lista Pracowników) się nie podpinają. Zbudowana strona działa poprawnie.

## 07-granice-rysunkow — 2026-11-01 00:09
Status: zrobione
Commit: `fc977d64` (lokalny, bez pushu)
Zmienione pliki:
- `src/scripts/baner/silnik.ts`: pole, maska przerw, hasło na całą długość, pionowe wygaszenie, płótno do dołu pola; przy okazji wariant i dane motywu dla 03–05;
- `src/scripts/baner/typy.ts`: komentarze pola, usunięte `podHaslem`, nowe `wariant` i `dane`;
- motywy w `src/scripts/baner/motywy/`: `fourier.ts`, `zloty-podzial.ts`, `dendryt.ts`, `lorenz.ts`;
- `src/components/NaglowekStrony.astro`: „nazwa/wariant”, `motywDane`;
- `src/lib/motywyBanerow.ts`: klucze „adres/*”.

Kryteria odbioru (pomiar na zbudowanej stronie przy 390×844, gotowy rysunek przy wymuszonym ograniczeniu ruchu, `getImageData` wszystkich płócien):
1. Build — spełnione: bez błędów i ostrzeżeń, konsola czysta.
2. Dół — spełnione: na 5 działach i /en/nauka/ suma krycia pikseli poniżej połowy hasła wynosi 0. Przed zmianą było 12–398, najwięcej w Studiach (Riemann).
3. Przerwy — spełnione:
   - Krycie w przerwach „← Strona główna”–tytuł i tytuł–hasło (do końca dłuższej linii + granica) wynosi 0.
   - Przed zmianą: Nauka 107, Studia 54.
   - W Nauce atraktor nie przechodzi już między linkiem a „Nauka”.
4. Góra — spełnione: płótno zaczyna się na 67 px (pasek menu 61 + 6), nad nim krycie 0.
5. Dopasowanie (390×844):
   - **Poprawka (1.11, podczas zlecenia 03):** pierwsze liczby w tym punkcie były zawyżone. Mierzyłem w ukrytym panelu przeglądarki, gdzie animacja wejścia tekstu (`przejscia.css`, 12 px) stała w miejscu, więc tekst był 12 px niżej niż naprawdę. Wartości poniżej są po korekcie (tekst na miejscu).
   - Pole przed: od linku + 2 px do 12 px nad kreską, 84–189 px (105 px). Pole po: 67–171 px (104 px).
   - Środek pola przesunął się o ok. 17 px w górę, a wysokość prawie się nie zmieniła (−1%). Motywy liczone z pola przesunęły się więc w górę o ok. 17 px przy tej samej wielkości; zmniejszania nie było.
   - Lorenz, Fourier, Riemann: środek ok. 17 px wyżej, skala ok. 99%.
   - Dendryt: losowanie w polu 69–169 zamiast 86–196, czyli ok. 22 px wyżej, wysokość 91% (dawniej sięgał 7 px pod dół pola).
   - Złoty podział: bez zmian (już stał nad hasłem); proste przycięte do pola.
   - Na dolnej granicy nic nie jest ucięte.
6. Długi tytuł — spełnione. Tymczasowo „Popularyzacja matematyki we Wrocławiu” na Nauce i Popularyzacji:
   - pole 67–210, pod połową hasła krycie 0, nad menu 0;
   - w przerwie tytuł–hasło tylko 4 jednostki w strefie przejścia za krótszą drugą linią tytułu (dozwolone).
7. Tryb ciemny, ograniczony ruch i zmiana rozmiaru — spełnione: ta sama maska i pole (liczone z układu, kolor nie wpływa); pomiar robiony w trybie ograniczonego ruchu.
8. Wydajność — spełnione: Nauka (kometa) 14 kl./s (w 02 było 15), Instytut 4,3 kl./s (w 02 było 4,3).
9. Komputer — spełnione: HTML 748 stron taki jak po 01. Różnice na 6 stronach wynikają tylko z daty budowy („dziś”, nowe ogłoszenia z 30 dni). Silnik działa tylko na telefonie.
10. Ten wpis — Nauka i Studia przed i po opisane w pkt 2–5.

Odstępstwa od zlecenia i powody:
- Wielkość rysunków działów praktycznie bez zmian (pole 104 zamiast 105 px), tylko przesunięcie w górę o ok. 17 px.
- Pole i maska przyjmują już wariant motywu i dane z budowy strony; to przygotowanie pod 03–05.

Pytania do użytkownika:
- Brak. (Wcześniejsze pytanie o powiększenie o 10% było skutkiem błędnego pomiaru — zob. pkt 5.)

## 03-animacje-nauka-seminaria-zaklady — 2026-11-01 10:53
Status: zrobione
Commit: `1c645c59` (lokalny, bez pushu)
Wykonanie: motywy pisali czterej podagenci (wydarzenia, analiza, struktury, badania), każdy na swoich plikach. Mapę, przypisanie zakładów i silnik zrobił koordynator, on też zbudował stronę i sprawdził wynik.

Zmienione pliki:
- **Nowe motywy** w `src/scripts/baner/motywy/`:
  - wydarzenia: `banach.ts`, `genealogia.ts`, `trzy-odleglosci.ts`;
  - analiza: `rozsadnik.ts`, `haar.ts`, `czebyszew.ts`, `wahadlo.ts`, `brown.ts`, `histogram.ts`, wspólne `_analiza.ts`;
  - struktury: `longimetr.ts`, `knaster.ts`, `eliptyczna.ts`, `geoplan.ts`;
  - badania: `wachlarz.ts`, `cytowania.ts` (wspólne łuki), `wspolautorzy.ts`, `bernoulli.ts`.
- **Zmienione:**
  - `src/lib/motywyBanerow.ts`: mapa stron;
  - `src/views/Zaklad.astro`: wariant „zaklad” motywu seminarium zakładu, bez seminarium — Lorenz;
  - `src/views/Grant.astro`, `Publikacje.astro`, `PublikacjeRok.astro`, `publikacjeDane.ts`: dane dla motywu (`motywDane`);
  - `src/scripts/baner/silnik.ts`: nowy pomiar po końcu wejścia tekstu, czyli `animationend`.

Kryteria odbioru:
1. Build i konsola — spełnione. `npm run build` bez błędów i ostrzeżeń. Na 14 stronach przejrzanych w przeglądarce (zbudowana strona) konsola bez błędów; na 32 stronach (zob. pkt 2) silnik wystartował bez ostrzeżeń `[baner]`.
2. Motyw każdej strony — spełnione. Sprawdziłem 32 strony (390 px): wszystkie seminaria, wszystkie 9 zakładów, Konferencje, Obrony, Obrona, Kalendarz, Granty, Grant, Publikacje, rocznik 2010, Sukcesy, Historia i 2 strony EN.
   - Na każdej motyw wystartował i ma właściwy wariant.
   - Każda wczytuje tylko swój kod (seminaria analizy dodatkowo `_analiza` 0,9 KB, rocznik — `cytowania`).
   - Gotowy rysunek mieści się w polu: pod połową hasła i nad paskiem menu krycie 0.
   - Kolor szaro-biały z tokenu.
   - Zgodność z prototypami podagenci sprawdzili zrzutami i odczytem pikseli (prototyp otwierany przez serwer dev).
3. Kalendarz bez bursztynowego motyla — spełnione: animacja trzech odległości. Statyczny rysunek od 02 jest szary.
4. Wydajność i dostępność — spełnione.
   - Spoczynek (pomiary podagentów, ≥ 30 s; moje kontrolne w nawiasach):
     - banach 4,4–4,7 w czasie wzrostu, ok. 1,8 między łamanymi (moje: 1,8);
     - genealogia 3,1, obrona 3,3; trzy odległości 0,8–2,0; rozsadnik 1,4;
     - haar 0,4–0,6 (moje, długi tytuł: 0,58); czebyszew 1,8–3,2; wahadło 2,9–3,9; brown 1,4–1,8; histogram 0,8–1,0;
     - longimetr 2,1–2,3; knaster 3,9 (moje: 4,1); eliptyczna 3,9; geoplan 2,6;
     - wachlarz 3,2–4,3 (moje: 0,8 w przerwie); cytowania 3,6–4; współautorzy 3,7; bernoulli 2,2.
   - Ograniczony ruch: statyczny rysunek, zero klatek, sprawdzony na wszystkich stronach.
   - Długi tytuł „Analiza harmoniczna i rozwinięcia ortogonalne” i tytuły 3- i 4-liniowe: granice trzymają.
   - Tryb ciemny: kolor z tokenu, hasło jedynym akcentem.
5. Rozmiary po budowie (bez kompresji):
   - wydarzenia: banach 3,2 KB, genealogia 4,9, trzy-odleglosci 2,5;
   - analiza: rozsadnik 1,2, haar 4,8, czebyszew 2,2, wahadlo 4,3, brown 3,1, histogram 2,5 (+ wspólne `_analiza` 0,9);
   - struktury: longimetr 3,7, knaster 3,4, eliptyczna 4,4, geoplan 4,6;
   - badania: wachlarz 3,2, cytowania 4,7, wspolautorzy 0,6 (+ cytowania), bernoulli 2,8;
   - silnik: 10,8 KB, wspólny.
6. Komputer bez zmian — spełnione: HTML 748 stron identyczny z buildem po 07, poza atrybutem `data-animacja*` i skryptem silnika (bez wpływu na wygląd na komputerze); CSS bez zmian.
7. Ten wpis.

Dopasowanie do pola (390×844): środki rysunków 10–28 px wyżej niż w prototypach. Skala w pionie:
- 100%: banach, genealogia, trzy odległości, wachlarz (ok. 93%), cytowania i bernoulli (ok. 95%);
- 89–94%: rozsadnik, haar, czebyszew, brown;
- 86–88%: wahadło i histogram (spłaszczenie wykresu);
- 83%: longimetr, knaster i eliptyczna przy jednoliniowym tytule (87–89% przy dłuższych), więcej niż 15% — uzasadnienie w odstępstwach.

Odstępstwa od zlecenia i powody:
- **Zmniejszenie powyżej 15% (struktury: 83% w pionie).** Pole w prototypie miało 114 px, nowe ma 104 px, a dół musi zostać 6–12 px nad połową hasła. Zmniejszone jest tylko w pionie (spłaszczenie łuków, krzywych i rozrzutu); szerokość i kratki geoplanu bez zmian.
- **Zakład Teorii Prawdopodobieństwa** (prototyp nie miał wariantu): ruch Browna w duchu teorii ryzyka — trzy trajektorie B(t) − ct, linie bieżącego maksimum i przerywany poziom ruiny u. Do akceptacji.
- **Rzadsze klatki przy wzroście linii** (krok 0,6–0,75 px zamiast 0,5 px) w knasterze, krzywej eliptycznej, wahadle, cytowaniach i Czebyszewie, żeby średnia mieściła się w 5 kl./s. Tempo linii bez zmian.
- **Czebyszew i Brown:** losowanie zdarzeń tylko tam, gdzie zmiana jest możliwa albo widoczna (w prototypie zdarzały się długie przestoje).
- **Bernoulli:** przestawienie, które wyprowadziłoby ścieżkę nad pole, losuje się od nowa. Historia ma osobny wariant (gęstsza ścieżka, znaczki dekad).
- **Krzywa eliptyczna:** gdy konstrukcja nie mieści się obok długiego tytułu (EN Algebra), widać samą krzywą.
- **Zanik 10 px przy prawym brzegu treści** jak w prototypach struktur — w kolorze motywu (silnik go nie robi).

Pytania do użytkownika:
- Wariant Browna dla Zakładu Teorii Prawdopodobieństwa (teoria ryzyka) — akceptujesz?
- Spłaszczenie motywów struktur do 83% w pionie przy krótkich tytułach — w porządku?

## 04-animacje-studia — 2026-11-01 11:44
Status: zrobione
Commit: `a6ec9087` (lokalny, bez pushu)
Wykonanie: motywy pisało dwóch podagentów (kierunki i specjalności; codzienność). Mapę zrobił koordynator, on też zbudował stronę i sprawdził wynik.

Zmienione pliki:
- **Nowe motywy** w `src/scripts/baner/motywy/`: `gradient.ts`, `permutacje.ts`, `kmeans.ts`, `przezycie.ts`, `okrag.ts`, `lotka.ts`, `kule.ts`, `droga.ts`.
- **Zmienione:**
  - motywy: `trzy-odleglosci.ts` (wariant `rytm`), `banach.ts` (wariant `pajeczyna`), `geoplan.ts` (wariant `podyplomowe`), `_analiza.ts` (tylko komentarz, bo korzystają z niego też motywy Studiów);
  - `src/lib/motywyBanerow.ts`: mapa Studiów i reguła „studia/*” → Riemann.

Kryteria odbioru:
1. Build i konsola — spełnione: `npm run build` bez błędów i ostrzeżeń. Na stronach sprawdzonych w zbudowanej wersji silnik wystartował bez ostrzeżeń; podagenci: brak błędów w konsoli.
2. Motyw każdej strony — spełnione. Sprawdziłem 26 stron (390 px, zbudowana strona):
   - kierunki: Matematyka, SIAD, ISIM;
   - wszystkie specjalności;
   - codzienność: plan zajęć, rok akademicki, zajęcia, pierwszy rok, egzaminy, procedura, szkoła doktorska i 2 podstrony, podyplomowe;
   - z Riemannem działu: MOST, skrypty, zadania z egzaminów (spoza tabeli);
   - EN: SIAD, ISIM, plan zajęć.

   Na każdej motyw wystartował z właściwym wariantem i wczytał tylko swój kod. Gotowy rysunek: pod połową hasła i nad paskiem menu krycie 0. Kalendarz zajęć to przekierowanie (bez banera).
3. Ten sam kod Riemanna — spełnione: Matematyka i strony Studiów spoza tabeli mają `data-animacja="riemann"` i wczytują ten sam plik co dział.
4. Wydajność i dostępność — spełnione. Pomiary podagentów (≥ 20–30 s albo symulacja pętli silnika):
   - kierunki i specjalności: gradient (SIAD) 2,5–2,8 kl./s, permutacje (ISIM) 1,6, kmeans 1,8, przezycie 1,0, okrag 0,7, lotka 1,0, kule 0,6;
   - codzienność: droga 3,6, rytm 2,2–2,4, pajęczyna 2,3–2,8 (chwilowo do 9 przy wyłanianiu odcinków), podyplomowe 2,3–2,7.

   Ograniczony ruch: statyczny rysunek na wszystkich stronach, także EN SIAD i ISIM. Tryb ciemny: kolor z tokenu.
5. Komputer bez zmian — spełnione: HTML 748 stron identyczny z buildem po 03, poza znacznikami motywu.
6. Ten wpis.

Rozmiary po budowie: gradient 4,0 KB, permutacje 3,0, kmeans 3,9, przezycie 2,4, okrag 4,9, lotka 3,0, kule 2,3, droga 2,4. Warianty powiększyły trzy-odleglosci do 3,4 KB, banach do 5,6 i geoplan do 5,8 (wszystko ≤ 15 KB).

Dopasowanie do pola (390 px): środki 6–48 px wyżej niż w prototypach. Skala 91–100%. W gradiencie SIAD minimum doliny przesunięte o 48 px w górę, żeby kółko nie leżało pod tytułem.

Odstępstwa od zlecenia i powody:
- **Pajęczyna w szkole doktorskiej jest zmniejszona do 50–70%** (szkoła 55%, podstrony 50–70%). Długi nadtytuł „Kolegium Doktorskie Matematyki” i dwuliniowe tytuły podstron zasłaniają środek pola. Przy 100% punkt stały wypadałby pod tekstem. Zmniejszanie krokami po 5%, aż punkt stały będzie widoczny. Na EN Rekrutacji punkt stały i tak zostaje częściowo pod tytułem.
- **ISIM:** ruch skrzyżowań trochę mocniejszy niż w prototypie (2–4 px, do 2 px/s), bo prototyp zgłaszał za słaby ruch. Tempo zmian nici zgodnie z tabelą.
- **Rytm:** łuk losowo dzieli się albo łączy (zgodnie z opisem w zleceniu). Kod prototypu robił to na przemian.
- **Nauczycielska (91%) i stosowana (92%):** w prototypach część konstrukcji i największa orbita wychodziły poza pole.
- **k-średnie:** grupa nie znika do zera (w prototypie mogła po długim czasie).
- **Podyplomowe:** korzysta z mechaniki geoplanu seminarium. Ma budowę 2,5 s, której prototyp nie miał.
- **Długie hasła i tytuły zasłaniają część rysunku.** Np. przy haśle Planu zajęć łuki widać od x ≈ 260 px. Tak działa maska silnika.

Pytania do użytkownika:
- Pajęczyna w szkole doktorskiej zmniejszona do 50–70%, żeby punkt stały był widoczny. Zostawić tak, czy 100% z punktem stałym pod tekstem?

## 05-animacje-instytut-ogolne — 2026-11-01 12:23
Status: zrobione
Commit: `dc5efbf3` (lokalny, bez pushu)
Wykonanie: motywy pisało dwóch podagentów (podstrony Instytutu; strony ogólne). Mapę i poprawkę silnika zrobił koordynator, on też zbudował stronę i sprawdził wynik.

Zmienione pliki:
- Nowe motywy w `src/scripts/baner/motywy/`: `kanapka.ts`, `luki.ts`, `dendrogram.ts`, `mapa.ts`, `motyl.ts`, `kratka.ts`.
- Zmienione motywy: `trzy-odleglosci.ts` (wariant `warto`), `banach.ts` (wariant `kratka`; `siec()` z parametrem domyślnym, pajęczyna jak dotąd).
- `src/views/Pracownicy.astro`, `src/views/ListaZakladow.astro`: tylko dane dla motywu (`motywDane`: liczby osób w grupach i zakładach, 42–43 B).
- `src/lib/motywyBanerow.ts`: mapa Instytutu i stron ogólnych, reguła „instytut/*” → dendryt.
- `src/scripts/baner/silnik.ts`: po pierwszym układzie silnik czeka na koniec wejścia tekstu i mierzy jeszcze raz. Gdy karta była w tle, pierwszy pomiar mógł trafić w trakcie animacji, a `animationend` przyjść, zanim powstał motyw.

Kryteria odbioru:
1. Build i konsola — spełnione: `npm run build` bez błędów i ostrzeżeń; silnik startuje bez ostrzeżeń; podagenci: brak błędów z motywów.
2. Motyw każdej strony — spełnione. Sprawdziłem w zbudowanej wersji (390 px):
   - strony z tabeli: Władze, Pracownicy, Struktura, Kontakt, Infrastruktura, Warto wiedzieć (lista i wpis), Szukaj, Deklaracja, Polityka;
   - Instytut i podstrona Infrastruktury (spoza tabeli: dendryt);
   - EN: Pracownicy, Szukaj.

   Motyw wystartował z właściwym wariantem i wczytuje tylko swój kod. Gotowy rysunek: pod połową hasła i nad paskiem menu krycie 0. Strony prawne: statyczna kratka, zero klatek po pierwszej (pomiar podagenta, 25 s).
3. Bez bursztynowo-brązowego trójkąta — spełnione: na telefonie statyczny rysunek jest szary od 02, a animacja go zastępuje (`.ph-m` ma krycie 0).
4. Wydajność i dostępność — spełnione:
   - spoczynek: kanapka 1,3 kl./s, łuki 2,6, dendrogram 0,8, mapa 0,6, motyl (Infrastruktura, długi tytuł) 2,4, Warto wiedzieć 2,0, Szukaj 2,1–2,2, kratka 0;
   - ograniczony ruch: gotowy rysunek, 0 klatek, na wszystkich stronach;
   - tryb ciemny: kolor z tokenu.
5. Komputer bez zmian — spełnione: HTML 748 stron identyczny z buildem po 04, poza znacznikami motywu.
6. Ten wpis.

Dotychczasowe warianty po zmianach (Kalendarz, plan zajęć, Konferencje, szkoła doktorska) — sprawdzone: działają jak przed zmianą.

Rozmiary po budowie: kanapka 4,3 KB, luki 3,7, dendrogram 3,6, mapa 4,3, motyl 2,5, kratka 0,5. Z wariantami trzy-odleglosci ma 6,2 KB, a banach 8,8 KB (+ kratka 0,5).

Dopasowanie do pola (390 px):
- środki 8–25 px wyżej niż w prototypach;
- skala: mapa i Szukaj 100%, Warto wiedzieć 100% (górny limit łuku 88%), kanapka 88%, łuki 87%, dendrogram 88%, motyl 90%.

Odstępstwa od zlecenia i powody:
- Łuki (Pracownicy): nowy łuk czeka, gdy dwa już rosną. W prototypie liczba łuków z czasem malała.
- Klatki rosnących linii co 0,75 px, gaśnięcie 8 kl./s zamiast 12 (łuki, motyl, belki dendrogramu). Tempo bez zmian.
- Motyl: trasa startuje od pierwszego widocznego węzła w swoim wierszu, żeby nie zaczynała się pod tekstem.
- Mapa: przy ograniczonym ruchu znacznik jest widoczny. W prototypie w statycznym rysunku znikał.
- Dendrogram: wysokości złączeń z prototypu są dla dzisiejszego układu 3/3/2 zakładów. Dla innego jest wzór ogólny.
- Warto wiedzieć: własna fabryka przenikania zamiast funkcji profili Kalendarza (inny rodzaj ruchu w prototypie); losowe przesunięcie β, jak w Kalendarzu.
- Mniej rysunku widać niż w prototypach. Hasło jest maskowane na całą długość (07), a cienia 25% nie wdrożono. Rysunki są więc widoczne głównie z prawej i nad tytułem; na EN Struktury głównie górne belki.
- Stała `OBSZARY` (zakład → obszar) jest w dwóch widokach, bo frontmatter `.astro` nie eksportuje. Przy zmianie obszarów trzeba poprawić oba.

Pytania do użytkownika:
- Podstrony Infrastruktury informatycznej (np. regulamin sieci) mają dendryt z działu (zgodnie z regułą „spoza tabeli”). Dać im motyl jak strona nadrzędna?

## 06-strona-glowna-b2 — 2026-11-01 13:35
Status: zrobione
Commit: `bcec3666` (lokalny, bez pushu)
Wykonanie: kod napisał jeden podagent i sprawdził go na serwerze dev. Koordynator przejrzał zmiany, zbudował stronę i sprawdził kryteria na buildzie. Potem zapisał pola, ten wpis i commit.

Zmienione pliki (Web-Core):
- `src/components/StronaGlowna.astro`: baner `.hero-b2` z `<picture>` i elementami telefonu (hasło, podtytuł, mały napis w pasie, przycisk, podpis). Osobny blok wydarzeń dla telefonu. Pozycje od czwartej mają klasę `.nadmiar`. Skrypt zwijania, dociągania i „Zobacz więcej”. Chowanie zakończonych wydarzeń przelicza teraz każdy blok osobno.
- `src/components/ZobaczWiecej.astro` (nowy): przycisk „••• Zobacz więcej (N)” / „Zwiń”.
- `src/components/Naglowek.astro`: klasa `hdr-glowna`. Na telefonie nagłówek strony głównej jest stale ciemny. „Przewinięty” znaczy tam „baner zwinięty”, od tego zależy kolor stopki na dole strony.
- `src/components/KartaWydarzenia.astro` (właściwość `klasa`), `src/components/ListaReferatow.astro` (`id`, `widoczne`).
- `src/lib/tresci.ts`: `wydarzeniaNaTelefon()` (30 dni kalendarzowych, najwyżej 10, z przypomnieniami terminów). `wydarzeniaNaGlowna()` bez zmian w działaniu.
- `src/lib/i18n.ts`: `nadchodzaceWydarzenia`, `naSkrotyIWydarzenia`, `wydzialUwr`, `zobaczWiecej`, `zwin` (PL, EN). `najblizsze` zostaje dla wpisu aktualności.
- `src/styles/telefon.css`: blok „Strona główna B2”, w całości w `@media (max-width: 760px)`.

Nakładka (poza gitem, do repozytorium Web-Ustawienia przy „push”, opis w `pola-do-cms.md`):
- `src/data/ustawienia.json`: `haslo`, `haslo_en`, `baner.zdjecie_telefon`, `baner.podpis_telefon(_en)` (puste), `wydarzenia_dni_telefon`, nowe `baner.opis(_en)`.
- `public/pliki/baner/instytut-telefon.jpg` (nowy): 884×1779, JPEG progresywny, 274 055 B, bez metadanych. Zrobiony z `instytut-telefon-884x1779.png` przez `sharp` z `node_modules` (q82, mozjpeg).

Kryteria odbioru (sprawdzone na buildzie, serwer plików, 390×844; panel przeglądarki był ukryty, więc przewijanie testowane w ramce z podmienionym `requestAnimationFrame` i zdarzeniami `scroll`/`scrollend`):
1. Build i konsola — spełnione: `npm run build` bez błędów; `/` i `/en/` bez błędów w konsoli.
2. Pierwszy ekran — spełnione. Zrzut zgodny z `B2-widok-v29.png`.
   - Zdjęcie od 107 px, z przejściem od paska.
   - Budynek kończy się ok. 440 px, a tytuł zaczyna na 603 px.
   - Hasło bursztynowe, w 1 linii. Przycisk 24 px nad dołem.
   - Tryb ciemny i EN sprawdził podagent.
3. Inne rozmiary — spełnione (PL i EN). Tytuł jest pod nagłówkiem: 338/319 px (360×640), 366/346 (375×667), 630/611 (430×932), 58/58 (740×360). Przycisk jest 26 px pod podtytułem. Hasło w 1 linii, bez przewijania w poziomie (EN 360 px: hasło do 316 px).
4. Przewijanie — spełnione.
   - Pas: dół banera na 97 px (61 + 36), nazwa w nagłówku, hasło w pasie (krycie 1).
   - Dociąganie: w dół 50 → Z, 9 → Z, 5 → 0; w górę z Z 600 → Z, 500 → 0.
   - Z palcem na ekranie nic się nie dzieje; po puszczeniu dociąga.
   - Poza strefą (1500, 2000) przewijanie jest zwykłe.
   - Przycisk: dokładnie Z = 747, fokus na „Na skróty”; od p > .25 `visibility: hidden`.
5. Sekcje — spełnione (dane testowe: 6 wydarzeń, 6 aktualności, 5 referatów).
   - „Nadchodzące wydarzenia”.
   - „Zobacz więcej (3)”, „(3)”, „(2)”; po rozwinięciu sam napis „Zwiń”.
   - Rozwinięta jedna sekcja; kotwica stoi w miejscu (0 px), a przewinięcie wyrównuje zwinięcie sekcji wyżej (−412 px).
   - Fokus zostaje na przycisku. Tab z 3. pozycji idzie prosto do przycisku.
   - Chowanie zakończonych wydarzeń z przestawionym zegarem sprawdził podagent: 4 → „(1)”, 2 → bez przycisku, 0 → komunikat.
6. Dostępność — spełnione.
   - Jeden `h1`.
   - Kontrast w najjaśniejszym miejscu pod tekstem (pomiar podagenta): biel 18,2 : 1, bursztyn 8,7 : 1, podtytuł 14,8 : 1.
   - `scroll-padding-top` 105 px.
   - Ograniczony ruch: bez wejścia, podskoku i paralaksy, przewijanie bez animacji (podagent).
   - Bez JS (ramka bez skryptów): baner 844 px, nie przyklejony, wszystkie 8 ukrytych pozycji widać, przycisków nie ma.
7. Wydajność — spełnione.
   - Na telefonie z banera pobiera się tylko `instytut-telefon.jpg` (274 KB), bez `kampus-zmierzch*`.
   - CLS 0 (pomiar w ukrytym panelu, warto potwierdzić na telefonie).
   - Skrypt w klatce czyta tylko `scrollY`; wymiary przy załadowaniu i `resize`.
8. Komputer 1280 px — spełnione.
   - HTML 748 stron porównany z buildem po 05 (bez skryptów): różni się tylko `/` i `/en/`.
   - Różnice: klasy `hdr-glowna` i `hero-b2`, `<picture>` z `<source>` telefonu, nowy alt, napis „Nadchodzące wydarzenia”, opakowanie `div[data-wydarzenia-blok]` wokół siatki wydarzeń.
   - Skrypt nagłówka zmienił się na wszystkich stronach, ale na komputerze działa jak dotąd.
   - Położenie i kolory elementów strony głównej (1280×900) identyczne. Wyjątki: szerokość nowego napisu i wysokość „Warto wiedzieć”, która zmienia się przy każdym wczytaniu, bo sekcja losuje kolejność.
9. `pola-do-cms.md` — sekcja „Zlecenie 06”.
10. Ten wpis.

Odstępstwa od zlecenia i powody:
- Strefa Z = wysokość banera (100svh) − pas zamiast `innerHeight − pas`. W emulacji to samo. Na telefonie z chowanym paskiem adresu `innerHeight` rośnie, a baner przykleja się zawsze po 100svh − pas.
- Po kliknięciu przycisku w banerze fokus idzie na nagłówek „Na skróty” (`tabindex="-1"`). Przycisk zaraz znika, więc inaczej fokus by przepadł.
- Ukryta nazwa w nagłówku (`.brand-txt`) ma też `visibility: hidden`, żeby nie była niewidocznym celem Tab.
- Tytuł w dwóch liniach przez `width: min-content`, bez `<br>` (bez zmiany znaczników komputera).
- Timer 140 ms tylko bez `scrollend` i po `touchend` (prototyp używał obu sposobów zawsze).
- Bez `baner.zdjecie` telefon zostaje przy dzisiejszym wyglądzie. Bez `zdjecie_telefon` dostaje zdjęcie komputera przycięte do kadru.
- Przy ok. ≤ 400 px link „Kalendarz →” przechodzi pod dłuższy nagłówek „Nadchodzące wydarzenia” (sekcja zawija się jak dotąd).
- Bez JS u góry banera zostaje ok. 107 px ciemnego pasa pod nagłówkiem (zdjęcie zaczyna się na 107 px).

Co sprawdzić na prawdziwym telefonie: płynność zwijania i dociągania (tu tylko symulacja zdarzeń), zachowanie przy chowanym pasku adresu, CLS.

Pytania do użytkownika:
- **Prawa do zdjęcia:** baner telefonu to kadr z fotografii fotopolska.eu nr 1158570 (autor: Corvus), powiększony do 884×1779. Przed pushem trzeba ustalić prawo do publikacji i treść podpisu (`baner.podpis_telefon`, dziś pusty).
- Nowy alt (`baner.opis`) jest wspólny dla obu zdjęć, więc zmienił się też na komputerze. Czy tak może zostać?
- W EN podtytuł ma 2 linie, więc otoczka obejmuje całą szerokość ekranu. Czy to w porządku?
- Hasło „Badania, studia i popularyzacja” / „Research, education and outreach” jest robocze, do zatwierdzenia.

## 05-animacje-instytut-ogolne (uzupełnienie) — 2026-11-01 14:05
Status: zrobione (odpowiedź na pytanie z 05: „Tak, motyl”)
Commit: `a7422bd4` (lokalny, bez pushu)

Zmienione pliki:
- `src/lib/motywyBanerow.ts`: reguła `'instytut/infrastruktura-informatyczna/*': 'motyl'`. 8 podstron Infrastruktury informatycznej (PL i EN, razem 16) ma sieć motylkową jak strona nadrzędna zamiast dendrytu z działu.

Sprawdzone:
- `npm run build` bez błędów.
- Komputer bez zmian: HTML 748 stron identyczny z buildem po 06, poza znacznikiem `data-animacja` na tych 16 stronach.
- Telefon 390 px, wszystkie 18 stron (z nadrzędną, PL i EN):
  - motyw `motyl` startuje i wczytuje tylko swój kod;
  - płótno zaczyna się 6 px pod paskiem (67 px) i kończy najpóźniej w połowie hasła albo ostatniej linii tytułu;
  - rysunek się pojawia; przy krótkich tytułach pole ma 68 px wysokości, ale sieć się mieści.

Co sprawdzić: podstrony z krótkim tytułem (np. „Tablica interaktywna”) — niska sieć w wąskim polu.

## 08-poprawki — 2026-11-01 14:50
Status: zrobione — oba punkty z pliku w chwili startu: 1. Nauka, atraktor bliżej prawej krawędzi; 2. Aktualności, fala Fouriera od końca „← Strona główna”.
Commit: `ae6d5d96` (lokalny, bez pushu)

Zmienione pliki:
- `src/scripts/baner/motywy/lorenz.ts`: po obrocie i zmniejszeniu cały rysunek przesunięty w poziomie tak, że najdalszy prawy punkt trajektorii (tej, po której jedzie kometa) leży na `G.x1`. Wielkość, obrót, pion i start komety (liczony po przesunięciu) bez zmian.
- `src/scripts/baner/motywy/fourier.ts`: fala od `G.link.r` do `G.x1`, liczba okresów `round(długość / 120)` (co najmniej 1). Bez linku od `G.x0` jak dotąd.
- `src/scripts/baner/typy.ts`, `src/scripts/baner/silnik.ts`: nowe pole `Pole.link: Linia | null`, czyli linia linku „←” (`t`, `b`, `r` — prawy koniec tekstu, bez granicy zanikania). Maska bez zmian.

Kryteria odbioru (build, serwer plików; ramki bez paska przewijania, bo w ukrytym panelu pasek zabierał 15 px szerokości):
- Punkt 1 (Lorenz):
  1. Prawy brzeg rysunku 16,0 px od prawej krawędzi przy 390 i 430 px, 15,2 px przy 360 px (grubość linii); `/nauka/` i `/en/nauka/` — spełnione.
  2. Granice z 07 — spełnione: płótno 67–170 px (pasek 61 + 6, połowa hasła 171), maska bez zmian.
  3. Ograniczony ruch — spełnione: gotowy rysunek, prawy brzeg 374,7 px przy 390.
  4. Komputer bez zmian — spełnione: HTML 748 stron identyczny z poprzednim buildem (silnik działa tylko na telefonie).
- Punkt 2 (Fourier):
  1. `/aktualnosci/` i `/en/aktualnosci/` — spełnione. Pierwszy punkt fali na końcu tekstu linku: PL 141,6 px (360, 390), 142,8 (430); EN „← Home” 81,7 / 82,9. Fala narysowana bez maski zaczyna się 1,5 px wcześniej (grubość linii) i kończy na `G.x1`.
  2. Budowanie, oddychanie i rozkłady — bez zmian w kodzie; granice z 07 jak w pkt 1.
  3. Ograniczony ruch — spełnione: gotowa fala od 143 px (PL) i 83 px (EN) do prawego brzegu.
  4. Komputer bez zmian — jak w pkt 1.

Co sprawdzić na telefonie: na stronie Aktualności początek fali przy końcu linku widać głównie nad linią linku i pod nią, bo przy samym tekście działa maska. Na EN fala zaczyna się dużo bardziej w lewo (krótki link) i gaśnie pod tytułem.

## 11-poprawki-i-podstrony — 2026-11-05 12:28
Status: zrobione — zalecenia 1–17, 19, 20 (3 sprawdzone bez zmian, 12 zrobione wcześniej na `wyglad/en`); **18 CZEKA — nie wykonane**. Gałąź `wyglad/zlecenie-11` (z `origin/wyglad/en`), 15 commitów `598d2a11`…`1a2ef702` + commit raportu, bez pushu. Szczegóły: `RAPORT-ZLECENIE-11.md`, zrzuty `raport-zrzuty/z11-*`.

Zmienione pliki (główne):
- Style: `src/styles/zalozyciele.css` (paleta, ciemny motyw, `--line-ui`, `--rule`, `--panel`, znak ciekawostki), `zal-tresc.css` (przyciski, pola, wzorzec treści), `zal-telefon.css`, `zal-granty-plan.css`.
- Nagłówki i strony: `src/components/zal/NaglowekZ.astro` (hasło i liczby razem, liczby w jednym rzędzie, długie tytuły, ciekawostki), `Podstrona.astro` (slot `bok`), strona główna (barwienie, górna linia, liczby nad „Szybkim dostępem”), menu działu i hamburger, przełącznik języka; Kalendarz, Aktualności, Pracownicy, Seminarium, Publikacje, Władze, Granty.
- Skrypty: `src/scripts/zal/przejazd.ts` (okładka ↔ Szybki dostęp).
- Nowe: `src/data/ciekawostki/{instytut,nauka,studia,popularyzacja}.json` + `README.md`, `src/lib/ciekawostki.ts`; `dok/en/TLUMACZENIA.md` sekcja 6.
- `.przekazanie/pola-do-cms.md` — sekcja „Zlecenie 11”.

Kryteria odbioru:
- Build bez błędów (748 stron). `astro check`: 3 błędy jak przed zleceniem (`process` w `astro.config.mjs`); nowy błąd z zalecenia 20 poprawiony (`eab091a0`). `astro check` uruchamiany z osobnej instalacji `@astrojs/check@0.9.4` + `typescript@5.6.3` w katalogu tymczasowym — **bez zmian w `package.json`**.
- Edge (Playwright), 1366–3440 i 390 px, jasny i ciemny motyw; wyniki pomiarów przy każdym zaleceniu w raporcie.
- Ciekawostki: dwie wizyty różne (14/14 stron Studiów), zestaw stały w obrębie wizyty, 0 powtórzeń w 40 losowaniach, bez mignięcia, działa bez JS i bez `sessionStorage`, tytuły nie wchodzą na tytuł strony (≥ 40 px).
- Przejazd okładki: 32/32 w Edge; iOS i Android niesprawdzone (brak urządzeń).

Odstępstwa: ciemny motyw tylko przez `[data-theme="dark"]`; Rekrutacja w ciemnym z granatowym napisem; liczby nad „Szybkim dostępem” gasną przy najechaniu środkowych działów w niskich oknach; ciekawostki bez JS kolejne z puli zamiast pierwszej; zestaw ciekawostek losowany przy pierwszej stronie działu; SIAD i Granty przy 1366/1440 o jedną liczbę mniej (szerszy opis znaku). Powody w raporcie.

Pytania (12, pełna lista w raporcie): ramki 3:1 w jasnym (`--line-ui: #8c8679`, niewdrożone); pole `przyciski` kierunków i link ISIM; `/nauka/sukcesy/historia` bez linku; „referaty” zamiast „seminaria” w liczbach okładki; szkic mocniej na telefonie; kadr zdjęcia Studiów na telefonie i autor; liczby pod opisem ciekawostki; pula ciekawostek w linii (18–43 KB po kompresji) czy w pliku; rektor Marczewski 1953 czy 1957–1962; test przejazdu na telefonach; angielska strona Wydziału.

Do zrobienia w CMS: wgrać `raport-zrzuty/z11-17-studia-hs-3200.jpg` jako `public/pliki/naglowki/studia.jpg` (Web-Ustawienia); wpisać hasła stron z liczbami (59 stron PL i EN — lista w raporcie); usunąć USOSweb z menu Studiów (`nawigacja.json`); zweryfikować ciekawostki.

## 13-plynnosc — 2026-11-05 15:10
Status: zrobione — punkty 1–10. Gałąź `wyglad/zlecenie-13` (z `wyglad/zlecenie-11`, `e8ae1099`), 9 commitów `143edb34`…`d153aada` + commit raportu, bez pushu. Szczegóły: `RAPORT-ZLECENIE-13.md`, zrzuty `raport-zrzuty/z13-*`.

Zmienione pliki (główne):
- Nowe: `src/components/ZdjecieZ.astro` (zdjęcia przez `astro:assets`: AVIF/WebP, `srcset`, `sizes` z pola kadru, rozmyta wersja w linii), `src/components/Fonty.astro` (`@font-face` latin/latin-ext/greek, preload, kroje zastępcze z metrykami).
- `src/lib/zdjecia.ts` (`rozmiarPola`, malutkie wersje z `sharp`), `src/layouts/Baza.astro` (kroje, `speculationrules` z `prerender`, pusty `touchstart`), `NaglowekZ.astro` i `Okladka.astro` (skrypty w linii: rysowanie szkicu, układ okładki), `SpisStrony.astro`, `menu.ts`, `okladka.ts`, `drugi-ekran.ts`, `szkice.ts`.
- Style: `global.css` (zmienne rytmu `--rytm`, `--t-*`; `:active`), `zalozyciele.css` (warstwy paska, okładka), `zalozyciele-strony.css`, `zal-dzialy.css`, `zal-podstrona.css`, `zal-tresc.css`, `przejscia.css`, `telefon.css`; zdjęcia w widokach (aktualności, obrony, Warto wiedzieć, zakłady, Władze, sukcesy).

Kryteria odbioru:
- Lighthouse przed/po (4 strony × komputer i telefon, mediana z 3): wynik telefon 73/87/69/93 → 82/92/95/93, komputer 94/99/98/97 → 98/100/100/100; CLS ≤ 0,003 (przed do 0,189); waga strony głównej na komputerze 1764 → 851 KB.
- Zrzuty bez zmian w wyglądzie (porównanie pikseli 1440 i 390 px; różnice tylko w miniaturach AVIF i w liczbie wydarzeń zależnej od godziny budowania).
- Szkic rysuje się od pierwszej klatki na `astro preview` przy Fast 3G (Nauka, Studia, Instytut).
- 4× wolniejszy CPU: bez długich klatek w animacjach; rozmycie paska zostawione (wyłączenie nic nie zmienia).
- bfcache: 14 stron × 2 — wszystkie z pamięci.

Narzędzia: Lighthouse 12.2.1 przez `npx` i Playwright w katalogu tymczasowym; `sharp` — zależność, którą Astro już ma. **Bez zmian w `package.json`.** Bez service workera.

Pytania (9, pełna lista w raporcie): preload krojów a Fast 3G (dławienie DevTools: pierwsza klatka o ~0,4 s później; Lighthouse: lepiej); kroje zastępcze na Androidzie; pominięta cyrylica i wietnamski; czas budowania (cache `node_modules/.astro` w Actions); osobny kadr okładki na telefon; ekrany 1×; galeria w aktualnościach; prerender tylko w Chromium; krótsze „Zobacz więcej”.

## 14-poprawki-po-11 — 2026-11-05 20:40
Status: zrobione zalecenia 25, 26, 23, 24, 27, 28. **Nie zrobione: 21 (CZEKA) i 22 (polecenie z czatu „nie wykonuj zaleceń 21 i 22”; w zleceniu dopisek „dalej od 22” — pytanie w raporcie).** Gałąź `wyglad/zlecenie-14`, bez pushu. Szczegóły: `RAPORT-ZLECENIE-14.md`, zrzuty `raport-zrzuty/z14-*`.

Do zrobienia przed publikacją: nałożyć `dok/latki/zlecenie-14/Web-Ustawienia.patch` (bez niej link „O stronie” w stopce daje 404) i wpisać adres redakcji na „O stronie”.

Zmienione pliki (główne): `zalozyciele.css` (paleta, panel, linia patrona), `Link.astro`, `src/lib/url.ts`, `src/plugins/rehype-zewn.mjs` i około 20 widoków (strzałki ↗), `PanelMenu.astro`, `src/scripts/zal/menu.ts`, `src/lib/menu.ts`, `StopkaZ.astro`, `i18n.ts`, `Okladka.astro` (zerowanie wizyty).

Sprawdzenie: `astro check` 6 błędów, żaden nowy (3 `process` w `astro.config.mjs`, 3 w `src/lib/zdjecia.ts` ze zlecenia 13). `dist/`: 0 linków wewnętrznych z `zew`, 0 `target="_blank"`, wyjątki w raporcie. Porównanie 745 stron ze zleceniem 13 znalazło 3 błędy tego zlecenia, naprawione osobnymi commitami (liczby banera, tytuły konferencji, „Rekrutacja ↗”).

Pytania (6, pełna lista w raporcie): zalecenie 22; filtr USOSweb i skrót SIAD w menu telefonu; panel rozwinięty na bieżącym dziale; ↗ przy każdym przedmiocie w Planie zajęć; adres redakcji; `@types/node`.

## 15-popularyzacja — 2026-11-05 21:05
Status: zrobione punkty 1–6. Gałąź `wyglad/zlecenie-15` (z `14fbe3cb`), 6 commitów `f04cc238`…`d609bd87` + commit raportu, bez pushu. Szczegóły: `RAPORT-ZLECENIE-15.md`.

Do zrobienia przed publikacją: sprawdzić sześć punktów „Do potwierdzenia” (raport), przejrzeć tłumaczenie, nałożyć łatki `dok/latki/zlecenie-15/Web-Popularyzacja.patch` i `Web-Ustawienia.patch`.

Zmienione pliki (główne): `src/views/Popularyzacja.astro`, `src/lib/widoki/popularyzacja.ts`, `TrescDzialu.astro` (jeden układ wierszy), `zal-dzialy.css`, `zal-tresc.css`, nowa wtyczka `src/plugins/rehype-bloki.mjs` i pole `bloki` w kolekcji `strony`, `src/lib/markdown.ts`, `astro.config.mjs`, `src/lib/widoki/strona.ts`, `NastepnaStrona.astro`, `patroni.ts`, `.gitignore`.

Nakładka zmieniona i **nieprzywrócona** (polecenie w zleceniu): `src/data/popularyzacja.json`, `src/data/nawigacja.json`, nowy katalog `src/content/strony/popularyzacja/`; oryginały w `.przekazanie/robocze/nakladka-przed-15/`.

Sprawdzenie: `astro check` 6 błędów, żaden nowy. Zrzuty 1440, 1920 i 390 px, jasny i ciemny, PL i EN; obok prototypu w raporcie. Bez sprawdzenia w samym Pages CMS.

Pytania (5, pełna lista w raporcie): trzecia liczba w banerze nie mieści się o 9 px; krótkie etykiety spisu; bloki w edytorze CMS; pole `linki`; pole `podstrona` w ciekawostkach.

## 16-wersja-angielska — 2026-11-05 21:51
Status: zrobione D1, D2, D4, D5, D6, D8, D10, D11, D14, D15, D16, D19, D20; D18 potwierdzone; D3, D7, D9, D12, D13, D17 bez zmian (decyzje). Gałąź `wyglad/zlecenie-16` (z `9fd255ee`), 12 commitów `cfe65d03`…`1137c1fe`, 2 commity decyzji o obronach (`4fe03c13`, `ac7855c2`), zalecenie 22 ze zlecenia 14 (`8f0019b2`), naprawa układu (`775aa7bf`), naprawa paska i okładki (`f6c64acf`) i 4 commity raportu, bez pushu. Szczegóły: `RAPORT-ZLECENIE-16.md`.

Decyzja właściciela po raporcie („Usuń”): osiem obron bez `tresc_en` (Web-Aktualnosci `feeacb9`, łatka odświeżona); tekst angielski składa widok i sam dobiera czas. Druga decyzja („Tak, zmień”): to samo po polsku, osiem obron bez `body` (Web-Aktualnosci `af154c1`), kod `src/lib/widoki/obrona.ts` i `src/views/Obrona.astro` (`ac7855c2`).

Do zrobienia przed publikacją: wkleić `skrypty/powiadomienia/Code.gs` do Google i wdrożyć nową wersję, przejrzeć tłumaczenia D4, D6, D8, 31 nazw przedmiotów i notki patronów, napisać „push”.

Repozytoria treści: 36 commitów w 20 klonach `C:\Users\Szymek\Documents\GitHub\tresci\`, bez pushu. Wszystkie łatki (`dok/latki/zlecenie-14`, `-15`, `dok/en/latki`, `dok/latki/zlecenie-16`) weszły czysto, bez `-3`.

Zmienione pliki (główne): `src/lib/osoby.ts`, `src/lib/i18n.ts`, nowy `src/lib/jezykTekstu.ts`, `src/layouts/Baza.astro`, `StopkaZ.astro`, `TytulReferatu.astro`, `TrescDzialu.astro`, `DrugiEkran.astro`, `src/pages/404.astro`, nowy `src/views/Powiadomienia.astro` i `src/pages/en/powiadomienia.astro`, `src/plugins/rehype-base.mjs`, `src/content.config.ts`, `skrypty/powiadomienia/Code.gs`, widoki grantów, seminariów, aktualności, kierunków.

Nakładka zmieniona i **nieprzywrócona** (polecenie w zleceniu); oryginały w `.przekazanie/robocze/nakladka-przed-16/`.

Sprawdzenie: `astro check` 6 błędów, żaden nowy; `sprawdz_tresci.py` OK (555 plików). Zrzuty 1440 i 390 px przed/po, 1920 px ciemny motyw, otwarte menu. Bez czytnika ekranu, Pages CMS i samego Google Apps Script.

Pytania (8, pełna lista w raporcie): „dr, prof. UWr”; „Mathematical Analysis” a „Advanced calculus”; „Iuvenes Wratislaviae”; „Admission” na stronie głównej bez dopisku; USOSweb; wpisy testowe; zalecenie 22 na telefonie; ciekawostka w banerze nachodząca na tytuł przy oknach 761–900 px.

## 14-poprawki-po-11, zalecenie 22 — 2026-11-05 23:35
Status: zrobione na polecenie właściciela, na gałęzi `wyglad/zlecenie-16`, osobnym commitem `8f0019b2`, bez pushu. Opis w `RAPORT-ZLECENIE-16.md`; `RAPORT-ZLECENIE-14.md` celowo bez zmian. Zalecenie 21 nadal CZEKA.

Zmienione pliki: `src/components/zal/DrugiEkran.astro`, `src/scripts/zal/drugi-ekran.ts`, `src/styles/zalozyciele-strony.css`, `src/components/WierszAktualnosci.astro`, `src/views/ListaAktualnosci.astro`. Bez nowych pól CMS.

Sprawdzenie: `astro check` 6 błędów, żaden nowy; `sprawdz_tresci.py` OK (555 plików). Główna i lista na 5 szerokościach, PL i EN, jasny i ciemny, filtry i szukanie; prototyp obok wyniku w raporcie. Bez Firefoksa, Safari i prawdziwych telefonów.

Decyzja właściciela po raporcie („Tak, napraw obie”), commit `775aa7bf`: pasek Studia i Warto wiedzieć na głównej poniżej 1366 px, lista Aktualności bez pustej kolumny poniżej 1368 px (klasa `z-pd-bez-boku`). Pliki: `src/styles/zalozyciele-strony.css`, `src/styles/zal-podstrona.css`, `src/views/ListaAktualnosci.astro`, `src/components/WierszAktualnosci.astro`.

Decyzja właściciela po raporcie („Tak, napraw”), commit `f6c64acf`, plik `src/styles/zalozyciele.css`: poniżej 1024 px linki tylko w panelu z burgera, przy 1024–1119 px bez podpisu Wydziału, nazwy działów na okładce maleją z oknem, panel co najmniej 360 px. Burger na podstronach był poza ekranem przy 761–971 px (EN 761–906 px). Pomiary w Edge bez alarmów; bez Firefoksa, Safari i prawdziwych urządzeń.

## 17-uwagi-z-ogladania — 2026-11-06 01:15
Status: zrobione punkty 1–6, na gałęzi `wyglad/zlecenie-16`, osobne commity, bez pushu. Raport: `RAPORT-ZLECENIE-17.md`.

Commity: klon Web-Instytut `7c43bdb` (punkt 1, kopia nakładki w `robocze/nakladka-przed-17`); Web-Core `3c3aa7ff` (2, panel testowy skali, tylko dev), `894017f8` (3, pas linków), `82d55d7b` (4, baner seminarium), `f0ba658c` (5, partnerzy bez domen), `f20a2b1e` (6, siatka boksów), `79621f12` (wąskie okna po punktach 3 i 4).

Ponad zlecenie: koordynatorzy i boksy w jednej kolumnie przy oknie 761–979 px; `white-space: nowrap` usunięte z linków pasa działu. Bez nowych pól CMS i zależności npm. Pole `haslo` seminariów: strona seminarium go nie używa, lista `/seminaria` tak.

Sprawdzenie: `astro check` 6 błędów, żaden nowy; `sprawdz_tresci.py` OK (555 plików); 30 stron (PL i EN) na 6 szerokościach od 390 do 1536 px i na granicy 979/980 px. Bez Firefoksa, Safari, prawdziwych telefonów i czytnika ekranu.

Pytania i decyzje czekające na właściciela są na początku raportu: wybór skali, inne linki z samą zmianą koloru, push.

## 18-uwagi-z-ogladania-2 — 2026-11-06 10:10
Status: zrobione wszystkie punkty GOTOWE (1–19), na gałęzi `wyglad/zlecenie-16`, osobne commity, bez pushu. Raport: `RAPORT-ZLECENIE-18.md`. Punkty 1–5 zrobiła wcześniejsza sesja, bez raportu; ta sesja: 6–19.

Commity: `da484544` (1), `4265fac4` (2), `15e58e19` (3), `2f2cc10f` (4), `70c3c6f9` (5), `3d91ed60` i `a1fca71b` (6), `ed8b9d9e` (7), `61cbbd0e` (8), `df04dde6` (9), `f5c355d1` (10), `f4e791c7` (11), `c9059874` (12), `9da772d4` (13), `7a6a3bf6` (14), `1c9c52f1` (15), `87d5339a` (16), `dc2b3b58` (17), `68ca1a7f` (18), `388bfdf9` (19). Klon Web-Ustawienia: `9e91818` (5), `e3d250a` (7), bez pushu.

Zmienione pliki: `src/components/Naglowek.astro`, `NaglowekStrony.astro`, `WierszAktualnosci.astro`; `src/components/zal/DrugiEkran.astro`, `NaglowekZ.astro`, `Okladka.astro`, `PanelMenu.astro`, `PasekMenu.astro`, `Podstrona.astro`, `SpisStrony.astro`, `TrescDzialu.astro`; `src/dev/panel-wariantow.ts`; `src/layouts/Baza.astro`; `src/lib/i18n.ts`, `liczbyTerminow.ts`, `menu.ts`, `patroni.ts`, `widoki/listaAktualnosci.ts`; `src/scripts/zal/drugi-ekran.ts`, `menu.ts`, `pasek.ts`, `przejazd.ts`; `src/styles/global.css`, `telefon.css`, `test-warianty.css`, `uklad-zwarta.css`, `zal-dzialy.css`, `zal-granty-plan.css`, `zal-menu.css`, `zal-podstrona.css`, `zal-przejscia.css`, `zal-telefon.css`, `zalozyciele-strony.css`, `zalozyciele.css`; `src/views/Aktualnosc.astro`, `ListaAktualnosci.astro`, `PlanZajec.astro`; nowy `RAPORT-ZLECENIE-18.md`; nowe `raport-zrzuty/z18-*` (126). Klon i nakładka (poza gitem Web-Core): `src/data/nawigacja.json`, nowy `public/pliki/naglowki/aktualnosci-skok.jpg`; kopia oryginału w `.przekazanie/robocze/nakladka-przed-18/`.

Kryteria odbioru:
- `astro check` bez nowych błędów: spełnione (6 błędów, ten sam stan co przed zleceniem).
- `npm run build`: spełnione (759 stron, `pagefind` 744). Dodatkowo `sprawdz_tresci.py` OK (555 plików). `pobierz_tresci.py` nieuruchamiany.
- Regresja końcowa: spełnione z jednym wyjątkiem. 17 stron PL i EN przy 8 szerokościach od 320 do 2560 px, 272 wejścia na serwerze deweloperskim: HTTP 200, bez błędów JS, bez przewijania w poziomie, poza `/studia/sprawy-studenckie` przy 320 px (8 px, tabela w treści, poza zleceniem, pytanie w raporcie).
- Punkty 1–5: nie sprawdzałem ponownie osobno. Zrzuty `z18-wpis-*` z punktu 4: niespełnione, nie ma ich w `raport-zrzuty` (pytanie w raporcie). `z18-aktualnosci-baner-*`: są.
- Punkt 6: spełnione. W `dist` 0 plików z `menu-telefon` i `mnav`. Skrypt Playwright: kolejność, szukanie, brak USOSweb, bieżący dział i strona na komputerze i telefonie, PL i EN. Panel bez przewijania przy 1536×730, 1366×640, 1920×950, wysokości w raporcie (Studia 620 / 604 / 620, EN 651 / 635 / 651). Telefon 390×780 przewija się panel. Klawiatura i bez JS sprawdzone. SIAD jako skrót: spełnione po polsku, w EN skrótu nie ma (pytanie). Bfcache tylko symulowany. Zrzuty `z18-menu-*`.
- Punkt 7: spełnione. Osoba cała przy 2560, 2048, 1536, 800, 390, 320 px, sprawdzone na zrzutach; filtr `none`. Kadr zmieniony na 48% 63%, podany w raporcie. Zrzuty `z18-aktualnosci-baner-foto-*`.
- Punkt 8: spełnione. 1536×730: 7 wpisów, 1920×940: 10, pomiar skryptem.
- Punkt 9: spełnione poza opisem w `dok/estetyka.md`: pliku nie ma w repozytorium. Funkcja w `src/lib/patroni.ts`, tabela 15 wpisów w raporcie.
- Punkt 10: spełnione. Kontrast ≥ 4,5:1 na każdym banerze, mierzony na najjaśniejszym pikselu, tabela w raporcie. Zrzuty `z18-pasek-*`.
- Punkt 11: spełnione. Pomiary i zrzuty `z18-telefon-akt-*`.
- Punkt 12: spełnione. Co 1 px od 320 do 760: najwyżej 3 linie, pasek 61 px; krój równy z komputerem, zmierzony. Okładka mieści się przy 360×640 i 390×760. Bez JS: Wydział. Bfcache tylko symulowany. Zrzuty `z18-okladka-telefon-*`.
- Punkt 13: spełnione. `v` i `X` w raporcie, proporcje 2,273. X przy pełnej wysokości ekranu 87–91%, nie 92% jak w tabeli zlecenia (przyczyna w raporcie). Zrzuty `z18-okladka-*`.
- Punkt 14: spełnione. Instytut przy 390: 344 px; wysokości w raporcie. Podpis bez nakładania przy 320, 360, 390, PL i EN, po poprawce. Zrzuty `z18-baner-dzial-*`.
- Punkt 15: spełnione. Cała pula rysunków, z pudełek ścieżek: 0 poza banerem i ekranem. Zrzuty `z18-znak-telefon-*`.
- Punkt 16: spełnione poza „dwie linie” dla najdłuższych nazw (EN „Diploma and student affairs” 3–4 linie, „Wydarzenia naukowe” przy 320 px 3 linie). Pas 92–97 px przy 390 PL; EN Studia 115 px. Klawiatura, `aria-expanded`, bez JS sprawdzone; czytnika ekranu nie. Zrzuty `z18-pas-karty-*`.
- Punkt 17: spełnione. Bez pustego pasa przy 320–430 px; plik 1920 px przy 390 px i 2×. Zrzuty `z18-studia-tablice-*`.
- Punkt 18: spełnione. Brak spisu przy 390 px, PL i EN; kotwice działają; komputer sprawdzony. Zrzuty `z18-bez-spisu-*`.
- Punkt 19: spełnione. Zimowy 187 z 300, 17 807 px; letni 293 z 304, 16 245 px; wyszukiwarka na komputerze działa. Zrzuty `z18-plan-telefon-*`.

Odstępstwa od zlecenia i powody (szczegóły przy punktach w raporcie):
- Punkt 6: drzewo robocze było czyste, punkt leżał w `3d91ed60` bez „Szerszego panelu”, więc drugi commit `a1fca71b`. `--marg` w panelu z granicą 340 px; okno niższe niż 660 px o 16 px ciaśniej.
- Punkt 7: kadr, szerokość zdjęcia 62% do 1270 px, telefon 78% od prawej.
- Punkt 8: poniżej 1180 px wyróżniony ze zdjęciem nad tekstem; kolor „czytaj dalej” jak w podglądzie.
- Punkt 10: pasek jasny od dolnej krawędzi; Aktualności 60% krycia; nazwa przejścia przeniesiona na `.z-pasek-in`.
- Punkt 12: cztery ustępstwa w pasku, żeby krój został bez zmian.
- Punkt 13: zanik dołu zdjęcia na telefonie, reguła dla orientacji poziomej, wysokość z pomiaru, szersze `sizes`.
- Punkt 14: mniejszy i wyższy podpis na wąskich ekranach.
- Punkt 16: przenoszenie długich nazw z dywizem.
- Testy w Chrome 156 zamiast Edge, który po aktualizacji nie startuje pod Playwrightem. Bez Firefoksa, Safari, prawdziwych telefonów i czytnika ekranu.

Pytania do użytkownika (pełna lista na początku raportu): krycie 60% na Aktualnościach; pas na okładce; podtytuł na innych stronach EN przy 421–490 px; długa nazwa grupy EN; SIAD po angielsku; brak `dok/estetyka.md`; brakujące zrzuty `z18-wpis-*`; Sprawy studenckie przy 320 px; oryginał zdjęcia; push.

## 19-uwagi-z-ogladania-3 — 2026-11-06 10:35
Status: zrobione wszystkie punkty GOTOWE (1–3), na gałęzi `wyglad/zlecenie-16`, osobne commity, bez pushu. Raport: `RAPORT-ZLECENIE-19.md`. Zlecenie jest otwarte; punkty dopisane po 10:29 nie są objęte.

Commity: `a7b61e45` (1), `2eeb7d89` (2), `c59eb46e` (3).

Zmienione pliki: `src/lib/tresci.ts`, `src/components/WierszAktualnosci.astro`, `src/components/zal/Okladka.astro`, `src/styles/zalozyciele.css`, `src/styles/zal-telefon.css`; nowy `RAPORT-ZLECENIE-19.md`; nowe `raport-zrzuty/z19-*` (22).

Kryteria odbioru:
- `astro check` bez nowych błędów: spełnione (6 błędów, ten sam stan). `npm run build`: spełnione (759 stron, `pagefind` 744). `sprawdz_tresci.py` OK (555 plików). `pobierz_tresci.py` nieuruchamiany.
- Regresja: 17 stron PL i EN przy 7 szerokościach od 320 do 2560 px, 238 wejść: HTTP 200, bez błędów JS, bez przewijania w poziomie, poza `/studia/sprawy-studenckie` przy 320 px (8 px, sprzed zlecenia, pytanie w raporcie 18).
- Punkt 1, ten sam dział na obu widokach: spełnione, skrypt, 12 wspólnych wpisów, 0 różnic, PL i EN; tabela 15 wpisów w raporcie.
- Punkt 1, kontrast ≥ 4,5:1 w każdym kolorze, obu motywach, także na boksie: spełnione, najmniej 5,24:1, liczone z kolorów obliczonych w przeglądarce. Zrzuty `z19-akt-kolory-*`.
- Punkt 1, opis w `dok/estetyka.md`: niespełnione, pliku nie ma w repozytorium; opis w komentarzu w `WierszAktualnosci.astro`.
- Punkt 2, tabela dla 6 okien, osobno PL i EN: spełnione, w raporcie. Odległość końców od łuku 58 ± 2 px: spełnione w poziomie (58 ± 0,1), po promieniu 50–57 px. Monotoniczny: tak wszędzie. Bez nachodzenia na szkice i markę: spełnione, odstęp do szkiców co najmniej 24 px.
- Punkt 2, proporcje zdjęcia: spełnione, 2,273–2,274 przy naturalnych 2,271–2,277. Zrzuty `z19-luk-*`. Telefon bez zmian: spełnione, pomiary przed i po identyczne przy 360, 390, 430 px, zrzuty przy 390 px.
- Punkt 2, wartości kontrolne: niespełnione co do stopni i R w EN, różnica większa niż „kilka px”, bo tabela powstała w Times; wyjaśnienie i warianty stałych w raporcie.
- Punkt 2, opis w `dok/estetyka.md`: niespełnione, pliku nie ma; opis w nagłówku `Okladka.astro` i przy `ULOZ`.
- Punkt 3, podpis na wysokości ostatniej linii opisu: spełnione, 0,3 px, wszystkie działy, 320–430 px, PL i EN.
- Punkt 3, bez nachodzenia szkicu i podpisu na tekst: spełnione, punkty na kreskach kontra prostokąty tekstu, co 2 px od 320 do 440, 488 pomiarów, 0 kolizji.
- Punkt 3, wysokość jak po punkcie 14 zlecenia 18: częściowo. Instytut, Nauka i Studia bez zmian przy 390; Popularyzacja 354 zamiast 335 (EN 346 zamiast 328); EN Studia przy 360: 347 zamiast 329. Wysokości w raporcie. Zrzuty `z19-baner-dzial-*`.

Odstępstwa od zlecenia i powody:
- Punkt 2: `letter-spacing: -.012em` na liniach tytułu, bo dziedziczony z `h1` był stały w px i rozjeżdżał wzory (R 1289 zamiast 968). Krok 5 jednym przeliczeniem liniowym zamiast 2–3 przebiegów.
- Punkt 3: wyższy baner tam, gdzie opis zawija się przez wymagany `max-width`. Reguły dla wąskich ekranów z punktu 14 zlecenia 18 usunięte.
- Testy w Chrome 156 zamiast Edge. Bez Firefoksa, Safari, prawdziwych telefonów i czytnika ekranu. Flaga wstawiona skryptem. Gałąź zapasowego skosu nie została wykonana.

Pytania do użytkownika (pełne na początku raportu): stałe łuku wobec tabeli policzonej w Times; wysokość banera Popularyzacji; brak `dok/estetyka.md`; kolor Instytutu nieużywany na liście Aktualności; bardzo długa flaga przy niskim oknie; push.


## Push i podgląd — 2026-11-06 10:55
Polecenie właściciela: wysłać wszystko na GitHuba, Web-Podglad ma pokazywać najnowszą wersję, starej wersji Web-Core nie ruszać. Zlecenie 20 nie zaczęte („Jeszcze nie jest dopracowywane”).

Co wysłane:
- Web-Core: gałąź `wyglad/zlecenie-16`, `df04dde6..3dd60358` (15 commitów). `main` bez zmian.
- 20 repozytoriów treści (wszystkie klony oprócz Web-Pracownicy, które nie ma zmian): nowa gałąź `wyglad/zlecenie-16` = lokalny `main` klonu + jeden commit z 52 plikami, którymi nakładka różniła się od klonów (hasła, liczby, wstępy działów, `ustawienia.json`, `studia.jpg`). `main` klonów lokalnie bez zmian, nadal przed `origin/main`. Na GitHubie `main` tych repozytoriów bez zmian.
- Web-Podglad `fcdcd85`: `podglad.yml` buduje kod z `wyglad/zlecenie-16`, a treści z `main` z domergowaną gałęzią `wyglad/zlecenie-16` repozytorium (`pobierz_tresci.py --lokalnie`). README zaktualizowane.

Dlaczego nie na `main` treści: `pobierz_tresci.py` bierze HEAD, a `powiadom.yml` po pushu na `main` przebudowuje starą stronę.

Nie wysłane: `public/pliki/baner/instytut-telefon.jpg` (kod go nie używa od zlecenia 18, prawa nieustalone). Pole `zdjecie_telefon` w `ustawienia.json` na gałęzi nadal na niego wskazuje, bez skutku.

Sprawdzenie: przebieg 42197477427 zielony, 759 stron, wszystkie 20 repozytoriów „main + wyglad/zlecenie-16”. Playwright na opublikowanej stronie: 12 adresów PL/EN przy 390×780, 360×640, 1536×730: bez przewijania w poziomie, błędów JS i HTTP. `main` w 22 repozytoriach taki sam przed i po; brak nowego przebiegu publikacji Web-Core po pushu.

Skutki uboczne: `/test-telefon/` na podglądzie to teraz 404, a krok „TEST telefonu” w każdym przebiegu kończy się ostrzeżeniem, bo łatka nie nakłada się na nową gałąź.

Uwaga na przyszłość: zmiana tylko w nakładce nie trafi na podgląd. Musi wejść na gałąź `wyglad/zlecenie-16` właściwego repozytorium treści. Przed startem strony treści z tych gałęzi trzeba przenieść na `main`.

## Przegląd zleceń 01–19 — 2026-11-06 10:55
Na prośbę właściciela, bez zmian w kodzie, po kodzie i raportach, bez przeglądarki i porównań z prototypami.
Pominięcia (potwierdzone w kodzie): 06.4 skrypt chowający zakończone wydarzenia usunięty w `573fe9ce` bez decyzji; 01.7 krótkie linki powrotu na telefonie (martwe pole `telefon` w `Obrona.astro:34`, `Seminarium.astro:46`); 11.4 `.btn` nadal okrągły (`global.css:128`, 404 i Powiadomienia); 06.3 EN „See more” zamiast „Show more”; 13.6 Galeria bez `srcset`; 18.4 brak zrzutów `z18-wpis-*`; 18.9, 19.1, 19.2 brak `dok/estetyka.md` na tej gałęzi.
Odstępstwa i decyzje: 18.3 pasek filtrów przy oknie 761–979 px, dwie kolumny od 1180 px; 11.14 Szkoła doktorska ma hasło i liczby, a zlecenie mówi „tylko liczby”.

## Drobne poprawki po przeglądzie, panel wariantów, zlecenie 20 — 2026-11-06 11:45
Drobne poprawki z przeglądu 01–19: `e1014a4f` (06.4 zakończone wydarzenia znikają w przeglądarce), `93d16ed6` (01.7 krótkie linki powrotu), `0a12ded4` (11 zal. 4 `.btn` bez zaokrągleń), `a43249f6` (06.3 „Show more”). Sprawdzone Playwrightem przy 1536 i 390, z przesuniętym zegarem, bez JS, w obu motywach.
Ograniczenie 06.4: liczba na okładce („1 wydarzenie”) dalej liczy się przy budowaniu, więc może się rozjechać z listą na kilka godzin, do następnej przebudowy.
Do sprawdzenia przy 01.7: zlecenie 17 (punkt 74) wspominało „← Wszystkie seminaria … na telefonie jak dziś”, a teraz na telefonie jest „← Seminaria”.

Panel wariantów (prośba właściciela, `e3545c2e`): `PANEL_WARIANTOW = false` w `astro.config.mjs` wyłącza całą integrację, także skrypt z `data-t-*`. Powrót: `true`. Zapisany wybór zostaje w `localStorage`. Zbudowana strona nigdy go nie miała.

Zlecenie 20: punkt 1 `352f6d49`, punkt 2 `16740eea`, wyniki i odstępstwa od wzoru w `RAPORT-ZLECENIE-20.md`. Treści: Web-Ustawienia `d5834d5f`, Web-Studia `3691cb50` na gałęzi `wyglad/zlecenie-16`, `main` klonów bez zmian.

Uwaga na przyszłość: `npm run build` przy działających serwerach deweloperskich nadpisuje wspólne `node_modules/.vite/deps` produkcyjnym Reactem (`jsxDEV is not a function`, pusta tabela na `/pracownicy` w trybie deweloperskim). Stało się o 11:38, naprawione o 11:42 zapisaniem `astro.config.mjs` (serwery same się restartują i przebudowują pamięć). Sprawdzone na 4321 i 4416. Po każdym buildzie trzeba to powtórzyć.
Podobnie: po zmianie `content.config.ts` dwa serwery naraz zapisują `.astro/data-store.json` i jeden może pokazać chwilowy błąd ENOENT. Mija po odświeżeniu.

Push po zleceniu 20 (11:44): Web-Core `wyglad/zlecenie-16` do `dd80f492`, Web-Ustawienia do `d5834d5`, Web-Studia do `3691cb5`. `main` wszystkich 22 repozytoriów bez zmian względem `main-przed`, bez nowego „Powiadom stronę”.
Web-Podglad: przebieg 42204938647 zielony, wdrożenie o 11:49:59, ale GitHub Pages serwował starą wersję do 11:56. Opublikowana strona sprawdzona po tej godzinie: pas 98 px (EN Studia 121,1), pole 128–1388, opisy na miejscu, menu 685×730 bez przewijania, 36 z 36 adresów przy 390, 360 i 1536 px bez błędów.

Po odbiorze zlecenia 20 (12:20), na prośbę właściciela, bez pushowania: kafelki działu `101b6682` (opis i liczba stron w `--text` po najechaniu i po rozwinięciu, 5,52–9,21), hamburger na komputerze `4a07fd08` (610 → 670 zamiast 640 → 720, margines 28 zamiast 36, ciaśniejsze rzędy do okna 800 px zamiast 660). Przegląd 20 wysokości okna przy 1366 i 1920 px: PL 0, EN 0 od 640 px wzwyż; zniknęło też EN 6 px przy 1536×730. Krzyżyk w miejscu hamburgera, odstęp pola szukania bez zmian. Pomiar najechania: `z20-najazd.mjs` w notatniku sesji, bo `z20-pas.mjs kontrast` liczy „opis najech.” z koloru karty zwiniętej i pokazuje stare wartości.

Push po poprawkach (12:18): Web-Core `wyglad/zlecenie-16` do `d87b9374`, przebieg Web-Podglad 42209285793 zielony.

Zlecenie 21, punkt 1 (12:30): `5b30aa4c`, podtytuł na karcie seminarium kursywą Brygady w `--muted`, jedna reguła w `zal-tresc.css`. Raport `RAPORT-ZLECENIE-21.md`, zrzuty `raport-zrzuty/z21-seminaria-*`. Właściciel kazał wysłać mimo „bez pushowania” w zleceniu: przebieg Web-Podglad 42209881498 zielony, nowa wersja na stronie od 12:29:57, sprawdzona. `main` wszystkich 22 repozytoriów bez zmian. `npm run build` wzięty z tego przebiegu, lokalnie nieuruchamiany, żeby nie psuć serwerów dev.

Zlecenie 21, punkty 2–10 i dwie uwagi dodatkowe (6.11, do 16:00). Commity: punkt 2 `0c8e36aa` i poprawka `58249970`, kreski działów `c58938e7`, punkt 3 `19772490`, nagłówek przy stopce `646dad8a`, punkt 4 `36972ca5`, punkt 5 `30507f14`, punkt 6 `0d151990`, punkt 7 `58e45142`, punkt 8 `846df24b`, punkt 9 `ee9215c3` i poprawka `4c234da8`, punkt 10 `a0a41461`. Raport `RAPORT-ZLECENIE-21.md`, zrzuty `raport-zrzuty/z21-*`.
Push na słowo „Po tym zlecenie 21 i push”: Web-Core `wyglad/zlecenie-16` do `a0a41461`, potem `4c234da8`. Web-Podglad: przebiegi 42226417017 i 42235208419, oba zielone. Pierwsza publikacja nie dotarła na stronę przez 37 minut, pomogło ponowienie samego kroku publikacji. `main` 22 repozytoriów bez zmian.
Na opublikowanej wersji znalazłem własny błąd: wejście na `#szybki-dostep` przy animacji wejścia kończyło 4 z 8 prób poza krawędzią (poprawka `4c234da8`, potem 16 z 16). Właściciel sprawdza na telefonie: prawdziwy pasek adresu, Safari, Android, gest odświeżania.

Zlecenie 22, etapy 0–7 (6.11), lokalnie, bez pushowania. Pobrane z `kopia/2026-11-01-estetyka-prototypy` (`0f04b1fd`) bez scalania, numer 22 był wolny. Web-Core: etap 5 `a43fb368` (na lokalnym `main` `446e98e3`), etap 6 `0ca71fff`. Treści: etap 1 w 18 repozytoriach, etap 2 w Web-Nauka `dcd364f`, Web-Ustawienia `8d7ce42`, Web-Studia `910f99c`, etap 3 gałąź Web-Pracownicy, etap 4 w 7 repozytoriach. Pełna tabela: `RAPORT-ZLECENIE-22.md`.
Klony stały na lokalnym `main` (ich commity są też na gałęzi); przełączone na `wyglad/zlecenie-16`, Web-Pracownicy dosklonowany do `tresci\`. Skrypt kontrolny: 211 problemów w 590 plikach przed, 0 w 567 po. Budowanie w worktree `Web-Core-z22` z własną kopią `node_modules` (żeby nie ruszyć `.vite` serwerów dev): 739 stron, zero danych testowych. Usunięte 53 pliki także z nakładki.
Widoczne wbrew tabeli etapu 2, z powodu: `naglowki_podstron.wariant` (linia pod nagłówkiem) i `pochodzenie` (zdanie nad wykazem, lista wyboru). Decyzja właściciela w raporcie. Czekam na słowo „push”.

Zlecenie 22, etap 8 i założenie etapu 9 (6.11). Właściciel: „Ukryj, potem push”: Web-Ustawienia `8c58e68` ukrywa cały `naglowki_podstron` oraz `haslo`, `haslo_en` w `ustawienia`; `pochodzenie` zostaje widoczne jako lista wyboru. Wypchnięte: `wyglad/zlecenie-16` w 21 repozytoriach treści i w Web-Core, na `main` Web-Core jeden commit `446e98e3`. Publikacja obecnej strony zielona, `/o-stronie/` 404, podgląd z hasłami i bez danych testowych, `main` treści bez zmian.
Harmonogram Web-Podglad nie działa co godzinę, jak zakłada zlecenie: GitHub uruchamia go nieregularnie. Workflow bez zmian, dwa przebiegi ręczne.
`test-cms` założone w sześciu repozytoriach, linki w raporcie. Czekam na zapisy właściciela, potem porównanie. Etap 10 dopiero po „przełącz”.
Na prośbę właściciela po 4 wpisy testowe (wydarzenia, referaty) na 9–19 listopada: Web-Aktualnosci `092316a`, Web-Sem-Rownania-Rozniczkowe `4ff405e`, Web-Sem-Statystyka `d92bebc`, Web-Sem-Prawdopodobienstwo `364ede0`, Web-Sem-Analiza-Harmoniczna `760e34a`. Tylko na gałęzi. Do usunięcia przed startem, lista w `RAPORT-ZLECENIE-22.md`. Uwaga: pierwszy przebieg mojego skryptu zostawił w dwóch klonach plik `tmp.*` poza commitem; usunięte.

Zlecenie 23, punkty 1–6 (6.11), lokalnie, bez pushowania. Zlecenie rosło w trakcie: najpierw punkty 1, 3, 4, potem punkt 2 dostał GOTOWE i doszły 5 i 6. Końcowe pobranie: `c9d3f0a2`, bez nowych punktów. Commity: punkt 1 `f6ec9126`, 3 `db2c0579`, 4 `ca26ba53`, 2 `ecea03d2`, 5 `fd6e6313`, 6 `61ed1dd0`. Raport `RAPORT-ZLECENIE-23.md`, zrzuty `raport-zrzuty/z23-*`.
Punkt 2 z prototypu, z poprawkami znalezionymi na kodzie: otwarcie menu na telefonie przenosiło na Szybki dostęp (panel stoi w tym obszarze), otwarty panel nie był wykrywany na komputerze, kółko na końcu panelu ruszało stronę, kotwica głębiej niż krawędź cofała stronę. Własne zdarzenie `z-okladka` zamiast udawanego `scroll`.
Odbiór na wersji zbudowanej w osobnym katalogu (`--lokalnie`, 747 stron): punkt 2 174 z 174, 288 prób w poziomie bez prawdziwych problemów, sygnet i linia bez uwag. `astro check` 6 błędów jak przed zleceniem. Do sprawdzenia przez właściciela na telefonie: czucie progu, Safari, czytniki, jasna linia z prawdziwym paskiem adresu, laptop dotykowy. Zlecenie 22 nadal na etapie 9, czeka na zapisy w CMS.

Zlecenie 23, wypchnięcie (6.11). Właściciel: „Tak push”. Wypchnięta tylko gałąź `wyglad/zlecenie-16` Web-Core (`714db59e..e0fbfdaa`): 7 commitów zlecenia i poprawka raportu. Przed pushem zlecenie pobrane jeszcze raz: dalej `c9d3f0a2`, 6 punktów. Repozytoria treści bez zmian, `main` bez zmian. Web-Podglad uruchomiony ręcznie (przebieg 42268895461).
CMS: `test-cms` bez zapisów właściciela we wszystkich 6 repozytoriach, etap 9 dalej czeka. Etap 10 po „przełącz”, etap 11 (dokument) jeszcze nienapisany.
Zlecenie 22, etap 9 odłożony przez właściciela („testy edycji zrobimy później”, 6.11), `test-cms` zostają. Etap 10 nieruszony: „zrobić resztę” to nie słowo „przełącz”, a warunkiem jest udany etap 9. Z kodu Pages CMS wynika, że pola ukryte powinny przetrwać zapis; to nie zastępuje próby (opis w raporcie).
Etap 11: `dok/start-strony.md` (`e790df80`), procedury nie wykonano. Dopisane względem zlecenia: warunki przed startem (próba w CMS, usunięcie 8 wpisów i 4 zdjęć testowych, `test-cms`) oraz uwaga o Web-Podglad po starcie. Stan z 6.11: `main` bez własnych commitów w 21 repozytoriach; zlecenie mówi o 20, bo Web-Pracownicy dostało gałąź w etapie 8.
Zlecenie 23 na opublikowanym Web-Podglad (przebieg `42268895461`, zielony): punkt 2 174 z 174, jasna linia 0 z 21 ramek (4 trafienia przez CDP to znany artefakt emulatora), sygnet i obrót 0 problemów. `main` 21 repozytoriów treści bez zmian, Web-Core nadal `446e98e3`. Lokalnie, niewypchnięte: dokument startu i raporty.

Poprawka na prośbę właściciela (6.11): na telefonie po stuknięciu w dział na okładce i powrocie gestem nazwa działu zostawała ciemna, praktycznie niewidoczna. Przyczyna: `:hover` zostaje na linku także po powrocie z bfcache, a wyjątek od globalnego `a:hover` był tylko w stylach komputera. `7de36474`: dwie reguły w `zal-telefon.css` (`.z-okl-dz`, `.z-strzalka`); ciemne są tylko pod palcem. Odtworzone na Web-Podglad: 8 z 8 prób (4 działy, 2 motywy), z regułą 0 z 8. Skan linków na stronie głównej, `/instytut/` i `/studia/`: został tylko `.skip`, który jest wyłącznie dla klawiatury. Lokalnie, bez pushowania.

Menu na telefonie, prośba właściciela (6.11): `b4f99c25`. Panel po każdym otwarciu ma wszystkie działy zwinięte, od góry, i nie koloruje bieżącej strony; `aria-current` zostaje dla czytników ekranu. Komputer bez zmian. Na serwerze lokalnym 392 sprawdzenia, 0 źle (telefon, telefon w poziomie, komputer, oba motywy). `astro check` 6 błędów jak dotąd.
Na słowo właściciela („push i publikacja”): wypchnięta tylko gałąź `wyglad/zlecenie-16` Web-Core, w tym dokument startu, raporty i poprawka `7de36474`. „Publikacja” to przebudowa Web-Podglad; `main` i obecna strona bez zmian.
Na opublikowanym Web-Podglad (przebieg `42278924602`, zielony): powrót gestem 0 z 8 z ciemną nazwą, menu 392 sprawdzenia i 0 źle, próg na telefonie 69 i 0 źle. `main` 21 repozytoriów treści bez zmian, Web-Core nadal `446e98e3`.

Zlecenie 22, etap 9, pierwsza próba właściciela (6.11): zapis odrzucony, „Resource not accessible by integration”. Przyczyna: aplikacji Pages CMS nie ma w organizacji IM-UWr, formularze otwierają się tylko dlatego, że repozytoria są publiczne. Dotyczy też edytorów. Instalację zrobić musi właściciel; zalecone 21 repozytoriów treści, bez `.github`, Web-Core i Web-Podglad. Zapisane w raporcie i `dok/start-strony.md` (`0ab17349`, lokalnie). `test-cms` bez zmian.
Właściciel zainstalował Pages CMS w IM-UWr (6.11, instalacja 179410413) na wszystkich repozytoriach, nie na wybranych 21. Działa, ale aplikacja ma też zapis w Web-Core, Web-Podglad i `.github`; zaproponowane zawężenie. Etap 9: zapisy można robić.

Zlecenie 22, etap 9, wynik (6.11): 9 zapisów właściciela w 6 repozytoriach. Pola ukryte przetrwały, budowa 747 stron przechodzi, 8 stron bez zmian w tekście i strukturze `<main>`. Defekt: rich-text przepisuje listę numerowaną na „Dla uczniów” (dalsze akapity wcięte 2 spacjami), etykiety „Krok N” znikają. Tylko ten 1 z 378 plików. Propozycja w raporcie: wtyczka Markdown; decyzja właściciela. `test-cms` zostaje do tej decyzji. Etap 10 nieruszony, brak słowa „przełącz”.

## 24-progi-i-naglowki — 2026-11-07 00:40
Status: GOTOWE, lokalnie, bez pushowania.
Zmienione pliki: `src/lib/media.ts`, 109 zapytań w `src`, `zalozyciele.css`, `zalozyciele-strony.css`, `zal-dzialy.css`, `zal-podstrona.css`, `zal-menu.css`, `zal-niski.css`, `zal-telefon.css`, `global.css`, `NaglowekZ.astro`, `Seminarium.astro`, `ListaAktualnosci.astro`, `Aktualnosc.astro`, `RAPORT-ZLECENIE-24.md`, `raport-zrzuty/z24-*`. Commity: `1e0a2c99`, `021e2254`, `d1b6a725`, `f9e4206e`, `dba7d890`, `ab33c482`, `303a7dba`, `acaac3bc`.
Kryteria odbioru: nagłówki od 1368 px 260 z 260 identyczne; pula ciekawostek 4155 prób, 0 błędów; długa ciekawostka 28 prób na 7 stronach, 0 błędów; telefon w widoku 600–980 px 860 prób, 0 błędów; 390 px opis schowany; telefon 390 i 412 px: 122 ze 130 identyczne, reszta to szum ±1 i ikona na 2 stronach. Macierz: 109 komórek z problemem przed, 10 po, wszystkie w treści (zlecenie 25). `astro check` 6 błędów jak przed zmianą.
Odstępstwa: margines też na `.z-pasek`; `.z-haslo` także na podstronach; od 1368 px rząd liczb liczony starą metodą, bo punkt 2 i punkt 3 sobie przeczą (na 12 stronach wracały liczby); długa ciekawostka po poprawce sprawdzona na 7 stronach, nie na wszystkich.
Pytania: w raporcie (kolejne liczby od 1368 px, `/studia/isim/` bez opisu przy 1024–1280 px).

## 25-tresc-gdy-brakuje-miejsca — 2026-11-07 02:30
Status: GOTOWE, lokalnie, bez pushowania.
Zmienione pliki: `src/plugins/postcss-tresc-telefon.mjs`, `src/plugins/rehype-limity.mjs`, `src/lib/limity.mjs`, `astro.config.mjs`, `src/components/zal/Podstrona.astro`, `SpisStrony.astro`, `TrescDzialu.astro`, `OsobaZ.astro`, `WladzeZ.astro`, `dzial/Kontakt.astro`, `TabelaPracownikow.tsx`, widoki `Kierunek`, `Publikacje`, `Seminarium`, `Specjalnosc`, `Zaklad`, `RokAkademicki`, `PlanZajec`, `ListaKonferencji`, `Aktualnosc`, `ListaAktualnosci`, style `zal-podstrona.css`, `zal-tresc.css`, `zal-dzialy.css`, `zal-granty-plan.css`, `zalozyciele-strony.css`, `global.css`, `RAPORT-ZLECENIE-25.md`, `raport-zrzuty/z25-*`.
Kryteria odbioru: Plan zajęć w obu semestrach PL i EN w 8 oknach, 0 przekroczeń; pole zwinięte do 1280 px; strony z samym tekstem mają pole przy każdym oknie; długie nazwisko w danych (osobny katalog, bez commita) daje widok telefonu treści przy nagłówku komputerowym; bez JS pole zwinięte do 1299 px; macierz 1 pozycja na 715 pomiarów (przewijany spis, punkt 2.15); telefon 130 zrzutów: wysokości bez zmian, różnice poniżej piksela przy „@”; nagłówki od 1368 px 259 z 260 identyczne, 1 tylko odcień; `astro check` 6 błędów, bez nowych.
Odstępstwa: limit komórki tylko do 30 znaków; nazwisko na Władzach limit 3 (z tytułami); kolumna nazw w Planie 232 px (Plan wyższy o 93 px); `auto-fill` z `max(…, %)`, żeby od 1368 px nie zmieniła się liczba kolumn; listy linków bez kontenera; telefon zachowuje interlinię 1,6 w nagłówku sekcji działu.
Pytania: w raporcie (spis na telefonie wobec decyzji ze zlecenia 18, Plan wyższy o 93 px).

Zlecenia 26 i 27 nierozpoczęte (7.11): właściciel polecił zatrzymać się po zleceniu 25. Plik zlecenia 26 tylko przeczytany, żadnych zmian w kodzie. Gałąź lokalnie na `c8815a68` i commicie raportu po nim, bez pushowania.

Uwaga dla zlecenia 28 (7.11, na prośbę właściciela; decyzja o osobnej wtyczce: „Nie teraz”): lista „Jak zacząć” na „Dla uczniów” (`Web-Popularyzacja`, `src/content/strony/popularyzacja/uczniowie.md`, treść PL i `tresc_en`) ma tytuł i opis kroku w osobnych akapitach. Pages CMS zapisuje opis z 2 spacjami zamiast 3, lista rozpada się na trzy, etykiety „Krok N” znikają. Propozycja bez osobnej wtyczki: po przebudowie `rehype-bloki.mjs` przepisać tę listę na nowy zapis osi (tytuł i opis w jednym punkcie), PL i EN, i sprawdzić ją symulacją zapisu z etapu 6a, bo ten etap obejmuje tylko kierunki. Zlecenie 30 przenosi Treść EN do edytora, więc bez tej zmiany ten sam błąd dotknie też „Step N”. Niesprawdzone: czy nowy zapis przetrwa zapis w edytorze na tej stronie.

## 26-strona-glowna-skala — 2026-11-07 10:52
Status: GOTOWE (punkty 1–4), lokalnie, bez pushowania. Punkt 5 pominięty: brak katalogu `.przekazanie\zdjecia\`.
Zmienione pliki: `src/components/zal/Okladka.astro`, `src/components/zal/DrugiEkran.astro`, `src/scripts/zal/drugi-ekran.ts`, `src/styles/zalozyciele.css`, `src/styles/zalozyciele-strony.css`, `RAPORT-ZLECENIE-26.md`, `raport-zrzuty/z26-*`. Commity: `c56b2861`, `3b8efbcd`, `fb27c52a`, `facb8bf3`, `6bf6ac39` (raport).
Kryteria odbioru: łuk 25% ± 2 od 1536×730 do 3840×2000 (3440×1300: 19,2%, okno ograniczone wysokością), 1024×700: 34%; 1920×950 i 1920×1080 okładka i drugi ekran identyczne z wersją przed; Szybki dostęp przy 2560×1300 i 3840×2000 w skali okładki, bez poziomego przewijania; animacje (przejazd, FLIP, ciągnięcie) zgodne przy zoom 1, 1,333 i 2; Ctrl + 200% przy 3840×2000 w Chrome, Edge i Firefoksie: tekst 40,8 px zamiast 29 px; drabinka: 1440×780 i 1536×730 krok 2, siatka w ekranie, 1280×600 przewija się bez pozycji uciętej w pół, 1707×830 i 1920×950 bez zmian, N zgodne w 60 porównaniach; telefon 390 i 412 px PL i EN, EN, ciemny motyw, bez JS identyczne; narzędzie ze zlecenia 24: 0 problemów przed i po; `astro check` 6 błędów jak przed; build 747 stron.
Odstępstwa: przy Ctrl + skala nie wyłącza się, tylko mnoży przez powiększenie z limitem 1366 px szerokości projektu (plateau 150–250%); w Firefoksie powiększenie z `devicePixelRatio` i wpisu `im-dpr-100` w `localStorage`; krok 4 zostawia układ kroku 3; dodatkowo krok 0 i wyrównanie nagłówków skryptem; U+2060 zamiast U+2011 w „e-maile”; `auto-fit` zamiast `auto-fill` i próg Studiów 1452 px zamiast 1366 px; 1366×620 nie mieści się na styk (brakuje 73 px); `.z-okl-liczby a` zostaje 12,5 px; Safari niesprawdzone; Ctrl + nie wciskany fizycznie, tylko przez API przeglądarek.
Pytania: w raporcie (wariant Ctrl +, polityka prywatności a `im-dpr-100`, Safari na Macu, panel menu przy 4K, 1366×620, próg 1452 px, plik zdjęcia do punktu 5).

Decyzja do zlecenia 26 (7.11, 10:52): Ctrl + przy 4K „Zostaje jak jest”, czyli wariant (a): skala mnożona przez powiększenie z limitem 1366 px szerokości projektu, bez zmian w kodzie. Pozostałe pytania z raportu (2–7) otwarte.

## 27-listy-jak-aktualnosci-i-drobne — 2026-11-07 12:23
Status: GOTOWE (punkty 1–7). Commity: `b73b943b`, `4eb3aa25`, `0e812dff`, `74c92909`, `9ed260c8`, `08fe2676`, `272b693b`, raport `62b40a19`. Na polecenie właściciela („commit i push, żeby się zaktualizował podgląd”) push gałęzi `wyglad/zlecenie-16` w Web-Core: najpierw `b4f99c25..08fe2676` (46 commitów: koniec zlecenia 22 oraz zlecenia 24–27), potem punkt 7 i raport. Ręcznie uruchomiony przebieg Web-Podglad 42367814871. Repozytoria treści bez zmian.
Zmienione pliki: `src/components/zal/ListaPokaz.astro` (nowy), `src/scripts/zal/panel-pokaz.ts` (nowy), `ListaAktualnosci.astro`, `listaAktualnosci.ts`, `Kalendarz.astro`, `kalendarz.ts`, `WierszWydarzenia.astro`, `ListaObron.astro`, `listaObron.ts`, `ListaWartoWiedziec.astro`, `listaWartoWiedziec.ts`, `WartoWiedziec.astro`, `src/lib/patroni.ts`, `NaglowekStrony.astro`, `NaglowekZ.astro`, `zalozyciele.css`, `zal-menu.css`, `zal-telefon.css`, `StopkaZ.astro`, `Szukaj.astro`, `404.astro`, `src/views/Aktualnosc.astro`, `src/pages/instytut/zaklady/index.astro`, `src/pages/en/instytut/zaklady/index.astro`, `skrypty/szerokosci/` (nowy: `pomiar.cjs`, `podsumuj.py`, `wzorzec.json`), `.github/workflows/qa.yml`, `RAPORT-ZLECENIE-27.md`, `raport-zrzuty/z27-*`.
Kryteria odbioru: każdy filtr, rok, dział i szukanie w Kalendarzu, Obronach i „Warto wiedzieć” na komputerze i telefonie, PL i EN, z klawiatury; Aktualności piksel w piksel jak przed (64 z 64); narzędzie ze zlecenia 24 na całej liście (715 renderów) macierze przed i po identyczne; kadr: ręce 12–25 px pod paskiem od 1024 do 2560 px (przed do −47 px); krzyżyk 24/24 px od rogu panelu, pole szukania 566 px przy 1920; Szukaj i 404 w linii tytułu nagłówka we wszystkich oknach; przekierowanie PL i EN z kotwicą; pierwszy przebieg pomiaru szerokości: 1308 renderów, 16 368 ciekawostek, 0 K, jedno fałszywe X (render bez CSS) i jedno fałszywe O (`.sr-only`) poprawione w narzędziu, wzorzec pusty; `astro check` 6 błędów jak przed; build 749 stron.
Odstępstwa: Popularyzacja nie dopisana do pola `dzial` „Warto wiedzieć”; Obrony w grupach nadchodzące/odbyte; Kalendarz, Obrony i „Warto wiedzieć” w jednej kolumnie przy szerokich oknach; daty w Archiwum w kolorze działu; zdjęcie banera najwyżej 980 px; obrys fokusu w stopce 2 px bez odstępu; ciekawostki w pomiarze podmianą w nagłówku; pełny przebieg pomiaru po poprawkach narzędzia przerwany na prośbę właściciela (poprawki sprawdzone na 28 renderach); pomiar w GitHub Actions jeszcze nie uruchomiony, harmonogram ruszy po scaleniu z `main`.
Pytania: w raporcie (1–6: dwie kolumny list, kolor dat w Archiwum, Popularyzacja w CMS, szerokość zdjęcia przy szerokich oknach, tekst wprowadzający Obron, ręczny przebieg pomiaru w Actions).

## 28-cms-kierunki-markdown — 2026-11-07 13:40
Status: GOTOWE lokalnie (etapy 0–6a), bez pushu; czeka na „push” (etap 7) i test w prawdziwym CMS (etap 8). Commity Web-Core: `a07f05ed`, `f3fa449a`, `dc14a7ce`, `eca4cafd`, `7f0fbff5`, `60193f77`, `a53a92a6`, raport `05886991`; Web-Studia: `320cefb`, `63ad234`, `98af815`; Web-Ustawienia: `24dbf2d`, `09431de`. Wszystko na `wyglad/zlecenie-16`.
Zmienione pliki: `src/plugins/rehype-bloki.mjs` i `.test.mjs`, `src/plugins/remark-wzory-edytora.mjs` (nowy), `src/lib/markdown.ts`, `src/lib/kierunki.ts`, `src/lib/tresci.ts`, `src/lib/widoki/kierunek.ts`, `src/views/Kierunek.astro`, `src/content.config.ts`, `.gitignore`, `skrypty/migracja/kierunki.py` (nowy), `skrypty/sprawdz_tresci.py`, `skrypty/test-edytora/` (nowy), `dok/sciagawka-edytora.md` (nowy), `RAPORT-ZLECENIE-28.md`, `raport-zrzuty/z28-*`; w klonach: `src/content/kierunki/*.md`, `src/content/kierunki-baner/*.json`, `src/data/przypomnienia.json`, `src/data/ustawienia.json`, `.pages.yml` (Web-Studia, Web-Ustawienia); `.przekazanie/pola-do-cms.md`.
Kryteria odbioru: migracja 1023 wartości przeniesionych, 110 pominiętych z powodem; porównanie przed/po (859 plików) tylko z dozwolonymi różnicami (lista roku, akapity „Szczegóły…”/„Wszystkie formularze…”, zdanie w pytaniu) i szumem (`DTSTAMP`, kolejność mapy strony); menu, kafelki, kalendarium i UID bez zmian; pomiar szerokości 96 renderów, układ jak przed; próbny kierunek bez banera i spoza listy w menu, kafelkach i mapie strony (usunięty); testy wtyczki 19/19; `sprawdz_pola_cms.py` 0 problemów (580 plików); `sprawdz_tresci.py` OK; `astro check` 6 błędów jak przed; zapis w symulowanym TipTap nie zmienia stron.
Odstępstwa: `pobierz_tresci.py --lokalnie` w głównym drzewie bez wcześniejszego sprawdzenia nakładki (14 identycznych plików spoza manifestu usuniętych); regresja kafelka „Dla nauczycieli” z etapu 1 poprawiona w etapie 6; pole `podpis` przypomnień spoza zlecenia; wzory: TipTap gubi `\{ \}`, `\|` i może zamienić dwa `_` w kursywę (poprawka wtyczką tylko na ukośniki dopisane przy zapisie); „Jak zacząć” na „Dla uczniów” nieruszone.
Pytania: w raporcie (1–5: wtyczka wzorów dla wszystkich pól, styl akapitów „Szczegóły…”, pole `podpis`, miejsce nowego kierunku, „Jak zacząć” w formacie osi).

## 29-cms-specjalnosci-i-popularyzacja — 2026-11-07 14:35
Status: GOTOWE lokalnie (etapy 1–4), bez pushu; czeka na „push” (etap 5) i test w prawdziwym CMS. Commity Web-Core: `0715563b`, `5d4f3c32`, `db36b984`, raport `ec2bc857`; Web-Spec-Analiza-Danych `a249995`, `e10514d`; Web-Spec-Aktuarialno-Finansowa `9ce52b7`, `72bc53e`; Web-Spec-Nauczycielska `e3a3ea7`, `ddc9f4b`; Web-Spec-Stosowana `5021e9d`, `4806331`; Web-Spec-Teoretyczna `22c7dc7`, `4f89fa8`; Web-Studia `9e28ae7`, `55e1a55`; Web-Popularyzacja `6608b03`, `a4f50c8`. Wszystko na `wyglad/zlecenie-16`.
Zmienione pliki: `src/plugins/kotwice.mjs`, `src/plugins/rehype-bloki.mjs` i `.test.mjs`, `src/lib/markdown.ts`, `src/lib/specjalnosci.ts` (nowy), `src/lib/widoki/specjalnosc.ts`, `src/lib/widoki/popularyzacja.ts`, `src/lib/widoki/kierunek.ts`, `src/lib/widoki/dzialStudia.ts`, `src/lib/sciezki.ts`, `src/pages/sitemap.xml.ts`, `src/content.config.ts`, `src/views/Specjalnosc.astro`, `src/views/Popularyzacja.astro`, `src/components/zal/TrescDzialu.astro`, `src/components/zal/Okladka.astro`, `.gitignore`, `skrypty/migracja/specjalnosci.py`, `popularyzacja.py`, `specjalnosc.pages.yml`, `formularze_specjalnosci.py` (nowe), `skrypty/sprawdz_tresci.py`, `dok/sciagawka-edytora.md`, `RAPORT-ZLECENIE-29.md`, `raport-zrzuty/z29-*`; w klonach: `src/content/specjalnosci/*.md`, `src/content/specjalnosci-baner/*.json`, `src/data/popularyzacja.md` (zamiast `.json`), `.pages.yml` (5 × Web-Spec-*, Web-Studia, Web-Popularyzacja); `.przekazanie/pola-do-cms.md`.
Kryteria odbioru: formularze „Treść” i „Baner i kafelek” we wszystkich 6 specjalnościach, „Strona działu Popularyzacja” z Treścią na górze; migracja 1981 + 42 wartości przeniesione, 36 pominiętych z powodem (ikony kafelków, `opublikowany`), skrypty powtarzalne i odmawiające drugiego uruchomienia; porównanie przed/po (749 stron) — różnice tylko na 10 stronach specjalności i niewidoczne (style globalne, `id` przy `###`, apostrofy EN; style i położenie elementów identyczne w przeglądarce, zrzuty identyczne co do piksela), kafelki specjalności, `/popularyzacja` i karty „Dla kogo” identyczne; testy wtyczki 23/23; `sprawdz_pola_cms.py` 0 problemów (586 plików); `sprawdz_tresci.py` OK; `astro check` 6 błędów jak przed; symulowany zapis w TipTap bez zmian poza 4 akapitami EN „No. …”.
Odstępstwa: `pobierz_tresci.py --help` w głównym drzewie nałożył treści z `main` (skrypt nie zna `--help`) — po minucie przywrócone `--lokalnie`, serwery dev nie działały; TipTap 3 zamienia akapit zaczynający się od „Xy. ” (No., Np., Dr.) na listę „1.” — ostrzeżenie w ściągawce i opisach pól, treść nie zmieniona; 2 linijki w opisach grupy „Kierunki” (Web-Studia) spoza zlecenia; po zmianie wtyczki serwer dev wymaga restartu z `--force`.
Pytania: w raporcie (1: pogrubić „No.” w 4 odpowiedziach EN) — decyzja właściciela „Tak, pogrub”: `eb14354` (Web-Spec-Analiza-Danych), `891742b` (Web-Spec-Nauczycielska), symulowany zapis bez zmian, strona różni się tylko pogrubieniem; raport `2dbe75ba`.
Push (słowo właściciela „push po zakończeniu”, 7.11 ok. 14:37): `wyglad/zlecenie-16` w 9 repozytoriach (Web-Core z commitami 28 i 29, Web-Studia, Web-Ustawienia, Web-Popularyzacja, 5 × Web-Spec-*), `main` nietknięty. `test-cms` od `wyglad/zlecenie-16` w Web-Studia, Web-Ustawienia, Web-Popularyzacja (stare z testu 22 zachowane jako `kopia/test-cms-zlecenie-22`) i Web-Spec-Stosowana — czeka na test właściciela (28 etap 8, 29 etap 5). Przebieg Web-Podglad uruchomiony ręcznie: run 42377831722 — sukces (Web-Core `2dbe75ba`, 1210 plików treści); strony specjalności i `/popularyzacja` na podglądzie równe lokalnemu buildowi poza hashami obrazów. Raport po pushu `900b0342` (wypchnięty); RAPORT-ZLECENIE-28 z dopiskiem o etapie 7.

## 30-cms-teksty-dzialow-i-formularze — 2026-11-07 15:51
Status: GOTOWE (etapy 1–5 bez testu w CMS); wypchnięte 7.11 o 15:53 po słowie właściciela „Po zakończeniu push”; czeka na test właściciela w CMS na `test-cms` (28, 29, 30 razem). Commity Web-Core: `8cdeba19`, `f9d6699a`, `2a491085`, `158128c0`, raport `01bb0437` i uzupełnienie po pushu; Web-Ustawienia `f1509cd`, `217a9bf`; Web-Instytut `f886ffb`, `a71e260`; Web-Nauka `dad4a5d`, `5de4170`; Web-Studia `ef51fa8`, `0200b1a`; Web-Aktualnosci `1a2a832`, `6319d7c`, `2fdd547`; Web-Pracownicy `43c9cd5`, `c4aa5f1`; Web-Popularyzacja `9ad0954`. Wszystko na `wyglad/zlecenie-16`.
Zmienione pliki: `src/lib/tekstyStron.ts` (nowy), `src/plugins/kotwice.mjs`, `src/plugins/rehype-bloki.mjs` i `.test.mjs`, `src/plugins/remark-wzory-edytora.mjs`, `astro.config.mjs`, `src/lib/markdown.ts`, `src/lib/tresci.ts`, `src/lib/sciezki.ts`, `src/lib/widoki/*` (strony działów, 11 list, obrona, publikacje, rok akademicki), `src/views/*` (te same strony), `src/components/zal/ListaPokaz.astro`, `Okladka.astro`, `dzial/Sekcja.astro`, `src/components/StronaGlowna.astro`, `src/styles/zalozyciele.css`, `zal-telefon.css`, `src/pages/sitemap.xml.ts`, `src/content.config.ts`, `.gitignore`, `skrypty/migracja/dzialy.py`, `wpisy.py`, `formularze.py` (nowe), `skrypty/sprawdz_tresci.py`, `skrypty/test-edytora/symulacja.mjs`, `dok/sciagawka-edytora.md`, `RAPORT-ZLECENIE-30.md`, `raport-zrzuty/z30-*`; w klonach: `src/data/{instytut,nauka,studia}.md` (nowe), `src/content/strony/*` (11 wpisów), `src/data/dzialy/*.json` (usunięte), `src/data/publikacje.json`, zakłady i „Warto wiedzieć” (grupa `karta`), 1 aktualność (bez `wyroznij_do`), `.pages.yml` (7 repozytoriów); `.przekazanie/pola-do-cms.md`, `.przekazanie/zlecenia/zasady.md` (sekcja „Teksty stron”).
Kryteria odbioru: migracja 108 wartości do 14 plików bez pominięć, karty 12 plików, `wyroznij_do` 1 plik; porównanie przed/po (5450 plików) — tekst 0 różnic, HTML 17 stron z różnicami niewidocznymi (atrybut `data-astro-cid`, apostrofy EN, klasa `lp-wstep`, skrypt okładki), pomiar w przeglądarce i zrzuty identyczne; strona bez wpisu (próba: Konferencje) działa z tytułem, opisem i hasłem z kodu; symulacja zapisu w TipTap 227 plików (w tym Pierwszy rok) — po dwóch poprawkach tekst stron bez zmian; `sprawdz_pola_cms.py` 0 (597 plików), `sprawdz_tresci.py` OK, `astro check` 6 błędów jak przed, testy wtyczki 24/24.
Odstępstwa: wtyczka wzorów we wszystkich Markdownach (pytanie 1 z raportu 28 rozstrzygnięte na „tak”) i tolerancja ostatniego kroku osi zapisanego przez edytor — obie z symulacji, bez zmian na dzisiejszych treściach; ścieżka „Stron” w Web-Instytut i Web-Nauka `src/content/strony`; nieużywane importy usunięte; pomiar w Edge.
Pytania: w raporcie (1: stała kotwica `#konsultacje` dla nagłówka „Office hours” zamiast HTML w Treści EN strony Zajęcia).
Push (słowo właściciela „Po zakończeniu push”, 7.11 15:53): `git pull --rebase` w 12 klonach i Web-Core bez zmian i konfliktów; `wyglad/zlecenie-16` w 8 repozytoriach (Web-Core `01bb0437`, Web-Ustawienia, Web-Instytut, Web-Nauka, Web-Studia, Web-Aktualnosci, Web-Pracownicy, Web-Popularyzacja), bez wymuszania, `main` nietknięty. Web-Podglad run 42383706719 — sukces (Web-Core `01bb0437`, 1221 plików treści); 26 stron na podglądzie z tym samym tekstem co lokalny build (różnice: nazwy obrazów, nazwa CSS, adres w „zgłoś błąd”). `test-cms` na nowym `wyglad/zlecenie-16` w Web-Studia, Web-Ustawienia, Web-Popularyzacja (przesunięte), Web-Spec-Stosowana (bez zmian), Web-Aktualnosci (nowe), Web-Nauka (stare z zapisem właściciela z 6.11 zachowane jako `kopia/test-cms-zlecenie-22`) — czeka na test właściciela (28 etap 8, 29 etap 5, 30 etap 5).
Pytanie 1 — decyzja właściciela „Tak, dodaj kotwicę” (7.11): stała kotwica `#konsultacje` dla nagłówka „Konsultacje” / „Office hours” na zwykłych stronach (kotwice typu `naglowek` w `src/plugins/kotwice.mjs`, wtyczka bloków, test 25/25, ściągawka) — Web-Core `84f3499f`; z Treści EN strony Zajęcia usunięty `<a id="konsultacje">`, link w Pierwszym roku EN `#office-hours` → `#konsultacje` — Web-Studia `8c7e561`. Build: zmienione tylko `/en/studia/zajecia` i `/en/studia/pierwszy-rok` (plus nieustalona kolejność dwóch wpisów na Pracownikach); symulowany zapis zostawia nagłówek i link. Wypchnięte; `test-cms` w Web-Studia przesunięte na `8c7e561`; do testu właściciela dopisany zapis bez zmian strony Zajęcia. Uwaga: obecna stopka nie pokazuje kolumn z `stopka.json`, więc z kotwicy korzystają dziś linki z Pierwszego roku (PL, EN), a nie stopka — poprawione w raporcie, `kotwice.mjs` i ściągawce.

## cms-listy-zwiniete — 2026-11-07 17:30
Status: GOTOWE i wypchnięte na `main` w 21 repozytoriach treści (jeden commit „CMS: listy domyślnie zwinięte, nagłówki pozycji”, tylko `.pages.yml`; inne gałęzie nietknięte). Wszystkie 50 list obiektów (`list: true`) → `list.collapsible` z `collapsed: true` i `summary`; listy tekstów bez zmian. Kontrola: YAML się wczytuje, każdy wzór używa pól swojej listy, `sprawdz_pola_cms.py` 0 problemów (597 plików). Strona się nie zmienia; wygląd w CMS niesprawdzony. Wzór `skrypty/migracja/specjalnosc.pages.yml` w Web-Core nieruszony.

| Repozytorium | Pole | Wzór nagłówka |
|---|---|---|
| Web-Aktualnosci | `aktualnosci/galeria` | `{index}. {podpis}` |
| Web-Aktualnosci | `aktualnosci/zalaczniki` | `{nazwa}` |
| Web-Aktualnosci | `obrony/recenzje` | `{recenzent}` |
| Web-Aktualnosci, Web-Instytut, Web-Nauka, Web-Pracownicy, Web-Studia | `strony/liczby` | `{n} {etykieta}` |
| Web-Instytut | `strona-dzialu/o_instytucie_fakty` | `{wartosc} {opis}` |
| Web-Instytut | `wladze/osoby`, `wladze/wydzial/osoby` | `{imie_nazwisko}` |
| Web-Instytut | `wladze/linki` | `{etykieta}` |
| Web-Nauka | `strona-dzialu/badania_fakty` | `{wartosc} {opis}` |
| Web-Nauka | `publikacje/lata` | `{rok}` |
| Web-Nauka | `publikacje/czasopisma` | `{nazwa}` |
| Web-Nauka | `publikacje-wykazy/grupy` | `{index}. {naglowek}` (nagłówek pusty w 21 z 35 grup) |
| Web-Nauka | `publikacje-wykazy/grupy/prace` | `{autorzy}: {tytul}{opis}` (praca ma albo `tytul`, albo `opis`) |
| Web-Popularyzacja | `popularyzacja/o_popularyzacji_fakty` | `{wartosc} {opis}` |
| Web-Popularyzacja | `popularyzacja/tradycja` | `{rok} {nazwa}` |
| Web-Popularyzacja | `popularyzacja/linki` | `{nazwa}` |
| Web-Sem-* (9) | `referaty/pliki` | `{nazwa}` |
| Web-Spec-* (5) | `specjalnosc-baner/opiekunowie` | `{imie_nazwisko}` |
| Web-Studia | `spec-matematyka-w-ekonomii-baner/opiekunowie` | `{imie_nazwisko}` |
| Web-Studia | `strona-dzialu/o_studiach_fakty` | `{wartosc} {opis}` |
| Web-Studia | `kierunki-baner/liczby` | `{wartosc} {etykieta}` |
| Web-Studia | `przypomnienia/przypomnienia` | `{data} {sprawa}` |
| Web-Studia | `kolory-dni/semestry` | `{nazwa}` |
| Web-Studia | `semestry/terminy/przerwy` | `{od} – {do}` |
| Web-Studia | `semestry/wolne` | `{od} {opis}` |
| Web-Studia | `semestry/zamiany` | `{data} {jak_dzien}` |
| Web-Studia | `semestry/wyjatki` | `{data} {kolor}` |
| Web-Ustawienia | `ustawienia/przyciski` | `{etykieta}` |
| Web-Ustawienia | `ustawienia/studia/kierunki` | `{nazwa}` |
| Web-Ustawienia | `ustawienia/partnerzy` | `{nazwa}` |
| Web-Ustawienia | `skroty/kafelki` | `{etykieta}` |
| Web-Ustawienia | `nawigacja/menu`, `menu/grupy/linki` | `{etykieta}` |
| Web-Ustawienia | `menu/grupy` | `{nazwa}` |

## 38-porzadki-web-core-i-galezie (etap 1) — 2026-11-18 00:31
Status: wstrzymane — STOP etapu 1, czeka na „push” (na GitHubie nic nie zmienione)
Zmienione pliki (worktree Web-Core-B, lokalna gałąź praca/38-porzadki, 2 commity): skrypty/porzadki/galezie.py (nowy); usunięte .github/workflows/sprawdz-galaz.yml, qa.yml, proza-domyslna-test.yml; dok/archiwum-silnika-banerow.md, dok/en/POSTEP.md, skrypty/pobierz_tresci.py (odwołania do gałęzi → znaczniki)
Kryteria odbioru: plan gałęzi gotowy — 92 gałęzie w 18 repozytoriach, 44 z commitami spoza main, 91 znaczników do utworzenia, 0 kolizji nazw; reszta kryteriów po „push” i w etapie 2
Odstępstwa od zlecenia i powody: brak; dodatkowo przegląd starych folderów (source, _stare, IM-Website-test) na prośbę właściciela
Pytania do użytkownika: w RAPORT-ZLECENIE-38.md (markdown-jawne-test.yml, .github/qa, krok wariantów w deploy.yml, materiały z IM-Website-test)

## 38-porzadki-web-core-i-galezie (etap 1 wykonany) — 2026-11-18 00:48
Status: etap 1 zrobiony po „push”; etap 2 w toku (lokalnie)
Zmienione na GitHubie: 92 gałęzie w 18 repozytoriach → znaczniki archiwum/<nazwa> (91 nowych, 1 istniał), gałęzie usunięte; archiwum/2026-11-09-silnik-banerow jest znacznikiem; main Web-Core 24c708e..222d5e4 (bez force)
Kryteria odbioru: „tylko main (+ zbudowana w Web-Podglad), każda usunięta gałąź ma znacznik” — spełnione, sprawdzone git ls-remote we wszystkich 23 repozytoriach; „usunięte workflowy gałęzi roboczych, deploy/przekaźnik/plan zostają” — spełnione (ls-tree origin/main); bez force-push — spełnione
Odstępstwa od zlecenia i powody: brak
Pytania do użytkownika: bez zmian (RAPORT-ZLECENIE-38.md)

## 31-cms-galeria-daty-nazwy — 2026-11-18 00:53
Status: wstrzymane — STOP etapu 4, czeka na akceptację trzech wpisów z 16.11 i „push” (na GitHubie nic nie zmienione)
Zmienione pliki: Web-Core, lokalna gałąź praca/31-galeria-daty-nazwy (na origin/main 222d5e47, 4 commity + raport): src/content.config.ts; skrypty/sprawdz_tresci.py, sprawdz_pola_cms.py; skrypty/migracja/formularze.py, formularze_31.py (nowy), termin.py (nowy), kontrola_redaktorow.py (nowy); skrypty/test-edytora/formularz.mjs (nowy); dok/sciagawka-edytora.md; RAPORT-ZLECENIE-31.md; raport-zrzuty/z31-* (16). Repozytoria treści: worktree GitHub/tresci-z31, lokalne gałęzie praca/31-galeria-daty-nazwy — .pages.yml w 16 repozytoriach (po 1 commicie), Web-Aktualnosci dodatkowo migracja 13 wpisów (osobny commit f5a8c36). Wspólne klony tresci i b7a307a nieruszone. .przekazanie/pola-do-cms.md: dopisana sekcja „Zlecenie 31”.
Kryteria odbioru: pusta pozycja galerii/załącznika — czerwony komunikat i blokada zapisu (symulacja), strona pomija z ostrzeżeniem (test budowy) — spełnione; termin na kliknięcie, max 1, pod „Rodzaj” — spełnione; CMS nie wpisuje dat wydarzenia (scenariusze 1 i 5) — spełnione; 13 wpisów przeniesionych, Kalendarz i .ics bez zmian poza trzema z 16.11 — lokalnie, czeka na akceptację; daty opcjonalne default "" (12 + 5 wymaganych w listach) — spełnione; nazwa pliku z tytułu — spełnione; ściągawka i lista PDF — spełnione (do poprawy Mapa-CMS-IM-UWr.pdf); kontrole: sprawdz_pola_cms 0, sprawdz_tresci OK (1 ostrzeżenie), astro check 0 błędów, zapis bez zmian 724 plików 0 różnic; kontrola redaktorów — skrypt i próba OK, właściwa w etapie 5
Odstępstwa od zlecenia i powody: 5 wymaganych dat w pozycjach list z default "" (nowa pozycja nie zapisze niezauważenie dzisiejszej daty); pozycja w 40 listach, 32 podpola wymagane — przegląd szerszy niż w zleceniu, decyzje w raporcie; Web-Spec-* pominięte (poza tresci.json)
Pytania do użytkownika: w RAPORT-ZLECENIE-31.md — akceptacja trzech wpisów z 16.11; rodzaj „Medali” (wydarzenie bez terminu); przemianowanie plików 2026-11-16-*.md; usunięcie field: create w konferencjach, grantach i referatach

## 31-cms-galeria-daty-nazwy (akceptacja) — 2026-11-18 00:52
Status: wstrzymane — czeka na „push”; właściciel zaakceptował zmiany w trzech wpisach z 16.11 („Akceptuję”)
Zmienione pliki: RAPORT-ZLECENIE-31.md (akceptacja odnotowana, commit lokalny)
Kryteria odbioru: „13 wpisów przeniesionych … zaakceptowanymi przez właściciela” — spełnione lokalnie, wypchnięcie w etapie 5
Odstępstwa od zlecenia i powody: brak nowych
Pytania do użytkownika: otwarte pytania 2–4 z raportu (rodzaj „Medali”, przemianowanie plików 2026-11-16-*.md, field: create w konferencjach, grantach i referatach)

## 31-cms-galeria-daty-nazwy (decyzja: Medale) — 2026-11-18 00:55
Status: wstrzymane — czeka na „push”; właściciel: „Medale Uniwersytetu…” (2026-11-16--2.md) jako „sukces”
Zmienione pliki: Web-Aktualnosci (worktree tresci-z31) b36d9af — rodzaj wydarzenie → sukces, osobny commit; Web-Core: skrypty/migracja/termin.py (DECYZJE, --decyzje), kontrola_redaktorow.py (decyzje przepuszczane tylko przy wartości sprzed decyzji), RAPORT-ZLECENIE-31.md
Kryteria odbioru: sprawdz_tresci OK bez ostrzeżeń; sprawdz_pola_cms 0; kontrola redaktorów przed/po OK (rodzaj 1 plik, decyzja właściciela)
Odstępstwa od zlecenia i powody: brak (zlecenie zakładało, że „Medale” są sukcesem)
Pytania do użytkownika: otwarte 3–4 z raportu (przemianowanie plików 2026-11-16-*.md, field: create w konferencjach, grantach i referatach)

## 38-porzadki-web-core-i-galezie (etap 2) — 2026-11-18 01:15
Status: wstrzymane — STOP etapu 2, czeka na „push” (lokalny commit 6bf211e na praca/38-porzadki; archiwum = 222d5e4)
Zmienione pliki: usunięte raport-zrzuty/ (613), RAPORT-*.md (21), PYTANIA.md, wyglad-podstron.json, skrypty/warianty.py, src/dev/panel-wariantow.ts, src/plugins/panel-wariantow.mjs, src/styles/test-warianty.css; zmienione astro.config.mjs, .github/workflows/deploy.yml (bez kroku wariantów), .gitignore, README.md (sekcja „Archiwa”), dok/start-strony.md; lokalnie .przekazanie/zlecenia/zasady.md (raporty tylko lokalnie)
Kryteria odbioru: identyczna budowa — spełnione (HTML 757/757, CSS 15/15, JS 33/33 bajt w bajt; .ics i powiadomienia.json różnią się tylko znacznikiem czasu budowy; sitemap i pagefind bez różnic); astro check 0 błędów przed i po; testy wtyczek 47/47; czas 30 s → 29 s; .gitignore pomija raporty — spełnione; archiwum pierwszej wersji — przygotowane lokalnie
Odstępstwa od zlecenia i powody: archiwum/pierwsza-wersja jako znacznik, nie gałąź (kryterium „tylko main”) — do potwierdzenia; .github/qa, skrypty/szerokosci, skrypty/migracja (31 niewypchnięte), src/assets/szkice (źródła szkice.json), dok/latki i dok/en zostają — opis w raporcie
Pytania do użytkownika: znacznik czy gałąź; .github/qa i szerokosci; dok/latki i dok/en; Podgląd nie buduje się od 17.11 22:12 przez pusty załącznik w Web-Aktualnosci/2026-11-16-.md

## 31-cms-galeria-daty-nazwy (przemianowanie) — 2026-11-18 01:03
Status: wstrzymane — czeka na „push”; właściciel: „Tak, przemianuj” (trzy pliki 2026-11-16-*.md)
Zmienione pliki: Web-Aktualnosci (worktree tresci-z31) d0e763f — 2026-11-16-.md → 2026-11-10-seminarium-wydzialowe-problem-milenijny.md, 2026-11-16--1.md → 2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza.md, 2026-11-16--2.md → 2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego.md (osobny commit, treść bez zmian); Web-Core: skrypty/migracja/termin.py (PRZEMIANOWANIA, --przemianuj), kontrola_redaktorow.py (zapis w starym pliku porównywany z nowym, przemianowanie liczone jako „(nazwa pliku)”), RAPORT-ZLECENIE-31.md
Kryteria odbioru: budowa 757 stron; porównanie z budową „po” — 16 plików, wszystkie zamierzone (nowe adresy i UID w .ics, „Medale” w Sukcesach i „Ostatnich sukcesach” Instytutu); sprawdz_tresci OK bez ostrzeżeń; sprawdz_pola_cms 0; kontrola redaktorów przed/po OK; skrypty powtórzone na gotowym stanie nic nie zmieniają
Odstępstwa od zlecenia i powody: brak (zlecenie zostawiało przemianowanie do decyzji właściciela). Stare adresy /aktualnosci/2026-11-16-…/ przestaną działać, seminarium dostaje w .ics nowy UID
Pytania do użytkownika: otwarte pytanie 4 z raportu (usunąć field: create w konferencjach, grantach i referatach)

## 38-porzadki-web-core-i-galezie (koniec) — 2026-11-18
Status: zrobione (etapy 1 i 2 wypchnięte po „push”)
Zmienione na GitHubie: znacznik archiwum/pierwsza-wersja → 222d5e4 (dawny main z raportami i zrzutami); main Web-Core 222d5e4..6bf211e (fast-forward, bez force): bez raport-zrzuty/, RAPORT-*.md, PYTANIA.md, panelu wariantów, wyglad-podstron.json, warianty.py i kroku wariantów w deploy.yml
Kryteria odbioru: wszystkie spełnione — tylko main (+ zbudowana) w 23 repozytoriach (ls-remote); archiwum pierwszej wersji jako znacznik; na main 0 raportów i zrzutów, .gitignore je pomija; budowa przed/po identyczna (HTML/CSS/JS bajt w bajt, w .ics i powiadomienia.json tylko czas budowy); workflowy gałęzi usunięte, deploy/przekaźnik/plan zostają; bez force-push
Odstępstwa od zlecenia i powody: archiwum/pierwsza-wersja to znacznik, nie gałąź (kryterium „tylko main”); skrypty/migracja zostaje do wypchnięcia 31
Pytania do użytkownika: markdown-jawne-test.yml; .github/qa i skrypty/szerokosci; dok/latki i dok/en; Podgląd nie buduje się od 17.11 22:12 (pusty załącznik w Web-Aktualnosci/2026-11-16-.md)

## 31-cms-galeria-daty-nazwy (field: create) — 2026-11-18 01:08
Status: wstrzymane — czeka na „push”; właściciel: „Tak, usuń” (pytanie 4). Pytań otwartych nie ma
Zmienione pliki: repozytoria treści (worktree tresci-z31, osobny commit w każdym) — .pages.yml bez filename.field: create w Web-Nauka (konferencje, granty) i 9 × Web-Sem-* (referaty); Web-Core: skrypty/migracja/formularze_31.py (operacja bez_field_create dla tych 11 kolekcji), skrypty/test-edytora/formularz.mjs (scenariusz 7), dok/sciagawka-edytora.md, RAPORT-ZLECENIE-31.md; .przekazanie/pola-do-cms.md (wiersz w sekcji „Zlecenie 31”)
Kryteria odbioru: nazwa pliku z tytułu przy zapisie — symulacja, scenariusz 7: OK w 11 kolekcjach (stara konfiguracja: 2026-.md, 2026-11-18-.md); formularze_31.py od zera na bazie 16 repozytoriów = .pages.yml z worktree; sprawdz_pola_cms 724 pliki, 0 problemów; zapis bez zmian 724 plików, 0 różnic; kontrola redaktorów przed pushem OK (0 nowych zapisów w 10 repozytoriach); istniejących plików nie trzeba przemianowywać
Odstępstwa od zlecenia i powody: brak
Pytania do użytkownika: brak; czeka na „push”

## 38 — naprawa Podglądu — 2026-11-18
Status: zrobione (za zgodą właściciela)
Zmienione: Web-Aktualnosci cc6a7b0 — usunięta pusta pozycja załącznika w src/content/aktualnosci/2026-11-16-.md
Kryteria odbioru: Podgląd zbudowany i opublikowany (run 44205492784: build i deploy success); strona wpisu odpowiada 200
Odstępstwa od zlecenia i powody: poza zleceniem 38, na prośbę właściciela
Pytania do użytkownika: brak

## 31-cms-galeria-daty-nazwy (push) — 2026-11-18 01:32
Status: zrobione — wypchnięte Web-Core i 16 repozytoriów treści; zostaje test w CMS (właściciel) i przegląd zapisów z 24 godzin
Zmienione pliki: Web-Core main 6bf211e6..e3625870 (7 commitów: content.config.ts, sprawdz_tresci.py, sprawdz_pola_cms.py, skrypty/migracja/{formularze.py, formularze_31.py, termin.py, kontrola_redaktorow.py}, skrypty/test-edytora/formularz.mjs, dok/sciagawka-edytora.md); raport i zrzuty tylko lokalnie (nowa reguła z zasady.md) — commity przeniesione na 6bf211e6 bez nich. Web-Aktualnosci cc6a7b0..7f0bd01 (4 commity: .pages.yml, migracja, decyzja „Medale”, przemianowanie); 15 repozytoriów po 1 commicie .pages.yml (Web-Nauka i Web-Sem-* razem z usunięciem field: create)
Kryteria odbioru: wszystkie spełnione poza testem w CMS (właściciel) i przeglądem z następnego dnia; astro check 0 błędów; budowa 757 stron, wynik jak przed rebase; Podgląd zielony po kodzie (e3625870, 13 ostrzeżeń „stary zapis terminu”) i po treściach (0 ostrzeżeń); kontrola redaktorów przed pushem 16 × OK (Web-Aktualnosci od bazy f8126af, z zapisem cc6a7b0 z 01:09), po pushu 16 × „tylko zmiany z migracji”; Kalendarz i strona główna na Podglądzie sprawdzone
Odstępstwa od zlecenia i powody: treści odtworzone od świeżego main po zapisie cc6a7b0 (migracja nie musiała już usuwać „- {}”), wynik identyczny ze starym; Podgląd po kodzie uruchomiony przez gh workflow run podglad.yml w Web-Podglad (zamiast przekaźnika z Web-Core; to samo działanie)
Pytania do użytkownika: brak; do zrobienia: test w CMS, przegląd zapisów do 19.11 ok. 01:25, porzucenie b7a307a we wspólnym klonie tresci/Web-Aktualnosci przed pull

## 41-podglad-szybciej-i-po-pushu-kodu — 2026-11-18 01:55
Status: zrobione i wypchnięte (tryb samodzielny; warunki pushu spełnione)
Zmienione pliki:
- Web-Podglad: `.github/workflows/podglad.yml`, `README.md`; usunięty `testy/telefon-TEST.patch` (`51c4b95`, `f11ae37`).
- Web-Core: `.github/workflows/podglad-przekaznik.yml` (`4511613b`).
- Web-Instytut: test serii zapisów, strona tymczasowa utworzona i usunięta, różnica netto zerowa (`0855f0d`..`311faae`).
Kryteria odbioru:
- Budowa krótsza — spełnione: zadanie `build`, mediana z 3, 323 → 61 s; start → publikacja 340 → 77 s. Optymalizacja zdjęć 156–249 s → 0,5 s.
- Pamięć npm i zdjęć działa — spełnione: trafienia w logu, 3066/3066 zdjęć z pamięci. Treści 15 → 2 s (`--depth=1`, 8 naraz).
- Seria zapisów — spełnione: 3 zapisy w 48 s → 2 przebiegi `cancelled` i 1 pełna budowa. „Zapis 3 z 3” widoczny 1:45 po ostatnim zapisie.
- Push kodu przebudowuje Podgląd — spełnione: przekaźnik po pushu `4511613b` → budowa 56 s.
- TEST telefonu usunięty — spełnione (wartość domyślna).
- Wynik identyczny — spełnione: `zbudowana` przed i po: 0 różnic w HTML, CSS, JS i obrazach. Różnią się tylko `DTSTAMP` w `.ics`, `wygenerowano` w `powiadomienia.json` i kolejność w `sitemap.xml` (zmieniała się też w starych budowach).
- Ochrona zmian redaktorów: w Web-Instytut każdy push obejmował tylko plik testowy; od bazy `3f9689a` nie przybył żaden zapis redaktora.
Odstępstwa od zlecenia i powody:
- Klucz pamięci zdjęć ma dodatkowo skrót listy plików w pamięci, żeby nowe rozmiary z kodu też trafiały do pamięci. Pamięć jest porządkowana po budowie.
- Seria zapisów: wybrałem przerywanie budowy w toku, nie wstrzymanie w przekaźniku, bo to dokładałoby 60 s do każdego zapisu.
- `actions/cache` v5 (Node 24).
Pytania do użytkownika:
- Drugi klucz sortowania, żeby kolejność konferencji z tą samą datą i `sitemap.xml` była stała.
- Podnieść `configure-pages`, `upload-pages-artifact` i `deploy-pages` (ostrzeżenia o Node 20)?
- (z 38) `skrypty/migracja/` zostaje, bo druga sesja używa kontroli redaktorów z 31. Usunąć po 40?
Dla zlecenia 33: `podglad.yml` ma `concurrency` tylko na poziomie zadań (`build`: `podglad-budowa`, `cancel-in-progress`; `deploy`: `pages`). Krok „Budowanie strony” używa `npm run build | tee`.

## 39-kierunki-bez-automatow-i-podyplomowe — 2026-11-18 02:05
Status: zrobione i wypchnięte (tryb samodzielny; warunki pushu spełnione)
Zmienione pliki:
- Web-Core (`0fa6731b`): `src/lib/kierunki.ts`, `src/lib/menu.ts`, `src/lib/widoki/dzialStudia.ts`, `src/components/zal/DrugiEkran.astro`, `dok/sciagawka-edytora.md`, `skrypty/migracja/kierunki_39.py` (nowy).
- Web-Ustawienia: `.pages.yml` i `src/data/ustawienia.json` (`5ecbef7`); `ustawienia.json` i `src/data/nawigacja.json` (`f145d85`).
- Web-Studia: `src/content/strony/studia/podyplomowe.md` → `src/content/kierunki/podyplomowe.md` (`b2a7c09`).
Kryteria odbioru:
- Tylko pozycje z listy — spełnione: menu, hamburger, `/studia` i kafelki z listy; test z kierunkiem spoza listy: ostrzeżenie w budowie, strona działa, brak w menu, kafelkach i liczbach.
- Bez wartości zastępczych, wygląd bez zmian — spełnione: lista ma wszystko jawnie; HTML 757 stron przed/po: 0 różnic poza `/studia/podyplomowe` (PL, EN). Stany pośrednie między pushami też bez różnic.
- Podyplomowe jako kierunek, jedna pozycja, menu jak dziś — spełnione (menu bajt w bajt; kafelek „Nauczanie matematyki” bez zmian). Strona ma szablon kierunku: drobne różnice wyglądu w raporcie ze zrzutami, bez poprawek.
- Formularz, ściągawka, PDF — spełnione; zdania do podmiany w PDF w raporcie (źródła PDF brak).
- Ochrona zmian redaktorów — przed pushem 0 zapisów od bazy w obu repozytoriach; po pushu tylko celowe pola (lista w raporcie). Przegląd następnego dnia: do 19.11, 02:00.
- Kontrole: `astro check` 0 błędów; `sprawdz_tresci.py` OK; `sprawdz_pola_cms.py` 0 problemów (724 pliki); symulacja formularza: zapis bez zmian 0 różnic. Podgląd zielony po każdym pushu.
Odstępstwa od zlecenia i powody:
- Kolejność pushy: lista (Web-Ustawienia `5ecbef7`) przed Web-Core, bo nowy kod bez wartości zastępczych pokazałby ze starą listą puste nazwy w menu; stary kod z nową listą sprawdzony: 0 różnic.
- Przyjąłem osobne pole „Nazwa w menu” (`nazwa_menu`, wymagane), bo zlecenie je przewiduje, a nazwa na kafelku zostaje bez zmian.
- Przyjąłem: liczby na `/studia` tylko z kierunków z listy; studia podyplomowe nie liczą się do kierunków ani stopni (inaczej 3 → 4).
Pytania do użytkownika:
- Skrót SIAD w menu to stała reguła wyświetlania (`skrotNazwy`), nie wartość zastępcza; wpisać „SIAD” wprost i usunąć regułę?
- Wygląd strony podyplomowych w szablonie kierunku (patron, styl liczb, kreska): zostawić czy przywrócić?
- PDF dla redaktorów: podmienić zdania z kroków 3–4 (w raporcie).

## 33-przelacznik-opublikowane-i-stan-budowy — 2026-11-18 02:08
Status: wstrzymane (polecenie właściciela „zatrzymaj się w bezpiecznym miejscu”); zrobione tylko rozpoznanie kodu, bez zmian, bez commitów i pushy
Zmienione pliki: brak (lokalna gałąź Web-Core `praca/33-opublikowane` = `origin/main`, bez zmian)
Kryteria odbioru: żadne jeszcze niespełnione; rozpoznanie (miejsca filtrów, formularze, dane, `podglad.yml`) i plan wznowienia w `RAPORT-ZLECENIE-33.md`
Odstępstwa od zlecenia i powody: brak
Pytania do użytkownika:
- Zakłady i „Warto wiedzieć” (pole `opublikowany` w schemacie): przełącznik w formularzu czy bez?
- Strona działu jako szkic przy fladze `TYLKO_OPUBLIKOWANE`: strona działu bez tekstu z pliku (nie może zniknąć, bo prowadzi do niej menu)?

## 32-menu-hamburger-pc-rozwijane (przerwane) — 2026-11-18 02:10
Status: przerwane na prośbę właściciela; kod gotowy, odbiór niezrobiony, nic nie wypchnięte. Lokalny commit `b2244d3e` na `praca/32-menu` (Web-Core-B), na `main` = `4511613b`; budowa przechodzi
Zmienione pliki: `src/styles/zal-menu.css`, `src/scripts/zal/menu.ts`, `src/styles/zalozyciele.css`, `src/components/zal/Okladka.astro`, `src/components/zal/PasekMenu.astro`, `src/components/Naglowek.astro`, `src/lib/i18n.ts` (`UWR_ADRES`)
Kryteria odbioru: stałe wielkości i adres UWr w jednym miejscu: tak; pozostałe niesprawdzone. Brakuje zrzutów „po”, porównania telefonu, `astro check` i konsoli. Plan wznowienia jest w `RAPORT-ZLECENIE-32.md`, zrzuty „przed” w `raport-zrzuty/z32-przed/`
Odstępstwa od zlecenia i powody: brak (Tab za ostatnią pozycją zamyka listę, wariant dopuszczony przez zlecenie)
Pytania do użytkownika:
- Krzyżyk w liście czy hamburger zmieniający się w ×? Na razie zostaje krzyżyk, propozycja ze zrzutem nieprzygotowana
- Podsumowanie nocy (okno Web-Core-B): `RAPORT-PODSUMOWANIE-18-11.md`

## 32-menu-hamburger-pc-rozwijane (push) — 2026-11-18 11:35
Status: zrobione, wypchnięte (tryb samodzielny). Web-Core `main` `0fa6731b..c2c193e0`; Podgląd 44285963010 zielony. Wznowione po przerwie z 02:06, rebase na zlecenie 39 bez konfliktów
Zmienione pliki: `src/styles/zal-menu.css`, `src/scripts/zal/menu.ts`, `src/styles/zalozyciele.css`, `src/components/zal/Okladka.astro`, `src/components/zal/PasekMenu.astro`, `src/components/Naglowek.astro`, `src/lib/i18n.ts` (`UWR_ADRES`)
Kryteria odbioru: wszystkie spełnione.
- Lista 8 px pod przyciskiem, prawa krawędź równo z nim, w 4 rozdzielczościach.
- Szerokość stała 560 px, linki działu w ≤ 2 wierszach, przewijanie w liście tylko przy 1280×720 z rozwiniętym działem.
- Klawiatura, Esc, klik obok i ponowny klik hamburgera działają.
- Punkt 8 (PL/EN): orzeł → uwr.edu.pl, położenie znaku identyczne co do 0,01 px.
- Telefon: 0 różnic poza szumem renderowania.
- `astro check` 0 błędów, testy 47/47, konsola czysta.
- Zrzuty: `raport-zrzuty/z32-przed2`, `z32-po`.
Odstępstwa od zlecenia i powody:
- Wielkości o stopień mniejsze (26 / 16 / 13,5 / 46 / 16 px), bo przy pełnej skali na 1536×864 rozwinięta lista sięgała 19 px nad dół okna. Zlecenie przewiduje ten krok.
- Tab za ostatnią pozycją zamyka listę (wariant dopuszczony).
Pytania do użytkownika:
- Krzyżyk w liście zostaje; × w miejscu hamburgera tylko na życzenie

## 32-menu-hamburger-pc-rozwijane (punkt 9, push) — 2026-11-18 12:05
Status: zrobione, wypchnięte osobnym commitem (tryb samodzielny). Web-Core `main` `c2c193e0..cbca5051`; Podgląd 44290545777 zielony (72 s)
Zmienione pliki: `src/styles/zal-menu.css` (zmienna `--menu-wiersz`, tylko blok komputera)
Kryteria odbioru: spełnione.
- Przy zwiniętych działach wszystkie 6 wierszy ma odstęp 68,19 px między separatorami (rozrzut 0,00 px). Dotyczy 1536×864, 1920×1080, 1280×720 i 1024×768, paska, okładki i jasnego paska.
- Przed zmianą „Aktualności” miały 46,69 px, „Rekrutacja ↗” 45,69 px.
- Cały wiersz jest linkiem, tekst wyśrodkowany w pionie, wcięcie i pismo bez zmian.
- Rozwinięty dział bez zmian (318,94 px).
- Telefon: 0 różnych pikseli.
- `astro check` 0 błędów, testy 47/47, konsola czysta.
- Zrzuty: `raport-zrzuty/z32p9-przed`, `z32p9-po`.
Odstępstwa od zlecenia i powody:
- Na `/aktualnosci/` wyśrodkowany jest tekst razem z kreską bieżącej strony, jak przy nazwach działów. Wysokość wiersza bez zmian.
- Przy 1024×768 z rozwiniętym działem lista jest teraz przewijana wewnątrz (o 41 px). Zlecenie przewiduje ten przypadek.
Pytania do użytkownika: brak


## 34-tryb-ciemny — 2026-11-18 12:22
Status: zrobione, wypchnięte (tryb samodzielny). Web-Core `main` `cbca5051..b7192769`; Podgląd 44293228901 zielony (81 s)
Zmienione pliki: `src/styles/zalozyciele.css`, `src/styles/global.css`, `src/styles/telefon.css`, `src/styles/tlo.css`, `src/styles/zal-dzialy.css`, `src/styles/zalozyciele-strony.css`, `src/styles/zal-telefon.css`, `src/styles/zal-granty-plan.css`, `src/components/zal/ListaPokaz.astro`
Kryteria odbioru: wszystkie spełnione.
- Tryb jasny: 40/40 zrzutów identycznych co do piksela.
- Wartości: tło #172032. Nauka `--d-a` #82d3aa, `--d-kafel` #293e49; pozostałe działy też jak w zleceniu. Kreska 2 px pod banerem działu, 1 px pod Aktualnościami. Szybki dostęp na #202a3c.
- Kontrast: 0 tekstów poniżej AA, najsłabszy 5,84. `--line-ui` 3,72 / 3,29. Kafelki 1,44–1,46.
- Przyciski nie przeskakują po ☀ (okładka i telefon).
- `astro check` 0 błędów, testy 47/47, konsola czysta.
- Zgodność z wzorem B (zrzuty obok siebie).
- Zrzuty: `raport-zrzuty/z34-przed4`, `z34-po4`, `z34-porownanie`.
Odstępstwa od zlecenia i powody:
- Hamburger telefonu bez kółka przez zmienną `--burger-tlo` w regułach, które już miały `!important`, bez nowych `!important`.
- Wewnątrz granatowego banera `--d-a` i `--d-kafel` liczą się z jego jasnej palety (`--ink: #fff`). Nic tam ich nie używa (0 różnic w banerze), wzór ze zlecenia zostawiony.
Pytania do użytkownika:
- Który pasek przycisków miałeś na myśli (pytanie ze zlecenia, nadal otwarte)? Na razie oba jak w prototypie, tylko w ciemnym.

## 33-przelacznik-opublikowane-i-stan-budowy (push kodu) — 2026-11-18 12:28
Status: częściowo — Web-Core (`b7192769..6e370e19`: `c70fc69b`, `cd35ea53`, `6e370e19`) i Web-Podglad (`f11ae37..e64e6a8`) wypchnięte, Podgląd zielony, plakietka działa na żywo; 6 repozytoriów treści (formularze + `opublikowany: true`) czeka na okno pusha wieczorem (punkt 4 „Ochrony zmian redaktorów”)
Zmienione pliki:
- Web-Core: `src/lib/tresci.ts`, `src/lib/szkice.ts` (nowy w części A), `src/lib/podglad.ts` (nowy), `src/lib/kierunki.ts`, `src/lib/menu.ts`, `src/lib/sciezki.ts`, `src/middleware.ts`, `src/pages/sitemap.xml.ts`, `src/layouts/Baza.astro`, `src/components/zal/StanBudowy.astro` (nowy), `src/lib/stanBudowy/{klient.js,styl.css,test-stany.json}` (nowe), `src/pages/podglad/[plik].ts` (nowy), `skrypty/bledy_budowy.py` (nowy), `skrypty/test-stanu-budowy.mjs` (nowy), `skrypty/migracja/opublikowany_33.py` (nowy), `skrypty/migracja/kontrola_redaktorow.py`, `skrypty/test-edytora/formularz.mjs`, `dok/sciagawka-edytora.md` oraz pliki części A (lista w commicie `c70fc69b`)
- Web-Podglad: `.github/workflows/podglad.yml`
- treści (lokalnie, `tresci-z33/*`, gałąź `praca/33-opublikowane`): `.pages.yml` i 28 plików danych w Web-Aktualnosci, Web-Instytut, Web-Nauka, Web-Popularyzacja, Web-Pracownicy, Web-Studia
Kryteria odbioru:
- przełącznik w kierunkach, specjalnościach, „Stronach” i stronach działów, z etykietą ze zlecenia: gotowe lokalnie, push treści wieczorem
- nowe strony domyślnie opublikowane (`default: true`), istniejące z jawnym `opublikowany: true`, żadna nie stała się szkicem: spełnione lokalnie (skrypt sprawdza każdy plik; symulator CMS 48 kontroli OK; zapis bez zmian na 725 plikach: 0 różnic)
- Podgląd pokazuje wszystko i oznacza szkice: spełnione (5 wpisów testowych lokalnie: strony są, etykiety „szkic”, żółty wiersz)
- flaga `TYLKO_OPUBLIKOWANE` ukrywa szkice wszędzie, Core zamrożony: spełnione (735 zamiast 759 stron, także podstrony szkicu; `deploy.yml` nadal wyłączony)
- stan budowy na żywo (plakietka, budowa w toku, dymek, czerwony pasek z polskim komunikatem i „Popraw w CMS”): spełnione; test w Edge 57 OK, 0 błędów w konsoli; na Podglądzie „Aktualna · zbudowana 18.11, 12:27”
- oszczędne zapytania: spełnione (pomiar 10 min: najwyżej 5 odpowiedzi 200 w oknie 10 min; 120 s / 20 s, pauza w tle, 403/429 obsłużone)
- B3 przeciąganie, 4/2 rogi, pamięć rogu, kliknięcie rozwija: spełnione (test i zrzuty `z33-*-rog-*`)
- B4 żółty wiersz z linkiem do formularza w CMS: spełnione (także przy ukryciu pośrednim)
- nic z części B w Core ani na stronie publicznej: spełnione (bez `PODGLAD=1` budowa co do bajtu jak przed zmianą)
- kontrola zmian redaktorów przed i po pushu: do zrobienia wieczorem przy pushu treści; przegląd następnego dnia 19.11
Odstępstwa od zlecenia i powody:
- wynik z API w `localStorage` (wspólny dla kart) zamiast `sessionStorage`: odpowiedź 304 też zmniejsza limit API (sprawdzone)
- `per_page=10` zamiast 5: przerwane przebiegi wypychałyby udane budowy potrzebne do mediany
- pole `opublikowany` pod parą tytuł / tytuł EN (nie między nimi)
- naprawiony brak `pipefail` w `podglad.yml` (zlecenie 41): nieudana budowa mogła opublikować niepełną stronę
- kolejność pushy: kod i workflow w dzień, treści wieczorem
Pytania do użytkownika:
- zakłady i „Warto wiedzieć”: dodać przełącznik w CMS?
- strona działu jako szkic: zostawić (strona zostaje bez tekstu, żółty pasek na Podglądzie) czy dodać też wiersz na plakietce?
- żółty pasek szkicu (`.notice-warn`, sprzed zlecenia) jest zasłonięty przez pasek menu / baner: przesunąć go pod pasek menu?
- dymek „Nowa wersja gotowa” po każdej udanej budowie (także z harmonogramu): zostawić czy tylko przy zmianie otwartej strony?

## 40-cms-jak-w-studiach-i-porzadek-pol (etap 0) — 2026-11-18 12:41
Status: wstrzymane na STOP po etapie 0 (zgodnie ze zleceniem): inwentaryzacja gotowa, bez zmian w repozytoriach, czeka na decyzje właściciela
Zmienione pliki: brak (raporty lokalne: `RAPORT-ZLECENIE-40-0.md`, `RAPORT-ZLECENIE-40-0-pola.md`)
Kryteria odbioru: etap 0 — pola (889 pól w 34 formularzach: 708 używanych, 60 technicznych ukrytych, 15 pustych nieużywanych, 25 z treścią nieużywanych, 13 czytanych, ale niewidocznych), teksty (układy starego parsera i odpowiedniki jawne dla 26 plików), projekt opisów i szablony wpisów: zrobione; etapy 1–6 i kryteria końcowe: niezaczęte
Odstępstwa od zlecenia i powody: brak; uwaga: wzór `strony/studia/podyplomowe.md` jest po zleceniu 39 w `kierunki/podyplomowe.md`
Pytania do użytkownika:
- pola z treścią, ale nieużywane (notatki „do uzupełnienia”, resztki starego banera, przyciski i zdjęcia nagłówków w Ustawieniach, `podtytul_en` kierunków, Facebook/YouTube): zatwierdzić rekomendacje z raportu?
- hasło bez liczb w banerze (dziś niewidoczne na 6 rodzajach stron): pokazywać czy ukryć pole? opisy konferencji: podłączyć?
- kolejność pól we wpisach: Treść po polach identyfikujących wpis (propozycja) czy na samej górze?
- opisy formularzy i szablony nowych wpisów: zatwierdzić; zgoda na `maTresc()` w Web-Core (Treść z samym komentarzem nie może włączać opisu, kasować zaproszenia na obronę ani trafiać do powiadomień)

## 35-szybki-dostep-miejsce — 2026-11-18 12:55
Status: zrobione, wypchnięte (tryb samodzielny). Web-Core `main` `6e370e19..70e9ab73` (po `rebase` na zlecenie 33; jeden konflikt w wierszu importu `DrugiEkran.astro`, połączone obie listy); Podgląd 44298270197 zielony (86 s)
Zmienione pliki: `src/scripts/zal/drugi-ekran.ts`, `src/styles/zalozyciele-strony.css`, `src/components/zal/DrugiEkran.astro`, `src/lib/tresci.ts`
Kryteria odbioru: spełnione, z zastrzeżeniem treści (szczegóły w `RAPORT-ZLECENIE-35.md`).
- Odstępy najwyżej 88 px projektu, nadwyżka pod „Warto wiedzieć”, długa kolumna do stopki. Studia nigdy nie są przypinane; kolejność ustępowania stopka → „Warto wiedzieć” → 2 pozycje → przewijanie.
- Krótkie kolumny „ile się zmieści”, „Zobacz więcej (N)” liczy tylko nadchodzące.
- „Ostatnio” tylko w wolnym miejscu, PL i EN. Zakończone wydarzenie przechodzi do „Ostatnio” (test `page.clock`). W scenariuszu „dużo” „Ostatnio” się nie pokazuje.
- 1920×950 typowo jak dziś: Studia 545 → 545, „Warto” 768 → 767; jedyna różnica to czwarte wydarzenie.
- Macierz 11 × 3: żadna dziura nie urosła. Z treścią „Warto wiedzieć” z 17.11 macierz zgadza się z tabelą zlecenia w tolerancji (wyjątek 1100×1300 typowo: jedna pozycja).
- Telefon: 0 różnic w 8 z 8 porównań. Ctrl + 125/150/200% bez nakładania; zmiana rozmiaru wraca do tego samego stanu; ciemny bez regresji; bez JS 3 pozycje.
- `astro check` 0 błędów (nowe podpowiedzi tylko w plikach zlecenia 33), testy 47/47, konsola czysta.
- Zrzuty i pomiary: `raport-zrzuty/z35-przed2`, `z35-po3`, `z35-po4` (wypchnięta), `z35-po3-1711`, `z35-testy`.
Odstępstwa od zlecenia i powody:
- Odstępy na Full HD 64 px zamiast 74–86, a 1707×830 typowo w trybie 2 zamiast 1. Powód: „Warto wiedzieć” ma dziś nowy wpis z tytułem w 3 wierszach (blok 113 zamiast 92 px). Logika jak w prototypie, sprawdzone na treści z 17.11.
- `data-tryb="miara"` na czas pomiaru (inaczej zapas bez JS chowa dokładane pozycje).
- Zakończone wydarzenia sprawdzane co 60 s i przenoszone do „Ostatnio” (w prototypie usuwane, tylko na starcie).
- Stałe „Ostatnio” (14 dni, 6 pozycji) w `tresci.ts`, bez `ustawienia.json` i bez pola w CMS.
- `dok/estetyka.md` nie istnieje na `main`, opis D3.4 jest w komentarzach w kodzie.
- W `dane_odbior.py` (narzędzie odbioru) komunikat „brak referatów” usuwany jak w prawdziwej budowie zamiast ukrywany.
Pytania do użytkownika:
- `dok/estetyka.md`: odtworzyć z `2f0db28c` i dopisać „Drugi ekran”, czy opis gdzie indziej?
- Po zamianie kolumn Aktualności jako krótka kolumna zostawiają pas 101–115 px (następna aktualność się nie mieści). Przyjąć czy dopuścić tam mniejszy odstęp?
- Wpis „Medale Uniwersytetu…” w „Warto wiedzieć” ma tytuł w 3 wierszach: skrócić czy zostawić?

## 33/39/40 — decyzje właściciela po raportach — 2026-11-18 13:10
Status: zapisane; wdrożenie w kolejności 33 (poprawki) → 39 (PDF) → 40 etapy 1–6
Zmienione pliki: brak (decyzje w raportach lokalnych 33, 39, 40-0)
Kryteria odbioru: nie dotyczy
Odstępstwa od zlecenia i powody: brak
Pytania do użytkownika: brak. Decyzje:
- 33: przełącznik „Opublikowane” w zakładach i „Warto wiedzieć”; szkic strony działu jako wiersz na plakietce; żółty pasek szkicu pod menu; dymek „Nowa wersja gotowa” tylko przy zmianie otwartej strony.
- 39: SIAD zostaje regułą `skrotNazwy`; podyplomowe na szablonie kierunku; poprawiony PDF dla redaktorów robi Code.
- 40: rekomendacje 1a zatwierdzone (ukryć notatki `do_uzupelnienia`, usunąć `etykieta_krotka`, resztki starego banera i `przyciski`, podłączyć `podtytul_en` i zdjęcia nagłówków działów); Facebook i YouTube jako ikony w stopce; hasło bez liczb ukryte; konferencja z opisem dostaje własną stronę; we wpisach Treść po polach identyfikujących, pola EN pod polskimi; `maTresc()` przed szablonami, opisy i szablony jak w raporcie 40-0.

## 37-wpis-aktualnosci-baner-dzialu — 2026-11-18 13:30
Status: zrobione i wypchnięte (Web-Core `70e9ab73..00fff0a8`, tryb samodzielny); Podgląd 44302708750 zielony
Zmienione pliki: `src/layouts/Baza.astro`, `src/components/zal/Podstrona.astro`, `src/components/NaglowekStrony.astro`, `src/components/zal/PasekMenu.astro`, `src/components/zal/PanelMenu.astro`, `src/views/Aktualnosc.astro`, `src/views/AktualnoscZamianaDni.astro`; komentarze: `src/lib/patroni.ts`, `src/components/zal/NaglowekZ.astro`
Kryteria odbioru: spełnione (szczegóły w `RAPORT-ZLECENIE-37.md`, zrzuty `raport-zrzuty/z37-*`).
- Każdy wpis ma baner podstrony działu według `dzialWpisu` (sygnet, kolor, zdjęcie), PL i EN, komputer i telefon, jasny i ciemny; wpisu z Instytutu w danych nie ma.
- Listy (Aktualności, Kalendarz, Obrony, „Warto wiedzieć”, PL i EN): 0 różnych pikseli w 12 z 12 porównań; w całej budowie zmieniły się tylko strony wpisów.
- Pasek i hamburger podświetlają dział wpisu; na telefonie tylko w znacznikach (panel z zasady 6.11 niczego nie podświetla).
- Kolory treści jak dziś: HTML treści, stopki i `<body>` identyczny na 342 stronach wpisów, piksele treści bez zmian (poza szumem JPEG w jednym zdjęciu galerii).
- „Następna strona w dziale” i „Zgłoś błąd” bez zmian; przejścia lista → wpis → wstecz przez przenikanie, bez skoków.
- `astro check` 0 błędów (6 podpowiedzi jak na `main`), testy 47/47, konsola czysta.
Odstępstwa od zlecenia i powody:
- Zamiany dni (osobny widok `AktualnoscZamianaDni.astro`) też dostały baner działu (Studia), żeby nie zostały jedynymi wpisami z banerem Aktualności.
- `<body data-dzial>` wpisu zostaje z adresu (bez działu), bo `[data-dzial]` przestawia `--accent` całej treści.
- Znak i ciekawostka patrona na wpisach niewidoczne, jak na stronach spoza menu działu.
Pytania do użytkownika:
- Podświetlenie działu wpisu w menu zostaje, czy wracamy do „Aktualności”?
- Na telefonie hamburger nie pokazuje bieżącego działu (6.11): wyjątek dla wpisów czy bez zmian?
- Znak i ciekawostka na wpisach: ukryte jak teraz czy pokazać?

## 33-przelacznik-opublikowane-i-stan-budowy (decyzje właściciela z 18.11) — 2026-11-18 13:34
Status: zrobione w kodzie, wypchnięte (Web-Core `00fff0a8..fb54f3f5`, Podgląd 44304735795 zielony); przełącznik w zakładach i „Warto wiedzieć” w lokalnym commicie Web-Instytut `b2de465`, push z resztą treści 33 wieczorem
Zmienione pliki: src/integracje/skrotyPodgladu.mjs (nowy), astro.config.mjs, src/components/zal/StanBudowy.astro, src/layouts/Baza.astro, src/lib/podglad.ts, src/lib/stanBudowy/klient.js, src/styles/global.css, skrypty/migracja/opublikowany_33.py, skrypty/test-stanu-budowy.mjs, dok/sciagawka-edytora.md; Web-Instytut .pages.yml (zaklady, warto_wiedziec) i 1 wpis „Warto wiedzieć”
Kryteria odbioru:
- strona działu-szkic: wiersz na plakietce z linkiem do formularza pliku (…/main/file/strona-dzialu) — spełnione (test PL i EN);
- żółty pasek pod paskiem menu, widoczny na komputerze i telefonie, także po przewinięciu — spełnione (test, zrzuty z33-*-pasek-szkicu);
- dymek tylko przy zmianie otwartej strony — spełnione (skróty stabilne między budowami: 755/755; test „zmieniona” i „bez zmian”; na żywo skroty.json i data-skrot);
- zakłady i „Warto wiedzieć” z przełącznikiem — w kodzie spełnione, w CMS po wieczornym pushu;
- budowa bez Podglądu: tylko nowa nazwa pliku CSS; astro check 0 błędów.
Odstępstwa od zlecenia i powody: na telefonie treść schodzi o wysokość paska (31 px), bo przypięty pasek zasłaniał link „← dział” w banerze.
Pytania do użytkownika: brak.

## 39-kierunki-bez-automatow-i-podyplomowe (PDF dla redaktorów) — 2026-11-18 13:34
Status: zrobione, wypchnięte z [skip ci] (Web-Core `fb54f3f5..5772282f`: źródło i skrypt; Web-Podglad `e64e6a8..f2fe4af`: PDF)
Zmienione pliki: dok/dla-redaktorow/mapa-cms.html (nowy), skrypty/pdf-dla-redaktorow.mjs (nowy); Web-Podglad dla-redaktorow/Mapa-CMS-IM-UWr.pdf
Kryteria odbioru: zdania z kroków 3–4 podmienione — spełnione; PDF ma 2 strony A4 — spełnione (skrypt sprawdza liczbę stron i przepełnienie)
Odstępstwa od zlecenia i powody: poprawiłem też inne nieaktualne miejsca (osobny formularz „Baner” nie istnieje od zleceń 28–29; podyplomowe są kierunkiem). Tabela układów na stronie 2 czeka na zlecenie 40.
Pytania do użytkownika: brak.

## 36-patron-raz-i-dotyk-na-okladce (część „Dotyk”, wariant A) — 2026-11-18 14:00
Status: zrobione, wypchnięte (Web-Core `5772282f..a0e32c28`, po rebase na 33 i 39; Podgląd 44308419922 zielony). Część „Odłożone” (przelot patrona do banera) niewdrożona, zgodnie z decyzją z 17.11, 22:40.
Zmienione pliki: src/scripts/zal/okladka.ts, src/styles/zalozyciele.css
Kryteria odbioru:
- stuknięcie: dorysowanie w 312–331 ms z nazwiskiem i barwieniem, potem przejście (start 330–348 ms) — spełnione (4 działy × tablet/laptop dotykowy × 1366×1024, 1180×820, 1280×800);
- przewinięcie i przytrzymanie bez przejścia, podwójne stuknięcie przechodzi raz — spełnione;
- po „wstecz” okładka czysta (bez .z-dotyk, barwienia i narysowanego patrona) — spełnione;
- mysz i klawiatura bez zmian (stan co klatkę i zrzuty przed/po; różnice tylko w podskakującej strzałce), laptop: palcem jak tablet, myszą jak komputer — spełnione;
- telefon 390 i 768 px: 0 różnic pikseli — spełnione;
- raport z seriami klatek i listą „Do raportu” — RAPORT-ZLECENIE-36.md, raport-zrzuty/z36-*.
Odstępstwa od zlecenia i powody:
- zamiast filmów serie klatek (screencast), bo recordVideo wymaga pobrania ffmpeg;
- dodatkowe progi: przesunięcie 12 px (na okładce touch-action: pinch-zoom, więc bez pointercancel), przytrzymanie 0,5 s (nie każda przeglądarka wysyła contextmenu), zgaszenie po podniesieniu palca bez kliknięcia;
- [data-z-dotyk] na okładce obok @media (hover: hover), bo laptop dotykowy ma kursor;
- dok/estetyka.md nie istnieje — opis w komentarzach nagłówków plików.
Pytania do użytkownika:
- 0,3 s, nazwisko i barwienie przy stuknięciu zostają?
- powiększyć pola dotyku poniżej 44 px pod (pointer: coarse)?
- tablet w pionie: węższa kolumna treści albo dwie kolumny Szybkiego dostępu?
- pełna nazwa SIAD tylko w title (na dotyku niewidoczna) — pokazać inaczej?
- zdjąć efekty najechania z linków na dotyku?

## 40-cms-jak-w-studiach-i-porzadek-pol, etap 1 (Web-Instytut) — 2026-11-18 14:05
Status: Web-Core zrobione i wypchnięte (`a0e32c28..0cda774c`); Web-Instytut: commit gotowy w `tresci-z40/Web-Instytut` (`88d8f50`), push w oknie wieczornym po treściach zlecenia 33 (zaplanowany na 20:41)
Zmienione pliki: Web-Core: src/lib/tresci.ts (maTresc, bezKomentarzy) i 12 miejsc z body?.trim(), src/lib/tekstyStron.ts, src/lib/widoki/strona.ts, skrypty/jawny-markdown-repo.mjs (nowy), skrypty/migracja/formularze_40.mjs (nowy), skrypty/sprawdz-jawny-markdown.mjs, skrypty/migracja/kontrola_redaktorow.py, dok/jawny-markdown.md; Web-Instytut: .pages.yml, 12 Stron, src/data/instytut.md
Kryteria odbioru (etap 1):
- Strony i strona działu w jawnym Markdownie z komentarzami i {#id} — spełnione (13 plików, 64 nagłówki z {#id});
- opisy formularzy, Treść na górze, pola EN pod polskimi, pola techniczne ukryte, decyzje 18.11 (władze) — spełnione;
- wygląd bez zmian: porównanie HTML całej strony 0 różnic (kod i dane, PL i EN) — spełnione;
- sprawdz_pola_cms.py 0 problemów, sprawdz-jawny-markdown OK, astro check 0 błędów, test:jawne 47/47 — spełnione;
- push treści z kontrolą redaktorów przed i po, test w CMS, przegląd następnego dnia — w toku (wieczór / 19.11).
Odstępstwa od zlecenia i powody: limity linii w jawnych Stronach dla tekstu polskiego (inaczej 2 strony zmieniłyby pomiar układu); dawne „Bloki wzorca” ukryte zamiast usunięte; etykiety pól, których nowy nagłówek nie pokazuje, poprawione („Opis strony dla Google”). Szczegóły: RAPORT-ZLECENIE-40-1.md.
Pytania do użytkownika: przywrócić limity linii w Stronach Studiów (brak od ich migracji)? ukryć też „Źródła” w „Warto wiedzieć” i Władzach?

## 44-kariera-podstrona-aktualnosci — 2026-11-18 14:16
Status: wstrzymane (limit użycia). Kod gotowy w lokalnym commicie WIP a4808af0 na gałęzi praca/44-kariera w Web-Core-B (niewypchnięty). Zmiany Web-Aktualnosci (.pages.yml: grupa „Termin zgłoszeń”, opis „Rodzaj”, opis Stron; nowy src/content/strony/kariera.md) niezacommitowane w klonie tresci-B/Web-Aktualnosci.
Zrobione: budowa OK; sprawdz_tresci.py i sprawdz_pola_cms.py OK (venv source/wc28-venv); symulacja formularza (scenariusz 9) 0 problemów, zapis bez zmian 726 plików bez różnic; porównanie HTML przed/po (raport-zrzuty/z44-html.txt) — różnice zgodne ze zleceniem, do sprawdzenia: .ics w kalendarzu (prawdopodobnie znacznik czasu budowy).
Zostało: przegląd różnic .ics, budowa testowa z terminami (wczoraj/dziś/później), zrzuty, astro check, testy, raport RAPORT-ZLECENIE-44.md, push Web-Core; push Web-Aktualnosci wieczorem lub po wiadomości do redaktorów. Potem zlecenie 43 i raport zbiorczy.
Pytania do użytkownika: plik strony to kariera.md (jak w zleceniu), choć adres to /aktualnosci/kariera — zostaje?

## 40-cms-jak-w-studiach-i-porzadek-pol, etap 2 (Web-Nauka) — 2026-11-18 15:05
Status: Web-Core zrobione i wypchnięte (`0cda774c..91b5beb8`, Podgląd zielony); Web-Nauka: commit gotowy w `tresci-z40/Web-Nauka` (`b01f1ec`), push w oknie wieczornym po treściach zleceń 33 i 40.1 (zaplanowany na 21:13)
Zmienione pliki: Web-Core: src/views/Konferencja.astro, src/lib/widoki/konferencja.ts, src/pages/nauka/konferencje/[slug].astro i wersja EN (nowe), src/lib/tresci.ts (adresKonferencji), src/lib/sciezki.ts, src/pages/sitemap.xml.ts, src/lib/kalendarz.ts, src/lib/motywyBanerow.ts, src/views/ListaKonferencji.astro, src/views/Zaklad.astro, src/views/DzialNauka.astro, skrypty/migracja/formularze_40.mjs, skrypty/jawny-markdown-repo.mjs; Web-Nauka: .pages.yml, 6 Stron, src/data/nauka.md
Kryteria odbioru (etap 2):
- Strony i strona działu w jawnym Markdownie z komentarzami i {#id} (w tym {#czasopisma}) — spełnione (7 plików, 10 nagłówków z {#id});
- opisy formularzy, Treść pod tytułami, tytuł EN pod polskim, pola techniczne ukryte, szablony Treści konferencji i projektu — spełnione;
- decyzja 18.11 „opisy konferencji: osobna strona i link z listy” — spełnione (17 stron PL i EN);
- porównanie HTML: kod — różnice tylko zatwierdzone (strony konferencji i linki do nich, ICS, mapa strony); dane — 0 różnic (923 pliki);
- sprawdz_pola_cms.py 0 problemów, sprawdz-jawny-markdown OK, astro check 0 błędów, test:jawne 47/47 — spełnione;
- push treści z kontrolą redaktorów, test w CMS, przegląd następnego dnia — w toku (wieczór / 19.11).
Odstępstwa od zlecenia i powody: szablon Treści projektu poprawiony względem raportu 40-0 („strona projektu pokaże same dane”, bo stronę ma każdy projekt); link na stronę konferencji także w kalendarzu, ICS i na stronach zakładów (jedna reguła, jak w projektach). Szczegóły: RAPORT-ZLECENIE-40-2.md.
Pytania do użytkownika: zostaje poprawione brzmienie szablonu projektu? dodać „Opis EN” konferencji?

## 40-cms-jak-w-studiach-i-porzadek-pol, etap 4 (Web-Pracownicy) — 2026-11-18 15:05
Status: Web-Core zrobione i wypchnięte (`23050dd2..641cf76e`, tylko skrypt; Podgląd zielony); Web-Pracownicy: commit gotowy w `tresci-z40/Web-Pracownicy` (`ff4aec1`), push w oknie wieczornym po treściach zlecenia 33 (zaplanowany na 21:43)
Zmienione pliki: Web-Core: skrypty/migracja/formularze_40.mjs; Web-Pracownicy: .pages.yml, src/content/strony/pracownicy.md
Kryteria odbioru (etap 4):
- tekst strony Pracownicy w jawnym Markdownie (format_tresci, komentarz; Treść pusta jak dotąd) — spełnione;
- opis formularza Pracownicy, Treść pod tytułami w Stronach, pola techniczne ukryte — spełnione;
- porównanie HTML 0 różnic (923 pliki), sprawdz_pola_cms.py 0 problemów, sprawdz-jawny-markdown OK, astro check 0 błędów — spełnione;
- push treści z kontrolą redaktorów, test w CMS, przegląd następnego dnia — w toku (wieczór / 19.11).
Odstępstwa od zlecenia i powody: etap 4 przed etapem 3 — Web-Aktualnosci ma niezatwierdzone zmiany .pages.yml drugiej sesji (zlecenie 44), etap 3 po ich pushu. Przy okazji poprawione dwa błędy w moich skryptach pushów 40 (warunek „33 na main” przez zamianę ścieżki w Git Bash; warunek porównania HTML), przez które push 40.1 o 20:41 zatrzymałby się bez powodu. Szczegóły: RAPORT-ZLECENIE-40-4.md.
Pytania do użytkownika: brak nowych.

## 44-kariera-podstrona-aktualnosci — 2026-11-18 15:10
Status: Web-Core zrobione i wypchnięte (`91b5beb8..23050dd2`, Podgląd 44319663976 zielony; na żywo /aktualnosci/kariera z 11 ofertami, ramka „(11)” na liście). Web-Aktualnosci: commit `e2b51a5` (.pages.yml + src/content/strony/kariera.md w jednym commicie) na lokalnej gałęzi praca/44-kariera w tresci-B/Web-Aktualnosci, od origin/main e4c9c62; push zaplanowany na 20:07 w tej sesji (fetch, kontrola zapisów redaktorów, sprawdz_pola_cms, symulacja formularza, push, Podgląd). Okno 1: etap 3 zlecenia 40 (Web-Aktualnosci) może nałożyć się na .pages.yml po tym pushu; jeśli wypchnie wcześniej, nałożę swoją grupę na nową wersję.
Zmienione pliki: Web-Core: src/lib/tresci.ts, src/content.config.ts, src/lib/tekstyStron.ts, src/lib/widoki/{listaAktualnosci,listaOfert,dzialStudia}.ts, src/views/{ListaAktualnosci,ListaOfert,Aktualnosc}.astro, src/components/WierszAktualnosci.astro, src/components/zal/ListaPokaz.astro, src/scripts/zal/czytaj-dalej.ts, src/pages/aktualnosci/kariera.astro i EN, src/pages/sitemap.xml.ts, skrypty/sprawdz_tresci.py, skrypty/test-edytora/formularz.mjs, .gitignore; Web-Aktualnosci: .pages.yml, src/content/strony/kariera.md (nowy).
Kryteria odbioru:
- oferty nie są na liście Aktualności, stronie głównej, w liczbie na okładce ani w RSS — spełnione (porównanie HTML przed/po: raport-zrzuty/z44-html3.txt);
- /aktualnosci/kariera i EN z aktualnymi i „Zakończonymi”, teksty w Strony → Kariera — spełnione (teksty z CMS po pushu Web-Aktualnosci, do tego czasu domyślne);
- ramka „Oferty pracy, staży i stypendiów (N) →” na komputerze i telefonie, N = aktualne — spełnione;
- opcjonalny termin zgłoszeń w formularzu, po terminie „Zakończone” i znika ze Studiów — spełnione na kopii testowej; w formularzu po pushu Web-Aktualnosci;
- Studia tylko aktualne oferty, link wstecz do Kariery — spełnione;
- ?rodzaj=kariera przekierowuje, nazwa „kariera” zastrzeżona dla wpisów — spełnione;
- bez migracji danych, zapisy redaktorów zachowane — zapis bez zmian 726 plików 0 różnic; kontrola przed/po pushu dziś wieczorem, przegląd 19.11.
Odstępstwa od zlecenia i powody: opis grupy z „(kliknij „Add an item”)” i etykieta z „(tylko oferty…)”; dopisek terminu także w wierszach list; zła data terminu i plik kariera.md to błędy w sprawdz_tresci.py (budowa tylko ostrzega). Szczegóły: RAPORT-ZLECENIE-44.md.
Pytania do użytkownika: nazwa pliku kariera.md zostaje? hasło „Praca, staże, stypendia”? nawigacja nowszy/starszy we wpisach ofert tylko po ofertach? wiadomość do redaktorów przed pushem Web-Aktualnosci?

## 40-cms-jak-w-studiach-i-porzadek-pol, etap 5 (seminaria, 9 repozytoriów) — 2026-11-18 15:15
Status: Web-Core zrobione i wypchnięte (`641cf76e..0b239768`, tylko skrypt; Podgląd zielony); 9× Web-Sem-*: commity gotowe w `tresci-z40/Web-Sem-*` (gałąź `praca/40-seminaria`), push w oknie wieczornym (zaplanowany na 22:13; próba bez pusha OK)
Zmienione pliki: Web-Core: skrypty/migracja/formularze_40.mjs; 9× Web-Sem-*: .pages.yml
Kryteria odbioru (etap 5):
- jeden wzór formularzy dla 9 repozytoriów, wdrożony skryptem — spełnione;
- opis formularza seminarium, Opis/Streszczenie pod tytułem, pola EN pod polskimi, notatka redakcyjna ukryta, szablon streszczenia — spełnione;
- wygląd bez zmian: dane bez zmian; szablon streszczenia sprawdzony budową (0 różnic w 926 plikach) — spełnione;
- sprawdz_pola_cms.py 0 problemów; kontrola redaktorów przed/po w 9 repozytoriach OK — spełnione;
- push treści, test w CMS, przegląd następnego dnia — w toku (wieczór / 19.11).
Odstępstwa od zlecenia i powody: puste `do_uzupelnienia` w 8 seminariach ukryte zamiast usunięte (lista 1c z raportu 40-0 nie miała wyraźnej decyzji). Szczegóły: RAPORT-ZLECENIE-40-5.md.
Pytania do użytkownika: usunąć pola z listy 1c raportu 40-0 (puste `do_uzupelnienia` w 8 seminariach, `partnerzy` i `baner.podpis_telefon(_en)` w Web-Ustawienia)?

## 43-plan-zajec-rok-akademicki-od-sierpnia — 2026-11-18 16:15
Status: częściowo. Etapy 1 i 3 zrobione i wypchnięte (`0b239768..057513dc`: `ee446fee` etap 1, `057513dc` etap 3; Podgląd 44323847367 zielony). Etap 2 niewdrożony — czeka na decyzję właściciela (dokumentacja GitHub nie potwierdza, że wywołanie enable zeruje licznik 60 dni; jest relacja przeciwna).
Zmienione pliki: skrypty/plan/pobierz_plan.py (etap 1); src/components/zal/Okladka.astro, src/styles/zalozyciele.css (etap 3).
Kryteria odbioru:
- zakładki zawsze zimowy i letni jednego roku akademickiego, zmiana 1 sierpnia — spełnione (test bez sieci na zapisanym terms_index: 7 dat ze zlecenia + granica 31.07/1.08 w dwóch latach; aktywna zakładka z wybierzSemestr() zgodna z tabelą zlecenia);
- ta sama reguła przy awarii USOS API — spełnione (test trybu awaryjnego);
- brak semestru w USOS nie psuje pobrania, pusta zakładka z komunikatem — spełnione (przebieg main() bez sieci, kod 0; budowa z pustym semestrem pokazuje „Plan na ten semestr nie jest jeszcze dostępny w USOS.” PL i EN);
- dzień zmiany w jednym miejscu — spełnione (ZMIANA_ROKU = (8, 1));
- --semestr jak dziś — spełnione (test z API i przy awarii);
- prawdziwe pobranie dziś: plan.json bez zmian — spełnione (stary i nowy skrypt identyczny wynik, równy plikowi w repozytorium);
- plan-zajec.yml i podglad.yml podtrzymywane co tydzień, deploy.yml wyłączony; nieudane podtrzymanie jako błąd — niespełnione, czeka na decyzję (warianty A–E w raporcie, rekomendacja A + B); deploy.yml dalej disabled_manually;
- logo UWr na każdej szerokości prowadzi na uwr.edu.pl, napisy jak dziś — spełnione (zlecenie 32; elementFromPoint 1920/1366/1024/390, PL i EN, okładka, drugi ekran, /instytut/wladze);
- wygląd bez zmian, osobny fokus dla logo i napisu — spełnione (18 par zrzutów: obszar logo bez różnic; różnice tylko tam, gdzie różnią się dwa wczytania tej samej budowy; Tab: pomiń → logo → napis, obwódka przy każdym).
Odstępstwa od zlecenia i powody: etap 2 niewdrożony (jak wyżej, zgodnie ze zleceniem); w etapie 3 poprawiona kolejność dopisku „(inna strona)” w linku Wydziału na okładce (był przed nazwą, zlecenie wymaga po); semestr nieznany w USOS jest pomijany przy pobieraniu (bez tego tryb awaryjny API robiłby do 2500 zapytań 3 razy dziennie). Szczegóły: RAPORT-ZLECENIE-43.md.
Pytania do użytkownika: etap 2 — który wariant (A enable co tydzień, B wzajemna kontrola stanu, C token właściciela, D commit z danymi, E przypomnienie)? poprawić też kolejność dopisku w linku Wydziału na okładce telefonu (Naglowek.astro)? przy awarii API brać daty semestrów z poprzedniego pliku?

## 40-cms-jak-w-studiach-i-porzadek-pol (etap 6: Web-Ustawienia) — 2026-11-18 15:35
Status: częściowo. Web-Core część 1/2 wypchnięta (`057513dc..1ab56e50`: ikony Facebooka i YouTube w stopce, skrypty). Commit Web-Ustawienia `05080a9` gotowy, push w oknie wieczornym (22:43), zaraz po nim część 2/2 Web-Core (zdjęcia nagłówków działów z CMS) — dopiero gdy dane są na main.
Zmienione pliki: Web-Core: src/components/zal/StopkaZ.astro, skrypty/migracja/formularze_40.mjs, skrypty/migracja/kontrola_redaktorow.py (--pomin), skrypty/sprawdz-jawny-markdown.mjs; wieczorem: src/components/zal/NaglowekZ.astro, src/components/NaglowekStrony.astro. Web-Ustawienia: .pages.yml, src/data/ustawienia.json, src/content/strony/{deklaracja-dostepnosci,polityka-prywatnosci,o-stronie}.md
Kryteria odbioru (etap 6):
- strony ze stopki w jawnym Markdownie, {#id} z dzisiejszymi adresami — spełnione (sprawdz-jawny-markdown OK, 18 nagłówków);
- opisy formularzy, Treść na górze, pola techniczne ukryte, decyzje 1a i pytanie 3 — spełnione;
- wygląd bez zmian poza zatwierdzonymi różnicami — spełnione: porównanie 925 plików, różnica tylko w bloku ikon stopki (decyzja 2), po jego wycięciu 0 różnic; wysokość stopki bez zmian (1024–2560 i telefon);
- sprawdz_pola_cms.py 0 problemów; kontrola redaktorów przed (0 zapisów od bazy f145d85) i po (OK z --pomin dla pól z decyzji) — spełnione;
- push treści, część 2 Web-Core, test w CMS, przegląd następnego dnia — w toku (wieczór / 19.11).
Odstępstwa od zlecenia i powody: Web-Core w dwóch częściach, treść pomiędzy — kod zdjęć nagłówków potrzebuje nowych danych (dziś w danych stare, nieużywane kadry), a push treści musi być wieczorem; inaczej nagłówki zmieniłyby się na kilka godzin. Szczegóły: RAPORT-ZLECENIE-40-6.md.
Pytania do użytkownika: lista 1c (jak w etapie 5); usunąć nieużywane pliki zdjęć po usuniętych polach (kampus-zmierzch-1200.jpg, instytut-telefon.jpg)? czy kadr nagłówka z CMS ma działać także na podstronach (zmieni wygląd podstron Instytutu i Nauki)?

## 40-cms-jak-w-studiach-i-porzadek-pol (etap 7: Web-Studia, Web-Popularyzacja) — 2026-11-18 15:45
Status: częściowo. Web-Core wypchnięty (`1ab56e50..3e81655e` i `3e81655e..add78d45`, tylko skrypty; Podgląd dla `3e81655e` zielony). Commity treści gotowe: Web-Studia `0217209` (baza `b2a7c09`), Web-Popularyzacja `2795ca8` (baza `0f76f88`); push w oknie wieczornym (23:13, `push40_studia_popularyzacja.sh`).
Zmienione pliki: Web-Core: skrypty/migracja/formularze_40.mjs, skrypty/migracja/kontrola_redaktorow.py. Web-Studia: .pages.yml, src/content/kierunki/{isim,matematyka,siad,szkola-doktorska}.md (tylko nagłówek YAML). Web-Popularyzacja: .pages.yml
Kryteria odbioru (etap 7):
- pola EN pod polskimi, Treść na górze, etykiety „… EN” — spełnione;
- pola nieużywane według decyzji 1a: `etykieta_krotka(_en)` usunięte z formularza i 4 kierunków — spełnione; `podtytul_en` niepodłączone (patrz pytania);
- wygląd bez zmian — spełnione (porównanie HTML Studiów: 0 różnic w 925 plikach; Popularyzacja zmienia tylko `.pages.yml`);
- sprawdz_pola_cms.py 0 problemów, sprawdz-jawny-markdown OK, kontrola redaktorów przed (0 zapisów od bazy) i po (OK) — spełnione;
- push treści, test w CMS, przegląd następnego dnia — w toku (wieczór / 19.11).
Odstępstwa od zlecenia i powody: `podtytul_en` nie podłączony mimo decyzji 1a — nowy nagłówek kierunku nie pokazuje nadtytułu w żadnym języku, więc podłączenie samego EN dałoby różnicę PL/EN; hasło na Stronach Studiów zostaje widoczne z opisem (pokazuje się na 4 z 13 stron z hasłem, jeden formularz dla wszystkich). Szczegóły: RAPORT-ZLECENIE-40-7.md.
Pytania do użytkownika: pokazać nadtytuł kierunku w obu językach czy zostawić niewyświetlany? pokazywać hasło Stron Studiów także bez liczb (9 stron)?

## 40-cms-jak-w-studiach-i-porzadek-pol (na koniec: dokumentacja) — 2026-11-18 15:55
Status: częściowo. Web-Core wypchnięty (`add78d45..910853ea`, tylko `dok/`). PDF „Mapa CMS” do Web-Podglad zaplanowany na 23:43, po pushach treści (`push40_pdf.sh`; próba: skrypt poprawnie czeka na treści na main).
Zmienione pliki: dok/jawny-markdown.md, dok/sciagawka-edytora.md, dok/dla-redaktorow/mapa-cms.html; wieczorem w Web-Podglad: dla-redaktorow/Mapa-CMS-IM-UWr.pdf
Kryteria odbioru:
- ściągawka, `jawny-markdown.md` i PDF dla redaktorów aktualne — spełnione dla etapów 1, 2, 4–7 (PDF: po pushu 23:43); Strony Aktualności opisane jako dawny format do etapu 3.
Odstępstwa od zlecenia i powody: dokumentacja przed etapem 3 (Web-Aktualnosci czeka na push zlecenia 44 z drugiego okna); po etapie 3 do usunięcia zdanie o dawnym formacie Stron Aktualności. Szczegóły: RAPORT-ZLECENIE-40-7.md, sekcja „Dokumentacja”.
Pytania do użytkownika: brak nowych.

## 43-plan-zajec-rok-akademicki-od-sierpnia (etap 2, po decyzji właściciela) — 2026-11-18 17:05
Status: zrobione; zostaje jednorazowe kliknięcie właściciela (uprawnienie Actions: Read and write dla aplikacji „IM-UWr strona powiadomienia”, instrukcja w README Web-Core, „Harmonogramy GitHub”, i w RAPORT-ZLECENIE-43.md). Wypchnięte: Web-Podglad `f2fe4af0..6abb1bb6`, Web-Core `b43b0aa8..d436ab69` (zwykły push). Przekaźnik 44341507520 i 44341705470, plan-zajec.yml 44341565229, podtrzymanie.yml 44341558338, Podgląd 44341742516 — zielone.
Zmienione pliki: Web-Core: .github/workflows/podglad-przekaznik.yml (krok „Harmonogramy” przed sygnałem), .github/workflows/plan-zajec.yml (cron pon. 04:13 UTC, zadanie „podtrzymanie”), README.md; Web-Podglad: .github/workflows/podtrzymanie.yml (nowy, pon. 04:43 UTC), .github/workflows/podglad.yml (tylko komentarz).
Kryteria odbioru:
- przekaźnik przy każdym przebiegu sprawdza plan-zajec.yml i podglad.yml, wyłączony włącza i zostawia ::warning — spełnione (21 scenariuszy z atrapą gh; na GitHubie: plan-zajec.yml PUT enable → 204);
- krok dla Web-Podglad bez uprawnienia aplikacji tylko ostrzega — spełnione (na GitHubie ostrzeżenie HTTP 403 z odsyłaczem do instrukcji, przekaźnik zielony, sygnał wysłany);
- cotygodniowe enable i czerwony przebieg z jasnym komunikatem (A + B) — spełnione (ręczne uruchomienia: 204 w Web-Core i dwa razy w Web-Podglad, kontrola drugiego repozytorium active; komunikaty błędów sprawdzone w scenariuszach);
- bez osobistych tokenów i bez commitów — spełnione (GITHUB_TOKEN i klucz aplikacji; przebiegi niczego nie commitują);
- pozostałe kroki jak przedtem — spełnione (zadanie „plan” i budowa Podglądu: te same kroki i wyniki; przekaźnik: tylko nowy krok);
- lista zaplanowanych workflowów i termin następnego podtrzymania — w raporcie (następne co tydzień: 23.11, 04:13 i 04:43 UTC; przekaźnik przy każdym zapisie); deploy.yml dalej disabled_manually;
- link do dokumentacji potwierdzającej zerowanie licznika — niespełnione, bo takiej nie ma; decyzja właściciela opiera się na przekaźniku, który włącza z powrotem niezależnie od licznika.
Odstępstwa od zlecenia i powody: główny mechanizm to przekaźnik (decyzja właściciela), co tydzień tylko zapas; w Web-Podglad osobny plik podtrzymanie.yml zamiast zadania w podglad.yml, bo plakietka stanu budowy czyta przebiegi podglad.yml; workflowów wyłączonych ręcznie nic nie włącza (ostrzeżenie / czerwony przebieg). Szczegóły: RAPORT-ZLECENIE-43.md.
Pytania do użytkownika: czy workflow wyłączony ręcznie też włączać automatycznie (dziś tylko ostrzeżenie)?

## 33-przelacznik-opublikowane-i-stan-budowy i 40-cms-jak-w-studiach-i-porzadek-pol (push treści) — 2026-11-18 17:25
Status: zrobione, oprócz etapu 3 zlecenia 40 (Web-Aktualnosci), który czeka na push zlecenia 44 z drugiego okna. Treści wypchnięte 16:48–17:17 (zwykły push, bez force), przed wieczorem na polecenie właściciela. Podgląd zielony po każdej serii: 44340270000, 44341742516, 44342490266, 44343845368, 44344905430 (w logach właśnie wypchnięte SHA).
Zmienione pliki (zakresy na main):
- 33: Web-Aktualnosci `e4c9c62..46d7f90`, Web-Instytut `311faae..b2de465`, Web-Nauka `498bc8d..e85c60a`, Web-Popularyzacja `0f76f88..72e08cd`, Web-Pracownicy `5bcaf22..4015203`, Web-Studia `b2a7c09..f31a027`;
- 40.1 Web-Instytut `b2de465..88d8f50`; 40.2 Web-Nauka `e85c60a..b01f1ec`; 40.4 Web-Pracownicy `4015203..ff4aec1`; 40.5 9× Web-Sem-* (tylko .pages.yml, zakresy w RAPORT-ZLECENIE-40-5.md);
- 40.6 Web-Ustawienia `f145d85..05080a9`, potem Web-Core `d436ab69..5131ebf2` (zdjęcia i kadry nagłówków działów z CMS);
- 40.7 Web-Core `910853ea..b43b0aa8` (skrypt formularzy Popularyzacji z polem „Opublikowane”), Web-Studia `f31a027..a8964db`, Web-Popularyzacja `72e08cd..0993e8e`;
- PDF „Mapa CMS”: Web-Podglad `6abb1bb..da76859` (`[skip ci]`).
Kryteria odbioru:
- „Ochrona zmian redaktorów” — spełnione: przed każdym pushem 0 zapisów redaktorów od bazy, kontrola po pushu OK w każdym repozytorium;
- strona bez zmian tam, gdzie zmieniają się tylko formularze i zapis Treści — spełnione: porównanie HTML przed/po 0 różnic (40.1, 40.2, 40.4, 40.6 z częścią 2 Web-Core, 40.7 Studia);
- przegląd zapisów redaktorów z 24 h i testy w CMS — do zrobienia 19.11, ok. 16:50–17:15 (lista w RAPORT-ZBIORCZY-2026-11-18.md).
Odstępstwa od zlecenia i powody: push treści przed oknem wieczornym — na wyraźne polecenie właściciela („Dobra, zgadzam sie wrażamy teraz”). W 40.7 bazą kontroli redaktorów jest commit zlecenia 33 na main, bo pierwszy przebieg (17:10) brał moją zmianę `.pages.yml` z 33 za zapis redaktora i się zatrzymał (nic nie wypchnięte); zapisy sprzed tego commitu sprawdziła kontrola 33. Szczegóły: RAPORT-ZLECENIE-33.md, RAPORT-ZLECENIE-40-1.md … 40-7.md.
Pytania do użytkownika: bez nowych; otwarte pytania etapów 1–7 bez zmian (RAPORT-ZBIORCZY-2026-11-18.md, „Pytania otwarte”).

## 44-kariera-podstrona-aktualnosci (push Web-Aktualnosci) — 2026-11-18 17:35
Status: zrobione. Web-Aktualnosci wypchnięte o 16:31 UTC (`46d7f90..422bb59`, zwykły push), wcześniej niż planowane 20:07 — na polecenie użytkownika. Powiadom 44348295078, przekaźnik 44348328367, Podgląd 44348385389 — zielone (w logu Web-Aktualnosci: main @ 422bb59).
Zmienione pliki: Web-Aktualnosci: .pages.yml (grupa „Termin zgłoszeń” zgloszenia/do_dnia, opis „Rodzaj”, opis Stron), src/content/strony/kariera.md (nowy; z opublikowany: true).
Kryteria odbioru:
- push po fetch i nałożeniu na nowy .pages.yml — spełnione (rebase na 46d7f90, zlecenie 33, bez konfliktów; zapisów redaktorów od podstawy brak);
- sprawdz_pola_cms.py i symulacja formularza — spełnione (0 problemów; zapis bez zmian 726 plików, 0 różnic; scenariusz 9 OK);
- Podgląd i strona Kariera z tekstami z kariera.md, ramka „(11)” — spełnione (na żywo PL i EN).
Odstępstwa od zlecenia i powody: push o 17:31, nie wieczorem — polecenie użytkownika; do kariera.md dopisane opublikowany: true, bo zlecenie 33 dało to pole wszystkim Stronom. Szczegóły: RAPORT-ZLECENIE-44.md, „Push Web-Aktualnosci”.
Pytania do użytkownika: czy napisać redaktorom o grupie „Termin zgłoszeń” i stronie Kariera w Stronach?

## 40-cms-jak-w-studiach-i-porzadek-pol (etap 3: Web-Aktualnosci) — 2026-11-18 18:10
Status: częściowo. Web-Core wypchnięty (`5131ebf2..0951f7b4`, tylko skrypt formularzy). Web-Aktualnosci: commit gotowy (`f91eac2` w `tresci-z40/Web-Aktualnosci`), push zaraz po pushu zlecenia 44 z drugiego okna — decyzja właściciela 18.11 („Przygotuj teraz”); skrypt czeka na 44 na main (do 23:30), potem na zielony Podgląd, robi migrację od nowa na main z 44 i wszystkie kontrole.
Zmienione pliki: Web-Core: skrypty/migracja/formularze_40.mjs; Web-Aktualnosci (po pushu): .pages.yml, src/content/strony/aktualnosci.md, obrony-doktorskie.md, kariera.md
Kryteria odbioru:
- Strony w jawnym Markdownie z komentarzem jak w Studiach — spełnione w commicie (2 pliki; po 44 także kariera.md, sprawdzone na kopii commitu 44);
- opisy formularzy Aktualności i Obron, Treść na swoim miejscu, pola EN pod polskimi, pola techniczne ukryte — spełnione;
- wygląd stron bez zmian — spełnione: porównanie HTML całej strony 0 różnic w 925 plikach; szablony Treści: różni się tylko niewidoczny komentarz w źródle strony testowej aktualności i oferty, obrona bez zmian;
- sprawdz_pola_cms 0 problemów, sprawdz-jawny-markdown OK, kontrola redaktorów przed i po: OK — spełnione na commicie; powtórzone przy pushu;
- test w CMS i przegląd 24 h po pushu — do zrobienia po pushu.
Odstępstwa od zlecenia i powody: opis formularza Aktualności uzupełniony o oferty „Kariera” (od zlecenia 44 nie ma ich na liście Aktualności); opis Treści EN obrony poprawiony zgodnie z widokiem obrony; push po 44, nie przed (decyzja właściciela). Szczegóły: RAPORT-ZLECENIE-40-3.md.
Pytania do użytkownika: brak nowych.

## 40-cms-jak-w-studiach-i-porzadek-pol (etap 3: push Web-Aktualnosci i dokumentacja) — 2026-11-18 18:10
Status: zrobione. Web-Aktualnosci `422bb59..56caf58` (18:03, zaraz po zleceniu 44 z drugiego okna; migracja od nowa na main z 44, także kariera.md); Web-Core dokumentacja `0951f7b4..02a2e8aa`; PDF „Mapa CMS” Web-Podglad `da76859..5b4e8f2` ([skip ci]). Podgląd 44354449898 zielony (z 56caf58).
Zmienione pliki: Web-Aktualnosci: .pages.yml, src/content/strony/aktualnosci.md, kariera.md, obrony-doktorskie.md; Web-Core: dok/jawny-markdown.md, dok/sciagawka-edytora.md, dok/dla-redaktorow/mapa-cms.html; Web-Podglad: dla-redaktorow/Mapa-CMS-IM-UWr.pdf
Kryteria odbioru:
- „Ochrona zmian redaktorów” — spełnione: 0 zapisów od bazy (422bb59), całe repozytorium pole po polu przed pushem i po nim: tylko zmiany z migracji;
- wygląd bez zmian — spełnione: HTML całej strony 0 różnic w 925 plikach (z /aktualnosci/kariera);
- dokumentacja i PDF aktualne — spełnione dla wszystkich etapów (bez wyjątku dla Stron Aktualności);
- test w CMS i przegląd 24 h — 19.11, ok. 18:05.
Odstępstwa od zlecenia i powody: push przed wieczorem — decyzja właściciela („Przygotuj teraz”: wypchnąć zaraz po 44). Pierwsze uruchomienie skryptu zatrzymało się przed czymkolwiek na nieśledzonym pliku skrypty/test-edytora/package-lock.json (nie mój); poprawka --untracked-files=no. Szczegóły: RAPORT-ZLECENIE-40-3.md.
Pytania do użytkownika: brak nowych.

## 45-tutornia — 2026-11-18 19:45
Status (19:52): wypchnięte na polecenie „Push”. Web-Core `02a2e8aa..3cde30e0` (19:41; Przekaźnik 44372472836 i Podgląd 44372512634 zielone). Treści (19:44): Web-Studia `a8964db..e7e297e`, Web-Ustawienia `05080a9..fb4bbfc` (`2ea29fc` + `fb4bbfc`), Web-Instytut `88d8f50..013024d`, Web-Nauka `b01f1ec..51626f2`, Web-Popularyzacja `0993e8e..aed9148`; Podgląd 44373000846 zielony. PDF „Mapa CMS” w Web-Podglad `5b4e8f2d..032794f8` `[skip ci]`, 2 strony. Przed pushem: 0 zapisów redaktorów od bazy w 5 repozytoriach; kontrola `po` pokazuje tylko zmiany zlecenia. Na żywo (19:46): Tutornia, kafelek na głównej, podtytuł i link w „W skrócie” na Studiach, 0 błędów konsoli. Jutro (19.11): przegląd zapisów redaktorów z ostatnich 24 h w 5 repozytoriach.
Zmienione pliki: Web-Core: src/lib/grafik.mjs, src/lib/grafikStrony.ts, src/components/grafik/{Plan,Teraz,Kafelek}.astro, src/scripts/grafik.ts, src/styles/grafik.css, src/plugins/{remark-jawne-bloki,rehype-bloki}.mjs, src/plugins/grafik.test.mjs, src/plugins/jawne-bloki.test.mjs, src/views/Strona.astro, src/lib/markdown.ts, src/lib/widoki/{strona,dzialStudia,dzialInstytut,dzialNauka,popularyzacja}.ts, src/components/zal/{DrugiEkran,TrescDzialu}.astro, src/styles/{zal-dzialy,zal-tresc,zalozyciele-strony}.css, src/data/ciekawostki/studia.json, skrypty/sprawdz_tresci.py, package.json, dok/{jawny-markdown,sciagawka-edytora,zasady-parsera}.md, dok/dla-redaktorow/mapa-cms.html; Web-Studia: src/content/strony/studia/{tutornia (nowy),pierwszy-rok,sprawy-studenckie}.md, src/data/studia.md, .pages.yml; Web-Ustawienia: src/data/{nawigacja,skroty}.json, .pages.yml; Web-Instytut, Web-Nauka, Web-Popularyzacja: .pages.yml.
Kryteria odbioru:
- strona, :::grafik, :::pary, ramka „Teraz”, baner, menu, kafelek, „W skrócie” z adresem, ciekawostka, linki, dokumentacja — spełnione;
- oś godzin z grafiku (zmiana 18:33) — spełnione: testy A, luka (9:00 10:00 11:00 12:15 … 17:00 18:00), 10:40–11:20; wariant z luką zbudowany i sfotografowany;
- porównanie HTML przed/po — spełnione z trzema różnicami spoza listy do akceptacji (arkusz .tu-* na 62 Stronach, inna stała ciekawostka bez JS na 10 stronach Studiów, „Następna strona” Pierwszy rok → Tutornia);
- 12 stanów na żywo, zrzuty (Tutornia 5 szerokości jasny/ciemny, główna 4, Studia „Na co dzień”, ramka błędów, bez JS) — spełnione, 0 błędów konsoli;
- astro check 0 błędów, test:jawne 61/61, sprawdz_pola_cms 0, sprawdz_tresci OK, sprawdz-jawny-markdown OK (6 repozytoriów), linki: qa.py 0 zepsutych (lychee niezainstalowany), symulacja formularza: pliki zlecenia bez różnic — spełnione.
Odstępstwa od zlecenia i powody: podtytuł „Na co dzień” zmieniony na „zajęcia, kalendarz, pierwszy rok, tutornia” na prośbę właściciela (mieści się w 1 linii od ok. 1240 px); poprawki znalezione w odbiorze (wąskie kolumny 1024–1280 px, podwójna kreska, ramka błędów, typy w grafik.ts); symulacja TipTap (etap 6a zlecenia 28) nie dotyczy pól `code` Stron studiów — opisane w raporcie, bez zmian w kodzie; linki sprawdzone qa.py zamiast lychee.
Pytania do użytkownika: akceptacja trzech różnic spoza listy; czy napisać redaktorom o polu „Link (opcjonalnie)” i grafiku Tutorni. Szczegóły: RAPORT-ZLECENIE-45.md.

## 47-warto-wiedziec-instytut — 2026-11-18 21:35
Status: zrobione lokalnie, nic nie wypchnięte (czeka na „push” po serii 47–48–46). Web-Core `praca/47-warto-wiedziec` `1e479c91` (od origin/main `3cde30e0`, worktree Web-Core-B); Web-Instytut `ef36a18` (baza `013024d`), Web-Ustawienia `50d5cde` (baza `fb4bbfc`), klony w tresci-B. „Dodano” u Bożejki, Rolskiego i Bilera ustawię w dniu pusha (`warto_wiedziec_47.py --dodano`). Test w CMS z właścicielem po pushu.
Zmienione pliki: Web-Core: src/content.config.ts, src/lib/{wartoWiedziec.ts (nowy), ww.mjs (nowy), wwSkrypty.ts (nowy), markdown.ts, motywyBanerow.ts, patroni.ts, podglad.ts, szkice.ts, tekstyStron.ts, widoki/listaWartoWiedziec.ts, widoki/wartoWiedziecWpis.ts}, src/components/ww/{OsHistorii,RamkiWW,SiatkaSylwetek}.astro (nowe), src/components/{NaglowekStrony,WartoWiedziec}.astro, src/components/zal/{DrugiEkran,NastepnaStrona}.astro, src/views/{SylwetkaWW (nowy),ListaWartoWiedziec,WartoWiedziecWpis}.astro, src/pages/{,en/}instytut/warto-wiedziec/ (nowe), src/pages/{,en/}warto-wiedziec/ (przekierowania), src/pages/sitemap.xml.ts, src/plugins/{remark-jawne-bloki,rehype-bloki}.mjs, src/plugins/ww.test.mjs (nowy), src/styles/{warto-wiedziec (nowy),zalozyciele-strony}.css, skrypty/migracja/{warto_wiedziec_47.py (nowy),formularze_40.mjs}, skrypty/{sprawdz_tresci.py,sprawdz-jawny-markdown.mjs,test-stanu-budowy.mjs,szerokosci/pomiar.cjs,test-edytora/formularz.mjs}, package.json, dok/{sciagawka-edytora,jawny-markdown}.md, dok/dla-redaktorow/mapa-cms.html, dok/en/TLUMACZENIA.md; Web-Instytut: src/content/warto_wiedziec/{sylwetki,nagrody,historie}/ (33 pliki, 4 przeniesione), src/content/strony/instytut/warto-wiedziec.md (przeniesiony), stary wpis o medalach usunięty, src/data/instytut.md, .pages.yml; Web-Ustawienia: src/data/nawigacja.json.
Kryteria odbioru:
- lista, sylwetka, nagroda, historia, :::w-skrocie, :::laureaci, oś czasu, strona główna, „Nowe”, szkice, menu, poprawki (Marczewski 1953–1957, 4 rektorów), EN, dokumentacja — spełnione;
- porównanie HTML przed/po — spełnione: 68 nowych stron, 769 plików tylko z pozycją menu, pozostałe różnice z listy dozwolonych plus „Następna strona” Kontakt → Warto wiedzieć, lista stron w skrypcie ciekawostek i inna stała ciekawostka bez JS na Infrastrukturze informatycznej; .ics i powiadomienia.json tylko znacznik czasu;
- test:jawne 76/76, Playwright (oś i strona główna) 36/36, flaga TYLKO_OPUBLIKOWANE (17 → 11 sylwetek, 6 szkiców poza mapą strony i Pagefind, linki → tekst), zrzuty 112 (jasny/ciemny, 4 szerokości), konsola czysta — spełnione;
- astro check 0 błędów, sprawdz_pola_cms 0 problemów, sprawdz_tresci 1 ostrzeżenie (Rolski „xxxx”, zgodnie ze zleceniem), sprawdz-jawny-markdown OK, linki qa.py 0 zepsutych (lychee niezainstalowany), symulacja formularza (scenariusz 10 a–c OK; 6 znanych różnic obron/grantu ze zlecenia 40) — spełnione;
- CMS z właścicielem, kontrola redaktorów przed pushem i po nim, przegląd 24 h — po pushu.
Odstępstwa od zlecenia i powody: „Dodano” w dniu pusha; poprawki w odbiorze (dotyk na osi — błąd prototypu, etykieta „szkic” w rzędzie strony głównej, grupa „Karta” Historii wymagana, bo Pages CMS nie sprawdza pustej grupy); strona główna EN losuje tylko wpisy z Treścią EN (dziś 3); ulubione ×2,8 w 100 losowaniach przy wadze 3 (losowanie bez powtórzeń); inna stała ciekawostka bez JS po nowej pozycji menu; lychee zastąpiony qa.py. Szczegóły: RAPORT-ZLECENIE-47.md.
Pytania do użytkownika: czy w czterech historiach (Pierwsze wykłady, Nowa Księga Szkocka, Taksonomia wrocławska, Aksjomat determinacji) zamienić pogrubione nazwiska na linki do sylwetek, żeby pokazała się „Ludzie w tej historii”.

## 48-opublikowane-seminaria-referaty-aktualnosci — 2026-11-18 22:06
Status: zrobione lokalnie, nic nie wypchnięte (czeka na „push” po serii 47–48–46). Web-Core `praca/48-opublikowane` `61d6e683` (od gałęzi 47, worktree Web-Core-B); Web-Aktualnosci `9513d48` (baza `abf23d3`), 9 × Web-Sem-* po jednym commicie (bazy w raporcie), klony w tresci-B. Raport: RAPORT-ZLECENIE-48.md. Test w CMS z właścicielem po pushu.
Zmienione pliki: Web-Core: src/lib/{tresci.ts, szkice.ts, podglad.ts, stanBudowy/klient.js}, src/middleware.ts, src/components/zal/StanBudowy.astro, src/views/Seminarium.astro, skrypty/migracja/{formularze_40.mjs, opublikowany_48.py (nowy)}, skrypty/test-edytora/formularz.mjs (scenariusz 11), skrypty/test-stanu-budowy.mjs, dok/sciagawka-edytora.md; Web-Aktualnosci: .pages.yml + 4 aktualności (jawne opublikowany: true); 9 × Web-Sem-*: .pages.yml (identyczna zmiana); .przekazanie/pola-do-cms.md (sekcja 48).
Kryteria odbioru:
- przełącznik w opisie seminarium i Referatach 9 seminariów oraz w Aktualnościach, etykieta z 33, trzy opisy — spełnione (symulacja zapisu 77/77, sprawdz_pola_cms 0 problemów);
- nowe wpisy domyślnie opublikowane, istniejące z jawnym true (Web-Aktualnosci 4 dopisane z 167, Web-Sem 0 z 40), żaden szkic — spełnione;
- Podgląd: etykieta, żółty pasek, wiersz B4 z linkiem do właściwego formularza (aktualność, opis seminarium `…/file/seminarium`, referat na stronie seminarium) — spełnione (test-stanu-budowy 0 problemów, zrzuty 20);
- flaga ukrywa szkice ze wszystkich miejsc z tabeli „Zakres”, referaty seminarium-szkicu razem z nim, liczby po filtrze, powiększona najnowsza opublikowana — spełnione (sprawdz48 0 problemów, liczby: Kariera 11→10, seminaria 9→8, archiwum 31→28, okładka 2→1 nowe);
- filtr w jednym miejscu (aktualnosci()/seminaria()/referaty() w tresci.ts) — spełnione, lista miejsc w raporcie;
- linki w treści do szkiców dają ostrzeżenie — spełnione (5/5 w budowie testowej);
- bez flagi: wynik = wynik 47 co do bajtu (poza znacznikami czasu); ze szkicami tylko etykiety i paski — spełnione;
- astro check 0 błędów, test:jawne 76/76, konsola czysta — spełnione; Core zamrożony, flaga nigdzie nie ustawiona;
- kontrola zapisów redaktorów przed pushem i po nim, przegląd 24 h — po pushu.
Odstępstwa od zlecenia i powody: linki w treści do szkiców z flagą stają się tekstem (zachowanie z 33, Markdown nietknięty, bez 404) mimo „nie usuwaj automatycznie” — pytanie; referaty bez własnych stron, więc wiersz i etykieta na stronie seminarium; referat testowy tylko w lokalnej nakładce (brak przyszłych referatów w danych); schemat bez zmian (pole i filtr były od migracji / zlecenia 33).
Pytania do użytkownika: linki do szkiców z flagą — tekst (jak dziś) czy link do 404 z ostrzeżeniem? Push treści 48 wieczorem czy po wiadomości do redaktorów (także 9 seminariów)?

## 46-zajawka-nie-na-stronie-wpisu — 2026-11-18 22:24
Status: zrobione lokalnie, nic nie wypchnięte (czeka na „push” po serii 47–48–46). Web-Core `praca/46-zajawka` `309dd78c` (od gałęzi 48, worktree Web-Core-B). Repozytoria treści bez zmian. Raport: RAPORT-ZLECENIE-46.md.
Zmienione pliki: Web-Core: src/lib/widoki/aktualnosc.ts (zajawkaNaStronie, siatka bezpieczeństwa), src/views/Aktualnosc.astro (p.wst tylko przy pustej treści, komentarz), dok/sciagawka-edytora.md (zdanie o zajawce w sekcji Aktualności).
Kryteria odbioru:
- strona wpisu (PL i EN, wszystkie rodzaje) bez akapitu zajawki — spełnione (330 stron, po zmianie 0 z p.wst);
- zajawka bez zmian na listach, stronie głównej, w Kalendarzu i w meta description/og:description — spełnione;
- wpis z pustą treścią pokazuje zajawkę — spełnione (kopia testowa PL i EN; w danych dziś 0 takich wpisów);
- porównanie HTML przed (wynik 48) i po: tylko brak p.wst na stronach wpisów + Pagefind + znaczniki czasu — spełnione;
- komentarz w Aktualnosc.astro i ściągawka zgodne; PDF-ów do poprawy brak (Mapa CMS, Czat AI — bez wzmianki o zajawce) — spełnione;
- astro check 0 błędów, test:jawne 76/76, sprawdz_tresci OK (1 ostrzeżenie z 47), zrzuty 13 + 1 „przed”, konsola czysta — spełnione.
Odstępstwa od zlecenia i powody: siatka EN liczy treść, którą strona EN pokazuje (Treść EN z samymi komentarzami też = pusta), dziś bez różnicy; wpis Gdesza nie ma karty (brak zdjęcia i terminu), choć zlecenie tak go opisuje.
Pytania do użytkownika: brak.

## 47-warto-wiedziec-instytut i 48 — decyzje właściciela — 2026-11-18 22:33
Status: odpowiedzi na pytania z raportów 47 i 48; nic nie wypchnięte, seria 47–48–46 dalej czeka na „push”. Web-Core `4e1d4c62` (na szczycie serii), Web-Instytut `b5e9faa` (gałąź 47).
Zmienione pliki: Web-Core: skrypty/migracja/warto_wiedziec_47.py (LINKI_HISTORII); Web-Instytut: historie pierwsze-wyklady, nowa-ksiega-szkocka, taksonomia-wroclawska, aksjomat-determinacji (pogrubione nazwiska → linki do sylwetek).
Kryteria odbioru:
- 47, pytanie 1 (tak): pod czterema historiami „Ludzie w tej historii”; budowa względem wyniku 46 zmienia tylko 20 stron (4 historie i 6 sylwetek, PL i EN) i Pagefind; linki wewnętrzne 0 zepsutych; pełna migracja od bazy daje to samo drzewo (poza kolejnością klucza w .pages.yml) — spełnione;
- 48, pytanie 1: linki w treści do szkiców z flagą zostają jako tekst + ostrzeżenie (jak w 33) — bez zmian;
- 48, pytanie 2: treści 48 idą zaraz po Web-Core, bez czekania na wiadomość do redaktorów — zapisane w raporcie.
Odstępstwa od zlecenia i powody: w Taksonomii linki tylko przy Perkalu i Steinhausie (pozostali autorzy nie mają sylwetek).
Pytania do użytkownika: brak nowych; zlecenie 49 czeka, aż 48 i 46 będą na origin/main.

## 47, 48, 46 — push — 2026-11-18 22:40
Status: wypchnięte po „push” właściciela. Web-Core `3cde30e0..4e1d4c62`; Web-Instytut `013024d..5f68249` (z „Dodano” 2026-11-18); Web-Ustawienia `fb4bbfc..50d5cde`; Web-Aktualnosci `9cf2e52..73569b8` (migracja 48 powtórzona na świeżym main po 5+1 zapisach redaktorów; wpis o nagrodzie Hulanickiego pominięty, bo redaktor nad nim pracował); 9 × Web-Sem-* jednym skryptem, 22:39, wszystkie OK.
Zmienione pliki: jak w wpisach 47, 48, 46 i „decyzje właściciela”.
Kryteria odbioru:
- kontrola zapisów redaktorów tuż przed każdym pushem — zrobiona (Web-Aktualnosci: zapisy zachowane, pole po polu tylko „opublikowany”); po pushu 0 zapisów plików z przełącznikiem;
- test w CMS z właścicielem i przegląd 24 h — do zrobienia.
Odstępstwa od zlecenia i powody: Web-Aktualnosci — wpis Hulanickiego bez jawnego `opublikowany: true` (redaktor go właśnie edytował; brak pola = opublikowane, CMS dopisze przy zapisie).
Pytania do użytkownika: brak.

## 49-seminarium-wydzialowe — 2026-11-18 23:03
Status: zrobione i wypchnięte (push automatyczny po odbiorze, polecenie właściciela). Web-Core `4e1d4c62..5dd156f5`, Web-Aktualnosci `945f2de..a6892d4`, Web-Ustawienia `50d5cde..1fb08e6` (menu „Warto wiedzieć”, decyzja właściciela w trakcie zlecenia). Raport: RAPORT-ZLECENIE-49.md.
Zmienione pliki: Web-Core: src/content.config.ts, src/lib/i18n.ts, src/lib/tresci.ts (jakWydarzenie, rodzajWiersza, rodzajWpisu, opisLang), src/lib/patroni.ts, src/lib/widoki/aktualnosc.ts, src/lib/widoki/listaAktualnosci.ts, src/views/Aktualnosc.astro, src/components/WierszWydarzenia.astro, src/components/zal/DrugiEkran.astro, skrypty/sprawdz_tresci.py, skrypty/migracja/formularze_40.mjs, skrypty/test-edytora/formularz.mjs (scenariusz 12), dok/sciagawka-edytora.md; Web-Aktualnosci: .pages.yml, 2026-11-10-seminarium-wydzialowe-problem-milenijny.md, 2026-06-16-seminarium-wydzialowe.md, 2026-10-17-rusza-tutornia.md; Web-Ustawienia: src/data/nawigacja.json.
Kryteria odbioru:
- formularz: opcja pod „Wydarzenie”, opisy pola i kolekcji, bez nowych pól, YAML się parsuje, sprawdz_pola_cms 0 — spełnione;
- plakietka i filtr „Seminaria wydziałowe” (też ?rodzaj=), mieści się przy 1536/1920/390 — spełnione;
- wpis z terminem jak „Wydarzenie” (Kalendarz pod „Wydarzenia”, podpisy, tytuł wykładu pod prelegentem, .ics, okładka +1, Nauka, kolory) — spełnione na wpisie testowym; bez terminu: ostrzeżenie i brak w Kalendarzu — spełnione;
- porównanie HTML przed/po: 30 plików, wszystkie różnice przy dwóch wpisach, Tutorni i filtrze; sitemap tylko kolejność; liczby w banerach bez zmian — spełnione;
- Tutornia: link PL/EN działa z przedrostkiem Podglądu, bez załącznika, PNG zostaje — spełnione;
- astro check 0 błędów, test:jawne 76/76, sprawdz_tresci OK, symulator formularza (scenariusz 12) OK, konsola czysta, 35 zrzutów — spełnione;
- push z kontrolą zapisów redaktorów: 0 nowych zapisów przed pushem, pole po polu po pushu — spełnione; przegląd 24 h — jutro.
Odstępstwa od zlecenia i powody: dodatkowe pole opisLang (lang="pl" dla polskiej zajawki na /en); jedna funkcja rodzajWiersza dla etykiety i podpisu; komunikat sprawdz_tresci w „…”; zmiana menu „Warto wiedzieć” (grupa „Ludzie”, opis „profesorowie, odkrycia, nagrody”, „Więcej” jak przed 47) na polecenie właściciela.
Pytania do użytkownika: przy seminarium wydziałowym tytuł wykładu jest w zajawce, a 46 ukrywa zajawkę na stronie wpisu — (a) ściągawka: tytuł wykładu także w treści, czy (b) wyjątek od 46 dla tego rodzaju? Mapa-CMS-IM-UWr.pdf: przy następnym generowaniu dopisać „seminaria wydziałowe”.

## 50-aktualnosci-bez-zawieszania — 2026-11-18 23:40
Status: zrobione i wypchnięte (push automatyczny po odbiorze, polecenie właściciela „50 tez z pushem”). Web-Core `5dd156f5..0c07b56e` (fast-forward, bez rebase: origin/main się nie zmienił); Podgląd zbudowany (44413386616, sukces), nowa wersja sprawdzona na opublikowanym Podglądzie. Raport: RAPORT-ZLECENIE-50.md.
Zmienione pliki: Web-Core: src/scripts/zal/czytaj-dalej.ts (czytajDalej w dwóch fazach: odczyty, potem zapisy), src/styles/zal-menu.css (blok komputera: visibility: inherit zamiast visible przy rozwiniętym dziale).
Kryteria odbioru:
- raptowna zmiana szerokości nie zawiesza Aktualności (PL, EN) ani Kariery; tabela przed/po (3 powtórzenia, Edge 157): duże skoki 1,03–1,65 s → 72–103 ms (13,6–18,9×), LayoutCount 124–159 → 7–28 — spełnione; skoki 1076↔768 0,16–0,25 s → 69–87 ms (2,2–3×, tam nie było zawieszenia) — odstępstwo opisane;
- „… czytaj dalej” przy tych samych wpisach: 8 szerokości, wszystkie filtry, szukanie, zmiana szerokości w karcie — 177 porównań, 0 różnic — spełnione;
- zamknięty panel: 0 widocznych linków, Tab po Esc do „← Nauka”, elementFromPoint w miejscu „Seminaria” trafia w baner, klik nie przenosi, bez ducha przy 1536→1000→1076 — spełnione;
- otwarty panel jak dziś: bieżący dział rozwinięty, animacja rozwijania i zwijania klatka w klatkę ta sama, telefon 390 i ciemny panel głównej identyczne bajt w bajt, jasny różni się tylko animowaną strzałką „Szybki dostęp” — spełnione;
- astro check 0 błędów, konsola czysta, zrzuty raport-zrzuty/z50-zrzuty (18) — spełnione;
- zmienione tylko czytaj-dalej.ts i jedna wartość w zal-menu.css — spełnione.
Odstępstwa od zlecenia i powody: baza 5dd156f5 zamiast 3cde30e (46–49 weszły wcześniej, jak przewiduje zlecenie); skoki 1076↔768 tylko 2,2–3× krócej (zostaje zwykłe przeliczenie strony, ślad: 0 przeliczeń z czytaj-dalej); LayoutCount 28 przy skokach do 768 px (14 zwykłych klatek bez skryptu + 4 drobne odczyty PasekMenu/uloz); pierwszy przebieg pomiaru gubił klatki dłuższe niż 1,5 s — powtórzony z poprawionym oknem; push bez czekania na „push” (polecenie właściciela).
Pytania do użytkownika: brak.

## 52-sylwetki-baner-i-tabisz — 2026-11-19 00:50
Status: zrobione i wypchnięte (push automatyczny po odbiorze, polecenie właściciela „Nie stopuj przed push. Automatyczny push po zakończeniu”). Web-Core `0c07b56e..b3ece9f8`, potem Web-Instytut `2328a0d..d6b936d` (fast-forward, bez rebase). Podgląd zbudowany (44423456003, sukces), sylwetki sprawdzone na opublikowanym Podglądzie. Raport: RAPORT-ZLECENIE-52.md.
Zmienione pliki: Web-Core: src/views/SylwetkaWW.astro, src/components/zal/NaglowekZ.astro (znakSam, ZNAK_SAM, DOPASUJ_SAM), src/components/zal/Podstrona.astro, src/components/NaglowekStrony.astro, src/lib/ww.mjs (liczbySylwetki, krotkiTekst, fnv1a), src/lib/wartoWiedziec.ts (liczbyBaneraWW, ostrzeżenia, bez dl.ww2-skrot w treści), src/lib/ciekawostki.ts (znakiDoSkryptu), src/content.config.ts (liczby w ww_sylwetki), src/styles/warto-wiedziec.css, src/styles/zalozyciele.css, src/plugins/ww.test.mjs, skrypty/migracja/formularze_40.mjs, skrypty/migracja/sylwetki_52.py (nowy), skrypty/test-edytora/formularz.mjs (scenariusz 13), dok/sciagawka-edytora.md, dok/jawny-markdown.md, dok/dla-redaktorow/mapa-cms.html, dok/en/TLUMACZENIA.md; Web-Instytut: .pages.yml, 18 plików src/content/warto_wiedziec/sylwetki/*.md.
Kryteria odbioru:
- 18 sylwetek PL i EN: trzy liczby z pola „Liczby”, figurka z puli Instytutu bez opisu, losowana przy wejściu (50 wejść, 0 powtórek; lista → sylwetka bez ciekawostki listy; bez JS stała) — spełnione;
- 18 × 14 szerokości + EN: liczby w rzędzie od 1024, tytuł w jednej linii, bez nachodzenia na figurkę, bez przewijania, konsola czysta; długi tytuł (49 znaków) chowa figurkę przy 1024/1366/1920, bez JS też — spełnione;
- portret opływany wstępem (200/160/110 px), sekcje pod nim, bez „W skrócie”; duży portret bez filtra (Tabisz jasny/ciemny), lista z filtrem — spełnione;
- pole „Liczby” w formularzu, :::w-skrocie usunięty z 17 plików i szablonu, zapas z ostrzeżeniem w kodzie (kopia testowa) — spełnione;
- Tabisz: bez #, ## z {#id}, komentarze, podpis EN bez kropki, liczby; proza bez zmian — spełnione;
- HTML przed/po: zmienione tylko 36 stron sylwetek, CSS tylko reguły sylwetek — spełnione; zrzuty wobec wzorca (37 + 24 zestawienia) — spełnione;
- astro check 0 błędów, test:jawne 78/78, sprawdz_pola_cms 0, sprawdz_tresci i sprawdz-jawny-markdown OK, symulator (scenariusz 13) OK — spełnione;
- ochrona zmian redaktorów: przed pushem 0 zapisów od bazy 2328a0d; po pushu pole po polu „OK, tylko zmiany z migracji” (body 18, liczby 18, podpis_en 1, tresc_en 1) — spełnione; test w CMS z właścicielem i przegląd 24 h — do zrobienia.
Odstępstwa od zlecenia i powody: w .pages.yml cudzysłowy „…” zamiast »…« (styl wszystkich opisów formularzy); etykiety pozycji liczby w stylu „… EN” (jak Warto wiedzieć i Studia); opis Treści „wstęp (obok portretu)”; zapas skraca podpis do 20 znaków całymi słowami z „…”; dodatkowo dok/en/TLUMACZENIA.md; budowa testowa czyści pamięć Astro (fałszywe „Duplicate id”); PDF mapy CMS nie generowany (strona 1 przepełniona już na origin/main).
Pytania do użytkownika: Krzywicki „1962 twierdzenie AKS” — skrótu AKS nie ma w tekście; połączyć z pełną nazwą w zajawce lub wstępie? Tabisz: zdjęcie 240×240 px (miękkie na ekranach 2×), puste „Źródło zdjęcia”, brak sekcji „Źródła” — uzupełnić?

## Start pracy samodzielnej (zlecenia 53 → 54 → 55 → 42) — 2026-11-19 11:15
Status: polecenie właściciela z 19.11 rano: praca bez właściciela do wieczora, push bez czekania na „push” po spełnieniu warunków (budowa PL i EN, testy i kontrole zielone, porównanie HTML wyjaśnione; fetch, rebase i budowa tuż przed pushem; pełna „Ochrona zmian redaktorów”; cisza 20 min od ostatniego zapisu redaktora). Zlecenia 51 nie wykonuję (zastąpione przez 53).
Zastane: żadne z 53, 54, 55, 42 nie było zaczęte (dziennik kończy się na 52 z 00:50; brak RAPORT-ZLECENIE-53/54/55/42; gałęzie lokalne bez tych numerów; Web-Core-B czysty na b3ece9f8 = origin/main; stash: 3 stare wpisy z 29.10–17.11, bez związku). Pracuję w folderze Web-Core (gałęzie praca/NN-…); Web-Core-B i tresci-B nietknięte. Nowe klony treści: ..\tresci-C (wszystkie repozytoria z tresci.json + Web-Podglad, main z GitHuba). Nakładka Web-Core przed pierwszą budową zapisana w tresci-C\nakladka-web-core-przed-19-11.tar; budowy przez pobierz_tresci.py --lokalnie ..\tresci-C (tresci-C\budowa.sh), jak w 47–52.

## 53-autokorekta-naglowkow-zobacz-tez-sylwetki-opublikowane — 2026-11-19 11:45
Status: zrobione i wypchnięte (push samodzielny po spełnieniu warunków). Web-Core `b3ece9f8..9c45eb80` (11:36), Web-Instytut `d6b936d..645a832` (11:37). Podgląd 44507399240 — sukces, sprawdzony na żywo. Raport: RAPORT-ZLECENIE-53.md.
Zmienione pliki: Web-Core: src/plugins/remark-jawne-bloki.mjs (poprawNaglowkiWW, {#id} bez spacji i przy każdym poziomie), src/lib/wartoWiedziec.ts (ww.tytul, ostrzeżenie), src/views/SylwetkaWW.astro („Zobacz też”), src/components/WartoWiedziec.astro, src/lib/widoki/wartoWiedziecWpis.ts (komentarze), src/plugins/ww.test.mjs, src/plugins/jawne-bloki.test.mjs, skrypty/migracja/sylwetki_53.py (nowy), dok/sciagawka-edytora.md, dok/jawny-markdown.md, dok/en/TLUMACZENIA.md; Web-Instytut: 6 sylwetek (opublikowany: true), u Bożejki i Rolskiego bez „Do pobrania”.
Kryteria odbioru:
- wpis testowy w stylu Tabisza sprzed 52 (PL i EN): jeden h1, wstęp, 3 sekcje z kreskami, spis, bez {#…} — spełnione (zrzuty 1920/1366/390, jasny/ciemny);
- prawdziwe wpisy WW bez zmian w HTML poza „Zobacz też” — spełnione (20 plików: 10 sylwetek PL i EN, tylko nagłówek, spis i id);
- {#id} bez spacji i przy każdym poziomie — spełnione (testy); w treściach dziś 0 takich nagłówków;
- ostrzeżenie w logu przy poprawce — spełnione (PL i „(Treść EN)” przy wpisie testowym, 0 przy innych);
- „Zobacz też” / „See also” w nagłówku i spisie — spełnione;
- testy 84/84, dokumentacja i TLUMACZENIA.md — spełnione;
- Bożejko i Rolski bez „Do pobrania”, „Źródła” i PDF bez zmian — spełnione;
- 18 sylwetek opublikowanych, widocznych w budowie publicznej; w Web-Instytut tylko opisane linie, kontrola przed (0 zapisów od bazy) i po pushu (pola opublikowany 6, body 2) — spełnione.
Odstępstwa od zlecenia i powody: baner listy w budowie publicznej „18 sylwetek”, nie „17” (żadna sylwetka nie jest już TBA); push bez „push” właściciela (polecenie z 19.11).
Pytania do użytkownika: zasada „osoba żyjąca = szkic” w opisie kolekcji i ściągawce — zostaje czy zmienić (szczegóły w raporcie)? Inne kolekcje z jawnym Markdownem: 0 plików z Treścią bez ## — rozszerzenie reguły nic by dziś nie zmieniło.

## 54-warto-wiedziec-styl-i-zrodla, część A i B — 2026-11-19 12:05
Status: obie części zrobione i wypchnięte (push samodzielny po spełnieniu warunków). A: Web-Instytut `645a832..a255edb` (11:46), Web-Core `9c45eb80..f12aeb15` (11:47, tylko dok/). B: Web-Core `f12aeb15..6193ddfd` (11:57), Web-Aktualnosci `eee693e..d9e2f3e` (11:57). Podgląd 44508857543 (po A) i 44510538471 (po B) — sukces, sprawdzone na żywo. Raport: RAPORT-ZLECENIE-54.md.
Zmienione pliki: A — Web-Instytut: 32 pliki WW skryptem `.przekazanie\zlecenia\zlecenie54.py` (zapisany bez zmian; 87 zamian, 2 sekcje „Źródła”), `.pages.yml` (6 zdań „Styl: …” w opisach Treści); Web-Core: dok/sciagawka-edytora.md, dok/jawny-markdown.md. B — Web-Core: cofnięty a5779a75 (content.config.ts z preprocess starej wartości, i18n.ts, tresci.ts, patroni.ts, aktualnosc.ts, listaAktualnosci.ts, Aktualnosc.astro, WierszWydarzenia.astro, DrugiEkran.astro), sprawdz_tresci.py (ostrzeżenie o starym rodzaju), formularze_40.mjs (opis kolekcji), test-edytora/formularz.mjs (scenariusz 12), dok/sciagawka-edytora.md; Web-Aktualnosci: .pages.yml (3 miejsca), tytuły 2 wpisów o seminarium.
Kryteria odbioru:
- A: 18 sylwetek od „Prof.”/„Dr”, dalej bez tytułu; Tabisz bez myślnika, lat i pogrubień, zajawki bez nazwiska; pogrubienia 88 (72 hasła w 15 sylwetkach, 16 lat w 4 nagrodach); Bożejko 38 i Rolski 26 źródeł, Rolski „ur. 1946”; 7 linków wewnętrznych działa (0 martwych na stronach WW) — spełnione;
- A: HTML przed/po — 57 plików: strony WW (tekst, zdjęte pogrubienia, linki) i kolejność karty Rolskiego (rok urodzenia), na stronie głównej tylko ukryta karta w puli — wyjaśnione; link Tabisz → Krzywicki nie dodał powiązania — spełnione;
- A: ściągawka, jawny-markdown.md, opisy pól — spełnione; astro check 0 błędów, test:jawne 84/84, sprawdz_tresci 0 ostrzeżeń, sprawdz-jawny-markdown OK, konsola 0 — spełnione;
- A: ochrona zmian redaktorów — 0 zapisów od bazy, skrypt na świeżym main daje identyczne 32 pliki, kontrola przed OK, po pushu tylko pola z tabeli — spełnione;
- B: formularz z 4 opcjami, opisy jak przed 49 (symulator scenariusz 12: 5/5), sprawdz_pola_cms 0 — spełnione; po pushu właściciel otwiera formularz Aktualności w CMS — do zrobienia;
- B: brak plakietki, filtra i podpisu seminarium; HTML przed/po — 28 plików, tylko tytuły dwóch wpisów — spełnione;
- B: wpis testowy ze starym rodzajem: budowa OK, Kalendarz „Wydarzenie”, ostrzeżenie — spełnione; ?rodzaj=seminarium-wydzialowe pokazuje wszystkie wpisy — spełnione;
- B: tytuły w jednolitej pisowni, ściągawka, „Rusza tutornia” bez zmian, zapisy redaktorów zachowane (kontrola przed i po: tylko tytul/tytul_en z tabeli) — spełnione.
Odstępstwa od zlecenia i powody: push bez „push” właściciela i bez wiadomości do redaktorów (polecenie z 19.11, cisza sprawdzona); scenariusz 12 napisany od nowa zamiast cofania 5dd156f5 (konflikt z późniejszym scenariuszem 13).
Pytania do użytkownika: pilnowanie stylu (ostrzeżenia czy automatyczne zdejmowanie pogrubień — rekomendacja: ostrzeżenia); zajawka pod tytułem 8 wierszy wydarzeń w Kalendarzu — pokazywać?; dopisać zdania „Styl: …” do generatora formularze_40.mjs przy następnej okazji?

## 55-portrety-sylwetek — 2026-11-19 12:55
Status: zrobione i wypchnięte (push samodzielny po spełnieniu warunków). Web-Core `6193ddfd..67ac130f` (12:36), Web-Instytut `a255edb..e88a088` (12:38), Web-Ustawienia `1fb08e6..fd49210` (12:40). Podgląd 44516354462, 44516690637, 44517040880 — sukces, sprawdzone na żywo. Raport: RAPORT-ZLECENIE-55.md, arkusz raport-zrzuty/z55-wybor.html.
Zmienione pliki: Web-Core — src/views/SylwetkaWW.astro (zdejmowanie „Fot./Fot:/Foto:/Photo:/Photo” z początku „Źródła zdjęcia”), skrypty/migracja/formularze_40.mjs (opisy pól Zdjęcie i Źródło zdjęcia), dok/sciagawka-edytora.md (zdanie o portrecie); Web-Instytut — 16 plików public/pliki/warto-wiedziec/portrety/<slug>.jpg (600×750), w 16 sylwetkach tylko linie obraz i obraz_zrodlo w „karta” (Tabisz: obraz_zrodlo dopisana), .pages.yml (2 opisy); Web-Ustawienia — o-stronie.md (śródtytuł {#portrety}, zdanie, 16 linii PL i EN). Pliki robocze poza repozytoriami: .przekazanie\robocze\55-portrety\ (oryginały, zrodla.json, kadry.json, portrety.py, zrodla.py, podlacz.py, arkusz.py).
Kryteria odbioru:
- portret 600×750 dla 16 osób z użytecznym źródłem; równy kadr tam, gdzie źródło pozwala (oczy 36–38%, głowa 48–54%), ciasne źródła (Perkal, Hartman, Ślebodziński, Krzywicki, Tabisz, Rolski, Knaster) z większą głową bez dorabiania tła — spełnione z odnotowanymi wyjątkami;
- wybór i obróbka w arkuszu z55-wybor.html, wynik odtwarzalny z oryginałów (portrety.py, kadry.json) — spełnione;
- bez naprawy twarzy, usuwania znaków wodnych i koloryzowania — spełnione;
- w sylwetkach tylko karta.obraz i karta.obraz_zrodlo, kontrola przed (0 zapisów od bazy) i po pushu (linia po linii OK; kontrola_redaktorow: pole karta w 16 plikach, 16 JPG) — spełnione;
- jeden „Fot.”/„Photo:” (0 „Fot. Fot.” w dist), opisy pól zgodne w CMS i generatorze, ściągawka — spełnione;
- „O stronie” PL i EN ze źródłem, licencją i zmianami, bez wypełniaczy, linki 200 — spełnione;
- lista „zgody przed startem” w raporcie — spełnione.
- astro check 0 błędów, test:jawne 84/84, sprawdz_tresci OK, sprawdz_pola_cms 0, sprawdz-jawny-markdown OK (Instytut, Ustawienia), konsola 0; HTML przed/po — 56 plików w dozwolonych miejscach + 16 nieużywanych kopii w _astro/ (zgłoszone w raporcie).
Odstępstwa od zlecenia i powody: Wikimedia zwracała HTTP 429 (oryginały, potem też miniatury) — Steinhaus z miniatury Commons 1280 px, warianty 2a, 4a, 11, 13a, 14a przez thumb.php w szerokości oryginału (sha256 inne niż oryginału); wariant B (Real-ESRGAN) pominięty — wymagałby pobrania i uruchomienia zewnętrznego programu bez potwierdzenia właściciela; push bez „push” właściciela i bez wiadomości do redaktorów (polecenie z 19.11, cisza sprawdzona).
Pytania do użytkownika: Ślebodziński 4a (1938, domena publiczna według Commons) zamiast 4b — zostaje?; Hulanicki z powiększeniem ×3,57 („słaba jakość”) — zostaje czy portret zastępczy do czasu większego pliku?; wysłać pismo do Archiwum UWr (tekst w raporcie)?

## 42-osoby-z-listy-pracownikow — 2026-11-19 14:25
Status: zrobione i wypchnięte (push samodzielny po spełnieniu warunków). Web-Core `67ac130f..608d6337` (13:46), potem treści: Web-Pracownicy `ff4aec1..19c92b2` (13:49), Web-Instytut `e88a088..d14657e` (13:51), Web-Nauka `51626f2..2db3479` (13:54), Web-Sem-Analiza-Harmoniczna `e25b641..f3cbe4a`, Web-Sem-Dydaktyka `b3d6e7f..7d0c6db`, Web-Sem-Dyskretna-Analiza-Harmoniczna `81716a7..4b9f116`, Web-Sem-Geometria `1700d8a..0787017`, Web-Sem-Prawdopodobienstwo `15169e5..c94a533`, Web-Sem-Rownania-Rozniczkowe `ba24c65..ac693ee`, Web-Sem-Statystyka `699c086..4a5d5d3`, Web-Sem-Teoria-Modeli `5a96f65..e1c73b9`, Web-Sem-Topologia `1cf30da..75558dc` (13:56–14:13), Web-Studia `e7e297e..608f1dc` (14:16). Podgląd po każdym pushu: 13 przebiegów sukces, 1 anulowany przez kolejkę (objęty następnym), 0 ostrzeżeń o osobach. Raport: RAPORT-ZLECENIE-42.md, zrzuty raport-zrzuty/z42-*.
Zastane: 42 niezaczęte; etap 0 na świeżym main zgodny z przeglądem z 18.11 co do sztuki (pewne 115, niejednoznaczne 0, spoza spisu 14 + 5) — bez STOP.
Zmienione pliki: Web-Core — src/content.config.ts, src/lib/osobySpisu.ts (nowy), src/lib/brakiOsob.ts (nowy), src/components/BrakOsoby.astro (nowy), src/components/zal/{StanBudowy,OsobaZ,WladzeZ}.astro, src/middleware.ts, src/lib/{tresci,podglad}.ts, src/lib/widoki/{grant,listaGrantow,zaklad,listaZakladow,seminarium,listaSeminariow,specjalnosc,kierunek,wladze,pracownicy}.ts, src/views/{Grant,DzialNauka,Zaklad,ListaZakladow,Seminarium,ListaSeminariow,Specjalnosc}.astro, skrypty/migracja/osoby_42.py (nowy), skrypty/migracja/formularze_40.mjs, skrypty/synchronizuj-katalog-pracownikow.mjs (nowy, zastępuje synchronizuj-katalog-opiekunow.mjs), skrypty/sprawdz_tresci.py, skrypty/test-edytora/formularz.mjs (scenariusz 14), dok/sciagawka-edytora.md, dok/jawny-markdown.md; treści — pola osób według migracji, .pages.yml, katalog _cms/pracownicy (12 repozytoriów), Web-Pracownicy .github/workflows/katalog-pracownikow.yml (wyłączony zmienną do czasu kluczy), Web-Studia README-jawny-markdown.md (zdanie). Lokalnie: .przekazanie\pola-do-cms.md (sekcja „Zlecenie 42”), tresci-C\z42-*.{sh,py,txt}, tresci-C\przeglad-24h.sh.
Kryteria odbioru:
- wybór ze spisu w polach „wybór”, spoza spisu ręcznie, pola tekstowe bez zmian, lista aktualizowana skryptem (automat gotowy, czeka na klucze) — spełnione;
- osoba, która odeszła: znika ze spisu, historia jako tekst bez linku, funkcja — znacznik na Podglądzie, brak wiersza na stronie publicznej (test lokalny, cofnięty; zrzuty) — spełnione;
- usuwanie osób w CMS wyłączone, katalog nie kasuje osób z odwołaniami — spełnione;
- migracja: 115 do spisu, 19 spoza, 128 × pracuje: true; HTML: nowy Core + stare treści = 0 różnic (publiczna i Podgląd), po migracji 24 pliki (nazwiska kierowników grantów ze spisu na listach zakładów i Nauki, kolejność koordynatorów AH i Topologii) — spełnione, różnice wyjaśnione w raporcie;
- astro check 0 błędów, test:jawne 84/84, sprawdz_tresci OK, sprawdz_pola_cms 0 (2160 plików), symulator scenariusz 14 OK — spełnione;
- ochrona zmian redaktorów: 0 zapisów od bazy w 13 repozytoriach, cisza spełniona, kontrola pole po polu przed i po pushu OK 13/13 — spełnione; przegląd 24 h po pushu — do zrobienia 20.11 (skrypt tresci-C\przeglad-24h.sh).
Odstępstwa od zlecenia i powody: push bez „push” właściciela i bez wiadomości do redaktorów (polecenie z 19.11, cisza sprawdzona); byli pracownicy na liście wyboru z dopiskiem, nie na końcu (Pages CMS nie ma sortowania); w Web-Studia kontrola po pushu powtórzona po poprawce narzędzia (błąd Windows „Filename too long” przy git show, odczyt przez git cat-file — wynik OK).
Pytania do użytkownika: które osoby odznaczyć jako byłych pracowników (23 emerytów w raporcie; odznaczenie usuwa też z grupy „Emeryci”)?; klucze automatu — kroki w raporcie i podsumowaniu; kolumna „ze spisu” w widoku listy CMS — zostaje?

## 56-bloki-w-tekscie-stron-dzialow — 2026-11-20 22:45
Status: zrobione i wypchnięte na „push” właściciela (20.11, 22:37): Web-Core `608d6337..7dfc959c` (fast-forward, main bez nowych zmian od startu; gałąź praca/56-bloki tylko lokalnie). Przekaźnik do Web-Podglad 44821889208 uruchomiony; wynik budowy Podglądu niesprawdzony. Odbiór lżejszy według decyzji właściciela z 22:26 (bez porównań pikselowych). Raport: RAPORT-ZLECENIE-56.md, zrzuty raport-zrzuty/z56-zrzuty/.
Zmienione pliki: src/components/zal/TrescDzialu.astro (otoczka div.tresc.z-dz-proza > div.prose, import tresc-zakladki), src/styles/zal-dzialy.css (akapity i linki w akapitach jak przed otoczką, reguły .z-dz dla h2/h3, a, ul poza otoczką, „O …” jako .z-dz-tresc > div > h2), src/lib/tekstyStron.ts (wstPierwszemu: wst tylko dla akapitu na najwyższym poziomie), src/lib/widoki/popularyzacja.ts (to samo). Lokalnie: raport-zrzuty/z56-skrypt/ (nakładka testowa i skrypty kontroli), tresci-C/z56-*.
Kryteria odbioru:
- /popularyzacja: kafelki i lista linków Piotra jak „Obozy” na /popularyzacja/uczniowie — spełnione (style obliczone 0 różnic przy 1920/1440/390, jasny i ciemny; zrzuty z56-obok-1440/390);
- każdy blok z punktu 1 działa w tekście działu, zakładki się przełączają — spełnione (próbka 12 bloków + ##, ###, listy, cytat, tabela w nakładce studia.md PL i EN: style 143 elementów równe podstronie wzorcowej; zakładki kliknięcie/strzałki/Home, pytania; zrzuty z56-bloki-1440/390);
- /instytut, /studia, /nauka: HTML różni się tylko otoczką i skryptem zakładek — spełnione (cały dist: 8 stron działów PL i EN, poza tym CSS, nowy JS, znaczniki czasu); zrzuty pikselowe zdjęte z odbioru decyzją z 22:26;
- akapity, p.wst, linki w akapitach, „O …”, „W skrócie”, sekcje pod tekstem bez zmian — spełnione (style obliczone przed/po: 32 warianty, 0 różnic, także najechanie);
- repozytoria treści bez zmian, w Web-Core tylko pliki kodu — spełnione (nakładka przywrócona pobierz_tresci.py, git status: 4 pliki kodu);
- astro check 0 błędów, testy wtyczek 84/84 — spełnione; sprawdz_tresci.py OK (594 pliki, 106 ciekawostek, 0 ostrzeżeń) — spełnione, po doinstalowaniu PyYAML 6.0.3 (pip --user) za zgodą właściciela.
Odstępstwa od zlecenia i powody: brak porównań pikselowych (decyzja właściciela 22:26); funkcja wst działa też w stronaListy (strony z listą) — dziś nie zmienia tam żadnego pliku.
Pytania do użytkownika: komentarz z migracji na górze Treści Piotra — redaktor może go usunąć?; kreska listy przed pozycjami :::pliki (także na podstronach) — poprawić osobnym zleceniem?

## 57-obrony-lista-wedlug-lat — 2026-11-22 14:35
Status: zrobione i wypchnięte (polecenie właściciela z 22.11: „po zakończeniu automatyczny push”). Web-Core `edbd51de..03a684ad` (14:33, fast-forward, main bez nowych zmian od startu; gałąź praca/57-obrony-lata tylko lokalnie). Przekaźnik do Web-Podglad 45028141727 uruchomiony; wynik budowy Podglądu niesprawdzony. Raport: RAPORT-ZLECENIE-57.md, zrzuty raport-zrzuty/z57-zrzuty/, narzędzia raport-zrzuty/z57-skrypt/.
Zmienione pliki: src/views/ListaObron.astro (układ jak Konferencje: spis, tekst jako pierwsza sekcja z p.wst, sekcje Nadchodzące/Odbyte, lata h3#rok-RRRR z liczbą w odmianie, skrypt ?rok; bez panelu „Pokaż”, szukania, napisu „Brak obron…” i linku do archiwum), src/lib/widoki/listaObron.ts (lata: { rok, lista }[], wst), src/components/WierszWydarzenia.astro (poziom 'h4'), src/lib/i18n.ts (usunięte nadchodzaceObrony, odbyteObrony, archiwumObron; archiwum i ustawienia.archiwum zostają — 404, Aktualności).
Kryteria odbioru:
- spis „Na tej stronie”: Nadchodzące, 2026…2013 (15 pozycji, lata z danych), bez panelu „Pokaż” i szukania — spełnione (HTML PL i EN);
- odbyte według lat, h3#rok-RRRR z liczbą w odmianie PL (8 obron, 4 obrony, 1 obrona…) i EN (1 defence / 8 defences), lata od najnowszego, w roku od najnowszej — spełnione (52 wiersze, 14 lat);
- Nadchodzące na górze od najbliższej, pusta sekcja z napisem PL/EN — spełnione (3 testowe obrony w nakładce, potem nakładka przywrócona pobierz_tresci.py, 52 obrony);
- brak linku „Archiwum starej strony” — spełnione;
- wiersze jak przed zmianą, z linią promotora — spełnione: getComputedStyle 10 elementów każdego wiersza, PL i EN, 1920/1440/1024/390, jasny i ciemny, z „ogranicz ruch” i bez: 0 różnic w dacie, etykiecie, kandydacie (h4/h3), linku, tytule i promotorze; różni się tylko dziedziczony stopień samego article (bez własnego tekstu); najechanie ten sam kolor;
- ?rok=RRRR prowadzi do roku — spełnione: ?rok=2015 → #rok-2015 (nagłówek na scroll-margin-top), ?rok=1999 i ?rok=abc → góra, ?rok znika z adresu (PL/EN, 1440/390); bez JS cała lista;
- spis myszą i klawiaturą, znacznik podąża za kółkiem — spełnione (1440: 15/15; 1920: 14/15 — klik w 2013, gdy strona już na dole, nie przesuwa znacznika; tak samo dziś w Konferencjach, wspólny SpisStrony — uwaga w raporcie);
- inne strony bez zmian — spełnione: cały dist przed/po różni się tylko /obrony-doktorskie PL i EN, usuniętym skryptem filtra, DTSTAMP w 154 .ics i czasem w powiadomienia.json; Kalendarz i wpisy Aktualności bajt w bajt; sitemap.xml identyczny; Pagefind 463/463 stron, 11 zapytań z tymi samymi wynikami;
- repozytoria treści bez zmian — spełnione;
- astro check 0 błędów i ostrzeżeń (8 dawnych podpowiedzi w innych plikach), sprawdz_tresci.py OK (641 plików), test:jawne 84/84, konsola 0 błędów — spełnione;
- zrzuty 1920/1440/1024/390, jasny i ciemny, góra / Nadchodzące (pusta i z testowymi) / 2026–2025 / koniec (2013), obok Konferencje — spełnione (z57-obok-*, z57-test-obok-*).
Odstępstwa od zlecenia i powody: kreska pod rokiem i h2 bez dolnego marginesu jak w zaakceptowanym prototypie (krój, stopień, kolor roku i liczby jak w Konferencjach); wiersze Nadchodzących mają h3 (pod h2, bez roku), pod rokiem h4; zerowanie przejścia koloru i odsunięcia podkreślenia z .tresc a na linku wiersza, żeby wiersz zachowywał się jak dawniej; skrypt ?rok przewija jak spis (scroll-margin-top), a kotwicę dopisuje po load, bo przeglądarka sama przewijała do kotwicy z podwójnym odstępem; push bez słowa „push” — polecenie właściciela z 22.11.
Pytania do użytkownika: poprawić w SpisStrony.astro znacznik przy kliknięciu ostatniej pozycji, gdy strona jest już na dole (jedna linia, wszystkie podstrony ze spisem)?; tytuły rozpraw zawsze lang="en" (ok. 33–34 po polsku) i „(promotor pomocniczy)” po polsku na EN — osobne zlecenie?

## poza-zleceniem-promotorzy-pomocniczy — 2026-11-22 15:05
Status: zrobione i wypchnięte (polecenie właściciela 22.11 w czacie: „Wywal z obron, promotorów pomocniczych … nie z CMS tylko z wyświetlania na stronie”, „Ważne i priorytetowe”; push potwierdzony przez właściciela). Web-Core `03a684ad..c8e6497b` (15:03); gałąź praca/promotorzy-pomocniczy tylko lokalnie.
Zmienione pliki: src/lib/tresci.ts (nowy filtr promotorzyNaStronie — bez wpisów z dopiskiem „(promotor pomocniczy)”), src/views/ListaObron.astro (linia promotora w wierszu), src/views/Obrona.astro (para Promotor/Supervisor), src/lib/widoki/obrona.ts (zdanie „Supervisor(s): …” w zaproszeniu EN złożonym z danych).
Kryteria odbioru:
- promotor pomocniczy niewidoczny na stronie, w CMS bez zmian — spełnione: 9 obron (Garncarek, Jagiełła, Cygan, Marcinkowski, Kołodziejska, Danielski, Żuchowski, Tadej, Mrowińska); dist przed/po różni się tylko 9 stronami obron i listą obron (PL i EN), indeksem wyszukiwarki i znacznikami czasu; „Promotorzy:” → „Promotor:”, „Supervisors:” → „Supervisor:”, gdy został jeden; kopromotor (Ghardallou) zostaje;
- astro check 0 błędów i ostrzeżeń — spełnione.
Odstępstwa od zlecenia i powody: brak.
Pytania do użytkownika: czy „(kopromotor)” też ukryć?

## 58-skrot-nazwy-wydzialu-w-pasku — 2026-11-22 15:15
Status: zrobione i wypchnięte (polecenie właściciela z 22.11: „I po 58 też automatyczny push”). Web-Core `c8e6497b..184ef501` (15:08, fast-forward, main bez nowych zmian od startu). Przekaźnik do Web-Podglad 45031185106 uruchomiony; wynik budowy Podglądu niesprawdzony. Gałąź praca/58-pasek-skrot tylko lokalnie. Raport: RAPORT-ZLECENIE-58.md, zrzuty raport-zrzuty/z58-zrzuty/, narzędzia raport-zrzuty/z58-skrypt/.
Zmienione pliki: src/lib/i18n.ts (wydzialKrotko: EN „Faculty of Math. & Comp. Science”, PL = wydzial), src/components/Naglowek.astro (.brand-sub: gdy skrót różny od pełnej nazwy, .bs-pelna i .bs-krotka z aria-hidden; PL sam tekst), src/styles/global.css (.bs-krotka domyślnie schowany), src/styles/zal-telefon.css (usunięta reguła „do 500 px” dla strony głównej EN, nowa reguła 421–519 px: pełna nazwa jako sr-only, skrót widoczny; komentarz z progiem).
Kryteria odbioru:
- EN 421–519 px: skrót w jednej linii przed flagą na każdej stronie z paskiem, także na stronie głównej po okładce — spełnione (pomiar co 1 px 360–1023 na 5 stronach EN: zakresy brak / skrót / pełna nazwa; arkusze z58-pasek-*);
- EN od 520 px pełna nazwa, do 420 px bez linii — spełnione;
- PL bez zmian — spełnione (HTML wszystkich stron PL identyczny poza nazwą pliku CSS; pomiar przed = po; arkusze PL);
- czytnik ekranu czyta pełną nazwę bez skrótu — spełnione (ariaSnapshot i getByRole przy 430, 519, 520, 600 px: „Mathematical Institute Faculty of Mathematics and Computer Science”);
- bez zmian komputer, okładka, menu, stopka, telefon w poziomie — spełnione (HTML EN różni się tylko .brand-sub na 469 stronach; piksele: pasek komputera 1280/1920 na 3 stronach 11×0 i 1×1 piksel szumu 1/255, okładka 390/430 PL i EN 8×0, poziomo 844×390 2×0);
- druga linia nigdy pod przyciskami 360–1023 — spełnione w EN (najmniej 4,9 px przy 421; przed: −70,7 px); PL jak dotąd 3,8 px przy 421 (Edge; zlecenie podaje 4 z Chrome w chmurze); bez przewijania w poziomie;
- astro check 0 błędów i ostrzeżeń, konsola 0 błędów — spełnione.
Odstępstwa od zlecenia i powody: domyślne ukrycie skrótu w global.css przy .brand-sub (skrót schowany wszędzie poza zakresem telefonu), reguły z progiem w zal-telefon.css; push bez słowa „push” — polecenie właściciela z 22.11.
Pytania do użytkownika: brak.

## 59-wersja-angielska-uzupelnienie — 2026-11-22 15:38
Status: zrobione i wypchnięte (polecenie właściciela z 22.11: „I potem 59 i po 59 też automatyczny push”). Web-Core `184ef501..9dc6ca58` (15:35:50), Web-Instytut `d14657e..e71567f`, Web-Studia `608f1dc..7d4a2f7`, Web-Popularyzacja `faf8ca1..e959453`, Web-Ustawienia `fd49210..3a318aa`, Web-Aktualnosci `e493493..848cb3e`, Web-Nauka `2db3479..8266198` (15:36:01–15:36:20); wszystkie fast-forward, przed pushem 0 nowych commitów redaktorów od bazy, kontrola po pushu pole po polu OK (z59-kontrola.py). Akcje: Web-Core push 45033685817 i 6 przekaźników do Web-Podglad (45033719064…45033741982) — success; budowa Podglądu 45033762571 — success (15:38). Gałęzie praca/59-wersja-angielska tylko lokalnie. Raport: RAPORT-ZLECENIE-59.md, zrzuty raport-zrzuty/z59-zrzuty/ (92 pliki przed | po), wynik raport-zrzuty/z59-wynik.json, narzędzia raport-zrzuty/z59-skrypt/ i tresci-C/z59-*.py.
Zmienione pliki: Web-Core — łatka EN (16 plików: dok/en/TLUMACZENIA.md, content.config.ts z polami galeria[].podpis_en, tresc_en konferencji, obraz_zrodlo_en sylwetek; WierszWydarzenia, DrugiEkran, en/publikacje.ts, osoby.ts, tresci.ts, wartoWiedziec.ts, widoki/konferencja.ts, widoki/obrona.ts, Aktualnosc.astro, AktualnoscZamianaDni.astro, Konferencja.astro, Obrona.astro, RokAkademicki.astro, SylwetkaWW.astro), punkt 4 (wartoWiedziec.ts portretHtml z lang: „Photo” na /en; SiatkaSylwetek, SylwetkaWW, WartoWiedziecWpis), poprawki PL 4 i 24–26 (ciekawostki/studia.json, DrugiEkran odmiana „referat/referaty/referatów”, Obrona.astro „Promotorzy”, langRozprawy w i18n.ts dla Obrona.astro i WierszWydarzenia.astro), bez importu ODBIORCY w Aktualnosc.astro. Repozytoria treści: łatki EN (Web-Instytut 47 plików z .pages.yml, Web-Studia 24, Web-Popularyzacja 5, Web-Ustawienia 5, Web-Aktualnosci 26 z .pages.yml, Web-Nauka 20 z .pages.yml), poprawki PL z punktu 6A (Web-Instytut, Web-Studia, Web-Popularyzacja, Web-Aktualnosci, Web-Nauka; lista „było → jest” w raporcie), {#dane-bibliograficzne} w EN artykułu o Annals (Web-Instytut). .przekazanie/pola-do-cms.md: sekcja „Zlecenie 59” (3 nowe pola).
Kryteria odbioru:
- 7 łatek nałożonych; konflikt tylko Obrona.astro (z wcześniejszą dziś zmianą bez promotorów pomocniczych) — rozwiązany, opis w raporcie; zmiany redaktorów od bazy-sha tylko w Web-Aktualnosci (3 obrony + 1 commit Claude), bez wspólnych plików z łatką — spełnione;
- łatki zmieniają tylko pola _en/tresc_en i .pages.yml (skrypt z59-tylko-en.py: 0 problemów w 6 repozytoriach) — spełnione;
- astro check 0 błędów (0 ostrzeżeń), test:jawne 84/84 — spełnione;
- sprawdz_tresci.py OK poza 3 znanymi błędami obrazów WW; sprawdz_pola_cms.py 0 problemów; sprawdz-jawny-markdown.mjs OK (Web-Studia, Web-Instytut, Web-Ustawienia) — spełnione;
- HTML PL przed/po: po łatkach 477/477 identyczne bajt w bajt; po poprawkach PL różnice tylko z punktu 6A (234 strony, 40 grup, lista w raporcie) — spełnione;
- poprawki 6A (1–33) zrobione, lista plik / było → jest w raporcie — spełnione;
- zrzuty 390 i 1920 px przykładów z /en (strona główna, MISIU, obrony, konferencje, WW, Popularyzacja, Matematyka, Rok akademicki) — spełnione;
- wspólne {#id}: spis „Na tej stronie” różny PL/EN na 2 stronach z 88 (przed: 40); Annals poprawione, Rok akademicki ma id w kodzie — pytanie niżej; przełącznik języka nie przenosi #kotwicy — częściowo;
- formularze CMS: YAML poprawny, nowe pola pod polskimi odpowiednikami — spełnione.
Odstępstwa od zlecenia i powody: Obrona.astro — „(auxiliary supervisor)” nie pokazuje się, bo decyzja właściciela z 22.11 ukrywa promotorów pomocniczych; Web-Aktualnosci nałożone na e493493 (bazy-sha 5ed05d3 + 3 zmiany redaktora w obronach); przecinek przed „której” także w konferencji 2019 (ten sam błąd); poza 6A: usunięty nieużywany import, kotwica w EN Annals; push bez słowa „push” — polecenie właściciela z 22.11.
Pytania do użytkownika: (1) czy przełącznik języka ma przenosić #kotwicę i czy ujednolicić id na stronie Rok akademicki (kod + {#legal-basis} + 3 linki #day-colours w Web-Studia); (2) zakresy dat z łącznikiem „8-13 maja 2022”, „7-12 maja 2023” w konferencjach 2021/2022 — poprawić?; (3) sprawy „Do decyzji” z raportów agentów nierozstrzygnięte w zleceniu — lista w raporcie, sekcja 8.

## 59-kotwice-i-ramka-dzis — 2026-11-22 15:55
Status: zrobione i wypchnięte po „Tak, push” właściciela: Web-Core `9dc6ca58..bf4ce0a1` (15:50:57), Web-Studia `7d4a2f7..eb6a4fc` (15:51:00), fast-forward, bez nowych zmian redaktorów; po pushu w Web-Studia zmienione tylko pola tresc_en/dalej_en. Akcje: Web-Core 45035041500, Web-Studia 45035046668, przekaźnik 45035067394, Podgląd 45035086146 — success. Gałęzie praca/59-kotwice tylko lokalnie. Decyzja właściciela z 22.11 po pytaniu 1 z raportu 59 („Dobra. Zgadzam się, popraw”) i jego uwaga o ramce „dziś” („Czemu czarny prostokącik wygląda jakby był za kafelkiem”). Opis w RAPORT-ZLECENIE-59.md, sekcja 9.
Zmienione pliki: Web-Core — src/scripts/zal/jezyk-kotwica.ts (nowy: przełącznik języka a.z-jezyk zabiera #kotwicę z adresu), src/components/Naglowek.astro (dołącza skrypt), src/lib/widoki/rokAkademicki.ts (id sekcji wspólne PL/EN: kolory-dni, rok-w-skrócie, do-pobrania), src/views/KoloryDniSemestr.astro (ramka „dziś” od środka kafelka, jak w legendzie; przy zamianie obwódka dnia przesunięta do środka). Web-Studia — src/data/rok-akademicki.md ({#legal-basis} → {#podstawa-prawna} w EN), src/content/strony/studia/pierwszy-rok.md i zajecia.md (linki EN #day-colours → #kolory-dni).
Kryteria odbioru:
- po zmianie języka czytelnik zostaje w tej samej sekcji — spełnione (przeglądarka: PL „Rok w skrócie” → EN „The year at a glance”, EN „Legal basis” → PL „Podstawa prawna”; bez kotwicy link na górę strony jak dotąd);
- spis „Na tej stronie” z tymi samymi id w PL i EN — spełnione na 88/88 stronach (z59-kotwice.py);
- strony PL bez zmian w treści — spełnione (477/477, różni się tylko hash skryptu/CSS); EN tylko Rok akademicki, Pierwszy rok, Zajęcia;
- ramka „dziś” na kafelku, nie w szczelinach — spełnione (zrzut raport-zrzuty/z59-zrzuty/z59-dzis-ramka-przed-po.png); astro check 0 błędów.
Odstępstwa od zlecenia i powody: brak.
Pytania do użytkownika: brak.

## media-foldery — 2026-11-22 22:15
Status: zrobione i wypchnięte na polecenie właściciela („Wszystkie repozytoria”, „Zrobisz push i od razu zaktualizujesz githuba?”, „I zaktualizuj instrukcje dla redaktorów”). Bez numeru zlecenia. Powód: na stronie pliki ze wszystkich repozytoriów są we wspólnym /pliki; ten sam plik w dwóch repozytoriach przerywał budowę Podglądu (pobierz_tresci.py) bez komunikatu dla redaktora, a Pages CMS widzi tylko swoje repozytorium. Najgroźniej w seminariach: 9 repozytoriów zapisywało slajdy do wspólnego /pliki/seminaria.
Zmienione pliki: 16 repozytoriów treści — .pages.yml: media jako lista własnych folderów (seminaria: public/pliki/seminaria/<nazwa>, etykieta „Media”; Aktualności: aktualnosci, obrony; Instytut: warto-wiedziec, wladze, zaklady; Nauka: nauka, konferencje; Studia: studia, szkola-doktorska; Ustawienia: baner, naglowki, partnerzy, ustawienia — pole „Logo” z public/pliki na public/pliki/ustawienia; Popularyzacja, Pracownicy: po jednym), options.media w każdym polu file/image, opisy pól Treść z adresem /pliki/… i uwagą o „-1”. Web-Sem-Rownania-Rozniczkowe: nadzieja-seminarium.pdf → public/pliki/seminaria/rownania-rozniczkowe/, link w opisie poprawiony (f783881). Web-Core 55693cab: skrypty/pobierz_tresci.py (adnotacja „Błąd plików” przy kolizji, tylko GITHUB_ACTIONS), skrypty/sprawdz_pola_cms.py (punkt 4: foldery Media), README.md, dok/dla-redaktorow/mapa-cms.html (foldery Media, „-1”; .dzialy li 8.2pt/1.3, bo strona 1 wystawała o 47 px już przed zmianą), .gitignore (/public/pliki/partnerzy/). Web-Podglad 3febc95: dla-redaktorow/Mapa-CMS-IM-UWr.pdf.
Kryteria odbioru:
- Pages CMS (Chrome właściciela): Równania — „Media” pokazuje tylko folder seminarium; Studia — dwie pozycje „Media: studia”, „Media: szkoła doktorska” — spełnione;
- sprawdz_pola_cms.py na klonach po zmianie: 0 problemów; stary stan: 16 zgłoszeń; sztuczne naruszenia (wspólny folder, pole bez media, plik poza folderem) wykryte — spełnione;
- symulowana kolizja w pobierz_tresci.py daje adnotacje „Błąd plików” — spełnione;
- Podgląd: krok „Treści” przechodzi (1333 plików z 16 repozytoriów, bez kolizji); budowa NIE przechodzi od 20:53 z innego powodu: Web-Popularyzacja 6d778b6 (pborod, 20:52) — w organizatorzy.md zakomentowana linia „- *konkurs od 1967*” w bloku :::kontakty („Blok kontakty wymaga jednej listy ul.”); plakietka pokazuje tylko ogólny błąd budowy.
Odstępstwa od zlecenia i powody: brak.
Pytania do użytkownika: (1) jak naprawić punkt PTM w organizatorzy.md (przywrócić rolę „konkurs od 1967”, inna rola, czy zostawić redaktorowi); (2) bledy_budowy.py nie rozpoznaje „Failed to parse Markdown file” z bloków jawnego Markdownu — redaktor dostaje tylko ogólny komunikat.

## krotkie-adresy-plikow — 2026-11-22 22:40
Zlecenie: od właściciela w rozmowie („Maximal friendly dla edytorów”): w linku redaktor wpisuje plik tak, jak widzi go w Media swojego repozytorium; plik z innego repozytorium — z nazwą repozytorium na początku; strona sama układa pełne ścieżki.
Zrobione: skrypty/adresy_plikow.py (Adresy.pelny/przepisz, foldery_media z .pages.yml wierszami, bez PyYAML) + skrypty/test_adresy_plikow.py (9 testów); pobierz_tresci.py przy nakładaniu plików tekstowych z src/ zamienia krótkie adresy w linkach i obrazkach Markdownu na /pliki/…; brak pliku = ostrzeżenie „Plik w treści” (::warning), nie błąd. Formy: nazwa.pdf, /nazwa.pdf, folder/nazwa.pdf, Web-Nauka/nazwa.pdf (nazwa repozytorium bez względu na wielkość liter), pliki/…; pomijane: /pliki, /grafiki, /kalendarz, /pagefind, /_astro, /en, adresy bez rozszerzenia, ze schematem, z #, linki w `kodzie`. Opisy pól Treść w .pages.yml 14 repozytoriów (Studia i Popularyzacja nie miały podpowiedzi o plikach). README, mapa-cms.html (też przykłady :::etapy i :::pliki), sciagawka-edytora.md. Web-Sem-Rownania-Rozniczkowe: link do artykułu Nadziei na krótki adres (pokaz działania).
Commity: Web-Core d6bf55a8; Web-Podglad 4a67c10 (PDF); repozytoria treści f8ab006, 0a9ad93, ce24898, 33d12b3, 1ad4e72, 4b620c8, fd45d84, 0649d14, 75adb22, 8189168, 0d8eb1d, 185eb62, d87bb27, adb36c9.
Kryteria odbioru:
- testy jednostkowe: 9/9; próba pobierz_tresci --lokalnie na wszystkich klonach: 3 zamiany, ostrzeżenie dla brakującego pliku, pozostałe 1332 pliki bajtowo bez zmian — spełnione;
- sprawdz_pola_cms.py na klonach: 0 problemów — spełnione;
- PDF dla redaktorów: 2 str. — spełnione;
- Podgląd po pushu: patrz niżej.
Uwaga: w drzewie Web-Core są niezatwierdzone zmiany innej sesji (bledy_budowy.py, src/lib/markdown.ts, tekstyStron.ts, widoki/*, bladTresci.mjs, blad-tresci.test.mjs) — nie dotykane.
Podgląd po pushu: przebieg 45072728687 — success; w kroku „Treści” „Krótkie adresy plików zamienione na /pliki/…: 1.”, bez BRAK PLIKU; na /seminaria/rownania-rozniczkowe link prowadzi do /Web-Podglad/pliki/seminaria/rownania-rozniczkowe/nadzieja-seminarium.pdf (200, application/pdf) — spełnione.

## bledy-budowy-bloki — 2026-11-22 22:36
Status: zrobione lokalnie w Web-Core, bez commita i pushu (zadanie z sesji nadrzędnej: „Nie commituj i nie pushuj bez polecenia właściciela”). Powód: od 20:53 Podgląd nie budował się przez blok :::kontakty w Web-Popularyzacja 6d778b6 (przebieg 45070803078), a plakietka pokazała tylko „Budowa zakończyła się błędem; szczegóły w dzienniku budowy.”. Dwie przyczyny: (1) src/lib/markdown.ts renderuje tekst pola bez ścieżki pliku, więc Astro pisze „Failed to parse Markdown file "undefined"” (fileURL odpada: zmienia HTML obrazków — remarkCollectImages i rehypeImages w @astrojs/markdown-remark); (2) podglad.yml zapisuje do budowa.log tylko stdout (`npm run build | tee`), a Astro wypisuje błędy przez console.error na stderr — skrypt nie dostaje żadnego komunikatu błędu (z kodu wynika, że dotyczy to też błędów schematu z zlecenia 33; we wszystkich 4 nieudanych budowach 22.11 tylko ogólna adnotacja).
Zmienione pliki: Web-Core — src/lib/bladTresci.mjs (nowy: błąd z file.fail → „Błąd w treści pliku "<plik>", pole <pole>, blok :::<blok>, wiersz <n>: <komunikat>”, inne błędy bez zmian), src/lib/markdown.ts (renderuj(): try/catch wokół processor.render; zrodlo {plik, pole, wiersze} w renderMarkdown, renderMarkdownZNaglowkami, renderKierunku, renderSpecjalnosci), plik i pole z wywołań: src/lib/widoki/strona.ts, popularyzacja.ts, rokAkademicki.ts (body/tresc_en, dalej/dalej_en), kierunek.ts, specjalnosc.ts, src/lib/wartoWiedziec.ts, src/lib/tekstyStron.ts (renderTekstu; podziel() podaje też numery wierszy części, żeby wiersz był wierszem pola, a nie wycinka; tekst części bez zmian), skrypty/bledy_budowy.py (bledy_tresci: nowy wiersz, bez niego zapasowo „Failed to parse Markdown file” → Błąd budowy z komunikatem i wierszem; etykieta_pola z .pages.yml: body → „Treść”; adnotacje_bledow wydzielone z main; w opisie wymagane 2>&1), skrypty/test_bledy_budowy.py (nowy, 8 testów) z danymi w skrypty/test-bledy-budowy/ (fragment dziennika przebiegu 45070803078, fragment lokalnej budowy 6d778b6 z nowym kodem, fragment .pages.yml Web-Popularyzacja), src/plugins/blad-tresci.test.mjs (nowy, 5 testów), package.json (test:jawne z nowym testem).
Kryteria odbioru:
- błąd bloku daje adnotację „Błąd treści” w formacie klient.js z nazwą bloku i wierszem — spełnione na prawdziwej lokalnej budowie (organizatorzy.md z 6d778b6 na nakładce, npx astro build 2>&1 | tee): „Web-Popularyzacja › strony › src/content/strony/popularyzacja/organizatorzy.md › Treść: Blok kontakty wymaga jednej listy ul. (blok :::kontakty, wiersz 10) › https://app.pagescms.org/im-uwr/web-popularyzacja/main/collection/strony/edit/src%2Fcontent%2Fstrony%2Fpopularyzacja%2Forganizatorzy.md”; wiersz 10 pola Treść = wiersz 92 pliku („:::kontakty” w sekcji Partnerzy). Na Podglądzie zadziała dopiero po zmianie podglad.yml (pytanie 1);
- ścieżka wskazuje właściwy wpis — spełnione: plik podaje kod (entry.filePath, .file modułu .md), bez zgadywania z dziennika; pole odróżnia Treść od Treść EN;
- test na fragmencie prawdziwego dziennika — spełnione: python skrypty/test_bledy_budowy.py 8/8; npm run test:jawne 89/89; npx tsc --noEmit 0 błędów;
- stary dziennik z Podglądu (bez pliku) daje „Błąd w treści (pliku nie podano): Blok kontakty wymaga jednej listy ul. (wiersz 10)” zamiast ogólnego komunikatu — spełnione.
Uwagi: lokalna budowa z --outDir poza katalogiem projektu zostawiła w .astro/ pośrednią budowę serwera (chunks, pages, _astro, kopie public/) — usunięte tylko pliki z 22:31; nakładka organizatorzy.md przywrócona (md5 jak przed). Pełnej budowy z porównaniem HTML nie było: zmiana działa tylko przy błędzie, a strony przed błędną wyrenderowały się w tej samej budowie.
Odstępstwa od zlecenia i powody: zamiast file.path w fail() — obudowanie render w markdown.ts i plik z miejsc wywołań (ścieżka w vfile zmieniłaby HTML obrazków; jedno miejsce obejmuje też błędy remark-jawne-bloki); Web-Podglad bez zmian (inne repozytorium, bez polecenia).
Pytania do użytkownika: (1) zmiana w Web-Podglad .github/workflows/podglad.yml, krok „Budowanie strony”: `npm run build 2>&1 | tee "$RUNNER_TEMP/budowa.log"` — bez niej żadna adnotacja z treścią błędu nie trafi na plakietkę; (2) commit i push zmian w Web-Core.

## jedno-media-obrony-minione (zlecenia 61–63) — 2026-11-22 23:05
Status: zrobione, wypchnięte (polecenie właściciela: „Jeśli umiesz zrobić bez pytań to zrób i push”, „Po zakończeniu commit i push”).
Opis: zlecenia 60–63 zapisane po fakcie w .przekazanie/zlecenia/ (prośba właściciela: changelog w kolejce zleceń).
Commity: Web-Core 44c1464c; Web-Podglad c9f7b20 (PDF); Web-Aktualnosci 3 commity (ostatni 0728d9d), Web-Instytut 1dd5806, Web-Nauka c7c9f11, Web-Studia 1bddcbc, Web-Ustawienia 76a9218, Web-Popularyzacja c040fc0, Web-Pracownicy e351412, seminaria dd128ca, 4371918, 49e143e, e94a083, e452282, d47df13, bd72cd5, 0728bd8, 6f7cbc7.
Kryteria odbioru:
- jedno Media w każdym repozytorium, sprawdz_pola_cms.py na klonach — 0 problemów — spełnione;
- nałożenie treści przed i po (narzędzie pomiar.py w scratchpadzie): 1378 odwołań /pliki zgodnych po przemapowaniu folderów, martwe 12 = 12 (stare), żaden plik nie zniknął — spełnione;
- testy: test_adresy_plikow.py 9/9, test_obrony_foldery.py 4/4 — spełnione;
- Podgląd (przebieg 45074862220, success): /pliki/studia/szkola-doktorska/… 200, stary /pliki/szkola-doktorska/… 404; /pliki/instytut/wladze/… 200; /pliki/ustawienia/naglowki/instytut.jpg 200; strona obrony M. Tadeja linkuje do /pliki/aktualnosci/obrony/MaciejTadej/… (200); minione referaty (topologia) przygaszone — zrzut; konferencje: 61 wierszy „minelo” — spełnione;
- automat obron: pierwszy przebieg 45074764838 success, bez zmian (zgodnie z oczekiwaniem). Zapis automatu (contents: write) sprawdzi dopiero pierwsza obrona dodana w CMS.
Odstępstwa: Studia i Popularyzacja bez podpowiedzi o plikach w opisach pól (nie miały jej wcześniej).
Uwaga: niezatwierdzone zmiany innej sesji w Web-Core (bledy_budowy.py, markdown.ts, tekstyStron.ts, widoki/*, package.json, bladTresci.mjs) nietknięte.

## tutornia-web-tutornia (zlecenie 64) — 2026-11-22 23:20
Status: zrobione, wypchnięte (polecenie właściciela: „edycja Tutorni (CMS) ląduje do nowego repo Web-Tutornia […] Zaktualizuj wszystkie miejsca, w tym instrukcje dla edytorów. Potem push”).
Opis: .przekazanie/zlecenia/64-tutornia-web-tutornia.md (changelog).
Commity: Web-Tutornia 99ba1b0 (pierwszy), Web-Studia 693aac9, Web-Core 81eb5a0c, Web-Podglad 37f7a11 (PDF mapy CMS).
Kryteria odbioru:
- sprawdz_pola_cms.py na klonach (17 repozytoriów) — 0 problemów — spełnione;
- nałożenie lokalne (pobierz_tresci.py --lokalnie): bez kolizji, tutornia.md tylko z Web-Tutornia, identyczna z dawną — spełnione;
- grafik.test.mjs 11/11; PDF mapy 2 strony — spełnione;
- powiadom.yml w Web-Tutornia (45075859634): klucz i sygnał do Web-Core — success — spełnione;
- Podgląd (45075911167, success; Web-Core 81eb5a0, Web-Tutornia 99ba1b0): /studia/tutornia i /en/studia/tutornia 200, plan dyżurów (tu-grafik, Sala 202) na stronie — spełnione;
- Pages CMS (Chrome właściciela, tylko odczyt): Web-Tutornia otwiera formularz „Tutornia” z treścią; „Strony studiów” w Web-Studia bez Tutorni — spełnione.
Do zrobienia przez właściciela: zaprosić studentów-tutorów (Pages CMS → Web-Tutornia → Admin → Collaborators albo współpracownicy na GitHubie).
Uwaga: niezatwierdzone zmiany innej sesji w Web-Core (bledy_budowy.py, markdown.ts, tekstyStron.ts, widoki/*, package.json, bladTresci.mjs) nietknięte.

## odbyte-obrony-minione-referaty-dwie-kolumny (zlecenie 65) — 2026-11-22 23:30
Status: zrobione, wypchnięte (polecenie właściciela: „Tak, tak samo […] układ obron doktorskich odbytych zrób taki sam jak przy konferencjach […] Tak samo dla odbytych seminariów […] Rozwinięcie kolejnego streszczenia zwija poprzednie”).
Opis: .przekazanie/zlecenia/65-odbyte-obrony-i-minione-referaty-dwie-kolumny.md (changelog).
Commity: Web-Core 629c820a (ListaObron.astro, Seminarium.astro).
Kryteria odbioru:
- obrony „Odbyte”: dwie kolumny na komputerze, styl wiersza Konferencji, przygaszone; telefon jedna kolumna — spełnione (zrzuty lokalne);
- minione referaty: dwie kolumny; rozwinięte streszczenie na cały rząd, sąsiad pod nim, jedno naraz, wiersz w tym samym miejscu ekranu — spełnione (test Playwright lokalnie i na Podglądzie);
- Podgląd 45077650288 success (Web-Core 629c820).
Uwaga: nakładka treści w Web-Core odświeżona z main (pobierz_tresci.py) do testów; niezatwierdzone zmiany innej sesji w Web-Core nietknięte.

## usuniete-wpisy-testowe (zlecenie 66) — 2026-11-22 23:40
Status: zrobione, wypchnięte (polecenie właściciela: „wywal wszystkie wpisy testowe”).
Opis: .przekazanie/zlecenia/66-usuniete-wpisy-testowe.md (changelog).
Commity: Web-Aktualnosci c0c03bc; seminaria 3dc3a28, c928a13, ad2662e, be54b69, b74daf4, 51150a0, 1137bd9, 008e9a4; Web-Core f23fb4dc (dok/start-strony.md).
Kryteria odbioru:
- skan 17 repozytoriów: poza 8 referatami i 4 zdjęciami brak wpisów testowych (fałszywe trafienia: test-*.pdf w Web-Studia, czasopismo TEST, „testowanie” w opisach) — spełnione;
- Podgląd 45078423921 success, wszystkie 9 commitów; 0 trafień „Prelegent testowy”/„TEST: ”/„sala TEST” na seminariach, w kalendarzu i na stronie głównej — spełnione.

## instrukcje-dla-redaktorow-w-pdf (zlecenie 67) — 2026-11-23 00:10
Status: zrobione, wypchnięte (polecenie właściciela: „oba pliki zrobić w pdf i wrzucić je na linki […] od razu widzi pdf”; „Z innych miejsc je wszędzie pousuwaj”).
Opis: .przekazanie/zlecenia/67-instrukcje-dla-redaktorow-w-pdf.md (changelog).
Adresy: https://im-uwr.github.io/Web-Podglad/dla-redaktorow/Mapa-CMS-IM-UWr.pdf, …/Sciagawka-edytora-IM-UWr.pdf (źródło: Web-Core public/dla-redaktorow/, skrypt skrypty/pdf-dla-redaktorow.mjs).
Commity: Web-Core 1a791362; Web-Podglad 321a0a0 [skip ci].
Kryteria odbioru:
- oba adresy 200, application/pdf, rozmiary jak pliki — spełnione (Podgląd 45080966245);
- kopie usunięte: Web-Podglad/dla-redaktorow/Mapa…, Web-Core dok/mapa-redakcyjna-IM-UWr.pdf, Web-Core/Claude outputs/Mapa… (Kosz) — spełnione; kopie w starych folderach (podglad-z33, tresci-B, tresci-C, Web-Core-B) — przy porządkach folderów.

## seminaria-minione-wedlug-lat (zlecenie 68) — 2026-11-23 00:45
Status: zrobione, wypchnięte (polecenie właściciela: „Przed pushem: git pull --rebase origin main, ponowna budowa i kontrole, potem push na main bez czekania na »push«”).
Zlecenie: zlecenia/68-seminaria-minione-wedlug-lat.md (pisane jako 67; 67 zajęte → 68). Raport: raporty/RAPORT-ZLECENIE-68.md.
Zmienione pliki: src/lib/daty.ts (rokAkademicki, od 1.10), src/lib/widoki/seminarium.ts (lataMinionych), src/views/Seminarium.astro (lata h3#rok-RRRR-RR, siatka na rok, tytuł h4, spis z latami, skrypt na wszystkie siatki).
Commity: Web-Core e081f76f (po rebase na 9f62de8d). Praca w osobnym worktree Web-Core-67 (usunięty po pushu).
Kryteria odbioru:
- podział na lata akademickie z liczbą (PL/EN odmiana), od najnowszego — spełnione (2626 wierszy PL+EN, reguła 1.10 bez błędu);
- spis: Nadchodzące, Minione, lata — spełnione (klik myszą i Enter, znacznik podąża);
- minione z jednego roku jak dotąd — spełnione (Analiza harmoniczna i Prawdopodobieństwo na treściach z main);
- wiersze jak przed zmianą, dwie kolumny i rozwijanie w każdym roku, kotwice #<slug> — spełnione (getComputedStyle 244 wierszy przy 1920/1440/1024/390, jasny i ciemny; 2648 linków z Kalendarza i listy seminariów);
- inne strony bez zmian — spełnione (diff dist: poza /seminaria/<id> tylko znaczniki czasu); repozytoria treści bez zmian — spełnione;
- raport: rozmiary (max DAH EN 894 KB, < 1 MB) i Kalendarz → Archiwum (pomiar bez emulacji CPU ×4 — niedostępna) — spełnione częściowo, opis w raporcie.
Odstępstwa: numer 68; push bez czekania na „push” (polecenie właściciela).
Uwaga: niezatwierdzone zmiany innej sesji w Web-Core nietknięte (praca tylko w worktree).
