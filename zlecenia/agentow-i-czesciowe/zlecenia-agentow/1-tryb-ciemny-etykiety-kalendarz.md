Pracujesz w repozytorium strony Instytutu Matematycznego UWr: /home/claude/web-core (Astro 5 + React, strona statyczna, gałąź `agent-nauka-podglad`, HEAD 9f394c81). Raport końcowy napisz PO POLSKU.

## BEZWZGLĘDNE ZASADY
- **NIE pushuj niczego.** Wolno tylko lokalny commit na `agent-nauka-podglad`.
- **NIE commituj** w repozytoriach treści (`.tresci/*`). **NIE uruchamiaj** `skrypty/pobierz_tresci.py`. Nakładki `src/data/*` nie ruszaj.
- Zmieniaj tylko to, co potrzebne. Inni agenci robią równolegle samodzielne prototypy HTML w scratchpadzie i nie dotykają repo. Buduj do własnego katalogu, nie do `dist`.
- Przeczytaj `README.md`. Przy decyzjach zostawiaj komentarze po polsku z datą „decyzja 31.10.2026”. Telefon = `@media (max-width: 760px)`, komputer = `(min-width: 761px)`. Istnieją klasy `.tylko-telefon` / `.tylko-komputer`.
- **Komputer (≥ 761 px) ma zostać bez zmian.** Wszystkie zmiany z tego zadania dotyczą tylko telefonu. Rób to tak, żeby później łatwo było rozszerzyć je na komputer: tokeny CSS, a nie selektory jednorazowe.

## Kontekst
Raport z propozycjami z 31.10: https://claude.ai/artifact/DhWpb96C3MMwNCZ6tM8n3V. Możesz go odczytać narzędziem Artifact (read), ale nie zmieniaj go. CSS makiet jest w `/tmp/claude-0/-home-claude/f8da5dc6-8de1-54ed-a382-aba453ec50fb/scratchpad/propozycje-tel/raport/zrodla/warianty.js` (stałe A1, B1, B_JS i inne). To szkic z dużą liczbą `!important`. Wdróż go porządnie, w stylach i komponentach, nie przez wstrzyknięcia.

Dziś na telefonie, już w kodzie:
- banery działów: bursztynowe hasło (`NaglowekStrony.astro`, prop `haslo`, `<p class="ph-haslo tylko-telefon">`), pod nim kreska i liczby w 3 kolumnach (`.pt-liczby`, `portal.css`, `text-wrap: balance`, funkcja `bezSierotek()` w `src/lib/i18n.ts`);
- Aktualności (`src/views/ListaAktualnosci.astro`): wiersz filtrów „lista rozwijana + Szukaj” i liczby w banerze;
- plakietki w jednej linijce z „+N” (skrypt w `src/components/WierszAktualnosci.astro`, zdarzenie `wa-przelicz`);
- rytm wierszy list, jasne kafelki dat w jasnym motywie, kropki `.kropki`/`.kropka`.

## Zadanie (decyzje użytkownika z 31.10)

### 1. Ciemny motyw: wariant A1 „stalowy granat” (tylko telefon)
W ciemnym motywie `--primary` jest bursztynowe, przez co na bursztynowo świecą:
- kafelki dat (`.datebox`, `.pt-dbox`),
- etykieta „Wydarzenie”,
- aktywne filtry (`.chip[aria-pressed='true']`),
- okrągły przycisk menu (`.burger`).

Wprowadź token „znacznik” według A1 z `warianty.js`:
- jasny motyw: `--znacznik: #1b2d52; --znacznik-ink: #fff`;
- ciemny motyw: `--znacznik: #2b4170; --znacznik-ink: #f1f4fa; --znacznik-tekst: #a9c0e8`;
- miesiąc na kafelku daty w ciemnym motywie zostaje bursztynowy;
- w granatowym banerze (`.ph-granat`) aktywny filtr jest biały z granatowym tekstem.

Tekstowe akcenty, które dziś w ciemnym motywie są bursztynowe (`.pt-k`, `.pt-all`, `.link-arrow` itd.), dostają `--znacznik-tekst`. Pełna lista jest w A_BAZA.

Bursztyn zostaje tylko jako akcent: hasło, rysunek w banerze, miesiąc na kafelku daty, kreski sekcji. Linki w treści i kreski sekcji zostaw bez zmian.

Uwaga: jasne kafelki dat w jasnym motywie (#eef2f9 z ramką) są już wdrożone. Nie psuj ich. W ciemnym motywie kafelki mają być według A1.

### 2. Etykiety: wariant B1 (Aktualności i Kalendarz identycznie, tylko telefon)
- **Kształt:** jak w B1 z `warianty.js`: **lekko zaokrąglone prostokąty**, promień ok. 6 px, a NIE pełne pastylki. Padding 1px 8px, 12,5 px, 700.
- **Kolory jak w B1 (tokeny `--et-*`):**
  - domyślnie szara mgiełka, np. Seminarium i Ogłoszenie;
  - Wydarzenie: granatowa mgiełka;
  - Sukces i Konferencja: bursztynowa mgiełka z ciemnym tekstem.
- **Obrona doktorska** (decyzja użytkownika: „mgiełka z biretem”):
  - mocniejsza granatowa mgiełka (jasny: tło #c3d2ee, tekst #0f2552; ciemny: tło `rgb(120 160 235 / .42)`, tekst #eef3ff);
  - przed napisem mała ikonka biretu 14 px w kolorze tekstu.
  - Ikonę zrób jako SVG w znacznikach albo maskę CSS. Wzór SVG (viewBox 0 0 24 24): `<path d="M12 4 2 9l10 5 10-5-10-5z" fill="currentColor"/><path d="M6 11.2V15c0 1.4 2.7 2.8 6 2.8s6-1.4 6-2.8v-3.8M21 9v5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>`.
  - Ikona ma `aria-hidden`.
- **Odbiorcy** (Studenci, Doktoranci, Pracownicy, Kandydaci…):
  - nie jako plakietki, tylko zwykły szary tekst małymi literami, po przecinku („studenci, doktoranci”), 13,5 px, 500, kolor `--et-dla`, jak `B_DLA`/`B_JS` w `warianty.js`, ale zrobione w komponencie, nie skryptem;
  - zwijanie do „+N” zostaje: skrypt w `WierszAktualnosci.astro` ma działać z nowym wyglądem; „+N” też jako szary tekst, pogrubiony.
- **Ta sama rodzina etykiet w Kalendarzu** (`src/components/KartaWydarzenia.astro`, `src/views/Kalendarz.astro`) i w Aktualnościach. Jeśli w Kalendarzu są odbiorcy, mają wyglądać tak samo, z „+N”. Sprawdź też inne listy używające tych plakietek (obrony, konferencje, seminaria) i ujednolić je.
- **Zakres:** telefon, jasny i ciemny motyw. Komputer bez zmian.

### 3. Kalendarz na telefonie przebudowany jak Aktualności
Strona `src/views/Kalendarz.astro`, adres `/kalendarz/`. Dziś na telefonie baner ma 403 px: długi opis i 5 przycisków kategorii w banerze (Wszystkie, Wydarzenie, Obrona doktorska, Konferencja, Seminaria). Pod banerem są „Nadchodzące / Archiwum”, a pierwszy wpis zaczyna się w 481 px. Zmień to tak:
- **Baner:**
  - tytuł;
  - bursztynowe hasło **„Co, gdzie i kiedy”** (EN: „What, where and when”), przez prop `haslo` w `NaglowekStrony`;
  - na telefonie opis znika, tak jak w działach. Opis zostaje w `<meta description>` i na komputerze.
  - pod hasłem kreska i **trzy liczby w 3 kolumnach** (`<ul class="pt-liczby tylko-telefon">`, jak w Aktualnościach), liczone przy budowaniu z najbliższych 30 dni od dnia budowania:
    - **seminaria**: referaty seminariów, odmiana „seminarium / seminaria / seminariów”;
    - **wydarzenia**: „wydarzenie / wydarzenia / wydarzeń”;
    - **obrony doktorskie**: „obrona / obrony / obron”.
  - Etykieta czasu: **„w ciągu 30 dni”** (EN: „in the next 30 days”), z `bezSierotek()`.
  - Zera pomijamy.
  - Etykiety mają się zmieścić w **2 równych linijkach** przy 390 i 360 px. Jeśli się nie mieszczą, sprawdź krótsze wersje, np. „przez 30 dni”, „do 30 dni”, i wybierz najkrótszą naturalną, która się mieści. Opisz to w raporcie.
- **Filtry na telefonie:**
  - przyciski kategorii z banera znikają (na komputerze zostają);
  - pod banerem jeden wiersz jak w Aktualnościach: lista rozwijana (Wszystkie, Seminaria, Wydarzenia, Obrony, Konferencje; liczba mnoga; ten sam wygląd i kod co w Aktualnościach, najlepiej wspólny) oraz pole **„Szukaj”**, które filtruje wpisy po tekście jak w Aktualnościach. Sprawdź, czy Kalendarz ma już jakieś wyszukiwanie; jeśli nie, dodaj je;
  - pod tym mały, zwarty przełącznik „Nadchodzące | Archiwum” w jednej linii, np. segmentowy, ok. 36 px wysokości.
- **Synchronizacja:** stan filtrów zsynchronizowany z przyciskami komputera. Parametry z adresu, jeśli Kalendarz je obsługuje, mają działać. Bez gubienia stanu przy zmianie szerokości przez 760 px.
- **Komputer bez zmian.**

### 4. Aktualności: krótsze etykiety liczb
W `ListaAktualnosci.astro` etykiety liczb „w ostatnim miesiącu” zmień na **„z 30 dni”** (EN: „in 30 days”): „2 ogłoszenia z 30 dni”, „4 wydarzenia z 30 dni”, „6 seminariów z 30 dni”. Mają się mieścić w 2 równych linijkach przy 390 i 360 px.

### 5. Jeden styl dla Aktualności i Kalendarza
Decyzja użytkownika: wszystkie zmiany mają dawać **taki sam styl** w Aktualnościach i Kalendarzu. Wspólne mają być:
- baner (hasło, kreska, 3 liczby),
- wiersz filtrów,
- etykiety,
- rytm wierszy,
- kropki,
- ciemny motyw.

Różnice wynikają tylko z treści: Kalendarz ma kafelki dat i przełącznik Nadchodzące/Archiwum, Aktualności mają datę tekstem i miniatury. Sprawdź to na zrzutach obok siebie.

## Weryfikacja (obowiązkowa)
- **Build** do własnego katalogu: `export NO_PROXY=localhost,127.0.0.1,::1 no_proxy=localhost,127.0.0.1,::1 npm_config_noproxy=localhost,127.0.0.1,::1; npx astro build --outDir <twój katalog w /tmp/claude-0/-home-claude/f8da5dc6-8de1-54ed-a382-aba453ec50fb/scratchpad/>/Web-Core`. Zrób też build SPRZED zmian. Serwuj `python3 -m http.server <wolny port>`, strona będzie pod `/Web-Core/`. Playwright jest zainstalowany (`require('playwright')`, `chromium.launch()` bez opcji); nie instaluj go ponownie.
- **Telefon** 390×844 i 360 px, isMobile, DPR 2, reducedMotion 'reduce'. Jasny i ciemny motyw (klucz `localStorage` „motyw”), PL i EN. Strony: `/kalendarz/`, `/aktualnosci/`, `/studia/`, `/nauka/`, strona główna, obrony, konferencje, seminaria.
  - Zrzuty przed/po oraz zestawienie Aktualności i Kalendarza obok siebie.
  - Zmierz wysokość banera Kalendarza i położenie pierwszego wpisu przed/po.
  - Podaj liczby, które wychodzą w Kalendarzu.
- **Testy działania:**
  - lista i szukaj w Kalendarzu filtrują poprawnie;
  - Nadchodzące/Archiwum działa;
  - „+N” działa w obu listach po zmianach.
- **Komputer** 1440×900, reducedMotion 'reduce', jasny i ciemny: porównanie pikselowe przed/po dla `/`, `/kalendarz/`, `/aktualnosci/`, `/studia/`, `/nauka/`, obron i konferencji. Ma być 0 różnic. Każdą różnicę wyjaśnij albo usuń.
- **Brak błędów** w konsoli i brak poziomego przewijania.

## Na koniec
- Lokalny commit na `agent-nauka-podglad` (opis po polsku), zakończony liniami:
```
Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TZCziyPYNSMRFYMjxrntio
```
- Raport (po polsku, zwięźle):
  - hash commita;
  - lista WSZYSTKICH zmienionych plików;
  - co zrobiłeś w każdym punkcie, z pomiarami przed/po;
  - wyniki testów;
  - pełne bezwzględne ścieżki do kluczowych zrzutów: Kalendarz i Aktualności obok siebie, jasny i ciemny, 360 px;
  - ryzyka.
- NIE pushuj.