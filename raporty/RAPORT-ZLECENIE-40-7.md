# Raport: zlecenie 40, etap 7 — porządek pól w Web-Studia i Web-Popularyzacja (18.11.2026)

## Stan
> **Aktualizacja 18.11, 17:20:** Web-Studia, Web-Popularyzacja i PDF wypchnięte 18.11 o 17:14 i 17:17 (przed wieczorem, na Twoje polecenie) — wynik w „Push treści” i „Dokumentacja”.

- **Web-Core** (część skryptów): wypchnięta, opis niżej w „Push Web-Core”.
- **Web-Studia i Web-Popularyzacja: commity gotowe, push wieczorem**, zaplanowany na **23:13** (po 33, 40.1, 40.2, 40.4, 40.5 i 40.6). Skrypt: `push40_studia_popularyzacja.sh` w scratchpadzie.
  - Klony robocze: `tresci-z40/Web-Studia` (gałąź `praca/40-studia`) i `tresci-z40/Web-Popularyzacja` (gałąź `praca/40-popularyzacja`).
  - **Bazy** (świeży `main`): Web-Studia `b2a7c09`, Web-Popularyzacja `0f76f88`. O 15:30 brak zapisów od bazy w obu.
- Format treści w obu repozytoriach był już jawny (wzorzec zlecenia), więc etap 7 to tylko formularze i jedno pole z decyzji 1a.

## Co zrobiłem

### Web-Studia (`.pages.yml` i 4 pliki kierunków)
- **Kierunki → Baner:**
  - pola EN pod polskimi: nadtytuł, nadtytuł EN, zdanie, zdanie EN, hasło, hasło EN, liczby;
  - liczby: wartość, wartość EN, podpis, podpis EN, pozycja;
  - **usunięte** `etykieta_krotka` i `etykieta_krotka_en` (krótszy podpis liczby; decyzja 18.11, lista 1a): z formularza i z nagłówków 4 plików kierunków (isim, matematyka, siad, szkoła doktorska). Strona tych pól nie czyta. Treść plików bez zmian.
- **Nadtytuł** (`podtytul`, `podtytul_en`): opis „Na stronie się nie wyświetla…” (patrz pytanie 1).
- **Strona działu:** „Wstęp pod tytułem” → „Opis strony dla Google (1–2 zdania)”, z opisem i przykładem (nowy nagłówek działu go nie pokazuje; trafia do Google i do podglądu linku).
- **Strony:**
  - „Krótki opis” → „Krótki opis (Google i podgląd linku)”, opis „Na samej stronie się nie wyświetla”;
  - hasło: opis „Hasło i liczby pokazują się na banerze tylko razem” (patrz „Przyjąłem sam”).
- **Przypomnienia** i **ogłoszenia o zamianach dni** (Kalendarz zajęć): pola EN pod polskimi.
- Wszędzie etykiety „EN: …” → „… EN”.
- Styl pliku `.pages.yml` bez zmian (listy wcięte jak w źródle); diff pokazuje tylko zmienione pola.

### Web-Popularyzacja (`.pages.yml`)
- **Strona działu i Strony:** tytuł EN pod tytułem, Treść i Treść EN na górze, pola EN pod polskimi.
- **Strona działu:** „Tekst pod tytułem” → „Opis strony dla Google (1–2 zdania)” (nowy nagłówek działu go nie pokazuje).
- **Strony:** opis i hasło z etykietami według tego, gdzie je widać: zdanie i tytuł karty „Dla kogo” na stronie Popularyzacji (dotąd etykiety mówiły też o banerze strony, a nowy baner ich nie pokazuje).
- Etykiety „EN: …” → „… EN”.

### Web-Core (skrypty)
- `formularze_40.mjs`: części Web-Studia i Web-Popularyzacja; operacja `naglowkiMd` (zmiana nagłówka YAML plików `.md` bez ruszania Treści); styl list w `.pages.yml` jak w źródle (Web-Studia ma listy wcięte, pozostałe repozytoria nie).
- `kontrola_redaktorow.py`: `--pomin` działa też dla pól w pozycjach list (np. `baner.liczby.etykieta_krotka`).

## Kontrole
- **Porównanie HTML całej strony** (Web-Studia: dane z `main` vs dane z commitu, ten sam kod): **0 różnic** w 925 plikach. Web-Popularyzacja zmienia tylko `.pages.yml` (budowa go nie czyta).
- **Skrypt na pozostałych repozytoriach** (Instytut, Nauka, Pracownicy, Ustawienia, 9 seminariów) po zmianach: „Bez zmian”.
- **Porównanie `.pages.yml` pole po polu** (przed/po): zmieniły się tylko kolejność, etykiety i opisy wymienione wyżej oraz usunięte `etykieta_krotka(_en)`; wartości `default`, `hidden`, `required`, `options` bez zmian.
- `sprawdz_pola_cms.py`: **0 problemów** (16 repozytoriów; Studia i Popularyzacja z klonów roboczych).
- `sprawdz-jawny-markdown.mjs`: **OK** (Web-Studia: 27 wpisów, 420 nagłówków `##`, wszystkie z `{#id}`; Web-Popularyzacja: 5 wpisów, 40 nagłówków).
- `kontrola_redaktorow.py`:
  - `przed`: 0 zapisów od bazy w obu repozytoriach;
  - `po` (baza → commit): „OK, tylko zmiany z migracji” (Web-Studia z `--pomin baner.liczby.etykieta_krotka`, `…_en`; bez tej opcji te pola są wykazane, więc kontrola działa).
- `astro check`: 0 błędów, 0 ostrzeżeń.

## Przyjąłem sam
- **Hasło na Stronach Studiów** (decyzja 18.11, pytanie 3: ukryć pole tam, gdzie się nie pokaże): w Web-Studia hasło ma 13 z 14 Stron, a pokazuje się tylko na 4 stronach z liczbami: Egzaminy i dyplom, Skrypty, Dokumenty szkoły doktorskiej (pole „Liczby”) i Plan zajęć (liczby z planu). Jeden formularz obsługuje wszystkie Strony, więc pola nie da się ukryć tylko na części z nich. Zostawiłem je widoczne, z opisem, kiedy się pokazuje.
- **Strony Popularyzacji:** opis i hasło zostają widoczne, bo pokazują się na kartach „Dla kogo”; poprawiłem tylko etykiety i opisy.
- **`etykieta_krotka` usunięte także z plików kierunków**, nie tylko z formularza (CMS i tak wyciąłby je przy pierwszym zapisie; tak samo jak w etapie 6).

## Pytania do Ciebie
1. **Nadtytuł kierunku (`baner.podtytul`, `podtytul_en`)**: decyzja 18.11 (lista 1a) mówi „podłączyć `podtytul_en`”. Okazało się, że nowy nagłówek kierunku nie pokazuje nadtytułu ani po polsku, ani po angielsku (strona używa polskiego tylko do policzenia stopni studiów na stronie „Studia”). Podłączenie samego EN dałoby nadtytuł tylko na stronach angielskich. Nie podłączałem; pola mają opis „Na stronie się nie wyświetla”. Co wybierasz: pokazać nadtytuł nad nazwą kierunku w obu językach (zmiana wyglądu 4 stron kierunków PL i EN), czy zostawić tak, jak jest?
2. **Hasło na Stronach Studiów bez liczb** (9 stron ma wpisane hasło, którego dziś nie widać, np. Pierwszy rok, Sprawy studenckie, Rekrutacja do szkoły doktorskiej): pokazywać hasło także bez liczb (jak na listach Aktualności i Kalendarza; zmiana wyglądu tych 9 stron PL i EN), czy zostawić tak, jak jest (opis w formularzu)?

## Push Web-Core
- **`1ab56e50..3e81655e`** (15:40): skrypt formularzy Studiów i Popularyzacji, `--pomin` dla pól w listach. Przed pushem `fetch` (bez nowych commitów na `main`), budowa OK, `astro check`: 0 błędów, 0 ostrzeżeń. Podgląd zielony: run 44326729373 zbudował `3e81655e`.
- **`3e81655e..add78d45`** (15:44): poprawka opisów hasła i opisu Stron (Studia, Popularyzacja) po sprawdzeniu, gdzie strona je pokazuje. Przed pushem `fetch` i rebase, budowa OK, `astro check`: 0 błędów, 0 ostrzeżeń. Podgląd zielony: run 44327594862 zbudował `add78d45`.
- Oba commity zmieniają tylko skrypty: wygląd strony bez zmian.
- Commity treści poprawione przed pushem (`--amend` na lokalnej gałęzi roboczej, nic nie było wypchnięte): Web-Studia `0217209`, Web-Popularyzacja `2795ca8`.

## Dokumentacja zlecenia 40 („Na koniec”)
- **Web-Core `add78d45..910853ea`** (15:52; przed pushem `fetch`, rebase bez nowych commitów, budowa OK; zmienia tylko `dok/`, więc Podgląd się nie przebudowuje):
  - `dok/jawny-markdown.md`: zakres formatu we wszystkich działach, stan etapów 1–7 (Aktualności: jeszcze dawny format), porządek formularzy;
  - `dok/sciagawka-edytora.md`: przepisana pierwsza część — jawny Markdown zamiast dawnego rozpoznawania układów; ściągawki z opisów pola Treść (Strony i wpisy); przykłady bloków; strony z listą, `{#sukcesy}`, `{#czasopisma}`, karty „Dla kogo”; szablony nowych wpisów; pola, których strona nie pokazuje. W „Gdzie co jest” poprawione nieaktualne wiersze (specjalności są w Web-Studia, nie w Web-Spec-*; ścieżka listy kierunków w Ustawieniach; nowe wiersze: strony ze stopki, nagłówki działów, Facebook i YouTube);
  - `dok/dla-redaktorow/mapa-cms.html` (źródło PDF): strona 2 — tabela bloków jawnego Markdownu zamiast „Układów, które strona rozpoznaje sama”; dodawanie pliku linkiem Markdown (pole Treść nie ma przycisku linku); baner kierunku bez nadtytułu; poprawiona ścieżka „Przypomnień o terminach”. PDF: 2 strony, treść mieści się na kartkach.
- **PDF w Web-Podglad** (`dla-redaktorow/Mapa-CMS-IM-UWr.pdf`): **wypchnięty o 17:17, `6abb1bb..da76859`** (`[skip ci]`), po pushach treści; skrypt `push40_pdf.sh` sprawdził, że treści etapów 1, 2, 4, 6 i 7 są na `main`, a PDF ma 2 strony. Przed pushem przewinięcie na nowy commit drugiej sesji w Web-Podglad (`6abb1bb`, zlecenie 43, etap 2).
- **Po etapie 3 (Aktualności)** trzeba jeszcze: w obu dokumentach i w PDF usunąć zdanie o dawnym formacie Stron Aktualności.

## Push treści (18.11, 17:11–17:14, przed wieczorem na Twoje polecenie: „Dobra, zgadzam sie wrażamy teraz”)
- **Poprawka przed pushem (Web-Core `910853ea..b43b0aa8`, 16:52):** zlecenie 33 dodało pole „Opublikowane” do formularzy Popularyzacji, a skrypt etapu 7 ustala pełną kolejność pól i przy innym zestawie pól się zatrzymuje. Teraz „Opublikowane” staje pod tytułem i tytułem EN (jak w Instytucie i Nauce), gdy formularz je ma. Sprawdzone na stanie po 33: wynik = sprawdzony formularz etapu 7 + pola „Opublikowane”; drugie uruchomienie bez zmian. Wieczorem byłby to STOP Popularyzacji (bez szkody, ale bez pushu).
- **Pierwsze uruchomienie (17:10): STOP w obu repozytoriach, nic nie wypchnięte.** `main` przesunęło się o commity zlecenia 33, więc skrypt zrobił formularze od nowa na świeżym `main` (Studia `a8964db`, Popularyzacja `0993e8e`). Kontrola zapisów miała jednak bazę sprzed 33 i uznała mój commit 33 (zmiana `.pages.yml`) za zapis redaktora („zmiana konfiguracji — sprawdź ręcznie”); wszystkie pliki danych: OK. To błąd w moim skrypcie, nie zapis redaktora.
- **Poprawka skryptu:** baza kontroli = commit zlecenia 33 na `main` (jak w skryptach 40.1, 40.2, 40.4). Zapisy redaktorów sprzed niego sprawdziła kontrola zlecenia 33 o 16:49: 0 od `b2a7c09` i od `0f76f88`.
- Przed drugim uruchomieniem sprawdziłem nowe commity: `.pages.yml` i 4 pliki kierunków identyczne z wynikiem testu na stanie po 33; zmiany danych etapu 7 identyczne z wcześniej sprawdzonymi.
- **Drugie uruchomienie (17:11–17:14):**
  - Web-Studia: baza `f31a027`, 0 zapisów od bazy; `sprawdz-jawny-markdown` OK (27 wpisów, 420 nagłówków); porównanie HTML: **0 różnic** w 925 plikach; **wypchnięte `f31a027..a8964db`**; kontrola po: „OK, tylko zmiany z migracji”;
  - Web-Popularyzacja: baza `72e08cd`, 0 zapisów od bazy; `sprawdz-jawny-markdown` OK (5 wpisów, 40 nagłówków); dane bez zmian; **wypchnięte `72e08cd..0993e8e`**; kontrola po: OK.
- Podgląd: **zielony** — przebieg 44344905430 zbudował stronę z `a8964db` i `0993e8e`.

## Następnego dnia (19.11)
- **Test w CMS (Studia → Kierunki):** otwarcie formularza (pola EN pod polskimi, w liczbach brak „Krótszy podpis”); zapis bez zmian: diff pusty.
- **Test w CMS (Popularyzacja → Strony):** otwarcie (Treść na górze), zapis bez zmian: diff pusty.
- **Przegląd zapisów redaktorów z 24 h po pushu** w obu repozytoriach.
