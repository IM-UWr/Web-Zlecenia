# Zlecenie 29: specjalności i strona działu Popularyzacji jako Markdown (GOTOWE, 7.11.2026)

Drugie z trzech zleceń „sprzątania CMS”. **Start po odbiorze lokalnym zlecenia 28** (kryteria etapów 6 i 6a), bo korzysta z jego wtyczki bloków, kotwic i wzoru formularzy. Tryb bez nadzoru: jak w 28 (od razu po 28, pytania nie zatrzymują, push i test w CMS na końcu 30). Zasady, decyzje właściciela i „Gdzie i jak” jak w `28-cms-kierunki-markdown.md`; poniżej tylko różnice.

**Cel.**
1. Każda z 6 specjalności dostaje formularz „Treść” (Nazwa, Treść, Nazwa EN, Treść EN) i osobny formularz „Baner i kafelek”. Dziś to jeden formularz z 75 polami.
2. Strona działu Popularyzacji przestaje być formularzem z 21 polami: tekst „O popularyzacji” idzie do Markdownu, drobne pola pod spodem.
3. Strony bez zmian w wyglądzie, poza różnicami zgłoszonymi w raporcie.

**Gdzie**
- Specjalności: klony `Web-Spec-Analiza-Danych`, `Web-Spec-Aktuarialno-Finansowa`, `Web-Spec-Nauczycielska`, `Web-Spec-Stosowana`, `Web-Spec-Teoretyczna` (w każdym jedna specjalność, wpis typu `file`) oraz `Web-Studia` (`spec-matematyka-w-ekonomii`, specjalność wygaszana).
- Popularyzacja: klon `Web-Popularyzacja` (`src/data/popularyzacja.json` i kolekcja `strony`).
- Kod: Web-Core, gałąź `wyglad/zlecenie-16`. Raport `RAPORT-ZLECENIE-29.md`, zrzuty `raport-zrzuty/z29-*`.
- Oszczędnie jak w 28 (bez subagentów, tylko potrzebne pliki, w raporcie lista różnic).
- Przed migracją: jak w 28, etap 0 (stan, edytorzy, zdjęcie „przed” wszystkich stron specjalności, stron kierunków z kafelkami specjalności i `/popularyzacja`, PL i EN).

## Etap 1. Specjalność: podział pól
Najpierw przeczytaj `src/views/Specjalnosc.astro` i `src/lib/widoki/specjalnosc.ts` i ustal, które pola wyświetla strona specjalności, a które czyta strona kierunku (kafelek) i inne strony. Podział docelowy:

| Formularz | Pola |
|---|---|
| **Treść** (`src/content/specjalnosci/<id>.md`) | `nazwa`, `nazwa_en`, treść PL (body), `tresc_en` |
| **Baner i kafelek** (osobny plik w tym samym repozytorium, np. `src/content/specjalnosci-baner/<id>.json`) | `kierunek`, `poziom`, `opis` (zdanie pod nazwą), `haslo`, `skrot`, `zaklad`, `opiekunowie[]` (`imie_nazwisko`, `rola`), `seminaria`, `wygaszana`, `na_stronie_kierunku`, `bez_podstrony`, `kolejnosc`, `kafelek_dla_kogo`, `kafelek_kariera`, wersje `_en`; ukryte: `zrodla`, `do_uzupelnienia` |

Do Markdownu (sekcje i nagłówki PL/EN dokładnie jak dziś na stronie specjalności):
- `body` → „O specjalności”;
- `dla_kogo` → „Dla kogo”;
- `dlaczego` → „Dlaczego warto” (kafelki);
- `etapy` → „Jak przebiega specjalność” (oś, „Kiedy: Tytuł”);
- `przedmioty` → „Czego się uczysz” (`###` grupa + lista);
- `umiejetnosci` → „Co będziesz umieć” (lista);
- `kariera` → „Po studiach”;
- `tematy_prac` → „Przykładowe tematy prac” (kafelki);
- `dokumenty` → „Dokumenty” (lista plików);
- `linki` → „Przydatne strony” (lista linków);
- `faq` → „Pytania i odpowiedzi” (`###` z „?”).

**Sekcje liczone z innych danych zostają liczone.** Dotyczy to opiekunów z danymi ze spisu pracowników, seminariów z pola `seminaria`, „Wybór specjalności” / terminów z danych kierunku i innych, które znajdziesz w szablonie. Każda dostaje **kotwicę** o swojej nazwie, dopisaną do wspólnej listy kotwic z zlecenia 28: strona wstawia sekcję pod nagłówkiem o tej nazwie, a bez nagłówka w jej dzisiejszym miejscu. Skrypt migracji wpisuje te nagłówki do treści w dzisiejszej kolejności.

Kafelki specjalności na stronie kierunku (zlecenie 28, kotwica „Specjalności”) czytają pola z „Baneru i kafelka” i mają wyjść identyczne.

## Etap 2. Popularyzacja: strona działu
- Nowy wpis typu `file` **„Strona działu Popularyzacja”**, na górze listy w Web-Popularyzacja (osobno od kolekcji „Strony”, żeby jego pola nie pojawiały się przy stronach „dla kogo”, i żeby strona działu nie stała się kartą „Dla kogo”).
- Pola: Tytuł · **Treść** (z `o_popularyzacji`; dziś akapity oddzielone pustą linią, czyli już Markdown) · Tytuł EN · **Treść EN**, a pod spodem: Wstęp pod tytułem (`wstep`), Hasło, „W skrócie” (`o_popularyzacji_fakty`), Tradycja (`rok`, `nazwa`; z niej liczą się liczby w banerze), wersje EN.
- `linki`: szablon ich dziś nie czyta (grupy biorą się z menu). Sprawdź to; jeśli to prawda, przenieś pole jako ukryte i zgłoś w raporcie.
- Karty „Dla kogo” i grupy z menu bez zmian.

## Etap 3. Skrypt migracji, formularze, szablony
- `skrypty/migracja/specjalnosci.*` i `skrypty/migracja/popularyzacja.*`. Zasady jak w 28: jedna zastępczość EN jak `wybierz()`, nazwiska EN przez `tytulyEn()`, raport przeniesionych i pominiętych wartości, odmowa ponownego uruchomienia.
- `.pages.yml` w 6 repozytoriach specjalności (5 identycznych, więc jeden szablon formularza dla wszystkich) i w Web-Studia oraz Web-Popularyzacja. Kolejność jak w 28: Treść i Treść EN na górze (`rich-text`, markdown), drobne pola niżej. Opis pola „Treść” = ściągawka z `dok/sciagawka-edytora.md`, z linijką o kotwicach tej strony („Seminaria”, „Opiekunowie specjalności”…).
- Listy wyboru `zaklad`, `seminaria`, `kierunek` zostają stałymi listami w `.pages.yml`, jak dziś. Nie naprawiaj tu sprawy „strony bezobsługowej” dla nowych seminariów i specjalności (osobny temat, `claude/start-2026-11-05.md`).
- Szablony `Specjalnosc.astro` i `Popularyzacja.astro` renderują Markdown przez wtyczkę bloków.
- `sprawdz_pola_cms.py`: nowe pliki i kolekcje, 0 problemów.

## Etap 4. Odbiór lokalny
- Porównanie przed/po (jak w 28, etap 6): 6 stron specjalności PL i EN, kafelki specjalności na 4 stronach kierunków, `/popularyzacja` PL i EN, karty „Dla kogo”. Dozwolone różnice: tylko zgłoszone w raporcie i uzasadnione; reszta to błąd.
- Zrzuty tylko tam, gdzie porównanie HTML pokazało różnicę (przed/po, 1440 i 390 px, tylko PL), jak w 28. Jeden raport na koniec zlecenia.
- `sprawdz_pola_cms.py` 0, `sprawdz_tresci.py` OK, `astro check` bez nowych błędów, testy wtyczki zielone.
- Symulacja zapisu w edytorze jak w 28, etap 6a, dla przerobionych plików specjalności i Popularyzacji.
- **Stop**, raport, czekanie na „push”. W trybie bez nadzoru: od razu zlecenie 30.

## Etap 5. Po słowie „push” (w trybie bez nadzoru: na końcu zlecenia 30)
Wypchnij `wyglad/zlecenie-16` we wszystkich dotkniętych repozytoriach razem z Web-Core. Sprawdź przebieg Web-Podglad. Test w CMS na `test-cms` (właściciel), w skrócie jak w 28, etap 8: w Web-Spec-Stosowana zapis bez zmian, dodanie tematu pracy, kroku osi i pytania; w Web-Popularyzacja zapis bez zmian i zmiana jednej liczby „W skrócie”. Porównanie, raport, usunięcie `test-cms`.

## Kryteria odbioru
- [ ] Specjalność: formularz „Treść” (4 pola) i „Baner i kafelek” osobno, we wszystkich 6.
- [ ] Popularyzacja: „Strona działu” z Treścią na górze; karty „Dla kogo” bez zmian.
- [ ] Wszystkie wartości przeniesione albo zgłoszone.
- [ ] Porównanie przed/po: tylko zgłoszone i uzasadnione różnice.
- [ ] Kontrole: 0 / OK / bez nowych błędów / testy zielone.
- [ ] Test w CMS: zapis bez zmian daje tę samą stronę.
