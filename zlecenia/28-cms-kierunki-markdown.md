# Zlecenie 28: kierunki jako jeden Markdown, bloki z tekstu (GOTOWE, 7.11.2026)

Pierwsze z trzech zleceń „sprzątania CMS” (28 → 29 → 30, **po kolei, nie równolegle**). 29 i 30 budują na tym, co powstanie tutaj.

**Tryb bez nadzoru** (decyzja właściciela 7.11, 01:14). Właściciel może puścić 28, 29 i 30 jednym poleceniem i odejść. Wtedy:
1. Robisz etapy lokalne 28 → 29 → 30 bez czekania. Następne zlecenie startuje, gdy poprzednie spełnia kryteria odbioru lokalnego (etapy 6 i 6a). Jeśli nie spełnia i nie umiesz tego naprawić, kończysz raportem i **nie** zaczynasz następnego.
2. Pytania nie zatrzymują pracy: wybierz najrozsądniejsze rozwiązanie, zapisz w raporcie „przyjąłem …, bo …” i idź dalej.
3. Push i test w prawdziwym CMS robicie **razem na końcu**, z właścicielem, dla wszystkich trzech zleceń (etapy 7–8 tego zlecenia przechodzą na koniec zlecenia 30).
4. Edytorzy: niczego nie wstrzymujesz, bo do pushu wszystko jest lokalne. Stan gałęzi domyślnej zapisz w raporcie. Przed pushem `git pull --rebase` w klonach; konflikty pokazujesz właścicielowi.
5. Zamiast testu w CMS przed zleceniem 29 jest test automatyczny zapisu edytora (etap 6a).

**Cel.** Edytor kierunku (Matematyka, ISIM, SIAD, Szkoła doktorska) dostaje jeden tekst zamiast ok. 100 pól. Formularz kierunku to: Nazwa, Treść, Nazwa EN, Treść EN. Baner kierunku jest w osobnym formularzu. Menu i kafelki kierunków są poziom wyżej, w jednej liście. Strona ma wyglądać tak samo jak dziś, poza różnicami wypisanymi w etapie 6.

**Decyzje właściciela (7.11, 00:10–01:00)**
- „Najlepiej jeden duży Markdown; strona bierze ten Markdown i wrzuca na swoje formatowanie, ale edytor musi mieć ułatwione zadanie.” Gdzie się nie da, zostają pola.
- W formularzu najpierw Markdown (PL, potem EN), dopiero pod nimi drobne pola.
- Tekst kierunku i pola banera to **osobne formularze** (osobne pliki, bo Pages CMS przy zapisie usuwa z pliku pola spoza formularza).
- Menu i kafelki kierunków: jedna lista dla wszystkich, w Web-Ustawienia (decyduje tylko właściciel). Kolejność = kolejność na liście.
- Program studiów: zakładki z nagłówków `###`, **bez** listy „Rozpocząłem studia w roku…”.
- Oś studiów z listy numerowanej; edytor nie musi pamiętać Shift+Enter (strona skleja kroki).

**Gdzie i jak**
- **Start dopiero po zleceniach 23–27** (sprawdź w `.przekazanie\dziennik.md`). Jeśli któreś nie jest skończone, zatrzymaj się i zapytaj właściciela. Ten sam zestaw plików (np. `Kierunek.astro`, `zal-tresc.css`, klony treści) ruszają też tamte zlecenia.
- Kod: `C:\Users\Szymek\Documents\GitHub\Web-Core`, gałąź `wyglad/zlecenie-16`. Treści: klony `C:\Users\Szymek\Documents\GitHub\tresci\<Repozytorium>`, ta sama gałąź (Web-Podglad szuka treści na gałęzi o tej samej nazwie co kod).
- **Bez pushowania** do etapu 7. Osobny commit na etap w każdym repozytorium, którego etap dotyczy.
- `skrypty/pobierz_tresci.py` tylko z `--lokalnie` albo `--galaz wyglad/zlecenie-16`.
- Danych nie kasujemy bez śladu: wszystko, co skrypt przenosi, ma trafić w nowe miejsce albo do raportu jako „pominięte, bo …”.
- Dziennik w `.przekazanie\dziennik.md`, raport `RAPORT-ZLECENIE-28.md`, zrzuty `raport-zrzuty/z28-*`.
- **Oszczędnie (tokeny i czas, decyzja właściciela 7.11):** bez subagentów; czytaj pliki wymienione w zleceniu i to, co znajdzie wyszukiwanie, nie całe katalogi; porównanie przed/po skryptem, w raporcie tylko lista różnic (bez wklejania HTML); dziennik i raport zwięzłe.
- Załączniki: `28-zalaczniki\szkic_konwersji_kierunkow.py` (szkic formatu, nie gotowy skrypt) i `28-zalaczniki\wzor\` (jego wynik dla 4 kierunków: docelowy Markdown PL i EN, baner, przypomnienia, menu). Liczby w zleceniu policzono na stanie z GitHuba: Web-Studia `910f99c`, Web-Core `b4f99c25` (6.11). Jeśli numer 28 jest zajęty, użyj kolejnego i napisz to w raporcie.

## Etap 0. Stan wyjściowy i zdjęcie „przed”
1. W Web-Core i w klonach Web-Studia, Web-Ustawienia: `git fetch`, `git status`, czysto i równo z `origin/wyglad/zlecenie-16`. Lokalne commity wypisz w raporcie.
2. **Edytorzy.** Sprawdź gałąź domyślną Web-Studia i Web-Ustawienia (`gh repo view IM-UWr/<repo> --json defaultBranchRef`). Jeśli to już `wyglad/zlecenie-16` (edytorzy mogą pisać), poproś właściciela o przerwę dla edytorów tych dwóch repozytoriów od etapu 4 do pushu w etapie 7 i zapisz to w raporcie (w trybie bez nadzoru: punkt 4 wyżej). Tuż przed etapem 4: `git pull --rebase`.
3. Zbuduj stronę z treściami z klonów w osobnym worktree (jak w zleceniach 22–25) i zachowaj wynik jako **„przed”**: wszystkie strony `/studia/<kierunek>` i `/en/studia/<kierunek>`, strona główna, `/studia`, menu, kalendarium i pliki `.ics`.

## Etap 1. Bloki z Markdownu (`src/plugins/rehype-bloki.mjs`)
Dziś wtyczka działa tylko przy `bloki: true` i zakłada osobne akapity w punkcie listy. Edytor Pages CMS (TipTap) ich nie robi: **Enter w liście tworzy nowy punkt**, a Shift+Enter zapisuje złamanie linii (`"  \n"`, czyli `<br>` w jednym akapicie). Wtyczka ma rozumieć oba zapisy.

**Linie punktu.** Treść punktu dzielimy na „linie”: osobne akapity oraz kawałki akapitu rozdzielone `<br>`. Pierwsza linia może zawierać pogrubienie i dalszy tekst po separatorze ` — `, ` – ` albo `: ` (separator usuwamy).

| Zapis w Markdownie | Wynik (klasy jak dziś w `zal-tresc.css`) |
|---|---|
| lista punktowana, każdy punkt zaczyna się pogrubieniem | kafelki `ul.dwa`: `<b>` tytuł, `<span>` reszta pierwszej linii |
| lista numerowana, pierwszy punkt zaczyna się pogrubieniem | oś `ol.etapy`. Pogrubienie „Etykieta: Tytuł” → `span.etyk` = Etykieta, `p.t` = Tytuł; bez dwukropka etykieta „Krok N” / „Step N” jak dziś. Reszta pierwszej linii → akapit opisu |
| w punkcie (kafelek, oś, kontakt): linia „Klucz: wartość” (klucz ≤ 20 znaków, zwykły tekst) | para w `dl.para` |
| w punkcie: linia z samym linkiem | `p.akcja` |
| **wyrozumiałość:** punkt listy numerowanej, który nie zaczyna się pogrubieniem | doklejany do poprzedniego kroku jako kolejne linie (edytor wcisnął Enter zamiast Shift+Enter) |
| lista punktowana: pierwsza linia kursywą (rola), dalej pogrubienie (osoba) w tej samej albo następnej linii | `.kontakty`: `span.etyk` rola, `<b>` osoba, pary z kolejnych linii („e-mail”, „tel.”, „pokój”) |
| lista, w której każdy punkt to sam link (opcjonalnie ` — opis`) | gdy choć jeden link prowadzi do pliku (rozszerzenie w adresie albo `/pliki/`): `ul.pliki` z ikoną i znacznikiem typu (PDF, DOCX…, „strona”/„page”), opis jako `<small>`; inaczej `ul.linki` |
| `###` zakończony „?” | pytanie `.faq` (`details`/`summary`), odpowiedź = wszystko do następnego nagłówka |
| tabela Markdown | `table.tab` (na telefonie bloki, jak dziś) |
| cytat zaczynający się pogrubieniem | ramka uwagi (bez zmian) |

**Kotwice** (nagłówek `##` o konkretnej nazwie, porównanie bez wielkości liter, PL i EN). Jedno wspólne miejsce w kodzie z listą kotwic, bo zlecenia 29–30 dopiszą swoje:
- „Specjalności” / „Specialisations”: pod nagłówkiem (i pod tekstem, jeśli edytor go dopisał) strona wstawia kafelki specjalności, jak dziś. Brak nagłówka → sekcja na końcu treści. Kierunek bez specjalności → nagłówek bez kafelków się nie wyświetla.
- „Program studiów” / „Curriculum” / „Program kształcenia” / „Programme”: `###` w tej sekcji to zakładki (`.tresc-taby`, skrypt przełączania z `Kierunek.astro` bez listy roku). Jedna podsekcja albo brak `###` → bez zakładek. Bez JS wszystkie programy jeden pod drugim, z podpisami, jak dziś.

**Gdzie działa:** kierunki zawsze; strony z `bloki: true` jak dziś; zlecenie 29 dopisze specjalności. Reguła „pierwszy akapit po pierwszym `##` → `.wst`” nie może zmienić wyglądu kierunków (wyłącz ją tam, jeśli zmienia).

**Testy:** fikstury z `28-zalaczniki\wzor\` plus warianty: oś wpisana samymi Enterami, kafelek z opisem po Shift+Enter, kontakt z rolą i nazwiskiem w jednej linii, lista mieszana (plik + strona), pytanie bez „?” (zostaje zwykłym `###`). Jeden plik testów, krótkie przypadki.

## Etap 2. Model danych
| Kolekcja / plik | Repozytorium | Pola |
|---|---|---|
| `kierunki` — `src/content/kierunki/<id>.md` | Web-Studia | `nazwa`, `nazwa_en`, treść PL (body), `tresc_en` |
| `kierunki_baner` — np. `src/content/kierunki-baner/<id>.json` (format wybierz tak, żeby czytały go bez zabiegów i Astro, i Pages CMS) | Web-Studia | `podtytul`, `opis`, `haslo`, `liczby[]` (`wartosc`, `etykieta`, `etykieta_krotka`), każde z `_en` |
| przypomnienia — `src/data/przypomnienia.json` | Web-Studia | lista: `sprawa`, `sprawa_en`, `data`, `co_roku`, `dni_przed`, `adres`, plus ukryte pole na stały UID (niżej) |
| menu i kafelki — `src/data/ustawienia.json` → `studia.kierunki` (dziś „Dodatkowe kafelki”) | Web-Ustawienia | lista: `adres`, `nazwa`, `poziom`, `opis` (kafelek), `opis_menu`, każde z `_en`; `w_menu`, `na_stronie_glownej` |

- **Brak pliku banera** → baner z samą nazwą, zdanie pod nazwą = pierwsze zdanie treści, bez liczb i hasła (strona bezobsługowa: nowy kierunek działa bez zaglądania do banera).
- **Kierunek spoza listy menu** → pojawia się sam na końcu menu „Studia” i kafelków, z pełną nazwą, poziomem „Kierunek” / „Programme” i zdaniem z banera.
- Lista menu po migracji: Matematyka, SIAD, ISIM, Szkoła doktorska (dzisiejsza `kolejnosc`), potem Studia podyplomowe (`w_menu: false`, bo dziś nie ma ich w menu). Menu i kafelki mają wyjść identyczne jak dziś.
- **Przypomnienia:** `tresci.ts` (ok. linii 287) bierze je z nowego pliku zamiast z `terminy` kierunków. **UID w `.ics` trzech istniejących przypomnień Matematyki nie może się zmienić** (dziś `termin-matematyka-<indeks>-<data>`), inaczej subskrybenci kalendarza dostaną duplikaty. Zachowaj stary UID w ukrytym polu, nowe pozycje dostają UID z adresu i sprawy.
- Zaktualizuj wszystkie miejsca, które czytają stare pola kierunków: m.in. `menu.ts`, `zal/DrugiEkran.astro`, `widoki/dzialStudia.ts`, `widoki/specjalnosc.ts`, `sciezki.ts`, `motywyBanerow.ts`, `sitemap.xml.ts` (pełna lista: wyszukaj w `src/`).

## Etap 3. Szablon `Kierunek.astro`
- Treść: Markdown z body (PL) albo `tresc_en` (EN; puste → polski z `lang="pl"`, jak dziś) przez wtyczkę bloków. Spis „Na tej stronie” z nagłówków `##`. Krótsze etykiety spisu Szkoły doktorskiej („O Kolegium”, „Pytania”, „Akty prawne”) zachowaj prostą mapą w kodzie albo zgłoś różnicę.
- Baner z `kierunki_baner` (liczby na telefonie i komputerze jak dziś, ta sama logika skracania).
- Usuń wpisane w kod zdania „Szczegóły egzaminów…” (`linkDyplom`) i „Wszystkie formularze…”: są teraz w treści i edytor może je zmienić.

## Etap 4. Skrypt migracji
`skrypty/migracja/kierunki.*` (Python albo TS; TS pozwala użyć `tytulyEn()` do nazwisk w kontaktach EN). Wzorem jest szkic i jego wynik w `28-zalaczniki\`. Skrypt:
1. Przerabia 4 pliki kierunków w klonie Web-Studia: zostają `nazwa`, `nazwa_en`, body, `tresc_en`. Kolejność sekcji i nagłówki PL/EN jak dziś na stronie (szkic je zawiera, także osobne nagłówki Szkoły doktorskiej).
2. Zapisuje pliki banerów, `przypomnienia.json` i listę w `ustawienia.json` (klon Web-Ustawienia), z zachowaniem „Dodatkowych kafelków”.
3. Wersja EN każdej wartości z tą samą zastępczością co dziś (`wybierz()`: puste `_en` → polskie), żeby strona EN wyszła taka sama.
4. Odmawia ponownego uruchomienia na już przerobionych plikach. Wypisuje statystykę: ile wartości przeniesiono, ile pominięto i dlaczego.

Po migracji popraw ręcznie jedną odpowiedź w pytaniach Matematyki (PL i EN): „Wybierz swój rok w sekcji „Program studiów”” → „Wybierz zakładkę ze swoim programem w sekcji „Program studiów””. Listy roku już nie ma. Sprawdź podobne odwołania w pozostałych kierunkach i wypisz w raporcie.

## Etap 5. Formularze (`.pages.yml`)
**Web-Studia**, grupa „Kierunki” (`type: group`):
- „Treść”: Nazwa · **Treść** (`rich-text`, `format: markdown`) · Nazwa EN · **Treść EN** (`rich-text`, `format: markdown`; dziś gołe pole `text`). Media przy treści: `public/pliki/studia`.
- „Baner”: Nadtytuł · Zdanie pod nazwą · Hasło · Liczby (Wartość, Podpis, Krótszy podpis na telefon) · wersje EN pod spodem.
- Osobny formularz „Przypomnienia o terminach” (strona główna i aktualności): Sprawa, Data, Co roku, Ile dni wcześniej (domyślnie 14), Link, wersja EN; UID ukryty.
- Opis pola „Treść” = ściągawka dla edytora (poniżej, dosłownie albo krócej, jeśli Pages CMS ucina długie opisy). Ten sam tekst w `dok/sciagawka-edytora.md`.

**Web-Ustawienia:** „Sekcja Studiuj matematykę” → lista „Kierunki w menu „Studia” i kafelki na stronie głównej (kolejność = kolejność na liście; kierunek spoza listy pojawi się sam na końcu)”.

**Ściągawka:**
> Piszesz jak w zwykłym edytorze. Kilka układów strona rozpoznaje sama:
> • Nagłówek 2 = nowa sekcja (pojawi się w spisie „Na tej stronie”).
> • Punkt listy zaczynający się pogrubieniem = kafelek (np. „Dlaczego warto”).
> • Lista numerowana z pogrubionym początkiem = oś kroków. W pogrubieniu tekst przed dwukropkiem to mała etykieta: „Semestry 1–2: Podstawy”.
> • W punkcie linia „Termin: …” albo „Formularz: …” = para; sam link w linii = przycisk. Kolejną linię w tym samym punkcie dodasz Shift+Enter (zwykły Enter też zadziała).
> • Nagłówek 3 zakończony znakiem „?” = rozwijane pytanie.
> • Lista samych linków = lista plików (PDF / strona).
> • Punkt z rolą kursywą i nazwiskiem pogrubionym = kontakt.
> • Pod nagłówkiem „Specjalności” strona sama wstawi kafelki specjalności; pod „Program studiów” nagłówki 3 stają się zakładkami.
> • Plik PDF: wgraj w „Media” i wklej link.

Zaktualizuj `skrypty/sprawdz_pola_cms.py` o nowe kolekcje i pliki. Wynik: 0 problemów.

## Etap 6. Odbiór lokalny
- Zbuduj stronę z treściami z klonów (osobny worktree) jako **„po”** i porównaj z „przed” (HTML po normalizacji: białe znaki, kolejność atrybutów, nazwy zasobów z hashami). Strony: 4 kierunki PL i EN, `/studia`, strona główna, menu, kalendarium, `.ics`.
- **Dozwolone różnice:** brak listy wyboru roku przy programach; zdania „Szczegóły egzaminów…” i „Wszystkie formularze…” jako zwykły akapit (jeśli styl się zmienił); poprawione zdanie w pytaniu o program; etykiety spisu, jeśli zgłoszone. **Każda inna różnica to błąd do poprawki albo pytanie w raporcie.**
- **Zrzuty tylko tam, gdzie porównanie HTML pokazało różnicę:** strona z różnicą, przed/po, 1440 i 390 px, tylko PL. Bez różnic nie rób zrzutów; porównanie HTML wystarcza.
- `sprawdz_pola_cms.py`: 0 problemów. `skrypty/sprawdz_tresci.py`: OK. `astro check`: bez nowych błędów. Testy wtyczki: zielone.

## Etap 6a. Symulacja zapisu w edytorze
Pages CMS zapisuje pole `rich-text` przez TipTap z `@tiptap/markdown` (wersje 3.x; rozszerzenia: StarterKit, Underline, Link, Image, Table, TableRow, TableHeader, TableCell). W osobnym skrypcie testowym (zależności tylko w `skrypty/test-edytora/`, nie w kodzie strony) przepuść każdy przerobiony plik treści (PL i EN) przez wczytanie i zapis tym edytorem, zbuduj stronę i porównaj z wynikiem „po”. Każda różnica to poprawka wtyczki: ma przyjmować to, co zapisuje edytor. Sprawdź też wzór `$\ell^2$` w akapicie. Limit: ok. 30 minut pracy. Jeśli TipTapa nie da się uruchomić bez przeglądarki, pomiń, zapisz w raporcie i zostaw to na test właściciela w etapie 8.

**Stop.** Raport i czekanie na „push”. W trybie bez nadzoru: od razu zlecenie 29.

## Etap 7. Po słowie „push” (w trybie bez nadzoru: na końcu zlecenia 30, razem z 29 i 30)
1. Wypchnij `wyglad/zlecenie-16` w Web-Studia, Web-Ustawienia i Web-Core razem (treści i kod muszą przyjść naraz).
2. Sprawdź najbliższy przebieg Web-Podglad i strony kierunków na podglądzie.
3. Załóż i wypchnij `test-cms` od `wyglad/zlecenie-16` w Web-Studia i Web-Ustawienia. Daj znać właścicielowi.

## Etap 8. Test w prawdziwym CMS (właściciel, potem Ty)
Właściciel w `https://app.pagescms.org/IM-UWr/Web-Studia/test-cms` (i Web-Ustawienia), jako edytor:
1. Matematyka → Treść: otwórz i zapisz **bez zmian**.
2. Dodaj wiersz do tabeli terminów.
3. Dodaj krok na osi, wciskając zwykły Enter między liniami.
4. Dodaj pytanie (Nagłówek 3 z „?”) z odpowiedzią.
5. Wgraj PDF w „Media” i podlinkuj go w „Aktach prawnych”.
6. Wpisz wzór `$\ell^2$` w zwykłym akapicie.
7. Zmień jedno słowo w Treści EN.
8. Matematyka → Baner: zmień hasło. Ustawienia: przesuń jeden kierunek na liście.

Potem Ty: porównaj `origin/test-cms` z `wyglad/zlecenie-16`, zbuduj stronę z `test-cms` i sprawdź każdy punkt. Dopuszczalne: zmiany zapisu Markdownu bez zmiany wyniku na stronie. Niedopuszczalne: inny wygląd po zapisie bez zmian (punkt 1), zgubione pola, zepsuty wzór, rozsypana tabela. Wynik do raportu. Jeśli coś się psuje: niczego nie scalaj, opisz i zaproponuj poprawkę (wtyczka ma przyjmować to, co zapisuje edytor). Po pozytywnym wyniku usuń `test-cms`.

## Kryteria odbioru
- [ ] Formularz kierunku: Nazwa, Treść, Nazwa EN, Treść EN; baner osobno; przypomnienia osobno; menu i kafelki w Ustawieniach.
- [ ] Wszystkie wartości z 4 starych plików są w nowych plikach albo w raporcie jako pominięte z powodem.
- [ ] Porównanie przed/po: tylko dozwolone różnice. Menu, kafelki, kalendarium i UID w `.ics` bez zmian.
- [ ] Wtyczka bloków: testy zielone, w tym oś wpisana samymi Enterami.
- [ ] Nowy kierunek bez pliku banera i spoza listy menu buduje się i pojawia w menu i kafelkach (sprawdź na próbnym pliku, potem go usuń).
- [ ] `sprawdz_pola_cms.py` 0 problemów, `sprawdz_tresci.py` OK, `astro check` bez nowych błędów.
- [ ] Etap 6a: symulowany zapis w edytorze nie zmienia strony (albo zapisany powód pominięcia).
- [ ] Po etapie 8: zapis bez zmian daje tę samą stronę; punkty 2–8 działają.

## Raport (`RAPORT-ZLECENIE-28.md`)
Jeden raport na koniec zlecenia (bez raportów cząstkowych): tabela etapów i commitów (repozytorium, commit, opis); statystyka migracji; lista różnic przed/po z oceną; zrzuty różnic (jeśli były); wynik testu w CMS punkt po punkcie; pytania do właściciela.
