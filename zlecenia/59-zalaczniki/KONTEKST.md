# Wspólny kontekst: przegląd i uzupełnienie wersji angielskiej strony IM UWr (22.11.2026)

## Zadanie (słowa właściciela strony)
„Sprawdźcie wersję angielską strony i znajdźcie, czy wszystkie miejsca mają odpowiedni angielski tekst. Jeśli nie, zredagujcie angielski tekst na podstawie polskiego.”

Czyli w swoim zakresie (podział niżej):
1. **Znajdź** każde miejsce, w którym strona `/en/...` pokazuje tekst polski zamiast angielskiego albo angielski zły (niepełny, nieaktualny względem polskiego, z błędami, niezgodny z zasadami niżej).
2. **Napisz/popraw** angielski tekst na podstawie polskiego, w odpowiednim polu `_en` (albo `tresc_en`) w plikach treści. Polskiego tekstu **nie zmieniasz** (błędy w polskim zgłoś w raporcie).
3. Rzeczy, których nie da się naprawić w treści (brak pola `_en` w schemacie, napis wpisany w kod), opisz w raporcie w sekcji „Potrzebne zmiany w kodzie” — z plikiem, linią i propozycją tłumaczenia. Kod zmienia tylko agent 3.

## Gdzie co jest (wszystko w chmurze, nic nie jest na komputerze właściciela)
- `/home/claude/en/repo/<Repo>` — **czyste** klony z GitHuba (stan main, SHA w `wspolne/bazy-sha.txt`). **Tylko do odczytu, nie zmieniaj.**
- `/home/claude/en/agenci/<N>/<Repo>` — **Twoje** kopie robocze (git, stan main). Tylko tu edytujesz. **Nie commituj, nie pushuj, nie dodawaj zdalnych repozytoriów.** Żadnych operacji na GitHubie.
- `/home/claude/en/site/Web-Core/` — zbudowana cała strona (stan main, tryb Podglądu: wszystkie wpisy, także nieopublikowane). Strony angielskie: `site/Web-Core/en/**/index.html`. Do oglądania obecnego stanu; nie przebudowuj całej strony (7 minut, dużo CPU), chyba że jesteś agentem 3 i testujesz kod (wtedy we własnej kopii).
- `/home/claude/en/skan.json` — wynik automatycznego skanu stron `/en` (adres → lista fragmentów z polskimi znakami/słowami; trzecie pole to `lang` elementu: `pl` = pole `_en` puste i strona pokazała polski tekst). Skan jest zgrubny: łapie też nazwiska i tytuły, które celowo zostają po polsku. Własny skan zakresu: `python3 /home/claude/en/narzedzia/skan_pl.py /home/claude/en/site/Web-Core /en/nauka/granty`.
- `/home/claude/en/repo/Web-Core/src/content.config.ts` — schemat treści: które pola mają wersję `_en`.
- `/home/claude/en/repo/Web-Core/dok/en/TLUMACZENIA.md` — słownik i dotychczasowe tłumaczenia (przeczytaj sekcje 1, 4, 5; trzymaj się przyjętych tam nazw).
- `/home/claude/en/repo/Web-Core/dok/en/POSTEP.md` — co już zrobiono przy pierwszym tłumaczeniu (5.11).
- `/home/claude/en/wspolne/instrukcja-dla-czatow.md` — zasady pisania Treści i Treści EN (Markdown, bloki, styl „Warto wiedzieć”). **Obowiązkowe.**
- `/home/claude/en/repo/Web-Core/skrypty/sprawdz_tresci.py` — szybka kontrola YAML i wymaganych pól: `python3 /home/claude/en/repo/Web-Core/skrypty/sprawdz_tresci.py <katalog lub plik>`.

## Jak strona używa wersji EN
- Strony angielskie mają adresy `/en/...`. Pole `X_en` puste → strona pokazuje polskie `X` z `lang="pl"`. Treść Markdown: polska w body pliku `.md`, angielska w polu `tresc_en` we frontmatterze (puste → polska).
- Linki wewnętrzne w Treści EN zostają bez `/en` (strona dopisuje sama).
- Nowe teksty są w polach, które już istnieją w schemacie. **Nie dodawaj nowych pól**, których nie ma w `content.config.ts` (zgłoś w raporcie). Jeśli pole istnieje w schemacie, ale nie ma go w `.pages.yml` danego repozytorium, wpisz wartość i zgłoś brak pola w CMS w raporcie.

## Format zapisu w plikach
- Frontmatter musi zostać poprawnym YAML. Dłuższe teksty (`tresc_en`) zapisuj jako blok literalny `|-` z wcięciem 2 spacji, wiersz po wierszu jak Markdown (akapit = jedna linia, puste linie między akapitami). Krótkie pola jako zwykły tekst w jednej linii; jeśli zawiera `: `, `#`, cudzysłów na początku itp., ujmij w cudzysłów.
- Nowe pole `X_en` wstaw zaraz po polu `X` (albo tam, gdzie stoją inne pola `_en` w tym pliku), nie przestawiaj pozostałych pól, nie zmieniaj formatowania reszty pliku (żeby różnica była mała).
- Pliki JSON: zachowaj wcięcia i kolejność kluczy, `ensure_ascii=False`.
- Po każdym pliku sprawdź: YAML się wczytuje, wartość po wczytaniu jest dokładnie taka, jak chcesz (żadnych zgubionych znaków), `sprawdz_tresci.py` bez błędów, a w Treści EN te same `{#id}` i ta sama liczba bloków `:::` co w polskiej.

## Zasady tłumaczenia (decyzje właściciela, 5.11.2026 i później — obowiązują)
- **Pisownia brytyjska** (programme, specialisation, centre, defence, honour, organise). Rzeczowy ton.
- **Stały słownik:** Instytut Matematyczny = Mathematical Institute; Uniwersytet Wrocławski / UWr = University of Wrocław; Wydział Matematyki i Informatyki = Faculty of Mathematics and Computer Science; Instytut Informatyki = Institute of Computer Science; Warto wiedzieć = Highlights; Aktualności = News; Popularyzacja = Outreach; Seminarium wydziałowe = Faculty seminar; obrona doktorska = PhD defence; Szkoła Doktorska = Doctoral School; zakład = (np. Zakład Statystyki) Department of Statistics — sprawdź w TLUMACZENIA.md i w istniejących `nazwa_en`, jakich nazw już używamy, i trzymaj się ich.
- **D1 — tytuły przy nazwisku na `/en`:** prof. dr hab. oraz „dr hab., prof. UWr” → „Prof. X”; dr hab. → „Dr hab. X”; dr, dr inż. → „Dr X”; mgr, mgr inż. → bez tytułu (wyjątek: doktorant przy obronie „X, MSc”). Bez amerykańskich stanowisk (Assistant/Associate Professor).
- **D4 — tytuły prac (dyplomowych itp.) w aktualnościach:** tytuł w oryginale, tłumaczenie w nawiasie: *„Tytuł polski”* (English translation).
- **D5 — tytuły rozpraw na stronach obron:** zostają w oryginale (kod dopisuje „Original title:”). Nie tłumacz pola tytułu rozprawy, chyba że schemat ma osobne pole EN i polski tytuł jest po polsku — wtedy zgłoś w raporcie, nie wypełniaj.
- **D6 — nazwy przedmiotów z USOS** w tekstach: nazwa polska kursywą + angielski odpowiednik w nawiasie przy pierwszym użyciu.
- **D8 — konkursy i programy** („Krok w Przyszłość”, „Diamentowy Grant”, OPUS, PRELUDIUM, SONATA…): nazwa polska + tłumaczenie w nawiasie przy pierwszym użyciu; nazwy programów NCN zostają bez tłumaczenia (to nazwy własne). Ujednolicaj z tym, co już jest w treściach.
- **D10 — tytuły referatów** zostają w oryginale; przy referacie po polsku kod dopisuje „(talk in Polish)”.
- **D17 — tematy prac na stronach specjalności** nie są tłumaczone.
- **D19 — daty w Treści EN** w zapisie angielskim („19 November 2026”, „1–15 October”).
- **D20 — linki do stron tylko po polsku** dostają „(in Polish)”.
- **Tytuły publikacji, książek, czasopism, prac, rozpraw, referatów** — w oryginale. **Nazwiska, adresy, e-maile, numery sal** — bez zmian (oprócz „s.”/„sala” → „room”).
- **Wzory i komentarze `<!-- … -->`** przepisujesz bez zmian.
- **Nie wymyślaj faktów.** Tłumaczysz to, co jest w polskim tekście. Jeśli polski tekst jest niejasny albo wygląda na błędny, tłumacz wiernie i zgłoś w raporcie.
- **Gdy angielski tekst już jest:** porównaj z polskim. Jeśli jest dobry i zgodny treścią — zostaw (nie przerabiaj dla stylu). Popraw, jeśli: czegoś brakuje względem polskiego (polski był później uzupełniony), są błędy językowe, niezgodność z decyzjami wyżej (np. „Institute of Mathematics” zamiast „Mathematical Institute”, amerykańska pisownia, tytuły D1), inne `{#id}`/bloki niż w polskim, zostawione polskie zdania.
- **Wpisy testowe** („TEST:”, „Testowe”, „Mister Test”, `test-*`) — nie tłumacz, wypisz w raporcie (są do usunięcia przed startem).

## Wyniki (obowiązkowo)
W katalogu `/home/claude/en/wyniki/<N>/`:
1. `<Repo>.patch` — dla każdego repozytorium, które zmieniłeś: `git -C /home/claude/en/agenci/<N>/<Repo> diff > /home/claude/en/wyniki/<N>/<Repo>.patch` (bez commitów; nowe pliki — nie twórz ich, chyba że konieczne, wtedy `git add -N` przed diff). Sprawdź, że łatka nakłada się na czysty klon: `git -C /home/claude/en/repo/<Repo> apply --check <łatka>`.
2. `raport.md` (po polsku, zwięźle):
   - **Podsumowanie:** ile plików/pól sprawdzono, ile uzupełniono (brakowało EN), ile poprawiono (EN był, ale zły), ile zostawiono.
   - **Tabela zmian:** plik → pole → co zrobiono (uzupełnione / poprawione + w 3–8 słowach dlaczego).
   - **Potrzebne zmiany w kodzie:** napisy po polsku na `/en`, których nie da się naprawić w treści (plik w Web-Core, linia, PL → proponowane EN), oraz pola, których brakuje w schemacie albo w `.pages.yml`.
   - **Do decyzji właściciela:** sporne tłumaczenia nazw, rzeczy wymagające wiedzy spoza tekstu.
   - **Błędy w polskim tekście** zauważone przy okazji (nie poprawiaj).
   - **Wpisy testowe**.
3. Przed oddaniem: `python3 /home/claude/en/repo/Web-Core/skrypty/sprawdz_tresci.py` na każdym zmienionym repozytorium (kopia robocza) bez błędów; `git apply --check` każdej łatki na czystym klonie OK.

## Podział na 4 agentów
- **Agent 1:** Web-Instytut — „Warto wiedzieć”: sylwetki `andrzej-hulanicki`, `andrzej-krzywicki`, `bronislaw-knaster`, `czeslaw-ryll-nardzewski`, `edward-marczewski`, `hugo-steinhaus`, `jan-mycielski`, `julian-perkal`, `kazimierz-urbanik` oraz wszystkie `nagrody/*`.
- **Agent 2:** Web-Instytut — „Warto wiedzieć”: sylwetki `krzysztof-tabisz`, `marek-bozejko`, `piotr-biler`, `roman-duda`, `stanislaw-hartman`, `tomasz-rolski`, `witold-wolibner`, `wladyslaw-narkiewicz`, `wladyslaw-slebodzinski` oraz wszystkie `historie/*`.
- **Agent 3:** kod Web-Core (napisy interfejsu na `/en`, mapy tłumaczeń `src/lib/en/*` — plan zajęć i publikacje, teksty domyślne w kodzie), Web-Ustawienia (menu, stopka, strony działów, strony prawne, o stronie, ciekawostki…), Web-Instytut **poza** `warto_wiedziec` (strony, zakłady, władze, instytut.md, w tym strona listy „Warto wiedzieć”), Web-Pracownicy, Web-Studia (kierunki, specjalności, strony studiów, tutornia, rok akademicki, szkoła doktorska), Web-Popularyzacja. Jedyny agent, który zmienia kod.
- **Agent 4:** Web-Aktualnosci (aktualności, obrony doktorskie, kariera, strony), Web-Nauka (konferencje, granty, sukcesy, publikacje — strony i dane), 9 repozytoriów Web-Sem-* (opisy seminariów, referaty: afiliacje, sale, streszczenia).

Repozytoria Web-Spec-* nie są już używane przez stronę (specjalności są w Web-Studia) — pomiń je.

Nie wchodź w zakres innego agenta. Jeśli coś z Twojego zakresu wymaga zmiany u innego (np. brak tłumaczenia w kodzie), opisz to w raporcie.
