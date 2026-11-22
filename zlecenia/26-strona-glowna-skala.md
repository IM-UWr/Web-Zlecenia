# Zlecenie 26: średnie i duże ekrany — strona główna (GOTOWE, 6.11.2026)

Stan: **wszystkie punkty GOTOWE** (decyzje właściciela 6.11, 22:45–23:01). Trzecie z czterech zleceń „średnie ekrany”. **Po zleceniu 24** (próg telefonu 1024 px); od zlecenia 25 niezależne, ale nie rób ich jednocześnie.

**Gdzie i jak:** jak w zleceniu 24 (gałąź `wyglad/zlecenie-16`, commit na punkt, bez pushowania, bez `pobierz_tresci.py`, dziennik, `RAPORT-ZLECENIE-26.md`, zrzuty `raport-zrzuty/z26-*`, numery linii ze stanu `b4f99c2`). Narzędzie odbioru: `24-zalaczniki/24-pomiar-szerokosci.cjs`. Wzór: `26-zalaczniki/26-strona-glowna-skala-prototyp.js`.

**Skala strony głównej** (punkty 1 i 2): `s = min(szerokość okna / 1920, wysokość okna / 950)`. Okładka i „Szybki dostęp” są zaprojektowane i zatwierdzone na Full HD (widok 1920×950); przy s = 1 wszystko zostaje jak dziś.

## 1. Okładka jako jedna kompozycja skalowana od Full HD — GOTOWE (decyzja 6.11, 22:50; zgłoszenie właściciela 22:45: „ciemny łuk się bardzo źle skaluje z rozmiarem”)
**Przyczyna:** skrypt ULOZ (`Okladka.astro:94–126`) prowadzi łuk 58 px (`ODSTEP`, `:76`) za końcem napisu „Wydział Matematyki i Informatyki” w marce, który ma stały rozmiar (logo 40 px, tekst 14 px — `zalozyciele.css:94, 396–398`), a wielkość tytułu dobiera tak, żeby końce „Instytut” i „Matematyczny” leżały na łuku. Wysokość okna wpływa tylko na położenie tytułu (`GORA` 0,29), szerokość wcale. Łuk stoi więc ok. 450–520 px od lewej: na wysokości tytułu **45% szerokości przy 1024×700, 34% przy 1280×600, 30% przy 1536×730, 25% przy 1920×950, 20% przy 2560×1300** (`26-okladka-dzis-i-skala.jpg`).

**Zmiana:** razem ze skalą s skalują się marka (`top` 18, `left` 48, odstęp 14, logo 40 px, napis 14 px, `padding-left` 14), lewy margines tytułu (48 px) i `ODSTEP` (58·s). Tytuł i łuk liczy dalej ten sam skrypt (s licz raz, w ULOZ, i ustaw jako zmienną CSS). Progi czytelności: logo ≥ 30 px, napis ≥ 12 px, marginesy ≥ 24 px.
- **Rząd czterech działów na dole** (`.z-okl-dzialy`, `.z-okl-szkic`, `.z-okl-nazwa`, `.z-okl-dz .slot`, `.z-okl-liczby`, `.z-strzalka`; `zalozyciele.css:416–470`) przejdź na tę samą skalę s zamiast `clamp()` od `--h` z górnymi limitami (dziś na 2560×1300 jest drobny). Drobny tekst ≥ 13 px. Hasła działów `text-wrap: balance` (dziś przy 1024 px samotne „A+”).
- **Telefon** (poniżej 1024 px po zleceniu 24) bez zmian — tam okładka ma własny układ.

Wynik prototypu (marka, margines i `ODSTEP`; bez rzędu działów): łuk na **34%** przy 1024×700, **27%** przy 1280×600, **25%** przy 1536×730, 1920×950, 2048×1040, 2560×1300 i 3840×2000; 19% na ultrawide 3440×1300 (ogranicza wysokość, resztę szerokości wypełnia zdjęcie) — `26-duze-ekrany-okladka-po-zmianie.jpg`.

**Odbiór:** 1920×950 i 1920×1080 piksel w piksel jak przed zmianą; łuk na wysokości środka pierwszej linii tytułu: 25% ± 2 punkty przy 1536×730, 2048×1040, 2560×1300, 3840×2000, najwyżej 35% przy 1024×700; okładka mieści się w jednym ekranie w każdym oknie od 1024×600; tytuł nie wchodzi na zdjęcie ani na łuk; rząd działów przy 2560×1300 w proporcjach jak przy 1920×950 (zrzuty obu do raportu).

## 2. „Szybki dostęp” na ekranach większych od Full HD — GOTOWE (decyzje 6.11, 22:54–22:58: „Dobra”, „Piękne, podoba mi się”)
Dziś drugi ekran nie powiększa się powyżej Full HD (tekst 14,5 px, margines 48 px, kolumny na całą szerokość), więc przy 2560 px i szerzej jest rzadki i rozstrzelony, a na 4K przy 100% wygląda jak drobny druk na plakacie (`26-drugi-ekran-2k-4k.jpg`, lewa kolumna).
- Gdy **s > 1**, drugi ekran powiększa się tą samą skalą s co okładka, razem z paskiem menu i stopką (prototyp: CSS `zoom` na `.z-druga`, `.z-pasek`, `.z-stopka`). Przy s ≤ 1 bez zmian.
- Pułapka z prototypu: minimalną wysokość drugiego ekranu liczoną od wysokości okna (`zalozyciele-strony.css:8`, `min-height: calc(100svh - var(--gora) - 47px)`) trzeba podzielić przez skalę, inaczej się podwaja.
- Sprawdź animację „Zobacz więcej” (`src/scripts/zal/drugi-ekran.ts`, FLIP z pozycji elementów) i przejazd z okładki (`przejazd.ts`) przy powiększeniu.
- **Ręczne powiększanie (Ctrl +) musi działać** (WCAG 1.4.4, tekst do 200%; uczelnię obowiązuje ustawa o dostępności cyfrowej). Gdy użytkownik sam powiększa stronę w przeglądarce, **skala s się wyłącza** (na okładce i na drugim ekranie) i działa zwykłe powiększanie. Poziom powiększenia przeglądarki odczytaj z porównania `outerWidth` z `innerWidth` (np. stosunek > 1,05 → powiększona); sprawdź w Chrome, Edge, Firefoxie i Safari i opisz wynik w raporcie. Skala systemu (100/150/200%) nie wyłącza s — na stronie głównej wygląd ma zależeć od wielkości monitora, nie od skali (decyzja 22:56–22:57).

**Odbiór:** 2560×1300 (skala 1,33) i 3840×2000 (skala 2) wyglądają jak 1920×950 w powiększeniu (zrzuty obok siebie w raporcie); 1920×950 piksel w piksel jak przed zmianą; bez poziomego przewijania; „Zobacz więcej” i przejazd z okładki działają przy obu skalach; w Chrome przy 3840×2000 Ctrl + 200% daje tekst wyraźnie większy niż przy 100% (opis ręcznego sprawdzenia w raporcie).

## 3. „Szybki dostęp” na niskich laptopach: drabinka wysokości — GOTOWE (decyzja 6.11, 23:01: „Tak”)
Dziś drugi ekran mieści się w jednym ekranie tylko przy 1707×830 i 1920×950. O tyle dół stopki wychodzi poza okno (minus pasek 61 px): 1280×600 **+395 px**, 1366×620 **+303**, 1440×780 **+122**, 1536×730 **+140** (Full HD przy 125% — przy 1536×730 dolna krawędź okna przecina „Warto wiedzieć” w połowie). Wysokość wyznacza lewa część (dwie krótkie kolumny po 3 pozycje, Studia, Warto wiedzieć); długa kolumna aktualności dopasowuje się sama.

Gdy drugi ekran nie mieści się w wysokości okna (komputer, s ≤ 1), rzeczy ustępują kolejno — rozstrzyga pomiar, jak w zleceniu 25:
1. **stopka schodzi pod ekran** (ok. 71 px);
2. **„Warto wiedzieć” schodzi pod ekran w całości**, nie cięte w pół (113–137 px + odstęp 22);
3. **krótkie kolumny pokazują po 2 pozycje zamiast 3** (ok. 71–96 px), „Zobacz więcej (N)” zostaje i liczy właściwe N;
4. gdy dalej się nie mieści — **zwykłe przewijanie**.

„Schodzi pod ekran” = siatka (Szybki dostęp, kolumny, Studia) wypełnia pierwszy ekran, a ustępujące części stoją pod nią, za zwykłym przewinięciem. Kolejność elementów dla czytnika ekranu bez zmian.

**Odbiór:** 1440×780 i 1536×730 — po krokach 1–2 cała siatka w jednym ekranie; 1366×620 — po krokach 1–3 na styk; 1280×600 — przewija się, bez ucinania pozycji w pół; 1707×830 i 1920×950 bez zmian; liczba w „Zobacz więcej (N)” zgadza się z ukrytymi pozycjami.

## 4. „Szybki dostęp” — drobne — GOTOWE (bez decyzji)
1. Nagłówki kolumn (`zalozyciele-strony.css:14, 49–53`, `DrugiEkran.astro:166`): `.z-h` z `flex-wrap: wrap`; zakres dat seminariów (`<small>`) `white-space: nowrap` i spacja przed nim (dziś „6– / 12 listopada”); `h2` `clamp(18px, 1.7vw, 22px)`, żeby „Nadchodzące wydarzenia” nie łamało się wcześniej niż pozostałe nagłówki i kreski stały na jednej wysokości.
2. Pasek „Szybki dostęp” (`zalozyciele-strony.css:16–17`): poniżej ok. 1100 px napis „Szybki dostęp” w osobnym wierszu (jak na telefonie, `:202`); „e‑maile” z łącznikiem niełamiącym (dziś „e- / maile”).
3. Kierunki studiów (`zalozyciele-strony.css:83, 158–163`): `repeat(auto-fill, minmax(110px, 1fr))` zamiast progów 1365/959 px (dziś tuż nad progami kolumny ok. 95–100 px i „Szkoła / doktorska”).

## 5. Zdjęcie okładki w większej rozdzielczości — GOTOWE, zależne od pliku
Największy plik okładki ma 2400 px. Na 2K przy 100% wystarcza, ale na 4K (przy 150% i 100%) i na ultrawide przeglądarka powiększa go ok. 1,4–1,5× i zdjęcie jest miękkie. Potrzebny większy kadr z oryginału 3500 px (fotopolska, kadry opisane w `claude/start-2026-11-05.md` w projekcie claude.ai). **Jeśli w `.przekazanie\zdjecia\` jest plik okładki szerszy niż 2400 px** (właściciel ma go przygotować), dodaj go jako największy wariant zestawu (`srcset` do szerokości pliku) i popraw `sizes`; **jeśli go nie ma — pomiń punkt** i zapisz w dzienniku pytanie.

## Raport
`RAPORT-ZLECENIE-26.md`: tabela położenia łuku (okna 1024×700 … 3840×2000, przed i po), zrzuty okładki i drugiego ekranu przy 1280×600, 1536×730, 1920×950, 2560×1300, 3440×1300, 3840×2000 (`raport-zrzuty/z26-*`), wynik sprawdzenia Ctrl + w czterech przeglądarkach, tabela drabinki (okno → które kroki zadziałały), pytania.
