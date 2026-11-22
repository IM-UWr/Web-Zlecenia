# Zlecenie 48: przełącznik „Opublikowane” także w seminariach, referatach i aktualnościach (18.11.2026)

**Decyzja właściciela (18.11, 19:38–19:39):** „Seminaria, referaty, aktualności powinny je mieć”, jako osobne zlecenie.
- To zmiana decyzji z 7.11 („seminaria bez przełącznika, mają być jak najprostsze”). Prostota zostaje: przełącznik jest domyślnie włączony, więc redaktor seminarium nie musi go dotykać.
- Reszta jak w zleceniu 33:
  - Podgląd pokazuje wszystko i oznacza szkice;
  - szkice znikają dopiero w budowie publicznej (`TYLKO_OPUBLIKOWANE=1`);
  - Core zostaje zamrożony, a flagi nigdzie nie ustawiaj.

**Wymaga zlecenia 33** (`widoczny()`, etykieta „szkic”, żółty pasek, wiersz B4 na plakietce, ściągawka). Na początku sprawdź, że 33 jest na `main` Web-Core. Jeśli nie jest, **STOP** i napisz to w raporcie.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela. Raport `RAPORT-ZLECENIE-48.md`, zrzuty `raport-zrzuty/z48-*`. Bez subagentów.
- **Kolejka:** okno 1, po zleceniu 42. Nie uruchamiaj go równolegle z 40 ani z 42, bo zmieniają te same formularze (`.pages.yml` seminariów i Web-Aktualnosci).
- **Ochrona zmian redaktorów:** jak w zleceniu 33 (sekcja o tej samej nazwie). W skrócie:
  - zawsze od świeżego `main`, zwykły commit, bez force-push;
  - baza = HEAD zanotowany na początku pracy, osobno w każdym repozytorium;
  - tuż przed pushem `git fetch` i `git log <baza>..origin/main`. Jeśli przybyły zapisy redaktorów, uruchom dopisanie pola jeszcze raz na świeżym `main`. Nie doklejaj starego wyniku;
  - kontrola pole po polu przed pushem i po nim, wynik w raporcie;
  - push wieczorem albo po wiadomości właściciela do redaktorów („zapiszcie i zamknijcie CMS na 15 minut”). Dotyczy to też redaktorów wszystkich 9 seminariów;
  - następnego dnia przegląd zapisów redaktorów z 24 godzin. Formularz otwarty przed pushem i zapisany po nim wytnie `opublikowany: true`. To nieszkodliwe (brak pola = opublikowane), ale podaj w raporcie, ile takich zapisów było.
- **Kolejność pushy:** Web-Core → Web-Aktualnosci → 9 × Web-Sem-* (jednym skryptem). Web-Core może iść pierwszy, bo nadmiarowe pole w pliku nie psuje budowy.

## Stan dziś (17.11, z inwentaryzacji do zleceń 33 i 40; sprawdź na `main`)
- **Web-Sem-* (9 repozytoriów, jeden układ):** formularze „Opis seminarium” (jeden plik) i „Referaty” (kolekcja), `.pages.yml` ok. 167 linii. Po zleceniu 40, etap 5, formularz ma wspólny wzór wdrażany skryptem.
- **Web-Aktualnosci:** aktualności (w tym „Rodzaj: Kariera”), obrony doktorskie i „Strony”. „Strony” mają już przełącznik ze zlecenia 33.
- **Kod:** lista filtrów `opublikowany` z 33 (A1) nie obejmowała aktualności, referatów ani opisów seminariów. Sprawdź, czy schematy tych kolekcji mają już pole `published` / `opublikowany`.

## Zakres

| Repozytorium | Formularz | Co szkic ukrywa w budowie publicznej |
|---|---|---|
| Web-Sem-* (9) | Opis seminarium | Stronę seminarium. Pozycję na liście seminariów, w menu, w Szybkim dostępie i w Kalendarzu. Linki z kierunków i specjalności (pola „seminaria”). Pośrednio **wszystkie referaty tego seminarium**. |
| Web-Sem-* (9) | Referaty | Stronę referatu (jeśli jest). Pozycję w zapowiedziach i w archiwum seminarium, w „Najbliższych seminariach” na stronie głównej, w Kalendarzu i w plikach `.ics`. Referat nie wchodzi do liczb („zapowiedziane referaty”, „referaty w archiwum”). |
| Web-Aktualnosci | Aktualności (także „Rodzaj: Kariera”) | Stronę wpisu. Pozycję na liście Aktualności (z filtrami) i w kolumnie na stronie głównej (także w „Ostatnio” ze zlecenia 35), w „Nadchodzących wydarzeniach”, w Kalendarzu i w `.ics` (gdy wpis ma „Termin wydarzenia”), na podstronie Kariera (zlecenie 44) i w „Aktualnościach dla studentów” na stronie Studiów. Wpis nie wchodzi do liczby na okładce, liczby w ramce Kariery ani liczb w banerach. |

Szkic znika też wszędzie poza tabelą: z mapy strony, z wyszukiwarki (Pagefind) i z RSS (jeśli jest).

**Bez przełącznika** (bez zmian): obrony doktorskie, pracownicy i zakłady. O „Warto wiedzieć” decyduje zlecenie 47.

## 1. Web-Core
1. **Schemat.** Pole `opublikowany` w kolekcjach referatów, opisów seminariów i aktualności, tak samo jak w 33 (`published` w `src/content.config.ts`: brak pola = opublikowane).
2. **Filtr w jednym miejscu.** Szkice odfiltruj przez `widoczny()` z 33 tam, gdzie kod wczytuje te kolekcje (wspólne funkcje w `src/lib/tresci.ts` i podobnych), a nie osobno w każdym widoku. Widoki dodane później (np. Kariera z 44, jeśli powstanie po tym zleceniu) dostaną wtedy filtr bez zmian.
   - Referaty seminarium, które jest szkicem, ukryj razem z nim (ukrycie pośrednie, jak w B4 zlecenia 33).
   - Zawsze powiększony jest pierwszy **widoczny** wpis Aktualności, czyli w budowie publicznej najnowszy opublikowany.
   - Wszystkie liczby licz po filtrze: banery, okładka, ramka Kariery, „Zobacz więcej (N)”.
   - Lista miejsc, w których działa filtr: do raportu.
3. **Oznaczenie szkicu na Podglądzie** (jak w 33, A2.2 i B4):
   - etykieta „szkic” / „draft” przy pozycji na listach, w kolumnach strony głównej, w Kalendarzu i na liście seminariów;
   - na stronie aktualności, referatu i seminarium: żółty pasek na górze i żółty wiersz na plakietce;
   - link „Włącz »Opublikowane« w CMS →” prowadzi do formularza tego wpisu. Przy referacie seminarium, które jest szkicem, prowadzi do formularza opisu seminarium. Opis seminarium to formularz jednego pliku, więc sprawdź, jaki adres ma taki formularz w Pages CMS (inny niż `…/collection/…/edit/…`).
4. **Linki w treści do szkiców.** W budowie z flagą wypisz w logu ostrzeżenie przy każdym linku w treści (Markdown), który prowadzi do strony, której nie będzie, np. link ze strony Pierwszy rok do szkicu aktualności. Nie usuwaj tych linków automatycznie. Lista do raportu.

## 2. Formularze
- **Pole `opublikowany`** (boolean):
  - Web-Sem-* (9): „Opis seminarium” i „Referaty”. Zmień wspólny wzór formularza (zlecenie 40, etap 5) i wdróż go skryptem we wszystkich 9 repozytoriach naraz, identycznie;
  - Web-Aktualnosci: „Aktualności”.
- **Ustawienia pola** jak w 33:
  - etykieta: „Opublikowane — widoczne na stronie publicznej (na Podglądzie widać zawsze)”;
  - pole stoi zaraz pod tytułem;
  - `default: true`.
- **Opisy pola:**
  - opis seminarium: „Odznacz, żeby przygotować seminarium bez pokazywania go na stronie publicznej (szkic). Razem z nim znikną wszystkie jego referaty.”;
  - referat: „Odznacz, żeby przygotować referat bez pokazywania go na stronie publicznej (szkic).”;
  - aktualność: „Odznacz, żeby przygotować wpis bez pokazywania go na stronie publicznej (szkic).”
- **Istniejące wpisy: jawna wartość**, jak w 33 (A2.4):
  - jeden commit na repozytorium;
  - `opublikowany: true` tylko w plikach bez tego pola. Istniejących wartości nie ruszaj;
  - dopisanie powtórz na świeżym `main` tuż przed pushem;
  - w raporcie podaj liczbę zmienionych plików w każdym repozytorium.
- **Ściągawka** (`dok/sciagawka-edytora.md`): reguła z 33 dotyczy teraz także aktualności, referatów i seminariów. Dopisz zdanie: „Odznaczenie »Opublikowane« w opisie seminarium ukrywa całe seminarium razem z referatami”.
- **Kontrola:** `sprawdz_pola_cms.py` daje 0 problemów.

## Odbiór lokalny
- **Wpisy testowe ustawione na szkic:**
  - jedna aktualność z „Terminem wydarzenia”;
  - jedna oferta „Kariera” (jeśli zlecenie 44 jest zrobione);
  - jeden zapowiedziany referat;
  - jedno seminarium z referatami.
- **Bez flagi:** porównanie wszystkich stron przed i po. Bez różnic poza etykietą „szkic” przy wpisach testowych.
- **Z `TYLKO_OPUBLIKOWANE=1`:**
  - każdy wpis testowy znika ze wszystkich miejsc z tabeli „Zakres”, a razem z seminarium testowym znikają jego referaty;
  - liczby się zgadzają;
  - powiększona jest najnowsza opublikowana aktualność;
  - w logu są ostrzeżenia o linkach do szkiców.
- **Symulacja zapisu w CMS** (jak w zleceniu 28, etap 6a), dla aktualności, referatu i opisu seminarium:
  - stary wpis otwarty i zapisany bez zmian zostaje opublikowany;
  - nowy wpis startuje jako opublikowany;
  - po odznaczeniu wpis staje się szkicem.
- **Plakietka B4:** żółty wiersz z działającym linkiem na stronie aktualności, która jest szkicem, na stronie referatu, który jest szkicem, i na stronie referatu seminarium, które jest szkicem.
- **Zrzuty:** lista Aktualności i strona seminarium z etykietą „szkic”, na komputerze i telefonie, w trybie jasnym i ciemnym.
- **Kontrole:** `astro check` bez nowych błędów, konsola czysta.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Przełącznik „Opublikowane” jest w opisie seminarium i w referatach wszystkich 9 seminariów oraz w aktualnościach, z tą samą etykietą co w 33. Każdy formularz ma właściwy opis.
- [ ] Nowe wpisy są domyślnie opublikowane. Istniejące mają jawne `opublikowany: true` i żaden nie zmienił się w szkic.
- [ ] Podgląd pokazuje wszystko i oznacza szkice (etykieta, żółty pasek, wiersz na plakietce z linkiem do właściwego formularza).
- [ ] Flaga `TYLKO_OPUBLIKOWANE` ukrywa szkice we wszystkich miejscach z tabeli „Zakres”, razem z referatami seminarium, które jest szkicem. Liczby liczone są po filtrze.
- [ ] Filtr działa w jednym miejscu (przy wczytywaniu kolekcji), nie w każdym widoku osobno.
- [ ] Linki w treści do szkiców dają ostrzeżenie w budowie z flagą.
- [ ] Core nadal zamrożony; flaga nigdzie nie ustawiona.
- [ ] Kontrola zmian redaktorów przed i po pushu jest w raporcie: wszystkie zapisy redaktorów zachowane. Przegląd z następnego dnia zrobiony.
