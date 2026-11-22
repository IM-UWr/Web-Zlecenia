# Raport: zlecenie 45, Tutornia (wersja z 18.11, 18:33: oś godzin z grafiku)

**Status (19:52):** **wypchnięte** na polecenie „Push”: Web-Core, pięć repozytoriów treści i PDF „Mapa CMS”. Podgląd zielony, strona sprawdzona na żywo. Szczegóły w sekcji „Push (18.11, 19:41–19:50)”. Zostaje jutrzejszy przegląd zapisów redaktorów i dwa pytania na końcu.

| Repozytorium | Gałąź lokalna | Commit(y) | Baza |
|---|---|---|---|
| Web-Core (worktree `Web-Core-B`) | `praca/45-tutornia` | `3cde30e0` | `02a2e8aa` |
| Web-Studia (`tresci-B`) | `praca/45-tutornia` | `e7e297e` | origin/main z klonu |
| Web-Ustawienia | `praca/45-tutornia` | `2ea29fc`, `fb4bbfc` (podtytuł) | jw. |
| Web-Instytut | `praca/45-tutornia` | `013024d` | jw. |
| Web-Nauka | `praca/45-tutornia` | `51626f2` | jw. |
| Web-Popularyzacja | `praca/45-tutornia` | `aed9148` | jw. |

Ostateczna budowa: `tresci-B/z45-po7` (kod = commit `3cde30e0`, nakładka = klony z tabeli). Budowa „przed”: `tresci-B/z45-przed` (te same klony na origin/main).

## Co jest zrobione

**Strona `/studia/tutornia` (PL i EN)**, plik `Web-Studia/src/content/strony/studia/tutornia.md` = załącznik A zlecenia (sprawdzone znak w znak):
- baner w kolorze Studiów: hasło, liczby (tutorów, dyżurów w tygodniu, sala) liczone z grafiku;
- ramka „Teraz” (kółko z inicjałami, etykieta z datą i godziną, tytuł, opis) — 9 stanów: teraz, wkrótce, dziś, koniec, weekend, wolne (z „wraca …”), przed startem, po semestrze, brak;
- siatka tygodnia na komputerze, lista dni na telefonie; „dziś”, linia „teraz”, minione dyżury przygaszone, znacznik „teraz”;
- `:::pary` („Gdzie i jak”), `:::linki` („Inne formy pomocy”);
- bez JavaScriptu: neutralne teksty („Sala 202 · dyżury według planu poniżej”, kafelek „sala 202”).

**Blok `:::grafik`** (`src/lib/grafik.mjs`, `src/components/grafik/`, `src/scripts/grafik.ts`):
- jedna linia = jeden dyżur (`- pon. 12:15–14:00 **Imię Nazwisko** — przedmioty`), pola `Sala:`, `Od:`, `Do:`;
- pusty blok w Treści EN bierze grafik z wersji polskiej;
- złe linie pomija, a na Podglądzie pokazuje czerwoną ramkę z numerem linii i powodem (na stronie publicznej ramki nie ma: `TYLKO_OPUBLIKOWANE`);
- **oś godzin z grafiku** (zmiana z 18:33): zakres od najwcześniejszego startu do najpóźniejszego końca (co 5 min), etykiety i linie na każdym różnym starcie, etykieta na końcu; w lukach ponad 90 min pełne godziny co najmniej 30 min od sąsiednich etykiet.

**Oś — testy ze zlecenia** (`src/plugins/grafik.test.mjs`, w `npm run test:jawne`):

| Grafik | Oś |
|---|---|
| A (dzisiejszy) | 12:15 13:15 14:15 15:15 16:15 17:00 |
| + pt. 9:00–10:30, pon. 16:15–18:00 | 9:00 10:00 11:00 12:15 … 16:15 17:00 18:00 |
| z 10:40–11:20 | 10:40 12:15 … (bez 11:00 i 12:00) |
| luka dokładnie 90 min / 120 min / pusty grafik | bez dodanej godziny / 10:00 / pusta oś |

Wariant z luką zbudowany naprawdę (budowa testowa `z45-test2`): oś 9:00 10:00 11:00 12:15 13:15 14:15 15:15 16:15 17:00 18:00 — zrzuty `z45-test-luka-1920.png`, `-siatka.png`, `-390.png`, `-en.png`.

**Reszta zlecenia:**
- **menu** „Na co dzień”: piąty link Tutornia (Web-Ustawienia `nawigacja.json`);
- **podtytuł grupy** (prośba właściciela w trakcie zlecenia): „zajęcia, kalendarz, pierwszy rok, tutornia” / EN „classes, calendar, first year, tutoring” — pomiar niżej;
- **Szybki dostęp**: piąty kafelek Tutornia po Seminariach z podpisem na żywo („teraz: Jacek Kowalski, do 16:00” z kropką, „od 14:15: …”, „jutro od 13:15 · sala 202”, „nieczynna, wraca 16 lis”, „rusza 19 paź” …); układ pięciu kafelków na każdej szerokości;
- **„W skrócie”**: nowe opcjonalne pole `adres` (Studia, Instytut, Nauka, Popularyzacja); na Studiach „Tutornia →” prowadzi do strony;
- **ciekawostka** „Seminarium w salonie”: `stan: przypieta`, `strona: /studia/tutornia`, dalej `ukryta: true` — na zwykłej budowie Tutornia losuje inne (sprawdzone 5 wczytań), po zdjęciu `ukryta` pokazuje się na Tutorni (budowa testowa, `z45-test-ciekawostka-*.png`);
- **linki** w Pierwszym roku (PL 2, EN 2) i Sprawach studenckich (PL 1, EN 1): z aktualności „Rusza tutornia” na `/studia/tutornia`;
- **dokumentacja**: `dok/jawny-markdown.md` (rozdział „Grafik dyżurów i pary”), `dok/sciagawka-edytora.md`, `dok/zasady-parsera.md`, `dok/dla-redaktorow/mapa-cms.html` (PDF próbnie: 2 strony, zapas 16/14 px); opisy pól Treść/Treść EN w `Web-Studia/.pages.yml`;
- **`sprawdz_tresci.py`**: ostrzega o złych liniach grafiku (np. `…tutornia.md: Treść, blok :::grafik, linia 17 („środa 25:00–26:00 **Ktoś**”): nie widzę dnia i godzin … — tej linii nie będzie w planie`). Używa parsera z `src/lib/grafik.mjs` przez Node (zamiast drugiej kopii w Pythonie); bez Node ostrzega, że kontrolę pominięto.

## Poprawki w trakcie odbioru

- **Podwójna kreska pod ramką „Teraz”**: Astro wstawia `<script>` między ramkę i pierwszy `##`; reguła obejmuje `.tu-teraz + script + h2`.
- **Wąskie kolumny (komputer ok. 1024–1280 px)**: znacznik „teraz” nachodził na godzinę i nazwisko, długie nazwiska ucinały się w poziomie, w krótkich dyżurach (45 min) przedmioty urywały się w pół linii. Teraz (kontener `.tu-dyz` poniżej 140 px): „teraz” w osobnej linii nad godziną, nazwisko 14 px z łamaniem, w krótkim dyżurze samo nazwisko. Sprawdzone automatycznie dla 10 szerokości × 3 chwil, PL i EN: 0 nachodzeń, 0 ucięć. Jedyne łamanie w środku słowa: „Programowanie” przy 1024–1050 px.
- **Ramka błędów**: lista szła wąsko (max-width prozy) z wcięciem; teraz na całą szerokość (`z45-test-ramka-bledu.png`).
- **`astro check`**: 4 błędy typów w `src/scripts/grafik.ts` (wynik `stanGrafiku` bez `etykieta` w obiekcie początkowym, `dzisPlan` mogło być `undefined`) — poprawione w `grafik.mjs`, bez zmiany działania.

## Podtytuł „Na co dzień” — pomiar

Podtytuł jest tylko na komputerze (na telefonie karty go nie pokazują). Szerokość tekstu w jednej linii i miejsce na karcie:

| Szerokość okna | miejsce | PL „zajęcia, kalendarz, pierwszy rok, tutornia” (250 px) | EN „classes, calendar, first year, tutoring” (223 px) |
|---|---|---|---|
| 1920, 1536, 1366 | 280 px | 1 linia | 1 linia |
| 1280 | 260 px | 1 linia | 1 linia |
| 1180 | 237 px | 2 linie | 1 linia |
| 1100 | 219 px | 2 linie | 2 linie |
| 1024 | 202 px | 2 linie | 2 linie |

PL mieści się w jednej linii od ok. 1240 px. Poniżej łamie się tak jak dziś sąsiednie karty: „egzaminy, dyplom, wnioski, wyjazdy” ma 2 linie już przy 1100 px, a przy 1024 px wszystkie trzy karty mają po 2 linie. Dzisiejszy tekst „plan, kalendarz, zajęcia, pierwszy rok” mieścił się od ok. 1140 px. Zrzut: `z45-studia-na-co-dzien-komputer.png` (1536 px, jedna linia).

## Odbiór lokalny

**Porównanie HTML przed/po** (całe `dist`, PL i EN; `raport-zrzuty/z45-html.txt`): 795 → 797 stron, nowe tylko `studia/tutornia` i `en/studia/tutornia`; różne 793 pliki w 28 grupach:
- dozwolone: menu (link Tutornia na każdej stronie), strona Studiów (karta „Na co dzień”: podtytuł, „5 stron”, link Tutornia; „W skrócie” z linkiem), strona główna (piąty kafelek), linki w Pierwszym roku i Sprawach studenckich (PL i EN), `sitemap.xml`;
- **poza listą, wynikające ze zmian** (proszę o akceptację):
  1. **arkusz grafiku na stronach typu Strona**: Astro łączy CSS na trasę `[...slug]`, więc 62 pozostałe Strony (np. Deklaracja dostępności, Infrastruktura informatyczna, strony Studiów) wczytują dodatkowy plik `_slug_.*.css` (9,6 KB) ze stylami `.tu-*`. Reguły dotyczą tylko elementów grafiku: porównanie pikseli 4 takich stron przed/po (stałe losowanie) — 3 identyczne, czwarta różni się tylko ciekawostką (pkt 2);
  2. **ciekawostka z budowania na 10 stronach Studiów** (Egzaminy i dyplom, Procedura dyplomowania, Program MOST, Skrypty, Sprawy studenckie; PL i EN): w danych losowania doszła strona Tutorni, więc stała ciekawostka zapisana w HTML (widoczna tylko bez JavaScriptu) jest inna. Losowanie w przeglądarce działa jak dotąd;
  3. **„Następna strona w dziale”** na Pierwszym roku prowadzi teraz do Tutorni (kolejność z menu), a z Tutorni do Egzaminów i dyplomu;
  4. `seminaria/powiadomienia.json`: tylko znacznik czasu budowy.

**12 stanów na żywo** (ostateczna budowa, 1536 × 864 ramka i siatka, 1920 × 950 kafelek; zrzuty `z45-stan-NN-*-{ramka,siatka,kafelek}.png`, 0 błędów konsoli):

| Chwila | Ramka | Przygaszone | Kafelek |
|---|---|---|---|
| śr. 18.11 14:55 | Teraz dyżuruje Jacek Kowalski | 6 | teraz: Jacek Kowalski, do 16:00 • |
| śr. 18.11 13:00 | Teraz dyżuruje Jakub Abramek | 5 | teraz: Jakub Abramek, do 14:00 • |
| śr. 18.11 16:51 | Na dziś to wszystko | 7 | jutro od 13:15 · sala 202 |
| pon. 23.11 14:05 | Za chwilę: Miłosz Cierkosz | 1 | od 14:15: Miłosz Cierkosz |
| wt. 24.11 9:30 | Dziś od 12:15 | 3 | dziś od 12:15 · sala 202 |
| pt. 20.11 17:30 | Na dziś to wszystko | 10 | pon. od 12:15 · sala 202 |
| sob. 21.11 | W weekend tutornia nie działa | 0 | pon. od 12:15 · sala 202 |
| czw. 12.11 (rektorskie) | Dziś tutornia nieczynna | 7 | nieczynna, wraca 16 lis |
| pt. 18.12 13:00 (plan środy) | Teraz dyżuruje Jakub Abramek | 5 | teraz: Jakub Abramek, do 14:00 • |
| pon. 28.12 (przerwa) | Dziś tutornia nieczynna | 0 | nieczynna, wraca 7 sty |
| pon. 12.10 | Tutornia rusza 19 października | 0 | rusza 19 paź |
| pon. 15.02.2027 | Dyżury w tym semestrze już się skończyły | 0 | sala 202 |

**Zrzuty** (`raport-zrzuty/`; budowa 6, która od ostatecznej różni się tylko poprawką typów w `grafik.mjs` bez zmiany działania; stany na żywo z budowy o HTML identycznym z ostateczną):
- Tutornia: `z45-tutornia-{1920,1536,1366,1024,390}-{jasny,ciemny}.png` (całe strony), EN `z45-tutornia-en-{1536,390}-jasny.png`;
- strona główna: `z45-glowna-{1920,1536,1366,390}.png`, `z45-glowna-1920-ciemny.png`, `z45-glowna-en-1536.png`;
- Studia z otwartym „Na co dzień”: `z45-studia-na-co-dzien-{komputer,telefon,en}.png`;
- bez JavaScriptu: `z45-bez-js-{tutornia,glowna}.png`;
- budowa testowa (luka, zła linia, ciekawostka bez `ukryta`): `z45-test-*.png`.

Strona główna, położenia przed/po: 1920 × 950 i 1536 × 864 bez zmian (kafelki w jednym rzędzie); 1366 × 768 nagłówek „Szybki dostęp” nad kafelkami, pasek 61 → 103 px, „Warto wiedzieć” bez zmian (768 px); telefon 2 × 2 + Tutornia na całą szerokość.

**Kontrole:**
- `npx astro check`: 0 błędów, 0 ostrzeżeń, 5 podpowiedzi (jak na `main`);
- `npm run test:jawne`: 61/61;
- `sprawdz_pola_cms.py ../tresci-B`: 727 plików w 16 repozytoriach, 0 problemów;
- `sprawdz_tresci.py`: OK (568 plików, 106 ciekawostek); na kopii z trzema złymi liniami: 3 ostrzeżenia, kod 0;
- `sprawdz-jawny-markdown.mjs`: OK w Web-Studia, Web-Instytut, Web-Nauka, Web-Popularyzacja, Web-Ustawienia, Web-Aktualnosci;
- **linki**: lychee nie jest zainstalowany na tym komputerze. Zamiast niego własne sprawdzenie plików i kotwic z `.github/qa/qa.py` (to samo, co robi QA w Actions obok lychee): 0 zepsutych linków wewnętrznych przed i po; 11 nieistniejących kotwic — te same 11 przed zmianą (zamiany dni, `#egzamin-magisterski`), żadna nowa;
- konsola: 0 błędów i ostrzeżeń na wszystkich 64 stronach z przebiegów zrzutów.

**Symulacja zapisu w CMS:**
- **formularz** (`skrypty/test-edytora/formularz.mjs ../tresci-B`, `raport-zrzuty/z45-formularz.txt`): 76 scenariuszy OK; zapis bez zmian 727 plików — pliki zlecenia 45 (Tutornia, Pierwszy rok, Sprawy studenckie, `studia.md` z `adres`, `nawigacja.json`, `skroty.json`) bez różnic. Skrypt zgłasza 6 różnic w plikach spoza zlecenia: 5 obron i 1 grant dostają szablon Treści przy pierwszym zapisie. To znane działanie ze zlecenia 40 (raport 40-3); strona liczy taki komentarz jak pustą Treść;
- **edytor TipTap** (etap 6a zlecenia 28, `raport-zrzuty/z45-edytor-tiptap.diff`): gdyby Treść była polem rich-text, zapis usunąłby komentarze wzorcowe i zostawił akapit `&nbsp;` nad „Planem dyżurów” (+73 px i druga kreska; sprawdzone budową). Tak samo dzieje się dziś z Pierwszym rokiem, Sprawami studenckimi i Zajęciami. **Nie dotyczy obecnego CMS**: od zlecenia 40 Treść i Treść EN Stron studiów to pola `code`, zapisywane znak w znak. Niczego w kodzie nie zmieniałem.

## Push (18.11, 19:41–19:50)

Kolejność jak w planie: najpierw Web-Core, potem Web-Studia, Web-Ustawienia i trzy pozostałe repozytoria treści, na końcu PDF. Wszystko zwykłym pushem, bez force, z fetch tuż przed pushem.

| Repozytorium | Push | Godzina | Przebiegi |
|---|---|---|---|
| Web-Core | `02a2e8aa..3cde30e0` (baza bez zmian, rebase pusty) | 19:41 | Przekaźnik `44372472836` zielony → Podgląd `44372512634` zielony |
| Web-Studia | `a8964db..e7e297e` | 19:44 | Podgląd `44373000846` zielony (dwa wcześniejsze przebiegi z 19:44 anulowane, bo zastąpił je nowszy) |
| Web-Ustawienia | `05080a9..fb4bbfc` (`2ea29fc` + `fb4bbfc`) | 19:44 | jw. |
| Web-Instytut | `88d8f50..013024d` | 19:44 | jw. |
| Web-Nauka | `b01f1ec..51626f2` | 19:44 | jw. |
| Web-Popularyzacja | `0993e8e..aed9148` | 19:44 | jw. |
| Web-Podglad (PDF) | `5b4e8f2d..032794f8` `[skip ci]` | 19:50 | bez przebiegu (`[skip ci]`) |

**Kontrole przed pushem:**
- Web-Core po rebase: przebudowa (`tresci-B/z45-push`, poza znacznikami czasu identyczna z `z45-po7`), astro check 0 błędów, `npm run test:jawne` 61/61;
- treści, według „Ochrony zmian redaktorów”: od bazy 0 zapisów redaktorów we wszystkich pięciu repozytoriach (`kontrola_redaktorow.py przed`);
- `sprawdz_pola_cms.py`: 0 błędów;
- `kontrola_redaktorow.py po` (`raport-zrzuty/z45-kontrola-po.txt`) pokazuje wyłącznie zmiany zlecenia 45. Skrypt oznacza je jako „NIEDOZWOLONE”, bo tak oznacza każdą zmianę danych spoza migracji.

**Sprawdzenie na żywo** (Podgląd, 19:46; zrzuty `raport-zrzuty/z45-zywo-*.png`):
- Tutornia (1536 i 390 px, EN 1536): ramka „Na dziś to wszystko”, oś 12:15 … 17:00, grafik jak w budowie lokalnej;
- strona główna (1920): piąty kafelek „Tutornia | jutro od 13:15 · sala 202”;
- Studia (1536): podtytuł „zajęcia, kalendarz, pierwszy rok, tutornia” w jednej linii, link w „W skrócie”;
- 0 błędów konsoli.

**PDF „Mapa CMS”:** wygenerowany z `dok/dla-redaktorow/mapa-cms.html` z `origin/main` (`node skrypty/pdf-dla-redaktorow.mjs`). Ma 2 strony, kontrola skryptu: OK. Strona 1 zawiera Tutornię (`:::grafik`) i „W skrócie (pozycja może mieć link)”. Strona 2 zawiera `:::pary`.

**Do zrobienia jutro (19.11):** przegląd zapisów redaktorów z ostatnich 24 h w Web-Studia, Web-Ustawienia, Web-Instytut, Web-Nauka i Web-Popularyzacja.

## Pytania do właściciela

- Czy akceptujesz trzy różnice spoza listy (arkusz `.tu-*` na Stronach, inna stała ciekawostka bez JS na 10 stronach Studiów, „Następna strona” z Pierwszego roku → Tutornia)?
- Czy napisać redaktorom o polu „Link (opcjonalnie)” w „W skrócie” i o grafiku Tutorni (jak edytować dyżury)?
