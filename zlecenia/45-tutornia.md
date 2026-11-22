# Zlecenie 45: Tutornia — podstrona Studiów z grafikiem z CMS, ramką „Teraz” i kafelkiem w Szybkim dostępie (18.11.2026)

**Decyzje właściciela (18.11):**
- **14:55:** tutornia ma mieć własną podstronę w Studiach, w grupie „Na co dzień”, oraz link w Szybkim dostępie jako 5. pozycję, po Seminariach. Na stronie: hasło (kolor Studiów), liczby i ładny grafik edytowany w CMS. Dziś grafik to obrazek przy aktualności „Rusza tutornia”.
- **16:49:** prototyp przyjęty („Zajebiste, daj na zlecenie”). Prototyp: https://claude.ai/artifact/B3eSc2U4kVPvygSYzJRubk (wersja z 16:55). Źródła prototypu: `.przekazanie\prototypy\45-tutornia\` (opis plików na końcu zlecenia).
- **16:51:** przygaszone mają być **wszystkie dyżury z bieżącego tygodnia, które już się odbyły, aż do obecnej godziny**, a nie tylko dzisiejsze.
- **18:15:** CMS Tutorni ma być zgodny z tym, co ustaliliśmy w zleceniu 40 (wzór Studiów): komentarze w treści według wzoru, tylko potrzebne pola. Treść w załączniku A poprawiona do standardowych komentarzy.
- **18:33:** zakres osi godzin ustawia się sam z grafiku, a w długich lukach oś dostaje pełne godziny (punkt 2, „Oś godzin”).
- **Decyzje domyślne** (pytania z 15:16 bez odpowiedzi; zmiana na prośbę właściciela):
  - hasło „Przyjdź z zadaniem, które nie wychodzi” / EN „Bring the problem you're stuck on”;
  - liczby: tutorzy · dyżury w tygodniu · sala;
  - tutornia działa tylko w dni zajęć z Roku akademickiego; w dzień zamiany dni obowiązują dyżury dnia, według którego planu są zajęcia (18.12.2026 = środa);
  - Szybki dostęp: od 1500 px nagłówek w jednym rzędzie z pięcioma kafelkami, 1024–1499 px nagłówek nad kafelkami;
  - ciekawostka „Seminarium w salonie” przypięta do Tutorni, ale zostaje ukryta (`ukryta: true`, źródłem jest wywiad i czeka na zgodę), więc do czasu jej odkrycia strona losuje ciekawostkę jak inne podstrony.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela. Raport `RAPORT-ZLECENIE-45.md`, zrzuty `raport-zrzuty/z45-*`. Bez subagentów.
- **Kolejność:** okno 2, po zleceniu 43. Korzysta z gotowych 33 (`widoczny()`, przełącznik „Opublikowane”), 35 (Szybki dostęp bez dziur: rachunek miejsca) i 40 (jawny Markdown, ściągawka).
- **Repozytoria treści:** Web-Studia (nowy plik strony, linki w dwóch stronach, opisy pól „Treść” w `.pages.yml`, pole `adres` w „W skrócie”) i Web-Ustawienia (`nawigacja.json`, `skroty.json`). Zasady „Ochrona zmian redaktorów” jak w zleceniach 31 i 40:
  - zawsze od świeżego `main`, zwykły commit, bez force-push;
  - tuż przed pushem `git fetch`; jeśli plik się zmienił, nanieś swoją zmianę na nową wersję;
  - push wieczorem albo po wiadomości właściciela do redaktorów; następnego dnia przegląd zapisów redaktorów z 24 godzin.
  - Kolejność pushy: najpierw Web-Core (obsługa bloków, kafelka i schematu), potem repozytoria treści. Plik `tutornia.md` z blokiem `:::grafik` bez kodu Web-Core zatrzymałby budowę („Nieznany znacznik”).

## Stan dziś (sprawdzone 18.11 na `main`)
- **Web-Core** `910853e`, **Web-Studia** `a8964db` (18.11, 17:10, po zleceniu 40, etap 7: porządek pól w formularzach Studiów), **Web-Ustawienia** `f145d85`.
- **Tutornia dziś:**
  - tylko aktualność `2026-10-17-rusza-tutornia` (Web-Aktualnosci) z obrazkiem planu `public/pliki/aktualnosci/plan_tutorni_2026_z.png`;
  - wzmianki z linkiem do tej aktualności: Web-Studia `src/content/strony/studia/pierwszy-rok.md` (PL ok. linii 378 i 598, EN w `tresc_en` ok. linii 23 i 243) oraz `sprawy-studenckie.md` (PL ok. linii 417, EN ok. linii 202);
  - „W skrócie” na stronie Studiów: `src/data/studia.md` → `o_studiach_fakty`, pozycja „Tutornia” bez linku.
- **Strony Studiów:**
  - pliki: Web-Studia `src/content/strony/studia/*.md`, kolekcja „Strony studiów” w `.pages.yml`. Pola: `tytul`, `tytul_en`, `opublikowany`, `body` (code/markdown, jawny), `tresc_en`, `format_tresci` (ukryte, `jawne`), `opis`, `opis_en`, `haslo`, `haslo_en`, `liczby`, `pasek_boczny`. **Formularz jest wspólny dla wszystkich podstron Studiów**, dlatego sala i daty grafiku idą do bloku, a nie do nowych pól;
  - render: `src/pages/[...slug].astro` → `src/views/Strona.astro` → `src/lib/widoki/strona.ts` (`daneStrony`: hasło, liczby z pola `liczby`, jawny Markdown przez `renderMarkdownZNaglowkami`).
- **Jawne bloki:**
  - `src/plugins/remark-jawne-bloki.mjs` (zbiór `BLOKI`; nieznany blok to błąd budowy);
  - `src/plugins/rehype-bloki.mjs` (`jawnaSekcja`, np. `kreski`, `linki`, `tabela`);
  - testy `jawne-bloki.test.mjs` i `rehype-bloki.test.mjs`;
  - opis dla redaktorów: `dok/jawny-markdown.md`, `dok/sciagawka-edytora.md`, `dok/zasady-parsera.md`.
- **Kalendarz zajęć:** `src/lib/kolory-dni.ts` (`infoDnia`: `kolor`, `plan` 1–5, `wolne`, `zamiana`; `semestry()`, `semestrDnia()`, `swietaPanstwowe()`) z danych Web-Studia `src/data/kolory-dni.json`. Już działa w przeglądarce (kafelek „Dziś: dzień …” w `DrugiEkran.astro`, moduł `kolory-dni` w paczce klienta).
- **Wzór ramki „Dziś”:** `src/views/RokAkademicki.astro` (`.kd-dzis`: kółko 72 px, etykieta, tytuł Brygadą, opis).
- **Szybki dostęp:**
  - `src/components/zal/DrugiEkran.astro`: `skroty.kafelki.slice(0, 4)`, specjalny kafelek dla `/studia/rok-akademicki`;
  - dane: Web-Ustawienia `src/data/skroty.json` (4 kafelki), formularz „Kafelki „Na skróty””;
  - style `.z-skr`: siatka `auto repeat(4, …)` od 1100 px, nagłówek w osobnym rzędzie przy 1024–1099 px, telefon 2 kolumny.
- **Menu:** Web-Ustawienia `src/data/nawigacja.json` → `menu[2]` (Studia), grupa „Na co dzień” (4 linki, `opis`: „plan, kalendarz, zajęcia, pierwszy rok”).
- **Ciekawostki:** `src/data/ciekawostki/studia.json`; `pulaDzialu()` w `src/lib/ciekawostki.ts` pomija `ukryta`, a przypięta ukryta karta się nie pokazuje.

## Docelowo

### 1. Strona `/studia/tutornia` (Web-Studia)
- Nowy plik `src/content/strony/studia/tutornia.md`, **treść dosłownie z załącznika A** (`.przekazanie\prototypy\45-tutornia\tutornia.md`). Strona jest zwykłą „Stroną studiów”: szablon podstrony Studiów (baner w kolorze działu, sygnet Knastera, spis „Na tej stronie”, „Następna strona w dziale”), wersja EN `/en/studia/tutornia` z `tresc_en`.
- Strona w `sitemap.xml` i w wyszukiwarce (Pagefind) jak inne strony.

### 1a. CMS jak w Studiach (wzór ze zlecenia 40, `dok/jawny-markdown.md`)
- **Formularz bez zmian:** Tutornia edytuje się w kolekcji „Strony studiów” Web-Studia (po zleceniu 40, etap 7: Tytuł, Tytuł EN, Opublikowane, Treść, Treść EN, potem drobne pola; `format_tresci` ukryte). **Żadnych nowych pól w tej kolekcji**: sala i daty grafiku są liniami w bloku. Pole „Liczby” zostaje dla Tutorni puste (liczby liczą się z bloku).
- **Komentarze w treści według wzoru Studiów** (załącznik A już tak ma):
  - na początku standardowe `<!-- UKŁAD JAWNY: … -->` (dosłownie jak w pozostałych stronach Studiów);
  - przed tekstem sekcji `<!-- TEKST: Zwykły Markdown. Specjalny układ wymaga jawnego znacznika bloku. -->`;
  - przy blokach jednoliniowe komentarze, pusta linia, blok:
    - `<!-- GRAFIK: Najpierw Sala:, Od: (np. 19.10.2026) i Do: (puste = do końca zajęć), potem jeden dyżur na linię: - pon. 12:15–14:00 **Imię Nazwisko** — przedmioty. -->`;
    - w Treści EN: `<!-- GRAFIK: Pusty blok wstawia grafik z wersji polskiej. Nie przepisuj dyżurów. -->`;
    - `<!-- PARY: Każdy punkt: **Etykieta:** treść. -->`;
    - `<!-- LINKI: Jeden link na punkt; po — można dopisać opis. -->` (standardowy);
  - `<!-- TERAZ: Ramkę „Teraz” … strona tworzy sama z grafiku. Nic tu nie wpisuj. -->` przed pierwszą sekcją.
- Komentarze GRAFIK i PARY dopisz do listy komentarzy wzorcowych w `dok/jawny-markdown.md`. Jeśli `sprawdz-jawny-markdown.mjs` sprawdza komentarze przy blokach, dodaj wzorce dla nowych bloków.

### 2. Blok `:::grafik` (Web-Core)
- **Składnia** (jedna linia = jedna informacja):
  ```
  :::grafik
  Sala: 202
  Od: 19.10.2026
  Do:

  - pon. 12:15–14:00 **Paulina Pawlik** — AM1, AM3, Algebra liniowa 1
  :::
  ```
  - `Sala:` numer sali (tekst); `Od:` pierwszy dzień dyżurów; `Do:` ostatni dzień, puste = koniec zajęć semestru, w którym leży `Od` (z `kolory-dni`). Daty `19.10.2026` albo `2026-10-19`.
  - Dyżur: `- <dzień> <od>–<do> **<Imię Nazwisko>** — <przedmioty>`. Dni: `pn`, `pon`, `poniedziałek`, `wt`, `wto`, `wtorek`, `śr`, `sr`, `środa`, `cz`, `czw`, `czwartek`, `pt`, `pią`, `piątek` (wielkość liter i kropka dowolne). Godziny `12:15`, `12.15`, `12` (pełna godzina). Separatory `–`, `—`, `-`, `do`. Imię i nazwisko w `**…**`; bez pogrubienia — do pierwszego ` — `, ` - ` albo `: `. Przedmioty opcjonalne, wyświetlane tak, jak je wpisano.
  - Komentarze `<!-- … -->` i puste linie pomijane. Kolejność linii dowolna (strona sortuje według dnia i godziny). Najwyżej jeden blok `:::grafik` na stronę.
  - Wzorcowy parser jest w prototypie (`tutornia.js`, funkcja `parsuj`). Linie bloku czytaj z tekstu źródłowego (pozycje węzła), bo Markdown w środku nie ma tu znaczenia.
- **Błędy nie zatrzymują budowy** (wyjątek od zasady innych bloków: grafik zmieniają często także studenci-redaktorzy):
  - linia, której parser nie rozumie, nie trafia na stronę;
  - na Podglądzie (budowa bez `TYLKO_OPUBLIKOWANE`) nad planem stoi czerwona ramka „Podgląd: tych linii grafiku strona nie rozumie” z numerem linii w bloku, tekstem linii, powodem i wzorem linii, jak w prototypie (`#tu-bledy`);
  - `skrypty/sprawdz_tresci.py` zgłasza ostrzeżenie (nie błąd).
  - Powody: brak dnia lub godzin, nieznany dzień, koniec przed początkiem, brak nazwiska, zła data w `Od`/`Do`, linia bez myślnika.
- **Wersja EN:** pusty blok `:::grafik` + `:::` w `tresc_en` wstawia grafik z wersji polskiej. Nazwy dni i teksty ramki po angielsku, nazwiska i przedmioty bez zmian. Pełny blok w `tresc_en` też działa (wtedy z niego).
- **Siatka tygodnia** (komputer, ≥ 1024 px), budowana statycznie przy budowaniu, żeby działała bez JavaScriptu. Wygląd jak w prototypie (`tutornia.css`, `.tu-siatka`):
  - kolumny pn–pt plus oś godzin 54 px;
  - wiersze co 5 min, 9 px;
  - **oś godzin liczona sama z grafiku** (nic nie ustawia się ręcznie):
    - zakres od najwcześniejszego początku do najpóźniejszego końca dyżuru w tygodniu (zaokrąglone do 5 min); dziś 12:15–17:00, po dopisaniu dyżuru 9:00–10:30 oś zaczyna się od 9:00;
    - etykiety i poziome linie na każdym różnym początku dyżuru (12:15, 13:15…), etykieta na końcu ostatniego (17:00);
    - **luki:** gdy między sąsiednimi etykietami (wliczając koniec) jest więcej niż 90 min, w luce dochodzą pełne godziny (10:00, 11:00…) z liniami, tylko te, które są co najmniej 30 min od sąsiednich etykiet (przykład: 9:00 → 12:15 daje 10:00 i 11:00, bez 12:00; 16:15 → 18:00 daje 17:00);
    - etykieta „teraz” zastępuje etykietę osi bliższą niż 12 min (niżej);
  - poziome linie godzin i pionowe linie dni w kolorze `--line`;
  - nagłówki dni Brygadą 18 px, nad grubą linią;
  - blok dyżuru: tło `color-mix(var(--d-j) 15%, var(--bg))`, lewa kreska 3 px `--d-a`; godziny (12 px, pogrubione, `--d-a`), nazwisko Brygadą 17 px, przedmioty 12,5 px szare (najwyżej 4 linie);
  - dyżur krótszy niż 60 min: godziny tylko dla czytnika ekranu, przedmioty najwyżej 2 linie;
  - nakładające się dyżury dzielą kolumnę po równo;
  - pod siatką zdanie z treści strony (akapit po bloku).
- **Telefon i okna < 1024 px** (to samo zapytanie co reszta strony, `src/lib/media`): lista dni (nazwa dnia Brygadą 21 px, wiersze: godziny w kolumnie 96 px, obok nazwisko i przedmioty), dzień bez dyżurów: „bez dyżurów”.
- **Dostępność:** każdy dzień to `section` z nagłówkiem `h3`, dyżury jako lista; kolejność czytania dzień po dniu (w prototypie `display: contents`).
- **Na żywo w przeglądarce** (skrypt, Europe/Warsaw, odświeżanie co minutę), bez zmiany układu:
  - **dziś:** kolumna podbarwiona (`--d-j` 8%), przy nazwie dnia „dziś” w kolorze `--d-a`, gruba linia pod nazwą w `--d-a`;
  - **linia „teraz”:** 2 px `--d-a` z kropką na początku, w kolumnie dzisiejszego dnia; na osi godzina (np. „14:55”) zamiast najbliższej etykiety osi (bliżej niż 12 min);
  - **trwający dyżur:** mocniejsze tło (`--d-j` 36%), kreska `--d-g`, znacznik „● teraz” w prawym górnym rogu;
  - **przygaszone (opacity .5): wszystkie dyżury bieżącego tygodnia, które już się skończyły, aż do obecnej godziny** — wcześniejsze dni pn–pt i dzisiejsze dyżury z końcem ≤ teraz. W dzień zamiany dni „dziś” to dzień planu. W weekend, w przerwach i poza okresem grafiku nic nie jest przygaszone (siatka pokazuje następny tydzień);
  - tryb ciemny: jak w prototypie (`:root[data-theme=dark] .tu`).

### 3. Ramka „Teraz” (nad pierwszą sekcją treści)
- Wygląd jak „Dziś” w Roku akademickim: kółko 72 px (telefon 56 px), etykieta z datą i godziną („Środa, 18 listopada 2026, 14:55”), tytuł Brygadą 30 px (telefon 25 px), opis. Kółko: pełne `--d-j` z inicjałami, gdy dyżur trwa; przerywane z inicjałami następnego tutora w pozostałych stanach.
- **Dzień otwarty** = dzień zajęć według `kolory-dni` (`infoDnia(d)?.kolor` niepuste; dni wolne, święta, przerwy i weekendy zamknięte) i data w zakresie `Od`–`Do`. Dyżury dnia = dyżury dnia tygodnia `infoDnia(d).plan`.
- **Stany i teksty PL** (EN analogicznie; wzór: prototyp, funkcja `stan`):
  | Stan | Tytuł | Opis |
  |---|---|---|
  | trwa dyżur | „Teraz dyżuruje Jacek Kowalski” (2+: „Teraz dyżurują A i B”) | „Do 16:00 · AM1, Algebra liniowa 1 · sala 202. Potem od 16:15: Eliza Laskowska.” albo „… Następny dyżur: jutro (czwartek), 13:15 — Róża Deć.” |
  | do dyżuru ≤ 30 min | „Za chwilę: Miłosz Cierkosz” | „Od 14:15 do 16:00 · AM1/I, … · sala 202.” |
  | dyżury dziś później | „Dziś od 12:15” (po przerwie: „Dziś jeszcze od …”) | lista „12:15–14:00 Cezary Goszczyński · 14:15–16:00 … · sala 202.” |
  | po dyżurach | „Na dziś to wszystko” | „Następny dyżur: poniedziałek, 23 listopada, 12:15 — Paulina Pawlik.” |
  | weekend | „W weekend tutornia nie działa” | jak wyżej |
  | dzień wolny | „Dziś tutornia nieczynna” | „Dzień rektorski. Następny dyżur: …” (opis dnia wolnego z `kolory-dni`) |
  | dzień zajęć bez dyżurów | „Dziś nie ma dyżurów” | „Następny dyżur: …” |
  | przed `Od` | „Tutornia rusza 19 października” | „Pierwszy dyżur: poniedziałek, 19 października, 12:15 — Paulina Pawlik · sala 202.” |
  | po `Do` / końcu semestru | „Dyżury w tym semestrze już się skończyły” | „Plan na kolejny semestr pojawi się tutaj, gdy będzie gotowy.” |
  - W dzień zamiany dni dopisek: „Dziś zajęcia według planu środy, więc dyżury też.”
  - „Następny dyżur”: dziś → „Potem od 16:15: …”; jutro → „jutro (czwartek), 13:15 — …”; dalej → „poniedziałek, 23 listopada, 12:15 — …”.
- **Bez JavaScriptu:** ramka z neutralnym tekstem („Sala 202 · dyżury według planu poniżej”, kółko przerywane), bez stanu z chwili budowania (strona przebudowuje się raz dziennie, więc taki stan byłby nieaktualny).
- `aria-live="polite"` jak w prototypie.

### 4. Baner
- Hasło z pola `haslo` / `haslo_en`.
- **Liczby liczone z bloku**, gdy pole `liczby` jest puste (wypełnione pole wygrywa):
  - liczba różnych osób: „9 tutorów” (1 tutor, w pozostałych przypadkach „tutorów”), EN „tutors”;
  - liczba dyżurów: „10 dyżurów w tygodniu” (1 dyżur, 2–4 dyżury, 5+ dyżurów, z regułą 12–14), EN „sessions a week”;
  - `Sala:` jako liczba: „202 sala tutorni”, EN „tutoring room”.
- Pod tytułem planu, w treści: linia „Semestr zimowy 2026/27 · od 19 października 2026 · sala 202” (nazwa semestru z `kolory-dni`, data z `Od`), jak `.tu-plan-meta` w prototypie.

### 5. Blok `:::pary` (ogólny, Web-Core)
- Lista punktów `- **Etykieta:** treść` → `dl` z parami w liniach (etykieta 150 px pogrubiona, treść obok, linie `--line` między parami), jak „Gdzie i jak” w prototypie (`dl.tu-para`). Na telefonie etykieta nad treścią.
- Walidacja jak w innych blokach: punkt bez `**…:**` na początku to błąd z czytelnym komunikatem.
- Dopisz do `BLOKI`, testów, `dok/jawny-markdown.md`, `dok/sciagawka-edytora.md` i `dok/zasady-parsera.md`. Klasa CSS wspólna (nie `tu-`).

### 6. Menu Studiów (Web-Ustawienia `nawigacja.json`)
- Grupa „Na co dzień”, 5. pozycja: `{ "etykieta": "Tutornia", "etykieta_en": "Tutoring room", "opis": "dyżury starszych studentów", "opis_en": "help from senior students", "adres": "/studia/tutornia" }`.
- Opis grupy: „plan, kalendarz, pierwszy rok, tutornia” / EN „timetable, calendar, first year, tutoring” (z „zajęciami” opis łamał się na 2 linie na karcie grupy).
- Na stronie Studiów karta grupy pokazuje „5 stron”; rząd podstron 5 pozycji (jak „Dyplom i sprawy”). Sprawdź, czy wszystko liczy się samo z danych.

### 7. Szybki dostęp (Web-Ustawienia `skroty.json` + `DrugiEkran.astro`)
- Piąty kafelek `{ "etykieta": "Tutornia", "etykieta_en": "Tutoring room", "adres": "/studia/tutornia" }`; w kodzie `slice(0, 5)` i siatka z liczbą kolumn = liczbie kafelków (przy 4 wygląda jak dziś).
- **Kafelek specjalny** dla `/studia/tutornia` (jak kafelek kolorów dni), podpis na żywo z tej samej funkcji co ramka „Teraz”; dane grafiku osadzone w stronie przy budowaniu. Teksty PL / EN:
  - trwa dyżur: kropka 8 px `--studia-j` + „teraz: Jacek Kowalski, do 16:00” (2+: „teraz: 2 tutorów, do 16:00”) / „now: …, until 16:00”;
  - ≤ 30 min: „od 14:15: Miłosz Cierkosz” / „from 14:15: …”;
  - dziś później: „dziś od 12:15 · sala 202” / „today from 12:15 · room 202”;
  - następny dzień: „jutro od 13:15 · sala 202”, dalej „pon. od 12:15 · sala 202” / „tomorrow from …”, „Mon from …”;
  - dzień wolny, następny dyżur dalej niż jutro: „nieczynna, wraca 7 sty” / „closed, back 7 Jan”;
  - przed `Od`: „rusza 19 paź” / „starts 19 Oct”;
  - po semestrze albo bez grafiku: „sala 202” / „room 202”.
  - Bez JavaScriptu: „sala 202”.
- **Układ:**
  - od 1500 px: nagłówek „Szybki dostęp” w jednym rzędzie z 5 kafelkami;
  - 1024–1499 px: nagłówek w osobnym rzędzie nad kafelkami (przy 1366 px w jednym rzędzie podpisy łamały się na 2 linie);
  - telefon: siatka 2×2, a Tutornia w trzecim rzędzie na całą szerokość.
  - **Uwzględnij to w rachunku miejsca ze zlecenia 35** (wysokość pasa z nagłówkiem nad kafelkami) i sprawdź Full HD 1920×950: Studia i „Warto wiedzieć” bez przesunięcia względem stanu po zleceniu 35.

### 8. „W skrócie” na stronie Studiów
- Nowe opcjonalne pole pozycji „W skrócie” `adres` (wszystkie działy; schemat Web-Core i formularze `.pages.yml` w repozytoriach działów, etykieta „Link (opcjonalnie)”). Z adresem wartość (np. „Tutornia”) jest linkiem, jak w prototypie (bez podkreślenia, podkreślenie po najechaniu, mała strzałka →).
- Web-Studia `src/data/studia.md`: Tutornia → `adres: /studia/tutornia`.

### 9. Ciekawostka
- `src/data/ciekawostki/studia.json`, karta `seminarium-w-salonie`: `stan: "przypieta"`, `strona: "/studia/tutornia"`, **`ukryta: true` zostaje**. Sprawdź, że do czasu odkrycia Tutornia dostaje ciekawostkę z losowania, a po usunięciu `ukryta` (test na kopii) — zawsze tę kartę.

### 10. Linki w treściach (Web-Studia)
- `pierwszy-rok.md` i `sprawy-studenckie.md` (PL i EN): link do aktualności → `/studia/tutornia` (`/en/studia/tutornia`).
- Zdania typu „plan dyżurów tutorów jest w załączniku do ogłoszenia” → „plan dyżurów jest na stronie tutorni” (EN analogicznie); daty „od 19 października” mogą zostać.
- Aktualność `2026-10-17-rusza-tutornia` bez zmian.
- Sprawdź kotwice EN z załącznika A (`/en/studia/zajecia#konsultacje` itd.) i popraw na istniejące.

### 11. Dokumentacja
- `dok/sciagawka-edytora.md`, `dok/jawny-markdown.md`, mapa CMS (`dok/dla-redaktorow`): blok `:::grafik` (sala, daty, linia dyżuru, pusty blok w EN, czerwona ramka na Podglądzie) i `:::pary`.
- **Opisy pól „Treść” i „Treść EN”** w kolekcji „Strony studiów” (`.pages.yml` Web-Studia): dopisz `:::grafik` i `:::pary` do listy przykładowych bloków (obowiązkowo; krótko, w stylu obecnego opisu). Zmiana opisów to zmiana `.pages.yml`, więc obowiązuje „Ochrona zmian redaktorów”.

## Odbiór lokalny
- **Porównanie HTML przed/po** (PL i EN, te same klony treści, bez przerwy między budowami). Dozwolone różnice:
  - nowa strona `/studia/tutornia` i `/en/studia/tutornia`;
  - menu (pozycja Tutornia na wszystkich stronach);
  - strona Studiów: grupa „Na co dzień”, link „W skrócie”;
  - strona główna: Szybki dostęp;
  - linki w „Pierwszym roku” i „Sprawach studenckich”;
  - mapa strony.
  Pozostałe strony bez różnic.
- **Testy jednostkowe parsera** (`:::grafik`): przykłady z załącznika A, warianty zapisu (`12.15-14`, `poniedziałek`, bez pogrubienia, kolejność dowolna), błędy (każdy powód), pusty blok EN, `Do` puste i wpisane, nakładające się dyżury.
- **Testy osi godzin:** grafik z załącznika A → 12:15 13:15 14:15 15:15 16:15 17:00; z dodatkowym dyżurem pt. 9:00–10:30 i pon. 16:15–18:00 → 9:00 10:00 11:00 12:15 13:15 14:15 15:15 16:15 17:00 18:00; z dyżurem 10:40–11:20 zamiast 9:00–10:30 → 10:40 12:15 … (bez 11:00 i 12:00, bo za blisko). Zrzut wariantu z luką.
- **Stany na żywo** (Playwright, `page.clock.setFixedTime`, strefa Europe/Warsaw), dla każdego zrzut ramki „Teraz”, siatki i kafelka Szybkiego dostępu:
  - śr. 18.11.2026 14:55 (trwa dyżur), śr. 18.11 13:00 (Abramek „teraz”, Kowalski zwykły, pn–wt przygaszone), śr. 18.11 16:51 (po dyżurach, pn–śr przygaszone);
  - pn. 23.11 14:05 (za chwilę), wt. 24.11 9:30 (dziś później), pt. 20.11 17:30, sob. 21.11;
  - czw. 12.11 (dzień rektorski), pt. 18.12 13:00 (zamiana dni: plan środy, Abramek „teraz”), pn. 28.12 (przerwa świąteczna), pn. 12.10 (przed startem), pn. 15.02.2027 (po semestrze).
- **Zrzuty stron:** Tutornia 1920×1080, 1536×864, 1366×768, 1024×768 i 390 px; tryb jasny i ciemny; z ramką błędów (kopia testowa z błędną linią). Strona główna (Szybki dostęp) 1920×950, 1536×864, 1366×768 i 390 px. Strona Studiów z otwartą grupą „Na co dzień” (komputer i telefon).
- **Edytor:** symulacja zapisu jak w zleceniu 28 (etap 6a). `tutornia.md` przepuszczony przez wczytanie i zapis edytorem daje pusty diff albo tylko opisaną kosmetykę; blok `:::grafik` przeżywa zapis bez zmian.
- **Kontrole:** `astro check` bez nowych błędów, `sprawdz_pola_cms.py`, `sprawdz_tresci.py` i `sprawdz-jawny-markdown.mjs` (z nowymi blokami) bez problemów, testy wtyczek zielone, konsola czysta, `lychee` bez nowych martwych linków.
- **Test w CMS z właścicielem** (jak w zleceniu 40, krok 8): otwarcie Tutorni w „Stronach studiów”, zapis bez zmian (pusty diff albo opisana kosmetyka), zmiana jednej linii grafiku i podgląd po przebudowie.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] `/studia/tutornia` i `/en/studia/tutornia` z treścią z załącznika A, w szablonie podstrony Studiów, w menu „Na co dzień” jako 5. pozycja.
- [ ] Baner: hasło i liczby 9 tutorów · 10 dyżurów w tygodniu · 202 sala tutorni, liczone z bloku.
- [ ] Siatka tygodnia (komputer) i lista dni (telefon) z bloku `:::grafik`, także bez JavaScriptu; EN z pustego bloku.
- [ ] Oś godzin sama z grafiku: zakres od najwcześniejszego do najpóźniejszego dyżuru, pełne godziny w lukach powyżej 90 min.
- [ ] Na żywo: dziś, linia „teraz”, trwający dyżur; **przygaszone wszystkie dyżury bieżącego tygodnia, które się skończyły, aż do obecnej godziny**; w weekend i poza zajęciami nic nie jest przygaszone.
- [ ] Ramka „Teraz” we wszystkich stanach z tabeli, z dniami wolnymi i zamianami dni z Roku akademickiego.
- [ ] Szybki dostęp: 5. kafelek „Tutornia” z podpisem na żywo; układ 1500+/1024–1499/telefon jak opisano; rachunek miejsca ze zlecenia 35 zgodny.
- [ ] Błędna linia grafiku nie zatrzymuje budowy: czerwona ramka tylko na Podglądzie, ostrzeżenie w `sprawdz_tresci.py`.
- [ ] CMS jak w Studiach (zlecenie 40): Tutornia w „Stronach studiów” bez nowych pól, komentarze w treści według wzoru, opisy „Treść”/„Treść EN” z `:::grafik` i `:::pary`.
- [ ] Blok `:::pary`, link w „W skrócie” (pole `adres`), przypięta (ukryta) ciekawostka, linki w treściach, dokumentacja.
- [ ] Zapisy redaktorów w Web-Studia i Web-Ustawienia zachowane (kontrola przed i po pushu, przegląd następnego dnia).

## Załączniki (`.przekazanie\prototypy\45-tutornia\`)
- **A. `tutornia.md`** — gotowy plik strony dla Web-Studia (frontmatter PL/EN, treść jawna z `:::grafik`, `:::pary`, `:::linki` i komentarzami według wzoru Studiów; wersja z 18:15; bez zmian 18:33).
- **B. Prototyp** — źródła artefaktu:
  - `tutornia.js`: parser, stany, siatka, kafelek; wzór logiki, nie kod do skopiowania;
  - `tutornia.css`: wygląd siatki, ramki, par i kafelka (zmienne strony: `--d-j`, `--d-a`, `--d-g`, `--line`, `--bg`, `--f-display`);
  - `tresc.html`: treść strony w HTML;
  - `powloka.html`: widoki i edytor CMS na żywo;
  - `build.py`: budowa prototypu na stronach Web-Podglad.
