# Raport: zlecenie 33 — przełącznik „Opublikowane” i stan budowy na Podglądzie (18.11.2026)

## Stan
> **Aktualizacja 18.11, 17:20:** Treści 6 repozytoriów wypchnięte 18.11 o 16:49 (przed wieczorem, na Twoje polecenie) — wynik w „Push treści” na końcu. Opis niżej to stan sprzed pushu.

- **Web-Core: wypchnięte** (`b7192769..6e370e19`), po fetch i rebase na zlecenia 32 (punkt 9) i 34 drugiego okna:
  - `c70fc69b` część A: jedna funkcja `widoczny()`, flaga `TYLKO_OPUBLIKOWANE`, etykieta „szkic” na Podglądzie;
  - `cd35ea53` skrypt migracji, scenariusz 8 w symulatorze CMS, `kontrola_redaktorow.py --dopisane`, ściągawka;
  - `6e370e19` część B (z B3 i B4): plakietka stanu budowy, ukrywanie pośrednie, `skrypty/bledy_budowy.py`, test w przeglądarce.
  - Podgląd po pushu (przebieg `44294422959`, przekaźnik): **zielony**. Strona bez zmian, bo stary workflow nie ustawiał jeszcze `PODGLAD=1`.
- **Web-Podglad: wypchnięte** (`f11ae37..e64e6a8`): `PODGLAD=1`, numer przebiegu, czas startu, pochodzenie plików treści, adnotacje błędów, `pipefail`. Budowa po pushu (przebieg `44294700774`): **zielona**. Plakietka jest na żywo: „Aktualna · zbudowana 18.11, 12:27”, `data-run` = numer przebiegu, wynik z API wspólny dla kart. Pliku testowego `podglad/stan-budowy-test.json` na Podglądzie nie ma (404).
- **Repozytoria treści: NIE wypchnięte — czekają na okno pusha** (punkt 4 „Ochrony zmian redaktorów”: wieczorem albo po Twojej wiadomości do redaktorów). Gotowe lokalne commity w `tresci-z33/<repozytorium>`, gałąź `praca/33-opublikowane`:

  | Repozytorium | Baza (`origin/main` przy migracji) | Commit |
  |---|---|---|
  | Web-Aktualnosci | `e4c9c62` | `46d7f90` |
  | Web-Instytut | `311faae` | `d2d52cb` |
  | Web-Nauka | `498bc8d` | `e85c60a` |
  | Web-Popularyzacja | `0f76f88` | `72e08cd` |
  | Web-Pracownicy | `5bcaf22` | `4015203` |
  | Web-Studia | `b2a7c09` | `f31a027` |

  Przy pushu: fetch; jeśli redaktorzy coś zapisali od bazy, migracja od nowa na świeżym `main` (`python skrypty/migracja/opublikowany_33.py <katalog>`), potem `kontrola_redaktorow.py przed … --dopisane opublikowany=true`, push, `kontrola_redaktorow.py po --przed <stary origin> --dopisane opublikowany=true`.
- **Kod jest gotowy na obie kolejności.** Bez migracji treści strona wygląda tak samo (brak pola = opublikowane). Migracja treści nie zmienia żadnej strony (porównanie niżej).

## Część A — przełącznik „Opublikowane”
- **Jedna funkcja** `widoczny()` (`src/lib/tresci.ts`) zamiast filtrów z A1. Na Podglądzie pokazuje wszystko. Z `TYLKO_OPUBLIKOWANE=1` ukrywa szkice w stronach, listach, menu, kafelkach, liczbach w banerach, `sitemap.xml`, Pagefind i `.ics`. Flagi nigdzie nie ustawiłem.
- **Szkic na Podglądzie:** żółty pasek jak dotąd, wiersz na plakietce (B4) i etykieta „szkic” / „draft” przy linkach w menu, listach i kafelkach.
- **Formularze** (6 repozytoriów, lista w `.przekazanie/pola-do-cms.md`):
  - pole `opublikowany` w „Stronach” (6 repozytoriów), na stronach działów (Instytut, Nauka, Studia, Popularyzacja), w kierunkach i specjalnościach;
  - w Web-Studia zastępuje dawne „Uwzględniaj w zestawieniach”;
  - etykieta, opis i `default: true` jak w zleceniu; pole zaraz pod tytułem (pod parą tytuł / tytuł EN).
- **Dane:** 28 plików bez pola dostało `opublikowany: true`; pliki z polem bez zmian. Żaden wpis nie ma dziś `false`. Skrypt sprawdza przy każdym pliku, że poza dopisanym polem dane są równe oryginałowi, a treść pod frontmatterem jest identyczna co do bajtu.
- **Ściągawka** (`dok/sciagawka-edytora.md`): reguła ze zlecenia.

### Ukrywanie pośrednie (B4: „wypisz przypadki”)
Przy fladze strona nie powstaje także wtedy, gdy szkicem jest wpis nadrzędny:
1. **Podstrony szkicu w „Stronach”.** Liczy się adres: wszystko pod adresem szkicu. Przykład z testu: szkic `instytut/infrastruktura-informatyczna` ukrywa jej 8 podstron, w PL i EN.
2. **Specjalności szkicu kierunku** (`/studia/<kierunek>/<specjalność>`).
3. **Strona działu jako szkic nie znika**, bo prowadzi do niej menu główne. Przy fladze zostaje bez tekstu z pliku. Na Podglądzie ma żółty pasek, ale bez wiersza szkicu na plakietce, bo strona powstanie także w budowie publicznej.

Wiersz szkicu przy ukryciu pośrednim mówi „…, bo strona nadrzędna jest szkicem” i linkuje do formularza wpisu z wyłączonym przełącznikiem.

### Odbiór lokalny A
- **Bez flagi, bez szkiców:** wszystkie strony bez różnic przed/po, co do bajtu. Różnią się tylko znaczniki czasu w `.ics` (`DTSTAMP`) i `seminaria/powiadomienia.json` (`wygenerowano`). Sprawdziłem po części A i po części B.
- **5 wpisów testowych jako szkice** (kierunek ISIM, Strony `instytut/kontakt` i `instytut/infrastruktura-informatyczna`, specjalność matematyka stosowana, strona działu Nauka):
  - Podgląd: wszystkie strony są, a przy linkach jest etykieta „szkic”;
  - flaga: 735 stron zamiast 759 (24 mniej: 4 szkice z własną stroną i 8 podstron, w PL i EN); znikają też z menu, list, kafelków, mapy strony i wyszukiwarki;
  - Wpisy testowe były tylko w lokalnej nakładce. Przywrócone: nakładka jest równa kopii sprzed testu.
- **Migracja treści:** budowa z migrowanymi plikami bez różnic względem budowy bez migracji.
- **Symulacja zapisu w CMS** (`skrypty/test-edytora`, scenariusz 8, jak w zleceniu 28):
  - stara strona otwarta i zapisana bez zmian zostaje opublikowana;
  - nowa startuje jako opublikowana;
  - po odznaczeniu staje się szkicem;
  - wynik: 48 kontroli OK.
  - Dodatkowo „zapis bez zmian” na wszystkich 725 plikach: 0 różnic.

## Część B — stan budowy na Podglądzie
- **Dane:**
  - pytanie przy wejściu, potem co 120 s, a w trakcie budowy co 20 s; pauza, gdy karta jest w tle;
  - przy 403/429 albo gdy z limitu zostało mniej niż 5: „Stan budowy chwilowo niedostępny” i ponowna próba po 10 min.
- **Wygląd (B2):**
  - plakietka „● Aktualna · zbudowana …”;
  - budowa w toku: napis, szacowany czas z mediany 5 udanych budów i pasek postępu; kolejka ma osobny napis;
  - dymek „Nowa wersja strony gotowa — Odśwież”;
  - czerwony pasek błędu pod paskiem menu, `role="alert"`, z polskim komunikatem, „Popraw w CMS” i „Szczegóły”. Da się go zwinąć do czerwonej plakietki, ale wraca na każdej podstronie, dopóki kolejna budowa się nie uda;
  - `role="status"` ogłasza tylko zmiany; tryb ciemny; `prefers-reduced-motion`.
- **B3:**
  - przeciąganie z progiem 6 px i `setPointerCapture`; róg w `localStorage` `im-plakietka-rog`;
  - komputer: 4 rogi, górne pod paskiem menu; telefon: 2 dolne;
  - rozwijanie w stronę środka ekranu; przycisk „Przenieś do innego rogu”; Escape zamyka szczegóły.
- **B4:** żółty wiersz także przy zwiniętej plakietce, z linkiem do formularza w Pages CMS. Adres formularza ustalany przy budowie: plik → repozytorium z `.tresci/pochodzenie.json`, który zapisuje `podglad.yml`.
- **Błędy budowy:**
  - `skrypty/bledy_budowy.py` czyta dziennik budowy i wypisuje adnotacje `::error title=Błąd treści::<repozytorium> › <formularz> › <plik> › <pole>: <komunikat> › <adres w CMS>`;
  - plakietka czyta je bez logowania (`/actions/runs/{id}/jobs` → `/check-runs/{job}/annotations`; sprawdzone na wcześniejszych nieudanych przebiegach, działa);
  - typowe komunikaty zod tłumaczy na polski („Required” → „brak wymaganego pola”).
  - Sprawdzone na prawdziwej nieudanej budowie lokalnej (zły typ pola i niedozwolona wartość) i na dzienniku w formacie z GitHuba.
- **Tylko Podgląd:** bez `PODGLAD=1` nie ma ani znacznika, ani plików `podglad/*` (porównanie co do bajtu wyżej). Plik testowy `stan-budowy-test.json` powstaje tylko w budowie lokalnej bez numeru przebiegu.

### Odbiór lokalny B
- **Test w przeglądarce** (`node skrypty/test-stanu-budowy.mjs http://localhost:4321/Web-Core raport-zrzuty`, Edge):
  - zakres: 6 stanów × komputer/telefon × jasny/ciemny, przeciąganie do każdego rogu, pamięć rogu po przejściu na inną podstronę i po odświeżeniu, kliknięcie bez przesunięcia, klawiatura, wiersze szkicu i linki;
  - wynik: **57 OK, 0 problemów, 0 błędów w konsoli**. Powtórzone po rebase na tryb ciemny ze zlecenia 34.
- **Prawdziwe API:** strona lokalna z `PODGLAD=1` pokazała „Aktualna”, a w trakcie pomiaru, gdy ruszyła budowa drugiego okna, „Przebudowa…”.
- **Pomiar przez 10 min** (`/instytut/struktura/`, zapis sieci przez CDP): odpowiedzi 200 w sekundach 1, 121, 242, 362, 483 i 603. W każdym oknie 10 min jest ich najwyżej 5. **Kryterium spełnione.**
- `astro check`: 0 błędów, 0 ostrzeżeń (podpowiedzi: 3 stare; nowe: 2 w `klient.js` „można użyć async” i nieużywana zmienna w `skrypty/test-stanu-budowy.mjs`).
- **Zrzuty** (`raport-zrzuty/`, 41 plików):
  - `z33-{komputer|telefon}-{jasny|ciemny}-{ok|w-toku|kolejka|nowa|blad|blad-zwiniety|limit|szczegoly}.png`;
  - `z33-komputer-rog-{ld|lg|pg|pd}.png`, `z33-telefon-rog-{ld|pd}.png`;
  - `z33-komputer-szkic.png`, `z33-komputer-szkic-posrednio.png`, `z33-komputer-opublikowana.png`.

## Decyzje przyjęte samodzielnie
- **Pole stoi pod parą tytuł / tytuł EN**, a nie między nimi. Przyjąłem tak, bo para musi zostać obok siebie. W specjalnościach, których pliki nie mają kolejności schematu, pole stoi po polu z najbliższym niższym miejscem w schemacie.
- **Istniejące klucze zostają na swoich miejscach;** dopisuję tylko brakujące. Przyjąłem tak, bo przestawianie zmieniało koniec bloku `tresc_en: |` w `historia.md`.
- **Strona działu jako szkic:** przy fladze zostaje, bez tekstu z pliku, z żółtym paskiem na Podglądzie (Twoja propozycja z pytania 2 z rana). Przyjąłem tak, bo menu główne musi mieć dokąd prowadzić. Do potwierdzenia, pytanie 2.
- **`localStorage` zamiast `sessionStorage`** dla wyniku z API (30 s), wspólny dla kart. Przyjąłem tak, bo:
  - odpowiedź 304 **też** zmniejsza limit (sprawdzone: 59 → 58 → 57), wbrew założeniu w B1;
  - dwie otwarte karty pytałyby osobno.
  - ETag przeglądarka i tak wysyła sama (`cache: 'no-cache'`).
- **`per_page=10` zamiast 5.** Przyjąłem tak, bo przerwane przebiegi (`cancelled`, częste po zleceniu 41) wypychałyby udane budowy z listy, a mediana potrzebuje 5 udanych.
- **Stały żółty kolor wiersza szkicu.** Przyjąłem tak, bo kolor akcentu zależy od działu i w części działów wiersz nie był żółty.
- **Link „Włącz »Opublikowane«” tylko do formularzy z przełącznikiem** (Strony, kierunki, specjalności). Przyjąłem tak, bo na stronach działu wiersza i tak nie ma.
- **Strony prawne i „O stronie” (Web-Ustawienia)** bez przełącznika. Przyjąłem tak, bo to nie są „Strony” z tego zlecenia (osobne formularze plików).
- **Kolejność pushy:** Web-Core i Web-Podglad w dzień, treści wieczorem, a nie „Web-Core, treści, Web-Podglad” z mojego planu. Przyjąłem tak, bo okno pusha dotyczy tylko repozytoriów treści, a workflow nie zależy od migracji.
- **Plakietka trafia też na gałąź `zbudowana`** (kopia do zrzutów), bo to ta sama budowa. Zrzuty z tej gałęzi będą ją miały w lewym dolnym rogu, z godziną budowy. Do porównań przed/po trzeba ją ukryć (`#stan-budowy{display:none}`).

## Znalezione przy okazji
1. **`podglad.yml` ze zlecenia 41 nie miał `pipefail`.**
   - Bez `shell:` Actions używa `bash -e {0}`, więc nieudane `npm run build | tee` nie przerywało kroku.
   - Niepełna strona mogła trafić na Podgląd. Mój wpis w rozpoznaniu z rana („pipefail jest domyślnie”) był błędny.
   - Naprawione w `e64e6a8`.
2. **Żółty pasek „ta strona nie jest jeszcze opublikowana”** (`.notice-warn` w `Baza.astro`, sprzed tego zlecenia) jest **zasłonięty**: na komputerze przez stały pasek menu, na telefonie przez baner. Nie zmieniałem tego, pytanie 3.
3. **Odpowiedź 304 też zmniejsza limit API** (wyżej). Zmieniłem założenie z B1 i opisałem to w decyzjach.
4. **Zlecenie 40** podaje `strony/studia/podyplomowe.md`; po zleceniu 39 to `kierunki/podyplomowe.md`.

## Pytania do Ciebie (niewdrożone)
1. **Zakłady i „Warto wiedzieć”** mają `opublikowany` w schemacie, ale nie mają przełącznika w CMS. Dodać go?
2. **Strona działu jako szkic:** zostawić jak teraz (strona zostaje, bez tekstu, żółty pasek tylko na Podglądzie)? Czy taki szkic ma też dostać wiersz na plakietce, np. „Tekst tej strony nie trafi na stronę publiczną”?
3. **Żółty pasek szkicu jest zasłonięty** (znalezisko 2). Przesunąć go pod pasek menu, tak jak czerwony pasek błędu?
4. **Dymek „Nowa wersja gotowa” pojawia się po każdej udanej budowie,** także po przebudowie z harmonogramu (co godzinę) albo po zmianie w innym repozytorium. Zostawić tak, czy pokazywać dymek tylko wtedy, gdy zmieniła się otwarta strona? Druga wersja wymaga skrótów stron w budowie.

## Do sprawdzenia
- **Dziś wieczorem:** push 6 repozytoriów treści z kontrolą przed i po (wyniki dopiszę tutaj).
- **Jutro (19.11):** zapisy redaktorów z 24 godzin po pushu treści: czy żaden formularz otwarty przed pushem nie usunął `opublikowany` ani nie przywrócił „Uwzględniaj w zestawieniach”. Do tego test w CMS: nowa Strona startuje z zaznaczonym „Opublikowane”, odznaczenie → szkic na Podglądzie z żółtym wierszem i działającym linkiem.
- **Pierwsza nieudana budowa po pushu:** czy czerwony pasek pokazuje adnotacje z linkiem „Popraw w CMS” (lokalnie sprawdzone tylko na dzienniku).

## Decyzje właściciela (18.11, ok. 13:05)
1. **Zakłady i „Warto wiedzieć”:** dodać przełącznik „Opublikowane” (formularze i `opublikowany: true` w istniejących plikach; push treści w oknie wieczornym).
2. **Strona działu jako szkic:** dodać wiersz na plakietce stanu budowy z linkiem do formularza.
3. **Żółty pasek szkicu:** przesunąć pod pasek menu, jak czerwony pasek błędu (tylko Podgląd).
4. **Dymek „Nowa wersja gotowa”:** tylko wtedy, gdy zmieniła się otwarta strona (skróty stron zapisane w budowie).

## Wdrożenie decyzji z 18.11 (push 13:34)
- **Web-Core `00fff0a8..fb54f3f5`** (po rebase na zlecenie 37), Podgląd 44304735795 zielony. Na żywo `podglad/skroty.json` (755 stron), a plakietka ma `data-skrot` i `data-plik`.
  - **Strona działu jako szkic:** wiersz „Szkic: tekstu tej strony nie będzie na stronie publicznej (strona zostanie, bez tekstu)” z linkiem do formularza pliku (`…/main/file/strona-dzialu`, `…/file/popularyzacja`). Adres formularza pliku sprawdziłem w źródłach Pages CMS (`app/(main)/[owner]/[repo]/[branch]/file/[name]`); z tego samego korzysta `skrypty/bledy_budowy.py`.
  - **Żółty pasek szkicu** przypięty pod paskiem menu (komputer: `--gora`, telefon: `--hdr-h`). Na telefonie mieści się w jednej linii, a treść schodzi o wysokość paska, bo inaczej pasek zasłaniał link „← dział” w banerze. Czerwony pasek błędu ma wyższy `z-index` i przy błędzie przykrywa żółty, bo ważniejszy jest błąd.
  - **Dymek „Nowa wersja gotowa” tylko przy zmianie tej strony.**
    - Integracja `src/integracje/skrotyPodgladu.mjs` działa tylko przy `PODGLAD=1`. Liczy skrót HTML każdej strony bez numeru przebiegu, czasu budowy i napisu plakietki, wpisuje go do plakietki i zapisuje `podglad/skroty.json`.
    - Klient po nowej udanej budowie pobiera `skroty.json` z serwera strony, nie z API GitHuba. Jeśli plik jest jeszcze ze starszej budowy, ponawia co 20 s, najwyżej 6 razy, a potem pokazuje dymek jak dotąd.
    - Sprawdzone: dwie budowy tych samych danych z innym numerem przebiegu i czasem dają 755 takich samych skrótów.
  - **Zakłady i „Warto wiedzieć”:** link do formularza w wierszu szkicu.
- **Web-Instytut (lokalnie, push dziś wieczorem z resztą 33):** commit przebudowany na `b2de465` z przełącznikiem „Opublikowane” w formularzach `zaklady` i `warto_wiedziec`. 12 z 13 plików miało już `opublikowany: true`, a jeden wpis „Warto wiedzieć” z CMS dostał je dopisane. Kontrola migracji (`--sprawdz`): 0 problemów.
- **Kontrole:**
  - test plakietki 69 OK (było 57; nowe: wiersz strony działu PL i EN, zakład, „Warto wiedzieć”, pasek pod menu na komputerze i telefonie przy przewinięciu 0 i 600 px, dymek a skrót strony), błędy w konsoli 0;
  - zwykła budowa (bez Podglądu) przed i po: 755 stron różni się tylko nazwą pliku CSS (dodane reguły `.szkic-pasek`), pliki ICS znacznikami czasu;
  - `astro check`: 0 błędów i 0 ostrzeżeń.
- Zrzuty: `raport-zrzuty/z33-komputer-pasek-szkicu.png`, `z33-telefon-pasek-szkicu.png`.

## Push treści (18.11, 16:49, przed wieczorem — na Twoje polecenie)
Ok. 16:47 napisałeś „Dobra, zgadzam sie wrażamy teraz” (po mojej propozycji pushu przed wieczorem, gdy redaktorzy wiedzą). Wieczorne zadania usunąłem, skrypt `push33_tresci.sh` uruchomiłem od razu.

| Repozytorium | Zapisów redaktorów od bazy | Wypchnięte | Kontrola po pushu |
|---|---|---|---|
| Web-Aktualnosci | 0 | `e4c9c62..46d7f90` | OK |
| Web-Instytut | 0 | `311faae..b2de465` | OK |
| Web-Nauka | 0 | `498bc8d..e85c60a` | OK |
| Web-Popularyzacja | 0 | `0f76f88..72e08cd` | OK |
| Web-Pracownicy | 0 | `5bcaf22..4015203` | OK |
| Web-Studia | 0 | `b2a7c09..f31a027` | OK |

- Commity jak w tabeli w „Stan” (Web-Instytut: `b2de465` — commit poprawiony po decyzjach z 13:05, przełącznik w Zakładach i „Warto wiedzieć”).
- Podgląd: **zielony** — przebieg 44340270000 (16:50) zbudował stronę z treściami po zleceniu 33 i Web-Core `b43b0aa8`; wcześniejsze przebiegi z tej serii pushy anulowała kolejka Podglądu (zostaje najnowszy).
- **Web-Aktualnosci:** druga sesja ma tam niewypchnięte zmiany formularzy (zlecenie 44). Przed swoim pushem zrobi `fetch` i rebase na ten commit.
