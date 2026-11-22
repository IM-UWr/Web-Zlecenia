# Raport: zlecenie 34, tryb ciemny „Granat z krawędzią”

**Status:** zrobione i wypchnięte 18.11.2026 o 11:16 UTC, w trybie samodzielnym.
- Web-Core `main`: `cbca5051..b7192769`, zwykły push, bez force.
- Przed pushem: `fetch` (`origin/main` bez zmian, więc `rebase` był pusty) i ponowna budowa.
- **Podgląd:** przebieg [44293228901](https://github.com/IM-UWr/Web-Podglad/actions/runs/44293228901) (`przebuduj`) zielony, trwał 81 s.
- **Historia:** praca zaczęła się nocą 17/18.11 w lokalnym commicie WIP na bazie `c2c193e0`. Po punkcie 9 zlecenia 32 przeniosłem ją `rebase` na `cbca5051` (bez konfliktów) i cały odbiór zrobiłem od nowa na tej bazie.

## Zmienione pliki
Wszystkie nowe reguły stoją pod `:root[data-theme="dark"]`, więc tryb jasny się nie zmienia. Reguły zmieniłem na miejscu, bez nakładki.

- **`src/styles/zalozyciele.css`:**
  - tokeny z tabeli zlecenia, w tym nowy `--pow-2`;
  - dopisane `--photo`, `--minione-*` i `--footer-*`;
  - nowa zmienna `--burger-tlo: transparent`;
  - kolory działów: `--d-a = color-mix(in oklab, var(--d-j) 80%, var(--ink))`, `--d-t = var(--surface)`, nowy `--d-kafel`;
  - `.akt-wydarzenie` na tokenach;
  - krawędź banera (`box-shadow: none` i `::after`);
  - najechanie na przyciski ☀, EN i ☰;
  - przyciski okładki bez kafelków, z cieniem pod treścią;
  - komentarz „Nocny granat” zamieniony na „Granat z krawędzią (zlecenie 34)”.
- **`src/styles/global.css`:**
  - usunięta druga definicja `--photo`, `--minione-*` i `--footer-*` dla trybu ciemnego. Zostawiłem jedną, w `zalozyciele.css`; ona i tak wygrywała, bo plik ładuje się później;
  - hamburger `.hdr-stopka` dostaje tło przez `var(--burger-tlo, …)`.
- **`src/styles/telefon.css`:**
  - `--znacznik*` z tokenów;
  - usunięty wiersz `--tint-ink: #d3dcea`.
- **`src/styles/tlo.css`:** `--kafel: var(--surface)` i `--kafel-ramka: var(--line)`. Klasa `.side-box` z tej listy nadal jest w zbudowanym HTML, na `/powiadomienia/`.
- **`src/styles/zal-dzialy.css`:**
  - najechanie w pasie `color-mix(in oklab, var(--d-a) 9%, var(--bg))`;
  - pas na komputerze na powierzchni;
  - na telefonie osobne kafelki `--d-kafel`, pole ze stronami w tym samym kolorze, `::before` z `--d-kafel`.
- **`src/styles/zalozyciele-strony.css`:** Szybki dostęp. Tło `--surface`, kreski 1 px `--line`, `h2` z odstępem 18 px, najechanie `--pow-2`.
- **`src/styles/zal-telefon.css`:**
  - hamburger przez `var(--burger-tlo, …)`, dwa miejsca;
  - komentarz.
- **`src/styles/zal-granty-plan.css`:** wybrany semestr i dzień, komputer i telefon.
- **`src/components/zal/ListaPokaz.astro`:** `.lp-uklad` na tokenach.

## Zrzuty (lokalnie, `raport-zrzuty/`)
- **`z34-przed4/`:** przed zmianą, `main` = `cbca5051`.
- **`z34-po4/`:** po zmianie, wersja wypchnięta.
  - Zakres zrzutów: 10 stron × (1536×864 przy skali 1,25 oraz telefon 390×844) × (u góry i po przewinięciu o 45%) × (jasny i ciemny), czyli po 80 zrzutów.
  - Każdy folder ma `pomiary.json` z wartościami wyliczonymi, kontrastem i położeniem przycisków.
- **`z34-porownanie/`:** zrzut wzoru B z artefaktu i mój wynik obok siebie. Pliki: `nauka-pc`, `glowna2-pc`, `plan-pc`, `aktualnosci-pc`, `nauka-przew-tel`, `popularyzacja-przew-tel`, `glowna-tel`.
- **`z34-wzor/`:** zrzuty wzorcowe z artefaktu.
- **Skrypt:** `z34-skrypt/zrzuty34.mjs`.
- **Foldery nieudanych przebiegów:** `z34-przed`, `z34-po`, `z34-przed2`, `z34-przed3`. Zostawione, nieużywane (przyczyna niżej).

## Wynik odbioru
- **Tryb jasny:** 40 z 40 par zrzutów jest identycznych co do piksela (0 różnych pikseli, także przy polu „Szukaj w aktualnościach”). Najechanie w jasnym też bez zmian (pasek, okładka, hamburger telefonu).
- **Wartości wyliczone (ciemny):**
  - `body` ma tło #172032;
  - **`--d-a` / `--d-kafel` na treści strony** (`body`, `.z-dz`) i tło kafelka na telefonie:

    | Dział | `--d-a` | `--d-kafel` |
    |---|---|---|
    | Instytut | #e7b576 | #383b43 |
    | Nauka | #82d3aa | #293e49 |
    | Studia | #77caf5 | #283d53 |
    | Popularyzacja | #f0a4c7 | #3b384c |

    Wszystkie jak w zleceniu.
  - **kreska pod banerem działu:** 2 px, kolor działu z przezroczystością 0,8; cień banera `none`;
  - **pod banerem Aktualności:** 1 px `rgba(201, 208, 222, .38)`;
  - **pas działu na komputerze:** #202a3c;
  - **Szybki dostęp:** tło #202a3c, kreski 1 px #323b4b, `h2` z odstępem 18 px;
  - **wybrany semestr w planie:** odcień 16% koloru działu, tekst #ecf0f7, kreska `inset 0 -2px`.
- **Kontrast (ciemny, 10 stron × 2 ekrany × 2 położenia):**
  - 0 tekstów poniżej progu (4,5 : 1, dla dużych 3 : 1);
  - najsłabszy to 5,84 („2 strony” na kafelku Popularyzacji na telefonie), tyle samo co w prototypie;
  - obrys `--line-ui`: 3,72 : 1 na tle i 3,29 : 1 na powierzchni;
  - kafelki działów na telefonie względem tła: 1,45 (Instytut), 1,46 (Nauka), 1,46 (Studia), 1,44 (Popularyzacja). Dawniej 1,40.
- **Przełączanie motywu:** przyciski na okładce komputera i w nagłówku telefonu mają identyczne położenie przed ☀ i po nim. Sprawdziłem to w obu kierunkach.
- **Najechanie w ciemnym:** tło 12% koloru tekstu i promień 4 px na okładce, na pasku i na hamburgerze telefonu. Na telefonie przez `--burger-tlo`, bez nowego `!important`.
- **Porównanie z wzorem B:**
  - wygląd zgodny: kreska banera, pas na powierzchni, osobne kafelki na telefonie (po poprawce 22:28), Szybki dostęp, plan zajęć, przyciski;
  - różnice w treści wynikają tylko z nowszych danych (aktualności, seminaria, ciekawostki);
  - kolory tekstu na zrzutach pikselowo zgadzają się z tokenami: #ecf0f7 i #d1d6df na #172032. Tekst we wzorze wygląda nieco cieńszy przez inne wygładzanie i kompresję webp.
- **`.z-nagl::after`:** przed zmianą nie był nigdzie używany, także po zleceniach 31–33 (`git grep` na `main`).
- **Kontrole:**
  - `npm run check`: 0 błędów, 0 ostrzeżeń, 3 wskazówki (jak przed zmianą);
  - `npm run test:jawne`: 47/47;
  - konsola: 0 błędów w obu przebiegach.

## Spostrzeżenie: baner granatowy ma własną paletę
- Pas `.ph-granat` (baner działu) ustawia u siebie `--ink: #fff` i `--surface: rgb(255 255 255 / .08)`. Ma też `data-dzial`, więc wewnątrz banera `--d-a` i `--d-kafel` liczą się z jego palety: Nauka w banerze #86d6ab zamiast #82d3aa.
- Nic w banerze nie korzysta dziś z tych zmiennych. Na komputerze nad dolną krawędzią banera jest 0 różnych pikseli między „przed” i „po”, a na telefonie w nagłówku zmienia się tylko hamburger bez kółka.
- Zostawiłem wzór ze zlecenia (`var(--ink)`, `var(--surface)`). Wewnątrz banera taki wynik jest spójny z jego jasną paletą.

## Decyzje przyjęte samodzielnie
- **Domyślne ze zlecenia:**
  - pasek przycisków i Szybki dostęp zmieniają się tylko w ciemnym;
  - kolejność przycisków na telefonie bez zmian (EN, ☀, ☰), odstępy na okładce bez zmian.
- **Hamburger telefonu bez kółka przez zmienną `--burger-tlo`:** zmienna ma wartość `transparent` tylko w ciemnym i jest używana w trzech regułach, które już miały `!important`. Przyjąłem to, bo zlecenie prosi, żeby nie dokładać nowych `!important`, jeśli się da.
- **Najechanie na hamburger telefonu również przez `--burger-tlo`:** z tego samego powodu.
- **Stopka:** dzisiejsza stopka `.z-stopka` ma tło z `--granat`, nie z `--footer-bg`. Nowe `--footer-*` działają tylko w starszych miejscach (`.hdr-stopka`, `.ftr-main`), ale zostały dopisane, bo tak każe zlecenie.
- **Promień przy najechaniu:** przycisk okładki ma w spoczynku promień 6 px, a przy najechaniu 4 px, jak w zleceniu. W spoczynku i tak nie ma tła, więc promień 6 px nie jest widoczny.

## Uwagi o skrypcie zrzutów
Pierwsze przebiegi przerywały się przy teście przycisków okładki. Po wejściu na drugi ekran strona zapamiętuje pominięcie okładki (`html.bez-okladki`), więc przyciski okładki miały rozmiar 0. To zamierzone zachowanie strony, nie błąd. Test przycisków działa teraz w świeżym kontekście przeglądarki.

## Kryteria odbioru
- [x] Tokeny ciemnego motywu jak w tabeli. Kolory działów i `--d-kafel` liczone z `color-mix`, bez kolorów wpisanych na sztywno w `ListaPokaz.astro`, `.akt-wydarzenie` i `zal-dzialy.css`.
- [x] Baner kończy się kreską 2 px w kolorze działu (granatowe banery: 1 px jasna linia), bez szarej kreski. Dotyczy komputera i telefonu.
- [x] Pas działu na komputerze leży na powierzchni. Na telefonie są osobne kafelki z odcieniem działu, nie jeden pas.
- [x] Szybki dostęp bez grubej kreski, na powierzchni.
- [x] Przyciski na okładce bez kafelków, hamburger na telefonie bez kółka. Nic nie przeskakuje po przełączeniu motywu.
- [x] Plan zajęć: wybrany semestr i dzień z odcieniem i kreską zamiast jaskrawego wypełnienia.
- [x] Wszystkie teksty ≥ AA w ciemnym. Tryb jasny bez zmian (zrzuty identyczne).

## Pytania do właściciela
- Brak nowych. Otwarte zostaje pytanie ze zlecenia, który pasek przycisków miałeś na myśli. Na razie oba wyglądają jak w prototypie, tylko w ciemnym.

## Do sprawdzenia
- **Na Podglądzie, w trybie ciemnym, na swoim ekranie:**
  - strona działu, czyli kreska pod banerem i pas;
  - druga część strony głównej (Szybki dostęp);
  - plan zajęć;
  - telefon: kafelki grup i hamburger bez kółka.
