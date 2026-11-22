# Raport: zlecenie 57, lista obron doktorskich według lat (22.11.2026)

Gałąź robocza `praca/57-obrony-lata` (lokalna) od `main` = `edbd51de`. Treści pobrane na start `pobierz_tresci.py` (52 obrony, Web-Aktualnosci `637dd618`). Pracowałem bez subagentów. Push według poleceń właściciela z 22.11: „po zakończeniu automatyczny push” (szczegóły na końcu).

## Co zmieniłem

| Plik | Zmiana |
|---|---|
| `src/views/ListaObron.astro` | Nowy układ jak w `ListaKonferencji.astro`: `Podstrona` ze spisem, `dzial="nauka"`, klasa `tresc z-ob`, bez `ListaPokaz` i bez ramki `z-pd-pelna`. Tekst nad listą jest pierwszą sekcją (`p.wst`). `section#z-nadchodzace` („Nadchodzące” / „Upcoming”) zawiera obrony od najbliższej, a gdy ich nie ma, napis „Nie zapowiedziano jeszcze kolejnych obron.” / „No upcoming defences announced.”. `section#z-odbyte` („Odbyte” / „Past”) ma rok jako `h3#rok-RRRR` + `sr-only ", "` + `<small>` z liczbą w odmianie. Spis: Nadchodzące i lata z danych. Skrypt starych adresów `?rok=`. Nowy komentarz na górze pliku. Usunięte: panel „Pokaż”, skrypt filtra, „Brak obron spełniających…”, link „Archiwum starej strony”. |
| `src/lib/widoki/listaObron.ts` | Zwraca `przyszle`, `lata: { rok, lista }[]` (odbyte w grupach, lata od najnowszego, w roku od najnowszej), teksty strony z `{ wst: true }`. Nie zwraca już `odbyte` (płaskiej listy) ani `ustawienia`. |
| `src/components/WierszWydarzenia.astro` | `poziom` przyjmuje też `'h4'`. Do tego komentarz o filtrze, który był na liście obron. HTML innych użyć bez zmian (patrz niżej). |
| `src/lib/i18n.ts` | Usunięte nieużywane klucze `nadchodzaceObrony`, `odbyteObrony`, `archiwumObron` (PL i EN). Klucz `archiwum` i `ustawienia.archiwum` zostają, bo używa ich strona 404 i lista Aktualności. |

### Szczegóły rozwiązania
- **Rok (h3):** krój, stopień, kolor i liczba (`small`) jak w Konferencjach (`.tresc h3` i ta sama reguła `h3 small`). Jak w zaakceptowanym prototypie: pod rokiem cienka kreska (`padding-bottom: 6px; border-bottom`), od której zaczynają się wiersze, a `h2` sekcji bez dolnego marginesu. Napis pustych Nadchodzących ma margines z prototypu (`10px 0 0`).
- **Nagłówki wierszy:** pod rokiem `h4` (jak w zleceniu). Pod „Nadchodzące” nie ma roku, więc wiersz ma `h3` (bezpośrednio pod `h2`, bez przeskoku poziomu). Wygląd obu jest ten sam, co potwierdza porównanie stylów.
- **`.tresc` a wiersz:** reguła `.tresc a` dokładała linkowi kandydata przejście koloru. Bez ustawienia „ogranicz ruch” wiersz po najechaniu podświetlałby się płynnie, a wcześniej zmieniał kolor od razu. Dokładała też `text-underline-offset`. Zerowanie: `.ob-sek :global(.ww-t a) { transition: initial; text-underline-offset: initial }`, na telefonie offset `3px` jak `main a` w `telefon.css`. Akapity, marginesy, `max-width` i `h4` wiersz ustawia sam (reguły z wyższą swoistością), więc `.tresc` ich nie zmienia.
- **`?rok=RRRR`:** skrypt usuwa `?rok` z adresu (`history.replaceState`) i przewija do `#rok-RRRR` tak jak spis: nagłówek staje na wysokości `scroll-margin-top` (20 px na komputerze, wysokość paska + 16 px na telefonie). Kotwicę dopisuje do adresu dopiero po `load`. Wcześniej przeglądarka sama przewijała do kotwicy z adresu i doliczała drugi raz `scroll-padding-top` z `html`, co dawało nagłówek o 79 px niżej. Po wczytaniu krojów i strony skrypt poprawia położenie, jeśli nikt jeszcze nie przewijał. Rok nieznany albo nie-liczba: góra strony, w adresie zostaje sama ścieżka. Inne parametry i kotwica nie są ruszane. Bez JS widać całą stronę.

## Sprawdzenie

Narzędzia w `raport-zrzuty/z57-skrypt/` (Edge przez Playwright, serwer plików `serwer57.mjs` na portach 4371–4374). Wyniki w `raport-zrzuty/z57-*.json`, zrzuty w `raport-zrzuty/z57-zrzuty/`.

### Cały `dist` przed i po (treści z `main`)
- HTML różni się tylko w `obrony-doktorskie/index.html` i `en/obrony-doktorskie/index.html`. Wszystkie inne strony są identyczne bajt w bajt, w tym Kalendarz (PL i EN), wpisy Aktualności z „Najbliższymi wydarzeniami”, strony obron i strona Nauki z licznikiem doktoratów. Inne użycia `WierszWydarzenia` mają więc ten sam HTML, a znacznik `data-astro-cid` się nie zmienił.
- `_astro/`: znika tylko skrypt filtra `ListaObron…CgNvWbYc.js`. Nowy skrypt `?rok` jest wpisany w stronę, inne pliki CSS/JS są identyczne.
- 154 pliki `.ics` różnią się tylko `DTSTAMP`, a `seminaria/powiadomienia.json` tylko polem `wygenerowano`. `sitemap.xml` jest identyczny.
- Pagefind: 463 strony PL i 463 EN, przed i po tyle samo. 11 zapytań (m.in. „obrony doktorskie”, „Mrowińska”, „Dołęga”, „promotor”, „PhD defences”, „supervisor”) daje te same adresy wyników (`z57-szukaj.json`).

### Strona po zmianie
- Spis PL: Nadchodzące, 2026, 2025, …, 2013 (15 pozycji), w EN „Upcoming”. Lata i liczby: 2026 — 8 obron, 2025 — 4 obrony, 2024 — 4 obrony, 2023 — 3 obrony, 2022 — 2 obrony, 2021 — 2 obrony, 2020 — 1 obrona, 2019 — 4 obrony, 2018 — 8 obron, 2017 — 3 obrony, 2016 — 2 obrony, 2015 — 5 obron, 2014 — 5 obron, 2013 — 1 obrona. W EN „1 defence / 8 defences”. W sumie 52 wiersze (`h4`).
- Nadchodzące: pusta sekcja z napisem PL/EN. Z 3 testowymi obronami w nakładce (3.12.2026, 15.12.2026, 20.01.2027; jedna z dwoma promotorami, jedna z polskim tytułem) kolejność jest od najbliższej, a linia „Promotor:/Promotorzy:” jest poprawna (zrzuty `z57-test-*`). Nakładka przywrócona: testowe pliki usunięte, `pobierz_tresci.py`, 52 obrony.

### Style wiersza (`getComputedStyle`, `z57-styl-wiersza*.json`)
Każdy wiersz (klucz: adres obrony) przed i po, w nim 10 elementów: wiersz, data, „mie rrrr”, etykieta, kandydat, link kandydata, nakładka `::before`, tytuł rozprawy, promotor i „Promotor:”. Wszystkie własności poza szerokością i wysokością. PL i EN, 1920, 1440, 1024 i 390 px, jasny i ciemny, z „ogranicz ruch” i bez niego.
- Data, etykieta, kandydat (`h4` po wobec `h3` przed), link, nakładka, tytuł, promotor i „Promotor:” mają 0 różnic we wszystkich 16 wariantach. Z danymi testowymi to samo, także dla wierszy nadchodzących (`h3`).
- Jedyna różnica: sam `article.ww` dziedziczy po `.tresc` stopień 17 px i interlinię 1,68 (wcześniej 16 px i 1,5). Nie ma on własnego tekstu, bo wszystkie jego elementy mają własny stopień i interlinię, więc wygląd się nie zmienia.
- Kolor kandydata po najechaniu na wiersz: przed i po `rgb(3, 115, 74)`, kursor `pointer`.

### Spis, klawiatura, `?rok` (`z57-spis*.json`)
- **Mysz** (1440 i 1920, PL i EN, płynne przewijanie): klik w każdą pozycję przewija nagłówek na `scroll-margin-top` (±2 px), oznacza pozycję i ustawia na niej znacznik. Wynik: 15/15 przy 1440. Przy 1920: 14/15, bo strona przewija się do końca już po kliku w 2014, a wtedy klik w 2013 nic nie przewija i znacznik zostaje na 2014. Tak samo zachowują się dziś Konferencje (przed i po zmianie), patrz uwagi.
- **Klawiatura:** fokus na „2019” i Enter przewijają do roku i przenoszą fokus na `h3#rok-2019`. Tab przechodzi do pierwszej obrony z 2019. To samo dla 2014.
- **Kółko:** 19 kroków od góry do dołu, znacznik zawsze na bieżącym roku (0 błędów). Odwiedza Nadchodzące, 2026…2013, z wyjątkiem 2021, który przy kroku 400 px przelatuje.
- **`?rok`:** `?rok=2015` ląduje na `#rok-2015` (h3 na 20 px przy 1440, na 77 px przy 390, czyli na wysokości `scroll-margin-top`). `?rok=2013` ląduje na dole strony z kotwicą. `?rok=1999` i `?rok=abc` zostają na górze (scrollY 0), a adres to sama ścieżka. W adresie nigdzie nie zostaje `?rok`. Sprawdzone dla PL i EN, przy 1440 i 390.
- **Bez JS** (`?rok=2015`): 52 wiersze, 14 lat, góra strony.
- **Konsola:** 0 błędów i ostrzeżeń we wszystkich przebiegach.

### Zrzuty (`raport-zrzuty/z57-zrzuty/`)
- `z57-obok-<pl|en>-<1920|1440|1024|390>-<light|dark>-<gora|nadchodzace|przejscie|koniec>.png`: obrony z lewej, Konferencje z prawej, w tych samych miejscach (64 zestawienia). „przejscie” to drugi rok spisu (obrony: 2025) na 40% wysokości okna, „koniec” to ostatni rok (2013) na 30% okna.
- `z57-test-obok-…`: to samo z 3 testowymi nadchodzącymi obronami.
- Pojedyncze zrzuty: `z57[-test]-<obrony|konferencje>-<pl|en>-…png`.
- Na telefonie spis jest schowany tak samo jak w Konferencjach (zlecenie 18, punkt 18). Przy 1024 px spis stoi z prawej jak w Konferencjach.

### Kontrole
- `npm run build`: bez błędów.
- `astro check`: 0 błędów, 0 ostrzeżeń, 8 podpowiedzi. Te same co przed zmianą, w innych plikach (`Sekcja.astro`, `stanBudowy/klient.js`).
- `sprawdz_tresci.py`: OK (641 plików, 106 ciekawostek).
- Repozytoria treści: bez zmian. W Web-Core zmienione tylko 4 pliki kodu.

## Odstępstwa od zlecenia i decyzje
- **Kreska pod rokiem i zerowy dolny margines `h2`:** wzięte z zaakceptowanego prototypu. Zlecenie mówi „styl roku i liczby jak h3/small w Konferencjach”: krój, stopień, kolor i liczba są te same, a kreska oddziela rok od pierwszego wiersza jak w prototypie.
- **Wiersze nadchodzące mają `h3`, nie `h4`:** stoją bezpośrednio pod `h2`, bez roku. Wygląd jest ten sam.
- **Dodatkowe zerowanie dwóch reguł `.tresc a` na linku wiersza:** potrzebne, żeby wiersz zachowywał się jak dawniej (wyżej).

## Uwagi dla właściciela (poza zakresem, bez zmian)
1. **Tytuł rozprawy zawsze jako angielski:** `lang="en"` w `WierszWydarzenia.astro` dla `rodzaj === 'obrona'`, w `obrona.ts` i w banerze strony obrony. Według zlecenia ok. 34 tytuły archiwalne są po polsku; moja zgrubna heurystyka (polskie znaki i spójniki) liczy 33 z 52 (np. „Silne symplektyczne foldy…”, „Oszacowania jąder całkowych”). Czytnik ekranu przeczyta je z angielską wymową.
2. **Dopisek „(promotor pomocniczy)” / „(kopromotor)”** zostaje po polsku na stronach EN (np. „Supervisors: Dr hab. Jan Dymara, Dr Damian Osajda (promotor pomocniczy)”).
3. **Spis „Na tej stronie”, ostatnia pozycja** (wspólny `SpisStrony.astro`, dotyczy wszystkich podstron ze spisem, także Konferencji): gdy strona jest już przewinięta do końca, klik w ostatnią pozycję nie przewija, więc znacznik zostaje na poprzedniej. Poprawka to jedna linia (`zaplanuj()` po ustawieniu `wybrana` w obsłudze kliknięcia), ale zmienia JS wszystkich podstron, więc jej nie robiłem.
4. **Wejście wprost na `…#rok-RRRR`** (link z innej strony, bez `?rok`): przeglądarka sama przewija do kotwicy i dolicza `scroll-padding-top` z `html` oraz `scroll-margin-top` nagłówka. Rok staje ok. 80 px niżej niż po kliknięciu w spis. Tak jest na całej stronie (np. Konferencje); skrypt `?rok` tego nie dotyczy.

## Push
Według polecenia właściciela z 22.11 („po zakończeniu automatyczny push”): commit `03a684ad` na `praca/57-obrony-lata` (gałąź tylko lokalnie), `git pull --rebase` na `main` (bez nowych zmian od startu), fast-forward i push tylko Web-Core: `edbd51de..03a684ad` o 14:33. Przekaźnik do Web-Podglad (przebieg 45028141727) ruszył; wyniku budowy Podglądu nie sprawdzałem.
