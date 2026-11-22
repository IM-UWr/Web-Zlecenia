# Zlecenie 51: nagłówki w Treści „Warto wiedzieć” wpisane inaczej niż `##` (sylwetka Tabisza, 18.11.2026)

**Skąd to zlecenie.** Redaktor wpisał w CMS Treść sylwetki `Web-Instytut/src/content/warto_wiedziec/sylwetki/krzysztof-tabisz.md` (commity `eed461a`–`2328a0d`, 18.11, 23:19–23:41) tak:

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

**Na Podglądzie** (`/instytut/warto-wiedziec/krzysztof-tabisz/`):
- **Nie ma sekcji ani kresek.** `trescWW` dzieli Treść tylko po `<h2`, więc cały tekst jest „wstępem”.
- **Śródtytuły są złote.** To `h3` w prozie w kolorze działu (`zal-tresc.css`, ok. 169).
- **Nie ma „Na tej stronie”.** Spis ma jedną pozycję („Inne sylwetki”), a `SpisStrony.astro` pokazuje go od 2.
- **Jest drugi `h1`** („Dr Krzysztof Tabisz”) pod tytułem z banera.
- **`{#…}` widać jako tekst**, bo `remark-jawne-bloki.mjs` (ok. 53–59) czyta je tylko przy `##` i tylko po spacji.

**Decyzja właściciela (18.11, 23:47):** zlecenie korygujące. Strona ma sama poprawnie pokazać taki tekst, bez wołania redaktora („strona bezobsługowa”). Plik Tabisza zostaje taki, jak go zapisał redaktor.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- Raport `RAPORT-ZLECENIE-51.md`, zrzuty `raport-zrzuty/z51-*`. Bez subagentów.
- Zmiana tylko w Web-Core. Repozytoria treści i `.pages.yml` bez zmian (redaktorzy właśnie pracują w Web-Instytut), więc sekcja „Ochrona zmian redaktorów” nie dotyczy tego zlecenia.

## Stan dziś (Web-Core `0c07b56`, Web-Instytut `2328a0d`)
- `src/lib/wartoWiedziec.ts`, `trescWW` (ok. 216–234):
  - `renderMarkdownZNaglowkami(src, lang, false, { ww })`;
  - potem `html.split(/(?=<h2[\s>])/)` daje wstęp i sekcje, a sekcja `{#zrodla}` idzie osobno.
- `src/plugins/remark-jawne-bloki.mjs` (ok. 53–59): `{#id}` działa tylko przy `heading.depth === 2`, z regexem `/\s+\{#(…)\}\s*$/u`.
- Z tego samego `trescWW` korzystają sylwetki (`SylwetkaWW.astro`) oraz nagrody i historie (`WartoWiedziecWpis.astro`).
- Procesory w `markdown.ts` są w pamięci podręcznej według klucza `lang:jawne:limityLinii`. Reguły z punktu 1 włączaj więc przy renderowaniu (np. przez `strona.ww` we frontmatterze), a nie przy tworzeniu procesora, żeby nie przeszły na inne strony.

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
- **Treść, która ma już `##`, zostaje bez zmian** (poza regułami A i B). Dziś dotyczy to wszystkich wpisów WW poza Tabiszem.
- **Ostrzeżenie w logu budowy** (`ostrzezWW`, jak przy „Lata: nie data”), osobno dla Treści EN, np. `…/krzysztof-tabisz.md: nagłówki poprawione automatycznie — usunięty tytuł „# Dr Krzysztof Tabisz”, ### → ## (3)`.
- **Bez ramki na Podglądzie:** strona wygląda dobrze, więc redaktor nie ma czego poprawiać.

### 2. `{#id}` także bez spacji i przy każdym poziomie (wszystkie strony z jawnym Markdownem)
- Regex `\s+\{#` zamień na `\s*\{#`, żeby `## Tytuł{#id}` działało jak `## Tytuł {#id}`.
- Przy `###` i głębszych `{#id}` też znika z tekstu i daje `id` nagłówka (bez sekcji i bez pozycji w spisie).
- Kolejność: najpierw punkt 1 (zmiana poziomów), potem `{#id}`. Wtedy `### …{#DzialalnoscNaukowa}` po zmianie na `##` daje sekcję `DzialalnoscNaukowa`.

### 3. Testy (`src/plugins/jawne-bloki.test.mjs` albo `ww.test.mjs`)
- **Tabisz w miniaturze:** `# Dr X Y`, akapit i 3× `###` z `{#id}` (jeden bez spacji). Wynik: 0 × `h1`, akapit we wstępie, 3 sekcje z właściwymi `id`, brak `{#` w HTML.
- `# Inny nagłówek` na początku (nie tytuł) daje sekcję `##`.
- Treść z `##` i `###` zostaje bez zmian.
- `###` i `####` bez `##` dają `##` i `###`.
- Nagłówek wewnątrz bloku `:::` zostaje bez zmian.
- `## Tytuł{#id}` w trybie jawnym bez `ww` (np. kierunek): `id` działa, w tekście nie ma `{#id}`.

### 4. Dokumentacja
- `dok/jawny-markdown.md` i `dok/sciagawka-edytora.md` (część „Warto wiedzieć”): krótko, że strona sama usuwa `#` z imieniem lub tytułem i traktuje `###` jak sekcje, gdy w Treści nie ma `##`. Zalecany zapis to nadal `## Tytuł {#id}`.
- Komentarz przy kodzie reguł z ich opisem i odwołaniem do zlecenia 51.

## Odbiór lokalny
- **Porównanie HTML przed i po** (PL i EN, te same klony treści, Web-Instytut na `2328a0d` albo nowszym). Dozwolone różnice:
  - `/instytut/warto-wiedziec/krzysztof-tabisz/` i `/en/instytut/warto-wiedziec/krzysztof-tabisz/`;
  - indeks wyszukiwarki (Pagefind) w części dotyczącej Tabisza;
  - strony z `{#id}` bez spacji albo przy `###` (punkt 2): wypisz je w raporcie z adresem i nagłówkiem.

  Każdą inną różnicę zgłoś.
- **Strona Tabisza (PL):**
  - jeden `h1`;
  - wstęp to akapit „Dr Krzysztof Tabisz (ur. 1950)…”;
  - sekcje `#DzialalnoscNaukowa`, `#DzialalnoscSpoleczna` i `#Odznaczenia` z czarnymi `h2` i kreskami, jak u Steinhausa;
  - „Na tej stronie” z 4 pozycjami (3 sekcje i „Inne sylwetki”);
  - nigdzie nie ma `{#`.
- **Strona Tabisza (EN):** to samo, z identyfikatorami sekcji nadanymi automatycznie.
- **Log budowy:** ostrzeżenie przy Tabiszu (PL i EN), bez nowych ostrzeżeń przy innych wpisach.
- **Zrzuty:** Tabisz PL i EN przy 1920×1080, 1366×768 i 390 px, w trybie jasnym i ciemnym; do porównania Steinhaus PL przy 1920×1080.
- **Kontrole:**
  - `astro check` bez nowych błędów;
  - testy wtyczek zielone;
  - `sprawdz_tresci.py` i `sprawdz-jawny-markdown.mjs` bez problemów;
  - konsola czysta.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Strona Tabisza (PL i EN) wygląda jak inne sylwetki: sekcje z kreskami, czarne nagłówki, spis po prawej, jeden tytuł, bez `{#…}` w tekście.
- [ ] Plik Tabisza w Web-Instytut nietknięty.
- [ ] Inne wpisy WW (z `##`) bez zmian w HTML.
- [ ] `{#id}` działa bez spacji i przy każdym poziomie na wszystkich stronach z jawnym Markdownem.
- [ ] Ostrzeżenie w logu przy automatycznej poprawce.
- [ ] Testy z punktu 3 zielone, dokumentacja zgodna z działaniem.

## Do raportu (bez zmian w tym zleceniu)
- **Inne kolekcje z jawnym Markdownem** (kierunki, specjalności, strony Instytutu, strony działów itd.): czy gdzieś jest Treść bez `##`, a z `#` albo `###`. Wypisz pliki. Właściciel zdecyduje, czy rozszerzyć regułę z punktu 1.
- **Głowa sylwetki bez `:::w-skrocie`** (Tabisz go nie ma): opisz i pokaż na zrzucie, czy obok portretu zostaje puste miejsce. Propozycje zostaw do decyzji właściciela.

## Do wiadomości właściciela
- Opis pola „Treść” w CMS (Sylwetki) mówi już, że „## rozpoczyna sekcję”, a szablon nowej sylwetki ma szkielet w komentarzu. Redaktor wkleił jednak tekst nad komentarzami, więc zostały one na końcu pliku, w tym nieaktualny już komentarz „TBA” (na stronie go nie widać).
- Ewentualna zmiana opisów w `.pages.yml` Web-Instytut to osobna sprawa, z ochroną zmian redaktorów.
