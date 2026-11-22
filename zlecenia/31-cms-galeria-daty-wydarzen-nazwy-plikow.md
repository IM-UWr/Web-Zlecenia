# Zlecenie 31: termin wydarzenia „na kliknięcie”, czerwony komunikat przy pozycji bez zdjęcia, pusta pozycja nie wywraca strony, nazwy plików z tytułu (17.11.2026)

**Skąd to zlecenie.** 16.11 wieczorem redaktor (Grzegorz Karch) dodał w CMS trzy aktualności i wyszły trzy problemy:
1. **Pusta pozycja galerii wywróciła budowę.**
   - W „Medale Uniwersytetu dla profesorów Bożejki i Rolskiego” (`Web-Aktualnosci/src/content/aktualnosci/2026-11-16--2.md`) kliknął „dodaj” w galerii, ale nie wybrał zdjęcia (`galeria: - {}`).
   - Każda budowa Podglądu kończyła się błędem `[InvalidContentEntryDataError] aktualnosci → 2026-11-16--2 … galeria.0.plik: Required`.
   - Właściciel usunął pozycję ręcznie 17.11, 14:50 (commit `c224fd6`).
2. **CMS sam wpisuje daty wydarzenia.** Pages CMS wstawia do pustego pola daty „teraz”, w nowym wpisie i przy otwieraniu starego wpisu (szczegóły w etapie 2). Zwykłe newsy stają się wydarzeniami, które od razu „mijają”, więc znikają ze strony głównej.
3. **Nazwy plików bez tytułu:** `2026-11-16-.md`, `--1`, `--2`.

**Decyzje właściciela (17.11):**
- 14:51: „Dobra, dodaj zlecenie”.
- 15:11: **wariant A**. Termin wydarzenia nie jest polem widocznym zawsze, tylko grupą, którą redaktor dodaje jednym kliknięciem.
  - Bez kliknięcia wpis jest zwykłą, bezterminową aktualnością.
  - Po kliknięciu pojawiają się pola terminu z opisem, że służą do Kalendarza, „Nadchodzących wydarzeń” i Szybkiego dostępu.
  - Prawdziwy przełącznik pokazujący pola jest niemożliwy, bo Pages CMS nie ma pól warunkowych (sprawdzone w kodzie: tylko `hidden` na stałe).
- 15:12: redaktor, który doda pozycję galerii bez zdjęcia, ma **dostać czerwony komunikat i nie móc zapisać**.

**Zasada nadrzędna:** strona ma być bezobsługowa. Formularz łapie błędy redaktora, zanim trafią do pliku, a gdy coś jednak przejdzie, strona to pomija i nie przerywa budowy.

**Gdzie:** Web-Core i klony repozytoriów treści: Web-Aktualnosci oraz wszystkie inne z `tresci.json` (przegląd `.pages.yml` w etapach 1, 3 i 4).

**Zasady pracy** (jak w `.przekazanie\zlecenia\zasady.md`, sekcja „Jedna gałąź `main`”):
- Pracuj na lokalnej gałęzi roboczej. Na `main` wypychasz dopiero po słowie „push” właściciela.
- **Od 9.11 redaktorzy edytują na żywo przez CMS** (każdy zapis to commit na `main` repozytorium treści). Zmiany w repozytoriach treści:
  - zawsze od świeżego `main`;
  - zwykły commit i zwykły push, **nigdy force-push i nigdy nadpisywanie `main` kopią**;
  - odrzucony push → `git pull --rebase` i powtórka;
  - `.pages.yml` i pliki danych jednego repozytorium w jednym commicie.
- Kolejność przy pushu: najpierw Web-Core (schemat czyta i stary, i nowy zapis terminu, patrz etap 2), potem repozytoria treści.
- Raport `RAPORT-ZLECENIE-31.md`, zrzuty `raport-zrzuty/z31-*`. Bez subagentów.

## Ochrona zmian redaktorów (obowiązkowo przy każdym pushu do repozytorium treści)
Redaktorzy zapisują w CMS na żywo, także w trakcie tego zlecenia. Ich zmiany nie mogą zginąć.

1. **Migracja na najświeższej wersji.**
   - Tuż przed pushem zrób `git fetch` i sprawdź, czy na `main` przybyły zapisy redaktorów od chwili, gdy zacząłeś (`git log <baza>..origin/main`).
   - Jeśli przybyły, nie doklejaj starego wyniku migracji. Przełącz się na świeży `main` i **uruchom skrypt migracji jeszcze raz** na aktualnych plikach.
   - Konflikty rozwiązuj ręcznie: weź wersję redaktora i nanieś na nią swoją zmianę. Nigdy odwrotnie i nigdy hurtem całych plików (`-X ours`, `checkout --ours/--theirs`).
2. **Kontrola przed pushem** (skrypt, wynik w raporcie):
   - weź każdy zapis redaktora od bazy (autor inny niż Code) i każdy plik, który zmienił;
   - porównaj pole po polu jego wersję z wersją, którą wypychasz;
   - każda wartość wpisana przez redaktora musi być w wyniku: bez zmian albo przeniesiona zgodnie z migracją (np. `wydarzenie_poczatek` → `termin`). Inaczej **STOP**.
3. **Kontrola po pushu:** porównanie pole po polu całego repozytorium przed i po. Różnice są dozwolone tylko w polach zmienianych celowo; ich lista trafia do raportu.
4. **Okno pusha:** wieczorem albo po wiadomości od właściciela do redaktorów: „zapiszcie i zamknijcie CMS na 15 minut, potem odświeżcie stronę”.
   - Pages CMS przy zapisie sprawdza wersję pliku. Jeśli plik zmienił się od otwarcia formularza, zapis jest odrzucony („File has changed since you last loaded it”), więc nic nie zostaje nadpisane. Redaktor traci jednak to, co wpisał, a nie zapisał.
   - Formularz otwarty przed pushem i zapisany po nim działa jeszcze według starej konfiguracji, a stara konfiguracja aktualności wstawiała daty wydarzenia „teraz”.
   - Dlatego **następnego dnia** przejrzyj zapisy redaktorów z 24 godzin po pushu: czy żaden nie przywrócił starych pól (`wydarzenie_*`) ani nie usunął nowych. Znalezione popraw osobnym commitem.
5. **Wszystko da się odwrócić:** każdy zapis redaktora to osobny commit. W razie straty przywróć wartość z historii **nowym commitem** (nigdy `reset` ani force-push) i opisz to w raporcie.

## Etap 0. Stan
- Świeże klony wszystkich repozytoriów treści (`main`). Zanotuj w raporcie HEAD każdego z nich (to jest **baza** do kontroli z sekcji „Ochrona zmian redaktorów”) i zapisy redaktorów od 16.11 (`git log --since=2026-11-16`).
- Czy budowa na obecnym `main` przechodzi? Jeśli nie, stop i raport.
- Czy właściciel dopisał już ręcznie `default: ""` przy `wydarzenie_poczatek` / `wydarzenie_koniec` albo poprawił daty w trzech wpisach z 16.11? Uwzględnij to w migracji.
- Przegląd: czy jakiś stary wpis zapisany po 17.11, 15:05 dostał daty wydarzenia równe chwili zapisu (stan z 15:05: nie, tylko trzy nowe wpisy z 16.11). Wynik do raportu.
- Zbuduj stronę „przed” do porównania w etapie 4.

## Etap 1. Pozycje list: czerwony komunikat w CMS i bezpieczna strona

### 1a. Czerwony komunikat w CMS
**Problem:** samo `required: true` na podpolu nie wystarczy.
- Pages CMS uznaje całkiem pustą pozycję listy (np. `{}` po kliknięciu „Add an item”) za nieistniejącą i jej nie sprawdza, a i tak zapisuje ją do pliku.
- Dzieje się tak w `lib/schema.ts`: `buildSchemaObject` dla nieobowiązkowego obiektu robi `preprocess(isEffectivelyEmpty → undefined)`.
- `required` na całej liście też odpada, bo wymusza co najmniej jedną pozycję.

**Rozwiązanie (wynika z kodu, potwierdź testem):** w każdej liście obiektów z wymaganym podpolem dodaj ukryte pole techniczne typu boolean:

```yaml
    - name: pozycja
      type: boolean
      hidden: true
```

Dlaczego to działa:
- Boolean ma domyślnie `false`, a `isEffectivelyEmpty` traktuje `false` jako wartość („Booleans … are meaningful”).
- Dodana pozycja przestaje więc być „pusta” i CMS sprawdza ją w całości: puste wymagane pole dostaje czerwone „This field is required” i zapis jest zablokowany.
- Ukryte pola są w schemacie walidacji (`generateZodSchema(fields)` bez `ignoreHidden`).
- W pliku pojawi się `pozycja: false`; strona to pole ignoruje.

Gdzie:
- **Web-Aktualnosci, `galeria`:** `plik` → `required: true`, pole `pozycja`, opis pod „Zdjęcie”: *„Wymagane. Jeśli nie chcesz zdjęcia, usuń tę pozycję ikoną kosza.”* Komunikatu błędu przy polu obrazka nie da się zmienić na polski; opis to nadrabia.
- **Web-Aktualnosci, `zalaczniki`:** tak samo dla pliku.
- **`termin` z etapu 2:** tak samo dla `dzien`.
- **Inne listy obiektów** z podpolem, bez którego pozycja nie ma sensu: znajdź w przeglądzie wszystkich `.pages.yml` i wypisz w raporcie z decyzją.
- **Widoczność błędu:** `galeria` ma `collapsible: collapsed: true`. Sprawdź, czy błąd w zwiniętej pozycji jest widoczny. Jeśli nie, ustaw `collapsed: false` dla list, w których jest pole wymagane.

### 1b. Strona pomija puste pozycje (siatka bezpieczeństwa)
Na wypadek, gdyby coś jednak przeszło (zmiana na GitHubie, inna wersja CMS):
- **Web-Core, `src/content.config.ts`:** `galeria` (linia 53) i każde pole-lista obiektów z wymaganym podpolem (m.in. `zalaczniki` / `plikList`, `termin`). Przed walidacją odfiltruj pozycje bez niepustego wymaganego podpola. Użyj jednej funkcji pomocniczej.
- Każda pominięta pozycja daje **ostrzeżenie w logu budowy** (plik, pole, numer pozycji), a nie błąd.
- `sprawdz_tresci.py`: ostrzeżenie przy pustej pozycji listy.

**Test:** tymczasowe kopie wpisu z `galeria:\n  - {}` (jak w commicie `8b59493`) i z pozycją z samym podpisem. Budowa przechodzi, wpis jest bez galerii, ostrzeżenie w logu. Kopie potem usuń.

## Etap 2. Termin wydarzenia „na kliknięcie” (wariant A)

### 2a. Formularz (Web-Aktualnosci `.pages.yml`)
- Pola `wydarzenie_poczatek`, `wydarzenie_koniec` i `wydarzenie_miejsce` znikają z formularza.
- Zamiast nich jest grupa `termin`: lista obiektów, najwyżej 1 pozycja; po dodaniu przycisk „Add an item” znika.
- Grupa stoi **zaraz pod „Rodzaj”**, żeby redaktor, który wybiera „Wydarzenie”, od razu ją widział.

```yaml
  - name: termin
    label: Termin wydarzenia
    description: >-
      Tylko jeśli wpis zapowiada wydarzenie (kliknij „Add an item”). Termin trafia do Kalendarza,
      do „Nadchodzących wydarzeń” i do Szybkiego dostępu na stronie głównej, a po jego końcu
      wpis znika z Aktualności na stronie głównej. Dzień, którego dotyczy zwykła informacja
      (np. dzień wręczenia medalu), wpisz w polu „Data”, nie tutaj.
    type: object
    list:
      max: 1
    fields:
    - name: dzien
      label: Dzień
      type: date
      required: true
      default: ""
    - name: godzina
      label: Godzina rozpoczęcia (np. 13:00; puste = cały dzień)
      type: string
      pattern:
        regex: '^(|([01]?[0-9]|2[0-3])[:.][0-5][0-9])$'
        message: Wpisz godzinę w formacie 13:00
    - name: dzien_konca
      label: Dzień zakończenia (tylko wydarzenia wielodniowe)
      type: date
      default: ""
    - name: godzina_konca
      label: Godzina zakończenia (puste = 2 godziny po rozpoczęciu)
      type: string
      pattern:
        regex: '^(|([01]?[0-9]|2[0-3])[:.][0-5][0-9])$'
        message: Wpisz godzinę w formacie 14:30
    - name: miejsce
      label: Miejsce (np. sala WS, Instytut Matematyczny UWr)
      type: string
    - name: pozycja
      type: boolean
      hidden: true
```

Dlaczego dzień i godzina osobno, a nie jedno pole daty z godziną:
- **Dzień:** pole `type: date` bez godziny, z `default: ""`, więc CMS nie wpisze niczego sam. Data i godzina razem dawały wczoraj „21:28” (godzina otwarcia formularza).
- **Godzina:** zwykły tekst, więc bez godziny wydarzenie jest całodniowe (szkoły, kongresy).
- **Pole z godziną (`time: true`) odpada:** nie umie wczytać daty bez godziny (`read()` zwraca pusto), więc trzy istniejące wydarzenia całodniowe straciłyby datę przy pierwszym zapisie w CMS.

**Uwagi:**
- Wzorzec godziny **musi dopuszczać pusty tekst** (`^(|…)$`). Puste pole tekstowe to `""`, a wzorzec sprawdza je mimo braku `required`.
- Sprawdź w CMS, czy tekst z `>-` w `description` wyświetla się poprawnie. Jeśli nie, zapisz go w jednej linii.

### 2b. Kod strony (Web-Core)
- **`src/content.config.ts`:** dodaj pole `termin`, czyli tablicę obiektów z filtrem pustych pozycji z etapu 1b. Z pierwszej pozycji wylicz dzisiejsze pola, najlepiej w `.transform()` schematu kolekcji, żeby reszta kodu się nie zmieniła:
  - `wydarzenie_poczatek` = `dzien` + (`T` + godzina, jeśli jest);
  - `wydarzenie_koniec`:
    - `dzien_konca` (+ `godzina_konca`, jeśli jest), albo
    - `dzien` + `godzina_konca`, gdy podano tylko godzinę końca, albo
    - pusto, gdy nie podano niczego (strona przyjmie wtedy 2 godziny po początku albo cały dzień);
  - `wydarzenie_miejsce` = `miejsce`.
  - Godziny normalizuj do `GG:MM` („9.30” → „09:30”).
  - Jeśli Astro nie przyjmie `.transform()` w schemacie kolekcji, zrób jedną funkcję pomocniczą i użyj jej w `src/lib/tresci.ts` (ok. 209–213 i 376–377) oraz `src/lib/widoki/aktualnosc.ts` (22–25).
- **Okres przejściowy:** gdy wpis nie ma `termin`, a ma stare `wydarzenie_*`, użyj starych pól i wypisz ostrzeżenie w logu. Dzięki temu Web-Core można wypchnąć przed migracją danych.
- **`skrypty/migracja/formularze.py`** (linia 277, lista pól): uaktualnij.
- **`sprawdz_tresci.py`:** ostrzeżenie, gdy `rodzaj: wydarzenie` nie ma terminu, i gdy `termin` stoi przy `rodzaj: sukces` albo `kariera` (to zwykle pomyłka).

### 2c. Migracja danych (osobny commit w Web-Aktualnosci, według zasad wyżej i sekcji „Ochrona zmian redaktorów”)
Przenieś wszystkie wpisy z `wydarzenie_*` do `termin` i usuń stare pola. Stan z 17.11, 15:12 to 13 wpisów:

| Plik | `termin` po migracji |
|---|---|
| `2026-06-16-seminarium-wydzialowe.md` | 23.06 · 12:30 · koniec 14:00 · sala 119, Instytut Informatyki |
| `2026-06-19-seminarium-ze-statystyki.md` | 22.06 · 11:00 · koniec 24.06 13:00 · sale 602 i 605… |
| `2026-07-14-szkola-baby-steps-beyond-the-horizon.md` | 30.08 · bez godziny · koniec 5.09 · Będlewo |
| `2026-09-10-wyklad-prof-uwe-franza.md` | 15.09 · 13:00 · koniec 14:30 · sala WS… |
| `2026-09-20-kurs-dla-studentow-pierwszego-roku.md` (ogłoszenie) | 25.09 · bez godziny · Wydział… |
| `2026-09-23-2-kongres-mlodych-odkrywcow.md` | 21.09 · bez godziny · koniec 22.09 · Wydział… |
| 4 × `test-2026-11-0*` | 1:1 (wpisy testowe do usunięcia przed startem) |
| `2026-11-16-.md` „Seminarium wydziałowe” | 10.11 · **13:00** (z treści wpisu; teraz 21:28 i koniec 16.11 21:28 to wartości CMS) · bez końca · Instytut Informatyki sala 119 |
| `2026-11-16--1.md` „Stypendium…” (sukces) | **bez terminu** (daty z CMS; dzień jest w „Data”) |
| `2026-11-16--2.md` „Medale…” (sukces) | **bez terminu** (jw.; miejsce „Aula Leopoldina” przepada, zgłoś) |

- Wartości przenoś dokładnie. Koniec tego samego dnia zapisuj tylko jako `godzina_konca`.
- Trzy wpisy z 16.11 opisz w raporcie jako zmiany do akceptacji przed pushem. Jeśli właściciel poprawił je już ręcznie, weź jego wartości.
- Wpisy, które redaktorzy zmienili lub dodali po etapie 0, migruj z ich aktualnej wersji (sekcja „Ochrona zmian redaktorów”, punkt 1).
- Kontrola: Kalendarz, „Nadchodzące wydarzenia”, pliki .ics i strony wpisów przed/po są identyczne, z wyjątkiem tych trzech wpisów.

### 2d. Pozostałe pola dat
Przejrzyj wszystkie pola `type: date` we wszystkich `.pages.yml`:
- pola opcjonalne (np. data końca, data ogłoszenia obrony) dostają `default: ""`;
- pola wymagane (`data` publikacji, termin referatu itp.) zostają z „teraz”.

Lista do raportu.

### 2e. Dla redaktorów
- Uaktualnij `dok/sciagawka-edytora.md` krótką regułą: „Wydarzenie = kliknij »Add an item« pod »Termin wydarzenia«; zwykła informacja = nic nie klikaj, dzień w polu »Data«”.
- Wypisz w raporcie, które PDF-y dla redaktorów (Web-Podglad `dla-redaktorow/`) trzeba poprawić.

## Etap 3. Nazwy plików nowych aktualności z tytułu
**Objaw:** `2026-11-16-.md`, `2026-11-16--1.md`, `2026-11-16--2.md`, czyli adresy `/aktualnosci/2026-11-16--2/`.

**Prawdopodobna przyczyna:** `filename: { template: '{year}-{month}-{day}-{primary}.md', field: create }`.
- Przy `field: create` Pages CMS liczy nazwę przy otwarciu formularza, gdy tytuł jest pusty, i pokazuje ją w polu, którego redaktorzy nie ruszają (`components/entry/entry.tsx`, ok. 192–203).
- Bez tego pola nazwa powstaje przy zapisie z tytułu (ok. 330–333; `{primary}` = `view.primary` = `tytul`).
- Sprawdź w teście.

**Zmiana:** w Web-Aktualnosci usuń `field: create`. Przejrzyj inne kolekcje z tym ustawieniem i wypisz je z rekomendacją. **Istniejących plików nie przemianowuj**; zapytaj w raporcie.

## Etap 4. Odbiór lokalny
- Budowa „po” przechodzi. Porównanie widocznego tekstu wszystkich stron przed/po (PL i EN).
- Dozwolone różnice:
  - „Stypendium” i „Medale” znikają z Kalendarza i z liczb wydarzeń, a wracają do Aktualności na stronie głównej;
  - „Seminarium wydziałowe” ma termin 10.11, 13:00, jednodniowy.
  - Każdą inną różnicę zgłoś.
- Kontrole:
  - `sprawdz_pola_cms.py` 0 problemów (uaktualnij go, jeśli nie zna `termin` i pola `pozycja`);
  - `sprawdz_tresci.py` OK;
  - `astro check` bez nowych błędów.
- Symulacja zapisu w CMS (jak w zleceniu 28, etap 6a), formularz aktualności:
  1. nowy wpis bez terminu: w pliku nie ma `termin` ani dat wydarzenia;
  2. „Add an item” w terminie i zapis bez wypełnienia: czerwone „Dzień”, zapis zablokowany;
  3. sam dzień: wydarzenie całodniowe; godzina „9.30”: przyjęta, na stronie 09:30; godzina „25:00”: czerwone „Wpisz godzinę w formacie 13:00”;
  4. „Add an item” w galerii bez zdjęcia: czerwone przy „Zdjęcie”, zapis zablokowany; to samo z samym podpisem;
  5. stary wpis bez terminu (np. `2026-10-17-rusza-tutornia.md`): otwarty i zapisany bez zmian nie dostaje terminu ani dat;
  6. nazwa pliku nowego wpisu powstaje z tytułu.
- **Stop**, raport, czekanie na „push”.

## Etap 5. Po słowie „push”
- **Kolejność:**
  1. Web-Core na `main` (czyta stary i nowy zapis);
  2. zielona budowa Podglądu;
  3. Web-Aktualnosci (`.pages.yml` + migracja) i inne repozytoria treści.

  Każde od świeżego `main`, bez force-push, z kontrolą przed i po pushu (sekcja „Ochrona zmian redaktorów”).
- Sprawdź zieloną budowę, Kalendarz i kolumnę „Aktualności” na stronie głównej.
- **Test w CMS** (właściciel, jedno podejście, Web-Aktualnosci): punkty 1–6 z etapu 4 na prawdziwym CMS, na wpisie testowym. Na koniec usuń wpis testowy. Wynik do raportu.
- **Następnego dnia:** przegląd zapisów redaktorów z 24 godzin po pushu (sekcja „Ochrona zmian redaktorów”, punkt 4).

## Kryteria odbioru
- [ ] Pozycja galerii lub załącznika bez pliku: w CMS czerwony komunikat i blokada zapisu (także całkiem pusta pozycja); strona i tak pomija puste pozycje z ostrzeżeniem w logu.
- [ ] „Termin wydarzenia” jako grupa dodawana jednym kliknięciem, najwyżej jedna, pod „Rodzaj”, z opisem. Bez terminu wpis nie jest wydarzeniem; dzień obowiązkowy, godziny sprawdzane.
- [ ] CMS nie wpisuje sam żadnej daty wydarzenia, ani w nowym, ani w starym wpisie.
- [ ] 13 wpisów przeniesionych; Kalendarz i .ics bez zmian poza trzema wpisami z 16.11 (zaakceptowanymi przez właściciela).
- [ ] Opcjonalne pola dat we wszystkich formularzach mają `default: ""`; lista w raporcie.
- [ ] Nazwa pliku nowej aktualności powstaje z tytułu; istniejące pliki nieprzemianowane.
- [ ] Ściągawka uaktualniona; lista PDF-ów do poprawy w raporcie.
- [ ] Kontrole 0 / OK / bez nowych błędów. Push bez force, od świeżego `main`.
- [ ] Kontrola zmian redaktorów przed i po pushu w raporcie: wszystkie zapisy redaktorów zachowane. Przegląd z następnego dnia zrobiony.

## Do wiadomości właściciela (nie do zrobienia w tym zleceniu)
- **Do czasu wdrożenia** każdy zapis starego wpisu w formularzu aktualności dopisuje daty wydarzenia równe chwili zapisu. Doraźnie można dopisać `default: ""` przy `wydarzenie_poczatek` i `wydarzenie_koniec` w `.pages.yml` (Pages CMS → Configuration).
- **Redaktorzy przestawiają sobie nawzajem zakłady:** Grzegorz Karch 16.11 przeniósł Michaela Hechta i Krzysztofa Krawczyka ze Statystyki do Równań Różniczkowych, a Hechta pborod 10.11 przeniósł w odwrotną stronę. Trzeba ustalić, kto decyduje.
- **Wpisy testowe** („TEST: …”) wypychają prawdziwe wpisy na stronie głównej; są na liście do usunięcia przed startem.
- **Literówki w nowych wpisach:** „prof. Grzegorz Karch…, która wygłosi” (→ „który”); „Wyróżnienia otrzymali nasz doktorant” (→ „Wyróżnienie otrzymał”).
