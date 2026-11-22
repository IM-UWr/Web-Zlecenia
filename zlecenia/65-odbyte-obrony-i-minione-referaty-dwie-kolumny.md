# Zlecenie 65 (22.11.2026): odbyte obrony i minione referaty w dwóch kolumnach jak minione Konferencje — WYKONANE

> Zapis po fakcie (changelog). Claude Code, 22.11.2026, ok. 23:15–23:30.

**Decyzje właściciela:**
- „Tak, tak samo”: odbyte obrony przygaszone jak minione referaty i konferencje (zlecenie 63);
- „układ obron doktorskich odbytych zrób taki sam jak przy konferencjach, czyli 2 kolumny i styl taki sam. Tak samo dla odbytych seminariów też daj taki sam styl”;
- „przy seminariach rozwinięcie streszczenia poszerza wiersz na całą kolumnę, a drugie wydarzenie, które było w wierszu, leci poziom wyżej albo poziom niżej, gdzie jest miejsce […] Rozwinięcie kolejnego streszczenia zwija poprzednie”.

## Co zrobiono (Web-Core 629c820a)
- `src/views/ListaObron.astro`, sekcja „Odbyte”:
  - wiersz bez wariantu „zwarty”, czyli taki jak w Konferencjach: dzień 34 px, data minionej szara;
  - na komputerze dwie kolumny (siatka i tytuł 19 px jak w `ListaKonferencji.astro`);
  - kandydat w `--text`, etykieta z `opacity: .8`, „Promotor:” w `--text`;
  - rok bez kreski pod spodem, jak w Konferencjach.

  „Nadchodzące” bez zmian (wariant zwarty, decyzja z 22.11 przy zleceniu 57).
- `src/views/Seminarium.astro`, „Minione referaty”: na komputerze dwie kolumny jak minione Konferencje (tytuł 19 px), przygaszenie z zlecenia 63 zostaje. Rozwijanie streszczenia:
  - rozwinięty wiersz zajmuje cały rząd (CSS `:has(details[open])`);
  - wiersz z lewej kolumny: sąsiad z prawej schodzi rząd niżej;
  - wiersz z prawej kolumny zostaje w swoim rzędzie, a sąsiad z lewej schodzi pod niego (skrypt ustawia `order`);
  - rozwinięte jest jedno naraz: `details name="streszczenie-minione"`, więc rozwinięcie kolejnego zwija poprzednie, także bez JS;
  - kliknięty wiersz nie ucieka spod kursora: po zwinięciu streszczenia wyżej strona przewija się o przesunięcie.

  Na telefonie jest jedna kolumna, jak dotąd. Bez JS lukę obok sąsiada wypełnia następny wiersz (`grid-auto-flow: dense`).

## Sprawdzenie
- Lokalnie (astro dev, Edge 1366 px, Seminarium Statystyka):
  - prawy wiersz rozwinięty: ten sam rząd i to samo miejsce na ekranie (y 354 → 354), szerokość 946 px, sąsiad niżej;
  - potem lewy wiersz rozwinięty: poprzedni zwinięty, miejsce bez zmian (523 → 523);
  - po zwinięciu układ wraca do wyjściowego.
- Obrony: 2 kolumny po 449 px (zrzut). Na telefonie (390 px) jedna kolumna (zrzut).
- Podgląd (przebieg 45077650288, success, Web-Core 629c820): ten sam test na żywej stronie daje ten sam wynik.
