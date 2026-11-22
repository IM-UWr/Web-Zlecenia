# Raport — zlecenie 59: uzupełnienie i poprawki wersji angielskiej (nałożenie łatek)

Data: 22.11.2026. Gałąź robocza `praca/59-wersja-angielska` w Web-Core i w 6 repozytoriach treści (klony w `..\tresci-C\`). Bez subagentów.

## Krótko
- Nałożyłem wszystkie 7 łatek. Jedyny konflikt był w `src/views/Obrona.astro`, bo łatka zderzyła się z dzisiejszą zmianą „bez promotorów pomocniczych na stronie” (c8e6497b). Rozwiązanie opisuję niżej.
- Sprawdziłem, że łatki treści zmieniają tylko pola `_en`/`tresc_en` (i `.pages.yml` w trzech repozytoriach). Wynik: 0 problemów w 6 repozytoriach.
- Zrobiłem punkt 4 („Photo” w portrecie zastępczym na `/en`).
- Zrobiłem poprawki polskich tekstów z punktu 6A (1–33), osobnymi commitami „Poprawki PL”. Pełna lista „było → jest” jest niżej.
- HTML przed i po łatkach:
  - strony PL po łatkach są identyczne bajt w bajt (477/477);
  - po poprawkach PL zmieniły się tylko miejsca z punktu 6A.
- `astro check`: 0 błędów, 0 ostrzeżeń. `test:jawne`: 84/84. `sprawdz_pola_cms.py`: 0 problemów. `sprawdz-jawny-markdown.mjs`: OK w 3 repozytoriach. `sprawdz_tresci.py`: OK, zostały tylko 3 znane błędy obrazów WW.
- Zrzuty przed i po (390 i 1920 px): `raport-zrzuty/z59-zrzuty/`.
- Push: sekcja „Push” na końcu.

## 1. Nałożenie łatek

### Web-Core (najpierw)
- Łatkę nałożyłem przez `git apply --3way` na świeży `main` (`184ef501`, po zleceniach 57 i 58 oraz po zmianie z promotorami pomocniczymi). Commit: `0dae52f7`.
- 15 z 16 plików weszło czysto.
- **Konflikt: `src/views/Obrona.astro`.** Łatka (stan z ok. 13:45) zmieniała stary wiersz `promotorzy` na „Supervisors” przy dwóch i więcej promotorach. W międzyczasie, w `c8e6497b`, ten wiersz już korzystał z `promotorzyNaStronie(obrona)`, które pomija promotorów pomocniczych (decyzja właściciela z 22.11).
- **Rozwiązanie konfliktu:** zostawiłem `promotorzyNaStronie(obrona)` i dodałem z łatki liczbę mnogą przy dwóch i więcej promotorach. Po punkcie 25 jest to `T('Promotorzy', 'Supervisors')`.
- **Skutek:** przykład z treści zlecenia „(auxiliary supervisor)” nie pojawi się na stronie, bo promotor pomocniczy jest ukryty decyzją właściciela. Dane w CMS są bez zmian. Obrona z dwoma promotorami wygląda np. tak: Ghardallou, `/en/obrony-doktorskie/2016-05-06-zeineb-ghardallou/`, „Supervisors: Prof. Ewa Damek, Prof. Mohamed Sifi (co-supervisor)”.
- Schemat (`content.config.ts`) ma nowe pola: `galeria[].podpis_en`, `tresc_en` w konferencjach, `obraz_zrodlo_en` w sylwetkach WW.

### Repozytoria treści
Bazy to stan `origin/main` z 15:11 (`tresci-C/z59-bazy.txt`). Łatki weszły przez `git apply --3way` bez konfliktów.

| Repozytorium | Baza | Łatka | Poprawki PL | Inne |
|---|---|---|---|---|
| Web-Instytut | `d14657e` (= bazy-sha) | `6b2668d` (47 plików) | `db4e712` | `e71567f` (kotwica, niżej) |
| Web-Studia | `608f1dc` (= bazy-sha) | `9f5d3e7` (24) | `7d4a2f7` | — |
| Web-Popularyzacja | `faf8ca1` (= bazy-sha) | `fa0b44a` (5) | `e959453` | — |
| Web-Ustawienia | `fd49210` (= bazy-sha) | `3a318aa` (5) | brak poprawek | — |
| Web-Aktualnosci | `e493493` (bazy-sha: `5ed05d3`) | `4988309` (26) | `848cb3e` | — |
| Web-Nauka | `2db3479` (= bazy-sha) | `0a1cd55` (20) | `8266198` | — |

**Zmiany redaktorów od `bazy-sha`.** Takie zmiany były tylko w Web-Aktualnosci, w 4 commitach po `5ed05d3`:

| Commit | Kto | Kiedy | Co zmienia |
|---|---|---|---|
| `637dd61` | Claude | 13:40 | obrony: pliki Szymona Cygana w archiwum, promotorzy 5 ostatnich obron |
| `d3bb118` | Symon Cygan (Pages CMS) | 14:49 | `obrony/2026-10-20-maciej-tadej.md` |
| `8ec0724` | Symon Cygan (Pages CMS) | 14:52 | `obrony/2026-10-27-malwina-mrowinska.md` |
| `e493493` | Symon Cygan (Pages CMS) | 14:52 | `obrony/2026-09-21-tomasz-zuchowski.md` |

Te commity zmieniają 6 plików w `src/content/obrony/`. Łatka ich nie dotyka (część wspólna zbiorów plików jest pusta), więc żaden polski tekst redaktora nie wymaga uzupełnienia EN z tego powodu. W pozostałych repozytoriach od `bazy-sha` nie było commitów.

### Łatki zmieniają tylko pola EN
Sprawdził to skrypt `tresci-C/z59-tylko-en.py`, z wynikami w `tresci-C/z59-tylko-en-<Repo>.txt`. Dla każdego zmienionego pliku `.md`/`.json` skrypt porównuje body i wszystkie pola bez `_en` przed łatką i po niej, po wczytaniu YAML/JSON, więc przeformatowanie `>-` nie przeszkadza.

| Repozytorium | Plików | Tylko `_en` | Pozostałe | Problemy |
|---|---|---|---|---|
| Web-Instytut | 47 | 46 | `.pages.yml` | 0 |
| Web-Studia | 24 | 24 | — | 0 |
| Web-Popularyzacja | 5 | 5 | — | 0 |
| Web-Ustawienia | 5 | 5 | — | 0 |
| Web-Aktualnosci | 26 | 25 | `.pages.yml` | 0 |
| Web-Nauka | 20 | 19 | `.pages.yml` | 0 |

### Nowe pola w CMS
Formularze CMS: YAML wszystkich trzech `.pages.yml` wczytuje się poprawnie, a każde nowe pole stoi zaraz pod polskim odpowiednikiem.

| Repozytorium | Kolekcja | Pole | Etykieta | Kolejność pól |
|---|---|---|---|---|
| Web-Aktualnosci | aktualności, galeria | `podpis_en` | Podpis EN | `plik`, `podpis`, `podpis_en`, `pozycja` |
| Web-Nauka | konferencje | `tresc_en` | Opis EN | `miejsce`, `body`, `tresc_en`, `strona` |
| Web-Instytut | sylwetki WW, karta | `obraz_zrodlo_en` | Źródło zdjęcia EN | `obraz`, `obraz_zrodlo`, `obraz_zrodlo_en` |

Wszystkie trzy są dopisane w `.przekazanie/pola-do-cms.md`, w sekcji „Zlecenie 59”.

## 2. Punkt 4: „Photo” w portrecie zastępczym
`portretHtml(w, klasa, lang = 'pl')` w `src/lib/wartoWiedziec.ts`: na `/en` napis brzmi `<small lang="en">Photo</small>`, na PL bez zmian `<small lang="pl">Zdjęcie</small>`. Napis pojawia się tylko na Podglądzie. Język przekazują wywołania:
- `portretyWW(lang)` i `trescWW`;
- `SiatkaSylwetek.astro`, `SylwetkaWW.astro`, `WartoWiedziecWpis.astro`;
- `DrugiEkran.astro` (kafel „Highlights”).

Commit: `ba30dbc4`. Strony PL po tym commicie są identyczne bajt w bajt.

## 3. Poprawki polskich tekstów (punkt 6A)
Każdy punkt jest zrobiony. Zmiany robił skrypt `tresci-C/z59-poprawki-pl.py`, który sprawdza, że każdy tekst „było” występuje dokładnie tyle razy, ile w kolumnie „Ile”. Jeśli liczba się nie zgadza, skrypt nic nie zapisuje. Gdzie ten sam błąd przeszedł do EN, poprawiłem też EN.

| Pkt | Plik | Było | Jest | Ile |
|---|---|---|---|---|
| 1 | `Web-Instytut WW sylwetki/stanislaw-hartman.md` | drugi — po Stanisławie Drobocie — | drugi — po Stefanie Drobocie — | 1 |
| 1 | `Web-Instytut WW sylwetki/stanislaw-hartman.md` (EN) | after that of Stanisław Drobot | after that of Stefan Drobot | 1 |
| 2 | `Web-Instytut WW sylwetki/tomasz-rolski.md` | oraz trzech książek | oraz czterech książek | 1 |
| 2 | `Web-Instytut WW sylwetki/tomasz-rolski.md` (EN) | and three books | and four books | 1 |
| 3 | `Web-Instytut WW sylwetki/marek-bozejko.md` | hiperoctaedralnymi | hiperoktaedralnymi | 1 |
| 4 | `Web-Instytut WW sylwetki/edward-marczewski.md` | [Czesława Ryll-Nardzewskiego]( | [Czesława Rylla-Nardzewskiego]( | 1 |
| 4 | `Web-Instytut WW sylwetki/wladyslaw-narkiewicz.md` | [Czesława Ryll-Nardzewskiego]( | [Czesława Rylla-Nardzewskiego]( | 1 |
| 4 | `Web-Instytut WW sylwetki/jan-mycielski.md` | [Czesławem Ryll-Nardzewskim]( | [Czesławem Ryllem-Nardzewskim]( | 1 |
| 4 | `Web-Instytut WW sylwetki/stanislaw-hartman.md` | Ryll-Nardzewskiego (także opis źródła i cytat „zbiorom interpolacyjnym … Hartmana”) | Rylla-Nardzewskiego | 4 |
| 4 | `Web-Instytut WW sylwetki/stanislaw-hartman.md` | Ryll-Nardzewskim | Ryllem-Nardzewskim | 3 |
| 4 | `Web-Core src/data/ciekawostki/studia.json` | wyniku Czesława Ryll-Nardzewskiego z 1951 | wyniku Czesława Rylla-Nardzewskiego z 1951 | 1 |
| 5 | `Web-Instytut WW sylwetki/witold-wolibner.md` | W 2012 roku Laszlo Székelyhidi | W 2012 roku László Székelyhidi | 1 |
| 5 | `Web-Instytut WW sylwetki/witold-wolibner.md` (zajawka) | trwa nieograniczenie długo – to klasyczny | trwa nieograniczenie długo — to klasyczny | 1 |
| 6 | `Web-Instytut WW sylwetki/wladyslaw-slebodzinski.md` | [Hugo Steinhausa]( | [Hugona Steinhausa]( | 1 |
| 7 | `Web-Instytut WW historie/wyklad-terencea-tao.md` | na cześć Profesora Eliasa M. Steina | na cześć Eliasa M. Steina | 1 |
| 7 | `Web-Instytut WW historie/wyklad-terencea-tao.md` | wprowadzający prof. Pawła Strzeleckiego | wprowadzający Pawła Strzeleckiego | 1 |
| 8 | `Web-Instytut WW sylwetki/andrzej-krzywicki.md` (zajawka) | Uczeń Witolda Wolibnera, od którego – według monografii wrocławskich szkół naukowych – zaczęła się we Wrocławiu teoria równań różniczkowych. Współautor twierdzenia Aronszajna–Krzywickiego–Szarskiego. | Według monografii wrocławskich szkół naukowych to od niego zaczęła się we Wrocławiu teoria równań różniczkowych. Uczeń Witolda Wolibnera, współautor twierdzenia Aronszajna–Krzywickiego–Szarskiego. | 1 |
| 8 | `Web-Instytut WW sylwetki/andrzej-krzywicki.md` | [Spis pracowników na Podglądzie nowej strony Instytutu](/pracownicy) | [Spis pracowników na stronie Instytutu](/pracownicy) | 1 |
| 8 | `Web-Instytut WW sylwetki/andrzej-krzywicki.md` (EN) | [Staff directory on the Preview of the Institute’s new website](/pracownicy) | [Staff directory on the Institute’s website](/pracownicy) | 1 |
| 9 | `Web-Instytut WW sylwetki/kazimierz-urbanik.md` (PL i EN) | (1930–2005)”](https://bib.wmi.uni.wroc.pl/sites/default/files/upload_attach/KU.pdf) | (1930–2005)”](http://www.math.uni.wroc.pl/sesja_Urbanik) | 2 |
| 10 | 6 sylwetek WW | tytuły w „…” | tytuły kursywą *…* | 61 (lista niżej) |
| 11 | `Web-Aktualnosci aktualnosci/2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu.md` | tytul: "Wykład popularnonaukowy z cyklu MISIU. " | tytul: "Wykład popularnonaukowy z cyklu MISIU" | 1 |
| 11 | jw. | dwóch wykładów - z matematyki | dwóch wykładów — z matematyki | 1 |
| 11 | jw. | miejsce: sala 25, Instytut Informatyki Uniwersytetu Wrocławskiego | miejsce: sala 25, Instytut Informatyki UWr | 1 |
| 12 | `Web-Aktualnosci aktualnosci/2026-11-10-seminarium-wydzialowe-problem-milenijny.md` | z naszego Instytutu, która wygłosi | z naszego Instytutu, który wygłosi | 1 |
| 12 | jw. | zdjecie_opis: "OpenAI votrex " | zdjecie_opis: OpenAI vortex | 1 |
| 12 | jw. | nazwa: "Slajd z wykładu prof. Grzegorza Karch " | nazwa: Slajd z wykładu prof. Grzegorza Karcha | 1 |
| 12 | jw. | miejsce: Instytut Informatyki sala 119 | miejsce: sala 119, Instytut Informatyki UWr | 1 |
| 13 | `Web-Aktualnosci aktualnosci/2026-11-18-nagroda-im-prof-andrzeja-hulanickiego-dla-agnieszki-i-mariusza.md` | Nagroda im. **Andrzeja Hulanickiego przyznawana** jest | **Nagroda im. Andrzeja Hulanickiego** przyznawana jest | 1 |
| 13 | jw. | podpis: "Agnieszka Hejna-Łyżwa i Mariusz Tobolski " | podpis: Agnieszka Hejna-Łyżwa i Mariusz Tobolski | 1 |
| 14 | `Web-Aktualnosci aktualnosci/2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza.md` | zajawka: "Dominik Gdesz został laureatem Studenckiego Programu Stypendialnego " | zajawka: Dominik Gdesz został laureatem Studenckiego Programu Stypendialnego. | 1 |
| 15 | `Web-Nauka konferencje/2020-`, `2021-`, `2022-19th-workshop-…` (pole `tytul`) | Noncommutative Probability, Noncommucative Harmonic | Noncommutative Probability, Noncommutative Harmonic | 3 |
| 16 | `Web-Nauka konferencje/2019-winter-school-in-abstract-analysis-2019.md` | Pittisburgh | Pittsburgh | 1 |
| 17 | `Web-Nauka konferencje/2021-xxxiv-konferencja-z-historii-matematyki.md` | 8-13 maja 2022 roku. ** | 8-13 maja 2022 roku.** | 1 |
| 17 | `Web-Nauka konferencje/2022-xxxiv-konferencja-z-historii-matematyki.md` | 7-12 maja 2023 roku. ** | 7-12 maja 2023 roku.** | 1 |
| 18 | `Web-Nauka konferencje/2020-xxxiv-konferencja-z-historii-matematyki.md` | 17-21 maja 2021 | 17–21 maja 2021 | 1 |
| 19 | `Web-Nauka konferencje/2017-` i `2018-winter-school-…` | (Sao Paulo) | (São Paulo) | 2 |
| 19 | `Web-Nauka konferencje/2017-`, `2018-` i `2019-winter-school-…` | Set Theory & Topology** której | Set Theory & Topology**, której | 3 |
| 19 | `Web-Nauka konferencje/2017-winter-school-…` | 28 stycznia - 4 lutego | 28 stycznia – 4 lutego | 1 |
| 19 | `Web-Nauka konferencje/2018-winter-school-…` | 27 stycznia - 3 lutego | 27 stycznia – 3 lutego | 1 |
| 19 | `Web-Nauka konferencje/2019-winter-school-…` | 26 stycznia - 2 lutego | 26 stycznia – 2 lutego | 1 |
| 20 | `Web-Studia kierunki/matematyka.md` | **Semestry 1: Podstawy** | **Semestr 1: Podstawy** | 1 |
| 20 | jw. | **Semestry 5–6: Przedmioty specjalnościowe.** — | **Semestry 5–6: Przedmioty specjalnościowe** — | 1 |
| 21 | `Web-Popularyzacja strony/popularyzacja/uczniowie.md` | Uniwerystetem | Uniwersytetem | 1 |
| 21 | jw. | postawowej | podstawowej | 1 |
| 21 | jw. | Ddla | Dla | 1 |
| 21 | jw. | dwóch wykładów - z matematyki | dwóch wykładów — z matematyki | 1 |
| 21 | jw. | kilkanaście godzin - aż | kilkanaście godzin — aż | 1 |
| 21 | jw. | i uważnego śledzenia rozumowań | i uważnego śledzenia rozumowań. | 1 |
| 22 | `Web-Popularyzacja strony/popularyzacja/nauczyciele.md` | W Polsce i zagranicą | W Polsce i za granicą | 1 |
| 23 | `Web-Popularyzacja data/popularyzacja.md` | akapit złamany w trzech liniach (także w środku tekstu linku) | jedna linia na akapit | 1 |
| 23 | jw. | ["Kalejdoskopu matematycznego"]( | [„Kalejdoskopu matematycznego”]( | 1 |
| 23 | jw. | szkół podstawowych (począwszy od trzeciej klasy) i średnich. . | szkół podstawowych (począwszy od trzeciej klasy) i średnich. | 1 |
| 24 | `Web-Core src/components/zal/DrugiEkran.astro` | `${n} referatów w tym tygodniu` (zawsze) | `odmiana()`: 1 referat, 2–4 referaty, 5+ referatów; EN 1 talk / talks | 1 |
| 25 | `Web-Core src/views/Obrona.astro` | „Promotor” także przy dwóch i więcej | „Promotorzy” przy dwóch i więcej (jak „Supervisors”) | 1 |
| 26 | `Web-Core src/views/Obrona.astro`, `src/components/WierszWydarzenia.astro` | polski tytuł rozprawy z `lang="en"` | `lang` według języka tytułu (`langRozprawy()` w `i18n.ts`): na PL polski tytuł bez `lang`, angielski z `lang="en"`; na EN bez zmian | — |
| 27 | `Web-Instytut WW sylwetki/marek-bozejko.md` (PL i EN, Źródła) | - [Nota biograficzna prof. Marka Bożejki (PDF)](…) — … | (pozycja usunięta) | 2 |
| 27 | `Web-Instytut WW sylwetki/tomasz-rolski.md` (PL i EN, Źródła) | - [Nota biograficzna prof. Tomasza Rolskiego (PDF)](…) — … | (pozycja usunięta) | 2 |
| 28 | `Web-Instytut WW sylwetki/marek-bozejko.md` (PL i EN) | Nagroda Humboldta … (2000) | … (2001) | 2 |
| 28 | jw. | a w 1991 roku został profesorem zwyczajnym. | a w 1990 roku został profesorem nadzwyczajnym. | 1 |
| 28 | jw. (EN) | became a full professor in 1991 | became an extraordinary professor in 1990 | 1 |
| 28 | `Web-Nauka strony/nauka/sukcesy/historia.md` (PL i EN) | - 2000 Marek Bożejko | - 2001 Marek Bożejko | 2 |
| 29 | `Web-Instytut WW sylwetki/roman-duda.md` (PL i EN) | link przy książce z 2019 r. → bazhum.muzhp.pl (artykuł z 2008 r.) | https://www.ihnpan.pl/a-history-of-polish-mathematics-by-roman-duda/ | 2 |
| 30 | `Web-Instytut WW sylwetki/witold-wolibner.md` (EN) | born in 1902 in Piotrowo, | born in 1902 in Piotrowie, | 1 |
| 31 | `Web-Studia kierunki/matematyka.md` | Przedmioty specjalności, zespołowy projekt specjalnościowy i praca licencjacka. | Przedmioty specjalności i zespołowy projekt specjalnościowy. | 1 |
| 31 | jw. (EN) | Specialisation courses, a team specialisation project and a bachelor's thesis. | Specialisation courses and a team specialisation project. | 1 |
| 32 | `Web-Instytut WW sylwetki/marek-bozejko.md` | Askeya–Wimpa–Kerowa | Askeya–Wimpa–Kerova | 1 |
| 33 | `Web-Aktualnosci aktualnosci/2026-05-12-ksztalcenie-w-krajowej-szkole-administracji-publicznej.md` (zajawka) | Krajowa Szkoła Administracji Publicznej prowadziła od 4 maja | Krajowa Szkoła Administracji Publicznej prowadzi od 4 maja | 1 |
| 33 | jw. (`zajawka_en`) | the National School of Public Administration recruited for | the National School of Public Administration is recruiting for | 1 |

**Punkt 10: tytuły w „…” zamienione na kursywę *…*.** Zmiana obejmuje Treść przed „Źródłami”. Za mapę posłużyła kursywa z tekstów EN. W cudzysłowie zostały: tytuły grantów i programów, nazwy plakatów, cytaty, nazwy seminariów, „Golden Oldies”, „Nauka” i nazwa zbioru archiwalnego. Link na kursywie pozostaje linkiem, bo liczba linków zewnętrznych na tych stronach się nie zmieniła.
- `roman-duda.md` (16): O zbiorach dwuspójnych, O pojęciu wymiaru, The origins of the concept of dimension, Colloquium Mathematicum, Wprowadzenie do topologii, Lwowska szkoła matematyczna, Pearls from a Lost City. The Lvov School of Mathematics, Matematycy XIX i XX wieku związani z Polską, Historia matematyki w Polsce na tle dziejów nauki i kultury, A History of Polish Mathematics. A Cultural Perspective from Origins to Modernity, Słownik biograficzny matematyków polskich, Wrocławska szkoła matematyczna, Wiadomości Matematyczne, Polskim Słowniku Biograficznym, Antiquitates Mathematicae, Matematyka a chaos.
- `piotr-biler.md` (12): Mathematische Annalen, Advances in Mathematics, Indiana University Mathematics Journal, Archive for Rational Mechanics and Analysis, Communications in Mathematical Physics, Warsztaty z równań różniczkowych cząstkowych, Colloquium Mathematicum, Bulletin of the Polish Academy of Sciences. Mathematics, Topological Methods in Nonlinear Analysis, Applicationes Mathematicae, Wiadomości Matematycznych, Proste nieliniowe równania ze skomplikowaną strukturą rozwiązań.
- `stanislaw-hartman.md` (11): O pewnych zagadnieniach związanych z pojęciami niezależności, Colloquium Mathematicum, Wrocławska szkoła matematyczna, Studia Mathematica, Compositio Mathematica, Teorię miary i całki Lebesgue’a, Wstęp do analizy harmonicznej, Wiadomości Matematycznych, Wiadomości Matematyczne, 34 lata, Wspomnienia (lwowskie i inne).
- `witold-wolibner.md` (10): Przyczynek do teorii funkcji analitycznych, Mathematische Zeitschrift, Sur un polynôme d'interpolation, Colloquium Mathematicum, Sur un théorème de W. Wolibner, Funkcje analityczne, Mechaniki, Nad trumną Witolda Wolibnera, Odrze, Wiadomościach Matematycznych.
- `wladyslaw-narkiewicz.md` (3): Mathematics of Computation, Wiadomościach Matematycznych, Delcie.
- `wladyslaw-slebodzinski.md` (9): Sur les équations canoniques de Hamilton, Ricci-Calculus, General Relativity and Gravitation, Formes extérieures et leurs applications, Exterior Forms and Their Applications, O geometrii tkanin, Colloquium Mathematicum, Wspomnieniach matematyka z lat 1903–1968, Wiadomościach Matematycznych.

Tytuł pracy w `Web-Nauka/src/data/publikacje/2017.json` („Wkład Czesława Ryll-Nardzewskiego…”) zostawiłem bez zmian, zgodnie ze zleceniem.

## 4. Porównanie HTML stron (cały `dist`)
Zrobiłem trzy budowy `PODGLAD=1` z lokalnych klonów (`budowa.sh`, log w `tresci-C/z59-budowy.log`):
- `z59-przed`: Web-Core `184ef501` i bazy treści;
- `z59-latki`: łatki i punkt 4;
- `z59-po`: z poprawkami PL.

Skrypt `tresci-C/z59-porownaj-pl.py` porównuje strony po normalizacji:
- `data-skrot` Podglądu;
- `uid` wysp, przy czym `props` wysp porównuje osobno po rozkodowaniu;
- hashe nazw `/_astro/*`;
- znaczniki czasu.

| Porównanie | Stron | Identyczne | Różne |
|---|---|---|---|
| PL przed → łatki | 477 | 477 bajt w bajt | 0 |
| PL łatki → poprawki PL | 477 | 243 | 234, w 40 grupach, wszystkie z punktu 6A (`tresci-C/z59-roznice-pl-po.txt`) |
| EN przed → łatki | 476 | 7 | 469, zgodnie z oczekiwaniem (łatka EN) |
| EN łatki → poprawki PL | 476 | 460 | 16, wszystkie z punktu 6A (`tresci-C/z59-roznice-en-po.txt`) |

Różnice PL łatki → poprawki PL, czyli co zmieniło się na 234 stronach:
- **159 stron:** w bocznej kolumnie „Wydarzenia” nowe miejsce i tytuł MISIU (pkt 11) oraz miejsce seminarium wydziałowego (pkt 12).
- **34 obrony:** polski tytuł rozprawy bez `lang="en"` (pkt 26).
- **Pojedyncze strony:**
  - aktualności z punktów 11–14 i 33 oraz Kariera;
  - strona główna i Kalendarz;
  - listy z „Noncommutative” (pkt 15);
  - konferencje 2017–2022 (pkt 16–19);
  - 10 sylwetek WW (pkt 1–10, 27–30, 32);
  - „Sukcesy — historia” (pkt 28);
  - Ghardallou: „Promotorzy” (pkt 25) i tytuł bez `lang="en"`;
  - Staniak: „Promotorzy”;
  - lista obron;
  - Popularyzacja ×3 (pkt 21–23);
  - Matematyka (pkt 20, 31).
- **Inne zmiany:** nie ma żadnych. Linki zewnętrzne w sylwetkach z punktu 10 zostały (ich liczba jest bez zmian).

Napisy „referat/referaty/referatów” (pkt 24) w dzisiejszej budowie pokazują „0 referatów w tym tygodniu” przed i po, więc na stronach nie ma różnicy. `odmiana()` daje: 1 referat, 2–4 referaty, 5–21 referatów, 22–24 referaty itd.

## 5. Kontrole
- `npx astro check`: 0 błędów, 0 ostrzeżeń, 9 podpowiedzi.
  - Łatka dodała w `Aktualnosc.astro` nieużywany import `ODBIORCY`. Usunąłem go w osobnym commicie `9dc6ca58`; podpowiedzi spadły z 10 do 9.
- `npm run test:jawne`: 84/84.
- `python skrypty/sprawdz_tresci.py` dla 6 repozytoriów: OK. Zostały:
  - 3 znane błędy „brak pliku obrazu” w `warto_wiedziec/nagrody`: `kategoria-a-plus`, `medal-sierpinskiego`, `nagroda-ptm-steinhausa`, bo obrazy leżą w Web-Aktualnosci;
  - komunikaty o README bez frontmattera.
- `python skrypty/sprawdz_pola_cms.py ../tresci-C`: 2207 plików w 16 repozytoriach, 0 problemów.
- `node skrypty/sprawdz-jawny-markdown.mjs`:
  - Web-Studia: OK, 426 nagłówków `##`, 0 bez `{#id}`;
  - Web-Instytut: OK, 292 nagłówki, 2 bez `{#id}`;
  - Web-Ustawienia: OK, 18 nagłówków, 0 bez `{#id}`.
- YAML trzech `.pages.yml`: poprawny; pola na miejscu (tabela w punkcie 1).
- `lang="pl"` na stronach `/en` (surowa liczba, razem z przełącznikiem języka w każdym nagłówku): 2875 przed → 2595 po łatkach.

### Wspólne `{#id}` (kryterium „przełącznik trafia w tę samą sekcję”)
Skrypt `tresci-C/z59-kotwice.py` porównuje id nagłówków h2–h4 i pozycji spisu „Na tej stronie” na stronach PL i ich odpowiednikach `/en` w Studiach, Instytucie (z WW) i Popularyzacji. Wyniki: `tresci-C/z59-kotwice-przed.txt` i `-po.txt`.

| | Stron z sekcjami | Różne id (nagłówki lub spis) | Różny spis „Na tej stronie” |
|---|---|---|---|
| przed łatkami | 88 | 58 | 40 |
| po łatkach | 88 | 20 | 2 |

- **Spis po łatkach różni się jeszcze na 2 stronach:**
  - **`/instytut/warto-wiedziec/artykul-w-annals-of-mathematics/`:** angielski nagłówek „Bibliographic details” nie miał `{#id}` i dostawał id z tekstu. Dopisałem `{#dane-bibliograficzne}` w polu EN; polska strona bez zmian. Commit Web-Instytut `e71567f`.
  - **`/studia/rok-akademicki/`:** id sekcji „Kolory dni”, „Rok w skrócie”, „Do pobrania” są w kodzie (`src/lib/widoki/rokAkademicki.ts`) i zależą od języka (`#kolory-dni` / `#day-colours`), a tekst roku w Web-Studia ma `{#legal-basis}`. Trzy linki EN w Web-Studia (pierwszy rok ×2, zajęcia) prowadzą do `/studia/rok-akademicki#day-colours`. Łatka tego nie ujednoliciła i ja też tego nie ruszałem. Pytanie 1 niżej.
- **Pozostałe 18 stron** różnią się tylko id nagłówków h3/h4 bez `{#id}`, które nie występują w spisie. Przed łatkami takich stron było więcej.
- **Ważne:** przełącznik języka (`a.z-jezyk` w `PasekMenu.astro`) to zwykły link do strony w drugim języku, bez `#kotwicy`. Dziś więc w ogóle nie przenosi do tej samej sekcji. Wspólne id pomagają tylko wtedy, gdy ktoś ręcznie zmieni w adresie `/` na `/en/` albo odwrotnie. Pytanie 1 niżej.

## 6. Zrzuty (`raport-zrzuty/z59-zrzuty/`)
Skrypt: `raport-zrzuty/z59-skrypt/zrzuty59.mjs` (Edge przez Playwright, jasny motyw). Każdy plik pokazuje „przed | po” obok siebie: `z59-<klucz>-<szerokość>-gora.png` (górne okno) i `-fragment.png` (wskazany fragment). Tekst fragmentów po zmianie i błędy konsoli są w `raport-zrzuty/z59-wynik.json`.

Mam 23 strony × 2 szerokości, czyli 92 pliki. Wszystkie odpowiedzi to 200 i wszystkie fragmenty się znalazły. Co widać „po”:

| Klucz | Strona | Co widać po zmianie |
|---|---|---|
| `en-glowna-wydarzenia` | `/en/` | „Upcoming events”: „Popular science lecture in the MISIU series”, „room 25, Institute of Computer Science, University of Wrocław”; seminarium „room 119, Institute of Computer Science, University of Wrocław” |
| `en-glowna-studia` | `/en/` | przycisk „Admissions (in Polish)”, wygląd przycisku bez zmian |
| `en-glowna-highlights` | `/en/` | „Highlights” zamiast „Did you know”, z kartami po angielsku |
| `en-misiu` | aktualność MISIU | tytuł EN, „For: prospective students”, miejsce po angielsku |
| `en-seminarium-karch` | aktualność 10.11 | tekst i podpisy EN |
| `en-hulanicki-galeria` | aktualność 18.11 | podpis galerii EN (`podpis_en`) |
| `en-obrona-ghardallou`, `pl-obrona-ghardallou` | obrona z dwoma promotorami | „Supervisors: Prof. Ewa Damek, Prof. Mohamed Sifi (co-supervisor)”, „Original title: …”; PL: „Promotorzy” |
| `en-obrona-hejna-online` | obrona zdalna | „… took place on Tuesday, 15 June 2021, 10:00, online.” (bez „in”); nazwisko bez „MSc” w nagłówku |
| `en-obrona-sydor-tytul-pl`, `pl-obrona-sydor-tytul-pl` | polski tytuł rozprawy | EN: „Original title:” i `lang="pl"`; PL: wygląd bez zmian, tytuł bez `lang="en"` |
| `en-obrony-lista` | lista obron, rok 2014 | polski tytuł z `lang="pl"`, „Supervisor: …” |
| `en-konferencja-2018-pah`, `en-konferencja-2019-winter` | konferencje | opis po angielsku (`tresc_en`) |
| `en-ww-marczewski` | sylwetka WW, portret | „Photo: University of Wrocław Archives” (było „Photo: Archiwum UWr”) |
| `en-ww-krzywicki` | sylwetka WW | pełna treść EN, Źródła bez „Preview” |
| `pl-ww-hartman` | sylwetka WW (PL) | tytuły kursywą (pkt 10), Stefan Drobot, Rylla-Nardzewskiego |
| `en-popularyzacja`, `en-popularyzacja-uczniowie`, `pl-popularyzacja` | Popularyzacja | Treści EN napisane od nowa; PL: akapit i „Kalejdoskopu matematycznego” |
| `en-matematyka`, `pl-matematyka` | Matematyka, etapy studiów | „Semestr 1”, semestry 5–6 bez pracy licencjackiej (PL i EN) |
| `en-rok-akademicki` | legenda kolorów dni | „an odd-numbered occurrence of that weekday in the semester” |

**Konsola:** 1 komunikat, na `/en/studia/rok-akademicki/` przy 1920 px w budowie „po”: „Failed to load resource: 403”. Lokalny serwer zwraca tylko 200 i 404, więc 403 przyszło z zasobu zewnętrznego. Strona różni się od „przed” tylko tekstem legendy. Komunikat wystąpił raz: przy 390 px na tej samej stronie i we wszystkich przebiegach „przed” go nie było. Uznaję go za przypadkowy, niezwiązany ze zmianą.

## 7. Odstępstwa od zlecenia i powody
1. **`Obrona.astro`:** konflikt z dzisiejszą zmianą (bez promotorów pomocniczych) rozwiązałem na korzyść decyzji właściciela. Przykład „(auxiliary supervisor)” z treści zlecenia nie pokaże się na stronie, a „(co-supervisor)” zostaje.
2. **Web-Aktualnosci:** łatkę nałożyłem na `e493493`, a nie na `5ed05d3` z `bazy-sha.txt`, bo redaktor dodał w międzyczasie 3 zmiany w obronach. Łatka nie dotyka tych plików i weszła czysto.
3. **Punkt 19:** przecinek przed „której” dopisałem także w konferencji 2019, bo ma ten sam błąd (zlecenie wymieniało 2017 i 2018).
4. **Poza zakresem 6A, ale zrobione (drobne):**
   - nieużywany import `ODBIORCY` po łatce (`9dc6ca58`);
   - `{#dane-bibliograficzne}` w EN artykułu o „Annals” (`e71567f`).
5. **Zauważone, nie poprawiane** (nie ma ich w 6A):
   - zakresy dat z łącznikiem „8-13 maja 2022” i „7-12 maja 2023” w opisach konferencji 2021 i 2022 (punkt 17 dotyczył tylko pogrubienia);
   - niejednolite kropki w tekstach linków w Popularyzacji.

## 8. Pytania do właściciela
1. ~~**Przełącznik języka i kotwice.**~~ Rozstrzygnięte: właściciel zgodził się na obie zmiany, a zrobione są w sekcji 9.
2. **Zakresy dat z łącznikiem** w konferencjach 2021 i 2022 („8-13 maja 2022”, „7-12 maja 2023”): poprawić na półpauzę jak w punkcie 18?
3. **Sprawy „Do decyzji” z raportów agentów** (`59-zalaczniki/raport-agent-*.md`), których zlecenie nie rozstrzyga. Zostawiłem je bez zmian, jak w łatkach:
   - agent 1: „Otton Nikodym” i „Marek Kac” w polskich formach; „PTM president” (limit banera);
   - agent 3: grafik Tutorni na `/en` z polskimi skrótami przedmiotów; niekonsekwentny dopisek „(in Polish)” przy linkach do serwisów tylko po polsku; skrót „IM PAN” w ciekawostce Ślebodzińskiego;
   - agent 4:
     - apostrofy `'` / `’` (89 : 10);
     - „Chilean-Polish Mathematical Meeting” a „Kongres”;
     - 87 tytułów grantów EN niesprawdzonych z tytułami NCN;
     - tytuły wykładów MISIU (oryginał polski i tłumaczenie);
     - link do strony seminarium wydziałowego tylko w EN wpisu z 10.11;
     - tytuł wpisu z 18.11 z samymi imionami;
     - „Program ESF” w polu `kod` grantu z 2005 r.

## Push
Push bez słowa „push”, na polecenie właściciela z 22.11: „I potem 59 i po 59 też automatyczny push”. Kolejność: najpierw Web-Core, potem repozytoria treści. Wszystkie pushe to fast-forward, bez force. Gałęzie `praca/59-wersja-angielska` zostały tylko lokalnie.

**Przed pushem** (`tresci-C/z59-kontrola.py przed`, wynik w `z59-kontrola-stan.json`):
- w żadnym z 7 repozytoriów nie było nowych commitów na `origin/main` od bazy (Web-Core `184ef501`, treści ze stanu 15:11);
- każdy push mógł być fast-forward;
- z plikami zmienionymi przez redaktorów od `bazy-sha` (6 obron w Web-Aktualnosci) nic się nie pokrywa;
- tuż przed pushem każdego repozytorium skrypt jeszcze raz robił `fetch` i liczył nowe commity: 0;
- ostatnia budowa `z59-final` z dokładnie wypychanych commitów zgadza się z `z59-po`: PL 477/477 identyczne, EN różni się tylko kotwicą w artykule o „Annals”.

| Repozytorium | Zakres | Godzina |
|---|---|---|
| Web-Core | `184ef501..9dc6ca58` | 15:35:50 |
| Web-Instytut | `d14657e..e71567f` | 15:36:01 |
| Web-Studia | `608f1dc..7d4a2f7` | 15:36:05 |
| Web-Popularyzacja | `faf8ca1..e959453` | 15:36:09 |
| Web-Ustawienia | `fd49210..3a318aa` | 15:36:12 |
| Web-Aktualnosci | `e493493..848cb3e` | 15:36:16 |
| Web-Nauka | `2db3479..8266198` | 15:36:20 |

**Po pushu** (`tresci-C/z59-kontrola.py po`): WYNIK OK. Skrypt porównał pole po polu (frontmatter YAML, JSON, body) każdy plik zmieniony pushem: `origin/main` przed pushem i po nim.
- W każdym repozytorium `origin/main` = nasz commit, a liczba zmienionych plików zgadza się z oczekiwaną.
- Każde zmienione pole to pole `_en`/`tresc_en` albo `.pages.yml`, albo pole z commitu „Poprawki PL”:

  | Repozytorium | Pola EN / `.pages.yml` | Pola z poprawek PL / kodu |
  |---|---|---|
  | Web-Instytut | 124 | 16 |
  | Web-Studia | 24 | 1 |
  | Web-Popularyzacja | 6 | 3 |
  | Web-Ustawienia | 6 | 0 |
  | Web-Aktualnosci | 46 | 11 |
  | Web-Nauka | 83 | 10 |
  | Web-Core | — | 20 plików kodu |

- Pliki redaktorów od `bazy-sha` są bajt w bajt takie jak przed pushem.
- Nic nie trzeba było przywracać.

**Akcje GitHub:**
- Web-Core: `push` 45033685817 — success.
- Przekaźnik do Web-Podglad z 6 repozytoriów treści: `repository_dispatch` 45033719064, 45033723504, 45033731758, 45033736762, 45033741477, 45033741982 — wszystkie success.
- „Powiadom stronę o zmianie” w repozytoriach treści, np. Web-Instytut 45033702391 i Web-Aktualnosci 45033723696 — success.
- Web-Podglad, „Podgląd nowego wyglądu”: ostatnie uruchomienie 45033762571 (ze stanem po wszystkich 7 pushach) — **success**, zakończone 15:38. Wcześniejsze uruchomienia z tej serii zostały anulowane jako zdublowane.

## 9. Dopisek po raporcie (22.11, ok. 15:40–15:55): kotwice przy zmianie języka i ramka „dziś”
Właściciel zgodził się na obie zmiany z pytania 1 („Dobra. Zgadzam się, popraw”). Przy okazji zgłosił, że czarny prostokąt „dziś” w kalendarzu kolorów dni wygląda, jakby był za kafelkiem. Gałąź robocza to `praca/59-kotwice` w Web-Core i Web-Studia.

| Repozytorium | Commit | Zmiana |
|---|---|---|
| Web-Core | `b62119bf` | Nowy `src/scripts/zal/jezyk-kotwica.ts`, dołączony w `Naglowek.astro`, więc działa na każdej stronie. Każdy przełącznik `a.z-jezyk` (pasek, nagłówek telefonu, okładka) bierze bieżącą `#kotwicę` z adresu. Kotwica jest ustawiana tuż przed użyciem linku: przy najechaniu (przed złożeniem strony w tle przez `speculationrules`), fokusie, naciśnięciu, kliknięciu (także środkowym i z Ctrl) i menu kontekstowym. Bez kotwicy link prowadzi, jak dotąd, na górę strony. |
| Web-Core | `b62119bf` | `src/lib/widoki/rokAkademicki.ts`: id sekcji takie same w EN jak w PL (`kolory-dni`, `rok-w-skrócie`, `do-pobrania`). |
| Web-Studia | `eb6a4fc` | `data/rok-akademicki.md`: EN `## Legal basis {#legal-basis}` → `{#podstawa-prawna}`. `pierwszy-rok.md` (×2) i `zajecia.md` (×1): linki EN `/studia/rok-akademicki#day-colours` → `#kolory-dni`. |
| Web-Core | `bf4ce0a1` | `src/views/KoloryDniSemestr.astro`: ramka „dziś” rysowana na kafelku, od środka (`outline-offset: -2.5px`, jak wzór „Dziś” w legendzie). Przy dniu z zamianą obwódka w kolorze dnia przesuwa się do środka (`inset 5px`), więc widać i ramkę, i zamianę. |

**Dlaczego ramka wyglądała na podłożoną.** Obrys miał `outline-offset: 1px`, więc leżał w całości na zewnątrz kafelka, w szczelinie między kafelkami (3 px), z jasnym paskiem 1 px przy kafelku. Pomiar w Edge (1×, 1,25× i 2×) pokazał, że sąsiednie kafelki go nie przykrywają: wszystkie krawędzie mają tę samą grubość. Wrażenie „pod spodem” brało się więc z tego, gdzie ramka leży, a nie z przykrycia. Zrzut przed | po: `raport-zrzuty/z59-zrzuty/z59-dzis-ramka-przed-po.png`. Pomiar robi skrypt `raport-zrzuty/z59-skrypt/dzis-ramka.mjs`.

**Sprawdzenie.** Budowa `z59-kotwice` (Core `bf4ce0a1`, Web-Studia `eb6a4fc`, `PODGLAD=1`):
- **Strony PL:** wszystkie 477 bez zmian w treści; różni się tylko hash pliku skryptu i CSS.
- **Strony EN:** różnice tylko na trzech stronach: Rok akademicki (id sekcji i spis), Pierwszy rok i Zajęcia (linki `#kolory-dni`).
- **Kotwice (`z59-kotwice.py`):** spis „Na tej stronie” ma te same id w PL i EN na wszystkich 88 stronach z sekcjami. Na 18 stronach różnią się tylko id nagłówków h3/h4 spoza spisu.
- **`astro check`:** 0 błędów, 0 ostrzeżeń.
- **Przeglądarka (panel przeglądarki, 1024 px):**
  - PL Rok akademicki, klik „Rok w skrócie” w spisie, potem flaga EN → `/en/studia/rok-akademicki/#rok-w-skr%C3%B3cie`, sekcja „The year at a glance” u góry okna;
  - EN, klik „Legal basis”, potem flaga PL → `/studia/rok-akademicki/#podstawa-prawna`, sekcja „Podstawa prawna”;
  - sylwetka Bożejki: bez kotwicy link bez `#`, z `#nagrody` link z `#nagrody`, po usunięciu kotwicy z adresu link znów bez `#`.

**Push** po zgodzie właściciela („Tak, push”):
- Web-Core `9dc6ca58..bf4ce0a1` (15:50:57), Web-Studia `7d4a2f7..eb6a4fc` (15:51:00). Oba pushe to fast-forward, bez force.
- Przed pushem: od poprzedniego pushu (15:36) nie było nowych commitów redaktorów.
- Po pushu w Web-Studia zmieniły się tylko pola EN: `tresc_en` w `pierwszy-rok.md` i `zajecia.md` oraz `dalej_en` w `rok-akademicki.md`. W Web-Core zmieniły się tylko 4 nasze pliki.
- Akcje GitHub: Web-Core push 45035041500, Web-Studia „Powiadom stronę o zmianie” 45035046668 i przekaźnik 45035067394 — wszystkie success. Budowa Podglądu na Web-Podglad 45035086146 — success; wcześniejsze uruchomienie z tej serii zostało anulowane jako zdublowane.
- Gałęzie `praca/59-kotwice` zostały tylko lokalnie.
