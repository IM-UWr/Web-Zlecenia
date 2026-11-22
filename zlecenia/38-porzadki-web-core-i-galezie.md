# Zlecenie 38: porządki — pierwsza wersja strony do archiwum, raporty poza `main`, stare gałęzie (punkty 1 i 2 kolejki) (17.11.2026)

**Decyzje właściciela:**
- **7.11:** pierwsza wersja strony, zbudowana przed „Założycielami” (bez patronów; warianty Obecna, Zwarta, Portal, Redakcyjna), idzie w całości na osobną gałąź `archiwum/pierwsza-wersja` i znika z `main`. Raporty i zrzuty zostają tylko lokalnie.
- **13.11:** stare gałęzie w repozytoriach treści (np. `cms-reorganizacja-2026-11`, sprzed edycji redaktorów) — **nie scalać**, tylko usunąć. Każdą najpierw zachować jako znacznik `archiwum/<nazwa>`.
- **17.11, 22:45:** „to jest ważne” — zlecenie do kolejki.
- **17.11, 23:01:** we wszystkich repozytoriach z CMS ma zostać tylko `main`.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`.
- Wszystko, co zmienia GitHub (push, nowe znaczniki, usuwanie gałęzi), dopiero po „push” właściciela.
- **Nigdy force-push i nigdy przepisywanie historii** (bez `filter-repo` ani BFG). Historia zostaje, więc pełny klon Web-Core dalej waży ok. 159 MB. Zyskują płytkie klony (`depth 1`), np. budowa Podglądu i nowe sesje Code.
- **Praca równoległa:** to zlecenie może iść równolegle z linią CMS (31 → 39 → 33 → 40), w osobnym worktree. Jeśli w trakcie na `main` Web-Core trafią zmiany z innego zlecenia, przed pushem przenieś się na nowy `main` (rebase) i powtórz porównanie przed/po na nowej bazie.
- Raport `RAPORT-ZLECENIE-38.md` tylko lokalnie: po etapie 2 raporty nie trafiają na `main`.
- Oszczędnie: bez subagentów, czytaj tylko potrzebne pliki.

## Stan dziś (sprawdzone 17.11, 22:50)

### Web-Core `main` (`24c708e`, 9.11)
- **Raporty i zrzuty:**
  - `raport-zrzuty/`: 613 plików, 164 MB;
  - 21 plików `RAPORT-ZLECENIE-*.md` oraz `RAPORT-PORZADKI.md`, `RAPORT-WYGLAD.md` i `PYTANIA.md`;
  - razem 1008 śledzonych plików.
- **Pozostałości pierwszej wersji:**
  - 14 komponentów w `src/components/` poza `zal/` (część używana także przez „Założycieli”, sprawdzić importy);
  - 33 widoki w `src/views/` (część używana);
  - panel wariantów: `src/dev/panel-wariantow.ts`, `src/plugins/panel-wariantow.mjs`;
  - `skrypty/warianty.py`, `wyglad-podstron.json`;
  - style wariantów, m.in. `test-warianty.css`, `uklad-zwarta.css`, `portal.css`.
  - **Uwaga:** `uklad-portal.css` jest nadal potrzebny, bo od `data-uklad="… portal-baner"` zależy położenie hasła i liczb.
- **Workflowy:**
  - zostają: `deploy.yml` (wyłączony od 7.11; przyszła strona publiczna), `podglad-przekaznik.yml`, `plan-zajec.yml`;
  - do usunięcia razem z gałęziami: `sprawdz-galaz.yml` (budował gałęzie `agent-*` i `qa-*`, tworzył gałęzie `podglad-*`), `qa.yml` (`qa-*`), `proza-domyslna-test.yml` (gałąź `markdown-domyslna-proza-2026-11`).

### Gałęzie i znaczniki na GitHubie (`git ls-remote`, 17.11)
- **Web-Core:** 47 gałęzi poza `main`:
  - `agent-*` (12) i `podglad-agent-*` (12);
  - `kopia/*` (4), `robocza-*` (5), `wariant-*` (3), `wyglad/*` (7);
  - `cms-reorganizacja-2026-11`, `markdown-domyslna-proza-2026-11`, `markdown-jawne-bloki-2026-11`;
  - `archiwum/2026-11-09-silnik-banerow` — archiwum zrobione jako gałąź, opisane w `dok/archiwum-silnika-banerow.md`.

  Znaczniki: `archiwum/2026-11-07-main`.
- **Web-Podglad:** `cms-reorganizacja-2026-11` i `markdown-jawne-bloki-2026-11`. **`zbudowana` zostaje**: `podglad.yml` zapisuje na nią kopię zbudowanej strony i z niej czyta.
- **Web-Ustawienia:** 8 gałęzi: `agent-nauka-podglad`, `cms-reorganizacja-2026-11`, `kopia/2026-11-06`, `kopia/test-cms-zlecenie-22`, `robocza-nauka-tekst`, `robocza-studia`, `test-cms`, `wyglad/zlecenie-16`.
- **Web-Pracownicy:** `cms-reorganizacja-2026-11`.
- **Seminaria (9 repozytoriów `Web-Sem-*`):**
  - w każdym `cms-reorganizacja-2026-11`;
  - `kopia/2026-11-06`: Topologia, Teoria Modeli, Statystyka;
  - `wyglad/zlecenie-16`: Topologia, Teoria Modeli, Statystyka, Równania Różniczkowe;
  - `test-cms`: Topologia.
  - Część repozytoriów ma już znaczniki `archiwum/kopia/2026-11-06` i `archiwum/wyglad/zlecenie-16`. Równania Różniczkowe ma i znacznik, i gałąź `wyglad/zlecenie-16`, więc porównaj commity.
- **Specjalności (5 repozytoriów `Web-Spec-*`;** nie ma ich w `tresci.json`, zostają puste na później):
  - `cms-reorganizacja-2026-11`, `kopia/2026-11-06`, `wyglad/zlecenie-16`;
  - `test-cms` w Aktuarialno-Finansowej i Stosowanej.
- **Tylko `main`:** Web-Aktualnosci, Web-Studia, Web-Nauka, Web-Instytut, Web-Popularyzacja.

## Etap 1. Stare gałęzie (wszystkie repozytoria IM-UWr)
1. **Plan (lokalnie, bez zmian na GitHubie).** Napisz skrypt w `skrypty/porzadki/`. Dla każdego repozytorium organizacji, poza `.github`, i każdej gałęzi poza `main` i `zbudowana` (Web-Podglad) zbierz:
   - ostatni commit: data, autor, temat;
   - liczbę commitów spoza `main` (`git rev-list --count origin/main..gałąź`);
   - czy zmiany są już w `main` (`git cherry`);
   - czy istnieje znacznik `archiwum/<nazwa>` i czy wskazuje ten sam commit.
2. **Tabela w raporcie i STOP.** Gałęzie z commitami spoza `main` oznacz wyraźnie. Zasada z 13.11: nie scalamy, archiwizujemy znacznikiem.
3. **Po „push”:**
   - Dla każdej gałęzi utwórz znacznik `archiwum/<nazwa>`. Jeśli znacznik o tej nazwie już istnieje i wskazuje inny commit, użyj `archiwum/<nazwa>-2`.
   - Wypchnij znacznik i dopiero potem usuń gałąź.
   - `archiwum/2026-11-09-silnik-banerow` zamień na znacznik o tej samej nazwie i popraw odwołanie w `dok/archiwum-silnika-banerow.md`.
4. **Workflowy:** usuń z `main` Web-Core `sprawdz-galaz.yml`, `qa.yml` i `proza-domyslna-test.yml`. `Web-Podglad/.github/workflows/markdown-jawne-test.yml` (izolowany test jawnego Markdownu) zostaw i w raporcie zapytaj, czy jest jeszcze potrzebny.
5. **Kontrola:** `git ls-remote` w każdym repozytorium pokazuje tylko `main` (w Web-Podglad także `zbudowana`), a każda usunięta gałąź ma swój znacznik. Lista w raporcie.

## Etap 2. Web-Core `main`: tylko to, czego używa obecna strona („Założyciele”)
1. **Gałąź archiwum.** `archiwum/pierwsza-wersja` = obecny `main` z raportami, zrzutami i starym silnikiem. Utwórz ją lokalnie, a wypchnij razem z resztą po „push”.
2. **Wykrycie nieużywanych plików:**
   - graf importów od `src/pages/**`, `astro.config.mjs`, `src/content.config.ts` i skryptów z `package.json`;
   - plus pliki wskazane w workflowach (Web-Core, Web-Podglad), m.in. `skrypty/pobierz_tresci.py`;
   - ostrożnie z importami dynamicznymi (`import.meta.glob`), stylami przez `@import`, plikami w `public/` i odwołaniami w `dok/`.
   - Kandydat do usunięcia to plik spoza grafu. **Lista w raporcie, z podziałem na foldery.**
3. **Skrypty, które zostają** (używane przez workflowy i zlecenia):
   - `pobierz_tresci.py`, `sprawdz_pola_cms.py`, `sprawdz_tresci.py`;
   - `plan/`, `powiadomienia/`, `synchronizuj-katalog-opiekunow.mjs`;
   - narzędzia jawnego Markdownu (`*jawny-markdown*`, `usun-otoczki-proza.mjs`) i `test-edytora/`.

   **Do usunięcia:** jednorazowe migracje (`skrypty/migracja/`) i `warianty.py`; zostają w archiwum.
   - **Ale:** zlecenie 31 poprawia `skrypty/migracja/formularze.py`. Jeśli 31 nie jest jeszcze wypchnięte, zostaw `skrypty/migracja/` i zapisz to w raporcie. Usuniemy je później jednym commitem.
4. **Co usunąć z `main`:**
   - `raport-zrzuty/`, `RAPORT-*.md`, `PYTANIA.md`;
   - nieużywane komponenty, widoki, style i skrypty;
   - `wyglad-podstron.json` i panel wariantów;
   - martwe gałęzie kodu, które czytają te pliki (np. przełączniki wariantów).

   Następnie:
   - do `.gitignore` dopisz `raport-zrzuty/`, `RAPORT-*.md` i `PYTANIA.md`;
   - w `.przekazanie\zlecenia\zasady.md` dopisz, że raporty i zrzuty są tylko lokalnie;
   - zaktualizuj `README.md` i pliki `dok/`, jeśli wskazują usunięte pliki.
5. **Kontrola: identyczny wynik budowy.**
   - Zbuduj stronę przed i po z tymi samymi klonami repozytoriów treści, bez przerwy między budowami (część treści zależy od dzisiejszej daty).
   - Porównaj `dist/`:
     - HTML po normalizacji (nazwy plików `_astro` z hashami, białe znaki) ma **0 różnic**;
     - zawartość CSS i JS jest identyczna;
     - `sitemap.xml`, `.ics` i `pagefind` bez różnic w treści.
   - Każda różnica to błąd: przywróć plik.
6. **Kontrole:** `astro check` bez nowych błędów, testy wtyczek (`src/plugins/*.test.mjs`) zielone, budowa trwa nie dłużej niż przed zmianami.
7. **STOP:** raport z listą usuniętych plików, rozmiarem katalogu roboczego przed i po oraz wynikiem porównania. Potem czekasz na „push”.

## Kryteria odbioru
- [ ] We wszystkich repozytoriach IM-UWr tylko `main` (oraz `zbudowana` w Web-Podglad); każda usunięta gałąź ma znacznik `archiwum/…`.
- [ ] `archiwum/pierwsza-wersja` zawiera dawny `main` w całości.
- [ ] Na `main` Web-Core nie ma raportów, zrzutów ani plików, których budowa nie używa; `.gitignore` je pomija.
- [ ] Budowa przed i po daje identyczny wynik (0 różnic w HTML, CSS i JS).
- [ ] Usunięte workflowy gałęzi roboczych; `deploy.yml`, przekaźnik i plan zajęć zostają.
- [ ] Bez force-push i bez przepisywania historii.
