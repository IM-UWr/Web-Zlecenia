# Zlecenie 58 (22.11.2026): krótsza angielska nazwa wydziału w pasku telefonu

**Skąd to zlecenie.** Na telefonie, po angielsku, przy szerokości 421–503 px druga linia paska „Faculty of Mathematics and Computer Science” (261 px) wchodzi pod flagę „PL” i księżyc, nawet o 71 px. Dzieje się to na każdej podstronie, na banerze i po przewinięciu. Na stronie głównej po zjechaniu z okładki tę linię ukrywa reguła „do 500 px” (`zal-telefon.css`, linia 67), ale przy 501–504 px nazwa stoi tam 3–7 px od flagi. Po polsku nazwa się mieści.

**Decyzja właściciela (22.11, 14:01–14:10):**
- „C mi się podoba, porównajmy to z D”;
- „D wygląda nieźle, wcale nie jest za blisko flagi”, „Bierzemy D”;
- strona główna po zjechaniu z okładki też dostaje skrót: „Tak, jak najbardziej, wdróż, jak sugerowałeś”.

**Prototyp:** https://claude.ai/artifact/HbpbbZUyJUWz8fPJ6vJz8z (sekcja „C czy D” i karta D w „Wszystkie warianty”). Źródło jest w `.przekazanie\prototypy\58-pasek-nazwa-wydzialu\`:
- `index.html` (zrzuty są tylko w artefakcie);
- skrypty pomiarów i zrzutów (`*.py`, Playwright);
- `strona-glowna-pasek.png`: strona główna dziś i z D.

Prototyp podmienia tekst skryptem tylko na potrzeby zrzutu, więc nie jest wzorem kodu.

## Zasady pracy
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- **Tylko Web-Core.** Repozytoriów treści nie zmieniasz. `pobierz_tresci.py` nie jest potrzebny, bo zmiana dotyczy tylko paska.
- Raport `RAPORT-ZLECENIE-58.md`, zrzuty `raport-zrzuty/z58-*`. Bez subagentów.
- **Kolejność:** zlecenie nie zależy od 57 (inne pliki). Jeśli 57 jest w toku, zrób 58 po nim.

## Stan dziś (Web-Core `main`, 7dfc959)
- `src/components/Naglowek.astro`: link `.brand-txt` ma `.brand-name` (`t(lang, 'instytut')`) i `.brand-sub` (`t(lang, 'wydzial')`). Na stronie głównej (`naOkladce`) obok stoi link `.z-wydzial` z nazwą wydziału w dwóch liniach (okładka). Po zjechaniu z okładki widać `.brand-txt` (klasa `.po-okladce`).
- `src/styles/global.css`:
  - linia 178: `.brand-name, .brand-sub { white-space: nowrap; }`;
  - linie 212–216: do 420 px `.brand-sub` jest ukryta, w obu językach.
- `src/styles/zal-telefon.css`:
  - linia 67: `@media (max-width: 500px) { .brand-okladka .brand-sub:lang(en) { display: none; } }`;
  - komentarz w linii 66.
- `src/styles/zal-niski.css`, linia 20: telefon w poziomie ukrywa `.brand-sub`. Bez zmian.
- **Pomiary w chmurze** (Chrome; krój Manrope 12 px; odstęp to lewa krawędź `.hdr-tools` minus prawy koniec napisu, mierzony przez `Range.getBoundingClientRect`):

| | 421 px | 430 px | 440 px | 480 px | 503 px | 515 px | 520 px |
|---|---|---|---|---|---|---|---|
| pełna EN (261 px), dziś | −71 | −62 | −53 | −16 | 5 | 16 | 20 |
| D „Faculty of Math. & Comp. Science” (186 px) | 5 | 13 | 22 | 59 | – | – | – |
| polska nazwa, dziś | 4 | 12 | 21 | 58 | 79 | – | 95 |

  Na stronie głównej po zjechaniu z okładki odstępy są te same co na podstronach.

## Docelowo
1. **Nowy tekst i18n `wydzialKrotko`** w `src/lib/i18n.ts`:
   - EN: „Faculty of Math. & Comp. Science”;
   - PL: taki sam jak `wydzial` (polska nazwa się mieści, skrótu nie ma).
   - Skrót renderuj tylko wtedy, gdy różni się od pełnej nazwy. Dzięki temu pasek PL ma dokładnie ten sam HTML co dziś.
2. **Pasek telefonu (`Naglowek.astro`, link `.brand-txt`), po angielsku:**
   - do 420 px: linia wydziału ukryta, jak dziś;
   - **421–519 px: „Faculty of Math. & Comp. Science”**;
   - od 520 px: pełna nazwa, jak dziś.
   - Dotyczy wszystkich stron z tym paskiem, także strony głównej po zjechaniu z okładki.
   - Reguła „do 500 px” z `zal-telefon.css` (linia 67) znika, bo zastępuje ją ta zmiana. Popraw też komentarz w linii 66.
3. **Czytniki ekranu zawsze czytają pełną nazwę.** Skrót jest tylko na ekranie:
   - np. pełna nazwa w tym zakresie jako `.sr-only`, a skrót z `aria-hidden="true"`;
   - dostępna nazwa linku zostaje jak dziś („Mathematical Institute Faculty of Mathematics and Computer Science”).
4. **Próg 519/520 px w jednym miejscu,** z komentarzem skąd się wziął: pełna nazwa mieści się z odstępem 16 px (`gap` paska) od ok. 515 px, a 520 px daje mały zapas. Krój, stopień i kolor drugiej linii bez zmian.
5. **Bez zmian:**
   - okładka strony głównej (`.z-wydzial`, dwie linie);
   - pasek komputera (`zal/PasekMenu.astro`, od 1024 px);
   - panel menu, stopka;
   - telefon w poziomie (`zal-niski.css`);
   - cała wersja PL.

**Wskazówka (nie przepis):** w `.brand-sub` dwa spany, np. `.bs-pelna` i `.bs-krotka`. Domyślnie `.bs-krotka { display: none }`, a w `@media (min-width: 421px) and (max-width: 519px)` pełna dostaje styl `.sr-only`, a krótka `display: inline`. Reguły dla telefonu trzymaj w `zal-telefon.css` przy innych regułach paska.

## Odbiór lokalny
- Build z obecną nakładką treści.
- **Zrzuty paska** (górne ok. 120 px, skala 2, jasny i ciemny tryb) przy 412, 421, 430, 440, 480, 500, 503, 515, 519, 520 i 560 px:
  - `/en/instytut/` (na banerze);
  - `/en/aktualnosci/` (po przewinięciu, jasny pasek);
  - `/en/` po zjechaniu z okładki;
  - dla porównania `/instytut/` i `/` (PL) przy tych samych szerokościach.
- **Pomiar co 1 px od 360 do 1023 px**, na co najmniej 4 stronach EN i 2 PL (także strona główna po zjechaniu z okładki):
  - napis drugiej linii nigdy nie wchodzi pod przyciski (odstęp ≥ 4 px, dziś tyle ma PL przy 421 px);
  - strona nie przewija się w poziomie przez pasek.
- **Dostępność:** przy 430 px dostępna nazwa linku `.brand-txt` (Playwright `accessibility.snapshot` albo `getByRole('link')`) zawiera pełną nazwę wydziału i nie zawiera skrótu.
- **Bez zmian:** HTML paska PL; pasek komputera przy 1280 i 1920 px (porównanie pikseli na 3 stronach); okładka strony głównej przy 390 i 430 px.
- **Kontrole:** `astro check` bez nowych błędów, konsola czysta.
- **Stop:** raport i czekanie na „push”. Push dotyczy tylko Web-Core.

## Kryteria odbioru
- [ ] EN, 421–519 px: w pasku jest „Faculty of Math. & Comp. Science” w jednej linii, przed flagą. Dotyczy każdej strony z paskiem, także strony głównej po zjechaniu z okładki.
- [ ] EN od 520 px: pełna nazwa. Do 420 px: bez linii wydziału, jak dziś.
- [ ] PL bez zmian (ten sam HTML i wygląd).
- [ ] Czytnik ekranu czyta pełną nazwę wydziału, bez skrótu.
- [ ] Bez zmian: komputer, okładka strony głównej, menu, stopka, telefon w poziomie.
- [ ] Przy żadnej szerokości 360–1023 px, w EN ani PL, druga linia nie wchodzi pod przyciski.

## Do raportu
- Lista zmienionych plików i opis rozwiązania.
- Tabela odstępów od flagi przed i po zmianie (421, 430, 440, 480, 503, 515, 520 px; EN i PL; podstrona i strona główna).
- Zrzuty i wynik pomiaru co 1 px.
