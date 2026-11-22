# Zlecenie 27: Kalendarz, Obrony i Warto wiedzieć w stylu Aktualności; drobne; pomiar szerokości co tydzień (GOTOWE, 6.11.2026)

Stan: **wszystkie punkty GOTOWE** (decyzje właściciela 6.11, 23:01–23:10). Ostatnie z czterech zleceń „średnie ekrany”. **Po zleceniach 24 i 25** (próg telefonu 1024 px, zasada treści z polem „Na tej stronie”).

**Gdzie i jak:** jak w zleceniu 24 (gałąź `wyglad/zlecenie-16`, commit na punkt, bez pushowania, bez `pobierz_tresci.py`, dziennik, `RAPORT-ZLECENIE-27.md`, zrzuty `raport-zrzuty/z27-*`, numery linii ze stanu `b4f99c2`, PL i EN). Narzędzie odbioru: `24-zalaczniki/24-pomiar-szerokosci.cjs`.

**Skąd to zlecenie.** Kalendarz, Obrony doktorskie i Warto wiedzieć nie mają pola „Na tej stronie”, a zostawiają po nim pusty pas 292 px z prawej (`zal-podstrona.css:5, 11`). Właściciel (23:01): „Kalendarz ma mieć podobny styl co Aktualności: kolorki, filtry, wyszukiwanie, »Pokaż« ładują do pływającego po prawej stronie jak Aktualności. Zdjęcie to, co w Aktualnościach. I ten sam styl banera (przechodzącego z ciemnego).” Dziś: `27-aktualnosci-i-kalendarz-dzis-1536.jpg`.

## 1. Kalendarz w stylu Aktualności — GOTOWE (decyzje 23:01–23:06)
Wzór: lista Aktualności na komputerze (`ListaAktualnosci.astro`, `WierszAktualnosci.astro`, panel „Pokaż” z prawej, `:35`, `:202–232`).
- **Baner jak w Aktualnościach:** granat z lewej przechodzi w zdjęcie po prawej w naturalnych kolorach (klasa `z-foto-nat`) i **to samo zdjęcie** (`aktualnosci-skok.jpg`, kadr z `NaglowekZ.astro:69`). Dziś warunek `fotoNat` obejmuje tylko `/aktualnosci` (`NaglowekZ.astro:60`) — rozszerz o `/kalendarz`, `/obrony-doktorskie` (lista) i `/warto-wiedziec` (lista), PL i EN.
- **Bez liczb w banerze** (23:06: „Wypad”; dziś „zapowiedziane referaty · nadchodzące wydarzenia”): samo hasło „Co, gdzie i kiedy” / EN, jak w Aktualnościach.
- **Kolory jak w Aktualnościach:** duża data i etykieta rodzaju w kolorze działu wpisu (seminarium — dział jego zakładu/Nauka, wydarzenie — `dzialWydarzenia`, obrona — jak w Aktualnościach). Ten sam wzór daty i wiersza co lista Aktualności (`WierszWydarzenia.astro` i `WierszAktualnosci.astro` mają już wspólny język).
- **Panel „Pokaż” z prawej, przyklejony** (jak w Aktualnościach): rodzaje (Wszystkie, Wydarzenia, Obrony, Konferencje, Seminaria) jako lista z zaznaczeniem wybranego, pod nią pole „Szukaj w kalendarzu”. Dzisiejszy rząd przycisków nad listą (`Kalendarz.astro` ok. :140) znika z komputera.
- **Przełącznik Nadchodzące / Archiwum zostaje nad listą, ale szeroki i wyraźny** (23:02: „szerszy, bardziej widoczny przełącznik”): na całą szerokość kolumny listy, dwie równe połówki, wysokość ok. 44 px, napis 15 px, wybrana połówka wypełniona (granat na jasnym tle, w ciemnym motywie odwrotnie), druga z obrysem; `aria-pressed`, fokus widoczny.
- **Widok telefonu** (poniżej 1024 px): filtry nad listą, jak Aktualności na telefonie; przełącznik Nadchodzące / Archiwum na całą szerokość.
- Adresy z parametrami (np. rodzaj, archiwum) działają jak dziś.

## 2. Obrony doktorskie (lista) i Warto wiedzieć (lista) w tym samym stylu — GOTOWE (decyzja 23:06: „tak”)
- Ten sam baner co Kalendarz i Aktualności (punkt 1), bez liczb, z hasłem strony.
- **Obrony:** panel „Pokaż” z prawej — filtr lat (lata, w których są obrony, od najnowszego; „Wszystkie” na górze) i pole szukania (imię i nazwisko, tytuł rozprawy, promotor). Kolory dat jak w Aktualnościach (obrona doktorska).
- **Warto wiedzieć:** panel „Pokaż” — filtr działu (Instytut, Nauka, Studia, Popularyzacja; tylko działy, które mają wpisy — pole `dzial` dziś nie zna Popularyzacji, zob. `claude/estetyka.md`, „CMS: dział przy aktualnościach”) i pole szukania. Kolory jak w Aktualnościach.
- Pojedyncze wpisy (obrona, wpis „Warto wiedzieć”) bez zmian.
- Widok telefonu: filtry nad listą.

**Odbiór (punkty 1–2):** Kalendarz, Obrony, Warto wiedzieć i Aktualności przy 1024, 1280, 1536, 1920 px obok siebie (zrzuty) — ten sam baner, ten sam panel z prawej, te same kolory; brak pustego pasa z prawej; filtry i szukanie działają (sprawdź każdy rodzaj, rok, dział i jedno wyszukiwanie z wynikiem i bez); przełącznik Nadchodzące / Archiwum działa, z klawiatury też; widok telefonu przy 390 i 900 px; narzędzie 0 K/R/O/W/X na tych stronach przy 1024–1920 px; PL i EN; jasny i ciemny motyw.

## 3. Kadr zdjęcia z Aktualności — GOTOWE
Przy ≥ 1536 px ręce skaczącej osoby chowają się pod paskiem menu (`zalozyciele.css:317`, kadr `48% 63%` w `NaglowekZ.astro:69`). Popraw kadr tak, żeby cała postać była pod paskiem przy 1024–2560 px, na wszystkich czterech stronach z punktów 1–2.

## 4. Przekierowanie `/instytut/zaklady/` → `/instytut/struktura/` — GOTOWE (decyzja 23:10: „ok”)
Strony zakładów są pod `/instytut/zaklady/<nazwa>/`, a lista zakładów jest na Strukturze. Sam adres `/instytut/zaklady/` nie ma strony (na GitHub Pages 404), a ludzie skracają adresy i mogą tam trafiać stare linki. Dodaj stronę przekierowania tym samym mechanizmem co `src/pages/studia/kalendarz-zajec.astro` (`Przekierowanie.astro`), PL i EN (`/en/instytut/zaklady/` → `/en/instytut/struktura/`). Poza mapą strony i wyszukiwarką.

## 5. Krzyżyk panelu menu w prawym górnym rogu panelu — GOTOWE (decyzja 23:10: „przenieśmy”)
Dziś krzyżyk zamykania stoi w miejscu przycisku ☰ (`zal-menu.css:76–85`, `--marg` z górną granicą 340 px), więc przy 1707–1920 px wypada na środku górnej krawędzi panelu, a pole „Szukaj na stronie” ma ok. 250 px (`27-panel-menu-1920-dzis.jpg`). Zmiana na komputerze: krzyżyk w prawym górnym rogu panelu (24 px od górnej i prawej krawędzi panelu, wyrównany do pola szukania), pole szukania na całą szerokość panelu minus krzyżyk i odstęp. Dotyczy panelu przy pasku i na okładce. Telefon bez zmian. Fokus po otwarciu i Esc jak dziś.

## 6. Drobne — GOTOWE (bez decyzji)
1. **Stopka** (`StopkaZ.astro:18`): elementy w `white-space: nowrap`, separator „·” jako `::before` następnego elementu — przy zawijaniu żaden separator nie zostaje na końcu ani na początku linii (dziś EN przy 960 px, PL poniżej ok. 840 px).
2. **Szukaj i 404** (`Szukaj.astro:19`, `404.astro:12`, `global.css:44–45, 123`): treść w linii kolumny strony (`--marg`), a nie starego `.wrap` z `--gutter` (dziś 24–30 px w lewo od tytułu przy 1024–1280, 17 px w prawo przy 1920).
3. **Godzina w karcie wydarzenia** (`Aktualnosc.astro:170`): przedział „10:00–14:00” bez łamania (twarda spacja / `nowrap`; dziś „10:00– / 14:00” także przy 1920 px).

## 7. Pomiar szerokości co tydzień — GOTOWE
Dodaj narzędzie `24-zalaczniki/24-pomiar-szerokosci.cjs` (z `24-podsumuj-pomiar.py`) do repozytorium (np. `skrypty/szerokosci/`) i do cotygodniowego sprawdzania w GitHub Actions obok pa11y i lychee:
- buduje stronę, serwuje `dist`, renderuje listę stron w 11 oknach (800–1920 px plus 2560×1300), PL i EN;
- przy nagłówkach z ciekawostką przechodzi przez całą pulę ciekawostek działu, nie przez jedno losowanie;
- wypisuje macierz strona × okno (K/R/O/W/X) i — z atrybutów ze zlecenia 25 — **na których stronach i od jakiej szerokości pole „Na tej stronie” się zwija albo treść przechodzi na widok telefonu**;
- wynik jako artefakt przebiegu (raport Markdown + zrzuty z problemami); przebieg kończy się błędem, gdy pojawi się nowa kolizja (K) albo poziome przewijanie (X).
Nowe zależności tylko w workflow (instalacja Playwrighta w przebiegu), nie w `package.json`, chyba że inaczej się nie da — wtedy jako `devDependencies` i opis w raporcie.

## Raport
`RAPORT-ZLECENIE-27.md`: zrzuty z punktów 1–3 i 5, opis filtrów i ich adresów, wynik pierwszego przebiegu pomiaru (punkt 7), pytania.
