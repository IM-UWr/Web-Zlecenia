# Zlecenie 30: teksty działów i stron z listami w „Stronach”, porządek formularzy, bez wyróżnień aktualności (GOTOWE, 7.11.2026)

Trzecie z trzech zleceń „sprzątania CMS”. **Start po odbiorze lokalnym zleceń 28 i 29.** Tryb bez nadzoru: jak w 28; na końcu tego zlecenia jest wspólny push i test w CMS dla 28, 29 i 30 (etap 5). Zasady i „Gdzie i jak” jak w `28-cms-kierunki-markdown.md`; poniżej różnice. Raport `RAPORT-ZLECENIE-30.md`, zrzuty `raport-zrzuty/z30-*`. Oszczędnie jak w 28 (bez subagentów, tylko potrzebne pliki, w raporcie lista różnic).

**Cel.** Każdy tekst strony leży w repozytorium, z którego pochodzi treść tej strony, a nie w Web-Ustawienia, i edytuje się go jak każdą stronę (tekst na górze, drobne pola pod spodem). Web-Ustawienia zostaje tylko dla właściciela: strona główna, menu, „Na skróty”, stopka, strony prawne i lista kierunków (z zlecenia 28). Formularze wpisów mają jeden porządek. Znika wyróżnianie aktualności.

**Decyzje właściciela (7.11, 00:40–01:05)**
- Tekst strony jest tam, gdzie jej treść. Strona działu i teksty nad listami (Seminaria, Konferencje…) to strony, nie pola w Ustawieniach.
- Strona to Markdown; **wpis** (konferencja, grant, aktualność, obrona, zakład, pozycja „Warto wiedzieć”) zostaje formularzem, bo strona sortuje, filtruje i liczy z jego pól.
- W formularzu **strony**: tekst na górze. W formularzu **wpisu**: najpierw to, bez czego wpis nie istnieje (tytuł, daty, miejsce), potem tekst, potem reszta.
- **Rezygnujemy z wyróżniania wpisów w aktualnościach** („niepotrzebna komplikacja, wywalamy z CMS i z kodu”).
- Seminaria i referaty bez zmian: tekst zostaje w edytorze kodu (Markdown z LaTeX-em), bo edytor z przyciskami mógłby psuć wzory.
- Władze Instytutu: później, nie w tym zleceniu.

**Gdzie:** klony Web-Ustawienia, Web-Instytut, Web-Nauka, Web-Studia, Web-Aktualnosci, Web-Pracownicy, Web-Popularyzacja; Web-Core. Etap 0 jak w 28 (stan, edytorzy, zdjęcie „przed” wszystkich stron z tabeli w etapie 1, strony głównej i stron działów, PL i EN).

## Etap 1. Teksty z Web-Ustawienia (`src/data/dzialy/*.json`) na swoje miejsca
Strona działu to **osobny wpis typu `file` „Strona działu …”** na górze listy w repozytorium działu, tak jak w zleceniu 29 dla Popularyzacji. Teksty nad listami to **strony w kolekcji „Strony”** tego repozytorium, pod adresem strony z listą (reguła „adres = ścieżka pliku”). Ścieżki ustal według dzisiejszych adresów stron.

| Dziś (Ustawienia) | Po zmianie |
|---|---|
| `instytut.json`: `wstep`, `haslo`, `o_instytucie`, `o_instytucie_fakty`, `sukcesy_opis` | Web-Instytut → **Strona działu Instytut**: Treść = „O Instytucie”; zdanie nad sukcesami pod kotwicą „Ostatnie sukcesy” w treści; pod spodem Wstęp, Hasło, „W skrócie” |
| `instytut.json`: `struktura_haslo`, `struktura_tekst` | Web-Instytut → Strony → **Struktura i zakłady** |
| `instytut.json`: `warto_wiedziec_haslo` | Web-Instytut → Strony → **Warto wiedzieć** |
| `instytut.json`: `kontakt_godziny` | tam, gdzie się wyświetla (sprawdź): w treści strony albo jako drobne pole jej ramki |
| `instytut.json`: `pracownicy_haslo` | Web-Pracownicy → Strony → **Pracownicy** |
| `nauka.json`: `wstep`, `haslo`, `badania_tekst`, `badania_fakty` | Web-Nauka → **Strona działu Nauka** (Treść = „Badania w Instytucie”) |
| `nauka.json`: `seminaria_*`, `konferencje_*`, `granty_*`, `sukcesy_*` | Web-Nauka → Strony → **Seminaria**, **Konferencje**, **Projekty i granty**, **Sukcesy** (Treść = tekst wprowadzający, Hasło w ramce) |
| `nauka.json`: `publikacje_*`, `czasopisma_tekst`, `rocznik_haslo` | Web-Nauka → Strony → **Publikacje**: jeden tekst; część o czasopismach pod kotwicą „Czasopisma redagowane w Instytucie” (EN: nagłówek jak dziś na stronie), lista czasopism pod nią; hasło strony rocznika w ramce |
| `nauka.json`: `obrony_*`, `obrona_haslo` | Web-Aktualnosci → Strony → **Obrony doktorskie**; hasło strony pojedynczej obrony w ramce |
| `studia.json`: `wstep`, `haslo`, `o_studiach`, `o_studiach_fakty`, `sekretariat_zakres` (ukryte od zlecenia 22) | Web-Studia → **Strona działu Studia** (`sekretariat_zakres` dalej ukryte) |
| `studia.json`: `plan_haslo` | Web-Studia → Strony → **Plan zajęć** |
| hasło „Co słychać w Instytucie” (wpisane w kod) | Web-Aktualnosci → Strony → **Aktualności** |

- Web-Aktualnosci i Web-Pracownicy dostają kolekcję „Strony” z tym samym formularzem co inne repozytoria.
- **Brak strony nic nie psuje:** lista działa dalej, z domyślnym tytułem i hasłem jak dziś, bez tekstu. Sprawdź to na jednej stronie, którą usuniesz na próbę.
- Tytuł strony z listą bierze się z jej formularza (na start obecny tytuł z kodu). Napis w menu zostaje w ustawieniach menu.
- Kotwice „Ostatnie sukcesy” i „Czasopisma redagowane w Instytucie” dopisz do wspólnej listy kotwic.
- Teksty przenosi skrypt `skrypty/migracja/dzialy.*`, słowo w słowo, PL i EN (dzisiejsze „akapity oddzielone pustą linią” to już Markdown). Potem: pliki `src/data/dzialy/*.json` i formularze „Strona działu …” znikają z Web-Ustawienia; kod przestaje je czytać.

## Etap 2. Bez wyróżnień aktualności
- Usuń pole `wyroznij_do` z formularza Web-Aktualnosci, ze schematu w `content.config.ts` i z plików aktualności (lista plików do raportu).
- Usuń `wyroznionaAktualnosc()` (`src/lib/tresci.ts`) i plakietkę na okładce (`wyrozniona` w `StronaGlowna.astro` i `zal/Okladka.astro`, klasa `z-okl-flaga`, `--flaga-max` i powiązane style oraz skrypt).
- **Zostaje** automatyczne powiększenie pierwszej, najnowszej aktualności na listach (`DrugiEkran.astro`, `ListaAktualnosci.astro`, `WierszAktualnosci.astro`). To nie wyróżnienie i nie ma pola.

## Etap 3. Porządek formularzy (`.pages.yml`)
**Strony** (kolekcje „Strony” we wszystkich repozytoriach, strony prawne w Web-Ustawienia, Rok akademicki):
- Tytuł · **Treść** · Tytuł EN · **Treść EN**, a pod spodem: Opis (pod tytułem i w Google), Hasło, Liczby, Prawy pasek.
- Treść EN jako `rich-text` (`format: markdown`) zamiast gołego `text`, tak jak w 28.
- Rok akademicki: tak samo, z dwoma polami tekstu (Treść i Koniec strony, każde z EN), bo między nimi strona wstawia kalendarz.
- Nowe widoczne pole **„Bloki”** (`bloki`, boolean, domyślnie wyłączone, etykieta: „Kafelki, oś i kontakty z list — zob. ściągawka”). Dziś `bloki: true` znika przy pierwszym zapisie, bo nie ma go w formularzu.

**Wpisy** (aktualności, obrony, konferencje, granty, zakłady, Warto wiedzieć): najpierw pola wymagane w schemacie Astro (tytuł / nazwa, daty, miejsce, rodzaj), potem Treść i Treść EN (`rich-text` tam, gdzie Treść EN już jest), potem reszta. Nowych pól EN nie dodawaj.
- Konferencje: `organizatorzy` strona nigdzie nie pokazuje → pole ukryte (danych nie kasujemy).
- Zakłady i Warto wiedzieć: pod tekstem jedna grupa pól „Karta” (krótka nazwa, kierownik, obszary, zdjęcie… / rok, zajawka, zdjęcie, link…).

**Bez zmian:** Web-Sem-* (seminaria i referaty, edytor kodu), Władze, Kalendarz zajęć, publikacje i wykazy, pracownicy (same dane).

Opis pola „Treść” na stronach z `bloki` i na stronach działów: krótka wersja ściągawki z `dok/sciagawka-edytora.md`. Uzupełnij ją o zasadę „tekst nad listą: lista stoi pod całym tekstem, chyba że jest kotwica”.

`sprawdz_pola_cms.py`: nowe kolekcje i pliki, 0 problemów.

## Etap 4. Odbiór lokalny
- Porównanie przed/po (jak w 28): strony działów (Instytut, Nauka, Studia), wszystkie strony z tabeli w etapie 1, jedna obrona, jeden rocznik publikacji, strona główna, PL i EN.
- Dozwolone różnice: brak plakietki wyróżnionej aktualności na okładce; inne tylko zgłoszone i uzasadnione.
- Zrzuty tylko tam, gdzie porównanie HTML pokazało różnicę (przed/po, 1440 i 390 px, tylko PL), jak w 28; tu na pewno okładka bez plakietki. Jeden raport na koniec zlecenia.
- Kontrole: `sprawdz_pola_cms.py` 0, `sprawdz_tresci.py` OK, `astro check` bez nowych błędów.
- Dopisz do `.przekazanie\zlecenia\zasady.md`: nowe teksty stron idą do „Stron” repozytorium działu; Web-Ustawienia tylko strona główna, menu, „Na skróty”, stopka, strony prawne i lista kierunków.
- Symulacja zapisu w edytorze jak w 28, etap 6a, dla nowych i przestawionych stron (w tym Pierwszy rok z Treścią EN).
- **Stop**, raport, czekanie na „push”. Jeśli 28–30 szły w trybie bez nadzoru: jeden krótki raport zbiorczy na górze `RAPORT-ZLECENIE-30.md` (co zrobione, co przyjęte bez pytania, co czeka na właściciela).

## Etap 5. Po słowie „push” (wspólny dla 28, 29 i 30)
Najpierw `git pull --rebase` w klonach i konflikty do właściciela. Wypchnij `wyglad/zlecenie-16` we wszystkich repozytoriach dotkniętych przez 28, 29 i 30 razem z Web-Core. Sprawdź Web-Podglad. Test w CMS na `test-cms` (właściciel, jedno podejście): punkty z zlecenia 28 (etap 8) i 29 (etap 5), a do tego:
1. Web-Studia → Strony → **Pierwszy rok**: otwórz i zapisz bez zmian (długa strona z tabelami; Treść EN pierwszy raz w edytorze z przyciskami).
2. Web-Nauka → Strony → Konferencje: dodaj link w tekście.
3. Web-Nauka → Strona działu Nauka: zmień jedną liczbę „W skrócie”.
4. Web-Aktualnosci: nowa aktualność (bez pola wyróżnienia), potem usuń.

Porównanie, budowa z `test-cms`, wynik do raportu, usunięcie `test-cms`.

## Kryteria odbioru
- [ ] W Web-Ustawienia nie ma tekstów działów ani stron z listami; formularze „Strona działu …” są w repozytoriach działów.
- [ ] Każda strona z tabeli w etapie 1 ma swój wpis; usunięcie wpisu niczego nie psuje.
- [ ] `wyroznij_do` usunięte z formularza, schematu, plików i kodu; plakietki na okładce nie ma; pierwsza aktualność na listach dalej powiększona.
- [ ] Formularze stron: tekst na górze, Treść EN w edytorze z przyciskami, pole „Bloki”. Formularze wpisów: pola wymagane, potem tekst.
- [ ] Porównanie przed/po: tylko dozwolone różnice.
- [ ] Kontrole: 0 / OK / bez nowych błędów. Test w CMS: zapis bez zmian daje tę samą stronę.
