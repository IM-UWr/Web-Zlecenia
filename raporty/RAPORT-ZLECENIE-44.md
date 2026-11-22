# Raport: zlecenie 44, „Kariera” jako podstrona Aktualności (wariant A)

**Status:** zrobione.
- Web-Core: wypchnięte 18.11.2026 o 14:00 UTC (15:00 czasu lokalnego), w trybie samodzielnym.
- Web-Aktualnosci: wypchnięte 18.11 o 16:31 UTC (17:31 czasu lokalnego), wcześniej niż zaplanowane 20:07, na polecenie użytkownika („Te zaplanowane też możesz już zacząć robić”). Szczegóły niżej, w „Push Web-Aktualnosci”.
- **Web-Core `main`:** `91b5beb8..23050dd2`, jeden commit, zwykły push, bez force.
- **Przed pushem:**
  - `fetch` dwa razy pokazał nowe commity drugiej sesji: `0cda774c` (zlecenie 40, etap 1) i `91b5beb8` (zlecenie 40, etap 2);
  - oba rebase bez konfliktów, choć oba zmieniają `src/lib/tresci.ts`, `src/lib/tekstyStron.ts` i `src/pages/sitemap.xml.ts`;
  - przebudowa z przebazowanego drzewa i powtórzone porównanie HTML z `main` = `91b5beb8` (`raport-zrzuty/z44-html3.txt`): ten sam zestaw różnic co przed rebase;
  - `astro check` 0 błędów, 0 ostrzeżeń, 5 podpowiedzi (jak na `main`); `npm run test:jawne` 47/47; symulacja formularza 0 problemów.
- **Podgląd:**
  - przebieg [44319663976](https://github.com/IM-UWr/Web-Podglad/actions/runs/44319663976) jest zielony (1 min 29 s);
  - na żywo `/Web-Podglad/aktualnosci/kariera/` (i EN) pokazuje 11 ofert;
  - lista Aktualności ma ramkę „Oferty pracy, staży i stypendiów (11) →”;
  - teksty strony są domyślne z kodu, bo `kariera.md` nie ma jeszcze w Web-Aktualnosci.
- **Web-Aktualnosci (`.pages.yml` i nowy `src/content/strony/kariera.md`):**
  - commit `e2b51a5` w jednym commicie, na lokalnej gałęzi `praca/44-kariera` w klonie `tresci-B/Web-Aktualnosci`;
  - podstawa: `origin/main` = `e4c9c62` (fetch o 15:05; `.pages.yml` na `main` bez zmian od mojego klonu);
  - **niewypchnięty**, bo zlecenie każe pushować „wieczorem albo po wiadomości właściciela do redaktorów”;
  - push zaplanowany w tej sesji na 20:07 (przed pushami treści okna 1 o 20:41, 21:13 i 21:43). Wcześniej: fetch, kontrola zapisów redaktorów, `sprawdz_pola_cms.py`, symulacja formularza; potem Podgląd. Jeśli sesja się wcześniej zakończy, kroki są w „Do sprawdzenia jutro”;
  - kod Web-Core działa bez niego: domyślne teksty Kariery, oferty bez terminu są aktualne.
  - Zlecenie 40 (okno 1) odłożyło etap 3 (Web-Aktualnosci), bo czeka na tę zmianę `.pages.yml`. Okno pusha treści drugiej sesji: wieczorem, około 21:13.
- Zlecenie kończy się słowami „Stop: raport i czekanie na push”. Web-Core wypchnąłem według zasad trybu samodzielnego, bo wszystkie kontrole przeszły.

### Push Web-Aktualnosci (18.11, 16:31 UTC)

- **Kiedy:** wcześniej niż wieczorem. Zlecenie mówi „wieczorem albo po wiadomości właściciela do redaktorów”; użytkownik o 17:30 polecił zacząć zaplanowane zadania od razu. Zadanie o 20:07 odwołane.
- **Przed pushem:**
  - `fetch`: od podstawy `e4c9c62` doszedł jeden commit, `46d7f90` (zlecenie 33, okno 1): przełącznik „Opublikowane” w Stronach (`.pages.yml`) i jawne `opublikowany: true` w `aktualnosci.md` i `obrony-doktorskie.md`;
  - zapisów redaktorów od podstawy: brak. Ostatnie zapisy w CMS: 18.11 08:23–08:28 (nowy wpis i zdjęcie) i 17.11 21:49–23:31 (poprawki dwóch wpisów z 16.11). Żaden nie dotyka `.pages.yml`;
  - `git rebase origin/main` bez konfliktów; zmiany nie nakładają się na zlecenie 33 (inne miejsca pliku);
  - do `kariera.md` dopisane `opublikowany: true` pod tytułem. Przyjąłem tak, bo zlecenie 33 dało to pole wszystkim istniejącym Stronom, a zapis w CMS i tak by je dopisał;
  - `sprawdz_pola_cms.py ../tresci-B`: 726 plików w 16 repozytoriach, 0 problemów;
  - `formularz.mjs ../tresci-B` (kod Web-Core `5131ebf2`): 0 problemów. Scenariusz 9 (termin zgłoszeń) OK, a zapis bez zmian w nowej konfiguracji: 726 plików, 0 różnic (`raport-zrzuty/z44-push-formularz.txt`).
- **Push:** `46d7f90..422bb59`, zwykły, bez force; tuż przed nim `fetch` bez nowych commitów.
- **Po pushu:**
  - „Powiadom stronę o zmianie” 44348295078 zielony;
  - przekaźnik 44348328367 zielony;
  - Podgląd [44348385389](https://github.com/IM-UWr/Web-Podglad/actions/runs/44348385389) zielony, w logu `Web-Aktualnosci: main @ 422bb59`.
- **Na żywo:**
  - `/aktualnosci/kariera/`: tytuł „Kariera”, hasło „Praca, staże, stypendia”, opis z `kariera.md`;
  - EN: „Careers”, „Jobs, internships, scholarships”;
  - teksty w `kariera.md` są takie same jak domyślne w kodzie, więc wygląd się nie zmienił; redaktorzy mogą je teraz zmieniać w CMS;
  - lista Aktualności: ramka „Oferty pracy, staży i stypendiów (11)”.
- **Okno 1, zlecenie 40, etap 3:** może nakładać swoje zmiany `.pages.yml` na `422bb59`.

## Zmienione pliki

**Web-Core** (`23050dd2`, 18 plików):

| Plik | Zmiana |
|---|---|
| `src/lib/tresci.ts` | `pozycjeAktualnosci()`: wszystkie wpisy, z `zgloszenia`. `listaAktualnosci()` bez ofert, `listaOfert()` same oferty. `jestOferta()`, `ofertaAktualna()`: brak terminu albo termin ≥ dziś. `ZAJETE_NAZWY_AKTUALNOSCI = ['kariera']`: wpis o tej nazwie jest pomijany |
| `src/content.config.ts` | grupa `zgloszenia: [{ do_dnia }]` → pole `zgloszenia_do`, tylko przy `rodzaj: kariera`. Ostrzeżenia w logu budowy: termin przy innym rodzaju, więcej niż 1 termin, plik `kariera.md` |
| `src/lib/widoki/listaAktualnosci.ts`, `src/views/ListaAktualnosci.astro` | bez opcji „Kariera” w filtrze rodzaju. Ramka z linkiem i liczbą aktualnych ofert pod polem szukania. `?rodzaj=kariera` przekierowuje na `/aktualnosci/kariera` |
| `src/lib/widoki/listaOfert.ts`, `src/views/ListaOfert.astro` (nowe) | strona Kariera: aktualne oferty, pod nimi „Zakończone”, szukanie |
| `src/pages/aktualnosci/kariera.astro`, `src/pages/en/aktualnosci/kariera.astro` (nowe) | adresy `/aktualnosci/kariera`, `/en/aktualnosci/kariera` |
| `src/components/zal/ListaPokaz.astro` | `bezFiltra`: panel tylko z polem szukania |
| `src/scripts/zal/czytaj-dalej.ts` (nowe) | „… czytaj dalej” wspólne dla listy Aktualności i Kariery, wyjęte z `ListaAktualnosci.astro` bez zmian działania |
| `src/components/WierszAktualnosci.astro` | w ofercie z terminem dopisek „Zgłoszenia do 15.12” albo „Nabór zakończony” |
| `src/views/Aktualnosc.astro` | w ofercie link wstecz „Wszystkie oferty” → Kariera. W metryczce „Zgłoszenia do 15 grudnia 2026” albo „Nabór zakończony” |
| `src/lib/widoki/dzialStudia.ts` | „Aktualności dla studentów”: oferty tylko aktualne |
| `src/lib/tekstyStron.ts` | domyślne teksty strony Kariera, PL i EN |
| `src/pages/sitemap.xml.ts` | `/aktualnosci/kariera` i wersja EN |
| `skrypty/sprawdz_tresci.py` | `zgloszenia` w kontroli pozycji list. Ostrzeżenia: termin przy innym rodzaju, więcej niż 1 termin. Błędy: data nie w formacie RRRR-MM-DD, plik `kariera.md` |
| `skrypty/test-edytora/formularz.mjs` | scenariusz 9 (termin zgłoszeń, pięć przypadków) |
| `.gitignore` | `/src/content/strony/kariera.md` (nakładka treści, jak inne Strony) |

**Web-Aktualnosci** (`e2b51a5`, lokalnie):
- `.pages.yml`:
  - opis pola „Rodzaj”;
  - nowa grupa „Termin zgłoszeń (tylko oferty: Rodzaj „Kariera”)” (`zgloszenia`, pole `do_dnia`, `max: 1`) zaraz pod „Termin wydarzenia”;
  - opis kolekcji Strony wymienia `kariera.md`.
- `src/content/strony/kariera.md` (nowy): tytuł, opis i hasło, PL i EN.

**`.przekazanie/`:** wpis w `dziennik.md`, sekcja „Zlecenie 44” w `pola-do-cms.md`.

## Jak to działa

- **Lista Aktualności** (`/aktualnosci`, EN):
  - bez wpisów „Kariera” i bez tej opcji w filtrze „Pokaż”;
  - pod polem szukania jest ramka „Oferty pracy, staży i stypendiów (N) →” / „Jobs, internships and scholarships (N) →”. N to liczba aktualnych ofert; przy 0 ramka zostaje, ale bez liczby;
  - stary adres `?rodzaj=kariera` przekierowuje na Karierę (skrypt w nagłówku, przed narysowaniem listy);
  - `?dla=studenci` również bez ofert, spójnie z listą.
- **Kariera** (`/aktualnosci/kariera`, EN `/en/aktualnosci/kariera`):
  - baner jak Aktualności, okruszki „Aktualności › Kariera”, panel z samym polem „Szukaj w ofertach”;
  - aktualne oferty od najnowszej daty publikacji; gdy ich brak — „Obecnie brak aktualnych ofert.”;
  - pod nimi „Zakończone”, w tym samym układzie, przygaszone: szara data, etykieta i kolor wyróżnienia, zdjęcie w szarości; tekst bez przezroczystości;
  - szukanie jak w Aktualnościach (także bez polskich znaków). Puste sekcje znikają, przy braku wyników jest „Brak ofert spełniających kryteria.”;
  - od 880 px szerokości listy dwie kolumny, jak w Aktualnościach.
- **Wpis oferty:**
  - adres bez zmian;
  - link wstecz „← Wszystkie oferty” / „All offers”;
  - przy terminie w metryczce „· Zgłoszenia do 15 grudnia 2026” albo „· Nabór zakończony”;
  - baner i menu bez zmian (zlecenie 37).
- **Strona główna i RSS:**
  - strona główna bez ofert, bo bierze `listaAktualnosci()`; liczba na okładce też bez nich;
  - RSS PL i EN bez ofert;
  - „Ostatnio” na drugim ekranie (zlecenie 35) bierze wydarzenia z kalendarza, nie aktualności, więc ofert nie dotyczy.
- **Studia:** „Aktualności dla studentów” pokazują oferty bez terminu i z terminem dziś lub później.
- **Kalendarz i `.ics`:** bez zmian.
- **Pagefind:** wpisy ofert dalej mają `data-pagefind-body`, więc wyszukiwarka je znajduje.
- **Przejście do „Zakończonych”:** samo, przy codziennej przebudowie Podglądu. Termin to cały dzień: w dniu terminu oferta jest jeszcze aktualna.

## Narzędzia odbioru (lokalnie, `raport-zrzuty/z44-skrypt/`)

- `html44.py`: porównanie HTML dwóch budów, z normalizacją nazw plików `_astro` i pustych znaków. Wyniki: `raport-zrzuty/z44-html.txt` (przed rebase), `z44-html3.txt` (po rebase na `91b5beb8`).
- `zrzuty44.mjs`: zrzuty, pomiar ramki, przekierowania, szukanie i konsola (Playwright, Edge). Wynik: `raport-zrzuty/z44-zrzuty/` i `zrzuty44.json`.
- **Budowy** w `tresci-B/`:
  - `z44-przed2` — `main` = `91b5beb8`, bez `kariera.md`;
  - `z44-po3` — `23050dd2` z `kariera.md` w nakładce;
  - `z44-test` — kopia testowa z terminami, tylko lokalnie.

## Wynik odbioru

### Porównanie HTML przed/po (te same klony treści, budowy jedna po drugiej)

908 wspólnych plików, 2 nowe (`aktualnosci/kariera/`, `en/aktualnosci/kariera/`), żadnego usuniętego. Różnice:

| Pliki | Różnica |
|---|---|
| `aktualnosci/index.html`, `en/aktualnosci/index.html` | bez 11 ofert, bez opcji „Kariera”, z ramką „(11)”, skrypt przekierowania |
| `index.html`, `en/index.html` | kolumna Aktualności bez ofert (były 4 z pokazanych). Liczba na okładce bez zmian, bo dziś nowe są 2 wpisy i żaden nie jest ofertą |
| `rss.xml`, `en/rss.xml` | bez 5 ofert spośród 30 pozycji |
| `sitemap.xml` | 2 nowe adresy Kariery, nic więcej |
| 22 wpisy ofert (11 PL + 11 EN) | link wstecz „Wszystkie oferty” zamiast „Aktualności” |
| 111 plików `.ics`, `seminaria/powiadomienia.json` | tylko znacznik czasu budowy (`DTSTAMP`) |
| Kalendarz, Obrony, „Warto wiedzieć” (PL i EN) | tylko nazwy plików `_astro` i puste znaki |
| strona Studiów i wszystkie pozostałe | 0 różnic (dziś żadna oferta nie ma terminu) |

### Termin zgłoszeń (kopia testowa wpisów, nie w repozytorium; budowa `z44-test`)

Terminy ustawione testowo:
- korepetytor: 17.11 (wczoraj);
- TEB: 18.11 (dziś);
- SP-107: 15.12;
- „tutornia”, rodzaj Ogłoszenie: 15.12;
- dodatkowo wpis testowy o nazwie pliku `kariera.md`.

Wyniki:
- **Kariera:**
  - aktualnych 10, w „Zakończonych” 1 (korepetytor); ramka na liście „(10)”;
  - wiersze: „Zgłoszenia do 18.11”, „Zgłoszenia do 15.12”, „Nabór zakończony” (EN „Apply by 18 Nov”, „Closed”).
- **Wpis:** metryczka „Kariera · Opublikowano 02.07.2026 · Dla: studenci · Zgłoszenia do 15 grudnia 2026” oraz „… · Nabór zakończony”. Link wstecz `/aktualnosci/kariera`, na 1536 i 390 px.
- **Ogłoszenie z terminem:** termin pominięty; ostrzeżenie w logu budowy i w `sprawdz_tresci.py`.
- **Wpis `kariera.md`:** pominięty z ostrzeżeniem, nie ma go na liście. `/aktualnosci/kariera` dalej jest stroną ofert.
- **Studia:**
  - pierwsza budowa nic nie rozstrzygnęła: oferty nie trafiły do pierwszych pozycji;
  - druga kopia testowa z datą publikacji 18.11 dla dwóch ofert: korepetytora (po terminie) nie ma, TEB (termin dziś) jest.

### Formularz (symulacja zapisu Pages CMS, `skrypty/test-edytora/formularz.mjs`, scenariusz 9)

- **9a:** stara oferta otwarta i zapisana bez zmian: brak `zgloszenia`, pusty diff.
- **9b:** dodany pusty termin: zapis zablokowany (`zgloszenia.0.do_dnia: Invalid date`).
- **9c:** termin 15.12 zapisuje `zgloszenia:\n  - do_dnia: 2026-12-15\n    pozycja: false`.
- **9d:** w pliku dochodzi tylko ta grupa.
- **9e:** drugi termin jest zablokowany (`max: 1`).
- **„Zapis bez zmian”** dla całej treści: 726 plików, 0 różnic danych.

### Przeglądarka (Edge, budowa po; `zrzuty44.json`)

- **Ramka pod polem szukania:**
  - 1536×864: x=1152, y=577, 236×59 px;
  - 1920×1080: x=1344, 236×59 px;
  - 390×844: pełna szerokość, 358×45 px.
  - Ramka ma `var(--line-ui)`, po najechaniu kolor wyróżnienia. Jasny i ciemny tryb czytelne.
- **Przekierowanie:** `/aktualnosci?rodzaj=kariera` → `/aktualnosci/kariera/`, EN tak samo.
- **Szukanie na Karierze:**
  - 11 → „korepetytor” 1, „stazE” 1;
  - „xyzxyz” 0, z komunikatem „Brak ofert spełniających kryteria.”;
  - po wyczyszczeniu z powrotem 11.
- **Konsola:** bez błędów.

### Zrzuty (`raport-zrzuty/z44-zrzuty/`)

- **Lista Aktualności z ramką:**
  - `lista-1536x864-{jasny,ciemny}-po.png`, `lista-1920x1080-{jasny,ciemny}-po.png`, `lista-390x844-{jasny,ciemny}-po.png`;
  - przed: `lista-*-jasny-przed.png`.
- **Kariera:** `kariera-{1536x864,390x844}-{jasny,ciemny}.png`, `kariera-en-…`. Budowa testowa: aktualne z terminem i bez, „Zakończone”.
- **Wpis oferty:** z terminem `wpis-termin-…`, po terminie `wpis-zakonczona-…` (1536 i 390, jasny i ciemny).
- **Szukanie bez wyników:** `kariera-szukanie-brak.png`.

### Kontrole

| Kontrola | Wynik |
|---|---|
| `npm run build` | OK; jedyne ostrzeżenia jak na `main` (brak katalogów `kierunki-baner`, `specjalnosci-baner` w nakładce) |
| `astro check` | 0 błędów, 0 ostrzeżeń, 5 podpowiedzi (jak na `main`) |
| `npm run test:jawne` | 47/47 |
| `skrypty/sprawdz_tresci.py` | OK (567 plików, 106 ciekawostek). Na kopii testowej oczekiwane ostrzeżenia i błędy |
| `skrypty/sprawdz_pola_cms.py ../tresci-B` | 0 problemów (726 plików, z nowym `.pages.yml`) |
| `formularz.mjs ../tresci-B` | 0 problemów |
| konsola przeglądarki | czysta |

## Odstępstwa od zlecenia i powody

- **Opis grupy terminu:** dopisałem „(kliknij „Add an item”)”, a do etykiety „(tylko oferty: Rodzaj „Kariera”)”. Powód: grupa stoi w formularzu każdego wpisu, a przycisk w Pages CMS jest po angielsku. Tak samo opisany jest „Termin wydarzenia” (zlecenie 31).
- **Dopisek terminu także w wierszach** Kariery i Studiów („Zgłoszenia do 15.12”, krótko, bo w wierszu mało miejsca), nie tylko we wpisie. Powód: bez tego na liście nie widać, która oferta wkrótce się kończy.
- **`sprawdz_tresci.py`, dwa błędy (nie ostrzeżenia):**
  - zła data terminu;
  - plik wpisu `kariera.md`.

  Budowa w obu przypadkach tylko ostrzega i pomija. Powód: oba to pomyłki, których redaktor nie zobaczy na stronie. Termin przy innym rodzaju jest ostrzeżeniem, jak w zleceniu.
- **Przekierowanie `?rodzaj=kariera` to skrypt na stronie**, nie przekierowanie serwera, bo strona jest statyczna (GitHub Pages). Bez JS lista pokazuje się bez filtra, a ramka prowadzi na Karierę.

## Decyzje podjęte samodzielnie (wartości domyślne zlecenia)

- **Hasło:** przyjąłem „Praca, staże, stypendia” / „Jobs, internships, scholarships”, bo zlecenie dało tytuł i opis, a hasła nie. Redaktor zmieni je w Strony → Kariera.
- **Bez wyróżnionego pierwszego wiersza** na Karierze, bo to lista ofert, nie zapowiedzi.
- **„Zakończone” przygaszone kolorem** (szare), nie przezroczystością, bo tekst ma zostać czytelny (kontrast).
- **Nawigacja „nowszy/starszy” we wpisach bez zmian.** We wpisie oferty prowadzi też do zwykłych aktualności i odwrotnie. Przyjąłem tak, bo zlecenie o niej nie mówi.
- **Strony zakładów bez zmian**, bo zlecenie ich nie wymienia (oferty nie mają przypisanego zakładu).
- **Plik strony nazwany `kariera.md`**, jak w zleceniu. Adres to `/aktualnosci/kariera`, czyli wyjątek od reguły „adres = ścieżka pliku”, opisany w opisie kolekcji Strony.
- **Push Web-Aktualnosci wieczorem** według zlecenia (nie od razu po Web-Core), bo kod nie potrzebuje go do działania. Ostatecznie o 17:31, na polecenie użytkownika.
- **`opublikowany: true` w `kariera.md`** (dopisane po rebase na zlecenie 33), bo tak mają wszystkie inne Strony.

## Pytania do użytkownika

1. Nazwa pliku `kariera.md` (adres `/aktualnosci/kariera`) zostaje? Ewentualnie `aktualnosci-kariera.md` albo podkatalog `aktualnosci/kariera.md`.
2. Hasło „Praca, staże, stypendia” zostaje?
3. Nawigacja „nowszy/starszy” we wpisie oferty: zostawić po wszystkich wpisach czy ograniczyć do ofert (a w zwykłym wpisie pomijać oferty)?
4. ~~Czy wysłać redaktorom wiadomość przed pushem Web-Aktualnosci?~~ Push już jest (16:31 UTC). **Rozstrzygnięte (18.11):** użytkownik sam powie redaktorom o nowej grupie „Termin zgłoszeń”, o stronie Kariera w Stronach i o tym, że oferty nie są już na liście Aktualności. README bez zmian.

## Do sprawdzenia jutro

- ~~Jeśli push Web-Aktualnosci o 20:07 się nie odbył~~ — odbył się o 16:31 UTC (`422bb59`).
- **Web-Aktualnosci po pushu:**
  - przegląd zapisów redaktorów z 24 godzin: czy nikt starym formularzem nie usunął grupy `zgloszenia` i czy zapisy ofert mają poprawny format;
  - `sprawdz_pola_cms.py` i `sprawdz_tresci.py` na świeżym klonie.
- **Podgląd:**
  - strona Kariera z tekstami z `kariera.md`;
  - pierwszy termin wpisany przez redaktora: dopisek w wierszu i metryczce, licznik w ramce;
  - po terminie oferta w „Zakończonych” po nocnej przebudowie.
- **Zlecenie 40, etap 3 (Web-Aktualnosci):** nakłada swoje zmiany `.pages.yml` na wersję z grupą `zgloszenia` (nie na starszą).
