# Raport — zlecenie 54: „Warto wiedzieć” — styl tekstu i źródła (część A); seminarium wydziałowe znów jako „Wydarzenie” (część B)

**Status:** obie części zrobione, sprawdzone lokalnie i wypchnięte bez czekania na „push” (polecenie właściciela z 19.11 rano: praca samodzielna, push po spełnieniu warunków; cisza w repozytoriach treści sprawdzona przed każdym pushem).

| Część | Repozytorium | Commit | Push |
|---|---|---|---|
| A | Web-Instytut | `645a832..a255edb` (32 pliki WW skryptem + opisy w `.pages.yml`) | 11:46:47 |
| A | Web-Core | `9c45eb80..f12aeb15` (tylko `dok/`) | 11:47:00 |
| B | Web-Core | `f12aeb15..6193ddfd` (cofnięcie 49 + preprocess, ostrzeżenie, symulator, ściągawka) | 11:57:50 |
| B | Web-Aktualnosci | `eee693e..d9e2f3e` (`.pages.yml` w 3 miejscach, tytuły 2 wpisów) | 11:57:53 |

Kolejność pushy jak w zleceniu (A: najpierw Web-Instytut, potem Web-Core; B: dowolna). Gałęzie robocze `praca/54-styl` i `praca/54b-seminaria` (Web-Core, Web-Instytut, Web-Aktualnosci) zostają lokalnie.

---

## Część A — styl tekstu „Warto wiedzieć”

### Wykonanie
1. **Skrypt z załącznika A** zapisany bez zmian do `.przekazanie\zlecenia\zlecenie54.py` (332 linie, sha256 `fac9fb18e877…b9cb111`), poza repozytoriami. Najpierw `--sprawdz` na Web-Instytut `645a832` (main po 53, bez „Do pobrania” u Bożejki i Rolskiego): każdy fragment „było” wystąpił dokładnie raz, bez STOP. Potem zapis w miejscu: **32 pliki, 87 zamian, 2 sekcje „Źródła”** (log `tresci-C/z54-skrypt.log`).
2. **Opisy pól** (`.pages.yml` Web-Instytut, punkt 3): zdanie „Styl: …” na końcu `description` pól Treść i Treść EN w `ww_sylwetki`, `ww_nagrody`, `ww_historie` (6 zdań, dokładnie jak w zleceniu). Poza `description` nic się nie zmieniło; plik się parsuje; `sprawdz_pola_cms.py` — 0 problemów.
3. **Dokumentacja Web-Core:** `dok/sciagawka-edytora.md` — punkt „Styl tekstu (zlecenie 54)” w części „Warto wiedzieć”, „Samo nazwisko bez linku powiązania nie daje.”, przy „Do pobrania” dopisek „tylko pliki, których nie ma w »Źródłach«”; `dok/jawny-markdown.md` — jedno zdanie z odesłaniem do stylu w ściągawce.

### Kontrola wyniku (skrypt `tresci-C/z54-kontrola.py`)
- **Pogrubienia:** razem **88** — hasła wyliczeń **72 w 15 sylwetkach**, lata laureatów **16 w 4 nagrodach**; poza regułą: 0.
- **Początek wstępu:** wszystkie **18 sylwetek** zaczyna się od „Prof. …”, Tabisz od „Dr Krzysztof Tabisz jest matematykiem…” (EN „Dr Krzysztof Tabisz is a mathematician…”); tytułów przy bohaterze po pierwszym zdaniu: 0. Pozostałe wystąpienia słowa „profesor” to opisy kariery („został profesorem”, „jako profesor Uniwersytetu…”), dozwolone.
- **Tabisz:** pierwsze zdanie ciągłe, bez myślnika i roku; zajawki PL i EN bez imienia i nazwiska („Matematyk, wieloletni pracownik…”, „Mathematician, long-serving…”); w tekście bez pogrubień; YAML OK.
- **Bożejko i Rolski:** nowe „Źródła” — **38** i **26** pozycji (licznik na stronie: „38 źródeł”, „26 źródeł”); Rolski „ur. 1946” pod portretem.

### Porównanie HTML przed i po (`TYLKO_OPUBLIKOWANE=1`, `z53-pub` → `z54a-pub`, PL i EN)
4969 plików w obu budowach; identyczne 4803, tylko czas 108, kolejność sitemap 1, **zmienione 57** (pełna lista `tresci-C/z54a-roznice.txt`):
- **56 stron „Warto wiedzieć”** (PL i EN): tekst z tabeli punktu 1 (tytuły, pierwsze zdania), zdjęte `<strong>` (77 par), nowe linki, opisy `<meta description>` Tabisza (zajawka) — dozwolone.
- **Kolejność karty Rolskiego** na liście sylwetek, w „Innych sylwetkach” i w puli strony głównej: wcześniej „lata: xxxx” (bez roku = na końcu listy), teraz „ur. 1946”, więc sortowanie po roku urodzenia stawia go przed Tabiszem (1950) i Bilerem. Na stronie głównej (`index.html`) zmienia się tylko kolejność ukrytej (`hidden`) karty Rolskiego w puli losowania; widoczne karty te same. Wyjaśnione, wynika z tabeli (pole `lata`).
- **Link Tabisz → Krzywicki:** w tekście Tabisza nowy link do sylwetki Krzywickiego. **Powiązania nie dodał:** strona Krzywickiego nie ma sekcji „Zobacz też” (ta pokazuje tylko nagrody i historie, które linkują osobę — zlecenie 53), Tabisz jest tam, jak przed zleceniem, tylko w siatce „Inne sylwetki”.
- Innych różnic brak.

### Linki wewnętrzne z punktu 2 (w budowie `z54a-pub`)
Wszystkie 7 istnieją: `/instytut/warto-wiedziec/andrzej-krzywicki` (linkuje 19 stron WW), `/instytut/warto-wiedziec/medal-uniwersytetu` (8), `/aktualnosci/2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego` (3), `/seminaria/dyskretna-analiza-harmoniczna` (1), `/nauka/sukcesy/historia` (9), `/nauka/granty/2017-2016-21-b-st1-00628` (1), `/nauka/granty/2008-bwz-184-jsk-jsps-08` (1). Pełny przegląd linków `/Web-Core/…` ze wszystkich stron WW PL i EN: **0 martwych**.

### Zrzuty (`raport-zrzuty/z54-zrzuty/`, 1920×1080, jasny; konsola: 0)
`z54a-tabisz-pl-1920.png`, `z54a-tabisz-en-1920.png` (cała strona), `z54a-bozejko-zrodla-1920.png` i `z54a-rolski-zrodla-1920.png` (rozwinięte „Źródła”), `z54a-bozejko-cala-1920.png`, `z54a-rolski-cala-1920.png`, `z54a-knaster-1920.png` (hasła wyliczeń pogrubione), `z54a-medal-uwr-1920.png` (tekst bez pogrubień, pogrubione lata laureatów), `z54a-annals-1920.png`, `z54a-tabisz-pl-390.png`.

### Kontrole
- `astro check`: 0 błędów, 0 ostrzeżeń, 8 podpowiedzi (jak po 53; 4 z lokalnych skryptów raportów spoza repozytorium);
- `npm run test:jawne`: 84/84;
- `sprawdz_tresci.py`: OK, 594 pliki, **0 ostrzeżeń** (dawne ostrzeżenie o „lata: xxxx” Rolskiego zniknęło);
- `sprawdz-jawny-markdown.mjs ../tresci-C/Web-Instytut`: OK (33 wpisy WW, złych linii bloków 0; nagłówki `##` bez `{#id}`: 2, sprzed zlecenia).

### Ochrona zmian redaktorów (Web-Instytut)
- Baza `645a832` (HEAD po 53). Tuż przed pushem: `git fetch`, `git log 645a832..origin/main` — **0 zapisów**; ostatni zapis redaktora `2328a0d` 18.11 23:41 (cisza spełniona).
- **Skrypt jeszcze raz na świeżym main** (osobne drzewo robocze z `origin/main`): ten sam wynik — 32 pliki, 87 zamian, każdy plik bajt w bajt taki jak na gałęzi.
- `kontrola_redaktorow.py przed --baza 645a832`: „Zapisów od bazy: 0. OK”.
- Po pushu `kontrola_redaktorow.py po --przed 645a832 --po origin/main`: zmienione pola `body` (32 pliki), `tresc_en` (5), `karta` (1: zajawka i zajawka EN Tabisza), `lata` (1: Rolski). Narzędzie zgłasza je jako „niedozwolone”, bo zna tylko migrację terminów (jak w 52 i 53); z `--pomin body --pomin karta --pomin lata --pomin tresc_en`: „OK, tylko zmiany z migracji”. Każda z tych zmian pochodzi z tabeli skryptu (`A02…`, zajawki Tabisza w liniach 91–95, `lata` Rolskiego w liniach 196–197). `git diff --numstat`: 33 pliki (32 WW + `.pages.yml`), +182 −120.

### Podgląd
Budowa Web-Podglad `44508857543` (tresc-zmieniona, 10:47 UTC): build i deploy — **zielone**. Na żywo: opis strony Tabisza „Matematyk, wieloletni pracownik…”, „Prof. Andrzej Krzywicki należy…”, Rolski „ur. 1946”. Push Web-Core `f12aeb15` zmienia tylko `dok/`, więc przekaźnik nie uruchamiał osobnej budowy.

### Do raportu (bez zmian w tym zleceniu)
**Pilnowanie stylu na przyszłość — dwa warianty do decyzji:**
1. **Ostrzeżenie** w `sprawdz_tresci.py` i w logu budowy (`ostrzezWW`): pogrubienie, które nie jest hasłem na początku akapitu wyliczenia ani rokiem w `:::laureaci`; „Prof./prof./Profesor/dr hab.” przed imieniem i nazwiskiem bohatera po pierwszym zdaniu sylwetki; „(ur. …)” albo „(1900–1980)” i myślnik definicji w pierwszym zdaniu.
   - Koszt: ok. 1,5–2 h (reguły w Pythonie i TS, testy). Logika pogrubień jest gotowa w `tresci-C/z54-kontrola.py` (te same wyrażenia). Ryzyko: fałszywe alarmy przy tytułach — reguła musi łapać tytuł **przed nazwiskiem**, nie samo słowo „profesor” (kontrola znalazła 41 wystąpień „profesor…” w opisach kariery, wszystkie poprawne).
2. **Strona sama zdejmuje pogrubienia** przy renderowaniu (jak autokorekta nagłówków z 53, z wpisem w logu budowy).
   - Koszt: ok. 1–1,5 h (wtyczka remark, testy). Działa tylko dla pogrubień; tytułów i pierwszego zdania nie da się poprawić automatycznie. Minus: redaktor widzi pogrubienie w CMS, a na stronie go nie ma, więc nie wie, że zrobił coś wbrew zasadzie.
   - **Rekomendacja:** wariant 1 (ostrzeżenia), ewentualnie z wariantem 2 tylko dla pogrubień, ale zawsze z ostrzeżeniem w logu.

**Inne miejsca z „prof. dr hab.” albo pogrubionymi nazwiskami poza „Warto wiedzieć”** (tylko lista; pełna lista plików: `tresci-C/z54-tytuly-poza-ww.txt`):
- „prof. dr hab.”: Web-Nauka — 27 plików (wszystkie w `granty/`), Web-Aktualnosci — 20 (17 `aktualnosci/`, 3 `obrony/`), Web-Studia — 7 (`strony/studia` 3+1, `kierunki` 2, `specjalnosci` 1).
- Pogrubione „**Prof./Dr Nazwisko**”: Web-Aktualnosci 3 wpisy (`2016-12-03-profesorowie-biler-i-januszkiewicz-…`, `2026-11-10-seminarium-wydzialowe-problem-milenijny`, `2026-11-18-nagroda-im-prof-andrzeja-hulanickiego-…`), Web-Studia 5 plików (`kierunki/isim.md`, `matematyka.md`, `siad.md`, `szkola-doktorska.md`, `strony/studia/pierwszy-rok.md`).

**Uwaga o generatorze:** `skrypty/migracja/formularze_40.mjs` (`WARTO_WIEDZIEC_47`) nie ma nowych zdań „Styl: …” w opisach Treści WW — zlecenie ograniczało zmiany w Web-Core do `dok/`. Gdyby ktoś wygenerował `.pages.yml` Web-Instytut od nowa, zdania znikną; dopisanie ich do generatora to kilka minut przy następnym zleceniu formularzy.

---

## Część B — seminarium wydziałowe znów jako „Wydarzenie” (cofnięcie 49)

### Web-Core (`6193ddfd`)
- **Cofnięty `a5779a75`** (`git revert --no-commit`, bez konfliktów; od 49 te pliki zmieniły tylko 52–54 w innych miejscach, które zostały): `i18n.ts` bez obu wpisów `seminarium-wydzialowe`; `tresci.ts` bez `jakWydarzenie`, `rodzajWiersza`, pól `rodzajWpisu` i `opisLang`; `aktualnosc.ts` i `Aktualnosc.astro` znów `d.rodzaj === 'wydarzenie'`; `WierszWydarzenia.astro` — opis tylko przy referacie, etykieta z `w.rodzaj`; `DrugiEkran.astro` — `RODZ_WYD` bez seminarium; `listaAktualnosci.ts` — filtr bez seminarium; `patroni.ts` — „1. sukces, obrona → Nauka”.
- **`content.config.ts`:** w `z.enum` cztery wartości (`ogloszenie`, `wydarzenie`, `sukces`, `kariera`); `preprocess` zamienia `seminarium-wydzialowe` na `wydarzenie`, z komentarzem „zlecenie 49 cofnięte w 54”.
- **`sprawdz_tresci.py`:** bez ostrzeżenia 49 („bez terminu”); nowe: „stary rodzaj „Seminarium wydziałowe” — strona traktuje wpis jak „Wydarzenie”; zmień Rodzaj w CMS” (dalej plik sprawdzany jak wydarzenie, np. ostrzeżenie o braku terminu).
- **`formularze_40.mjs`:** opis kolekcji dokładnie jak w B1 (zgodny z `.pages.yml` — sprawdzone porównaniem tekstu); komentarz o 49 usunięty.
- **`skrypty/test-edytora/formularz.mjs`:** scenariusz 12 to krótka kontrola (opcje, opisy bez seminarium, oba wpisy zapisane bez zmian = pusty diff) i nie pomija się już po cichu; komentarz w nagłówku poprawiony. Commit 49 ze scenariuszem (`5dd156f5`) nie był cofany osobno — scenariusz napisany od nowa.
- **Ściągawka:** punkt „Seminarium wydziałowe” brzmi dokładnie jak w B4.

### Web-Aktualnosci (`d9e2f3e`)
- **`.pages.yml`, tylko trzy miejsca:** opcja `seminarium-wydzialowe` usunięta (kolejność: Ogłoszenie, Wydarzenie, Sukces, Kariera); opis pola „Rodzaj” = samo zdanie o „Karierze”, jak przed 49 (bez cudzysłowu YAML, bo nie ma dwukropka); opis kolekcji bez seminariów. Plik się parsuje.
- **Tytuły (B5):** wszystkie cztery pola miały dokładnie wartości z kolumny „Jest”, więc zmienione: Karch — „Seminarium wydziałowe — prof. Grzegorz Karch” / „Faculty seminar — Prof. Grzegorz Karch”; Vitek — „Seminarium wydziałowe — prof. Olga Vitek” / „Faculty seminar — Prof. Olga Vitek”. Nazwy plików, zajawki, treść i reszta pól bez zmian.
- Wpis „Rusza tutornia” bez zmian (punkt 9 zlecenia 49 zostaje; na jego stronie zmienia się tylko tytuł sąsiedniego wpisu w „Nowszy / Starszy wpis”).

### Porównanie HTML przed i po (`TYLKO_OPUBLIKOWANE=1`, `z54a-pub` → `z54b-pub`, PL i EN)
4969 plików w obu; identyczne 4836, tylko czas 104, sitemap 1, **zmienione 28** (`tresci-C/z54b-roznice.txt`) — **wyłącznie tytuły dwóch wpisów**: strony wpisów (tytuł, `<title>`, `og:title`), lista Aktualności, Kalendarz, strona główna, RSS, `wydarzenia.ics`, `wszystko.ics` i `.ics` obu wpisów, „Nowszy / Starszy wpis” na sąsiednich wpisach, strona zakładu Równań Różniczkowych i strona Studiów (lista aktualności). Filtra „Seminaria wydziałowe” nie było też przed zmianą (żaden wpis nie miał tego rodzaju), więc w HTML brak różnicy. Liczby w banerach i na okładce bez zmian. Innych różnic brak.

### Wpis testowy (kopia lokalna, usunięta po próbie)
`2026-11-19-test-54-stary-rodzaj.md` z `rodzaj: seminarium-wydzialowe` i terminem 22.11.2026 13:00 (za 3 dni): budowa `z54b-test` przechodzi; w Kalendarzu wiersz „Wydarzenie · niedz. 13:00 · sala 119”, `data-rodzaj="wydarzenie"`; strona wpisu z etykietą „Wydarzenie”; jest w `wydarzenia.ics`; `sprawdz_tresci.py` — 1 ostrzeżenie o starym rodzaju. Zrzut `z54b-kalendarz-test-stary-rodzaj-1920.png`.

### Adres `?rodzaj=seminarium-wydzialowe`
Lista Aktualności (PL i EN) z tym parametrem i z dowolnym nieznanym (`?rodzaj=xyz`) pokazuje wszystkie wpisy (158 z 158), w panelu zaznaczone „Wszystkie”/„All”, konsola czysta; `?rodzaj=wydarzenie` dalej filtruje (7). Bez zmian w kodzie — tak działa nieznany `?rodzaj=` (skrypt `tresci-C/z54b-rodzaj.mjs`).

### Formularz i kontrole
- **Symulator** (`node skrypty/test-edytora/formularz.mjs ../tresci-C`, log `tresci-C/z54b-formularz.log`): scenariusz 12 — 5/5 OK (opcje, opis pola, opis kolekcji, oba wpisy: pusty diff). Wynik całości „Problemów: 1” to znane od 48 „6 znanych różnic” w „Zapisie bez zmian” (5 obron i 1 grant z pustą Treścią dostają komentarz-szablon); ten sam wynik daje wersja symulatora sprzed zmiany (`z54b-formularz-stary.log`).
- `sprawdz_pola_cms.py ../tresci-C`: 753 pliki w 16 repozytoriach, **0 problemów**;
- `astro check`: 0 błędów, 0 ostrzeżeń, 8 podpowiedzi; `test:jawne` 84/84; `sprawdz_tresci.py`: OK, 594 pliki, 0 ostrzeżeń;
- pozostałości 49 w kodzie: brak (`seminarium-wydzialowe` tylko w preprocess, ostrzeżeniu i nazwach plików w symulatorze).
- **PDF-y dla redaktorów** (Web-Podglad `dla-redaktorow/`: `Czat-AI-formatowanie-tresci.pdf`, `Mapa-CMS-IM-UWr.pdf`): nie wymieniają rodzaju „Seminarium wydziałowe” (tekst wyciągnięty `pdftotext`; „seminari…” tylko w opisie repozytoriów seminariów). Nic do poprawy.

### Zrzuty (`raport-zrzuty/z54-zrzuty/`, konsola: 0)
`z54b-karch-1920.png`, `z54b-karch-390.png` (cała strona), `z54b-karch-en-1920.png`, `z54b-kalendarz-archiwum-karch-1920.png` i `z54b-kalendarz-wiersz-karch.png` (wiersz „Wydarzenie · wt. 13:00 · Instytut Informatyki sala 119”; wpis jest miniony, więc w widoku „Archiwum”), `z54b-kalendarz-test-stary-rodzaj-1920.png`, `z54b-aktualnosci-lista-1920.png` (panel „Pokaż”), `z54b-aktualnosci-stary-parametr-1920.png`.

### Ochrona zmian redaktorów (Web-Aktualnosci)
- Baza `eee693e` (ostatni zapis właściciela w CMS 19.11 01:28 — cisza spełniona). Przed pushem `git fetch`: 0 zapisów od bazy; `kontrola_redaktorow.py przed --baza eee693e`: „OK, wszystkie wartości redaktorów są w wyniku”.
- Po pushu `kontrola_redaktorow.py po --przed eee693e --po origin/main`: zmienione tylko `tytul` (2) i `tytul_en` (2) — dokładnie tabela B5 (narzędzie zgłasza je jako „niedozwolone”, bo nie zna tej zmiany; z `--pomin tytul --pomin tytul_en`: „OK”). `git diff --numstat`: `.pages.yml` +2 −4, dwa wpisy po +2 −2.

### Podgląd
Przekaźnik Web-Core (`6193ddfd`) i push Web-Aktualnosci: budowa `przebuduj` anulowana przez następną, budowa Web-Podglad `44510538471` (tresc-zmieniona, 10:58–10:59 UTC) — **zielona**. Na żywo: „Seminarium wydziałowe — prof. Grzegorz Karch”, EN „Faculty seminar — Prof. Olga Vitek”; na liście Aktualności brak „Seminaria wydziałowe”.

### Po pushu — krok dla właściciela
Otwórz formularz Aktualności w Pages CMS: „Rodzaj” ma 4 opcje (Ogłoszenie, Wydarzenie, Sukces, Kariera), opis pola i kolekcji bez seminariów; formularz się otwiera.

### Do raportu (część B)
**Tytuł wykładu (zajawka) pod tytułem wiersza w Kalendarzu przy każdym wydarzeniu z Aktualności** — tylko ocena: dotyczy **8 wierszy** w Kalendarzu (PL i EN; 7 w Archiwum, 1 nadchodzący), wszystkie 8 wpisów ma zajawkę (63–141 znaków, mediana 107). Wiersz wyglądałby jak wiersz referatu (opis drobniej pod tytułem, jak 31 referatów z opisem). Przy zajawce typu „W imieniu Dziekana zapraszamy…” powtarzałaby się treść tytułu, więc sens ma głównie przy seminarium wydziałowym (tytuł wykładu). Zmiana w kodzie: jedna linia w `WierszWydarzenia.astro` (warunek `zOpisem`) + `opisLang`; nie wdrażałem.

---

## Decyzje podjęte domyślnie (bez właściciela)
- Push bez „push” właściciela i bez wiadomości do redaktorów — wg polecenia z 19.11 (cisza w repozytorium treści zamiast „wieczorem”).
- B5: tytuły zmienione, bo wszystkie miały dokładnie wartości z kolumny „Jest”.
- Opis pola „Rodzaj”: bez cudzysłowu YAML (jak przed 49; tekst nie ma dwukropka).
- `sprawdz_tresci.py`: plik ze starym rodzajem sprawdzany dalej jak „wydarzenie” (np. ostrzeżenie o braku terminu) — spójne z tym, jak czyta go strona.

## Do obejrzenia na Podglądzie
- https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/krzysztof-tabisz/ (i `/en/…`)
- https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/marek-bozejko/ i `/tomasz-rolski/` (rozwiń „Źródła”)
- https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/bronislaw-knaster/, `/medal-uniwersytetu/`, `/artykul-w-annals-of-mathematics/`
- https://im-uwr.github.io/Web-Podglad/aktualnosci/2026-11-10-seminarium-wydzialowe-problem-milenijny/ i https://im-uwr.github.io/Web-Podglad/kalendarz/#archiwum
