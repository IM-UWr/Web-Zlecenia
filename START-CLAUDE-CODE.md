# Start sesji Claude Code: strona IM UWr (5.11.2026)

Przeczytaj to na początku każdej nowej sesji. Potem użytkownik poda nazwę pliku zlecenia z `.przekazanie\zlecenia\` (np. `11-poprawki-i-podstrony.md`) i to zlecenie wykonujesz.

## Podział pracy
- Koncepcje, prototypy i zlecenia przygotowuje rozmowa w claude.ai (projekt „IM Strona”). **Kod zmieniasz Ty**, w tym folderze (`C:\Users\Szymek\Documents\GitHub\Web-Core`, Astro 5, treści z repozytoriów IM-UWr/Web-* jako lokalna nakładka w `src/data`, `src/content`, `public/pliki`).
- Przed zleceniem przeczytaj `.przekazanie\zlecenia\zasady.md` (z uwagą na górze) i **całe** zlecenie. **Nagłówek zlecenia ma pierwszeństwo** (gałąź, baza, zakres, commity).

## Zasady stałe
- Odpowiadaj po polsku.
- **Push na GitHub tylko po słowie „push” od właściciela.** Commity lokalne — tylko jeśli zlecenie tak mówi.
- **Nie uruchamiaj `skrypty/pobierz_tresci.py`** (nadpisze lokalne teksty w nakładce). Nie zmieniaj repozytoriów treści (Web-*).
- W `.przekazanie\` zmieniaj tylko `dziennik.md` i `pola-do-cms.md`.
- Każdy nowy tekst w wersji PL i EN; nowe pola CMS dopisz do `.przekazanie\pola-do-cms.md`.
- Nie dodawaj zależności npm bez potrzeby (jeśli trzeba — opisz w dzienniku).

## Materiały wzorcowe
- Po `git fetch origin` czytaj z gałęzi `origin/kopia/2026-11-01-estetyka-prototypy` przez `git show origin/kopia/2026-11-01-estetyka-prototypy:<ścieżka>` (**nie scalaj tej gałęzi** — nie ma wspólnej historii z kodem): prototyp `proto/zalozyciele.src.html` (wartości CSS i zachowanie), `dok/estetyka.md` (specyfikacja wyglądu), `ciekawostki/<patron>/ciekawostki.json`, `zdjecia/wybrane/*`.
- Raporty poprzednich prac są w repozytorium: `RAPORT-WYGLAD.md`, `RAPORT-PORZADKI.md`, `PYTANIA.md`, `dok/en/POSTEP.md`.

## Sprawdzanie
- `npm run build` bez błędów, `npx astro check` bez nowych błędów.
- Zrzuty (Playwright, jeśli jest; inaczej opisz, jak sprawdziłeś): komputer 1440 i 1920 px, telefon 390 px, jasny i ciemny motyw.
- Użytkownik może mieć uruchomione serwery na portach 4321 (ten folder) i 4322 (`..\Web-Core-porzadki`) — do własnych testów używaj innego portu.

## Gdy coś niejasne
- Wybierz rozwiązanie najbliższe prototypowi i ustaleniom, zapisz pytanie w raporcie/dzienniku i pracuj dalej; nie zatrzymuj się na drobiazgach.
- Decyzji oznaczonych w zleceniu jako „CZEKA” nie wykonuj.

## Przerwana sesja
- Jeśli zaczynasz od nowa w trakcie zlecenia: sprawdź `git status`, `git log` na gałęzi zlecenia i `.przekazanie\dziennik.md`, potem kontynuuj od następnego niezrobionego punktu.

## Na koniec zlecenia
- Raport wskazany w zleceniu i wpis w `.przekazanie\dziennik.md` (format w `zasady.md`).
