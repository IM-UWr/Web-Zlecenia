# Raport: zlecenie 40, etap 0 — inwentaryzacja formularzy CMS (18.11.2026)

## Stan
- **Tylko inwentaryzacja. Nic nie zmieniłem** w Web-Core ani w repozytoriach treści. Nie ma commitów ani pushy.
- **STOP:** czekam na Twoje decyzje (sekcja „Pytania”). Etapy 1–6 zacznę po nich, od Web-Instytut.
- **Dane:** `origin/main` 16 repozytoriów treści z 18.11, ok. 12:30, bez Web-Spec-*.
  - Web-Aktualnosci `e4c9c62`, Web-Instytut `311faae`, Web-Nauka `498bc8d`, Web-Popularyzacja `0f76f88`, Web-Pracownicy `5bcaf22`, Web-Studia `b2a7c09`, Web-Ustawienia `f145d85`, Web-Sem-* jak w raporcie 31.
  - Kod: Web-Core `6e370e19`. Strona: budowa Podglądu z tymi danymi.
  - Dziś wieczorem push treści ze zlecenia 33 doda pole `opublikowany` w 6 repozytoriach. Etap 0 tego jeszcze nie uwzględnia; zmiana jest dopisana w `pola-do-cms.md`.
- **Pełna tabela pól:** `RAPORT-ZLECENIE-40-0-pola.md`. Każde pole każdego formularza: typ, czy ukryte, w ilu plikach ma treść, czy widać je na stronie, kategoria.
- **Poprawka do zlecenia:** wzór `strony/studia/podyplomowe.md` jest po zleceniu 39 w `kierunki/podyplomowe.md`.

## Jak sprawdzałem
1. **Pola formularzy** z `.pages.yml`, także pola w obiektach i listach: 889 pól w 34 formularzach.
2. **Czy strona czyta pole:**
   - nazwa pola w kodzie Web-Core (bez nakładki treści);
   - dla kolekcji także obecność w schemacie (`content.config.ts`), bo pole spoza schematu Astro odrzuca.
3. **Czy pole widać:** każdą wartość tekstową z danych (fragment ok. 30 znaków) szukałem w zbudowanej stronie, PL i EN.
4. **Ręczna kontrola w kodzie** wszystkich pól, które w kroku 2 albo 3 wypadły podejrzanie.

**Ograniczenie:** „używane” przy nazwach ogólnych (`opis`, `adres`, `etykieta`) to przybliżenie. W etapie każdego repozytorium sprawdzę je dokładnie, zanim cokolwiek usunę. Nic nie zostanie usunięte bez Twojej decyzji z tego raportu.

## 1. Pola

| Kategoria | Pól | Co dalej |
|---|---|---|
| używane | 708 | zostają |
| techniczne, już ukryte (`pozycja`, `uid`, `format_tresci`…) | 60 | bez zmian |
| puste i nieużywane | 15 | do usunięcia (lista 1c) |
| z treścią, ale nieużywane | 25 | **Twoja decyzja** (1a) |
| z treścią, czytane, ale niewidoczne na stronie | 13 | **Twoja decyzja** (1b) |

Nieukrytych pól technicznych nie znalazłem. Po migracji do jawnego Markdownu dojdzie ukryte `format_tresci`.

### 1a. Z treścią, ale nieużywane (kod ich nie czyta)

| Repozytorium → formularz | Pole | Treść | Moja rekomendacja |
|---|---|---|---|
| Web-Instytut → władze | `do_uzupelnienia` | 5 notatek („Zakres obowiązków zastępców…”) | ukryć: to notatki dla redakcji, nie dla czytelników |
| Web-Sem-Dydaktyka → opis seminarium | `do_uzupelnienia` | 2 notatki | ukryć, jak wyżej |
| Web-Studia → kierunki | `baner.liczby.etykieta_krotka`, `…_en` | 4 z 5 kierunków | usunąć: pozostałość starego banera; strona używa pełnej etykiety |
| Web-Studia → kierunki | `baner.podtytul_en` | 4 z 5 | **podłączyć**: strona EN pokazuje dziś polski podtytuł |
| Web-Ustawienia → strona główna | `naglowki_podstron.zdjecia.*` (zdjęcie i kadr dla 5 działów) | 5 zdjęć | **podłączyć**: nowy nagłówek ma te zdjęcia i kadry wpisane na stałe w `NaglowekZ.astro`; po podłączeniu zmienisz je w CMS. Inaczej: usunąć |
| Web-Ustawienia → strona główna | `przyciski` (3 przyciski: kandydaci, studenci, …) | tak | usunąć: nowa okładka ich nie pokazuje (do rekrutacji prowadzi menu, „Rekrutacja ↗”) |
| Web-Ustawienia → strona główna | `facebook`, `youtube` | adresy profili | podłączyć (ikony w stopce) albo usunąć; dziś nigdzie ich nie widać |
| Web-Ustawienia → strona główna | `baner.zdjecie_male`, `baner.zdjecie_telefon`, `baner.podpis`, `baner.podpis_en`, `baner.kadr` | tak | usunąć: nowa okładka sama dobiera rozmiary i kadr; podpisu zdjęcia nie pokazuje |

### 1b. Czytane, ale niewidoczne na stronie

| Repozytorium → formularz | Pole | Dlaczego niewidoczne | Pytanie |
|---|---|---|---|
| Web-Nauka → konferencje | Treść (`body`) | lista konferencji nie pokazuje opisu; 17 z 61 konferencji ma opis | **podłączyć** (przykład ze zlecenia): rozwijany opis przy konferencji albo osobna strona; inaczej ukryć |
| Web-Instytut → władze; Web-Ustawienia → deklaracja, prywatność, O stronie; strona wyszukiwania (`szukaj_haslo`); Web-Studia → 9 z 13 Stron | `haslo`, `haslo_en` | nowy nagłówek pokazuje hasło tylko razem z liczbami w banerze | pokazywać hasło także bez liczb? Czy ukryć pole tam, gdzie się nie pokaże? |

### 1c. Puste i nieużywane — do usunięcia
- Web-Sem-* (8 repozytoriów, bez Dydaktyki): `do_uzupelnienia` w opisie seminarium.
- Web-Ustawienia: `partnerzy` (lista pusta, strona jej nie czyta), `baner.podpis_telefon`, `baner.podpis_telefon_en` (etykieta w CMS mówi już „nieużywany”).

Puste, ale **używane** pola zostają, bo strona pokaże je po wpisaniu. To m.in.:
- `album` w aktualnościach;
- `kwota` i `strona` w grantach;
- `promotorzy` i `bip` w obronach;
- `dyzur` u władz;
- `kontakt_godziny` na stronie działu Instytut.

## 2. Teksty stron i stron działów

| Repozytorium | Plików | Nagłówków `##` | Znaków | Z tłumaczeniem EN |
|---|---|---|---|---|
| Web-Instytut (11 Stron, strona działu, tekst „Warto wiedzieć”) | 13 | 33 | 31 tys. | 12 |
| Web-Nauka (6 Stron, strona działu) | 7 | 15 | 16 tys. | 7 |
| Web-Aktualnosci (tekst Aktualności — pusty, Obrony doktorskie) | 2 | 1 + lista | 1,4 tys. | 1 |
| Web-Pracownicy (tekst Pracowników — pusty) | 1 | lista | 0 | 0 |
| Web-Ustawienia (deklaracja, prywatność, O stronie) | 3 | 9 | 5,6 tys. | 3 |
| Web-Studia, Web-Popularyzacja | 20 | — | — | już jawny Markdown |

**Co dziś rozpoznaje stary parser.** W tych 5 repozytoriach prawie nic:
- **Strony nie mają włączonych „Bloków wzorca”** (`bloki: true`). Parser nie robi więc z nich kafelków, osi, kontaktów, plików ani pytań. To zwykły Markdown:
  - akapity i nagłówki `##`;
  - listy;
  - tabele (2, infrastruktura informatyczna);
  - cytaty (8: infrastruktura informatyczna, deklaracja, prywatność).
- **Akapit wstępu (`.wst`):** na stronach działów Instytut i Nauka oraz w tekstach nad listami (granty, konferencje, publikacje, sukcesy, seminaria, struktura) pierwszy akapit dostaje wyróżnienie.
- **Sekcje przenoszone w inne miejsce strony** (`podziel()`, kotwice typu „strona”):
  - `/instytut`: sekcja „Ostatnie sukcesy” (`#sukcesy`);
  - `/nauka/publikacje`: „Czasopisma redagowane w Instytucie” (`#czasopisma`).
  - W trybie jawnym tego podziału nie ma. Potrzebny jest jawny odpowiednik, np. `## Ostatnie sukcesy {#sukcesy}` i obsługa w widoku. To zmiana w Web-Core w etapie 1 (Instytut) i 2 (Nauka).
- **Stałe id nagłówka:** „Konsultacje” (`#konsultacje`).

**Odpowiedniki jawne:**

| Dziś | Jawnie |
|---|---|
| zwykły akapit, lista, tabela, cytat | bez zmian (proza bez otoczek); `:::tabela` i `:::ramka` tylko wtedy, gdy ma się zmienić wygląd, czyli nie w tym zleceniu |
| akapit wstępu (`.wst`) | jak w Studiach i Popularyzacji (sprawdzę w etapie 1, czy jawny tryb robi go tak samo) |
| sekcja przenoszona (`#sukcesy`, `#czasopisma`) | `## … {#id}` i zmiana w widoku |
| id nagłówków `##` (58 nagłówków w 4 repozytoriach) | `{#id}` z dzisiejszym id przy każdym `##`; adresy sekcji się nie zmienią |

**Skutek:** migracja tych repozytoriów to głównie `format_tresci: jawne`, komentarz `<!-- UKŁAD JAWNY: … -->`, `{#id}` i dwie sekcje przenoszone. Ryzyko zmiany wyglądu jest małe. Kontrola: porównanie HTML przed i po.

## 3. Projekt opisów (zmiany względem dziś)
Dziś opis formularza mają Strony, strony działów, zakłady, „Warto wiedzieć”, władze, publikacje i referaty. Opisy pól są rzadkie: 0–3 na formularz, wobec 2–5 w Studiach.

| Formularz | Proponowany opis formularza („co to i gdzie widać”) | Kolejność pól |
|---|---|---|
| Aktualności | „Ogłoszenia, wydarzenia, sukcesy i oferty pracy. Widać je w Aktualnościach i na stronie głównej; wydarzenie z terminem trafia też do kalendarza.” | tytuł, **tytuł EN** → data, rodzaj, termin → Treść, Treść EN → zajawka, **zajawka EN** → reszta (dziś tytuł EN i zajawka EN są na samym dole) |
| Obrony doktorskie | „Publiczne obrony rozpraw doktorskich. Lista w Nauce → Obrony doktorskie. Pusta Treść = strona sama napisze zaproszenie.” | bez zmian (kandydat, tytuł rozprawy, termin, miejsce → Treść, Treść EN → reszta) |
| Konferencje | „Konferencje i warsztaty Instytutu. Lista w Nauce → Konferencje (nadchodzące i według lat).” (+ zdanie o opisie po decyzji 1b) | tytuł, **tytuł EN** → początek, koniec, miejsce → Treść → reszta (dziś tytuł EN pod Treścią) |
| Projekty i granty | „Projekty badawcze pracowników. Lista w Nauce → Projekty i granty; projekt z opisem ma własną stronę.” | tytuł, **tytuł EN** → rodzaj, lata → Treść → reszta (dziś tytuł EN pod Treścią) |
| Pracownicy | „Spis osób: pracownicy, doktoranci, administracja. Widać go w Pracownikach, na stronach zakładów i przy władzach.” | bez zmian (nie ma Treści) |
| Opis seminarium (9×) | „Opis seminarium: prowadzący, kontakt, archiwum. Widać go na stronie seminarium w Nauce → Seminaria.” | nazwa, nazwa EN → **Treść, Treść EN** → hasło, prowadzący, kontakt… (dziś Treść na 11. miejscu z 12) |
| Referaty (9×) | bez zmian opisu | tytuł, język, prelegent, afiliacja, termin, sala → **Treść (streszczenie), Treść EN** → pliki (dziś pliki nad Treścią) |
| Władze | bez zmian opisu; opisy pól z przykładami (dziś 0) | bez zmian |
| Strona główna i kontakt, „Na skróty”, Menu główne | „Tylko właściciel. …” + gdzie widać (okładka, stopka, menu) | po decyzjach 1a |
| Deklaracja, Prywatność, O stronie | „Tekst strony … (link w stopce).” | Treść na górze (już jest) |
| Strony i strony działów (5 repozytoriów) | jest; dopisać ściągawkę jawnego Markdownu w opisie pola Treść, jak w Studiach | Treść i Treść EN na górze (już są) |

- **Pola drobne:** krótki opis z przykładem i informacją, co się stanie przy pustym polu, jak w Studiach.
- **Etykiety EN:** „… EN” pod polskim polem; w kilku formularzach (Ustawienia) jest dziś „EN: …” na początku.
- **Pytanie 3:** we wpisach Treść stoi dziś po polach, które wpis identyfikują (tytuł, data, termin). Proponuję tak zostawić i tylko dosunąć pola EN do polskich. Zlecenie mówi „Treść na górze”, ale tytuł i data są kluczem wpisu na liście w CMS.

## 4. Szablony nowych wpisów
**Propozycja domyślnej Treści** (pole `code`, Markdown; komentarz w Treści nie trafia na stronę):

| Wpis | `default` |
|---|---|
| Aktualność | `<!-- TEKST: Zwykły tekst. Akapity oddziela pusta linia. Pliki: wgraj w „Media” i wklej link. -->` + `<!-- Rejestracja, program, plakat: wstaw link w osobnej linii. -->` |
| Konferencja | to samo + `<!-- Program, rejestracja, opłaty: każda informacja w osobnym akapicie. -->` (po decyzji 1b) |
| Grant | `<!-- OPIS PROJEKTU: Cel i wyniki projektu. Pusta Treść = projekt bez własnej strony. -->` |
| Obrona | `<!-- Zostaw puste, a strona sama napisze zaproszenie. Własny tekst zastępuje zaproszenie. -->` |
| Referat | `<!-- STRESZCZENIE: Zwykły tekst; wzory w $…$. Slajdy: dodaj w „Pliki” niżej. -->` |
| Zakład | `<!-- TEKST: Czym zajmuje się zakład. Skład i seminaria strona dopisze sama. -->` |
| „Warto wiedzieć” | `<!-- TEKST: Pusta Treść = sama zajawka bez własnej strony. -->` |

**Ryzyko, które trzeba usunąć przed szablonami.** Strona traktuje „niepustą Treść” jako „wpis ma opis”. Treść z samym komentarzem zmieniłaby wygląd:
- **granty:** projekt dostałby link do własnej, pustej strony (`maOpis`);
- **obrony:** zniknęłoby automatyczne zaproszenie (strona bierze je tylko przy pustej Treści);
- **referaty i opis seminarium:** pusta ramka streszczenia, a **tekst komentarza trafiłby do powiadomień o seminariach** (`seminaria/powiadomienia.json`: streszczenie bez usuwania komentarzy);
- **„Warto wiedzieć”:** wpis dostałby własną, pustą podstronę, link i miejsce w mapie strony;
- **aktualności:** bez skutków (strona wpisu jest zawsze, zajawka nie bierze się z Treści);
- **zakłady:** do sprawdzenia w etapie 1.

**Dodatkowo:** Pages CMS wstawia `default` także przy otwarciu **istniejącego** wpisu z pustą Treścią. Pierwszy zapis takiego wpisu, np. któregoś z 94 grantów bez opisu, dopisałby komentarz.

**Jak tego uniknąć:**
- jedna funkcja w Web-Core, np. `maTresc(body)`: Treść bez komentarzy HTML, po `trim()`;
- użyć jej we wszystkich miejscach powyżej;
- w powiadomieniach usuwać komentarze ze streszczenia.
- To zmiana w Web-Core przed pierwszym repozytorium z szablonami. Porównanie HTML przed/po: 0 różnic, bo dziś nikt komentarzy we wpisach nie ma.

## Pytania do Ciebie
1. **Pola z 1a:** zatwierdzasz moje rekomendacje (ukryć notatki, usunąć resztki starego banera i przyciski, podłączyć `podtytul_en` i zdjęcia nagłówków działów)? Facebook i YouTube: podłączyć w stopce czy usunąć?
2. **Hasło bez liczb (1b):** pokazywać czy ukryć pole tam, gdzie się nie pokaże? **Opisy konferencji:** podłączyć?
3. **Kolejność we wpisach:** Treść po polach identyfikujących wpis, a pola EN obok polskich (moja propozycja), czy Treść na samej górze?
4. **Opisy i szablony (sekcje 3 i 4):** zatwierdzasz albo poprawiasz teksty? Zgoda na `maTresc()` w Web-Core przed szablonami?

## Decyzje właściciela (18.11, ok. 13:05)
1. **Pola z 1a:** wszystkie rekomendacje zatwierdzone:
   - ukryć notatki `do_uzupelnienia` (władze, Sem-Dydaktyka);
   - usunąć `etykieta_krotka` (kierunki), resztki starego banera okładki (`zdjecie_male`, `zdjecie_telefon`, `podpis`, `podpis_en`, `kadr`) i `przyciski`;
   - podłączyć `baner.podtytul_en` kierunków i `naglowki_podstron.zdjecia.*` (zdjęcia nagłówków działów).
2. **Facebook i YouTube:** ikony z linkami w stopce (PL i EN).
3. **Hasło bez liczb:** ukryć pole tam, gdzie się nie pokaże. Wartości zostają w plikach, wygląd bez zmian.
4. **Opisy konferencji:** osobna strona konferencji z opisem i link z listy, jak granty.
5. **Kolejność we wpisach:** tytuł, tytuł EN → data, rodzaj, termin → Treść, Treść EN → reszta; pola EN tuż pod polskimi.
6. **Szablony:** najpierw `maTresc()` w Web-Core, potem opisy i szablony Treści w brzmieniu z sekcji 3 i 4.
