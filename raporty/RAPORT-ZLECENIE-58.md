# Raport: zlecenie 58, krótsza angielska nazwa wydziału w pasku telefonu (22.11.2026)

Gałąź robocza `praca/58-pasek-skrot` (lokalna), zrobiona po 57 i przeniesiona (`rebase`) na `main` = `c8e6497b` (57 i poprawka promotorów pomocniczych). Treści bez zmian: obecna nakładka, `pobierz_tresci.py` niepotrzebny. Pracowałem bez subagentów. Push według polecenia właściciela z 22.11: „I po 58 też automatyczny push” (szczegóły na końcu).

## Co zmieniłem

| Plik | Zmiana |
|---|---|
| `src/lib/i18n.ts` | Nowy tekst `wydzialKrotko`: EN „Faculty of Math. & Comp. Science”, PL taki sam jak `wydzial` („Wydział Matematyki i Informatyki”, bez skrótu, z komentarzem). |
| `src/components/Naglowek.astro` | W `.brand-sub` linku `.brand-txt`: gdy `wydzialKrotko` różni się od `wydzial` (dziś tylko EN), dwa spany: `.bs-pelna` (pełna nazwa) i `.bs-krotka` (skrót, `aria-hidden="true"`). Gdy się nie różni (PL), sam tekst, więc HTML jak dotąd. Komentarz na górze pliku i przy zmiennych. |
| `src/styles/global.css` | `.brand-sub .bs-krotka { display: none; }` (domyślnie skrót schowany, także na komputerze i w poziomie). |
| `src/styles/zal-telefon.css` | Usunięta reguła `@media (max-width: 500px) { .brand-okladka .brand-sub:lang(en) { display: none; } }`, a jej komentarz poprawiony (odsyła do nowej reguły). Przy regułach paska (`.hdr.jasny .brand-sub`) nowa reguła `@media (min-width: 421px) and (max-width: 519px)`: `.bs-pelna` dostaje styl `.sr-only` (zostaje dla czytników), `.bs-krotka` dostaje `display: inline`. Nad nią komentarz, skąd próg: pełna nazwa ma 261 px i mieści się z odstępem 16 px (`gap` paska) od ok. 515 px, a 520 px daje mały zapas; skrót ma 186 px. To jedyne miejsce tego progu. |

### Jak to działa
- **Do 420 px:** cała `.brand-sub` jest ukryta jak dotąd (`global.css`), w obu językach.
- **421–519 px, EN:** widać „Faculty of Math. & Comp. Science”. Pełna nazwa jest w drzewie dostępności (styl `.sr-only`), a skrót jest dla czytników ukryty.
- **Od 520 px, EN:** pełna nazwa, skrót `display: none`.
- **Strona główna po zjechaniu z okładki:** ta sama reguła, bo dawna reguła „do 500 px” zniknęła. Przy 421–519 px jest więc skrót, a od 520 px pełna nazwa. Wcześniej do 500 px linii nie było, a przy 501–504 px pełna nazwa stała 3–5 px od flagi.
- **Krój, stopień i kolor** drugiej linii się nie zmieniły: spany nie mają własnych stylów poza widocznością.
- **Bez zmian:** okładka (`.z-wydzial`), pasek komputera (`PasekMenu`), panel menu, stopka, telefon w poziomie (`zal-niski.css` dalej chowa całą `.brand-sub`) i cały PL.

## Sprawdzenie

Narzędzia w `raport-zrzuty/z58-skrypt/` (Edge przez Playwright, serwer plików z 57 na portach 4381 i 4382: przed = `main` `c8e6497b`, po = gałąź 58). Wyniki w `raport-zrzuty/z58-*.json`, zrzuty w `raport-zrzuty/z58-zrzuty/`.

### Cały `dist` przed i po
- HTML różni się tylko na 469 stronach EN. Na każdej z nich różnica to wyłącznie zawartość `.brand-sub` (dwa spany zamiast tekstu; `html58.py`). Wszystkie strony PL są identyczne, poza nazwą wspólnego pliku CSS w `<link>` (nowy skrót pliku).
- `_astro/`: zmienia się tylko wspólny arkusz `index.*.css` (nowe reguły z `global.css` i `zal-telefon.css`).
- Poza tym różnią się tylko znaczniki czasu: `DTSTAMP` w 154 plikach `.ics` i `wygenerowano` w `seminaria/powiadomienia.json`. Pagefind: 980 plików przed i po.

### Pomiar co 1 px, 360–1023 px (`pomiar58.mjs`, `z58-pomiar-przed.json`, `z58-pomiar-po.json`)
Strony EN: `/en/instytut/` (baner), `/en/aktualnosci/` (po przewinięciu, jasny pasek), `/en/` (po zjechaniu z okładki), `/en/nauka/konferencje/` (baner), `/en/obrony-doktorskie/` (po przewinięciu). Strony PL: `/instytut/`, `/` (po zjechaniu z okładki), `/aktualnosci/`. Odstęp liczę jak w zleceniu: lewa krawędź `.hdr-tools` minus prawy koniec widocznego napisu drugiej linii (`Range.getBoundingClientRect`). Krój Manrope 12 px.

Odstęp od flagi (px):

| | 421 | 430 | 440 | 480 | 500 | 503 | 515 | 519 | 520 |
|---|---|---|---|---|---|---|---|---|---|
| EN podstrona, przed | −70,7 | −62,4 | −53,2 | −16,4 | 2,0 | 4,8 | 15,8 | 19,5 | 20,4 |
| EN strona główna po okładce, przed | brak linii | brak | brak | brak | brak | 4,8 | 15,8 | 19,5 | 20,4 |
| **EN po (podstrona i strona główna)** | **4,9** | **13,2** | **22,4** | **59,2** | **77,5** | **80,3** | **91,4** | **95,0** | **20,4** |
| PL (przed = po) | 3,8 | 12,1 | 21,3 | 58,1 | 76,5 | 79,3 | 90,3 | 94,0 | 94,9 |

Przed zmianą strona główna EN miała pełną nazwę od 501 px (2,9 px przy 501). Wszystkie 5 stron EN po zmianie mają te same wartości.

Wynik po zmianie, dla każdej z 8 stron i każdej szerokości 360–1023:
- **Zakresy tekstu w EN:** 360–420 brak linii, 421–519 „Faculty of Math. & Comp. Science”, 520–1023 pełna nazwa. Tak jest na każdej z 5 stron, także na stronie głównej po okładce.
- **Najmniejszy odstęp w EN:** 4,9 px przy 421 px. Żadna szerokość nie ma odstępu poniżej 4 px. Przed zmianą odstęp był poniżej 4 px przy 421–502 px na podstronach i przy 501–502 px na stronie głównej.
- **PL bez zmian:** najmniejszy odstęp to 3,8 px przy 421 px, a 4 px nie ma tylko przy tej jednej szerokości. Tak samo przed zmianą. Zlecenie podaje 4 px z Chrome w chmurze, a lokalny Edge mierzy 3,8, bo inaczej zaokrągla krój. Jest to stan dzisiejszy, który zlecenie przyjmuje za wzór, więc PL nie ruszałem.
- **Przewijanie w poziomie:** brak przy każdej szerokości (`scrollWidth` = szerokość okna).
- **Druga linia w jednej linii:** zawsze (wysokość napisu = jedna interlinia).
- **Pierwsza linia** („Mathematical Institute”) ma te same odstępy przed i po zmianie.
- **Konsola:** 0 błędów i ostrzeżeń.

### Zrzuty paska (`zrzuty58.mjs`, `raport-zrzuty/z58-zrzuty/`)
Górne 120 px, skala 2, jasny i ciemny tryb, przy 412, 421, 430, 440, 480, 500, 503, 515, 519, 520 i 560 px:
- arkusze `z58-pasek-<en-instytut|en-aktualnosci|en-glowna|pl-instytut|pl-glowna>-<light|dark>.png`: wiersz = szerokość, z lewej przed, z prawej po;
- pojedyncze zrzuty `z58-<strona>-<szerokość>-<motyw>-<przed|po>.png` (220 plików).

Na arkuszach EN przy 421–503 px przed zmianą pełna nazwa wchodzi pod flagę i księżyc. Po zmianie skrót stoi przed flagą, a od 520 px jest pełna nazwa jak dotąd. Arkusze PL: po lewej i po prawej ten sam obraz.

### Dostępność (`z58-wynik.json`)
Dostępna nazwa linku `.brand-txt` (Playwright `ariaSnapshot` i `getByRole('link', { name, exact: true })`) na `/en/instytut/` i `/en/` po okładce:
- przy 430, 519, 520 i 600 px: „Mathematical Institute Faculty of Mathematics and Computer Science”, bez skrótu, `getByRole` znajduje 1 link;
- przy 400 px: „Mathematical Institute” (linia wydziału ukryta, jak dotąd);
- dla porównania `/instytut/`: „Instytut Matematyczny Wydział Matematyki i Informatyki” od 430 px.

### Piksele przed = po (`z58-wynik.json`)
- Pasek komputera, 1280 i 1920 px, `/en/instytut/`, `/en/aktualnosci/`, `/en/`, jasny i ciemny tryb: 11 z 12 porównań ma 0 różnych pikseli. `/en/aktualnosci/` przy 1920 px w ciemnym trybie: 1 piksel różni się o 1/255 w kanale niebieskim (x ≈ 1488, `z58-rozne-pasek-komputera-1920-dark-*.png`). To szum wygładzania, bo HTML i CSS paska komputera się nie zmieniły.
- Pasek na okładce strony głównej (telefon, dotyk), 390 i 430 px, PL i EN, jasny i ciemny: 0 różnic (8 porównań).
- Telefon w poziomie 844×390, `/en/instytut/` i `/en/`: 0 różnic.

### Kontrole
- `npm run build`: bez błędów.
- `astro check`: 0 błędów, 0 ostrzeżeń, 9 podpowiedzi. Żadna nie dotyczy zmienionych plików (`Sekcja.astro`, `stanBudowy/klient.js` i podobne).
- Repozytoria treści: bez zmian. W Web-Core zmienione tylko 4 pliki kodu.

## Kryteria odbioru
- [x] EN, 421–519 px: „Faculty of Math. & Comp. Science” w jednej linii, przed flagą, na każdej stronie z paskiem, także na stronie głównej po zjechaniu z okładki.
- [x] EN od 520 px pełna nazwa, do 420 px bez linii wydziału.
- [x] PL bez zmian: ten sam HTML (wszystkie strony PL identyczne poza nazwą pliku CSS) i ten sam wygląd (arkusze PL, pomiar).
- [x] Czytnik ekranu czyta pełną nazwę wydziału, bez skrótu.
- [x] Bez zmian: komputer, okładka strony głównej, menu, stopka, telefon w poziomie (HTML poza `.brand-sub` identyczny; piksele jak wyżej).
- [x] Przy żadnej szerokości 360–1023 px druga linia w EN nie wchodzi pod przyciski (najmniej 4,9 px). PL ma jak dotąd 3,8 px przy 421 px (patrz wyżej).

## Odstępstwa od zlecenia i decyzje
- **Brak.** Rozwiązanie jest takie jak we wskazówce zlecenia (`.bs-pelna` / `.bs-krotka`, `.sr-only` w zakresie 421–519 px).
- Domyślne `display: none` skrótu jest w `global.css` przy `.brand-sub`, a nie w `zal-telefon.css`. Dzięki temu skrót jest schowany wszędzie poza zakresem telefonu. Wszystkie reguły z progiem są w `zal-telefon.css`.
- Push bez słowa „push”: polecenie właściciela z 22.11.

## Push
Według polecenia właściciela z 22.11 („I po 58 też automatyczny push”): commit `184ef501` na `praca/58-pasek-skrot` (gałąź tylko lokalnie), `git pull --rebase` na `main`, fast-forward i push tylko Web-Core. Na `main` od startu nie było nowych zmian. Wynik: `c8e6497b..184ef501` o 15:08. Przekaźnik do Web-Podglad (przebieg 45031185106) ruszył; wyniku budowy Podglądu nie sprawdzałem.
