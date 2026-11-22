# Zlecenie 64 (22.11.2026): Tutornia w osobnym repozytorium Web-Tutornia — WYKONANE

> Zapis po fakcie (changelog). Claude Code, 22.11.2026, ok. 23:00–23:15.

**Decyzje właściciela:**
- „edycja Tutorni (CMS) ląduje do nowego repo Web-Tutornia. To damy studentom, niech sobie edytują. Zaktualizuj wszystkie miejsca, w tym instrukcje dla edytorów. Potem push”;
- nowe repozytorium treści jest publiczne (jak pozostałe: Web-Core i Podgląd pobierają treści bez klucza);
- „Po zakończeniu commit i push”.

## Co zrobiono
- **Web-Tutornia** (nowe, publiczne repozytorium IM-UWr, pierwszy commit 99ba1b0):
  - `src/content/strony/studia/tutornia.md`: strona przeniesiona z Web-Studia bez zmian treści, adres `/studia/tutornia` (i `/en/…`) bez zmian;
  - `.pages.yml`: jeden formularz „Tutornia” (typ `file`, ten jeden plik) z polami kolekcji „Strony studiów”, żeby zapis w CMS nie gubił danych. W opisie Treści i Treści EN zostaje podpowiedź o `:::grafik`. Media jest jedno: `public/pliki/tutornia` (`/pliki/tutornia`, folder dopisany do `.gitignore` Web-Core);
  - `.github/workflows/powiadom.yml` jak w innych repozytoriach: po zapisie sygnał przebudowy do Web-Core;
  - `README.md` dla studentów: jak edytować, plan dyżurów (`:::grafik`), zasada linku do pliku, ostrzeżenie, że repozytorium jest publiczne.
- **Web-Studia** (693aac9): strona Tutorni usunięta, a „Strony studiów” nie mają już wzmianki o `:::grafik` w opisach Treści (`:::pary` zostaje).
- **Web-Core** (81eb5a0c):
  - `tresci.json`: Web-Tutornia po Web-Studia;
  - instrukcje: README (wiersz w tabeli repozytoriów), mapa CMS (Tutornia z przyciskiem „Web-Tutornia ↗”, bez linku w „Stronach studiów”), `dok/sciagawka-edytora.md` (Web-Tutornia → Tutornia → Treść), `dok/jawny-markdown.md`; komentarz w `src/plugins/grafik.test.mjs`.
- **Web-Podglad** (37f7a11): PDF mapy CMS (2 strony).

## Sprawdzenie
- Pola formularza obejmują wszystkie klucze front matter strony. Strona w Web-Tutornia jest identyczna z dawną w Web-Studia.
- `sprawdz_pola_cms.py` na klonach (17 repozytoriów): 0 problemów.
- Nałożenie treści lokalnie (`pobierz_tresci.py --lokalnie`): bez kolizji. Web-Tutornia daje 1 plik, a `tutornia.md` pochodzi tylko z niej.
- Testy grafiku (`grafik.test.mjs`): 11/11. PDF mapy: 2 strony, treść mieści się.
- Automat `powiadom.yml` w Web-Tutornia (przebieg 45075859634): klucz aplikacji i sygnał do Web-Core zakończone sukcesem, czyli sekret i zmienna organizacji są widoczne dla nowego repozytorium.
- Pages CMS (Chrome właściciela): Web-Tutornia otwiera się od razu na formularzu „Tutornia” z całą treścią i grafikiem, więc aplikacja Pages CMS ma dostęp do nowego repozytorium. „Strony studiów” w Web-Studia nie mają już Tutorni. Niczego nie zapisywano.
- Budowa Podglądu i strona `/studia/tutornia` po pushu: wynik w `.przekazanie/dziennik.md` (wpis „tutornia-web-tutornia”).

## Do zrobienia przez właściciela
- Dostęp dla studentów-tutorów: w Pages CMS, w repozytorium Web-Tutornia, „Admin → Collaborators”: zaproszenie e-mailem, bez konta GitHub. Można też dodać ich na GitHubie jako współpracowników z prawem zapisu.
