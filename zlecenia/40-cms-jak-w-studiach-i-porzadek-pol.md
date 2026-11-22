# Zlecenie 40: wszystkie formularze CMS przyjazne jak w Studiach i porządek pól (punkt 3 kolejki) (17.11.2026)

**Decyzje właściciela:**
- **17.11, 22:47:** „Pamiętasz, jak ładnie user friendly zrobiłeś CMS w Studiach? Z opisami, z komentarzami user friendly? Możesz tak zrobić wszystkie pozostałe CMS?”
- **Kolejka, punkt 3 (7.11 i 13.11):** wykryć pola, których strona nie używa, i przygotować listę do decyzji właściciela. Puste pola usunąć; pola z treścią ukryć, podłączyć albo usunąć. Przestrzegać zasad, żeby nie zgubić zmian redaktorów.
- **17.11, 22:45:** „to jest ważne”.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- **Zasady z kolejki, punkt 3 (obowiązkowe, bo redaktorzy edytują na żywo):**
  - zawsze od świeżego `main`, zwykły commit, nigdy force-push i nigdy nadpisywanie `main` kopią;
  - odrzucony push → `pull --rebase` i ponów;
  - najpierw Web-Core (pole wypada ze schematu albo staje się opcjonalne), potem repozytorium treści: `.pages.yml` i dane w jednym commicie;
  - pole usunięte z formularza Pages CMS wytnie z pliku przy następnym zapisie, więc najpierw sprawdź w kodzie, że strona go nie czyta.
- Do tego sekcja „Ochrona zmian redaktorów” niżej.
- **Po zleceniach 31, 39 i 33**, które zmieniają formularze. Na końcu kolejki CMS, przed zleceniem 36.
- **Jedno repozytorium = jedna sesja Code**, z osobnym raportem i osobnym „push”. Raporty `RAPORT-ZLECENIE-40-<etap>.md`, zrzuty `raport-zrzuty/z40-*`.
- Oszczędnie: bez subagentów, czytaj tylko potrzebne pliki.

## Ochrona zmian redaktorów (obowiązkowo przy każdym pushu do repozytorium treści)
Redaktorzy zapisują w CMS na żywo, także w trakcie tego zlecenia. Ich zmiany nie mogą zginąć. Migracja do jawnego Markdownu przepisuje treść wielu stron, więc ryzyko jest tu największe.

1. **Migracja na najświeższej wersji.**
   - Tuż przed pushem: `git fetch` i sprawdź, czy na `main` przybyły zapisy redaktorów od chwili, gdy zacząłeś (`git log <baza>..origin/main`). Baza = HEAD zanotowany na początku pracy nad tym repozytorium.
   - Jeśli przybyły, nie doklejaj starego wyniku. Przełącz się na świeży `main` i **uruchom skrypt migracji jeszcze raz** na aktualnych plikach.
   - Ręczne poprawki po migracji (komentarze, `{#id}`) nanoś ponownie skryptem albo listą zmian, nie kopiowaniem starych plików.
   - Konflikty rozwiązuj ręcznie: weź wersję redaktora i nanieś na nią swoją zmianę. Nigdy odwrotnie i nigdy hurtem całych plików (`-X ours`, `checkout --ours/--theirs`).
2. **Kontrola przed pushem** (skrypt, wynik w raporcie):
   - weź każdy zapis redaktora od bazy (autor inny niż Code) i każdy plik, który zmienił;
   - porównaj jego wersję z wersją, którą wypychasz: pola pole po polu, a treść (Markdown) przez porównanie tekstu po migracji (`porownaj-jawny-markdown.mjs`);
   - każda wartość i każde zdanie wpisane przez redaktora musi być w wyniku. Inaczej **STOP**.
3. **Kontrola po pushu:** porównanie pole po polu całego repozytorium przed i po. Różnice tylko w polach zmienianych celowo i w składni treści (bloki, komentarze); tekst bez zmian. Lista w raporcie.
4. **Okno pusha:** wieczorem albo po wiadomości od właściciela do redaktorów danego repozytorium: „zapiszcie i zamknijcie CMS na 15 minut, potem odświeżcie stronę”.
   - Pages CMS przy zapisie sprawdza wersję pliku. Jeśli plik zmienił się od otwarcia formularza, zapis jest odrzucony („File has changed since you last loaded it”) i nic nie zostaje nadpisane. Redaktor traci jednak to, co wpisał, a nie zapisał.
   - Formularz otwarty przed pushem i zapisany po nim działa jeszcze według starej konfiguracji. **Następnego dnia** przejrzyj zapisy redaktorów z 24 godzin po pushu: czy żaden nie usunął nowych pól (np. `format_tresci`) ani nie przywrócił starych. Znalezione popraw osobnym commitem.
5. **Wszystko da się odwrócić:** każdy zapis redaktora to osobny commit. W razie straty przywróć wartość z historii **nowym commitem** (nigdy `reset` ani force-push) i opisz to w raporcie.

## Wzorzec: Web-Studia i Web-Popularyzacja (opis w `dok/jawny-markdown.md`)

**Jeden formularz = jedna strona:**
- treść, dane i baner razem;
- Treść i Treść EN na górze, drobne pola niżej;
- pola techniczne ukryte (`hidden: true`, np. `format_tresci`).

**Jawny Markdown** (`format_tresci: jawne`):
- pole Treść to `type: code`, `format: markdown`;
- układ wskazują jawne bloki `:::kafelki`, `:::etapy`, `:::kontakty`, `:::linki`, `:::pliki`, `:::tabela`, `:::pytania`, `:::zakladki`, `:::ramka{tytul="…"}`…;
- `{#id}` przy `##` zachowuje adresy sekcji;
- zwykły tekst to proza bez otoczek.

**Komentarze dla redaktora** przy blokach (nie widać ich na stronie). Krótkie, w trybie rozkazującym, z wielkimi literami na początku, np.:
- `<!-- KAFELKI: Każdy punkt: **Tytuł** — opis. Dalsze linie: Klucz: wartość lub sam link jako przycisk. -->`
- `<!-- ZAKŁADKI: każdy nagłówek ### rozpoczyna osobną zakładkę. -->`
- Na początku treści `<!-- UKŁAD JAWNY: … -->`.

Wzory: `Web-Studia/src/content/kierunki/matematyka.md` i `.../strony/studia/podyplomowe.md`.

**Opisy w formularzu:**
- kolekcja: co to jest i gdzie widać to na stronie;
- pole Treść: ściągawka jawnego Markdownu (jak w Web-Studia);
- drobne pola: krótki opis z przykładem i informacją, co się stanie, gdy pole zostanie puste;
- etykiety po polsku; pola EN pod polskimi, z dopiskiem „EN”.

**Listy:** zwinięte, z nagłówkiem pozycji (jest od 7.11).

## Stan dziś (17.11; repozytoria z `main`)

| Repozytorium | Formularze (kolekcje / pliki) | Linie `.pages.yml` | `description` | Jawny Markdown | Komentarze w treści |
|---|---|---|---|---|---|
| Web-Studia | strona działu, kierunki, specjalności, strony, rok akademicki, przypomnienia, kalendarz zajęć, katalog opiekunów | 772 | 24 | tak | 27 plików |
| Web-Popularyzacja | strona działu, strony | 176 | 6 | tak | 5 plików |
| Web-Instytut | strona działu, zakłady, strony, „Warto wiedzieć”, władze | 622 | 14 | nie | 0 |
| Web-Nauka | strona działu, konferencje, projekty i granty, publikacje, wykazy prac, strony | 543 | 11 | nie | 0 |
| Web-Aktualnosci | aktualności, obrony doktorskie, strony | 403 | 8 | nie | 0 |
| Web-Pracownicy | pracownicy, strony | 196 | 5 | nie | 0 |
| Web-Ustawienia (tylko właściciel) | strona główna i kontakt, „Na skróty”, menu główne, deklaracja dostępności, polityka prywatności, O stronie | 692 | 10 | nie | 0 |
| Web-Sem-* (9, jeden układ) | opis seminarium, referaty | ok. 167 | ok. 4 | nie | 0 |

- **Gdzie Web-Core już obsługuje `format_tresci: jawne`:**
  - „Strony” wszystkich repozytoriów (`src/lib/widoki/strona.ts`, `tekstyStron.ts`);
  - strony działów (`tekstyStron.ts`, ok. linii 185);
  - kierunki, specjalności, Popularyzacja, Rok akademicki.
- **Gdzie nie obsługuje:** wpisy, czyli aktualności, obrony, konferencje, granty, zakłady, „Warto wiedzieć”, pracownicy, opisy seminariów i referaty.
- **Narzędzia w Web-Core:**
  - `skrypty/usun-otoczki-proza.mjs`: migracja samej składni, bez zmian tekstu; raport albo `--zapisz`; dziś dla Web-Studia;
  - `porownaj-jawny-markdown.mjs`: porównanie treści stron przed i po;
  - `sprawdz-jawny-markdown.mjs`: formularz i powiązania; dziś dla Web-Studia;
  - `test-jawny-markdown-ui.mjs`;
  - `sprawdz_pola_cms.py`: dane kontra formularze.
- **Pages CMS wstawia `default` każdego pola**, także pola `code`, gdy pole jest puste lub brakuje go przy otwarciu wpisu (`lib/schema.ts`, `initializeState` → `getDefaultValue`).
- **Web-Spec-* (5 repozytoriów) poza zakresem.** Nie ma ich w `tresci.json`; zostają puste na później.

## Etap 0. Inwentaryzacja (bez zmian w repozytoriach) → raport i STOP

1. **Pola.** Dla każdego pola każdego formularza (oprócz Web-Spec-*) ustal:
   - czy strona je czyta (wyszukaj w kodzie Web-Core);
   - czy w danych ma treść (ile wpisów).

   Przypisz pole do jednej kategorii:
   - **używane** → zostaje;
   - **puste i nieużywane** → do usunięcia;
   - **z treścią, ale nieużywane** → decyzja właściciela: ukryć (`hidden: true`), podłączyć (np. opisy konferencji) albo usunąć (treść zostaje w historii gita);
   - **techniczne** → ukryć.
2. **Teksty.** Dla każdej strony i strony działu:
   - lista układów, które dziś rozpoznaje stary parser (kafelki, osie, pytania, pliki…);
   - odpowiadające im bloki jawne;
   - liczba plików.

   **Wpisy zostają formularzami.** Strona sortuje je, filtruje i liczy z ich pól.
3. **Projekt opisów:** tabela kolekcji z proponowanym `description` i kolejnością pól. Tylko krótko: zmiany względem dziś.
4. **Szablony nowych wpisów** (aktualność, konferencja, grant, zakład, referat…): propozycja treści domyślnej pola Treść (`default`), np.:
   - `<!-- TEKST: Zwykły tekst. Akapity oddziela pusta linia. Pliki: wgraj w „Media” i wklej link. -->`
   - plus 1–2 komentarze o tym, co w danym wpisie bywa (lista plików, link do rejestracji).

   Sprawdź, czy strona nie wyświetla komentarzy we wpisach (stary parser) i czy pusta treść z samym komentarzem nie zmienia wyglądu (np. „czytaj więcej”, zajawka). Jeśli zmienia, opisz to i zaproponuj, jak tego uniknąć.

**STOP.** Właściciel decyduje o polach z treścią i zatwierdza (albo poprawia) opisy i szablony.

## Etapy 1–6. Repozytorium po repozytorium

**Kolejność:**
1. Web-Instytut;
2. Web-Nauka;
3. Web-Aktualnosci;
4. Web-Pracownicy;
5. seminaria: jeden wzór formularza dla 9 repozytoriów, wdrożony skryptem we wszystkich;
6. Web-Ustawienia;
7. na koniec porządek pól w Web-Studia i Web-Popularyzacja (format już jawny).

**W każdym repozytorium:**
1. **Baza.** Zanotuj HEAD świeżego `main` repozytorium (baza do „Ochrony zmian redaktorów”).
2. **Web-Core najpierw.**
   - Schemat: usuwane pola wypadają albo stają się opcjonalne.
   - Jeśli trzeba, obsługa jawnego formatu tam, gdzie go nie ma (tylko strony i strony działów).
   - Jeden commit na lokalnej gałęzi Web-Core.
3. **Strony i strona działu → jawny Markdown.**
   - `format_tresci: jawne` (ukryte pole w formularzu, `default: jawne`).
   - Bloki jawne w miejsce automatycznego rozpoznawania, z komentarzami przy blokach w stylu Studiów.
   - `{#id}` zachowujące dzisiejsze adresy sekcji.
   - Migracja skryptem: uogólnij `usun-otoczki-proza.mjs` / `porownaj-jawny-markdown.mjs` / `sprawdz-jawny-markdown.mjs` na dowolne repozytorium. Bez zmian tekstu.
4. **Formularze:**
   - kolejność: Treść na górze;
   - opisy kolekcji i pól według zatwierdzonego projektu;
   - pola techniczne ukryte;
   - usunięcia i ukrycia według decyzji z etapu 0;
   - szablony nowych wpisów (`default`), jeśli zatwierdzone.
5. **Wpisy:** format bez zmian. Pole Treść dostaje opis-ściągawkę dla zwykłego tekstu.
6. **Kontrola:**
   - porównanie HTML przed/po wszystkich stron z tego repozytorium (PL i EN): **0 różnic**, poza zgłoszonymi i zatwierdzonymi;
   - `sprawdz_pola_cms.py` 0 problemów;
   - uogólniony `sprawdz-jawny-markdown.mjs` OK;
   - `astro check` bez nowych błędów;
   - zrzuty tylko tam, gdzie porównanie pokazało różnicę.
7. **Push po „push”:** najpierw Web-Core, potem repozytorium treści, z kontrolą przed i po pushu (sekcja „Ochrona zmian redaktorów”).
8. **Test w CMS z właścicielem:**
   - otwarcie formularza;
   - zapis bez zmian: diff pusty albo tylko kosmetyka formatu, opisana;
   - zapis z drobną zmianą;
   - nowy wpis z szablonem.
9. **Następnego dnia:** przegląd zapisów redaktorów z 24 godzin po pushu.

## Na koniec
- Zaktualizuj `dok/jawny-markdown.md` (zakres: wszystkie działy) i `dok/sciagawka-edytora.md`.
- PDF-y dla redaktorów (`Web-Podglad/dla-redaktorow/`): aktualizacja albo lista zmian do naniesienia w raporcie.

## Kryteria odbioru
- [ ] W każdym repozytorium treści (bez Web-Spec-*) strony i strona działu są w jawnym Markdownie, z komentarzami przy blokach jak w Studiach.
- [ ] Każda kolekcja ma opis „co to i gdzie widać”; pola mają krótkie opisy z przykładem; Treść jest na górze; pola techniczne są ukryte.
- [ ] Pola nieużywane usunięte, ukryte albo podłączone według decyzji właściciela; strona nie straciła żadnej wyświetlanej treści.
- [ ] Wygląd stron bez zmian (porównanie HTML), poza zatwierdzonymi różnicami.
- [ ] `sprawdz_pola_cms.py` 0 problemów; zapis w CMS przetestowany w każdym repozytorium.
- [ ] Ściągawka, `jawny-markdown.md` i PDF-y dla redaktorów aktualne.
- [ ] W każdym repozytorium kontrola zmian redaktorów przed i po pushu w raporcie: wszystkie zapisy redaktorów zachowane. Przegląd z następnego dnia zrobiony.
