# Raport: zlecenie 39 — kierunki w menu i kafelkach bez automatów; studia podyplomowe jako kierunek (18.11.2026)

## W skrócie

**Stan: wypchnięte 18.11, 01:58–02:01** (Web-Ustawienia, Web-Core, Web-Studia; szczegóły w „Push” niżej). Podgląd był zielony po każdym pushu. Strona na żywo jest zgodna z lokalną budową: strona główna, `/studia`, podyplomowe i kierunki, PL i EN. Zostało: przegląd zapisów redaktorów do 19.11, ok. 02:00, i Twoje decyzje z „Pytań”.

- **Tylko lista.** Menu „Studia”, panel hamburgera, pole kierunków na `/studia` i kafelki strony głównej pokazują wyłącznie pozycje z listy w Ustawieniach, w jej kolejności. Kierunek spoza listy ma swoją stronę, ale nie pojawia się sam: budowa wypisuje ostrzeżenie (test niżej).
- **Bez wartości zastępczych.** Kod nie uzupełnia już pustych pól pozycji listy, więc strona pokazuje to, co wpisano. Każda z 5 pozycji ma wszystko wpisane jawnie. Menu i kafelki są bajt w bajt takie jak przed zmianą.
- **Studia podyplomowe są kierunkiem:** plik `kierunki/podyplomowe.md` w Web-Studia, adres bez zmian.
  - Mają jedną pozycję na liście z „pokaż w menu”; ręczny link zniknął z `nawigacja.json`.
  - Menu wygląda jak dziś: „Studia podyplomowe — kwalifikacje do nauczania”, a kafelek: „Nauczanie matematyki”.
- **Nowe pole „Nazwa w menu”** (`nazwa_menu`, PL i EN). Bez niego nazwa w menu musiałaby być taka sama jak na kafelku (patrz „Decyzje przyjęte samodzielnie”).
- **Strona podyplomowych** ma teraz szablon kierunku. Tekst jest identyczny, różnice w wyglądzie są drobne (zrzuty niżej). Poprawki tylko po Twojej decyzji.
- **Kontrole:**
  - `astro check`: 0 błędów;
  - `sprawdz_tresci.py`: OK;
  - `sprawdz_pola_cms.py`: 0 problemów (724 pliki, 16 repozytoriów);
  - symulacja formularza Pages CMS (zapis bez zmian): 724 pliki, 0 różnic;
  - kontrola zmian redaktorów: przed pushem 0 zapisów od bazy w obu repozytoriach. Wynik po pushu jest niżej.

## Commity

| Repozytorium | Commit | Treść |
|---|---|---|
| Web-Core | 0fa6731b | `kierunki.ts`, `menu.ts`, `DrugiEkran.astro`, `widoki/dzialStudia.ts`, ściągawka, `skrypty/migracja/kierunki_39.py` |
| Web-Ustawienia | 5ecbef7 | `.pages.yml` (formularz listy) i `ustawienia.json` (jawne wartości) w jednym commicie |
| Web-Ustawienia | f145d85 | „pokaż w menu” dla studiów podyplomowych, ręczny link usunięty z `nawigacja.json` |
| Web-Studia | b2a7c09 | `strony/studia/podyplomowe.md` → `kierunki/podyplomowe.md` |

## Etap 1. Bez automatu i bez wartości zastępczych

### Kod (Web-Core)
- **`src/lib/kierunki.ts`:**
  - `pozycjeKierunkow()` zwraca tylko pozycje listy. Przy kierunku z pliku dokleja ten plik (do kafelka), ale nie dopisuje kierunków spoza listy.
  - Dla każdego opublikowanego kierunku spoza listy wypisuje raz na budowę ostrzeżenie: „[kierunki] Kierunek <nazwa> nie jest na liście w Ustawieniach — nie ma go w menu ani w kafelkach (/studia/<id>; nie liczy się też w liczbach na stronie „Studia”)”.
  - `listaKierunkow()` (liczby na `/studia`) bierze tylko kierunki z listy, w jej kolejności. Nie ma już „spoza listy na końcu, alfabetycznie”.
  - Typ `PozycjaKierunku`: nowe `nazwa_menu`, `nazwa_menu_en`. Komentarze opisują nowe zasady.
- **`src/lib/menu.ts`:**
  - etykieta = `nazwa_menu`, opis = `opis_menu`, EN = `_en` albo polska wartość (ta zasada obowiązuje na całej stronie);
  - usunięte: pełna nazwa kierunku zamiast pustego opisu, skrót w miejsce nazwy.
- **`src/components/zal/DrugiEkran.astro`** (kafelki): bez „Kierunek” / „Programme” w pustym napisie nad nazwą i bez zdania z banera lub z treści w pustym opisie.
- **`src/lib/widoki/dzialStudia.ts`:** studia podyplomowe nie liczą się do „kierunków” ani „stopni studiów” (`jestPodyplomowe`), tak jak szkoła doktorska nie liczy się do kierunków.

### Migracja listy (Web-Ustawienia 5ecbef7, formularz i dane w jednym commicie)
`skrypty/migracja/kierunki_39.py lista` wpisuje do każdej pozycji to, co strona pokazywała dotąd. Wartości są liczone dawną logiką `menu.ts` i kafelków, łącznie z zastępczymi:

| Pozycja | Wpisane jawnie (dotąd liczone zastępczo) |
|---|---|
| Matematyka | nazwa w menu „Matematyka” / „Mathematics”; „pokaż w menu”, „pokaż na stronie głównej” |
| SIAD | nazwa w menu i opis w menu: pełna nazwa PL/EN („Sztuczna inteligencja w analizie danych”, „AI in Data Science” / „Artificial Intelligence in Data Science”) |
| ISIM | nazwa w menu „ISIM”, opis w menu: pełna nazwa PL/EN |
| Szkoła doktorska | nazwa w menu „Szkoła doktorska” / „Doctoral school” |
| Nauczanie matematyki | nazwa i opis w menu z ręcznego linku: „Studia podyplomowe” / „kwalifikacje do nauczania” (EN „Postgraduate studies” / „teaching qualifications”) |

Każda pozycja ma jawne `w_menu` i `na_stronie_glownej`. Oba pola działają w kodzie, a w formularzu mają `default: true`.

### Formularz listy (`.pages.yml` Web-Ustawienia)
- Nazwa listy: „Kierunki w menu „Studia” i kafelki na stronie głównej”. Usunąłem zdania o automacie („kierunek spoza listy pojawi się sam na końcu”) i o pustych polach.
- Opis listy: „Tylko pozycje z tej listy są w menu „Studia” (komputer i telefon), na stronie /studia i w kafelkach na stronie głównej, w kolejności listy. **Nowy kierunek pojawi się w menu i kafelkach dopiero po dodaniu go tutaj.** Strona pokazuje pola tak, jak są wpisane: puste pole zostaje puste.”
- Pola (każde z opisem: gdzie je widać, z przykładem):
  - Adres (wymagane), Nazwa w menu (wymagane, nowe), Opis w menu (wymagane);
  - Nazwa na kafelku (wymagane), Napis nad nazwą na kafelku, Zdanie na kafelku;
  - Pokaż w menu „Studia”, Pokaż kafelek na stronie głównej;
  - wersje EN.
  - Ukryte pole `pozycja` jak w zleceniu 31: CMS sprawdza wymagane pola także w nowej, pustej pozycji.

### Dokumentacja
- Zaktualizowałem komentarze w `kierunki.ts`, `menu.ts` i `DrugiEkran.astro`.
- `dok/sciagawka-edytora.md`: nowy kierunek trafia do menu i kafelków dopiero po dopisaniu na listę (robi to administrator). Wszystkie pola listy są jawne, a studia podyplomowe to kierunek.
- **PDF dla redaktorów.** Nie znalazłem źródła. `Web-Podglad/dla-redaktorow/` ma tylko gotowy PDF, ten sam co lokalny `Claude outputs/Mapa-CMS-IM-UWr.pdf`. Zdania do podmiany na stronie 2, w ramce „Jak dodać nowy kierunek”:
  - **Krok 3.**
    - Jest: „Po ok. 10 minutach strona kierunku działa, a kierunek sam pojawia się na końcu menu „Studia” i kafelków na stronie głównej.”
    - Ma być: „Po ok. 10 minutach strona kierunku działa pod adresem /studia/<nazwa-pliku>. W menu „Studia” i w kafelkach pojawi się dopiero po dopisaniu na listę w Ustawieniach (krok 4).”
  - **Krok 4.**
    - Jest: „Podpięcie i kolejność (administrator): Web-Ustawienia → lista „Kierunki w menu „Studia” i kafelki na stronie głównej”: adres /studia/<nazwa-pliku>, krótka nazwa do menu, opis kafelka, miejsce na liście.”
    - Ma być: „Menu i kafelki (administrator): Web-Ustawienia → Strona główna i kontakt → „Kierunki w menu „Studia” i kafelki na stronie głównej” → nowa pozycja: adres /studia/<nazwa-pliku>, nazwa i opis w menu, nazwa, napis i zdanie na kafelku (PL i EN), miejsce na liście. Strona pokazuje pola tak, jak są wpisane: puste pole zostaje puste.”

## Etap 2. Studia podyplomowe jako kierunek

### Przeniesienie (Web-Studia b2a7c09)
`skrypty/migracja/kierunki_39.py przenies` przenosi `strony/studia/podyplomowe.md` do `kierunki/podyplomowe.md` (git rozpoznaje to jako przeniesienie). Mapowanie pól:
- `tytul` → `nazwa`, `tytul_en` → `nazwa_en`;
- `opis`, `haslo` (PL/EN) → `baner.opis`, `baner.haslo` (PL/EN);
- `liczby[].n` → `baner.liczby[].wartosc`, etykiety PL/EN bez zmian;
- `format_tresci: jawne`, `opublikowany: true`, `tresc_en` i tekst PL z komentarzami `<!-- … -->` bez zmian. Skrypt sprawdza równość danych przed zapisem.

Strona nie miała nadtytułu, więc baner też go nie ma. Pliki w `public/pliki/studia/podyplomowe/` zostały bez zmian. Kontrola pole po polu: przeniesionych 19 pól, wartości bez zmian, nic nie dodano poza strukturą banera.

### Jedna pozycja na liście (Web-Ustawienia f145d85)
- „Nauczanie matematyki”: `w_menu: true`.
- Ręczny link „Studia podyplomowe — kwalifikacje do nauczania” usunięty z grupy „Kierunki” w `nawigacja.json`. Grupa zostaje i dalej bierze kierunki z listy.
- Menu (komputer i hamburger, PL i EN) jest bajt w bajt takie jak dziś. Kafelek na stronie głównej dalej nazywa się „Nauczanie matematyki”.

### Wygląd strony `/studia/podyplomowe` (szablon kierunku)
Tekst widoczny na stronie jest identyczny (PL i EN). Różnice w wyglądzie:
1. **Baner:** inny fakt i rysunek patrona. Szablon kierunku dobiera patrona po swojemu.
2. **Liczby** (3 semestry, 380 godzin zajęć, 90 godzin praktyk) mają styl liczb kierunku (`kh-liczby`), są nieco wyższe.
3. **Sekcje** są opakowane w `<section id>` z tymi samymi id, więc kotwice i spis „Na tej stronie” działają jak dotąd. Kreska oddzielająca przesunęła się pod pierwszą sekcję.
4. **Wysokość strony:** +19 px na komputerze, +39/40 px na telefonie.

Zrzuty (lokalnie, `raport-zrzuty/`): `z39-podyplomowe-1440-przed.png` / `z39-podyplomowe-1440.png`, `-390`, `-en-1440`, `-en-390` (każdy przed i po).

Nie poprawiałem tego. Jeśli wolisz dawny wygląd któregoś elementu, napisz którego.

### Odwołania
- **Linki do `/studia/podyplomowe`:** 384 linki w 378 plikach, przed i po tyle samo, adres bez zmian. Linkują m.in. strona główna, `/studia`, szkoła doktorska i specjalność „Nauczycielska” (`/studia/matematyka/matematyka-nauczycielska`, 2 linki).
- **Mapa strony:** te same adresy, inna kolejność.
- **Okruszki** „← Studia”, **„Następna strona w dziale → Plan zajęć”** i tytuł karty są bez zmian. Inne strony mają bajt w bajt ten sam HTML, więc „Następna strona” na nich też się nie zmieniła.

## Odbiór lokalny

### Porównanie HTML przed/po
- **Przed:** budowa z `main` po zleceniu 31 i 41, z dzisiejszymi danymi.
- **Po:** nowy kod z nowymi danymi.

Wyniki:
- 757 stron, w tym menu „Studia”, panel hamburgera, `/studia`, strona główna z kafelkami i 4 kierunki PL i EN: **0 różnic** w HTML.
- Różnią się tylko `/studia/podyplomowe` i `/en/studia/podyplomowe` (opis wyżej), a poza HTML: znacznik czasu w `seminaria/powiadomienia.json`, DTSTAMP w `.ics` i kolejność w `sitemap.xml`.
- Tekst widoczny we wszystkich 885 plikach: 0 różnic.

### Stany pośrednie między pushami
Każdy stan, który może być na żywo między kolejnymi pushami, zbudowałem i porównałem z „przed”:
- stary kod + nowa lista (Web-Ustawienia 5ecbef7): 0 różnic;
- nowy kod + nowa lista: 0 różnic;
- nowy kod + lista z podyplomowymi w menu (f145d85) + stara strona podyplomowych: 0 różnic względem „przed”;
- nowy kod + lista 5ecbef7 + przeniesiona strona: 0 różnic względem „po”.

Kolejność pushy treści była więc bez znaczenia dla wyglądu.

### Test automatu
Dodałem lokalnie `kierunki/test-spoza-listy.md`. Wynik:
- budowa wypisała ostrzeżenie;
- strona `/studia/test-spoza-listy` zbudowała się i działa;
- kierunku nie ma w menu, w hamburgerze, w kafelkach ani w liczbach na `/studia`.

Po teście plik usunąłem.

### Kontrole
- `npx astro check`: 0 błędów.
- `skrypty/sprawdz_tresci.py`: OK (565 plików).
- `skrypty/sprawdz_pola_cms.py` na wszystkich 16 repozytoriach (Web-Ustawienia i Web-Studia w wersji zlecenia 39): 724 pliki, 0 problemów.
- `skrypty/test-edytora/formularz.mjs`: zapis bez zmian w nowej konfiguracji, 724 pliki, 0 różnic.

## Ochrona zmian redaktorów
Kontrola: skrypt `kontrola39.py` (w notatkach sesji; robi to samo co `kontrola_redaktorow.py` z 31, ale dla pól tego zlecenia).
- **Baza:** Web-Ustawienia 3f6bca2, Web-Studia b76a2c6 (`main` po zleceniu 31).
- **Przed pushem:** w obu repozytoriach 0 zapisów redaktorów od bazy. Sprawdzałem tuż przed każdym pushem: Web-Ustawienia o 01:58 i 02:00, Web-Studia o 02:00. Za każdym razem wypychany commit był potomkiem `origin/main`, czyli push bez scalania.
- **Po pushu** (pole po polu, przed i po):
  - Web-Ustawienia 3f6bca2..5ecbef7:
    - `.pages.yml`: tylko formularz listy `studia.kierunki` (opis listy, nowe pola `nazwa_menu`, `nazwa_menu_en`, `pozycja`, nowe etykiety, opisy, wymagania, kolejność);
    - `ustawienia.json`: tylko `studia.kierunki[0–4]` (dopisane `nazwa_menu`, `nazwa_menu_en`, `w_menu`, `na_stronie_glownej`, a przy SIAD, ISIM i podyplomowych `opis_menu`, `opis_menu_en`). 25 pól, każde dopisane, żadne nie zmienione ani usunięte.
  - Web-Ustawienia 5ecbef7..f145d85:
    - `ustawienia.json`: `studia.kierunki[4].w_menu` false → true;
    - `nawigacja.json`: `menu[2].grupy[0].linki[0]` (ręczny link „Studia podyplomowe — kwalifikacje do nauczania”) usunięty.
  - Web-Studia b76a2c6..b2a7c09: `strony/studia/podyplomowe.md` → `kierunki/podyplomowe.md`. Wszystkie 19 pól jest pod nowymi nazwami z tymi samymi wartościami, a tekst PL bez zmian. Innych plików push nie zmienił.
- **Następnego dnia** (do 19.11, ok. 02:00) trzeba przejrzeć zapisy redaktorów w Web-Studia i Web-Ustawienia:
  - czy ktoś nie odtworzył `strony/studia/podyplomowe.md` (stary formularz „Strony” otwarty przed pushem);
  - czy nikt nie usunął nowych pól listy.

  Znalezione trzeba poprawić osobnym commitem.

## Push (18.11, tryb samodzielny)
Warunki z trybu samodzielnego: wszystkie kontrole przeszły; kontrola redaktorów nie znalazła utraconej zmiany. Przed pushem Web-Core zrobiłem `fetch` i `rebase` na `origin/main`, na którym było już zlecenie 41 (`4511613b`, tylko przekaźnik). Po rebase powtórzyłem budowę (`z39-final`): 0 różnic względem budowy sprzed rebase.

| Godzina | Push | Podgląd |
|---|---|---|
| 01:58 | Web-Ustawienia 3f6bca2..5ecbef7 | przebieg przerwany przez kolejny (zlecenie 41: nowa budowa przerywa poprzednią) |
| 01:58 | Web-Core 4511613b..0fa6731b | przekaźnik → „przebuduj”, run 44212184796: **success** (kod 39 + lista 5ecbef7) |
| 02:00 | Web-Ustawienia 5ecbef7..f145d85, Web-Studia b76a2c6..b2a7c09 | run 44212524231: **success** |

Strona na żywo po ostatniej budowie, z pominięciem skrótów plików `_astro`, wygląda tak:
- strona główna, `/studia` (PL, EN): identyczne z lokalną budową;
- `/studia/podyplomowe` (PL, EN), `/studia/matematyka`, `/studia/siad`: różni się tylko adres strony w linku „Zgłoś błąd” (Web-Podglad zamiast Web-Core);
- `sitemap.xml`: ma `/studia/podyplomowe`.

Nie wypychałem gałęzi roboczych. Lokalne `praca/39-kierunki` w Web-Core, Web-Ustawienia i Web-Studia są równe `origin/main`.

## Decyzje przyjęte samodzielnie
1. **Osobne pole „Nazwa w menu” (`nazwa_menu`, wymagane, PL/EN).** Przyjąłem tę rekomendację, bo zlecenie ją przewiduje, gdy lista nie pozwala na inną nazwę w menu niż na kafelku. Dzięki temu:
   - nazwa na kafelku „Nauczanie matematyki” zostaje bez zmian;
   - menu wygląda jak dziś („Studia podyplomowe”).

   Dawne pole „Nazwa w menu i na kafelku” służy teraz tylko kafelkowi („Nazwa na kafelku”) i jest wymagane. Wymagane są też „Nazwa w menu” i „Opis w menu”.
2. **Liczby na `/studia` tylko z kierunków z listy.** Przyjąłem, bo „bez automatu spoza listy”. Dotąd kierunek spoza listy zmieniał liczbę kierunków bez wiedzy redaktora.
3. **Studia podyplomowe nie liczą się do „kierunków” ani „stopni studiów” na `/studia`.** Przyjąłem, bo po przeniesieniu liczba zmieniłaby się z 3 na 4, a wygląd ma zostać bez zmian.
4. **Kolejność pushy: lista (Web-Ustawienia 5ecbef7) przed Web-Core.** To odstępstwo od „najpierw Web-Core, potem treści”. Przyjąłem je, bo:
   - nowy kod nie ma już wartości zastępczych, więc ze starą listą pokazałby puste nazwy w menu;
   - stary kod z nową listą buduje identyczną stronę (sprawdzone).

## Pytania
1. **Skrót SIAD w menu.** W polu „Nazwa w menu” jest pełna nazwa „Sztuczna inteligencja w analizie danych”. Strona pokazuje ją jako „SIAD” z pełną nazwą w podpowiedzi. To stała reguła wyświetlania (`skrotNazwy` w `patroni.ts`, także w spisie działu), a nie wartość dla pustego pola, więc zostawiłem ją, by wygląd się nie zmienił. Opis pola o tym mówi. Czy wolisz wpisać „SIAD” wprost i usunąć regułę? Wtedy zniknie podpowiedź z pełną nazwą.
2. **Wygląd strony podyplomowych:** różnice z sekcji „Wygląd strony” (patron, styl liczb, kreska). Zostawić szablon kierunku czy coś przywrócić?
3. **PDF dla redaktorów:** podmienić zdania z kroków 3–4 (wyżej). Źródła PDF nie ma w repozytoriach.

## Uwaga dla zlecenia 33
Nowy plik `kierunki/podyplomowe.md` ma już `opublikowany: true` (przeniesione ze strony). Migracja 33 ma go objąć tak jak pozostałe kierunki.

## Kryteria odbioru
- [x] Menu, hamburger, pole kierunków i kafelki pokazują tylko pozycje z listy. Kierunek spoza listy ma stronę, ale nie pojawia się sam.
- [x] W kodzie nie ma wartości zastępczych dla pozycji listy. Lista ma wszystko wpisane jawnie, wygląd bez zmian.
- [x] Studia podyplomowe są kierunkiem z jedną pozycją na liście, ręczny link zniknął z menu, menu wygląda jak dziś.
- [x] Formularz listy z jasnymi opisami. Ściągawka zaktualizowana, a zdania do podmiany w PDF są wypisane.
- [ ] Kontrola zmian redaktorów przed i po pushu jest w raporcie (zrobiona; wszystkie zapisy zachowane, bo od bazy nie było żadnego). Przegląd z następnego dnia: do zrobienia 19.11, ok. 02:00.

## Przegląd zapisów redaktorów po pushu (18.11, 11:20, częściowy; okno 24 h kończy się 19.11 ok. 02:00)
- Web-Ustawienia (`origin/main` = `f145d85`) i Web-Studia (`origin/main` = `b2a7c09`): od pushu nie było żadnego zapisu.
- Nikt więc nie odtworzył `strony/studia/podyplomowe.md` ani nie usunął nowych pól listy.
- Do powtórzenia po 02:00 19.11.

## Decyzje właściciela (18.11, ok. 13:05)
1. **SIAD:** zostaje reguła `skrotNazwy` (wygląd bez zmian).
2. **Strona podyplomowych:** zostaje szablon kierunku.
3. **PDF dla redaktorów:** przygotuję poprawiony PDF ze zdaniami z kroków 3 i 4 (`Web-Podglad/dla-redaktorow/`).

## PDF dla redaktorów (decyzja 18.11; push 13:34)
- Źródła PDF nie było. Odtworzyłem je jako `dok/dla-redaktorow/mapa-cms.html` w Web-Core (`fb54f3f5..5772282f`, `[skip ci]`); PDF robi `node skrypty/pdf-dla-redaktorow.mjs <katalog>` w Edge, z kontrolą liczby stron.
- **Web-Podglad `e64e6a8..f2fe4af`** (`[skip ci]`, bez przebudowy): nowy `dla-redaktorow/Mapa-CMS-IM-UWr.pdf`, dwie strony A4.
- **Zmiany w treści:**
  - kroki 3 i 4 w ramce „Jak dodać nowy kierunek” w brzmieniu z tego raportu;
  - kroki 1 i 2: jeden formularz „Kierunki” z banerem (osobnego formularza „Baner” nie ma od zleceń 28–29);
  - strona 1: Studia podyplomowe wśród kierunków (nie ma ich już w Stronach studiów); kierunki i specjalności w jednym formularzu; w Ustawieniach lista kierunków w menu „Studia”;
  - data „stan na 18 listopada 2026”.
- **Strona 2:** tabela „Układy, które strona rozpoznaje sama” opisuje stare rozpoznawanie. Dopisałem tylko, gdzie ono dziś działa (strony działów Instytut i Nauka, Strony z „Bloki”), i wiersz o jawnych blokach w Studiach i Popularyzacji. Całą tabelę przepisze zlecenie 40 (punkt „Na koniec”).
- Wygląd zbliżony do pierwszej wersji (kolory działów, układ), czcionka systemowa zamiast DejaVu Sans.
