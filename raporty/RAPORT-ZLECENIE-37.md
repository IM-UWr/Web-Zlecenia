# Raport: zlecenie 37, wpis w Aktualnościach z banerem swojego działu

**Status:** zrobione i wypchnięte 18.11.2026 o 12:18 UTC, w trybie samodzielnym.
- Web-Core `main`: `70e9ab73..00fff0a8`, jeden commit, zwykły push, bez force.
- Przed pushem: `fetch`, `origin/main` bez nowych commitów (commit leży wprost na nim), budowa z tego samego drzewa (`tresci-B/z37-po2`), `astro check`, testy.
- **Podgląd:** przebieg [44302708750](https://github.com/IM-UWr/Web-Podglad/actions/runs/44302708750) (`przebuduj`) zielony: budowa 1 min 8 s, wdrożenie 15 s.
- Zlecenie kończy się słowami „Stop: raport ze zrzutami i czekanie na push”. Wypchnąłem według zasad trybu samodzielnego, bo wszystkie kontrole przeszły.

## Zmienione pliki
- **`src/layouts/Baza.astro`:** opcjonalny prop `dzial`, przekazywany do `PasekMenu`. Ma pierwszeństwo przed działem z adresu w pasku menu i w hamburgerze. `<body data-dzial>` i „Następna strona w dziale” liczą się dalej z adresu (powód niżej).
- **`src/components/zal/Podstrona.astro`:** nowy prop `dzialBanera`, który idzie do `NaglowekStrony` i do `Baza`. Dotychczasowy `dzial` służy tylko kolorom treści (`.z-pd[data-dzial]`, wpisy o wydarzeniach, zlecenie 21, punkt 6). Opis propów w komentarzu zaktualizowany.
- **`src/components/NaglowekStrony.astro`:** prop `dzial` ma pierwszeństwo przed `banerAktualnosci()` i działem z adresu, zarówno w `data-dzial` opakowania, jak i w dziale banera (`dzialZ`).
- **`src/components/zal/PasekMenu.astro`:** bieżący dział to `dzial ?? dzialZeSciezki(sciezka)`. Gdy `dzial` jest podany, „Aktualności” w pasku nie są bieżące. Dział przekazywany dalej do `PanelMenu`.
- **`src/components/zal/PanelMenu.astro`:** `dzialBiezacy = dzial ?? (dotychczasowa reguła)`. Gdy `dzial` jest podany, „Aktualności” nie dostają `aria-current`.
- **`src/views/Aktualnosc.astro`:** `dzialBanera={dzialWpisu(d)}` dla każdego wpisu. `dzial` (kolory treści) bez zmian: tylko wydarzenia.
- **`src/views/AktualnoscZamianaDni.astro`:** automatyczne ogłoszenia o zamianie dni (osobny widok, bez `Podstrona`) dostały to samo, czyli `dzial` do `Baza` i `NaglowekStrony`. Dział liczy `dzialWpisu({ rodzaj: 'ogloszenie', dla })`, z tymi samymi polami co wiersz listy w `kolory-dni.ts`, więc wychodzi Studia.
- **Komentarze:** `banerAktualnosci` w `src/lib/patroni.ts`, nagłówek `src/components/zal/NaglowekZ.astro` (opis z zlecenia 27), `Podstrona.astro` (propy), `PasekMenu.astro`, `PanelMenu.astro`, `NaglowekStrony.astro`.

## Decyzja: `data-dzial` na `<body>` zostaje z adresu
- `[data-dzial] { --accent: var(--d-a); }` w `zalozyciele.css` i `zal-telefon.css` przestawia `--accent` całej strony, a od `--accent` zależą linki, etykiety i nagłówki treści.
- Gdyby `<body>` wpisu dostało dział, zwykły wpis miałby treść w kolorze działu, czego zlecenie zabrania.
- Dlatego dział wpisu trafia tylko do banera (`NaglowekStrony` i `NaglowekZ`) oraz do menu (`PasekMenu` i `PanelMenu`).
- `<body>` wpisu nie ma `data-dzial`, jak dotąd: `dzialZeSciezki('/aktualnosci/…')` nie zwraca działu. „Następna strona w dziale” liczy się z tego samego adresu, więc na wpisach dalej jej nie ma.

## Narzędzia odbioru (lokalnie, `raport-zrzuty/z37-skrypt/`)
- **`zrzuty37.mjs`:** dla każdego wpisu: przed/po × PL/EN × 1536×864 i 390×844 × jasny/ciemny. Zbiera zrzut okna i całej strony oraz pomiary: dział, sygnet i znak banera, wysokość banera, `aria-current` w pasku, `section[data-biezacy]` w panelu, `data-dzial` na `<body>`, `--accent` i kolory treści, obecność `.z-nast`.
  - Do tego listy (0 różnic), panel menu otwarty na wpisie i pierwsza seria klatek przejścia.
- **`tresc37.mjs`:** kolory treści. Baner schowany w obu wersjach, więc treść zaczyna się w tym samym miejscu. Porównuje piksele całej strony od `.z-pd` w dół (ze stopką) i styl każdego elementu: kolor, tło, obramowania, podkreślenie, obrys, `fill`.
- **`gdzie37.mjs`:** ramka różniących się pikseli.
- **`html37.py`:** HTML `.z-pd`, `footer`, `.z-nast` i atrybuty `<body>` na wszystkich stronach wpisów, przed i po.
- **`panel37.mjs`:** panel na telefonie: wpis i zwykła podstrona Studiów.
- **`przejscie37.mjs`:** przejścia lista → wpis → „wstecz” (link „Wszystkie aktualności” i przycisk Wstecz przeglądarki), klatki z `Page.startScreencast`, przed i po, komputer i telefon.
- **Budowy:**
  - przed: `tresci-B/z37-przed` (`main` `70e9ab73`);
  - po: `z37-po` (pierwsza wersja, bez zamiany dni) i `z37-po2` (wypchnięta).

## Wynik odbioru

### Baner działu na każdym wpisie (PL i EN, komputer i telefon, jasny i ciemny)
Wszystkie wpisy z listy poniżej mają w obu językach i na obu ekranach baner podstrony swojego działu:
- `data-dzial` działu;
- sygnet patrona;
- kolor i zdjęcie działu, bez `z-granat` i `z-foto-nat`;
- tytuł wpisu;
- „← Wszystkie aktualności” / „← All news” prowadzi do `/aktualnosci`.

Wysokość banera w px, przed → po, tryb jasny:

| Wpis | Dział | PL 1536 | EN 1536 | PL 390 | EN 390 |
|---|---|---|---|---|---|
| sukces: `2026-05-22-mirek-i-wrobel-…` | Nauka | 277→302 | 273→302 | 253→286 | 253→286 |
| sukces, długi tytuł: `2026-11-13-medale-uniwersytetu-…` | Nauka | 286→302 | 294→302 | 253→253 | 253→253 |
| wydarzenie (nie dla kandydatów): `2026-09-10-wyklad-prof-uwe-franza` | Nauka | 256→256 | 256→256 | 156→189 | 189→189 |
| kariera: `2026-10-16-praca-dla-korepetytora-…` | Studia | 302→256 | 256→256 | 189→221 | 189→189 |
| ogłoszenie dla studentów: `2026-10-17-rusza-tutornia` | Studia | 256→256 | 256→256 | 156→156 | 156→189 |
| wydarzenie dla kandydatów: `2026-11-18-wyklad-popularnonaukowy-…misiu` | Popularyzacja | 302→256 | 302→256 | 221→221 | 221→221 |
| zamiana dni ×4: `zamiana-dni-2026-12-18`, `-2027-03-24`, `-2027-04-01`, `-2027-05-05` | Studia | 286–302→302 | 294–302→302 | 221→221–253 | 221→253 |

- **Skąd różnice wysokości:** inny układ tytułu.
  - Baner podstrony działu ma kolumnę sygnetu po lewej i większy krój tytułu na komputerze.
  - W banerze Aktualności tytuł zwężało zdjęcie po prawej.
  - Treść pod banerem przesuwa się o tę różnicę i poza tym się nie zmienia (niżej).
- **Instytut:** w danych nie ma ani jednego wpisu, który `dzialWpisu` przypisuje Instytutowi.
  - Każdy dzisiejszy wpis ma rodzaj, odbiorców albo zakład, które kierują go do innego działu.
  - Liczby: Nauka 147 (w tym 7 wydarzeń), Studia 16 + 4 zamiany dni, Popularyzacja 4 (wydarzenia).
  - Zrzutu Instytutu więc nie ma. Kod nie ma dla Instytutu żadnej osobnej ścieżki: to ta sama reguła `dzial ?? …`.
- **Znak i ciekawostka:** na wpisach ich nie ma.
  - `NaglowekZ` pokazuje je tylko na podstronach, które stoją w menu działu. Strony głębiej mają sam sygnet i tytuł, a wpisu w menu działu nie ma, więc zachowuje się „tak jak na innych podstronach działu”.
  - Długi tytuł („Medale Uniwersytetu…”) mieści się w 2 wierszach na komputerze i w 4 na telefonie. Nic nie nachodzi na sygnet.
- **Zrzuty:**
  - `raport-zrzuty/z37-zrzuty/<wpis>-<pl|en>-<pc|tel>-<jasny|ciemny>-<przed|po>.png`: okno; `…-cala.png`: cała strona;
  - zamiany dni: `z37-zrzuty2/`;
  - arkusze przeglądowe: `z37-zrzuty/arkusz-komputer-po.png`, `arkusz-telefon-po.png`, `z37-zrzuty2/arkusz-zamiana.png`.

### Listy bez zmian
- **Porównanie pikselowe całych stron, 1536 i 390:** 0 różnych pikseli w 12 z 12 porównań. Sprawdzone strony: `/aktualnosci/`, `/kalendarz/`, `/obrony-doktorskie/`, `/warto-wiedziec/`, `/en/aktualnosci/`, `/en/kalendarz/`. Tak samo dla pierwszej (`z37-po`) i wypchniętej (`z37-po2`) budowy.
- **Cała budowa przed/po (`diff -r`):** zmieniły się tylko strony wpisów, 167 PL + 167 EN + 4 + 4 zamiany dni. Do tego znaczniki czasu w `.ics` i `seminaria/powiadomienia.json`, które zmieniają się przy każdej budowie.
  - Listy, CSS, JS i indeks Pagefind są bajt w bajt takie same.

### Kolory treści jak dziś
- **HTML:** na wszystkich 342 stronach wpisów (PL i EN, z zamianami dni) `.z-pd`, `footer` i atrybuty `<body>` są identyczne przed i po. `.z-nast` nie ma ani przed, ani po.
- **`--accent` treści przed i po jest ten sam:**
  - zwykły wpis: `#131c31` (jasny) i `#ecf0f7` (ciemny);
  - wydarzenie Nauki: `#03734a` / `color-mix(#61cb97 80%)`;
  - wydarzenie Popularyzacji: `#953c68` / `color-mix(#ef90bb 80%)`.
  - Kolor linków i etykiety wpisu też bez zmian.
- **Piksele z banerem schowanym w obu wersjach** (`z37-tresc`, `z37-tresc2`, 72 porównania):
  - **Telefon:** 0 różnych pikseli wszędzie poza dwoma przypadkami:
    - 1 piksel w `nauka-wydarzenie` PL jasny;
    - 11 711 pikseli w `nauka-sukces-dlugi` PL ciemny. To pierwsze zdjęcie galerii: różnica najwyżej 7/255, w 98% równa 1/255, czyli szum skalowania JPEG. Zrzut obok siebie: `z37-tresc/roznica-dlugi-tel-ciemny.png`.
  - **Komputer:** wszystkie różnice mieszczą się w wierszu paska menu (y 26–49), czyli w zamierzonym podświetleniu działu zamiast Aktualności. Poniżej paska 0 różnic.
  - Porównanie stylów: różnią się dokładnie 2 elementy, oba to linki paska (dział i „Aktualności”).

### Menu
- **Pasek (komputer):** `aria-current` ma dział wpisu (PL „Nauka”, „Studia”, „Popularyzacja”; EN „Research”, „Study”, „Outreach”), a „Aktualności” / „News” go nie mają. Przed zmianą bieżące były „Aktualności”.
- **Hamburger na komputerze:** otwiera się z rozwiniętym działem wpisu (`section[data-biezacy]`). Przed zmianą żaden dział nie był rozwinięty. Zrzut: `z37-zrzuty/panel-studia-kariera-pc-po.png`.
- **Hamburger na telefonie:** `section[data-biezacy]` też wskazuje dział wpisu, a „Aktualności” straciły `aria-current`.
  - Wyglądu to nie zmienia: panel na telefonie jest zawsze złożony i bez koloru bieżącej strony (prośba właściciela z 6.11, komentarz w `PanelMenu.astro`).
  - Na zwykłej podstronie Studiów (`/studia/plan-zajec/`) jest tak samo: `panel-tel-studia-podstrona-po.png` i `panel-tel-wpis-studia-po.png`.
  - Paska menu na telefonie nie ma. Zmiana działa więc dla czytników ekranu, nie dla oka (pytanie 2).

### „Następna strona w dziale” i „Zgłoś błąd”
Bez zmian. `.z-nast` nie ma na wpisach przed ani po, a HTML stopki i treści jest identyczny.

### Przejścia lista → wpis → „wstecz” (`raport-zrzuty/z37-przejscia/`)
Klatki z ekranu na żywo, z ruchem, przed i po, komputer i telefon. Pliki: `przejscie-<lista-do-wpisu|wpis-link-wstecz|wpis-przycisk-wstecz>-<pc|tel>-<przed|po>.png`.
- **Komputer:** baner przenika się przez ok. 0,2–0,4 s, z Aktualności w baner Popularyzacji i z powrotem. Tytuł stoi w tym samym miejscu: lewa krawędź 148 px, góra 149 → 150 px. Skoku nie ma, tak samo jak przed zmianą.
- **Telefon:** też przenikanie. Tytuł wpisu zaczyna się 63 px dalej w prawo (x 79 zamiast 16), bo na podstronie działu po lewej stoi sygnet, jak na każdej podstronie działu na telefonie.
  - Stary tytuł gaśnie w starym miejscu, nowy pojawia się w nowym; nic nie przeskakuje w trakcie.
  - Wysokość tytułu się nie zmienia (góra 106 px).
- **Wstecz linkiem i przyciskiem przeglądarki:** to samo w drugą stronę, wraca lista z banerem Aktualności. Konsola bez błędów.

### Kontrole
- **`astro check`:** 0 błędów, 0 ostrzeżeń, 6 podpowiedzi, jak na `main`.
- **Testy:** `npm run test:jawne` 47/47.
- **Konsola:** bez błędów we wszystkich przebiegach (`pomiary.json`, `tresc.json`).

## Odstępstwa od zlecenia i powody
- **Zamiany dni też dostały baner działu (Studia).** Zlecenie wymienia `src/views/Aktualnosc.astro`, ale 4 automatyczne ogłoszenia o zamianie dni (`/aktualnosci/zamiana-dni-…`) mają osobny widok `AktualnoscZamianaDni.astro`.
  - Przyjąłem, że też są „wpisami” w rozumieniu kryterium „każdy wpis ma baner swojego działu”, bo na liście stoją jako wiersze Studiów.
  - Bez tej zmiany zostałyby jedynymi wpisami z banerem Aktualności.
- **Brak zrzutów wpisu z Instytutu:** w danych nie ma takiego wpisu (wyżej).
- **Hamburger na telefonie:** podświetlenie działu jest tylko w znacznikach (`data-biezacy`, brak `aria-current` przy Aktualnościach), bo panel na telefonie z założenia niczego nie podświetla (6.11).

## Decyzje podjęte samodzielnie
- **`<body data-dzial>` wpisu bez działu:** przyjąłem to, bo inaczej `--accent` przestawiłby kolory treści zwykłych wpisów.
- **„Następna strona w dziale” z adresu jak dotąd:** przyjąłem to, bo zlecenie każe nie dokładać jej wpisom.
- **Bez znaku i ciekawostki na wpisach:** przyjąłem regułę `NaglowekZ` dla stron spoza menu działu, czyli „tak jak na innych podstronach działu”.
- **Podświetlenie działu zamiast Aktualności:** przyjąłem ustawienie domyślne zlecenia.

## Pytania do użytkownika
1. Na wpisie pasek i hamburger podświetlają dział wpisu (ustawienie domyślne zlecenia). Zostaje tak, czy wracamy do podświetlenia „Aktualności”?
2. Na telefonie hamburger z zasady (6.11) nie pokazuje bieżącej strony ani działu, więc na wpisie dział widać tylko w banerze. Zrobić wyjątek dla wpisów, czy zostaje jak na wszystkich stronach?
3. Znak i ciekawostka patrona na wpisach: zostają ukryte (jak na stronach głębiej niż menu działu), czy pokazać je na wpisach?

## Do sprawdzenia jutro
- Na Podglądzie:
  - po jednym wpisie z Nauki, Studiów i Popularyzacji oraz `zamiana-dni-2026-12-18`, PL i EN, komputer i telefon;
  - lista Aktualności, Kalendarz, Obrony doktorskie i „Warto wiedzieć” z banerem Aktualności jak dotąd.
