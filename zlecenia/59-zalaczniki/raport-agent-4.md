# Raport agenta 4 — wersja angielska: Web-Aktualnosci, Web-Nauka, 9 × Web-Sem-* (22.11.2026)

Podstawy: Web-Aktualnosci `5ed05d3`, Web-Nauka `2db3479`, Web-Sem-* jak w `wspolne/bazy-sha.txt`.

## Podsumowanie

**Sprawdzono** (każdy plik: skrypt braków + automatyczne porównanie PL/EN — akapity, zdania, liczby, linki, pogrubienia, `{#id}`, pisownia amerykańska, tytuły D1, „Institute of Mathematics”, daty; potem lektura): 

| Zakres | Pliki | Pola EN sprawdzone |
|---|---|---|
| Web-Aktualnosci: aktualności (w tym 11 „Kariera”, 3 seminaria wydziałowe/wydarzenia) | 164 | 596 |
| Web-Aktualnosci: obrony doktorskie (żadna nie ma Treści — tekst EN składa kod) | 52 | — |
| Web-Aktualnosci: strony | 3 | 11 |
| Web-Nauka: granty / konferencje | 94 / 61 | 87 / 9 |
| Web-Nauka: strony Nauki, `nauka.md`, `publikacje.json`, 23 wykazy roczne (nagłówki, uwagi) | 31 | 70 |
| Web-Sem-*: opisy seminariów / referaty | 9 / 31 | 27 / 53 |

**Wynik:**
- **Uzupełniono 6 pól** (brakowało EN) w 3 aktualnościach.
- **Poprawiono 32 pola** (EN był, ale zły) w 24 plikach Web-Aktualnosci i 2 plikach Web-Nauka.
- **Zostawiono** resztę (ok. 815 pól): tłumaczenia z 5.11 są kompletne i poprawne. Problemy były prawie wyłącznie we wpisach dodanych później przez redaktorów w CMS (czerwiec–listopad 2026).
- Repozytoria **Web-Sem-*** nie wymagają zmian, więc nie ma dla nich łatek. Streszczenia referatów po polsku mają EN, a pozostałe streszczenia są po angielsku. Afiliacje i sale po polsku mają `_en`.
- **17 polskich opisów konferencji** przetłumaczyłem do osobnej łatki **warunkowej** (`Web-Nauka-konferencje-tresc_en.patch`), bo schemat konferencji nie ma pola `tresc_en` (szczegóły w sekcji „Potrzebne zmiany w kodzie”).

Pliki wynikowe:
- `Web-Aktualnosci.patch` (25 plików, +66/−127),
- `Web-Nauka.patch` (2 pliki, +6/−6),
- `Web-Nauka-konferencje-tresc_en.patch` (17 plików, +69; nakładać dopiero po dodaniu pola).

Wszystkie trzy przechodzą `git apply --check` na czystych klonach. Dwie łatki Web-Nauka zmieniają różne pliki, więc można je nakładać niezależnie. `sprawdz_tresci.py`: Web-Aktualnosci — OK, 219 plików; Web-Nauka — OK, 162 pliki, także z łatką konferencji.

## Tabela zmian

### Web-Aktualnosci

| Plik (`src/content/…`) | Pole | Co zrobiono |
|---|---|---|
| `aktualnosci/2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu.md` | `tytul_en` | **uzupełnione** — „Popular science lecture in the MISIU series”. Polski tytuł był na 169 stronach `/en` (pasek „Upcoming events”, strona główna, kalendarz). |
| ten sam | `zajawka_en` | poprawione — wcześniej niepełne zdanie i „high school”; teraz rozwinięty skrót MISIU |
| ten sam | `tresc_en` | poprawione — pisownia brytyjska (behaviour, colouring, specialist), półpauzy ze spacjami, rozwinięcie skrótu MISIU, tytuły wykładów w oryginale z tłumaczeniem w nawiasie (D10/D4) |
| `aktualnosci/2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza.md` | `tytul_en`, `zajawka_en`, `zdjecie_opis_en` | **uzupełnione** (wzór jak w innych wpisach o Stypendium im. Steinhausa) |
| ten sam | `tresc_en` | poprawione — Programme, organised, honourable |
| `aktualnosci/2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego.md` | `zalaczniki[0,1].nazwa_en` | **uzupełnione** — „Biographical note on Prof. … (Polish)” (sprawdziłem, że PDF-y są po polsku) |
| `aktualnosci/2026-11-18-nagroda-im-prof-andrzeja-hulanickiego-dla-agnieszki-i-mariusza.md` | `tytul_en`, `zajawka_en`, `tresc_en` | poprawione — „Institute of Mathematics” zmienione na „Mathematical Institute”; „Dr.” na „Dr”; recognised, organising, organisation; „The Professor …” na „Prof. …” |
| `aktualnosci/2026-11-10-seminarium-wydzialowe-problem-milenijny.md` | `tresc_en` | poprawione — data i godzina po amerykańsku („November 10, at 1:00 p.m.”, „12:30 p.m.”) zmienione na „10 November at 13:00”; „Professor” na „Prof.” (D1); „Room” na „room”; proste cudzysłowy; tytuł wykładu w oryginale + tłumaczenie (D10) |
| ten sam | `zdjecie_opis_en` | poprawione — podpis „Grzegorz Karch” nie pasował do zdjęcia (wizualizacja wiru, PL „OpenAI votrex”); teraz „OpenAI vortex” |
| ten sam | `zalaczniki[0].nazwa_en` | poprawione — „Prof.” (D1) i dopisek „(Polish)”, bo slajdy są po polsku |
| `aktualnosci/2026-07-14-szkola-baby-steps-beyond-the-horizon.md` | `tresc_en` | poprawione — brakowało dwóch zdań z polskiego („Oczekujemy, że każdy z zaproszonych wykładowców…”, „Zachęcamy studentów do udziału…”) |
| `aktualnosci/2026-09-23-2-kongres-mlodych-odkrywcow.md` | `zajawka_en` | poprawione — brakowało „z niemal 20 szkół średnich” |
| `aktualnosci/2026-10-17-rusza-tutornia.md` | `tresc_en` | poprawione — link wewnętrzny z `/en/` zmieniony na `/studia/tutornia` (zasada: linki bez `/en`) |
| `aktualnosci/2026-06-19-seminarium-ze-statystyki.md` | `tresc_en` | poprawione — skrót „(IM UWr)” (5×) zmieniony na „(Mathematical Institute, UWr)” |
| `aktualnosci/2026-05-29-lvzhou-chen-laureatem-nagrody-im-kamila-duszenki.md` | `tresc_en` | poprawione — „math clubs” na „mathematics clubs” |
| `aktualnosci/2026-04-20-konkurs-prac-dyplomowych.md` | `tresc_en` | poprawione — usunięte „, MSc” przy 3 promotorach (D1: mgr bez tytułu) |
| `zdjecie_opis_en` w 13 aktualnościach: `2015-01-01-stypendium-im-hugona-steinhausa-…`, `2016-11-13-…-hoffmanna`, `2017-11-13-agnieszka-hejna-…-dyplom-roku`, `2017-11-14-…-dyszewskiego`, `2018-03-29-agnieszka-hejna-…-marcinkiewicza`, `2018-04-10-agnieszka-hejna-…-krok-w-przyszlosc`, `2018-11-12-…-hejny`, `2019-11-14-…-kani`, `2020-03-23-agnieszka-hejna-…-ptm`, `2021-03-19-nagroda-dla-agnieszki-hejny`, `2021-11-16-…-cygana`, `2024-11-14-…-korpalskiego`, `2025-11-05-…-blaszkiewicza` | `zdjecie_opis_en` | poprawione — „X, MSc” zmienione na „X” (D1; „MSc” zostaje tylko przy kandydacie na stronie obrony) |
| `strony/obrony-doktorskie.md` | `tresc_en` | poprawione — proste cudzysłowy zmienione na “…” |

### Web-Nauka

| Plik | Pole | Co zrobiono |
|---|---|---|
| `src/content/strony/nauka/sukcesy/historia.md` | `tresc_en` | poprawione — `{#id}` sekcji inne niż w polskim (`{#lectures-and-congresses}` zamiast `{#wykłady-i-kongresy}` itd., 4 sekcje); teraz takie same jak w polskim, więc przełącznik języka trafia do tej samej sekcji |
| `src/data/publikacje.json` | `czasopisma[1].redakcja_en` | poprawione — „Institute of Mathematics, University of Wrocław” zmienione na „Mathematical Institute, …” |
| `src/data/publikacje.json` | `czasopisma[0].opis_en` | poprawione — optimization zmienione na optimisation |
| (łatka warunkowa) 17 konferencji: `2016-7th-euro-japanese-workshop-on-blow-up`, `2016-combinatorics-and-groups`, `2016-mathematics-of-pattern-formation`, `2016-stochastic-models-v`, `2016/2017/2018/2019-winter-school-in-abstract-analysis-*`, `2016-xxx-…`, `2017-xxxi-…`, `2018-xxxii-…`, `2019-xxxiii-…`, `2020/2021/2022-xxxiv-konferencja-z-historii-matematyki`, `2018-probabilistic-aspects-of-harmonic-analysis`, `2024-contemporary-harmonic-analysis-and-its-synergies` | `tresc_en` (pola nie ma w schemacie) | **przetłumaczone, poza główną łatką**. Linki takie same jak w polskim; przy PDF-ach z programem dopisek „(in Polish)” (D20). |

Celowo **bez zmian**:
- **7 grantów z tytułem po angielsku**, np. `merg-ct-2006-046543`, `2009-001-2009-2010`, `2005-automata-…`, mają puste `tytul_en`. Wpisanie tego samego tytułu sprawiłoby, że kod pokazałby go drugi raz jako „Original title:”.
- **Referat `2026-06-11-bhattacharjee`**: oryginał jest po angielsku, więc nie dostał `tresc_en`.
- **Tytuły rozpraw (D5) i referatów (D10)** zostały w oryginale.

## Potrzebne zmiany w kodzie (dla agenta 3)

1. **`src/lib/tresci.ts:220` (`MIEJSCA_EN`)** — dwa miejsca wydarzeń zostają po polsku na `/en`:
   - „room 25, Instytut Informatyki Uniwersytetu Wrocławskiego” (MISIU 27.11; widoczne w pasku „Upcoming events” na ok. 164 stronach i na stronie głównej),
   - „Instytut Informatyki sala 119” (seminarium 10.11).

   Proponowane reguły:
   - `[/Instytut Informatyki Uniwersytetu Wrocławskiego/g, 'Institute of Computer Science, University of Wrocław']`
   - `[/Instytut Matematyczny Uniwersytetu Wrocławskiego/g, 'Mathematical Institute, University of Wrocław']`
   - `[/Wydział Matematyki i Informatyki Uniwersytetu Wrocławskiego/g, 'Faculty of Mathematics and Computer Science, University of Wrocław']`
   - po regule „…UWr”: `[/Instytut Informatyki(?! UWr)/g, 'Institute of Computer Science']`, `[/ sala (\w+)/g, ', room $1']`
   - `[/Politechnika Wrocławska/g, 'Wrocław University of Science and Technology']`

   Prościej: redaktor może ujednolicić polskie miejsce do wzoru „sala 119, Instytut Informatyki UWr”.
2. **Podpisy galerii** — w schemacie brak `podpis_en`: `content.config.ts:171`, `galeria: lista(z.object({ plik, podpis }))`. Trzeba dodać `podpis_en: optStr` (plus pole w `.pages.yml` Web-Aktualnosci i `wybierz()` w widoku). Proponowane tłumaczenia 3 obecnych podpisów:
   - „J.M. Rektor i prof. Marek Bożejko” → „The Rector and Prof. Marek Bożejko”,
   - „J.M. Rektor i prof. Tomasz Rolski” → „The Rector and Prof. Tomasz Rolski”,
   - „Agnieszka Hejna-Łyżwa i Mariusz Tobolski” → „Agnieszka Hejna-Łyżwa and Mariusz Tobolski”.
3. **Opisy konferencji** — `content.config.ts:434` (konferencje), `src/lib/widoki/konferencja.ts:14–17` i `Konferencja.astro`. Nie ma pola `tresc_en`, więc 17 polskich opisów pokazuje się na `/en` z `lang="pl"`. Wewnątrz takiego opisu znacznik linku zewnętrznego jest po polsku: „Program konferencji (inna strona)”.
   - Propozycja: `tresc_en: optStr` w schemacie, render jak w `aktualnosc.ts` (`htmlEn`) i pole „Opis EN” w `.pages.yml` (kolekcja konferencje, Web-Nauka).
   - Tłumaczenia są gotowe w `Web-Nauka-konferencje-tresc_en.patch`.
   - To samo przyda się dla grantów (`content.config.ts:451`); dziś żaden grant nie ma opisu.
4. **`src/views/Aktualnosc.astro:63`** i **`src/views/AktualnoscZamianaDni.astro:36`** — `ODBIORCY[x][lang].toLowerCase()` daje na `/en` „For: students, **phd** students, staff”. Należy użyć `odbiorcyMalymi(x, lang)` z `src/lib/i18n.ts:295`, które daje „PhD students”.
5. **Obrony:**
   - (a) **`src/views/Obrona.astro:38`** — tytuł rozprawy ma na sztywno `lang="en"`, a 32 z 52 tytułów są po polsku. Na `/en` brak etykiety „Original title:” (D5; jest już w `Konferencja.astro:32` i `Grant.astro:38`). To samo dotyczy listy `/en/obrony-doktorskie` i kalendarza `/en/kalendarz`: polskie tytuły rozpraw bez `lang="pl"` (D14).
   - (b) **`Obrona.astro:50`** — etykieta `t(lang,'promotorzy')` (`i18n.ts:187`) zawsze brzmi „Supervisor”, także przy dwóch promotorach. W `ListaObron.astro:49` jest już liczba mnoga („Supervisors:”).
   - (c) **`src/lib/osoby.ts:29` (`tytulyEn`)** — nie tłumaczy dopisków w polu `promotorzy`. Zostaje po polsku: „(promotor pomocniczy)” w 6 obronach (garncarek, jagiella, cygan, marcinkowski 2015, kolodziejska 2024, danielski 2025) i „(kopromotor)” w 1 (ghardallou 2016). Proponuję „(auxiliary supervisor)” i „(co-supervisor)”.
   - (d) **`src/lib/widoki/obrona.ts:59` (`zaproszenieEn`)** — „…, in ${miejsce}”:
     - przy miejscu „online” (2 obrony: hejna 2021, kania-strojec 2021) wychodzi „took place …, in online.”;
     - przy „University of Tunis El Manar, Tunis” wychodzi „in University of …”.

     Propozycja: dla „online” pisać „online” bez „in”, a dla nazw instytucji „at”.
6. **Brak pola w CMS:** referaty mają w schemacie `pliki[].nazwa_en`, ale w `.pages.yml` żadnego z 9 repozytoriów Web-Sem-* go nie ma. Dziś żaden referat nie ma plików, więc niczego nie wpisywałem.
7. **(drobne, `src/lib/en/publikacje.ts`)** — w wykazie 2018 zostają polskie zwroty opisu bibliograficznego, np. „Recenzent : ks. dr hab. …, prof. UP JPII”, „Materiały V Konferencji …, 9-10 grudnia 2016”. To sprawa mapy zwrotów, nie treści.

## Do decyzji właściciela

1. **Apostrofy:** w polach EN moich repozytoriów 89 wartości ma prosty `'` („Prime Minister's”, „master's”), a 10 ma `’`. Zasada mówi o `’`, ale nie zmieniałem masowo (duża łatka, zmiana wyłącznie typograficzna). W nowych i poprawianych tekstach używałem `’` tylko tam, gdzie już było. Do decyzji: jedna masowa zamiana `'`→`’` we wszystkich polach EN.
2. **Opisy konferencji:** czy dodajemy `tresc_en` do schematu? Tłumaczenia są gotowe (punkt 3 wyżej).
3. **„Chilijsko-polski Kongres Matematyczny”** — `tytul_en` brzmi „Chilean-Polish Mathematical Meeting” (Kongres ≠ Meeting). Proszę sprawdzić oficjalną nazwę angielską na https://somachi-ptm.pwr.edu.pl/.
4. **Tytuły grantów EN** (87, z tłumaczenia 5.11) to wierne tłumaczenia, ale nie sprawdzałem ich z oficjalnymi tytułami angielskimi w bazie NCN (projekty NCN mają oficjalny tytuł EN). Przy kolejnej redakcji warto je porównać i w razie różnic przyjąć oficjalne.
5. **MISIU:** redaktor podał tytuły wykładów tylko po angielsku. Zgodnie z D10/D4 dałem oryginał polski i tłumaczenie w nawiasie. Do potwierdzenia, czy tak ma zostać.
6. **Wpis z 10.11 (prof. Karch):** EN ma link do strony seminarium wydziałowego (wmi.uwr.edu.pl), którego nie ma w polskim. Zostawiłem go. Strona jest po polsku, więc można rozważyć dopisek „(in Polish)” albo usunięcie linku.
7. **„(IM UWr)” w listach prelegentów** zamieniłem na „(Mathematical Institute, UWr)”. „MIM UW” zostawiłem, bo to angielski skrót wydziału UW.
8. **Tytuł z 18.11:** „Prof. Andrzej Hulanicki Award for Agnieszka and Mariusz” — imiona bez nazwisk jak w polskim. Może lepiej z pełnymi nazwiskami w obu językach.
9. **Grant `2005-automata-theory-…`:** pole `kod` = „Program ESF (European Science Foundation)” pokazuje się na `/en` z amerykańskim „Program”. To nie jest numer grantu — lepiej przenieść do pola „Program”.

## Błędy w polskim tekście (niepoprawiane)

- **`aktualnosci/2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu.md`:**
  - tytuł kończy się kropką i spacją („…MISIU. ”);
  - „dwóch wykładów - z matematyki” — łącznik zamiast półpauzy;
  - miejsce „sala 25, Instytut Informatyki Uniwersytetu Wrocławskiego” niezgodne ze wzorem „…, Instytut Informatyki UWr”.
- **`aktualnosci/2026-11-10-seminarium-wydzialowe-problem-milenijny.md`:**
  - „prof. Grzegorz Karch …, **która** wygłosi” → „który”;
  - podpis zdjęcia „OpenAI votrex ” → „vortex”;
  - załącznik „Slajd z wykładu prof. Grzegorza Karch ” → „Slajdy z wykładu prof. Grzegorza Karcha”;
  - miejsce „Instytut Informatyki sala 119” → „sala 119, Instytut Informatyki UWr”.
- **`aktualnosci/2026-11-18-nagroda-im-prof-andrzeja-hulanickiego-…`:** „Nagroda im. **Andrzeja Hulanickiego przyznawana** jest” — pogrubienie obejmuje „przyznawana” zamiast nazwy nagrody. Podpis galerii kończy się spacją.
- **`aktualnosci/2026-11-11-stypendium-…-gdesza.md`:** zajawka bez kropki, ze spacją na końcu.
- **`aktualnosci/2026-05-12-ksztalcenie-w-krajowej-szkole-…`:** zajawka „prowadziła” (czas przeszły), treść „prowadzi” (teraźniejszy).
- **Konferencje (Web-Nauka):**
  - `2019-winter-school-…`: „Pittisburgh” → „Pittsburgh”;
  - `2021-` i `2022-xxxiv-…`: pogrubienie zamknięte po spacji („…roku. **”) — Markdown może go nie zamknąć;
  - tytuł „19th Workshop: … **Noncommucative** Harmonic Analysis…” (2020, 2021, 2022) — literówka, widoczna też na `/en`, bo to pole `tytul`;
  - `2017–2019 winter school`: brak przecinka przed „której”, „Sao Paulo”;
  - `2020-xxxiv`: „17-21 maja” — łącznik zamiast półpauzy.
- **Daty aktualności:** 7 aktualności ma datę `2015-01-01`, która wygląda na zastępczą. Na przykład `2015-01-01-stypendium-mnisw-dla-dra-mariusza-mirka` dotyczy stypendium „na lata 2016–2018”.

## Wpisy testowe (do usunięcia przed startem; nie tłumaczyłem)

- **Referaty testowe — 9 plików**, wszystkie mają już pola EN z poprzedniego etapu:
  - `Web-Sem-Analiza-Harmoniczna/…/test-2026-11-10-analiza-harmoniczna.md`
  - `Web-Sem-Dydaktyka/…/test-2026-11-09-dydaktyka.md`
  - `Web-Sem-Dyskretna-Analiza-Harmoniczna/…/test-2026-11-10-dyskretna-analiza-harmoniczna.md`
  - `Web-Sem-Geometria/…/test-2026-11-12-geometria.md`
  - `Web-Sem-Prawdopodobienstwo/…/test-2026-11-12-mister-test.md`
  - `Web-Sem-Rownania-Rozniczkowe/…/test-2026-11-09-mister-test.md`
  - `Web-Sem-Statystyka/…/test-2026-11-10-mister-test.md`
  - `Web-Sem-Teoria-Modeli/…/test-2026-11-13-teoria-modeli.md`
  - `Web-Sem-Topologia/…/test-2026-11-13-topologia.md`

  Na `/en` ich polskie tytuły („TEST: Przykładowy referat - …”) widać na stronie głównej i w kalendarzu.
- **Osierocone grafiki testowe** w Web-Aktualnosci: `public/pliki/aktualnosci/test-{dzien-otwarty,kolo-gry-kombinatoryczne,warsztaty-liczby-pierwsze,wyklad-macierze-losowe}.jpg`. Wpisy testowe aktualności i obron już usunięto, grafiki zostały.
