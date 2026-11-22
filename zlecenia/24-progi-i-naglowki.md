# Zlecenie 24: średnie ekrany — próg widoku telefonu i nagłówki (GOTOWE, 6.11.2026)

Stan: **wszystkie punkty GOTOWE** (decyzje właściciela 6.11, 21:55–22:16). Pierwsze z czterech zleceń „średnie ekrany” (24 → 25 → 26 → 27).

**Gdzie i jak** (tak samo jak w zleceniach 17–23)
- Gałąź `wyglad/zlecenie-16`, po commitach zleceń 21–23. Osobny commit na każdy punkt. **Bez pushowania**, także w repozytoriach treści.
- **Nie uruchamiaj `skrypty/pobierz_tresci.py`** (najwyżej z `--lokalnie`, jeśli naprawdę trzeba).
- Dziennik w `.przekazanie\dziennik.md`, raport `RAPORT-ZLECENIE-24.md`, zrzuty `raport-zrzuty/z24-*`.
- Numery linii są ze stanu `b4f99c2` (6.11, 20:21). Jeśli numer 24 jest zajęty, użyj kolejnego i napisz to w raporcie (wtedy przesuń też numery 25–27 i odwołania między nimi).
- Każdy nowy tekst ma wersję PL i EN.

**Skąd to zlecenie.** Właściciel zgłosił, że strona psuje się na średnich ekranach. Przegląd (raport https://claude.ai/artifact/V8F6WnmDJZvoGh44Mq2DSd, 65 stron PL i EN × 11 okien 800–1920 px, pięciu agentów): od 1366 px wszystko jak we wzorcu, poniżej ok. 1100 px psuje się — przy 1024 px 5 z 16 szablonów, przy 860 px 9. Przyczyna: są dwa układy (telefon ≤ 760, komputer ≥ 761 liczony w stałych pikselach pod kolumnę 1240 px; poniżej 1368 px margines ma stałe 64 px), a tekst patrona i ciekawostka są przypięte absolutnie do prawej krawędzi i nie ustępują miejsca tytułowi.

**Narzędzie odbioru (dla zleceń 24–27):** `24-zalaczniki/24-pomiar-szerokosci.cjs` (Playwright, bez dodawania zależności do `package.json`: `npx playwright install chromium` i uruchomienie przez `npx`/`NODE_PATH`). Renderuje listę stron w 11 oknach i zgłasza: kolizje tekstu (K), tekst poza ramką kafelka/pola/przycisku (R), tekst obcięty przez overflow (O), tekst poza oknem (W), poziome przewijanie (X); robi zrzuty. Adres strony w zmiennej `BAZA` (np. zbudowane `dist` serwowane lokalnie albo `npm run preview`), wyniki w `raport-zrzuty/szerokosci/` (zmienna `OUT`). `24-podsumuj-pomiar.py` robi z wyników macierz strona × okno. Detektor nie widzi kolizji tekstu z rysunkami SVG, strzałek z `::after` ani tekstu łamanego litera po literze — to sprawdzaj na zrzutach. **Ciekawostki są losowane przy każdej wizycie:** przy odbiorze nagłówków przejdź przez **całą pulę** ciekawostek działu na każdej stronie (np. ustawiając zestaw w `sessionStorage` „im-ciek-zestaw” przed wejściem albo podmieniając ciekawostkę skryptem), nie przez jedno losowanie.

## 1. Widok telefonu poniżej 1024 px — GOTOWE (decyzja 6.11, 22:10–22:16)
Właściciel: „może zrobimy, że tryb mobilny startuje szybciej, bo teraz dość szybko ucina cyferki, np. startuje już przy 1000 około”. Ustalony próg: **1024 px** — w tym samym miejscu, w którym pasek menu przechodzi w hamburgera (`zalozyciele.css:496`), więc na stronie jest jedno przełączenie zamiast dwóch.

- `src/lib/media.ts`: `MQ_TELEFON = '(max-width: 1023px), (max-height: 500px) and (pointer: coarse)'`, `MQ_KOMPUTER = '(min-width: 1024px) and (min-height: 501px), (min-width: 1024px) and (pointer: fine)'`, `sizesTelefon` z `(max-width: 1023px)`. Komentarze w pliku zaktualizuj.
- Wszystkie dosłowne kopie w CSS i skryptach (dziś 56× `max-width: 760px` i 32× `min-width: 761px` w `src`, lista plików: `grep -rln "max-width: 760px\|min-width: 761px" src`) zmień na nowe wartości. Komentarze typu „≤ 760 px”, „≥ 761 px” — na „telefon” / „komputer” albo nowe liczby.
- Progi wewnątrz widoku komputera, które przestają mieć sens (komputer zaczyna się od 1024 px), usuń albo przenieś: `zalozyciele.css:491–504` (pasek: 1024–1119 i ≤ 1023), `zalozyciele-strony.css:149, 158, 162` (761–1179, 761–1365, 761–959), `Seminarium.astro:180` (761–979). Przejrzyj też progi wewnątrz telefonu (np. 720, 780, 820 px ze zlecenia 23): telefon ma teraz do 1023 px szerokości.
- **Widok telefonu na szerokości 760–1023 px:** wzorem zlecenia 23 (telefon w poziomie) tekst ciągły i listy w kolumnie najwyżej ok. 720 px, wyśrodkowanej; banery, zdjęcia i paski na całą szerokość; liczby w banerach w trzech kolumnach. Zrzuty kopii podglądu z tak przesuniętym progiem: `24-telefon-390-800-980-{studia,sd,plan,glowna}.jpg` — trzymały się dobrze (wszystkie 3 liczby widoczne, Plan zajęć i drugi ekran głównej czytelne).
- Zmiana względem zlecenia 23: **iPad pionowo (820×1180) dostaje teraz widok telefonu**; iPad poziomo (1024×768, 1180×820) i iPad Pro (1366×1024) zostają przy komputerze.

**Odbiór:** okna 800×900, 860×780, 960×950, 1000×800 → widok telefonu na wszystkich stronach z listy narzędzia; 1024×700 i szersze → widok komputera; bez poziomego przewijania; tekst ciągły w widoku telefonu nie szerszy niż ok. 720 px; telefon 390×844 i 412×915 piksel w piksel jak przed zmianą; `grep` w `src`: zero `max-width: 760px` i `min-width: 761px`; `astro check` bez nowych błędów, `npm run build` przechodzi.

## 2. Nagłówki 1024–1367 px zmniejszają się razem z oknem — GOTOWE (decyzja 6.11, 22:03–22:16)
Właściciel: „a gdyby w D1 zmniejszać też baner? czcionki, krój itd. … od 1300 mógłby się już zaczynać zmniejszać”, „i głowę też zmniejszać”, „i symbol też”. Ustalono start przy **1368 px** (tam kończy się rosnący margines, więc nagłówek ma tam dokładnie dzisiejsze rozmiary i przejście jest niewidoczne).

- Każdy rozmiar w nagłówku = wartość przy 1368 px × szerokość/1368, z dolnym progiem. Od 1368 px **bez zmian**. Duże rzeczy maleją swobodnie, drobny tekst ma próg ok. 13 px.
- Wartości z prototypu (`24-zalaczniki/24-skala-naglowkow-prototyp.css`, wstrzyknięty w podgląd; przenieś porządnie, bez `!important`, najlepiej jako `clamp()` w istniejących regułach `zalozyciele.css` i zmiennych):
  - **wspólne:** margines `--marg: max(clamp(24px, 4.68vw, 64px), calc((100% - var(--kol)) / 2))` zamiast `max(64px, …)` — poniżej 1368 px maleje z 64 do 24 px, wyżej rośnie z kolumny jak dziś; dotyczy nagłówków i treści, żeby tekst trzymał jedną linię (`.z-nagl`, `.z-dz`, `.z-pd`, `.z-stopka`, `.z-nast`);
  - **baner działu:** wysokość 300 → 230 px (+ `--gora`), tytuł 76 → 44 px (`clamp(44px, 5.56vw, 76px)`), hasło 19 → 15 px, góra bloku tytułu 50 → 34 px; głowa (szkic) 230 → 140 px (`16.8vw`, proporcje 1 : 1,2), odstęp szkicu od marginesu 40 → 14 px; notka patrona: szerokość 270 → 200 px, przesunięta za szkicem (`right: marg + szkic + odstęp`), imię 23 → 18 px, notka 14 → 13 px; podpis 46 → 30 px wysokości, `right` 60 → 22 px;
  - **liczby w banerach:** liczba 30 → 22 px, etykieta 13 px;
  - **nagłówek podstrony:** tytuł 58 → 40 px (dalej działa skrypt dopasowania, punkt 3), wcięcie tytułu na sygnet 122 → 84 px, sygnet 74 → 52 px (wysokość × 1,2), podpis mały 56 → 40 px; symbol ciekawostki 200 → 120 px (`14.6vw`; bez liczb 145×170 w tych samych proporcjach), opis ciekawostki: szerokość 300 → 210 px, stoi tuż na lewo od symbolu (`right: znak-p + symbol + 16 px`), tytuł opisu 15 → 13,5 px;
  - **kursywny tytuł ciekawostki** (`zalozyciele.css:356`) poniżej 1368 px łamie się w swojej kolumnie (bez `white-space: nowrap` i `margin-left: -160px`); od 1368 px bez zmian.
- Zdjęcie Studiów przypięte do szkicu (`zalozyciele.css:219–222`, liczy z `--m` i 155 px) przelicz z nową szerokością szkicu i marginesem, tak żeby twarz Knastera dalej wypadała jak dziś.
- Wynik prototypu: **0 kolizji w nagłówkach** na 17 stronach (4 działy, 2 EN, 11 podstron z ciekawostką, po 3 losowania) przy 860–1280 px; przy 800 px tylko SIAD. Zrzuty: `24-skala-860-1100.jpg` (dziś: `24-dzis-studia-860.jpg`, `24-dzis-szkola-doktorska-960.jpg`).

**Odbiór:** 1368, 1440, 1536, 1920 px — nagłówki piksel w piksel jak przed zmianą (4 działy, 6 podstron); 1024, 1100, 1180, 1280, 1366 px — narzędzie: 0 kolizji i 0 obcięć w nagłówkach na wszystkich stronach z nagłówkiem (PL i EN) **przy każdej ciekawostce z puli**; na zrzutach tekst nie wchodzi na szkic, podpis, symbol ani kreskę notki; drobny tekst w nagłówku nigdzie poniżej 13 px.

## 3. Skrypt dopasowania obejmuje hasło, jedno długie słowo i baner działu — GOTOWE (decyzja 6.11, 22:16)
Dziś `DOPASUJ` (`NaglowekZ.astro:149–181`) zmniejsza tylko tytuł podstrony (`.z-nagl-pod`) i tylko gdy ma ponad dwie linie (`:176`), szerokość h1 ma dolny próg 240 px (`:175`), hasła nie ogranicza, a na banerze działu przycina wyłącznie rząd liczb (`:179`).
- Tytuł maleje także, gdy wystaje w poziomie (jedno długie słowo, np. „Matematyka”, „Organizatorzy”, „Infrastruktura”, „Popularyzacja”): `scrollWidth > clientWidth` albo prawy brzeg tekstu za granicą. Bez progu 240 px: granica wygrywa, najmniej 44 px (podstrona) / 44 px (baner działu).
- Hasło dostaje `max-width` do granicy i się zawija (najwyżej 2 linie).
- To samo na **banerze działu**: granicą jest lewy brzeg tekstu notki patrona (linie wyrównane do prawej — liczyć z prostokątów tekstu, jak dziś dla ciekawostki) minus 40 px.
- Granicę rzędu liczb stosuj tylko wtedy, gdy rząd i tekst patrona/ciekawostki nakładają się w pionie (dziś przy 960–1180 px znikają liczby, które z niczym by nie kolidowały).

**Odbiór:** jak w punkcie 2; dodatkowo przy 1024 px Podyplomowe, Organizatorzy, Infrastruktura informatyczna, ISIM, SIAD, Seminaria, Obrony — tytuł nie dotyka ciekawostki przy żadnej ciekawostce z puli.

## 4. Bezpiecznik i pierwsza liczba — GOTOWE (decyzja 6.11, 22:16)
- **Bezpiecznik:** jeśli mimo punktów 2–3 tekst nagłówka (ścieżka, tytuł, hasło, liczby) dotyka opisu ciekawostki (np. przyszła, dłuższa ciekawostka z CMS), **opis ciekawostki się chowa, symbol zostaje**. Na banerze działu analogicznie chowa się akapit notki patrona, a imię i linia „lata · patron działu · sala” zostają. Ten sam pomiar co w skrypcie dopasowania, przed pierwszym narysowaniem, po `document.fonts.ready` i przy zmianie rozmiaru okna.
- **Pierwsza liczba nigdy ucięta w pół słowa** (dziś „8 semestrów kształceni”, „94 projekty bac”, „kierunki stud” — `NaglowekZ.astro:179–180` zostawia zawsze pierwszą, a rząd ma `overflow: hidden`, `zalozyciele.css:233`). Gdy pierwsza liczba nie mieści się w całości, **znika cały rząd razem z kreską**.

**Odbiór:** podmień na próbę jedną ciekawostkę na bardzo długą (np. 80 znaków w tytule) — przy 1024–1367 px opis znika, symbol zostaje, bez kolizji; w żadnym oknie od 1024 px żadna etykieta liczby nie jest ucięta.

## 5. Ciekawostka w widoku telefonu, gdy jest miejsce — GOTOWE (decyzja 6.11, 22:10–22:16)
Właściciel: „zrobimy tak, że w trybie mobilnym, jeśli jest miejsce, to dalej po lewej od symbolu damy ciekawostkę, a jak nie, to znika”.
- W widoku telefonu opis ciekawostki (dziś `display: none`, `zal-telefon.css` ok. :234) pokazuje się z lewej od symbolu, **jeśli mieści się w szerokości** (16 px odstępu od tytułu, ścieżki, hasła i liczb) **i w wysokości nagłówka** (dół opisu nie niżej niż dół nagłówka minus jego dolny padding). Inaczej znika, symbol zostaje.
- Wzór: `24-zalaczniki/24-ciekawostka-telefon-prototyp.js` (CSS i funkcja „jest miejsce?”), zrzuty `24-ciekawostka-telefon-700-980.jpg`. W prototypie brakowało sprawdzenia wysokości — na Organizatorach przy 700 px niski nagłówek bez liczb ucinał tekst od dołu; dołóż je.
- Pomiar w tych samych chwilach co w punkcie 4 i po wylosowaniu ciekawostki (skrypt CK). Bez JavaScriptu: opis schowany jak dziś.

**Odbiór:** 7 podstron z pliku prototypu przy 600, 700, 800, 900, 980 px, każda ciekawostka z puli: opis albo widoczny w całości bez dotykania tekstu i bez ucięcia, albo schowany; telefon 390 px bez zmian (opis schowany).

## Raport
`RAPORT-ZLECENIE-24.md`: co zmieniono w każdym punkcie, macierz z narzędzia (przed i po, okna 800–1920), lista stron, na których przy 1024–1367 px zadziałał bezpiecznik (punkt 4), zrzuty `raport-zrzuty/z24-*` (Studia, Popularyzacja, Szkoła doktorska, Podyplomowe przy 860, 1024, 1180, 1366, 1920 px), pytania.
