# Zlecenie 44: „Kariera” jako podstrona Aktualności, poza listą aktualności (18.11.2026)

**Decyzje właściciela (18.11):**
- **11:52:** „Kariera nie powinna lądować w aktualnościach, powinna mieć swoją własną, małą podsekcję, klikalną z poziomu Aktualności.”
- **11:55: wariant A** („zdecydowanie tak”). Ten sam formularz co dziś: redaktor dalej wybiera „Rodzaj: Kariera”. Strona wyjmuje te wpisy z Aktualności i pokazuje je na własnej podstronie. Bez osobnego formularza i bez przenoszenia wpisów.
- **11:58: zgoda na trzy propozycje:**
  1. link z Aktualności jako ramka „Oferty pracy, staży i stypendiów (N) →” w prawej kolumnie, w miejscu dzisiejszego filtra „Kariera”;
  2. strona główna bez ofert (kolumna Aktualności i liczba na okładce); strona Studiów zostawia oferty w „Aktualnościach dla studentów”;
  3. opcjonalny termin zgłoszeń, dodawany kliknięciem jak „Termin wydarzenia”. Po terminie oferta przechodzi do sekcji „Zakończone”. Oferta bez terminu jest aktualna, dopóki redaktor jej nie usunie albo nie dopisze terminu.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela (albo w trybie autonomicznym według zasad z 18.11).
- **Kolejność:** okno 2, po zleceniu 36. Korzysta z gotowych 31 (wzór grupy „Termin wydarzenia”), 33 (funkcja `widoczny()`, szkice), 35 (Szybki dostęp) i 37 (baner wpisu).
- **Repozytorium treści Web-Aktualnosci** (`.pages.yml` i jeden nowy plik `src/content/strony/kariera.md`):
  - zawsze od świeżego `main`, zwykły commit, bez force-push; `.pages.yml` i nowy plik w jednym commicie;
  - zlecenie 40 (okno 1) też zmienia `.pages.yml` Web-Aktualnosci. Tuż przed pushem `git fetch`; jeśli `.pages.yml` się zmienił, nanieś swoją zmianę na nową wersję, nie nadpisuj jej starą;
  - push wieczorem albo po wiadomości właściciela do redaktorów; następnego dnia przegląd zapisów redaktorów z 24 godzin (czy nikt starym formularzem nie usunął nowej grupy).
  - Danych istniejących wpisów nie zmieniaj (żadnej migracji).
- Raport `RAPORT-ZLECENIE-44.md`, zrzuty `raport-zrzuty/z44-*`. Bez subagentów.

## Stan dziś (sprawdzone 18.11 na `main`)
- **Formularz** (Web-Aktualnosci, `.pages.yml`): pole „Rodzaj” (`rodzaj`, select) z opcjami Ogłoszenie, Wydarzenie, Sukces, Kariera. Grupa „Termin wydarzenia” (`termin`, `type: object`, `list: max: 1`) z zlecenia 31 jest wzorem dla nowej grupy.
- **Wpisy „Kariera”:** 11 (praca dla nauczycieli matematyki, staże, stypendium doktoranckie, KSAP). Żaden nie ma terminu zgłoszeń.
- **Gdzie widać je dziś:**
  - lista Aktualności: `src/lib/widoki/listaAktualnosci.ts` (`daneListyAktualnosci`, `rodzaje` z filtrem „Kariera”), widok `src/views/ListaAktualnosci.astro`, panel „Pokaż” (`?rodzaj=kariera`);
  - strona główna: `aktualnosciNaGlowna()` w `src/lib/tresci.ts` (ok. linii 399) ich nie odfiltrowuje → kolumna Aktualności w `src/components/zal/DrugiEkran.astro` i liczba na okładce (`liczbyNaOkladke`);
  - strona Studiów: `src/lib/widoki/dzialStudia.ts` (ok. linii 54), wpisy `dla: studenci`;
  - RSS: `src/pages/rss.xml.ts` i `src/pages/en/rss.xml.ts` (`listaAktualnosci`, 30 najnowszych).
- **Wpis:** `src/views/Aktualnosc.astro`, link wstecz „Wszystkie aktualności” → `/aktualnosci`. `dzialWpisu()` w `src/lib/patroni.ts` daje „kariera” → Studia.
- **Teksty listy:** Web-Aktualnosci → Strony → Aktualności (`src/content/strony/aktualnosci.md`, `stronaListy('aktualnosci')` w `src/lib/tekstyStron.ts`).
- **Trasy:** `src/pages/aktualnosci/[slug].astro`, `zamiana-dni-[data].astro`, `index.astro` (i to samo pod `en/`).

## Docelowo

### 1. Lista Aktualności bez ofert
- Wpisy `rodzaj: kariera` nie są na liście Aktualności (PL i EN). Filtr „Kariera” znika z panelu „Pokaż” (wynika to samo z listy rodzajów).
- **Ramka z linkiem** do podstrony:
  - komputer: w prawej kolumnie panelu „Pokaż”, pod filtrami, w stylu panelu (bez nowego koloru);
  - telefon: pełna szerokość, nad listą, pod polem szukania;
  - tekst: „Oferty pracy, staży i stypendiów (3) →” / EN „Jobs, internships and scholarships (3) →”. Liczba = aktualne oferty (punkt 3). Przy zerze bez liczby.
- **Stare linki:** `/aktualnosci?rodzaj=kariera` (i EN) przekierowuje na podstronę Kariera (w skrypcie listy, `location.replace`).

### 2. Podstrona Kariera
- **Adres:** `/aktualnosci/kariera`, EN `/en/aktualnosci/kariera`. Baner Aktualności (`banerAktualnosci()` już obejmuje `/aktualnosci/…`). Link wstecz „← Aktualności”.
- **Teksty edytowalne w CMS:** nowy plik Web-Aktualnosci `src/content/strony/kariera.md`, czytany jak `aktualnosci.md` (`stronaListy('kariera')`). Treść startowa:
  - tytuł „Kariera” / „Careers”;
  - opis „Oferty pracy, staży i stypendiów dla studentów, absolwentów i doktorantów.” / „Job, internship and scholarship offers for students, graduates and PhD students.”;
  - hasło według wzoru `aktualnosci.md`; zaproponuj w raporcie.
- **Lista:**
  - u góry **aktualne** oferty, od najnowszej daty publikacji; pod nimi sekcja **„Zakończone”** / „Closed” (oferty po terminie zgłoszeń), przygaszona, w tym samym układzie wierszy;
  - wiersze jak na liście Aktualności (`WierszAktualnosci`); przy ofercie z terminem dopisek „Zgłoszenia do 15.12” / „Apply by 15 Dec” (po terminie „Nabór zakończony” / „Closed”);
  - pole szukania (jak w Aktualnościach), bez filtra rodzaju;
  - gdy aktualnych ofert brak: krótki napis „Obecnie brak aktualnych ofert.” / „No current offers.” nad sekcją „Zakończone”.
- **Mapa strony:** podstrona w `sitemap.xml`.
- **Zarezerwowany adres:** sprawdź, że żaden wpis aktualności nie może dostać nazwy pliku `kariera` (generator nazw plików z zlecenia 31 i `sprawdz_tresci.py`). Jeśli może, dodaj blokadę albo czytelny błąd kontroli.

### 3. Termin zgłoszeń w formularzu
- **Nowa grupa** w `.pages.yml` Web-Aktualnosci, zaraz pod „Termin wydarzenia”, według tego samego wzoru (`type: object`, `list: max: 1`, dodawana przyciskiem):
  - nazwa np. `zgloszenia`, etykieta „Termin zgłoszeń (tylko oferty: Rodzaj „Kariera”)”;
  - pole „Do dnia” (`date`, wymagane w grupie);
  - opis: „Tylko dla ofert pracy, staży i stypendiów. Po tym dniu oferta przechodzi do »Zakończonych« na stronie Kariera i znika ze strony Studiów. Bez terminu oferta jest aktualna, dopóki jej nie usuniesz.”
- **Opis pola „Rodzaj”:** dopisz, że „Kariera” trafia na podstronę Kariera, a nie na listę Aktualności i stronę główną.
- **Schemat** (`src/content.config.ts`): grupa opcjonalna. Termin przy wpisie innego rodzaju strona pomija, a `sprawdz_tresci.py` zgłasza ostrzeżenie (nie błąd budowy).
- **Aktualna oferta** = brak terminu albo termin ≥ dziś (cały dzień terminu oferta jest jeszcze aktualna). Podgląd przebudowuje się codziennie, więc przejście do „Zakończonych” dzieje się samo.

### 4. Wpis oferty
- Adres bez zmian (`/aktualnosci/<nazwa>`), więc istniejące linki działają.
- Link wstecz: „Wszystkie oferty” / „All offers” → `/aktualnosci/kariera`.
- Przy ofercie z terminem, pod tytułem lub w metryczce: „Zgłoszenia do 15 grudnia 2026” albo „Nabór zakończony”.
- Baner i podświetlenie w menu według zlecenia 37 (bez zmian w tym zleceniu).

### 5. Strona główna, Studia, RSS
- **Strona główna:** `aktualnosciNaGlowna()` pomija `kariera`. Dzięki temu oferty znikają z kolumny Aktualności i z liczby na okładce. Sprawdź też Szybki dostęp po zleceniu 35 („Ostatnio”): jeśli bierze aktualności, oferty pomija.
- **Studia:** „Aktualności dla studentów” dalej pokazują oferty, ale tylko aktualne (bez tych po terminie).
- **RSS** (PL i EN): bez ofert, jak lista Aktualności.
- **Kalendarz i `.ics`:** bez zmian.
- **Wyszukiwarka (Pagefind):** wpisy ofert dalej wyszukiwalne.

## Odbiór lokalny
- **Porównanie HTML przed/po** (PL i EN) na tych samych klonach treści, bez przerwy między budowami. Różnice tylko:
  - lista Aktualności: bez 11 ofert, bez filtra „Kariera”, z ramką;
  - strona główna: kolumna Aktualności i liczba na okładce bez ofert;
  - RSS bez ofert;
  - wpisy ofert: link wstecz;
  - nowa podstrona Kariera i jej pozycja w mapie strony.
  Pozostałe strony, w tym strona Studiów (dziś żadna oferta nie ma terminu), bez różnic.
- **Termin zgłoszeń** (na kopii testowej wpisu, nie w repozytorium): termin wczoraj → oferta w „Zakończonych”, znika ze Studiów, licznik w ramce maleje; termin dziś → aktualna; bez terminu → aktualna.
- **Formularz:** symulacja zapisu jak w zleceniu 31 (etap 4): stara oferta otwarta i zapisana bez zmian daje pusty diff albo tylko opisaną kosmetykę; dodanie terminu zapisuje grupę w oczekiwanym formacie.
- **Przekierowanie** `?rodzaj=kariera` działa (PL i EN).
- **Zrzuty:** lista Aktualności z ramką (komputer 1536×864 i 1920×1080, telefon 390 px), podstrona Kariera z ofertą aktualną, z terminem i zakończoną, wpis oferty z terminem; tryb jasny i ciemny.
- **Kontrole:** `astro check` bez nowych błędów, `sprawdz_pola_cms.py` i `sprawdz_tresci.py` bez problemów, testy wtyczek zielone, konsola czysta.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Oferty („Rodzaj: Kariera”) nie są na liście Aktualności, na stronie głównej, w liczbie na okładce ani w RSS.
- [ ] Podstrona `/aktualnosci/kariera` (i EN) z aktualnymi ofertami i sekcją „Zakończone”; teksty edytowalne w CMS (Strony → Kariera).
- [ ] Ramka „Oferty pracy, staży i stypendiów (N) →” na liście Aktualności (komputer i telefon), liczba = aktualne oferty.
- [ ] Opcjonalny termin zgłoszeń w formularzu, dodawany kliknięciem; po terminie oferta sama przechodzi do „Zakończonych” i znika ze Studiów.
- [ ] Strona Studiów pokazuje tylko aktualne oferty; wpisy ofert mają link wstecz do Kariery.
- [ ] `?rodzaj=kariera` przekierowuje na podstronę; adres `kariera` nie koliduje z nazwami wpisów.
- [ ] Bez migracji danych; zapisy redaktorów w Web-Aktualnosci zachowane (kontrola przed i po pushu, przegląd następnego dnia).
