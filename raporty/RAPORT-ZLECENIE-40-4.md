# Raport: zlecenie 40, etap 4 — Web-Pracownicy (18.11.2026)

## Dlaczego etap 4 przed etapem 3
Etap 3 to Web-Aktualnosci. Druga sesja (okno Web-Core-B) ma w tym repozytorium niezatwierdzone zmiany `.pages.yml` (zlecenie 44, „Kariera”, wstrzymane; wpis w dzienniku 14:16). Gdybym teraz przestawił i opisał formularze Aktualności, jej zmiany trafiłyby na konflikt w tych samych miejscach pliku. Etap 4 od etapu 3 nie zależy, więc zrobiłem go najpierw. Etap 3 zrobię, gdy zlecenie 44 będzie wypchnięte.

## Stan
> **Aktualizacja 18.11, 17:20:** Web-Pracownicy wypchnięte 18.11 o 16:57 (przed wieczorem, na Twoje polecenie) — wynik w „Push treści”.

- **Web-Core: wypchnięte** `23050dd2..641cf76e`: zmiana tylko w skrypcie `skrypty/migracja/formularze_40.mjs` (opis formularzy Web-Pracownicy), strona bez zmian. Przed pushem rebase na zlecenie 44 z drugiego okna, budowa i `astro check` od nowa. **Podgląd zielony**: run 44319917747 zbudował stronę z `641cf76e`.
- **Push treści zaplanowany na 21:43** (po 33 o 20:07, 40.1 o 20:41 i 40.2 o 21:13).
- **Web-Pracownicy: commit gotowy, push wieczorem** (po treściach zlecenia 33). Skrypt: `push40_pracownicy.sh` w scratchpadzie.
  - Sprawdzając warunki skryptów pushów, znalazłem błąd we wszystkich trzech (40.1, 40.2, 40.4): Git Bash zamieniał `origin/main:.pages.yml` na ścieżkę Windows, więc warunek „zlecenie 33 jest już na main” zawsze kończył się STOP. Poprawione (`MSYS_NO_PATHCONV=1` tylko w tym poleceniu) i sprawdzone na commicie 33. Porównania HTML tego błędu nie miały (czytają pliki `src/…`, które działają).
  - Klon roboczy: `tresci-z40/Web-Pracownicy`, gałąź `praca/40-pracownicy`, commit `ff4aec1` na commicie zlecenia 33 (`4015203`, jeszcze niewypchniętym).
  - **Baza** (świeży `main`): `5bcaf22`. O 14:58 brak zapisów redaktorów od bazy.

## Co zrobiłem (commit `ff4aec1`: `.pages.yml` i jeden plik)
- **`src/content/strony/pracownicy.md` → jawny Markdown:** `format_tresci: jawne` i komentarz `<!-- UKŁAD JAWNY: … -->` w Treści. Treść była pusta i taka zostaje (sam komentarz nie trafia na stronę). Nagłówków `##` nie ma.
- **Formularz Strony:** tytuł, tytuł EN, Opublikowane → Treść, Treść EN → reszta; ściągawka jawnego Markdownu (z informacją, że tekst stoi nad listą osób); ukryte `format_tresci` i dawne „Bloki wzorca”; „Krótki opis (Google i podgląd linku)” z przykładem.
- **Formularz Pracownicy:** opis z raportu 40-0 („Spis osób: pracownicy, doktoranci, administracja. Widać go w Pracownikach, na stronach zakładów i przy władzach.”). Kolejność pól bez zmian (formularz nie ma Treści).

## Kontrole
- **Porównanie HTML całej strony** (nowy kod: dane Web-Pracownicy `origin/main` → commit, 923 pliki): **0 różnic** (PL i EN). Zrzutów nie robiłem.
- `astro check`: 0 błędów (po rebase na zlecenie 44 z drugiego okna).
- `sprawdz_pola_cms.py`: **0 problemów** (724 pliki, 16 repozytoriów, Web-Pracownicy z klonu roboczego).
- `sprawdz-jawny-markdown.mjs`: **OK** (1 plik, bez nagłówków `##`).
- `kontrola_redaktorow.py`: `po` (4015203 → ff4aec1): zmienione tylko `body` i `format_tresci` w 1 pliku i `.pages.yml` — „OK, tylko zmiany z migracji”; `przed`: 0 zapisów od bazy.

## Przyjąłem sam
- **Kolejność etapów 4 przed 3** (powód wyżej).
- **Komentarz `UKŁAD JAWNY` także w pustej Treści**, jak we wszystkich Stronach po migracji: redaktor, który zacznie pisać tekst nad listą, od razu widzi zasady.

## Pytania do Ciebie
Brak nowych.

## Push treści (18.11, 16:55–16:58, przed wieczorem na Twoje polecenie: „Dobra, zgadzam sie wrażamy teraz”)
- baza = commit zlecenia 33 na `main` (`4015203`); `origin/main` = baza, więc commit `ff4aec1` poszedł bez ponownej migracji;
- `sprawdz-jawny-markdown`: OK; `sprawdz_pola_cms.py`: 0 problemów; kontrola redaktorów przed: 0 zapisów od bazy;
- porównanie HTML całej strony: **0 różnic** w 925 plikach;
- **wypchnięte `4015203..ff4aec1`**; kontrola po pushu: OK;
- Podgląd: **zielony** — przebieg 44341742516 zbudował stronę z `ff4aec1`.

## Następnego dnia (19.11)
- Test w CMS: Strony → Pracownicy (otwarcie, zapis bez zmian); Pracownicy → dowolna osoba (otwarcie, zapis bez zmian: diff pusty).
- Przegląd zapisów redaktorów z 24 h po pushu: czy nikt nie usunął `format_tresci`.
