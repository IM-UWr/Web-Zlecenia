# Zlecenie 61 (22.11.2026): link do pliku = ścieżka w Media; jedno Media w każdym repozytorium — WYKONANE

> Zapis po fakcie (changelog). Claude Code, 22.11.2026, ok. 22:15–23:00.

**Skąd to zlecenie.** Po zleceniu 60 redaktor musiał wpisywać pełny adres `/pliki/seminaria/rownania-rozniczkowe/plik.pdf`. W repozytoriach z kilkoma źródłami Media („Media: studia”, „Media: szkoła doktorska”) zasada była nieintuicyjna.

**Decyzje właściciela:**
- „redaktorzy […] tylko wpisują adres, jak by od razu byli w media […], a strona sobie sama ogarnia na podstawie tego, z którego repozytorium wchodzimy. A jeśli ktoś chce z innego repozytorium, to musi np. Nazwa/repozytorium i potem ścieżka. Maximal friendly dla edytorów”;
- „Folder Media powinien być jeden w każdym repo i redaktor powinien wpisywać adres dokładnie na podstawie folderów, który widzi. Czyli plik w media: nazwa pliku. Plik w Folderze1: Folder1/plik.pdf”;
- „piszemy ogólną zasadę w instrukcji”;
- „wywal z instrukcji repozytoria specjalności”;
- „Jeśli umiesz zrobić bez pytań, to zrób i push”.

## Zasada dla redaktorów
W linku wpisz, gdzie plik leży w Media:
- `[tekst](plik.pdf)`: plik leży bezpośrednio w Media;
- `[tekst](Folder1/plik.pdf)`: plik w folderze, tyle folderów, ile widać;
- `[tekst](Web-Nauka/folder/plik.pdf)`: plik z Media innego repozytorium.

Pełne `/pliki/…` też działa. Brakujący plik daje ostrzeżenie „Plik w treści”, a nie błąd budowy.

## Co zrobiono
- Web-Core:
  - nowy `skrypty/adresy_plikow.py` z testami `skrypty/test_adresy_plikow.py`;
  - `pobierz_tresci.py` przy nakładaniu zamienia krótkie adresy w linkach i obrazkach Markdownu w `src/` na pełne;
  - `sprawdz_pola_cms.py` wymaga jednego Media w repozytorium;
  - domyślne zdjęcia nagłówków działów są teraz w `/pliki/ustawienia/naglowki/` (`NaglowekStrony.astro`, `zal/NaglowekZ.astro`).
- Jedno Media, a dawne foldery stały się podfolderami:
  - Aktualności: `aktualnosci/obrony`;
  - Instytut: nowy folder `instytut`, w nim `warto-wiedziec`, `wladze`, `zaklady` (30 plików);
  - Nauka: `nauka/konferencje`;
  - Studia: `studia/szkola-doktorska` (86 plików);
  - Ustawienia: `ustawienia/baner`, `naglowki`, `partnerzy` (9 plików).
  Odwołania przepisano w 25 plikach treści i w polach formularzy.
- Podpowiedź przy polu „Treść” w 14 repozytoriach (Studia i Popularyzacja nie miały podpowiedzi o plikach).
- Instrukcje: README („Dla redaktorów”, bez wiersza Web-Spec-…), `dok/dla-redaktorow/mapa-cms.html` z PDF-em w Web-Podglad, `dok/sciagawka-edytora.md`.
- Pokaz: link do artykułu Nadziei w Równaniach ma postać `(nadzieja-seminarium.pdf)`.

## Commity
- Web-Core: d6bf55a8 (krótkie adresy), 44c1464c (jedno Media, instrukcje).
- Web-Podglad: 4a67c10, c9f7b20 (PDF).
- Repozytoria treści: 8189168 (Równania, link) oraz 22.11 ok. 22:55 po jednym commicie w każdym z 16 (Aktualności: trzy).

## Sprawdzenie
- Testy adresów: 9/9.
- Nałożenie wszystkich treści przed zmianą i po niej:
  - 1378 odwołań `/pliki` przed i po;
  - martwych linków 12 przed i 12 po (stare, sprzed zmiany);
  - żaden plik nie zniknął.
- `sprawdz_pola_cms.py`: 0 problemów.
- Podgląd po pierwszej części: link w Równaniach prowadzi do PDF (200).
