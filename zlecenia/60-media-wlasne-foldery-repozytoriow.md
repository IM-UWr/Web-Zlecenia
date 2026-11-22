# Zlecenie 60 (22.11.2026): każde repozytorium treści ma własny folder Media — WYKONANE

> Zapis po fakcie (changelog). Praca wykonana w rozmowie z właścicielem w Claude Code 22.11.2026, ok. 19:30–22:15.

**Skąd to zlecenie.** Redaktor seminarium Równań różniczkowych wgrał PDF do Media i pytał, jak go podlinkować. Wyszło przy tym, że Media wszystkich repozytoriów trafia na stronie do wspólnego `/pliki`. Ten sam plik w dwóch repozytoriach zatrzymywał więc budowę, a Podgląd zostawał w starej wersji bez czytelnego komunikatu. Pages CMS nie widzi plików innych repozytoriów, więc tego nie wykryje.

**Decyzje właściciela:** „Czy możemy to jakoś naprawić?” → „Wszystkie repozytoria”; „Zrobisz push i od razu zaktualizujesz githuba?”; „I zaktualizuj instrukcje dla redaktorów”; „Przywróć rolę” (PTM w organizatorach Popularyzacji).

## Co zrobiono
- 16 repozytoriów treści: w `.pages.yml` Media tylko we własnych folderach repozytorium (`public/pliki/<folder>`, np. seminarium `seminaria/<slug>`), a pola plików i obrazków wskazują swój folder. Pliki przeniesiono, odwołania przepisano.
- `skrypty/pobierz_tresci.py`: gdy ten sam plik jest w dwóch miejscach, na GitHubie powstaje adnotacja „Błąd plików” ze zdaniem dla redaktora. Plakietka stanu budowy na Podglądzie ją pokazuje.
- `skrypty/sprawdz_pola_cms.py`, punkt 4: pilnuje folderów Media (własne, niepokrywające się, pola z `options.media`, pliki tylko w Media).
- README i mapa CMS (PDF w Web-Podglad): foldery Media i „-1” przy powtórzonej nazwie.
- Web-Popularyzacja: przywrócona rola „konkurs od 1967” przy PTM w `:::kontakty` (budowa Podglądu wróciła).

## Commity
Web-Core 55693cab; Web-Podglad 3febc95 (PDF); repozytoria treści: f783881 (Równania), 85a9ff7 (Popularyzacja, PTM) i po jednym w pozostałych.

## Sprawdzenie
Pages CMS w Chrome właściciela pokazuje własne foldery. `sprawdz_pola_cms.py` na klonach: 0 problemów (wcześniej 16 zgłoszeń). Symulowana kolizja daje adnotację. PDF działa pod nowym adresem na Podglądzie (200), a stary adres daje 404.

Ciąg dalszy: zlecenia 61 i 62 (jedno Media w repozytorium, link = ścieżka w Media, obrony).
