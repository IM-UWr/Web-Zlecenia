# Raport: zlecenie 48, przełącznik „Opublikowane” w seminariach, referatach i aktualnościach (18.11.2026)

**Status:** zrobione lokalnie, **nic nie wypchnięte**. Czeka na „push” razem ze zleceniami 47 i 46 (jedno STOP na końcu serii). Test w CMS z właścicielem po pushu (lista niżej).

| Repozytorium | Gałąź lokalna | Commit | Baza (HEAD main na starcie) |
|---|---|---|---|
| Web-Core (worktree `Web-Core-B`) | `praca/48-opublikowane` (od gałęzi 47) | `61d6e683` | `3cde30e0` (origin/main) + 47 `1e479c91` |
| Web-Aktualnosci | `praca/48-opublikowane` | `9513d48` | `abf23d3` |
| Web-Sem-Analiza-Harmoniczna | `praca/48-opublikowane` | `e25b641` | `5eb2b74` |
| Web-Sem-Dydaktyka | `praca/48-opublikowane` | `b3d6e7f` | `9c5b94c` |
| Web-Sem-Dyskretna-Analiza-Harmoniczna | `praca/48-opublikowane` | `81716a7` | `bc395d4` |
| Web-Sem-Geometria | `praca/48-opublikowane` | `1700d8a` | `2f1da74` |
| Web-Sem-Prawdopodobienstwo | `praca/48-opublikowane` | `15169e5` | `ad6e073` |
| Web-Sem-Rownania-Rozniczkowe | `praca/48-opublikowane` | `ba24c65` | `d7fc10b` |
| Web-Sem-Statystyka | `praca/48-opublikowane` | `699c086` | `0548f72` |
| Web-Sem-Teoria-Modeli | `praca/48-opublikowane` | `5a96f65` | `68515d1` |
| Web-Sem-Topologia | `praca/48-opublikowane` | `1cf30da` | `3aba9c1` |

Warunek ze zlecenia: zlecenie 33 jest na `main` Web-Core (sprawdzone na świeżym `origin/main` na początku serii: `widoczny()`, `TYLKO_OPUBLIKOWANE`, etykieta „szkic”, żółty pasek, wiersz B4, ściągawka). Zlecenie 40 (wspólny wzór formularzy `formularze_40.mjs`) też jest na `main`.

## Co jest zrobione

**Schemat:** bez zmian — pole `opublikowany: published` (brak pola = opublikowane) jest w kolekcjach `aktualnosci`, `seminaria` i `referaty` w `src/content.config.ts` od przeniesienia kodu, a `widoczny()` filtruje je w `aktualnosci()`, `seminaria()` i `referaty()` od zlecenia 33, część A. Brakowało ukrycia pośredniego referatów, oznaczeń referatu-szkicu, wiersza B4 dla tych formularzy i samych przełączników w CMS.

**Kod (Web-Core):**
- `referaty()` (`src/lib/tresci.ts`): przy `TYLKO_OPUBLIKOWANE=1` referaty seminarium-szkicu znikają razem z nim (ukrycie pośrednie, jak podstrony w 33). Filtr dalej w jednym miejscu, więc działa wszędzie, gdzie są referaty: Kalendarz, `.ics`, „Najbliższe seminaria”, strony zakładów, liczby.
- Referat nie ma własnej strony — jest kotwicą `/seminaria/<seminarium>#<plik>` na stronie seminarium. Na Podglądzie referat-szkic ma etykietę „szkic” / „draft” przy tytule (`Seminarium.astro`), a plakietka strony seminarium dostaje żółty wiersz „Szkic: referatu „…” nie będzie na stronie publicznej. Włącz »Opublikowane« w CMS →” z linkiem do formularza „Referaty” tego pliku (`StanBudowy.astro`, `klient.js`; kilka referatów-szkiców = kilka wierszy).
- `szkice.ts`: rejestr kotwic referatów-szkiców; middleware oznacza linki do takiej kotwicy etykietą (Podgląd), a z flagą zamienia je na tekst z ostrzeżeniem `[szkice]`, tak samo jak linki do stron-szkiców z 33. Etykieta i jej styl są wspólne (`ETYKIETA_SZKICU`).
- `podglad.ts`: link „Włącz »Opublikowane« w CMS” dla aktualności (`…/collection/aktualnosci/edit/…`), referatów (`…/collection/referaty/edit/…`) i opisu seminarium — to formularz jednego pliku, więc adres ma postać `https://app.pagescms.org/im-uwr/web-sem-<…>/main/file/seminarium` (jak przy „Stronie działu” i „Popularyzacji”). Na stronie seminarium-szkicu (gdzie są też jego referaty) wiersz prowadzi do formularza opisu seminarium.

**Gdzie działa filtr (lista do raportu).** Kolekcje czytają tylko trzy funkcje w `src/lib/tresci.ts`: `aktualnosci()`, `seminaria()`, `referaty()`. Na nich stoją `pozycjeAktualnosci` (→ `listaAktualnosci`, `listaOfert`, `aktualnosciNaGlowna`, `liczbyNaOkladke`, „Aktualności dla studentów” w `dzialStudia.ts`), `wszystkieWydarzenia` (→ Kalendarz, `.ics`, „Nadchodzące wydarzenia”, `wydarzeniaNaTelefon`) i `referatyWTygodniu`. Korzystają z nich: `sciezki.ts` (strony szkiców nie powstają), `sitemap.xml`, `rss.xml` (PL i EN), `kalendarz/[plik].ics`, `seminaria/powiadomienia.json`, widoki `listaAktualnosci` (lista z filtrami, Kariera, ramka „Oferty pracy… (N)”), `aktualnosc`, `listaSeminariow` (+ menu i Szybki dostęp), `seminarium`, `zaklad`, `specjalnosc` (pola „seminaria”), `dzialInstytut`, `listaSukcesow`, `kalendarz`, `DrugiEkran` (kolumny strony głównej, „Ostatnio”), `Okladka` (liczby). Pagefind indeksuje gotowe strony, więc szkiców tam nie ma. Jedyne bezpośrednie `getCollection` tych kolekcji poza `tresci.ts` to `szkice.ts` — celowo, bo zbiera same szkice do oznaczeń.

**Formularze (CMS):** pole `opublikowany` (tak/nie, `default: true`, etykieta jak w 33: „Opublikowane — widoczne na stronie publicznej (na Podglądzie widać zawsze)”), zaraz pod tytułem (pod parą PL/EN, gdy jest tytuł EN):
- Web-Aktualnosci, „Aktualności”: „Odznacz, żeby przygotować wpis bez pokazywania go na stronie publicznej (szkic).”;
- 9 × Web-Sem-*, „Opis seminarium”: „Odznacz, żeby przygotować seminarium bez pokazywania go na stronie publicznej (szkic). Razem z nim znikną wszystkie jego referaty.”;
- 9 × Web-Sem-*, „Referaty”: „Odznacz, żeby przygotować referat bez pokazywania go na stronie publicznej (szkic).”

Zmiana idzie przez wspólny wzór `skrypty/migracja/formularze_40.mjs` (Web-Aktualnosci: etap 3; Web-Sem-*: etap 5). We wszystkich 9 seminariach zmiana `.pages.yml` jest identyczna (ten sam diff, 11 linii, sprawdzone sumą kontrolną). Przy okazji skrypt czyta źródło z `\r\n` → `\n` (na checkoucie z CRLF przestawiał wcięcia kotwic YAML).

**Istniejące wpisy, jawna wartość** (`skrypty/migracja/opublikowany_48.py`, idempotentny, z kontrolą YAML i treści pod frontmatterem; jeden commit na repozytorium, razem z formularzem):

| Repozytorium | Plików | Dopisane `opublikowany: true` | Z polem wcześniej | `false` |
|---|---|---|---|---|
| Web-Aktualnosci (aktualności) | 167 | **4** | 163 | 0 |
| 9 × Web-Sem-* (opisy) | 9 | **0** | 9 | 0 |
| 9 × Web-Sem-* (referaty) | 31 | **0** | 31 | 0 |

Cztery pliki: `2026-11-10-seminarium-wydzialowe-problem-milenijny`, `2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza`, `2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego`, `2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu` (dodane w CMS po migracji, bez pola). Żaden wpis nie stał się szkicem. Dopisanie powtórzę na świeżym `main` tuż przed pushem.

**Dokumentacja:** `dok/sciagawka-edytora.md` — sekcja „Opublikowane” (zlecenia 33 i 48): lista formularzy z przełącznikiem rozszerzona o Aktualności, opis seminarium i Referaty; zdanie ze zlecenia: „**Odznaczenie »Opublikowane« w opisie seminarium ukrywa całe seminarium razem z referatami.**”; osobno referat-szkic i aktualność-szkic; „Bez przełącznika: obrony, konferencje, granty i pracownicy”. `.przekazanie/pola-do-cms.md` — sekcja „Zlecenie 48”.

## Odstępstwa od zlecenia i powody
1. **Linki w treści do szkiców (punkt 4, „Nie usuwaj tych linków automatycznie”).** Ostrzeżenie w logu jest przy każdym takim linku. Plik Markdown redaktora zostaje nietknięty, ale w HTML budowy z flagą link staje się samym tekstem, jak od zlecenia 33 („nieopublikowane strony znikają, a razem z nimi linki do nich”). Bez tego strona publiczna miałaby linki prowadzące do 404. Rozumiem „nie usuwaj” jako „nie zmieniaj treści redaktora”: po opublikowaniu celu link wraca sam. Pytanie 1 niżej.
2. **„Strona referatu”.** Referaty nie mają własnych stron, więc żółty wiersz i etykieta referatu-szkicu są na stronie seminarium, przy kotwicy referatu. Żółtego paska na górze tam nie ma, bo sama strona seminarium jest opublikowana. Referaty seminarium-szkicu nie dostają osobnych wierszy: pasek i wiersz strony prowadzą do formularza opisu seminarium (zgodnie z punktem 3).
3. **Zapowiedziany referat testowy.** W danych nie ma żadnego przyszłego referatu, więc do odbioru dodałem w nakładce lokalnej plik `src/content/referaty/statystyka/test-2026-11-25-referat-testowy.md` (25.11, 14:15, s. 605). Plik istniał tylko na czas budów testowych i nie trafił do żadnego repozytorium.
4. **Ramka Kariery.** Liczba „w ramce Kariery” to „Oferty pracy, staży i stypendiów (N) →” na liście Aktualności. Na samej stronie Kariera licznika nie ma.

## Pytania do właściciela
1. Linki w treści do szkiców przy budowie z flagą: zostawić jak w 33 (sam tekst + ostrzeżenie, bez 404) czy zostawić linki (prowadzące do 404) i tylko ostrzegać? Dziś obowiązuje pierwsze.
   **Decyzja właściciela (18.11, ok. 22:30): sam tekst + ostrzeżenie, jak w 33.** Bez zmian w kodzie.
2. Termin pusha 48 w repozytoriach treści: wieczorem czy po Twojej wiadomości do redaktorów („zapiszcie i zamknijcie CMS na 15 minut”), także do redaktorów 9 seminariów?
   **Decyzja właściciela (18.11, ok. 22:30): „Teraz”** — repozytoria treści 48 idą zaraz po Web-Core w kolejności pusha, bez czekania na wiadomość do redaktorów. Sam push nadal po słowie „push”.

## Odbiór lokalny
Budowy (nakładka w `Web-Core-B`, wynik w `tresci-B/…`; skrypty `tresci-B/z48-budowy.sh`, `z48-podglad.sh`, `z48-linki.sh`; po każdej nakładka wraca do stanu z repozytoriów treści — kontrola: zostały tylko szkice z 47, czyli 6 sylwetek osób żyjących):
- A `z48-po` — dane po migracji, kod 48, bez flagi;
- B `z48-ref` — A + referat testowy (opublikowany);
- C `z48-szkice` — B + szkice testowe: aktualność z terminem (MISIU, 27.11), oferta Kariera (korepetytor), seminarium z referatami (Prawdopodobieństwo, 3 referaty), zapowiedziany referat (testowy, Statystyka);
- D `z48-flaga` — C z `TYLKO_OPUBLIKOWANE=1`;
- E `z48-podglad` — C + szkice testowe 33/47, `PODGLAD=1`, `pochodzenie.json` (plakietka);
- F/G `z48-linki`, `z48-linki-podglad` — C + akapit testowy na stronie „Pierwszy rok” z linkami do wszystkich czterech szkiców i do referatu seminarium-szkicu (z flagą i bez).

**Przed i po (bez flagi, bez szkiców):** A względem wyniku 47 (`z47-po`): wszystkie strony identyczne co do bajtu; różnią się tylko znaczniki czasu (`DTSTAMP` w `.ics`, „wygenerowano” w `powiadomienia.json`).

**Bez flagi, ze szkicami (C względem B, `raport-zrzuty/z48-skrypt/porownaj48.py`):** 5013 plików w obu. 24 strony różnią się tylko etykietą „szkic” (lista i EN lista Aktualności, Kariera, strona główna PL/EN, Kalendarz, lista seminariów, strona Statystyki z referatem-szkicem, strona zakładu, dwie specjalności, trzy aktualności sąsiadujące ze szkicami — przy linku „Nowszy / Starszy wpis”; z flagą ten link prowadzi do najbliższego opublikowanego wpisu); 6 stron samych szkiców — etykietą i żółtym paskiem „Podgląd — ta strona nie jest jeszcze opublikowana”. Innych różnic: 0.

**Z flagą (D, `raport-zrzuty/z48-skrypt/sprawdz48.py`): 0 problemów.**
- strony szkiców (aktualność, oferta, seminarium; PL i EN) i ich `.ics` (w tym 4 pliki `.ics` referatów) są bez flagi, nie ma ich z flagą;
- w budowie z flagą ani śladu żadnego z czterech szkiców w HTML, XML (mapa strony, RSS), JSON, `.ics` i indeksie Pagefind (bez flagi są na 8–14 stronach);
- powiększona aktualność: bez flagi szkic MISIU (18.11), z flagą najnowsza opublikowana (Medale, 13.11);
- liczby (`liczby48.py`): okładka „2 nowe aktualności” → „1 nowa aktualność”; ramka „Oferty pracy, staży i stypendiów (11)” → „(10)” (PL i EN); lista seminariów „9 seminariów” → „8”, „1 zapowiedziany referat” → brak, „31 referatów w archiwum” → „28” (3 referaty Prawdopodobieństwa); Kalendarz bez referatu testowego, seminarium i wykładu. Liczba „wydarzeń” na okładce (1) się nie zmienia, bo liczy 6 dni, a szkic jest za 9 dni.

**Linki w treści do szkiców (F):** w logu budowy z flagą 5 ostrzeżeń `[szkice]` — do aktualności, oferty, seminarium, kotwicy referatu-szkicu i kotwicy referatu seminarium-szkicu; link do opublikowanego seminarium bez ostrzeżenia i zostaje linkiem. Bez flagi (G) wszystkie linki zostają, z etykietą „szkic”. W danych prawdziwych nie ma dziś żadnego linku w treści do szkiców 48 (w D jest 13 ostrzeżeń, wszystkie o sylwetkach-szkicach z 47). Linki wewnętrzne (`qa.py`) w D i F: 0 zepsutych; 11 nieistniejących kotwic jak w budowie bez szkiców (stare, bez związku z 48).

**Symulacja zapisu w CMS** (`skrypty/test-edytora/formularz.mjs`, nowy scenariusz 11, log `tresci-B/z48-formularz.log`): 77/77 OK dla Aktualności, opisu seminarium i Referatów we wszystkich 9 seminariach: pole pod tytułem, tak/nie, domyślnie zaznaczone, etykieta jak w 33; stary wpis bez pola po zapisie bez zmian → `opublikowany: true`; nowy wpis → opublikowany; po odznaczeniu → `opublikowany: false`; trzy różne opisy, identyczne w 9 seminariach. Zapis bez zmian 756 plików: jak przed zleceniem — 6 znanych różnic spoza zlecenia (5 obron i 1 grant dostają szablon Treści, zlecenie 40).

**Plakietka B4 (E, `skrypty/test-stanu-budowy.mjs`, zrzuty `raport-zrzuty/z48-stan/`): 0 problemów, konsola czysta.** Aktualność-szkic: żółty pasek + wiersz z linkiem `…/web-aktualnosci/main/collection/aktualnosci/edit/src%2Fcontent%2Faktualnosci%2F2026-11-18-…md`; seminarium-szkic (PL i EN): pasek + wiersz z linkiem `…/web-sem-prawdopodobienstwo/main/file/seminarium`; referat-szkic na stronie Statystyki (PL i EN): wiersz z linkiem `…/web-sem-statystyka/main/collection/referaty/edit/src%2Fcontent%2Freferaty%2Fstatystyka%2Ftest-…md`, etykieta przy tytule, bez paska. Testy 33/47 dalej przechodzą.

**Zrzuty** (`raport-zrzuty/z48-zrzuty/`, 20 plików, Podgląd E): lista Aktualności, lista seminariów, strona seminarium z referatem-szkicem, strona seminarium-szkicu, strona główna; komputer 1440 i telefon 390; jasny i ciemny. Konsola czysta.

**Kontrole:** `astro check` 0 błędów, 0 ostrzeżeń (4 podpowiedzi, jak przed zmianą); `npm run test:jawne` 76/76; `sprawdz_pola_cms.py` 0 problemów (756 plików, 16 repozytoriów); `opublikowany_48.py --sprawdz` 0 problemów.

## Test w CMS z właścicielem (po pushu)
1. Web-Aktualnosci, „Aktualności”: przełącznik „Opublikowane” zaraz pod tytułem (pod EN), zaznaczony; opis jak wyżej.
2. Otworzyć starą aktualność i zapisać bez zmian: brak commita albo commit bez zmian w pliku.
3. Nowa aktualność „Test 48”: startuje jako opublikowana; odznaczyć, zapisać → na Podglądzie etykieta „szkic” na liście, żółty pasek i wiersz plakietki z linkiem do tego wpisu w CMS; potem usunąć wpis.
4. Dowolne Web-Sem-*, „Opis seminarium”: przełącznik pod nazwą, opis o referatach. Nie odznaczać na prawdziwym seminarium (Podgląd pokazałby je jako szkic do kolejnej budowy) — wystarczy obejrzeć formularz.
5. „Referaty”: nowy referat „Test 48” w przyszłości, odznaczony → na Podglądzie etykieta przy tytule na stronie seminarium i wiersz plakietki z linkiem do formularza „Referaty”; potem usunąć.
6. To samo pole widać w pozostałych 8 seminariach (identyczna zmiana).

## Kontrola zapisów redaktorów przed „push” (fetch 18.11, 22:1x)
- **Web-Aktualnosci:** od bazy `abf23d3` doszły 2 zapisy przez Pages CMS (`34cfa21`, `7829e4e`, oba 21:50, konto właściciela). Oba dotyczą wpisu `2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego.md` — jednego z 4 plików, do których 48 dopisuje `opublikowany: true`. Zmiany: zajawka PL i EN, `tytul_en` przeniesiony, `pozycja: false` w terminach. Pola `opublikowany` tam nie ma. **Przy pushu nie użyję commitu `9513d48` w obecnej postaci:** na świeżym `main` ponownie uruchomię `formularze_40.mjs` i `opublikowany_48.py`, a potem sprawdzę pole po polu, że zapisy z 21:50 zostały.
- 9 × Web-Sem-*: od baz 0 nowych commitów.

## Push (zrobię po „push”)
1. Web-Core: rebase serii 47–48–46 na `origin/main`, push `main` (pole w plikach nie psuje budowy, więc Web-Core może iść pierwszy).
2. Web-Aktualnosci: `git fetch`, `git log abf23d3..origin/main`. Jeśli przybyły zapisy redaktorów, na świeżym `main` ponownie `formularze_40.mjs` i `opublikowany_48.py` (nie doklejam starego wyniku); kontrola pole po polu przed i po pushu.
3. 9 × Web-Sem-*: jednym skryptem, każde od swojej bazy z tabeli, tak samo.
4. Następnego dnia: przegląd zapisów redaktorów z 24 h, w tym liczba zapisów, które wycięły `opublikowany: true` (formularz otwarty przed pushem, zapisany po nim — nieszkodliwe, brak pola = opublikowane).

## Push (18.11.2026, po „push” właściciela; decyzja: „Teraz”)
- **Web-Core:** w serii, `3cde30e0..4e1d4c62`.
- **Web-Aktualnosci:** od bazy `abf23d3` przybyło do 22:37 pięć zapisów: wpis o Medalach (konto właściciela: 21:50 ×2, 22:16) i nowy wpis o nagrodzie im. Hulanickiego ze zdjęciami (redaktor, 22:26–22:37). Commitu `9513d48` nie użyłem. Na świeżym `main` uruchomiłem jeszcze raz `formularze_40.mjs` (zmiana `.pages.yml` identyczna jak wcześniej) i `opublikowany_48.py`. Pierwsza próba pushu: tuż przed nim fetch pokazał kolejny zapis (zdjęcie, 22:37), więc wszystko powtórzyłem na nowym `main` (`praca/48-opublikowane-push2`).
  - **Wpis o nagrodzie Hulanickiego zostawiłem bez zmian:** redaktor pracował nad nim w tej samej minucie. Moja zmiana tego pliku mogłaby zablokować jego zapis w CMS (konflikt wersji). Brak pola = opublikowane, a przy następnym zapisie nowy formularz sam wpisze `opublikowany: true`.
  - Pole po polu przed pushem (YAML, `origin/main` → commit): 4 pliki (seminarium wydziałowe, Gdesz, Medale, MISIU) różnią się tylko dopisanym `opublikowany: true`, treść pod frontmatterem identyczna co do bajtu. Zmiany z Medali (zajawka PL/EN, `tytul_en`, `pozycja`) zostały.
  - Push `9cf2e52..73569b8` o 22:38:57. Po pushu: 1 nowy commit redaktora (zdjęcie `agnieszkaimariusz2.jpeg`, 22:39), żadnego zapisu plików z przełącznikiem.
- **9 × Web-Sem-*** (skrypt `tresci-B/z48-push-sem.sh`, log `z48-push-sem.log`): w każdym fetch i kontrola od bazy — 0 nowych commitów, więc pushowane commity z odbioru. 22:39:14–22:39:45, wszystkie OK, `origin/main` = gałąź. Zmiana w każdym: tylko `.pages.yml` (+11 linii, identycznie). Po pushu 0 nowych.
- Jutro: przegląd zapisów redaktorów z 24 h, w tym ile zapisów wycięło `opublikowany: true` (formularz otwarty przed pushem) i czy wpis Hulanickiego dostał pole przy zapisie.
