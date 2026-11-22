# Zlecenie 63 (22.11.2026): minione referaty i konferencje przygaszone — WYKONANE

> Zapis po fakcie (changelog). Claude Code, 22.11.2026, ok. 22:45.

**Decyzje właściciela:** „w seminariach na stronie seminariów też zeszłe referaty zrób mniej wyraziste, jak na szybkim dostępie”; „I przy konferencjach to samo”.

## Co zrobiono (Web-Core 44c1464c)
Wzór jest z „Ostatnio” w Szybkim dostępie (`zalozyciele-strony.css`: `.z-w.minelo`, `.z-przeszle`): data w `--muted`, tytuł w `--text` zamiast `--ink`, etykieta z `opacity: .8`. Kolory są z tokenów, więc tryb ciemny nie potrzebuje osobnych reguł.
- `src/views/Seminarium.astro`: sekcja „Minione referaty” (`.ref.maly`); prelegent ma tu też grubość 500.
- `src/views/ListaSeminariow.astro`: referaty z „W tym tygodniu” 90 minut po początku dostają klasę `minelo`. Strona liczy to przy budowie, a skrypt na stronie oznacza też referaty, które skończyły się po zbudowaniu (`data-koniec`).
- `src/views/ListaKonferencji.astro`: sekcja „Minione” (lata).

## Sprawdzenie
Budowa Podglądu po pushu; wynik w `.przekazanie/dziennik.md` (wpis „jedno-media-obrony-minione”).
