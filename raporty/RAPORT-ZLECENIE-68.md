# Raport — zlecenie 68: minione referaty na stronie seminarium według lat akademickich

Data: 23.11.2026. Zlecenie pisane jako 67; numer 67 był już zajęty (instrukcje dla redaktorów w PDF), więc to jest **68** (`zlecenia/68-seminaria-minione-wedlug-lat.md`). Praca w osobnym worktree `Web-Core-67` (gałąź `zlecenie-67` z `origin/main`), bo w głównym folderze Web-Core równolegle pracowała inna sesja. Bez subagentów. Push na `main` na polecenie właściciela („push na main bez czekania na »push«”).

## Krótko
- Minione referaty są podzielone na lata akademickie (od 1.10): `h3#rok-RRRR-RR` z tekstem „2025/26” i liczbą („4 referaty”, „25 referatów”, „1 talk”, „10 talks”). Lata i referaty od najnowszego.
- Każdy rok ma własną siatkę dwóch kolumn (zlecenie 65). Rozwinięcie streszczenia działa w każdym roku i zwija streszczenie także w innym roku.
- Tytuł minionego referatu pod rokiem jest w `h4`. Obliczone style wiersza są identyczne jak przed zmianą przy 1920, 1440, 1024 i 390 px (jasny i ciemny).
- Spis „Na tej stronie”: Nadchodzące referaty, Minione referaty, potem lata (płasko, jak w Konferencjach, bo spis nie ma wcięć).
- Seminarium z minionymi z jednego roku wygląda jak dotąd (bez nagłówków lat, tytuł w `h3`, spis bez lat).
- Poza stronami `/seminaria/<id>` (PL i EN) `dist` jest bez zmian (różnią się tylko znaczniki czasu budowy).
- Żadna strona seminarium nie przekracza 1 MB (największa: DAH EN 894 KB).

## Zmienione pliki (Web-Core)
- `src/lib/daty.ts`: nowa funkcja `rokAkademicki(termin)` (od 1.10, np. „2025/26”). Podobnej nie było; Plan zajęć ma inną regułę (rok od 1.08, zlecenie 43) i nie został zmieniony.
- `src/lib/widoki/seminarium.ts`: `daneSeminarium()` zwraca też `lataMinionych: { rok, id, lista }[]` (jak `daneListyKonferencji()`).
- `src/views/Seminarium.astro`:
  - sekcja `#z-minione`: dla każdego roku `h3.sem-rok` i własna `div.ref-dwie`; gdy rok jest jeden, jedna siatka bez nagłówka (jak przed zmianą);
  - tytuł: `h4` pod rokiem, `h3` bez podziału; selektory `.ref h3` → `.ref :is(h3, h4)`;
  - `letter-spacing: -0.005em` przy tytule. Bez tego `h4` dostawał `-0.01em` z `global.css` (`h1, h2, h3, h4`), a `h3` ma `-0.005em` z `main :is(h1, h2, h3)`. Dla `h3` wartość się nie zmienia;
  - styl liczby przy roku (`h3.sem-rok small`) jak w Konferencjach i Obronach;
  - skrypt: `querySelectorAll('.ref-dwie')`, nasłuch `click` i `toggle` na każdej siatce. Po każdym `toggle` kolejność (`order`) liczy się we wszystkich siatkach naraz, bo `details name="streszczenie-minione"` jest wspólne dla strony;
  - komentarz na górze pliku opisuje nowy układ (zlecenie 68).

## Dane do testów
- Archiwum nie było jeszcze na `main` (po kilka referatów w repozytoriach `Web-Sem-*`). Paczkę `67-tresci-archiwum.zip` rozpakowałem poza gitem i nałożyłem przez `pobierz_tresci.py --zrodlo …` (8 repozytoriów, 1324 referaty).
- Budowa: 953 strony, 0 błędów.
- Na koniec przywróciłem zwykłą nakładkę (`pobierz_tresci.py` bez opcji). Budowa na treściach z `main` też przeszła (953 strony).
- Na treściach z `main` sprawdziłem też przypadek jednego roku: Analiza harmoniczna i Prawdopodobieństwo mają minione z jednego roku, więc są bez podziału. DAH i Statystyka mają dwa lata, więc są z podziałem.

## Rozmiary stron seminariów (z archiwum)
| Seminarium | Minione | Lata | PL przed → po | EN przed → po | PL gzip |
|---|---|---|---|---|---|
| Dyskretna analiza harmoniczna | 260 | 14 | 883 → 889 KB | 888 → 894 KB | 128 KB |
| Prawdopodobieństwo | 147 | 13 | 668 → 673 KB | 666 → 671 KB | 94 KB |
| Topologia | 157 | 12 | 421 → 425 KB | 422 → 426 KB | 65 KB |
| Geometria | 238 | 14 | 343 → 348 KB | 346 → 351 KB | 48 KB |
| Teoria modeli | 98 | 9 | 272 → 275 KB | 273 → 276 KB | 46 KB |
| Równania różniczkowe | 158 | 13 | 227 → 231 KB | 233 → 238 KB | 49 KB |
| Analiza harmoniczna | 230 | 14 | 217 → 222 KB | 218 → 223 KB | 36 KB |
| Statystyka | 25 | 5 | 80 → 81 KB | 79 → 81 KB | 22 KB |
| Dydaktyka | 0 | — | 51 → 51 KB | 51 → 51 KB | 15 KB |

Podział na lata dodaje ok. 4–6 KB na stronę. **Żadna strona nie przekracza 1 MB.** Najbliżej jest DAH (889/894 KB), głównie przez streszczenia z KaTeX-em w HTML.

Propozycja na wypadek przekroczenia 1 MB (bez wdrażania): starsze lata (np. starsze niż 5 lat) na osobnych podstronach `/seminaria/<id>/rok-RRRR-RR`. Spis i kotwice lat zostają, a stare kotwice `#<slug>` przekierowuje mały skrypt. Druga możliwość: streszczenia minionych wczytywane dopiero przy rozwinięciu (fragmenty HTML). To jednak wyłącza je z indeksu wyszukiwarki, chyba że indeks dostaną osobno.

## Odbiór lokalny — wyniki
Serwowane lokalnie dwie budowy (przed i po) z tymi samymi treściami. Wbudowana przeglądarka Claude, emulacja rozmiarów okna.

- **HTML:** na wszystkich 9 stronach seminariów (PL i EN) po usunięciu nagłówków lat, zamianie h4→h3 i scaleniu siatek HTML jest identyczny jak przed zmianą. Kotwice referatów są te same: 1313 minionych i 11 nadchodzących.
  - Jedyna różnica techniczna: dynamiczny tag tytułu ma atrybut `data-astro-cid-…="true"` zamiast pustego. Selektory CSS działają tak samo.
- **Reszta `dist`:**
  - poza `/seminaria/<id>` (PL i EN) różnią się tylko `DTSTAMP` w plikach `.ics` i pole `wygenerowano` w `seminaria/powiadomienia.json` (czas budowy);
  - pliki w `_astro`: 3382 przed i po (inne nazwy CSS/JS);
  - indeks wyszukiwarki: 926 stron i 58 525 słów, tak samo jak przed zmianą.
- **Style wiersza (`getComputedStyle`):** sprawdziłem wszystkie 244 wiersze Geometrii: dzień, miesiąc, etykietę, tytuł, prelegenta, afiliację, `details`, „Streszczenie”, streszczenie i pliki, łącznie 29 właściwości. Są równe jak przed zmianą przy 1920×1080, 1440×900, 1024×768 i 390×844, w trybie jasnym i ciemnym (ciemny na telefonie).
  - Pominąłem wysokość komórki siatki i `time.dz`, bo rozciągają się do wysokości rzędu, a pary w rzędach przesuwają się na granicach lat.
  - Pierwszy pomiar wykazał różnicę `letter-spacing` tytułu (`h4` −0,19 px, `h3` −0,095 px). Poprawiłem ją, opis wyżej.
- **Rok:** styl `h3` roku i `small` jest identyczny jak w Konferencjach i Obronach: Brygada 23 px w kolorze działu, liczba 13 px/600 szara, odstęp 10 px pod `h2`, 30 px między latami, `scroll-margin-top` 20 px. Czytnik ekranu odczytuje nagłówek jako „2019/20, 23 referaty”.
- **Rok akademicki:** reguła 1.10 dla wszystkich 2626 wierszy (PL+EN) bez błędu, np. 25.09.2019 → 2018/19, 2.10.2019 → 2019/20. Lata malejąco na każdej stronie.
- **Dwie kolumny (zlecenie 65), 1440×900:** rozwinąłem streszczenie w prawej kolumnie w latach 2025/26, 2018/19 i 2013/14, w tym jeden raz prawdziwym kliknięciem myszy.
  - Za każdym razem wiersz zajmuje cały rząd (948 px), a sąsiad z lewej schodzi pod niego.
  - Poprzednie streszczenie, także w innym roku, się zwija.
  - Kliknięty wiersz przesuwa się o 0 / 0 / −0,2 px.
  - Na telefonie (390 px) rozwinięcie nie zmienia kolejności, a wiersz przesuwa się o 0 px.
- **Spis:**
  - klik w rok, myszą i Enterem z klawiatury: przewinięcie do `h3` (20 px od góry okna), fokus na nagłówku, adres `#rok-RRRR-RR`, w spisie podświetlony ten rok;
  - przy zwykłym przewijaniu znacznik przechodzi na bieżący rok (2023/24, 2018/19, 2015/16, Nadchodzące);
  - przy 1024×768 spis z 16 pozycjami mieści się w kolumnie (521 px);
  - na telefonie spis jest schowany, jak dotąd.
- **Kotwice z Kalendarza:** wszystkie 2648 linków `seminaria/<id>#<slug>` z Kalendarza i listy seminariów (PL i EN) trafiają w istniejące `id`. W przeglądarce sprawdziłem trzy:
  - 2014: `analiza-harmoniczna#2014-01-15-wrobel`, wiersz widoczny na dole strony, bo dalej nie da się przewinąć;
  - 2019: `dyskretna-analiza-harmoniczna#2019-01-10-vergara`, wiersz 99 px od góry, tak samo jak przed zmianą (`scroll-padding-top` 79 px + 20 px);
  - 2025, EN: `en/seminaria/geometria#2025-11-24-tao-2`, 99 px.
- **Lista seminariów:** baner „1313 referatów w archiwum” zgadza się z sumą minionych na stronach seminariów (1313).
- **Kontrole:**
  - `astro check`: 0 błędów, 0 ostrzeżeń, 4 podpowiedzi (dawne, w innych plikach);
  - `sprawdz_tresci.py`: OK;
  - konsola przy zwykłym wczytaniu stron seminariów (PL i EN) czysta. Błąd „View transition aborted” pojawiał się tylko przy moich skryptowych przejściach między stronami w trakcie animacji.
- **Zrzuty** zrobiłem w katalogu tymczasowym; zgodnie z zasadami ich nie przechowuję. Pokazały:
  - przejście Nadchodzące → Minione → „2026/27 · 4 referaty” (1440);
  - rozwinięte streszczenie Jing Tao (2025/26) na cały rząd (1440);
  - przejście 2026/27 → 2025/26 i koniec listy 2013/14 z linkiem „Archiwum referatów ↗” (390);
  - spis z latami przy 1024 px.

## Kalendarz → Archiwum (telefon 390 px), tylko pomiar
- `/kalendarz/` ma 1,22 MB HTML (EN 1,25 MB) i 14 610 elementów. Archiwum po przełączeniu ma ok. 257 000 px wysokości i 1424 widoczne wiersze.
- Przełączenie na „Archiwum”: 268 ms (styl i układ). Na słabszym telefonie (CPU ×4) to zapewne ok. 1 s, jednorazowo.
- Przewijanie skokami po 400 px z wymuszonym trafieniem w punkt: mediana 11 ms, maksimum 20 ms na krok. Samo przewijanie po wczytaniu nie wymaga przeliczania układu.
- **Czego nie mogłem zmierzyć:**
  - w tej przeglądarce nie mam emulacji słabszego CPU ×4;
  - panel przeglądarki był schowany, więc klatki animacji są dławione i pomiar płynności przewijania byłby niewiarygodny.
- Ocena (szacunek): przewijanie raczej płynne. Odczuwalny może być moment przełączenia na Archiwum i pierwsze wczytanie (1,2 MB). Do potwierdzenia na prawdziwym telefonie lub w DevTools (Performance, CPU 4× slowdown).
- Kodu Kalendarza nie zmieniałem.

## Odstępstwa i uwagi
- Numer 68 zamiast 67 (patrz wyżej). Worktree i gałąź robocza miały nazwę `zlecenie-67` z polecenia właściciela.
- Zlecenie mówiło „push po słowie »push«”. Właściciel w poleceniu startowym kazał wypchnąć na `main` bez czekania. Przed pushem: `git pull --rebase origin main` (doszedł commit `9f62de8d` z CLAUDE.md i .gitignore), ponowna budowa i kontrole.
