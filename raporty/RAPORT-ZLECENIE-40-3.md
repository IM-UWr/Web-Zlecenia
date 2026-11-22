# Raport: zlecenie 40, etap 3 — Web-Aktualnosci (18.11.2026)

## Stan
- **Zrobione i wypchnięte** (Twoja decyzja 18.11: „Przygotuj teraz” — przygotować i wypchnąć zaraz po zleceniu 44 z drugiego okna). Zlecenie 44 było już na `main` (`422bb59`, push drugiej sesji ok. 17:32), więc etap 3 poszedł od razu po przygotowaniu.
- **Web-Core:** `5131ebf2..0951f7b4` (tylko skrypt formularzy; strona bez zmian), potem dokumentacja `0951f7b4..02a2e8aa` (tylko `dok/`). **Podgląd zielony**: przebieg 44353459620 zbudował stronę z `0951f7b4`.
- **Web-Aktualnosci: wypchnięte `422bb59..56caf58`** o 18:03 — migracja zrobiona od nowa na `main` z 44, objęła też `kariera.md`. Wynik w „Push”.
- **Dokumentacja i PDF „Mapa CMS”:** `dok/jawny-markdown.md`, `dok/sciagawka-edytora.md` i źródło PDF bez wyjątku „Strony Aktualności w dawnym formacie”, z Karierą i szablonami aktualności i obrony (`02a2e8aa`); PDF w Web-Podglad `da76859..5b4e8f2` (`[skip ci]`, 2 strony).
- **Baza** (świeży `main` na początku pracy, 17:35): `46d7f90`. Zapisów redaktorów od bazy: 0.

## Co zrobiłem

### Web-Core (tylko skrypt)
`skrypty/migracja/formularze_40.mjs`, nowa funkcja `aktualnosci()`. Działa na `.pages.yml` sprzed zlecenia 44 i po nim: 44 dodaje grupę „Termin zgłoszeń” (`zgloszenia`) za terminem wydarzenia, opis pola „Rodzaj” i `kariera.md` w opisie Stron. Każde inne nowe pole zatrzymuje skrypt (sprawdzenie kolejności).

### Web-Aktualnosci (jeden commit: `.pages.yml` i Strony)
- **Strony → jawny Markdown:** `aktualnosci.md` i `obrony-doktorskie.md` (po 44 także `kariera.md`) dostają `format_tresci: jawne` i komentarz `<!-- UKŁAD JAWNY: … -->` na początku Treści (i Treści EN, gdy jest). Nagłówków `##` nie ma, więc `{#id}` niepotrzebne. Tekst bez zmian.
- **Formularze** (zatwierdzony projekt z raportu 40-0 i decyzja 18.11 o kolejności we wpisach):

| Formularz | Kolejność | Inne zmiany |
|---|---|---|
| Aktualności | tytuł, **tytuł EN** → data, rodzaj, termin wydarzenia (po 44: termin zgłoszeń) → Treść, Treść EN → zajawka, **zajawka EN** → reszta (dziś tytuł EN i zajawka EN były na samym dole) | opis formularza; ściągawka zwykłego Markdownu przy Treści; **szablon Treści** nowej aktualności; etykiety „… EN” |
| Obrony doktorskie | bez zmian (kandydat, tytuł rozprawy, termin, miejsce → Treść, Treść EN → reszta) | opis formularza; ściągawka; **szablon Treści** nowej obrony; poprawiony opis Treści EN; etykiety „… EN” |
| Strony | tytuł, tytuł EN, Opublikowane → Treść, Treść EN → opis, hasła, liczby, prawy pasek | ściągawka jawnego Markdownu („Strona z listą: tekst stoi nad listą; pusta Treść albo sam komentarz = sama lista”); ukryte `format_tresci` i dawne „Bloki wzorca”; „Krótki opis (Google i podgląd linku)” z przykładem; etykiety „… EN” |

Szablony (brzmienie z raportu 40-0, sekcja 4):
- aktualność: `<!-- TEKST: Zwykły tekst. Akapity oddziela pusta linia. Pliki: wgraj w „Media” i wklej link. -->` + `<!-- Rejestracja, program, plakat: wstaw link w osobnej linii. -->`;
- obrona: `<!-- Zostaw puste, a strona sama napisze zaproszenie. Własny tekst zastępuje zaproszenie. -->`.

Istniejące wpisy: wszystkie 167 aktualności mają Treść, więc CMS nie wstawi im szablonu. Żadna z 5 obron nie ma Treści, więc przy pierwszym zapisie obrony CMS dopisze komentarz szablonu. Strona traktuje taki komentarz jak pustą Treść (`maTresc()`, etap 1) i pokazuje zaproszenie jak dotąd (sprawdzone niżej).

## Kontrole
- **Porównanie HTML całej strony** (kod `origin/main`, dane Web-Aktualnosci `46d7f90` → `f91eac2`): **0 różnic** w 925 plikach (PL i EN). Zrzutów nie robiłem, bo nie było różnic.
- **Szablony Treści** (dwie budowy całej strony z trzema wpisami testowymi — aktualność, oferta „Kariera”, obrona — raz z pustą Treścią, raz z samym szablonem; Treść EN pusta):
  - różnią się tylko 4 pliki z 932: strony testowej aktualności i oferty (PL i EN), i to wyłącznie niewidocznym komentarzem w pustym bloku tekstu w źródle HTML;
  - obrona: strony identyczne, zaproszenie złożone z danych zostaje (PL i EN);
  - listy Aktualności i Kariery, strona główna, kalendarz, RSS i indeks wyszukiwarki: bez różnic.
- `sprawdz_pola_cms.py`: **0 problemów** (725 plików, 16 repozytoriów, Web-Aktualnosci z klonu roboczego).
- `sprawdz-jawny-markdown.mjs`: **OK** (2 pliki, bez nagłówków `##`).
- `kontrola_redaktorow.py`: `przed` — 0 zapisów od bazy; `po` (`46d7f90` → `f91eac2`): zmienione tylko `body` (2), `tresc_en` (1), `format_tresci` (2) i `.pages.yml` — „OK, tylko zmiany z migracji”.
- **Próba na wersji po zleceniu 44** (kopia commitu `422bb59` z klonu drugiej sesji, tylko odczyt): migracja przeniosła też `kariera.md`; formularze z grupą „Termin zgłoszeń” na miejscu (za terminem wydarzenia), opis pola „Rodzaj” ze zlecenia 44 został; drugi przebieg skryptu: „Bez zmian”; `sprawdz-jawny-markdown`: OK (3 pliki).

## Przyjąłem sam (zlecenie przewiduje domyślne albo moją rekomendację)
- **Opis formularza Aktualności uzupełniony o oferty.** Zatwierdzone brzmienie mówiło, że wszystkie wpisy widać w Aktualnościach i na stronie głównej. Od zlecenia 44 oferty („Kariera”) są na stronie Kariera i na stronie Studiów, a nie na liście Aktualności. Opis mówi więc: „…Ogłoszenia, wydarzenia i sukcesy widać w Aktualnościach i na stronie głównej; wydarzenie z terminem trafia też do kalendarza. Oferty (rodzaj „Kariera”) są na stronie Kariera i na stronie Studiów.”
- **Opis Treści EN obrony poprawiony.** Dotychczasowy mówił, że pusta Treść EN pokaże „albo opis po polsku, gdy jest”. Strona angielska bierze jednak tylko Treść EN, a bez niej zaproszenie złożone z danych (`src/lib/widoki/obrona.ts`), nigdy polski opis. Nowy opis mówi to wprost.
- **Etykiety „EN: …” → „… EN”** we wszystkich trzech formularzach, jak w Studiach i Ustawieniach (wzorzec zlecenia: „pola EN pod polskimi, z dopiskiem EN”).
- **Push po 44, a nie przed nim** (Twoja decyzja), więc ta sama migracja obejmie `kariera.md`, a druga sesja nie trafi na konflikt w formularzach.

## Pytania do Ciebie
Brak nowych.

## Push
Skrypt `push40_aktualnosci.sh` w scratchpadzie. Czeka, aż na `main` Web-Aktualnosci pojawi się commit zlecenia 44, i wtedy:
1. sprawdza, że część Web-Core etapu 3 jest na `main`, i przewija lokalny Web-Core do `origin/main` (porównanie HTML na kodzie z `main`);
2. robi migrację od nowa na świeżym `main` (nowa gałąź, oba skrypty, commit z tym samym opisem) i sprawdza, że drugi przebieg skryptu formularzy nic nie zmienia;
3. kontrole (każda = STOP): `sprawdz-jawny-markdown`, `sprawdz_pola_cms.py`, kontrola redaktorów `przed` (baza = commit zlecenia 44 na `main`), porównanie całego repozytorium pole po polu `origin/main` → wynik (tylko zmiany z migracji), porównanie HTML całej strony (0 różnic);
4. push zwykły, bez force; kontrola po pushu; potem sprawdzę Podgląd.

Baza kontroli = commit zlecenia 44: zapisy redaktorów sprzed niego sprawdziła kontrola pushu 44, a wszystkie wartości z `main` i tak porównuje krok „całe repozytorium pole po polu” przed pushem.

**Wynik (18.11, 18:01–18:04):**
- pierwsze uruchomienie (18:00) zatrzymało się przed czymkolwiek na warunku „niezatwierdzone zmiany w Web-Core”: liczył się nieśledzony plik `skrypty/test-edytora/package-lock.json` (nie mój, był od początku). Poprawka: `--untracked-files=no`, jak wcześniej w `naglowek40b.sh`;
- Podgląd po 44: przebieg 44353459620 zielony, zbudowany z `422bb59`;
- migracja od nowa na `422bb59` → `56caf58`: 3 Strony (`aktualnosci`, `kariera`, `obrony-doktorskie`) i `.pages.yml`; drugi przebieg skryptu formularzy: „Bez zmian”;
- `sprawdz-jawny-markdown`: OK (3 pliki); `sprawdz_pola_cms.py`: 0 problemów (726 plików);
- kontrola redaktorów `przed` (baza `422bb59`): 0 zapisów; całe repozytorium `422bb59` → `56caf58` pole po polu: zmienione tylko `body` (3), `format_tresci` (3), `tresc_en` (1) i `.pages.yml` — „OK, tylko zmiany z migracji”;
- porównanie HTML całej strony: **0 różnic** w 925 plikach (z `/aktualnosci/kariera`);
- **wypchnięte `422bb59..56caf58`**; kontrola po pushu: OK;
- Podgląd: **zielony** — przebieg 44354449898 zbudował stronę z `56caf58`.

## Następnego dnia (19.11)
- Test w CMS z Tobą: Aktualności (otwarcie istniejącego wpisu, zapis bez zmian; nowa aktualność z szablonem), Obrony (otwarcie istniejącej obrony wstawi szablon; zapis z samym szablonem — zaproszenie zostaje), Strony → Aktualności, Kariera, Obrony doktorskie (zapis bez zmian).
- Przegląd zapisów redaktorów z 24 h po pushu: czy żaden formularz otwarty przed pushem nie usunął `format_tresci`.
