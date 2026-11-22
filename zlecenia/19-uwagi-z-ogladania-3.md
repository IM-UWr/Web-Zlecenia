# Zlecenie 19: uwagi z oglądania, część 3 (OTWARTE, 6.11.2026)

Stan: **otwarte** — właściciel dopisuje kolejne punkty. Wykonuj tylko punkty oznaczone **GOTOWE** i dopiero po zakończeniu zlecenia 18.

**Gdzie i jak** (tak samo jak w zleceniach 17 i 18)
- Gałąź `wyglad/zlecenie-16`, po commitach zlecenia 18. Osobny commit na każdy punkt. **Bez pushowania**, także w repozytoriach treści.
- **Nie uruchamiaj `skrypty/pobierz_tresci.py`.**
- Dziennik w `.przekazanie\dziennik.md`, raport `RAPORT-ZLECENIE-19.md`.
- Kopia bezpieczeństwa stanu z 6.11, 02:08 jest na GitHubie w gałęziach `kopia/2026-11-06-*` (tylko do odtworzenia, nie scalać).

## 1. Lista Aktualności: kolory działów jak na Szybkim dostępie — GOTOWE (decyzja 6.11, 02:18)
Właściciel: na Szybkim dostępie wpisy mają kolory, a na stronie Aktualności nie. Punkt zmienia wcześniejsze ustalenie „kolor jednolity” (zlecenie 18, punkty 3 i 9). Wykonaj po punkcie 9 zlecenia 18, bo korzysta z jego reguły.

**Dlaczego dziś nie ma kolorów:** `.wa-data` i `.wa-rodz` w `WierszAktualnosci.astro` używają już `var(--d-a)`, ale `<article class="wa">` nie ma `data-dzial`, więc zmienna ma kolor neutralny. Na Szybkim dostępie wiersz dostaje `data-dzial` z `dzialWpisu`.

- Użyj wspólnej funkcji z punktu 9 zlecenia 18 (`src/lib/`), bez kopii reguły.
- `PozycjaListy` (`src/lib/tresci.ts`) nie ma pola `zaklad`, a reguła go potrzebuje: dodaj je w `listaAktualnosci()`.
- `WierszAktualnosci.astro`: `<article ... data-dzial={dzial}>`. Kolor działu dostają data, etykieta rodzaju, tytuł po najechaniu i obrys fokusu. Tekst etykiety bez zmian („Rodzaj · odbiorcy”).
- Dotyczy też wpisu wyróżnionego (boks na papierze) i wiersza po filtrze lub szukaniu.
- Bez zmian: nagłówki miesięcy, filtry i szukanie, baner.
- Komputer i telefon, PL i EN. W ciemnym motywie kolory z istniejącej reguły `[data-dzial]`.
- Popraw komentarze w `WierszAktualnosci.astro` i opis koloru w `dok/estetyka.md`.

**Odbiór**
- `astro check` bez nowych błędów, `npm run build` przechodzi.
- Ten sam wpis ma ten sam dział na Szybkim dostępie i na liście. W raporcie tabela: 15 ostatnich wpisów → dział na obu widokach.
- Kontrast daty i etykiety co najmniej 4,5:1 w każdym kolorze działu, w obu motywach; także na boksie wyróżnionym.
- Zrzuty listy przy 1536 i 390 px, jasny i ciemny motyw → `raport-zrzuty/z19-akt-kolory-*`.

## 2. Okładka (komputer, PL i EN): tytuł i ciemne pole kończą się na jednym łuku — GOTOWE (decyzja 6.11, 02:26; EN 02:44)
Właściciel wybrał to ustawienie w podglądzie „Półksiężyc” (suwaki: „Matematyczny” 62 %, odstęp 23 %, wygięcie 60, wysokość tytułu 29 %). Łuk zastępuje skos z `ULOZ` (prosta o nachyleniu 0,32) **na komputerze, w obu językach**. Wersję angielską właściciel wybrał o 02:44 (propozycja C): mniejsze „Mathematical” nad dużym „Institute”. Wykonaj po punkcie 13 zlecenia 18 (kadr zdjęcia), bo ten punkt z niego korzysta.

**Zasada:** ciemne pole po lewej kończy się łukiem koła wygiętym w stronę zdjęcia, jak „(”. Łuk przechodzi 58 px za końcami trzech napisów: nazwy wydziału w marce (`.z-okl-marka`, bez zmian: top 18 px, left 48 px), „Instytut” i „Matematyczny”. Łuk jest **monotoniczny**: w dół zawsze przesuwa się w prawo i nigdzie nie wraca w lewo. To znaczy, że środek koła leży po prawej i nie niżej niż środek marki.

**Stałe** — w jednym obiekcie na początku skryptu, osobno dla każdego języka (np. `UKLAD = { pl: {...}, en: {...} }`), z komentarzem. Właściciel może je później zmienić: wtedy zmienia się tylko liczby, bez ruszania wzorów.
- ODSTEP = 58 px (wspólne).
- PL: MAT = 0,62 (stopień „Matematyczny” / stopień „Instytut”), ODST = 0,23 (odstęp między liniami / stopień „Instytut”), K = 0,60, GORA = 0,29.
- EN: MAT = 0,55 (stopień „Mathematical” / stopień „Institute”), ODST = 0,23 (odstęp / stopień „Institute”), K = 0,60, GORA = 0,29.
- K to wygięcie: nachylenie odcinka marka→koniec pierwszej linii = K × nachylenie odcinka między końcami linii. K = 1 daje prostą.

**Algorytm** (w skrypcie `ULOZ`, przy każdym przeliczeniu, jak dziś)
1. H, W: wymiary okładki. u = prawa krawędź napisu wydziału (`.z-okl-marka > span:last-child`) + ODSTEP. yM = środek pionowy `.z-okl-marka`. lewa = lewa krawędź tytułu (48 px).
2. wI, wM: szerokości „Instytut” i „Matematyczny” (EN: wA = „Mathematical”, wN = „Institute”) przy 100 px (ukryta miarka ze stylem `h1`: krój, waga 500, letter-spacing −0,012em), podzielone przez 100.
3. Obliczenia (0,49 = połowa line-height 0,98, czyli środek linii):
   - s2 = (wM·MAT − wI) / (0,49·(1 + MAT) + ODST);
   - top = GORA·H (góra pierwszej linii h1);
   - f1 = (K·s2·(top − yM) + u − lewa − ODSTEP) / (wI − 0,49·K·s2);
   - f2 = MAT·f1;
   - odstęp = ODST·f1.

   **EN** (duże jest drugie słowo, F = stopień „Institute”), c = u − lewa − ODSTEP:
   - s12 = (wN − wA·MAT) / (0,49·MAT + ODST + 0,49);
   - F = (c + K·s12·(top − yM)) / (wA·MAT − 0,49·MAT·K·s12);
   - f1 („Mathematical”) = MAT·F, f2 („Institute”) = F, odstęp = ODST·F.

   Dzisiejsze wykrywanie „drugie słowo krótsze” (`wyr`) nie jest już potrzebne: układ wybiera `lang`.
4. Ustaw `--f1` i `--f2`, `.w2 { margin-top: odstęp }` (zamiast 0,04em) oraz top h1 (zamiast `clamp(84px, calc(var(--h) * .2), 220px)`).
5. Szkice działów: jeśli dół „Matematyczny” + 24 px wypada niżej niż góra rzędu szkiców (`.z-okl-szkic`), zmniejsz top i policz krok 3 jeszcze raz (2–3 przebiegi; f1 zależy od top liniowo). Top nie może być mniejszy niż dół marki + 40 px.
6. Zmierz prawdziwe końce linii (`getBoundingClientRect()` spanów `.w1` i `.w2`: `right` i środek pionowy). Daje to trzy punkty:
   - P0 = (u, yM);
   - P1 = (koniec `.w1` + 58, środek `.w1`);
   - P2 = (koniec `.w2` + 58, środek `.w2`).

   Policz koło przez te trzy punkty: cx, cy, R. Sprawdź, czy cx jest większe niż x każdego punktu i czy cy ≤ yM + 1. Jeśli nie (nie powinno się zdarzyć), zostaje dzisiejszy skos, a w DEV pojawia się ostrzeżenie w konsoli.
7. Ciemne pole: `--skos` na `.z-skos` zamiast gradientu liniowego:
   - `radial-gradient(circle at {cx}px {cy}px, rgb(9 16 34 / 0) {R−30}px, rgb(9 16 34 / .62) {R}px, rgb(9 16 34 / .97) {R+30}px)`;
   - maska `linear-gradient(90deg, #000 {cx}px, transparent {cx}px)`, żeby na prawo od środka koła nic się nie przyciemniało (ultrawide).

   Górny cień i dolny pas pod działami bez zmian.
8. Zdjęcie: `--foto-x = max(0, min(koniec napisu wydziału, x łuku na wysokości 0) − 130)`, gdzie x(y) = cx − √(R² − (y − cy)²). Dalej kadr z punktu 13 zlecenia 18 bez zmian (D, top, `object-fit: fill`, `max-width: none`). Maska lewej krawędzi zdjęcia (0 → 140 px) też bez zmian.

**Wartości kontrolne z podglądu** (krój strony może je zmienić o kilka px):

| Okno (wysokość okładki) | „Instytut” | „Matematyczny” | Odstęp | R | Środek koła |
|---|---|---|---|---|---|
| 1536×864 (730) | 128 | 79 | 29 | ≈1020 | (1390, −198) |
| 1920×1080 (940) | 136 | 84 | 31 | ≈1220 | (1587, −234) |
| 2560×1440 (1300) | 150 | 93 | 34 | ≈1560 | (1923, −296) |

| EN: okno (wysokość okładki) | „Mathematical” | „Institute” | Odstęp | R |
|---|---|---|---|---|
| 1536×864 (730) | 63 | 115 | 27 | ≈1820 |
| 1920×1080 (940) | 65 | 118 | 27 | ≈2190 |
| 2560×1440 (1300) | 68 | 123 | 28 | ≈2820 |

Po angielsku napis wydziału w marce („Faculty of Mathematics / and Computer Science”) jest dłuższy, więc u jest większe niż po polsku. Mierz go w każdym języku.

- Przy wysokości 730 krok 5 może podnieść tytuł. W podglądzie top spada wtedy do ok. 172 px, a „Instytut” do ok. 122 px.
- „Instytut” ma prawie stały rozmiar w px, bo marka ma stały rozmiar.
- Szerokość okna nie zmienia tytułu ani łuku (16:9 i ultrawide wychodzą tak samo). Zmienia się tylko zdjęcie.

**Bez zmian**
- Telefon (≤ 760 px).
- Strona bez JS: zwykły gradient, jak dziś.
- Flaga „wyróżnione” stoi nad tytułem i nie przesuwa h1. Jeśli sięgałaby łuku, łamie się na dwie linie (max-width: do łuku − 24 px).

**Komentarze i dokumentacja:** w nagłówku `Okladka.astro`, przy `ULOZ` i w `dok/estetyka.md` („Okładka”) zmień opis skosu na opis łuku.

**Odbiór**
- `astro check` bez nowych błędów, `npm run build` przechodzi.
- W raporcie tabela dla okien 1280×600, 1536×730, 1920×940, 2560×940, 2560×1300 i 3440×1300. Kolumny: f1, f2, odstęp, top, R, cx, cy, odległość każdego z trzech końców od łuku (58 ± 2 px), monotoniczność (tak/nie), czy tytuł nachodzi na szkice lub markę.
- Tabela z odbioru osobno dla PL i EN.
- Zrzuty PL i EN przy 1536×730, 1920×940 i 2560×940 → `raport-zrzuty/z19-luk-*`. Zdjęcie bez ściskania i rozciągania (sprawdzenie proporcji jak w punkcie 13 zlecenia 18).
- Telefon bez zmian: zrzut przy 390 px.

## 3. Telefon, baner działu: podpis na wysokości krótkiego opisu, szkic tuż nad nim — GOTOWE (decyzja 6.11, 02:33)
Właściciel: „niech podpis będzie na wysokości »Topolog, oddany dydaktyce«”. Wykonaj po punkcie 14 zlecenia 18 i zmień jego wynik: `.z-szkic-ramka { top: 24px; }` i `.z-slot { order: 3; }` z tamtego punktu przestają obowiązywać. Dotyczy `.z-baner-dzialu` (cztery strony działów, PL i EN), tylko telefon (≤ 760 px, `zal-telefon.css`). Komputer i banery podstron bez zmian. Podgląd przy `npm run dev`: `http://localhost:4321/Web-Core/@fs/C:/Users/Szymek/Documents/GitHub/Web-Core/.przekazanie/prototypy/telefon.html#s=instytut&m=i`.

Szkic i podpis idą za blokiem patrona w przepływie, bez stałych `top`, bo wysokość zależy od hasła i opisu. Ujemne marginesy nie zmieniają wysokości banera. Wartości z podglądu:
- `.z-patron { order: 2; }`, `.z-patron p { max-width: calc(100% - 150px); }`;
- `.z-szkic-ramka { order: 3; position: relative; top: auto; right: auto; flex: none; align-self: flex-end; margin: -172px -14px 6px 0; }`;
- `.z-podpis-ramka { order: 4; position: relative; top: auto; right: auto; flex: none; align-self: flex-end; margin: -23.5px -2px -4.5px 0; }`;
- `.z-slot { order: 5; }`;
- do 340 px: `.z-szkic-ramka { width: 104px; height: 125px; margin-top: -131px; }`.

**Odbiór**
- Podpis stoi na wysokości ostatniej linii krótkiego opisu we wszystkich działach.
- Szkic i podpis nie nachodzą na hasło, nazwisko, linię lat ani opis przy 320, 360, 390 i 430 px, PL i EN (w podglądzie PL bez kolizji). Jeśli nachodzą, popraw to i opisz w raporcie.
- Wysokość banera taka sama jak po punkcie 14 zlecenia 18. Podaj wysokości wszystkich działów przy 360 i 390 px.
- Zrzuty czterech działów przy 390 px, jasny i ciemny motyw → `raport-zrzuty/z19-baner-dzial-*`.
