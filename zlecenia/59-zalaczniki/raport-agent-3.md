# Agent 3 — raport (wersja angielska strony IM UWr, 22.11.2026)

Zakres: kod Web-Core (napisy interfejsu, `src/lib/en/*`, ciekawostki), Web-Ustawienia, Web-Instytut poza `warto_wiedziec/`, Web-Pracownicy, Web-Studia, Web-Popularyzacja. Na końcu dopisane punkty od koordynatora (agent 4 i agent 2).

## Podsumowanie

- **Sprawdzone pliki treści:** Web-Ustawienia 7 (3 strony, 4 JSON), Web-Instytut 23 (12 stron, 9 zakładów, `instytut.md`, `wladze.json`), Web-Pracownicy 129, Web-Studia 28, Web-Popularyzacja 5. Pary pól PL/EN: **530** (w tym 46 par body/`tresc_en`), plus 106 ciekawostek patronów (Web-Core), plan zajęć (188 przedmiotów, 49 uwag z USOS) i wykazy publikacji 2003–2025.
- **Uzupełnione (brakowało EN):** 1 pole (`opis_en` strony listy „Warto wiedzieć” — na `/en` wychodził polski wstęp). Pozostałe „braki” to treści bez widocznego tekstu (sam komentarz w body: `strony/pracownicy.md`, `strony/instytut/warto-wiedziec.md`, `strony/studia/plan-zajec.md`) albo specjalność bez podstrony (`matematyka-w-ekonomii.md`) — zostawione.
- **Poprawione (EN był, ale zły/nieaktualny/niezgodny z zasadami):** 47 plików treści.
  - 3 Treści EN napisane od nowa, bo polska wersja została przebudowana (inne sekcje, nowe bloki): `data/popularyzacja.md`, `popularyzacja/uczniowie.md`, `popularyzacja/nauczyciele.md`.
  - 42 pliki jawnego Markdownu miały w EN **inne `{#id}`** niż w PL (zasada: te same id) i **linki wewnętrzne z `/en/`** (zasada: bez `/en`). Ujednolicone ok. 170 id (po kolejności nagłówków, po sprawdzeniu, że sekcje sobie odpowiadają) i ok. 150 linków; kotwice w linkach między stronami przepięte na nowe id. Test w zbudowanej stronie: wszystkie linki z kotwicą na stronach `/en` z mojego zakresu trafiają w istniejące id (0 błędów).
  - kilkanaście poprawek treściowych (tabela niżej).
- **Zostawione bez zmian:** pozostałe ~480 par (tłumaczenia zgodne z PL; pisownia brytyjska sprawdzona automatycznie — „program” tylko w znaczeniu programu komputerowego, „Center” tylko w nazwie własnej).
- **Kod Web-Core:** 16 plików (+83/−33) — tabela niżej. Plan zajęć: wszystkie przedmioty i uwagi z obecnego planu mają EN; ~300 „polskich” fragmentów na `/en/studia/plan-zajec` to nazwiska prowadzących, a 2 nazwy przedmiotów cytowane w uwagach („Miara i całka R”, „Programowanie i analiza danych w R”) zostają celowo (TLUMACZENIA.md, sekcja 2). Mapa publikacji: dopisane brakujące zwroty.
- **Test budowy** (kopia `/home/claude/en/build` + moje zmiany + łatka konferencji agenta 4): `astro build` OK (953 strony). **Wszystkie 477 stron HTML PL identyczne** z obecną witryną (po usunięciu skrótów zasobów i losowych uid wysp). Inne pliki PL: różnią się tylko znacznikiem czasu (`DTSTAMP` w .ics, `wygenerowano` w powiadomienia.json), kolejnością w sitemap.xml (ten sam zbiór adresów) i eksportem schematu CMS (`collections/*.schema.json` — nowe pola). Budowałem 3 razy (trzeci raz po dopisanych punktach agenta 4 — żeby potwierdzić PL bez zmian; za drugim razem wyszły różnice białych znaków po komentarzach JSX, poprawione). Ostatnia zmiana (`obraz_zrodlo_en`, punkt od agenta 2) — sprawdzona tylko kompilatorem Astro i esbuild, **bez pełnej budowy**.
- Skan (`skan_pl.py`) mojego zakresu po zmianach: jedyne fragmenty z `lang="pl"` to tematy prac na specjalnościach (D17, celowo) i zajawka MISIU na stronie głównej (Web-Aktualnosci, agent 4).
- `sprawdz_tresci.py` na każdym zmienionym `src/`: OK (Web-Instytut — tylko 3 istniejące wcześniej ostrzeżenia o obrazach z Web-Aktualnosci w `warto_wiedziec/nagrody`). `git apply --check` każdej łatki na czystym klonie: OK.

Wyniki: `Web-Core.patch`, `Web-Ustawienia.patch`, `Web-Instytut.patch`, `Web-Studia.patch`, `Web-Popularyzacja.patch`. Web-Pracownicy — bez zmian (funkcje mają dobre EN, stopnie zamienia kod wg D1), brak łatki.

## Tabela zmian (treści)

| Plik | Pole | Co zrobiono |
|---|---|---|
| Web-Ustawienia `strony/deklaracja-dostepnosci.md`, `polityka-prywatnosci.md`, `o-stronie.md` | `tresc_en` | poprawione: `{#id}` jak w PL (3 + 1 + 5) |
| Web-Ustawienia `strony/o-stronie.md` | `tresc_en` | poprawione: „Portraits in “Did you know”” → “Highlights” (słownik) |
| Web-Ustawienia `data/nawigacja.json` | `menu[2].grupy[1].nazwa_en` | poprawione: „Everyday” → „Day to day” (błędny rzeczownik) |
| Web-Ustawienia `data/nawigacja.json` | `menu[4]…linki[0].opis_en` | poprawione: „clubs, camps…” → „maths circles, camps…” (kółka ≠ koła naukowe) |
| Web-Ustawienia `data/stopka.json` | `kolumny[1].linki[3].etykieta_en` | poprawione: „Admissions (in Polish)” (D20, jak w menu) |
| Web-Instytut `strony/instytut/warto-wiedziec.md` | `opis_en` | uzupełnione (na `/en` był polski wstęp listy) |
| Web-Instytut `strony/instytut/kontakt.md`, `infrastruktura-informatyczna.md` + 8 podstron | `tresc_en` | poprawione: id jak w PL, linki bez `/en` |
| Web-Instytut `zaklady/dydaktyka.md` | `tresc_en` | poprawione: brakowało zdania o praktykach (link `/studia/matematyka#praktyki`) |
| Web-Instytut `zaklady/analiza-funkcjonalna.md` | `tresc_en` | poprawione: „Professor” → „Prof.” (D1) |
| Web-Studia `kierunki/matematyka.md` | `tresc_en` | poprawione: etapy I stopnia nieaktualne (PL: „Semestr 1 / 2–4 / 5–6”, bez terminów i formularzy przy etapach) |
| Web-Studia `kierunki/isim.md`, `siad.md`, `szkola-doktorska.md`, `podyplomowe.md` | `tresc_en` | poprawione: linki bez `/en`; podyplomowe — id jak w PL |
| Web-Studia `specjalnosci/*` (5) | `tresc_en` | poprawione: `tytul="Who is it for"` → „Who it is for” (instrukcja) |
| Web-Studia `specjalnosci/matematyka-nauczycielska.md` | `tresc_en` | poprawione: polski nagłówek „## Seminaria” → „Seminars”; linki bez `/en` |
| Web-Studia `strony/studia/*` (14 stron) | `tresc_en` | poprawione: id jak w PL, linki bez `/en`, kotwice między stronami |
| Web-Studia `strony/studia/szkola-doktorska/dokumenty.md` | `tresc_en` | poprawione: brakowało „(as of 12 April 2024)” |
| Web-Studia `strony/studia/szkola-doktorska/stypendia-i-granty.md` | `tresc_en` | poprawione: kredyt studencki — brakowało „na okres kształcenia” |
| Web-Popularyzacja `data/popularyzacja.md` | `tresc_en` | napisane od nowa: nowy wstęp i 4 kafelki (EN miał stary tekst bez kafelków); szkic w komentarzu zostawiony |
| Web-Popularyzacja `popularyzacja/uczniowie.md` | `tresc_en` | napisane od nowa: PL ma inne sekcje (MISIU, Konkursy, …) i bloki |
| Web-Popularyzacja `popularyzacja/nauczyciele.md` | `tresc_en` | napisane od nowa: nowa sekcja „Dolnośląski Kongres…”, zmienione kafelki i tabela |
| Web-Popularyzacja `popularyzacja/organizatorzy.md` | `opis_en`, `tresc_en` | poprawione: nazwa pracowni jak w `nazwa_en` zakładu („Mathematics Education and Outreach Unit”); id jak w PL |
| Web-Popularyzacja `popularyzacja/wszyscy.md` | `tresc_en` | poprawione: id jak w PL |

## Zmiany w kodzie Web-Core (zrobione)

| Plik:linia | PL → EN (było → jest) |
|---|---|
| `src/components/zal/DrugiEkran.astro:215` | Warto wiedzieć → „Highlights” (było „Did you know”; słownik) |
| `src/components/zal/DrugiEkran.astro:124` | „1 referat w tym tygodniu” → „1 talk this week” (było „1 talks”) |
| `src/components/zal/DrugiEkran.astro:205` | Rekrutacja na studia → „Admissions (in Polish)” (było „Admission”; D20) |
| `src/views/RokAkademicki.astro:72–73` | „dzień tygodnia występuje w semestrze po raz nieparzysty/parzysty” → „an odd-/even-numbered occurrence of that weekday in the semester” (było niegramatyczne „for an odd time”) |
| `src/lib/en/publikacje.ts:43–47, 66` | „(praca, mimo daty 2007, ukazała się dopiero w roku 2008; [praca] nie była sprawozdawana…)” (5 wariantów) → „(the paper, although dated 2007, appeared only in 2008; it was not reported in 2007)”; „Japoński przekład” → „Japanese translation of”; „320 stron.” → „320 pp.”; „Recenzent :” → „Reviewer:”; „Materiały V Konferencji "…", 9-10 grudnia 2016” → „Proceedings of the 5th Conference "…", 9–10 December 2016” |
| `src/lib/tresci.ts:221–231` (`MIEJSCA_EN`, agent 4 p. 1) | „… Uniwersytetu Wrocławskiego” (Wydział/IM/II) → „…, University of Wrocław”; „Instytut Informatyki” → „Institute of Computer Science”; „Instytut Informatyki sala 119” → „Institute of Computer Science, room 119”; „Politechnika Wrocławska” → „Wrocław University of Science and Technology”; „budynek” → „Building” |
| `src/content.config.ts:172` + `src/views/Aktualnosc.astro:113` (agent 4 p. 2) | nowe pole `galeria[].podpis_en`; na `/en` podpis EN (puste = polski) — sprawdzone w teście |
| `src/content.config.ts:448`, `src/lib/widoki/konferencja.ts:18–19`, `src/views/Konferencja.astro:44` (agent 4 p. 3) | nowe pole `tresc_en` konferencji, render jak w aktualnościach; z łatką `Web-Nauka-konferencje-tresc_en.patch` wszystkie 17 stron `/en/nauka/konferencje/*` mają angielski opis (lang=pl na konferencjach: 30 → 0) |
| `src/views/Aktualnosc.astro:63`, `AktualnoscZamianaDni.astro:36` (agent 4 p. 4) | „For: … phd students” → „PhD students” (`odbiorcyMalymi`) |
| `src/views/Obrona.astro:28, 40` (agent 4 p. 5a) | polski tytuł rozprawy na `/en`: „Original title: <span lang="pl">…</span>” (D5, D14; 35 obron); po polsku bez zmian |
| `src/components/WierszWydarzenia.astro:39`, `DrugiEkran.astro:69` (p. 5a) | polski tytuł rozprawy na liście obron, w kalendarzu i na głównej: `lang="pl"` (było `lang="en"`/brak) |
| `src/views/Obrona.astro:52` (p. 5b) | dwóch promotorów: „Supervisors” (tylko `/en`; PL bez zmian) |
| `src/lib/osoby.ts:43–44` (p. 5c) | „(promotor pomocniczy)” → „(auxiliary supervisor)”, „(kopromotor)” → „(co-supervisor)” |
| `src/lib/widoki/obrona.ts:62–63` (p. 5d) | „…, in online.” → „…, online.”; „in University of Tunis…” → „at University of Tunis…” |
| `src/content.config.ts:512`, `src/lib/wartoWiedziec.ts`, `src/views/SylwetkaWW.astro:35, 55` (agent 2) | nowe pole `obraz_zrodlo_en`; na `/en` „Photo: …” z pola EN, puste = polskie z `lang="pl"` (gdy wygląda na polskie) |
| `dok/en/TLUMACZENIA.md` | dopisane wiersze z powyższymi tłumaczeniami (sekcje 1 i 3) |

Punkty od agenta 4: **zrobione 1, 2, 3, 4, 5a–d, 7**. **Nie zrobione:** p. 6 (brak `pliki[].nazwa_en` w `.pages.yml` 9 repozytoriów Web-Sem-* — to konfiguracja CMS cudzych repozytoriów; dziś żaden referat nie ma plików) i sugestia `tresc_en` dla grantów (żaden grant nie ma opisu — bez potrzeby teraz).

## Potrzebne zmiany poza moimi łatkami

**Pola w `.pages.yml` (do dopisania przez redakcję/koordynatora):**
- Web-Aktualnosci, kolekcja aktualności, `galeria` → `fields`, po polu `podpis` (ok. l. 178):
  ```yaml
      - name: podpis_en
        label: 'EN: podpis'
        type: string
  ```
  Tłumaczenia od agenta 4: „The Rector and Prof. Marek Bożejko”, „The Rector and Prof. Tomasz Rolski”, „Agnieszka Hejna-Łyżwa and Mariusz Tobolski”.
- Web-Nauka, kolekcja `konferencje`, po polu `body` (ok. l. 143):
  ```yaml
    - name: tresc_en
      label: Opis EN
      description: Opis po angielsku, w tym samym układzie co opis. Puste = wersja angielska pokaże opis polski.
      type: code
      options:
        format: markdown
  ```
  Po dodaniu pola można nałożyć `wyniki/4/Web-Nauka-konferencje-tresc_en.patch`.
- Web-Instytut, „Warto wiedzieć” → Sylwetki, po `obraz_zrodlo` (ok. l. 438):
  ```yaml
      - name: obraz_zrodlo_en
        label: 'EN: źródło zdjęcia'
        description: Po angielsku, bez „Photo:” (strona dopisuje je sama). Puste = źródło polskie.
        type: string
        default: ""
  ```
  (pole leży w grupie „Karta”, jak `obraz_zrodlo`; schemat spłaszcza grupę).

**Napisy w kodzie, których nie zmieniałem (tylko Podgląd albo do decyzji):**
- `src/lib/wartoWiedziec.ts:185` — „Zdjęcie” w zaślepce portretu (tylko Podgląd, `lang="pl"`) — na stronie publicznej nie występuje.
- `src/components/zal/StanBudowy.astro`, `components/grafik/Plan.astro:38–40`, `components/ww/RamkiWW.astro` — komunikaty Podglądu dla redakcji po polsku (celowo).
- `src/views/Zaklad.astro:79`, `Specjalnosc.astro:65` — etykieta „e-mail” na `/en` (poprawna; w innych miejscach „Email”) — można ujednolicić.

## Do decyzji właściciela

1. **Tutornia — grafik na `/en`** pokazuje polskie skróty przedmiotów („AM1”, „WdM(R)”, „AiT(R)”, „Alglin 1R”, „Algebra liniowa 1”, „Miara i całka”, „Programowanie”, „Wstęp do kombinatoryki”). Danych grafiku nie zmieniałem. Propozycja: mapa skrótów przy wyświetlaniu na `/en` (jak `src/lib/en/plan.ts`) według nazw EN z USOS: AM → Advanced calculus, WdM → Introduction to abstract mathematics, AiT → Analysis and topology, Alglin/Algebra liniowa → Linear algebra, Miara i całka → Measure and integral, Programowanie → Programming, Wstęp do kombinatoryki → Introduction to combinatorics; albo (prościej) zdanie pod grafikiem w Treści EN z objaśnieniem skrótów.
2. **Wspólne `{#id}` PL/EN**: ujednoliciłem EN do polskich id (także z polskimi znakami, np. `#zgłoszenia`), zgodnie z instrukcją. Jeśli ktoś udostępnił link do starej angielskiej kotwicy (np. `/en/studia/zajecia#forms`), przestanie trafiać w sekcję (strona się otworzy).
3. **„Admissions (in Polish)”** na stronie głównej (D20) — przycisk jest dłuższy niż „Admission”; wygląd przycisku nie powinien się zmienić, ale warto rzucić okiem.
4. **Nazwa pracowni**: przyjąłem „Mathematics Education and Outreach Unit” (= `nazwa_en` w zakładach); w Popularyzacji było „Laboratory of Mathematics Education (and Outreach)”.
5. **IM PAN**: w moim zakresie nie ma innej rozwiniętej nazwy niż oficjalna; w ciekawostce Ślebodzińskiego (`src/data/ciekawostki/nauka.json`, „Geometry group at IM PAN”) zostaje skrót — można rozwinąć na „Institute of Mathematics of the Polish Academy of Sciences”, kosztem długości zdania w banerze.
6. Dopisek „(in Polish)” (D20): w Treściach EN linki do serwisów tylko po polsku (FMW, Portal) mają „(in Polish)” niekonsekwentnie (w kafelkach Popularyzacji bez dopisku, jak dotąd).

## Błędy w polskim tekście (nie poprawiałem)

- Web-Studia `kierunki/matematyka.md`, etapy I stopnia: „**Semestry 1: Podstawy**” (powinno „Semestr 1”); „**Semestry 5–6: Przedmioty specjalnościowe.** —” (kropka w pogrubieniu); w etapie 3 „praca licencjacka”, a strony specjalności piszą, że na I stopniu nie ma pracy dyplomowej (sprzeczność do wyjaśnienia; EN przetłumaczony wiernie).
- Web-Popularyzacja `data/popularyzacja.md`: akapit złamany w trzech liniach (renderuje się jako jeden akapit), łamanie linii w środku tekstu linku, cudzysłowy "…" zamiast „…”, w kafelku „Dla uczniów” zbędne „ .”, niekonsekwentne kropki w tekstach linków.
- Web-Popularyzacja `popularyzacja/uczniowie.md`: „Uniwerystetem”, „postawowej”, „Ddla”, brak kropki po „rozumowań”, łącznik „-” zamiast półpauzy („dwóch wykładów - z matematyki”, „kilkanaście godzin - aż”); `nauczyciele.md`: „zagranicą” (→ „za granicą”).
- Kod (PL): `DrugiEkran.astro:124` — „2 referatów w tym tygodniu” (brak formy „referaty” dla 2–4); `Obrona.astro:52` — „Promotor” także przy dwóch promotorach; `Obrona.astro:40` i `WierszWydarzenia.astro:39` — na stronach PL polskie tytuły rozpraw mają `lang="en"`. Nie zmieniałem, żeby strony PL zostały bez zmian.

## Wpisy testowe / do usunięcia przed startem

W moim zakresie brak. Na stronach mojego zakresu widać cudze wpisy testowe: „TEST: Przykładowy referat – …” i „Prelegent testowy” (Web-Sem-*, na `/en/` i w kalendarzu).

## Dla innych agentów (zauważone przy okazji)

- Agent 4 (Web-Aktualnosci): `2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza.md` — brak `tytul_en` i `zajawka_en` (na `/en/instytut`, `/en/studia` i głównej tytuł i zajawka po polsku); `2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu.md` — zajawka po polsku na `/en/`.
- Agenci 1/2: lista `/en/instytut/warto-wiedziec` pokazuje polskie tytuły historii i nagród oraz podpisy sylwetek tam, gdzie brak `tytul_en`/`podpis_en`.
