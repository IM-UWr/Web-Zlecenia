# Zlecenie 53 (19.11.2026): autokorekta nagłówków w Treści „Warto wiedzieć”, „Zobacz też” zamiast „W »Warto wiedzieć«” na stronie sylwetki, wszystkie sylwetki opublikowane, bez „Do pobrania” u Bożejki i Rolskiego

**Zastępuje zlecenie 51.** Autokorekta nagłówków (punkty 1, 2, 4 i 5) to treść zlecenia 51 z 18.11. Plik 51 zostaje bez zmian jako zapis, ale **51 nie wykonuj osobno**: wszystko z niego jest tutaj, dostosowane do stanu po 52.

**Kolejność: po zleceniu 52.** Właściciel 18.11 o 23:58 odłożył 51, a 19.11 o 00:31 przywrócił autokorektę jako następne zlecenie („autokorektor pójdzie jako kolejne zlecenie”). Pracuj na `main` z wdrożonym 52, bo oba zmieniają `src/lib/wartoWiedziec.ts` (`trescWW`) i `src/views/SylwetkaWW.astro`. Numery linii niżej pochodzą sprzed 52, więc szukaj po nazwach.

**Skąd to zlecenie.** Redaktor wkleił do CMS Treść sylwetki Tabisza w postaci typowej dla czatów AI (Web-Instytut `2328a0d`, 18.11, 23:19–23:41):

```
# Dr Krzysztof Tabisz

**Dr Krzysztof Tabisz (ur. 1950)** – …

### Działalność naukowa i akademicka{#DzialalnoscNaukowa}
…
### Działalność społeczna i opozycyjna {#DzialalnoscSpoleczna}
…
### Odznaczenia i wyróżnienia {#Odznaczenia}
```

Treść EN ma ten sam układ: `# Dr Krzysztof Tabisz` i trzy `###`, bez `{#id}`.

**Skutek na stronie:**
- **Nie było sekcji ani kresek.** `trescWW` dzieli Treść tylko po `<h2`, więc cały tekst stał się „wstępem”.
- **Śródtytuły były złote.** To `h3` w prozie w kolorze działu.
- **Nie było „Na tej stronie”.** Spis miał jedną pozycję, a pokazuje się od 2.
- **Był drugi `h1`** pod tytułem z banera.
- **`{#…}` było widać jako tekst.**

Zlecenie 52 porządkuje sam plik Tabisza (punkt 6). To zlecenie sprawia, że strona sama poradzi sobie z następnym takim tekstem („strona bezobsługowa”).

**Decyzje właściciela:**
- **18.11, 23:47:** zlecenie korygujące; strona ma sama poprawnie pokazać taki tekst, bez wołania redaktora.
- **19.11, 00:31:** autokorekta idzie jako zlecenie po 52.
- **19.11, 00:33:** zapisać to wszystko jako zlecenie 53, bez nadpisywania 51.
- **19.11, 00:40:** „Zobacz też” zostaje („teraz rozumiem koncepcję, ok”).
- **19.11, 00:40:** u Bożejki i Rolskiego usunąć „Do pobrania” z notami biograficznymi, bo nota stoi też w „Źródłach” („to się dubluje”); lepsze źródła niż nota szukają agenci w czacie, osobno (punkt 7).
- **19.11, 00:37:** akceptacją tekstów osób żyjących zajmą się redaktorzy przed publikacją strony („będzie ok”), więc publikujemy wszystkie sylwetki już teraz.
- **19.11, 00:31:** na stronie sylwetki nagłówek „W »Warto wiedzieć«” znika, bo „jesteśmy w tym dziale, to trochę dublowanie”.
- **19.11, 00:32:** „włącz wszystkie strony sylwetek jako opublikowane” (punkt 6). Cofa to decyzję domyślną zlecenia 47 („osoby żyjące jako szkic do czasu akceptacji tekstu”) dla obecnych 18 sylwetek.

**Decyzja domyślna** (zmiana na prośbę właściciela): nowy nagłówek to **„Zobacz też”** (EN „See also”).
- Każdy wiersz pod nim ma już nazwę swojej grupy („Nagrody i wyróżnienia” albo „Historie”), więc nagłówek z nazwą grupy powtarzałby ją.
- Strony nagrody i historii też używają „Zobacz też w »…«”.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- Raport `RAPORT-ZLECENIE-53.md`, zrzuty `raport-zrzuty/z53-*`. Bez subagentów.
- **Repozytoria:** Web-Core (punkty 1–5) i **Web-Instytut** (punkt 6: pole `opublikowany` w 6 plikach; punkt 7: sekcja „Do pobrania” w 2 plikach; `.pages.yml` bez zmian).
- **Ochrona zmian redaktorów (jak w zleceniach 31, 40, 47 i 52).** Redaktorzy właśnie edytują sylwetki.
  - Zawsze od świeżego `main`, zwykły commit, bez force-push. Baza = HEAD zanotowany na początku pracy.
  - Zmiany skryptem w miejscu (punkt 6: jedna linia `opublikowany: false` → `opublikowany: true`; punkt 7: usunięcie jednej sekcji), nie kopiowaniem plików.
  - Tuż przed pushem `git fetch` i `git log <baza>..origin/main`. Jeśli redaktor zmienił któryś z 6 plików, uruchom skrypt jeszcze raz na świeżym `main`.
  - Kontrola przed pushem i po nim: w każdym pliku różnica to dokładnie opisane linie (punkt 6: jedna linia; punkt 7: sekcja „Do pobrania”). Wynik w raporcie.
  - Push wieczorem albo po wiadomości właściciela do redaktorów („zapiszcie i zamknijcie CMS na 15 minut”).
- **Kolejność pushy:** Web-Core, potem Web-Instytut.

## Stan dziś (przed 52: Web-Core `0c07b56`, Web-Instytut `2328a0d`)
- `src/lib/wartoWiedziec.ts`, `trescWW`:
  - `renderMarkdownZNaglowkami(src, lang, false, { ww })`;
  - potem `html.split(/(?=<h2[\s>])/)` daje wstęp i sekcje, a sekcja `{#zrodla}` idzie osobno.
- `src/plugins/remark-jawne-bloki.mjs` (`visit`, warunek `heading.depth === 2`): `{#id}` działa tylko przy `##`, z regexem `/\s+\{#(…)\}\s*$/u`.
- Z tego samego `trescWW` korzystają sylwetki (`SylwetkaWW.astro`) oraz nagrody i historie (`WartoWiedziecWpis.astro`).
- Procesory w `markdown.ts` są w pamięci podręcznej według klucza `lang:jawne:limityLinii`. Reguły z punktu 1 włączaj więc przy renderowaniu (np. przez `strona.ww` we frontmatterze), a nie przy tworzeniu procesora, żeby nie przeszły na inne strony.
- **Nagłówek powiązań:** `SylwetkaWW.astro`, `const wWW = lang === 'en' ? \`In ${tytulListy}\` : \`W „${tytulListy}”\``. Używają go `h2#w-warto-wiedziec-h` i pozycja spisu `w-warto-wiedziec`.

## Docelowo

### 1. Porządkowanie nagłówków w Treści „Warto wiedzieć” (PL i EN, wszystkie trzy grupy)
Reguły działają tylko przy renderowaniu Treści WW (tryb `ww`), przed podziałem na sekcje. Dotyczą tylko nagłówków na najwyższym poziomie dokumentu (nie tych wewnątrz bloków `:::`).
- **A. Tytuł na początku znika.**
  - Usuwany jest pierwszy nagłówek `#`, przed którym nie ma prozy (najwyżej komentarze `<!-- … -->` albo blok `:::w-skrocie`), jeśli jego tekst zawiera tytuł wpisu albo tytuł zawiera jego tekst.
  - Porównanie bez wielkości liter, polskich znaków, interpunkcji i podwójnych spacji.
  - Tytuł: dla PL `tytul`; dla EN `tytul_en`, a gdy jest pusty, `tytul`. Przekaż go w opcji `ww` z `trescWW`.
  - Przykład: „Dr Krzysztof Tabisz” zawiera „Krzysztof Tabisz”, więc nagłówek znika.
- **B. Pozostałe `#` stają się `##`.** Na stronie jest jeden `h1` (baner).
- **C. Gdy nie ma `##`, najwyższy poziom staje się `##`.** Jeśli po A i B w Treści nie ma żadnego `##`, najpłytszy z użytych poziomów (`###`–`######`) staje się `##`, a głębsze przesuwają się o tyle samo (np. `###` → `##`, `####` → `###`).
- **Treść, która ma już `##`, zostaje bez zmian** (poza regułami A i B). Po 52 dotyczy to wszystkich wpisów WW.
- **Ostrzeżenie w logu budowy** (`ostrzezWW`, jak przy „Lata: nie data”), osobno dla Treści EN, np. `…/plik.md: nagłówki poprawione automatycznie — usunięty tytuł „# Dr Krzysztof Tabisz”, ### → ## (3)`.
- **Bez ramki na Podglądzie:** strona wygląda dobrze, więc redaktor nie ma czego poprawiać.

### 2. `{#id}` także bez spacji i przy każdym poziomie (wszystkie strony z jawnym Markdownem)
- Regex `\s+\{#` zamień na `\s*\{#`, żeby `## Tytuł{#id}` działało jak `## Tytuł {#id}`.
- Przy `###` i głębszych `{#id}` też znika z tekstu i daje `id` nagłówka (bez sekcji i bez pozycji w spisie).
- Kolejność: najpierw punkt 1 (zmiana poziomów), potem `{#id}`. Wtedy `### …{#DzialalnoscNaukowa}` po zmianie na `##` daje sekcję `DzialalnoscNaukowa`.

### 3. Strona sylwetki: „Zobacz też” zamiast „W »Warto wiedzieć«”
- **`SylwetkaWW.astro`:**
  - nagłówek sekcji powiązań: „Zobacz też” (EN „See also”), także w spisie „Na tej stronie”;
  - id sekcji `zobacz-tez`, nagłówka `zobacz-tez-h` (dziś `w-warto-wiedziec`; nikt do niego nie linkuje, sprawdź `grep`);
  - zmienna `tytulListy` niepotrzebna w tym miejscu, jeśli nic innego jej nie używa.
- **Zawartość sekcji bez zmian:** te same wiersze (nagrody i historie, które linkują do osoby) z nazwą grupy pod tytułem, jak na zrzucie z 19.11 (Medal Uniwersytetu Wrocławskiego · Nagrody i wyróżnienia · 2 laureatów z Instytutu).
- **Komentarze i dokumentacja:** wszystkie wzmianki „W »Warto wiedzieć«” w znaczeniu tej sekcji zamień na „Zobacz też”:
  - `SylwetkaWW.astro` (komentarz na początku);
  - `src/components/WartoWiedziec.astro` (linie ok. 4 i 25);
  - `src/lib/wartoWiedziec.ts` (ok. 190);
  - `src/lib/widoki/wartoWiedziecWpis.ts` (ok. 35);
  - `dok/sciagawka-edytora.md` (ok. 185 i 188);
  - `dok/jawny-markdown.md` (ok. 225);
  - `dok/en/TLUMACZENIA.md`: wiersz „sylwetka — powiązania” → „Zobacz też | See also”.
- **Strony nagrody i historii** („Zobacz też w »Historie«” / „w »Nagrody i wyróżnienia«”) bez zmian.

### 4. Testy (`src/plugins/jawne-bloki.test.mjs` albo `ww.test.mjs`)
- **Tabisz w miniaturze:** `# Dr X Y`, akapit i 3× `###` z `{#id}` (jeden bez spacji). Wynik: 0 × `h1`, akapit we wstępie, 3 sekcje z właściwymi `id`, brak `{#` w HTML.
- `# Inny nagłówek` na początku (nie tytuł) daje sekcję `##`.
- Treść z `##` i `###` zostaje bez zmian.
- `###` i `####` bez `##` dają `##` i `###`.
- Nagłówek wewnątrz bloku `:::` zostaje bez zmian.
- `## Tytuł{#id}` w trybie jawnym bez `ww` (np. kierunek): `id` działa, w tekście nie ma `{#id}`.

### 5. Dokumentacja
- `dok/jawny-markdown.md` i `dok/sciagawka-edytora.md` (część „Warto wiedzieć”): krótko, że strona sama usuwa `#` z imieniem lub tytułem i traktuje `###` jak sekcje, gdy w Treści nie ma `##`. Zalecany zapis to nadal `## Tytuł {#id}`.
- Komentarz przy kodzie reguł z ich opisem i odwołaniem do zlecenia 53 (dawniej 51).

### 6. Wszystkie sylwetki opublikowane (Web-Instytut, decyzja 19.11, 00:32)
- **Stan na 18.11, 23:41 (`2328a0d`):** 12 sylwetek ma `opublikowany: true`, a 6 ma `opublikowany: false`:
  - `marek-bozejko.md`;
  - `tomasz-rolski.md`;
  - `piotr-biler.md`;
  - `roman-duda.md`;
  - `wladyslaw-narkiewicz.md`;
  - `andrzej-krzywicki.md`.
- **Zmiana:** w tych 6 plikach `opublikowany: true`. Nic poza tym (pola, Treść, „Dodano” bez zmian). Jeśli przed pushem któryś plik ma już `true` albo pojawiła się nowa sylwetka ze szkicem, wypisz to w raporcie i nie ruszaj nowych plików bez pytania.
- **Skutek:** wszystkie 18 sylwetek widać w budowie publicznej (`TYLKO_OPUBLIKOWANE=1`):
  - w siatce i w liczbie w banerze listy (17 sylwetek bez TBA, dziś 11);
  - w „Innych sylwetkach”, na stronie głównej, w mapie strony i w wyszukiwarce;
  - linki do nich w laureatach i w tekstach innych sylwetek znów są linkami z portretem.

  Znaczek „szkic” (Podgląd) znika.
- **Bez zmian:** opis kolekcji „Sylwetki” w `.pages.yml` i ściągawka („Sylwetka osoby żyjącej: odznacz »Opublikowane«, dopóki osoba nie zaakceptuje tekstu”). To zasada na przyszłość; jej zmiana tylko na prośbę właściciela (do raportu).

### 7. Bożejko i Rolski bez „Do pobrania” (Web-Instytut, decyzja 19.11, 00:40)
- **Pliki:** `src/content/warto_wiedziec/sylwetki/marek-bozejko.md` i `tomasz-rolski.md`.
- **Usuń w Treści PL** całą sekcję od `## Do pobrania {#do-pobrania}` do linii przed `## Źródła {#zrodla}`:
  - nagłówek;
  - komentarz `<!-- PLIKI: … -->`;
  - blok `:::pliki` z notą biograficzną;
  - puste linie wokół, tak żeby przed `## Źródła` została jedna pusta linia.
- **Bez zmian:**
  - sekcja „Źródła” (nota zostaje tam na razie jedynym źródłem; nowe źródła przyjdą osobnym zleceniem po poszukiwaniach);
  - pliki PDF w `public/pliki/aktualnosci/` (linkuje do nich też aktualność o medalach i „Źródła”);
  - reszta Treści i pola.
- **Skutek na stronie:** u obu osób nie ma sekcji „Do pobrania” ani jej pozycji w spisie „Na tej stronie”.
- **Treść EN:** obie sylwetki mają ją pustą (sprawdź); jeśli przed pushem redaktor dopisał EN z „Downloads”, usuń tam tę samą sekcję.

## Odbiór lokalny
- **Wpis testowy (tylko lokalnie, nie do repozytorium):**
  - skopiuj Tabisza w wersji sprzed 52 (Web-Instytut `2328a0d`, `src/content/warto_wiedziec/sylwetki/krzysztof-tabisz.md`) do lokalnego klonu treści jako `test-naglowki.md`, z `tytul: Test Nagłówków`;
  - pierwszą linię Treści PL zamień na `# Dr Test Nagłówków`, a EN na `# Dr Test Nagłówków`;
  - po odbiorze plik usuń.
- **Porównanie HTML przed i po** (PL i EN, te same klony treści po 52, bez wpisu testowego). Dozwolone różnice:
  - na stronach sylwetek z powiązaniami: nagłówek i pozycja spisu „Zobacz też” / „See also” oraz nowe `id` (punkt 3);
  - strony z `{#id}` bez spacji albo przy `###` (punkt 2): wypisz je w raporcie z adresem i nagłówkiem.

  Każdą inną różnicę zgłoś. Sama autokorekta (punkt 1) na prawdziwych treściach po 52 nie powinna zmienić niczego.
- **Strona wpisu testowego (PL):**
  - jeden `h1`;
  - wstęp to akapit „Dr Krzysztof Tabisz (ur. 1950)…”;
  - trzy sekcje `#DzialalnoscNaukowa`, `#DzialalnoscSpoleczna` i `#Odznaczenia` z czarnymi `h2` i kreskami, jak u Steinhausa;
  - „Na tej stronie” z sekcjami;
  - nigdzie nie ma `{#`.
- **Strona wpisu testowego (EN):** to samo, z identyfikatorami sekcji nadanymi automatycznie.
- **Log budowy:** ostrzeżenie przy wpisie testowym (PL i EN), bez nowych ostrzeżeń przy innych wpisach.
- **Budowa z `TYLKO_OPUBLIKOWANE=1` po zmianie punktu 6:** 18 kart w siatce sylwetek, baner listy „17 sylwetek”, linki do Bożejki i Rolskiego w „Laureaci z Instytutu” przy Medalu UWr z mini portretami, żadnego znaczka „szkic”.
- **Zrzuty:**
  - wpis testowy PL i EN przy 1920×1080, 1366×768 i 390 px, w trybie jasnym i ciemnym;
  - sylwetka Bożejki (ma powiązanie z Medalem UWr) z „Zobacz też” przy 1920×1080, PL i EN.
- **Kontrole:**
  - `astro check` bez nowych błędów;
  - testy wtyczek zielone;
  - `sprawdz_tresci.py` i `sprawdz-jawny-markdown.mjs` bez problemów;
  - konsola czysta.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Wpis testowy w stylu Tabisza sprzed 52 (PL i EN) wygląda jak inne sylwetki: sekcje z kreskami, czarne nagłówki, spis po prawej, jeden tytuł, bez `{#…}` w tekście.
- [ ] Prawdziwe wpisy WW (po 52) bez zmian w HTML poza „Zobacz też”.
- [ ] `{#id}` działa bez spacji i przy każdym poziomie na wszystkich stronach z jawnym Markdownem.
- [ ] Ostrzeżenie w logu przy automatycznej poprawce.
- [ ] Na stronie sylwetki „Zobacz też” / „See also” zamiast „W »Warto wiedzieć«” / „In Highlights”, w nagłówku i w spisie.
- [ ] Testy z punktu 4 zielone, dokumentacja i `TLUMACZENIA.md` zgodne z działaniem.
- [ ] Bożejko i Rolski bez „Do pobrania” (sekcja i pozycja w spisie); „Źródła” i pliki PDF bez zmian.
- [ ] Wszystkie 18 sylwetek ma `opublikowany: true` i są widoczne w budowie publicznej. W Web-Instytut zmieniona tylko ta jedna linia w 6 plikach, zapisy redaktorów zachowane (kontrola przed pushem i po nim).

## Do raportu (bez zmian w tym zleceniu)
- **Zasada „osoba żyjąca = szkic”** w opisie kolekcji „Sylwetki” i w ściągawce: zostaje czy znika po decyzji z punktu 6 (akceptacja tekstów przez redaktorów przed publikacją strony, 19.11, 00:37)? Do decyzji właściciela.
- **Inne kolekcje z jawnym Markdownem** (kierunki, specjalności, strony Instytutu, strony działów itd.): czy gdzieś jest Treść bez `##`, a z `#` albo `###`. Wypisz pliki. Właściciel zdecyduje, czy rozszerzyć regułę z punktu 1.
