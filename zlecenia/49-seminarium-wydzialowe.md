# Zlecenie 49: rodzaj „Seminarium wydziałowe” w Aktualnościach i link do Tutorni we wpisie (18.11.2026)

**Decyzje właściciela (18.11):**
- **21:48:** „Dodamy do cms aktualności dodatkową kategorię. Seminarium wydziałowe.” Obecne wpisy o seminarium wydziałowym mają rodzaj „Wydarzenie” i przedrostek „SEMINARIUM WYDZIAŁOWE:” w tytule, a to „dość średnio wygląda”.
- **21:51: wariant A**, czyli sama nowa opcja w polu „Rodzaj”, bez nowych pól w formularzu. Wariant B (grupa „Wykład” z prelegentem, afiliacją, tytułem wykładu i streszczeniem, wpis ułożony jak referat) odrzucony: „B skonfunduje edytorów”.
- **21:53: „Zrób zlecenie 49”.** Przyjęte ustawienia zaproponowane w rozmowie, opisane niżej w „Docelowo”.
- **22:21 (zmiana decyzji z 22:14):** „Tytuł to kto, a zajawka to tytuł referatu”. Dotyczy obu istniejących wpisów, opisu pola i ściągawki. (O 22:14 było odwrotnie: „Tytuł to tytuł, autor do zajawki”; ta wersja nieaktualna.)
- **22:25:** „W wpisie o tutorni zamiast linkować do pdf podlinkuj nową zakładkę tutornii.” **22:27:** „Dodaj je do 49. Zaraz puszczę 49 całe.” Punkt 9 (osobne zlecenie 50 wycofane i włączone tutaj). 49 rusza od razu, bez czekania na 46 i 48 (sekcja „Kolejka” niżej).

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela. Raport `RAPORT-ZLECENIE-49.md`, zrzuty `raport-zrzuty/z49-*`. Bez subagentów.
- **Kolejka (zmiana 22:27):** właściciel uruchamia 49 od razu, w oknie 2, **bez czekania na 46, 47 i 48**. O 22:27 żadnego z nich nie było jeszcze na `origin/main` (Web-Core `main` = `3cde30e`).
  - Pracuj od świeżego `main`. Przed pushem zrób `git fetch` i rebase na `origin/main` (Web-Core i Web-Aktualnosci osobno).
  - Możliwe nakładanie się z tymi zleceniami:
    - `.pages.yml` Web-Aktualnosci i wczytywanie kolekcji w `src/lib/tresci.ts` (48);
    - `src/views/Aktualnosc.astro` (46);
    - `dok/sciagawka-edytora.md` (47 i 48).
  - Jeśli któreś z nich wejdzie na `main` przed Twoim pushem, nanieś swoje zmiany na ich wersję. Nie cofaj ich zmian. Jeśli 49 wejdzie pierwsze, one zrobią to samo po swojej stronie.
  - Numery linii w „Stan dziś” mogą się przesunąć. Szukaj po nazwach.
- **Kolejność pushy:** najpierw Web-Core, potem Web-Aktualnosci.
  - Powód: schemat musi znać nową wartość, zanim formularz ją zaoferuje. Gdyby było odwrotnie, pierwszy zapis z nową opcją zepsułby budowę (`z.enum`).
- **Ochrona zmian redaktorów (Web-Aktualnosci):**
  - zawsze od świeżego `main`, zwykły commit, bez force-push;
  - `.pages.yml`, poprawka dwóch wpisów (punkt 8) i wpisu o tutorni (punkt 9) w jednym commicie;
  - tuż przed pushem `git fetch` i `git log <baza>..origin/main`. Jeśli przybyły zapisy redaktorów (zwłaszcza w tych trzech wpisach albo w `.pages.yml`), nanieś zmianę jeszcze raz na świeży `main`. Nie doklejaj starego wyniku;
  - push wieczorem albo po wiadomości właściciela do redaktorów;
  - następnego dnia przegląd zapisów redaktorów z 24 godzin.
- **Ostrożnie z YAML w `.pages.yml`.** 18.11 o 19:02 etykieta z „: ” bez cudzysłowów wywaliła formularz Aktualności na ok. 2 minuty. Etykiety i opisy z dwukropkiem albo cudzysłowem bierz w cudzysłów. Po zmianie sprawdź, że plik się parsuje i że `sprawdz_pola_cms.py` daje 0 problemów.

## Stan dziś (sprawdzone 18.11, ok. 21:50 i 22:27: Web-Core `main` = `3cde30e` po zleceniu 45, Web-Aktualnosci `main` = `59d7427`, Web-Studia `main` = `e7e297e`)
- **Formularz** (Web-Aktualnosci, `.pages.yml`): pole „Rodzaj” (`rodzaj`, select, `default: ogloszenie`) z opcjami Ogłoszenie, Wydarzenie, Sukces, Kariera. Opis pola mówi tylko o „Karierze”. Opis kolekcji: „Ogłoszenia, wydarzenia, sukcesy i oferty…”.
- **Schemat:** `src/content.config.ts` (ok. linii 162), `z.enum(['ogloszenie', 'wydarzenie', 'sukces', 'kariera'])`.
- **Nazwy:** `src/lib/i18n.ts`, `RODZAJE` (plakietki, liczba pojedyncza) i `RODZAJE_FILTRY` (filtry, liczba mnoga).
- **Filtr Aktualności:** `src/lib/widoki/listaAktualnosci.ts` (ok. linii 20), lista `['ogloszenie', 'wydarzenie', 'sukces', 'obrona']`. Filtr pojawia się tylko wtedy, gdy są wpisy danego rodzaju. Panel „Pokaż”: `ListaPokaz.astro`, adres `?rodzaj=…`.
- **„Wpis o wydarzeniu”** (kolor działu w etykiecie, dacie i linkach; `.akt-wydarzenie`):
  - `src/views/Aktualnosc.astro` (ok. linii 48): `oWydarzeniu = d.rodzaj === 'wydarzenie'`;
  - `src/lib/widoki/aktualnosc.ts` (ok. linii 35): kolory wierszy „Najbliższych wydarzeń” tylko we wpisie `wydarzenie`.
- **Dział wpisu:** `src/lib/patroni.ts`, funkcja `dzialWpisu()`: `wydarzenie` daje Nauka (albo Popularyzacja, gdy pierwszym odbiorcą są kandydaci). Inne rodzaje idą dalej według odbiorców.
- **Pozycje Kalendarza z aktualności:** `src/lib/tresci.ts`, funkcja `wszystkieWydarzenia()` (ok. linii 233). Każdy wpis z terminem dostaje `rodzaj: 'wydarzenie'`, bez względu na rodzaj wpisu. Na tym `rodzaju` opierają się:
  - etykieta wiersza w Kalendarzu i w „Najbliższych wydarzeniach” (`WierszWydarzenia.astro`, `RODZAJE[w.rodzaj]`, `data-rodzaj`);
  - filtr Kalendarza (`Kalendarz.astro`, rodzaje `wydarzenie / obrona / konferencja / referat`);
  - liczby „nadchodzące wydarzenia” (`liczbyTerminow.ts`) i liczba na okładce;
  - plik `wydarzenia.ics`.
- **Strona główna:**
  - `src/components/zal/DrugiEkran.astro`, kolumna „Nadchodzące wydarzenia”: podpis `co` z `RODZ_WYD`. Dla `wydarzenie` podpisu rodzaju nie ma, tylko godzina i miejsce;
  - kolumna Aktualności: `RODZAJE[p.rodzaj]` małymi literami.
- **Kontrola treści:** `skrypty/sprawdz_tresci.py` (ok. linii 105–111) ostrzega przy `wydarzenie` bez terminu.
- **Ściągawka:** `dok/sciagawka-edytora.md` (ok. linii 151–152 i 184) opisuje „Termin wydarzenia” i rodzaj „Wydarzenie”.
- **Wpisy o seminarium wydziałowym:** dwa, oba z rodzajem `wydarzenie`:
  - `2026-11-10-seminarium-wydzialowe-problem-milenijny.md`: tytuł „SEMINARIUM WYDZIAŁOWE: Problem Milenijny i jego rozwiązanie zaproponowane przez OpenAI.”, EN „FACULTY SEMINAR: The Millennium Prize Problem and OpenAI’s Proposed Solution”; bez zajawki;
  - `2026-06-16-seminarium-wydzialowe.md`: tytuł „Seminarium wydziałowe: prof. Olga Vitek”, EN „Faculty seminar: Prof. Olga Vitek”; zajawka z tytułem wykładu, datą i salą.
  - `2026-06-19-seminarium-ze-statystyki.md` to seminarium Zakładu Statystyki, a nie wydziałowe. Nie ruszaj go.
- **Wpis o tutorni** `src/content/aktualnosci/2026-10-17-rusza-tutornia.md` („Rusza tutornia”, ogłoszenie, dla studentów):
  - załącznik „Plan dyżurów tutorów (semestr zimowy 2026/27)” / „Tutors' schedule (winter semester 2026/27, Polish)” prowadzi do `/pliki/aktualnosci/plan_tutorni_2026_z.png`. To obrazek PNG, nie PDF, i używa go tylko ten wpis;
  - treść PL kończy się zdaniem „Plan dyżurów tutorów znajduje się w załączniku poniżej.”, a treść EN zdaniem „The tutors' schedule is attached below.”;
  - strona Tutorni istnieje od zlecenia 45: `/studia/tutornia`, EN `/en/studia/tutornia` (tytuł „Tutornia” / „Tutoring room”). Strony Pierwszy rok i Sprawy studenckie linkują do niej jako `[tutornia](/studia/tutornia)`, a po angielsku `(/en/studia/tutornia)`.

## Docelowo

### 1. Nowa wartość i nazwy
- Wartość w danych: `seminarium-wydzialowe`.
- Plakietka (`RODZAJE`): „Seminarium wydziałowe” / „Faculty seminar”.
- Filtr (`RODZAJE_FILTRY`): „Seminaria wydziałowe” / „Faculty seminars”.
- Schemat (`content.config.ts`): wartość dopisana do `z.enum`. Domyślna wartość bez zmian (`ogloszenie`).

### 2. Formularz (Web-Aktualnosci, `.pages.yml`)
- W polu „Rodzaj” nowa opcja `seminarium-wydzialowe`, etykieta „Seminarium wydziałowe”, **zaraz pod „Wydarzenie”**. Kolejność: Ogłoszenie, Wydarzenie, Seminarium wydziałowe, Sukces, Kariera.
- Opis pola „Rodzaj”: dopisz przed zdaniem o „Karierze”: „»Seminarium wydziałowe« działa jak »Wydarzenie«: dodaj »Termin wydarzenia«. W tytule wpisz prelegenta, np. »Prof. Jan Kowalski«, bez »Seminarium wydziałowe«, bo pokazuje to plakietka. Tytuł wykładu wpisz w zajawce.”
- Opis kolekcji: „Ogłoszenia, wydarzenia, seminaria wydziałowe, sukcesy i oferty pracy, staży i stypendiów. Ogłoszenia, wydarzenia, seminaria wydziałowe i sukcesy widać w Aktualnościach i na stronie głównej; wpis z terminem trafia też do kalendarza. Oferty (rodzaj »Kariera«) są na stronie Kariera i na stronie Studiów.”
  - Jeśli ten opis ustawia też skrypt (`skrypty/migracja/formularze_40.mjs`), zmień go i tam, żeby ponowne uruchomienie nie przywróciło starego tekstu.
- **Żadnych nowych pól.**

### 3. Zachowanie jak „Wydarzenie”
- Jedna funkcja, np. `jakWydarzenie(rodzaj)` (`wydarzenie` albo `seminarium-wydzialowe`), zamiast porównań rozsianych po plikach. Użyj jej:
  - w `Aktualnosc.astro`: `oWydarzeniu`, czyli klasa `.akt-wydarzenie` i kolory działu;
  - w `aktualnosc.ts`: kolory wierszy „Najbliższych wydarzeń” we wpisie.
- Wpis z terminem trafia tam, gdzie wpis „Wydarzenie”: Kalendarz, „Nadchodzące wydarzenia” w Szybkim dostępie i „Ostatnio w kalendarzu”, `wydarzenia.ics`, liczby „nadchodzące wydarzenia” w banerach i liczba wydarzeń na okładce.
- **Pozycja Kalendarza zostaje rodzajem `wydarzenie`** (`Wydarzenie.rodzaj`, `data-rodzaj`). Dzięki temu w Kalendarzu jest pod filtrem „Wydarzenia”, liczy się do „nadchodzących wydarzeń” i jest w `wydarzenia.ics` bez dalszych zmian. Rodzaj wpisu przekaż osobnym polem, np. `rodzajWpisu?: string` w `Wydarzenie`, ustawianym w `wszystkieWydarzenia()`.
- **Dział:** w `dzialWpisu()` seminarium wydziałowe zawsze daje Nauka, także gdy pierwszym odbiorcą są kandydaci. Popraw komentarz nad funkcją.

### 4. Podpisy „seminarium wydziałowe” w wierszach wydarzeń
- **Kalendarz i „Najbliższe wydarzenia” na stronie wpisu** (`WierszWydarzenia.astro`): etykieta „Seminarium wydziałowe · wt. 10 listopada, 13:00 · …” zamiast „Wydarzenie · …”, PL i EN.
- **Strona główna, „Nadchodzące wydarzenia” i „Ostatnio w kalendarzu”** (`DrugiEkran.astro`): podpis jak przy obronie, np. „seminarium wydziałowe · 13:00 · s. 119” (EN „faculty seminar · …”). Zwykłe wydarzenia dalej bez podpisu rodzaju.
- **Tytuł wykładu pod prelegentem w wierszach wydarzeń.** Tytuł wpisu to prelegent, a tytuł wykładu jest w zajawce (punkt 8). Pozycja Kalendarza z aktualności ma już `opis` = zajawka, ale `WierszWydarzenia.astro` pokazuje `opis` tylko przy referacie. Pokazuj go też przy seminarium wydziałowym, tym samym stylem (`.ww-opis`). Działa to w Kalendarzu i w „Najbliższych wydarzeniach” na stronie wpisu. Strona główna (`DrugiEkran.astro`) bez tej zmiany: wiersz ma tytuł (prelegenta) i podpis z punktu wyżej.
- **Lista Aktualności, kolumna Aktualności na stronie głównej, metryczka wpisu, „Aktualności dla studentów” na stronie Studiów:** biorą nazwę z `RODZAJE`, więc wystarczy punkt 1. Sprawdź. Lista Aktualności pokazuje zajawkę pod tytułem już dziś.

### 5. Filtr w Aktualnościach
- `listaAktualnosci.ts`: `seminarium-wydzialowe` zaraz po `wydarzenie`. Filtr pokazuje się tylko przy wpisach tego rodzaju, jak dziś.
- `?rodzaj=seminarium-wydzialowe` (PL i EN) wybiera filtr.
- Sprawdź, że dłuższa nazwa „Seminaria wydziałowe” mieści się w panelu „Pokaż” na komputerze (1536 i 1920 px) i na liście wyboru na telefonie (390 px).

### 6. Bez zmian
- Kolumna „Seminaria” na stronie głównej, lista seminariów, strony seminariów i filtr „Seminaria” w Kalendarzu: tylko referaty seminariów Instytutu, jak dziś.
- Wygląd strony wpisu poza plakietką i kolorami „wpisu o wydarzeniu”: bez zmian (wariant B odrzucony).
- RSS, mapa strony i wyszukiwarka: bez zmian w działaniu (zmieniają się tylko tytuły i zajawki dwóch wpisów z punktu 8).

### 7. Kontrole i ściągawka
- `sprawdz_tresci.py`: ostrzeżenie „bez terminu” obejmuje też seminarium wydziałowe, np. „rodzaj »Seminarium wydziałowe« bez terminu — wpis nie trafi do Kalendarza (dodaj »Termin wydarzenia«)”.
- Jeśli symulator formularza (`skrypty/test-edytora/formularz.mjs`) albo `sprawdz_pola_cms.py` mają gdzieś listę wartości „Rodzaju”, dopisz nową.
- `dok/sciagawka-edytora.md`, przy „Termin wydarzenia”: „Seminarium wydziałowe: Rodzaj »Seminarium wydziałowe« i »Termin wydarzenia«. W tytule prelegent, np. »Prof. Jan Kowalski«, bez »Seminarium wydziałowe:«, bo pokazuje to plakietka. W zajawce tytuł wykładu.”
- PDF-y dla redaktorów (Web-Podglad, `dla-redaktorow/`): jeśli wymieniają opcje „Rodzaju”, napisz to w raporcie. Nie generuj ich w tym zleceniu.

### 8. Dwa istniejące wpisy (Web-Aktualnosci, w commicie z `.pages.yml`)
Zasada właściciela (22:21): **tytuł to prelegent, zajawka to tytuł wykładu.**
- `2026-11-10-seminarium-wydzialowe-problem-milenijny.md`:
  - `rodzaj: seminarium-wydzialowe`;
  - `tytul` i `tytul_en`: „Prof. Grzegorz Karch”;
  - nowe `zajawka`: „Problem Milenijny i jego rozwiązanie zaproponowane przez OpenAI” (bez kropki na końcu);
  - nowe `zajawka_en`: „The Millennium Prize Problem and OpenAI’s Proposed Solution”.
- `2026-06-16-seminarium-wydzialowe.md`:
  - `rodzaj: seminarium-wydzialowe`;
  - `tytul` i `tytul_en`: „Prof. Olga Vitek”;
  - `zajawka` i `zajawka_en`: „Statistical methods increase the accuracy and the interpretability of quantitative proteomic investigations” (tytuł wykładu w języku oryginału, jak przy referatach). Zastępują dzisiejsze zajawki, w których oprócz tytułu wykładu była data i sala.
- Zmień tylko te pola. Reszta pliku bajt w bajt bez zmian, w stylu YAML, jaki plik ma dziś (pierwszy bez cudzysłowów, drugi w cudzysłowach). Nowe pola w pierwszym wpisie wstaw tam, gdzie zapisałby je Pages CMS (według kolejności pól w formularzu). Nazwy plików i adresy wpisów bez zmian.
- Treść wpisów (akapity „W imieniu Dziekana…”) bez zmian.

### 9. Wpis „Rusza tutornia”: link do strony Tutorni zamiast załącznika (Web-Aktualnosci, w tym samym commicie)
- `2026-10-17-rusza-tutornia.md`:
  - usuń pole `zalaczniki`. Jedyna pozycja to stary plan. Plik `public/pliki/aktualnosci/plan_tutorni_2026_z.png` zostaw w repozytorium (nie usuwaj);
  - treść PL: zamień zdanie „Plan dyżurów tutorów znajduje się w załączniku poniżej.” na „Aktualny plan dyżurów tutorów jest na stronie [Tutornia](/studia/tutornia).”;
  - treść EN (`tresc_en`): zamień zdanie „The tutors' schedule is attached below.” na „The current tutors' schedule is on the [Tutoring room](/en/studia/tutornia) page.”
- Reszta wpisu bez zmian: tytuł, zajawka, data, odbiorcy i styl YAML (cudzysłowy). Nazwa pliku i adres bez zmian.
- Link musi działać także z przedrostkiem adresu Podglądu, tak jak linki na stronie Pierwszy rok.

## Odbiór lokalny
- **Porównanie HTML przed i po** (PL i EN), na tych samych klonach treści, bez przerwy między budowami. Różnice tylko:
  - w miejscach, gdzie widać tytuł, zajawkę albo rodzaj dwóch wpisów z punktu 8 (strony wpisów, listy, Kalendarz, „Nowszy / Starszy wpis” u sąsiadów, strona główna, RSS);
  - na stronie wpisu „Rusza tutornia” (PL i EN): bez sekcji „Załączniki”, z linkiem w treści (punkt 9);
  - nowy filtr „Seminaria wydziałowe” w Aktualnościach.
  - Pełna lista różnic do raportu. Liczby w banerach i na okładce bez zmian.
- **Wpis testowy** (kopia lokalna, nie w repozytorium): seminarium wydziałowe z terminem za 3 dni, 13:00, sala 119. Sprawdź, że:
  - jest w Kalendarzu pod filtrem „Wydarzenia” z etykietą „Seminarium wydziałowe”, a pod prelegentem widać tytuł wykładu z zajawki;
  - jest w „Nadchodzących wydarzeniach” z podpisem „seminarium wydziałowe · 13:00 · …”, w kolorze Nauki;
  - liczba „nadchodzące wydarzenia” rośnie o 1;
  - jest w `wydarzenia.ics`;
  - nie ma go w kolumnie „Seminaria”;
  - strona wpisu ma kartę „Kiedy / Gdzie” i kolory „wpisu o wydarzeniu”.
  - Ten sam wpis bez terminu: ostrzeżenie w `sprawdz_tresci.py`, a w Kalendarzu go nie ma.
- **Formularz:** symulacja zapisu jak w zleceniu 31 (etap 4):
  - stary wpis otwarty i zapisany bez zmian daje pusty diff;
  - wybór nowej opcji zapisuje `rodzaj: seminarium-wydzialowe`;
  - plik `.pages.yml` się parsuje.
  - Po pushu właściciel otwiera formularz Aktualności w Pages CMS. Zapisz to w raporcie jako krok dla niego.
- **Zrzuty:**
  - wpis prof. Karcha z 10.11 (komputer 1536×864 i 1920×1080, telefon 390 px);
  - wpis „Rusza tutornia” (komputer i telefon);
  - lista Aktualności z wybranym filtrem „Seminaria wydziałowe” (komputer i telefon);
  - wiersz w Kalendarzu;
  - „Nadchodzące wydarzenia” z wpisem testowym;
  - tryb jasny i ciemny.
- **Kontrole:** `astro check` bez nowych błędów, `sprawdz_pola_cms.py` i `sprawdz_tresci.py` bez problemów, testy wtyczek zielone, konsola czysta.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] W formularzu Aktualności „Rodzaj” ma opcję „Seminarium wydziałowe” pod „Wydarzenie”; opisy pola i kolekcji ją wymieniają, opis pola mówi „prelegent w tytule, tytuł wykładu w zajawce”; żadnych nowych pól; formularz się otwiera.
- [ ] Plakietka „Seminarium wydziałowe” / „Faculty seminar” na liście Aktualności, na stronie głównej, na stronie wpisu i na stronie Studiów; filtr „Seminaria wydziałowe” w Aktualnościach (także `?rodzaj=seminarium-wydzialowe`).
- [ ] Wpis z terminem zachowuje się jak „Wydarzenie”: Kalendarz (filtr „Wydarzenia”, etykieta „Seminarium wydziałowe”), „Nadchodzące wydarzenia” z podpisem „seminarium wydziałowe”, `.ics`, liczby; dział Nauka; kolory „wpisu o wydarzeniu”.
- [ ] Kolumna i lista „Seminaria” oraz filtr „Seminaria” w Kalendarzu bez zmian.
- [ ] Dwa istniejące wpisy mają nowy rodzaj, w tytule prelegenta (bez przedrostka), a w zajawce tytuł wykładu; reszta plików i adresy bez zmian.
- [ ] W Kalendarzu i w „Najbliższych wydarzeniach” wiersz seminarium wydziałowego pokazuje pod prelegentem tytuł wykładu (zajawkę), jak wiersz referatu.
- [ ] Wpis „Rusza tutornia” bez załącznika ze starym planem, z linkiem do strony Tutorni w treści PL i EN, działającym na Podglądzie; plik PNG zostaje w repozytorium.
- [ ] Ostrzeżenie w `sprawdz_tresci.py` przy seminarium wydziałowym bez terminu; ściągawka uzupełniona.
- [ ] Push w kolejności Web-Core → Web-Aktualnosci; zapisy redaktorów zachowane (kontrola przed i po pushu, przegląd następnego dnia).
