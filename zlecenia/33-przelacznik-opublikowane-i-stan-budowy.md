# Zlecenie 33: przełącznik „Opublikowane” bez odmrażania starej strony i stan budowy na żywo na Podglądzie (17.11.2026)

**Decyzje właściciela (17.11, 21:47–22:51):**
- **Przełącznik „Opublikowane” ma być już teraz.** Stara strona (Core) zostaje przy tym zamrożona. Nową publiczną stronę włączymy, gdy będzie gotowa.
- **Stan budowy na Podglądzie.** Redaktorzy mają widzieć na żywo (z GitHub Actions), czy strona się buduje, czy jest zbudowana i kiedy była ostatnia budowa. Forma: dyskretnie, gdy wszystko jest w porządku, a głośno, gdy trzeba coś zrobić („zajebiste”).
- **22:51: nowe strony domyślnie jako opublikowane** (`default: true`). Szkic to świadomy wybór redaktora: odznacza „Opublikowane”.
- **18.11, 11:29 (dopisane w trakcie kolejki):**
  - plakietkę stanu budowy da się przeciągnąć; po puszczeniu wskakuje w najbliższy róg, który przeglądarka zapamiętuje (B3);
  - na podstronie, której nie będzie na stronie publicznej, plakietka mówi to wprost i prowadzi do przełącznika w CMS (B4).
  - Jeśli część B jest już zrobiona, dołóż B3 i B4 osobnym commitem.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- **Repozytoria treści:**
  - redaktorzy edytują na żywo, więc zawsze od świeżego `main`, zwykły commit, bez force-push;
  - `.pages.yml` i dane jednego repozytorium w jednym commicie (kolejka, punkt 3);
  - do tego sekcja „Ochrona zmian redaktorów” niżej.
- Zmiana w `IM-UWr/Web-Podglad` (workflow) też tylko po „push”.
- Raport `RAPORT-ZLECENIE-33.md`, zrzuty `raport-zrzuty/z33-*`. Bez subagentów.

## Ochrona zmian redaktorów (obowiązkowo przy każdym pushu do repozytorium treści)
Redaktorzy zapisują w CMS na żywo, także w trakcie tego zlecenia. Ich zmiany nie mogą zginąć.

1. **Migracja na najświeższej wersji.**
   - Tuż przed pushem: `git fetch` i sprawdź, czy na `main` przybyły zapisy redaktorów od chwili, gdy zacząłeś (`git log <baza>..origin/main`). Baza = HEAD zanotowany na początku pracy.
   - Jeśli przybyły, nie doklejaj starego wyniku. Przełącz się na świeży `main` i **uruchom skrypt migracji jeszcze raz** na aktualnych plikach.
   - Konflikty rozwiązuj ręcznie: weź wersję redaktora i nanieś na nią swoją zmianę. Nigdy odwrotnie i nigdy hurtem całych plików (`-X ours`, `checkout --ours/--theirs`).
2. **Kontrola przed pushem** (skrypt, wynik w raporcie):
   - weź każdy zapis redaktora od bazy (autor inny niż Code) i każdy plik, który zmienił;
   - porównaj pole po polu jego wersję z wersją, którą wypychasz;
   - każda wartość wpisana przez redaktora musi być w wyniku. Inaczej **STOP**.
3. **Kontrola po pushu:** porównanie pole po polu całego repozytorium przed i po. Różnice tylko w polach zmienianych celowo (tu: `opublikowany`, etykieta i opis w `.pages.yml`); lista w raporcie.
4. **Okno pusha:** wieczorem albo po wiadomości od właściciela do redaktorów: „zapiszcie i zamknijcie CMS na 15 minut, potem odświeżcie stronę”.
   - Pages CMS przy zapisie sprawdza wersję pliku. Jeśli plik zmienił się od otwarcia formularza, zapis jest odrzucony („File has changed since you last loaded it”) i nic nie zostaje nadpisane. Redaktor traci jednak to, co wpisał, a nie zapisał.
   - Formularz otwarty przed pushem i zapisany po nim działa jeszcze według starej konfiguracji. **Następnego dnia** przejrzyj zapisy redaktorów z 24 godzin po pushu: czy żaden nie usunął nowych pól ani nie przywrócił starych. Znalezione popraw osobnym commitem.
5. **Wszystko da się odwrócić:** każdy zapis redaktora to osobny commit. W razie straty przywróć wartość z historii **nowym commitem** (nigdy `reset` ani force-push) i opisz to w raporcie.

## Część A. Przełącznik „Opublikowane”

### A1. Stan dziś
- **Schemat:** `published = z.preprocess(v => v == null || v === '' ? true : v, z.boolean())` w `src/content.config.ts` (linia 26). Brak pola oznacza „opublikowane”.
- **Żółty pasek:** strona z `opublikowany: false` dostaje na górze pasek „Podgląd — ta strona nie jest jeszcze opublikowana” (`src/layouts/Baza.astro`, ok. linii 139).
- **Wiele miejsc ukrywa nieopublikowane wpisy także na Podglądzie** (`opublikowany !== false`), a Podgląd ma pokazywać wszystko:
  - `src/lib/tresci.ts:17` (`opublikowane`);
  - `src/lib/tekstyStron.ts:155`, `src/lib/kierunki.ts:27`;
  - `src/lib/widoki/dzialStudia.ts:26`, `popularyzacja.ts:63`, `pracownicy.ts:13`, `kierunek.ts:24`, `listaWartoWiedziec.ts:9`;
  - `src/components/WartoWiedziec.astro:33`;
  - `src/pages/sitemap.xml.ts:19–26`.
- **Formularze:** przełącznik jest tylko w Web-Studia, w kolekcjach `kierunki`, `specjalnosci` i `strony`, z mylącą etykietą „Uwzględniaj w zestawieniach” i `default: true`.
- **Core:** workflow „Budowanie i publikacja strony” (`deploy.yml`) jest wyłączony od 7.11 i **zostaje wyłączony**.

### A2. Docelowo
1. **Jedna funkcja widoczności.** Wszystkie filtry z A1 korzystają z jednej funkcji, np. `widoczny(wpis)` w `src/lib/tresci.ts`:
   - **domyślnie (Podgląd):** pokazuje wszystko;
   - **przy budowie z flagą `TYLKO_OPUBLIKOWANE=1`** (przyszła strona publiczna): tylko `opublikowany !== false`. Dotyczy to stron, list, menu, kafelków, liczb w banerach, mapy strony (`sitemap.xml`), wyszukiwarki (Pagefind) i plików `.ics`.
   - Flagi nigdzie dziś nie ustawiaj, bo Core zostaje zamrożony. Sprawdź ją tylko lokalnie: przy budowie z flagą nieopublikowane strony znikają, a razem z nimi linki do nich.
2. **Oznaczenie szkicu na Podglądzie.**
   - Strona: żółty pasek jak dziś, a do tego żółty wiersz na plakietce (B4).
   - Listy, kafelki i menu: mała etykieta „szkic” / „draft” przy nieopublikowanej pozycji, żeby redaktor wiedział, co nie trafi na stronę publiczną. Dyskretnie, w stylu plakietki z części B (B2).
3. **Formularze.** Pole `opublikowany` (boolean) w kolekcjach:
   - `kierunki` i `specjalnosci` (Web-Studia);
   - **„Strony”** we wszystkich repozytoriach, które je mają;
   - **„Strona działu …”** (Web-Instytut, Web-Nauka, Web-Studia, Web-Popularyzacja).

   Ustawienia pola:
   - etykieta: **„Opublikowane — widoczne na stronie publicznej (na Podglądzie widać zawsze)”**; pole stoi zaraz pod tytułem;
   - opis: „Odznacz, żeby przygotować stronę bez pokazywania jej na stronie publicznej (szkic)”;
   - **`default: true`** (decyzja 22:51): nowe strony są od razu opublikowane.

   **Bez przełącznika:** seminaria, referaty, aktualności, pracownicy, zakłady i „Warto wiedzieć” (lista do raportu). Zakłady i „Warto wiedzieć” mają to pole w schemacie, więc zapytaj o nie właściciela.
4. **Istniejące wpisy: jawna wartość.**
   - Przy `default: true` otwarcie starej strony bez tego pola wstawi `true`, czyli to, co już dziś obowiązuje (brak pola = opublikowane). Nic się więc po cichu nie ukryje.
   - Mimo to ujednolić dane: jednym commitem w każdym repozytorium dopisz `opublikowany: true` do wszystkich istniejących wpisów tych kolekcji, które nie mają pola. Istniejących wartości (także `false`) nie ruszaj.
   - Ten commit dotyka wielu plików redaktorów, więc obowiązuje sekcja „Ochrona zmian redaktorów”, zwłaszcza punkt 1: dopisanie uruchom ponownie na świeżym `main` tuż przed pushem.
   - Kontrola: każdy plik tych kolekcji ma jawne `opublikowany`.
5. **Ściągawka** (`dok/sciagawka-edytora.md`), krótka reguła: „Nowa strona jest od razu opublikowana. Żeby przygotować ją po cichu, odznacz »Opublikowane«: wtedy widać ją tylko na Podglądzie, z żółtym paskiem i etykietą »szkic«”.

## Część B. Stan budowy na żywo (tylko Podgląd)

### B1. Skąd dane
- **API GitHuba.** Budowę Podglądu robi workflow `podglad.yml` w publicznym repozytorium `IM-UWr/Web-Podglad`. Przeglądarka może pytać API GitHuba bez logowania (CORS jest dozwolony):
  - `GET https://api.github.com/repos/IM-UWr/Web-Podglad/actions/workflows/podglad.yml/runs?per_page=5`;
  - pola: `status` (`queued` / `in_progress` / `completed`), `conclusion` (`success` / `failure` / `cancelled`), `run_started_at`, `updated_at`, `html_url`, `id`.
- **Limit zapytań.** Bez logowania to około 60 zapytań na godzinę na adres IP, a cała sieć uniwersytecka może wychodzić z jednego adresu. Dlatego:
  - zapytania warunkowe z `If-None-Match` (ETag), bo odpowiedź 304 nie liczy się do limitu;
  - pytanie przy wejściu na stronę, potem co **120 s**, a co **20 s** tylko w trakcie budowy;
  - pauza, gdy karta jest w tle;
  - wynik trzymany w `sessionStorage` przez 30 s, żeby przejście między podstronami nie pytało od nowa;
  - przy błędzie 403 lub 429 plakietka pokazuje „Stan budowy chwilowo niedostępny” i wraca do odpytywania po 10 min.
- **Dane wpisane przy budowie.** `podglad.yml` ustawia przy budowie zmienne `PODGLAD=1`, `PODGLAD_RUN_ID=${{ github.run_id }}` i czas startu. Strona zna więc swoją wersję. Jeśli najnowsza udana budowa w API ma inne `id`, gotowa jest nowsza wersja.
- **Komunikat błędu.**
  - W `podglad.yml` budowa zapisuje swoje wyjście do pliku. Przy porażce krótki skrypt wyciąga z niego błędy treści Astro (np. `InvalidContentEntryDataError`: kolekcja, wpis, pole, komunikat) i wypisuje je jako adnotacje `::error title=…::…`.
  - Plakietka czyta je przez `GET /repos/IM-UWr/Web-Podglad/actions/runs/{id}/jobs` i `GET /repos/IM-UWr/Web-Podglad/check-runs/{job_id}/annotations`. Sprawdź, czy dla publicznego repozytorium działa to bez logowania; jeśli nie, pokaż tylko link „Szczegóły”.
  - Typowe komunikaty przetłumacz na polski (np. `Required` → „brak wymaganego pola”).
  - Dodaj link **„Popraw w CMS”** w formacie `https://app.pagescms.org/im-uwr/<repozytorium małymi literami>/main/collection/<kolekcja>/edit/<ścieżka pliku zakodowana w URL>`. Przykład: `…/web-aktualnosci/main/collection/aktualnosci/edit/src%2Fcontent%2Faktualnosci%2F2026-11-16--2.md`. Kolekcję i repozytorium weź z `tresci.json` i mapowania w `skrypty/pobierz_tresci.py`.

### B2. Wygląd (decyzja: dyskretnie, a głośno, gdy trzeba działać)
- **Wszystko w porządku:** mała plakietka, domyślnie w lewym dolnym rogu (da się ją przenieść, B3): „● Aktualna · zbudowana 17.11, 21:12” (EN: „● Up to date · built 17 Nov, 21:12”).
  - Nie zasłania treści ani przycisków; na telefonie jest mniejsza, nad dolną krawędzią.
  - Po kliknięciu rozwija szczegóły: ostatnie 3 budowy z godzinami i link do GitHub Actions.
- **Budowa w toku:** plakietka się rozwija: „◐ Przebudowa… zmiany będą widoczne za ok. 4 min”.
  - Czas szacuj z mediany ostatnich 5 udanych budów; do tego cienki pasek postępu.
  - Kolejka (`queued`) dostaje osobny napis.
- **Nowa wersja gotowa przy otwartej stronie:** dymek „Nowa wersja strony gotowa — Odśwież”; przycisk przeładowuje stronę.
- **Budowa nieudana:** czerwony pasek na górze, pod paskiem menu, `role="alert"`:
  - treść: „Strona się nie zbudowała, pokazujemy wersję z 17.11, 21:12”;
  - komunikat błędu po polsku z nazwą wpisu, „Popraw w CMS” i „Szczegóły”;
  - pasek da się zwinąć do czerwonej plakietki, ale wraca na każdej podstronie, dopóki kolejna budowa się nie uda.
- **Dostępność i tryby:** `role="status"` z `aria-live="polite"` dla zmian stanu; wszystko dostępne z klawiatury; zgodne z trybem ciemnym; przy `prefers-reduced-motion` bez animacji.
- **Tylko na Podglądzie:** element renderuje się tylko przy `PODGLAD=1`. Na przyszłej stronie publicznej i w Core go nie ma.

### B3. Przeciąganie plakietki (decyzja 18.11, 11:29: przyciąganie do rogu)
- **Przeciąganie myszą lub palcem.** Po puszczeniu plakietka przesuwa się płynnie do najbliższego rogu okna (liczy się środek plakietki). Przy `prefers-reduced-motion` przeskakuje bez animacji.
- **Rogi:**
  - komputer: cztery rogi; górne pod paskiem menu (nie na nim), z tym samym odstępem od krawędzi co dolne;
  - telefon: tylko dwa dolne rogi, bo u góry jest nagłówek z menu.
- **Kliknięcie a przeciąganie:**
  - przeciąganie zaczyna się dopiero po przesunięciu wskaźnika o ok. 6 px;
  - krótsze przesunięcie to zwykłe kliknięcie: rozwija szczegóły jak dotąd;
  - po przeciągnięciu kliknięcie się nie wywołuje.
- **Pamięć:**
  - wybrany róg w `localStorage` (np. `im-plakietka-rog`), więc plakietka stoi w tym samym rogu na każdej podstronie i po odświeżeniu;
  - odczyt i zapis w `try/catch`; bez pamięci domyślny lewy dolny róg.
- **Kierunek rozwijania:** szczegóły, dymek „Nowa wersja…” i wiersz szkicu (B4) otwierają się w stronę środka ekranu (z dolnego rogu w górę, z prawego w lewo), żeby nie wychodziły poza okno.
- **Klawiatura i czytniki:**
  - w rozwiniętych szczegółach przycisk „Przenieś do innego rogu” (EN „Move to another corner”), który przechodzi po rogach po kolei;
  - uchwyt ma `aria-label`.
- **Czerwony pasek błędu** zostaje na górze i się nie przesuwa.
- **Technicznie:**
  - Pointer Events (`pointerdown` / `pointermove` / `pointerup`, `setPointerCapture`);
  - `touch-action: none` tylko na plakietce, żeby przewijanie strony działało jak dotąd;
  - pozycja przez atrybut rogu (np. `data-rog="ld"`) i zmienne CSS, bez nasłuchiwania przewijania.

### B4. Strona tylko na Podglądzie (decyzja 18.11, 11:29)
- **Kiedy:** otwarta podstrona nie powstałaby w budowie publicznej (`TYLKO_OPUBLIKOWANE=1`).
  - Decyduje ta sama funkcja `widoczny()` co w budowie publicznej (A2.1), a nie osobny warunek. Informacja pojawi się więc także na stronach ukrytych pośrednio, np. na podstronie szkicu.
  - W raporcie wypisz, jakie przypadki ukrycia pośredniego istnieją.
  - Na stronach opublikowanych wiersza nie ma.
- **Co widać:** dodatkowy żółty wiersz na plakietce, także zwiniętej:
  - PL: „Szkic: tej strony nie będzie na stronie publicznej. Włącz »Opublikowane« w CMS →”;
  - EN: „Draft: this page won't be on the public site. Turn on "Published" in the CMS →”.
- **Link:**
  - prowadzi do formularza tej strony w Pages CMS, w tym samym formacie adresu co „Popraw w CMS” (B1); repozytorium, kolekcję i ścieżkę pliku wpisz przy budowie;
  - przy ukryciu pośrednim link prowadzi do wpisu, który ma wyłączony przełącznik;
  - gdy adresu nie da się ustalić, sam tekst bez linku.
- **Żółty pasek na górze strony (A2.2) zostaje.** Plakietka go nie zastępuje.

## Odbiór lokalny
- **Część A:**
  - porównanie wszystkich stron przed i po na Podglądzie (bez flagi): bez różnic, poza etykietą „szkic” przy wpisie testowym ustawionym na szkic;
  - budowa z `TYLKO_OPUBLIKOWANE=1`: wpis testowy znika ze strony, list, menu, mapy strony i wyszukiwarki;
  - symulacja zapisu w CMS (jak w zleceniu 28, etap 6a): stara strona otwarta i zapisana bez zmian zostaje opublikowana; nowa startuje jako opublikowana; po odznaczeniu staje się szkicem.
- **Część B:**
  - test na prawdziwym API (strona lokalna z `PODGLAD=1`) we wszystkich stanach. Stany „w toku” i „błąd” zasymuluj odpowiedziami zapisanymi w pliku (tryb testowy `?stan=w-toku` / `?stan=blad`, tylko lokalnie);
  - zrzuty plakietki, rozwinięcia, dymka i czerwonego paska na komputerze i telefonie, w trybie jasnym i ciemnym;
  - pomiar: strona otwarta przez 10 min bez budowy wysyła najwyżej 5 zapytań z odpowiedzią 200;
  - B3: przeciągnięcie do każdego rogu (komputer 4, telefon 2); róg zapamiętany po przejściu na inną podstronę i po odświeżeniu; kliknięcie bez przesunięcia rozwija szczegóły; „Przenieś do innego rogu” działa z klawiatury; zrzuty rozwiniętej plakietki w każdym rogu;
  - B4: wpis testowy ustawiony na szkic pokazuje żółty wiersz z działającym linkiem do swojego formularza w CMS; opublikowana strona nie ma tego wiersza.
- **Kontrole:** `astro check` bez nowych błędów, konsola czysta.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Przełącznik „Opublikowane” jest w kierunkach, specjalnościach, „Stronach” i stronach działów, z jasną etykietą.
- [ ] Nowe strony domyślnie są opublikowane; istniejące mają jawne `opublikowany: true` i żadna nie zmieniła się w szkic.
- [ ] Podgląd pokazuje wszystko i oznacza szkice.
- [ ] Flaga `TYLKO_OPUBLIKOWANE` ukrywa szkice wszędzie; Core nadal zamrożony.
- [ ] Na Podglądzie widać stan budowy na żywo:
  - dyskretna plakietka;
  - rozwinięcie przy budowie;
  - dymek po nowej wersji;
  - czerwony pasek przy błędzie, z polskim komunikatem i linkiem do CMS (albo samym „Szczegóły”, jeśli adnotacje nie są dostępne).
- [ ] Zapytania do API są oszczędne (ETag, 120 s / 20 s, pauza w tle), a limit jest obsłużony.
- [ ] Plakietkę da się przeciągnąć; wskakuje w najbliższy róg (komputer 4, telefon 2 dolne) i zostaje tam na kolejnych podstronach; kliknięcie dalej rozwija szczegóły.
- [ ] Na stronie, której nie będzie na stronie publicznej, plakietka mówi to wprost i linkuje do przełącznika w CMS.
- [ ] Nic z części B nie trafia do Core ani na stronę publiczną.
- [ ] Kontrola zmian redaktorów przed i po pushu w raporcie: wszystkie zapisy redaktorów zachowane. Przegląd z następnego dnia zrobiony.
