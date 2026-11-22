# Zlecenie 39: kierunki w menu i kafelkach bez automatów; studia podyplomowe jako kierunek (punkty 4 i 7 kolejki) (17.11.2026)

**Decyzje właściciela (7.11, 19:11–19:40; 17.11, 22:45 „to jest ważne”):**
- **Lista kierunków zostaje w Web-Ustawienia** (Strona główna i kontakt → Sekcja „Studiuj matematykę” → „Kierunki w menu „Studia” i kafelki na stronie głównej”). Przeniesienie listy do Web-Studia odwołane.
- **Bez automatu „spoza listy”.** Do menu i kafelków trafia tylko to, co ktoś świadomie dopisał na listę.
- **Bez ukrytych wartości domyślnych.** Każda pozycja ma wszystko wpisane jawnie, więc redaktor nie szuka w dwóch miejscach.
- **Studia podyplomowe jako kierunek,** z jedną pozycją na liście.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- **Repozytoria treści** (Web-Ustawienia, Web-Studia): zasady z kolejki, punkt 3, i sekcja „Ochrona zmian redaktorów” niżej:
  - zawsze od świeżego `main`, zwykły commit, nigdy force-push;
  - najpierw Web-Core, potem treści; `.pages.yml` i dane jednego repozytorium w jednym commicie.
- **Przed zleceniem 33:** jego migracja dopisze `opublikowany` także do nowego pliku kierunku.
- Raport `RAPORT-ZLECENIE-39.md`, zrzuty `raport-zrzuty/z39-*`. Bez subagentów.

## Ochrona zmian redaktorów (obowiązkowo przy każdym pushu do repozytorium treści)
Redaktorzy zapisują w CMS na żywo, także w trakcie tego zlecenia. Ich zmiany nie mogą zginąć. Tu dotyczy to zwłaszcza pliku `podyplomowe.md`, który przenosisz, i `nawigacja.json` / `ustawienia.json`.

1. **Migracja na najświeższej wersji.**
   - Tuż przed pushem: `git fetch` i sprawdź, czy na `main` przybyły zapisy redaktorów od chwili, gdy zacząłeś (`git log <baza>..origin/main`). Baza = HEAD zanotowany na początku pracy.
   - Jeśli przybyły, nie doklejaj starego wyniku. Przełącz się na świeży `main` i **powtórz zmianę**: przeniesienie pliku z jego aktualnej treści, migrację listy.
   - Konflikty rozwiązuj ręcznie: weź wersję redaktora i nanieś na nią swoją zmianę. Nigdy odwrotnie i nigdy hurtem całych plików (`-X ours`, `checkout --ours/--theirs`).
2. **Kontrola przed pushem** (skrypt, wynik w raporcie):
   - weź każdy zapis redaktora od bazy (autor inny niż Code) i każdy plik, który zmienił;
   - porównaj pole po polu jego wersję z wersją, którą wypychasz. Przy przeniesionym pliku porównaj stary i nowy plik;
   - każda wartość wpisana przez redaktora musi być w wyniku. Inaczej **STOP**.
3. **Kontrola po pushu:** porównanie pole po polu przed i po (Web-Ustawienia; w Web-Studia stary plik podyplomowych z nowym). Różnice tylko w polach zmienianych celowo; lista w raporcie.
4. **Okno pusha:** wieczorem albo po wiadomości od właściciela do redaktorów: „zapiszcie i zamknijcie CMS na 15 minut, potem odświeżcie stronę”.
   - Pages CMS przy zapisie sprawdza wersję pliku. Jeśli plik zmienił się od otwarcia formularza, zapis jest odrzucony („File has changed since you last loaded it”) i nic nie zostaje nadpisane. Redaktor traci jednak to, co wpisał, a nie zapisał.
   - Strona podyplomowych otwarta w starym formularzu „Strony” i zapisana po pushu odtworzyłaby stary plik. **Następnego dnia** przejrzyj zapisy redaktorów z 24 godzin po pushu: czy nie powstał z powrotem `strony/studia/podyplomowe.md` i czy nikt nie usunął nowych pól. Znalezione popraw osobnym commitem, przenosząc zmianę redaktora do nowego pliku.
5. **Wszystko da się odwrócić:** każdy zapis redaktora to osobny commit. W razie straty przywróć wartość z historii **nowym commitem** (nigdy `reset` ani force-push) i opisz to w raporcie.

## Stan dziś (17.11)

**Web-Core, `src/lib/kierunki.ts` (72 linie):**
- `listaKierunkow()` (ok. linii 22–29): kierunki z listy w jej kolejności, a **kierunki spoza listy na końcu, alfabetycznie**.
- `pozycjeKierunkow()` (ok. linii 48–60): do pozycji z listy **dopisuje kierunki spoza listy** z poziomem „Kierunek” / „Programme” i zdaniem z banera albo pierwszym zdaniem treści (`pierwszeZdanie`).
- Typ `PozycjaKierunku`: `adres`, `nazwa`, `poziom`, `opis` (kafelek), `opis_menu` (pod nazwą w menu), `w_menu`, `na_stronie_glownej` oraz wersje EN.
- Komentarz przy `opis_menu`: puste pole w menu zastępuje pełna nazwa kierunku. Zastępowanie pustych pól jest też w `src/lib/menu.ts`; wyszukaj wszystkie miejsca.

**Lista** (`Web-Ustawienia/src/data/ustawienia.json` → `studia.kierunki`), 5 pozycji:

| Pozycja | Adres | Uwagi |
|---|---|---|
| Matematyka | `/studia/matematyka` | jest opis w menu („I i II stopień, pięć specjalności”) |
| Sztuczna inteligencja w analizie danych | `/studia/siad` | **bez opisu w menu**: dziś bierze pełną nazwę z Web-Studia |
| ISIM | `/studia/isim` | **bez opisu w menu**: dziś bierze pełną nazwę z Web-Studia |
| Szkoła doktorska | `/studia/szkola-doktorska` | jest opis w menu („Kolegium Doktorskie Matematyki”) |
| Nauczanie matematyki | `/studia/podyplomowe` | poziom „Podyplomowe”, `w_menu: false` |

**Kierunki w Web-Studia:** `isim`, `matematyka`, `siad`, `szkola-doktorska`. Plik `kierunek-testowy.md` już usunięty.

**Studia podyplomowe dziś są w trzech miejscach:**
- **Strona:** `Web-Studia/src/content/strony/studia/podyplomowe.md`, jawny Markdown, 185 linii. Ma tytuł, opis, hasło i liczby (3 semestry, 380 godzin zajęć, 90 godzin praktyk; PL/EN). Pliki leżą w `public/pliki/studia/podyplomowe/`.
- **Ręczny link w menu:** `Web-Ustawienia/src/data/nawigacja.json` (ok. linii 182–186), w menu „Studia” → „Kierunki”: „Studia podyplomowe — kwalifikacje do nauczania” (EN „Postgraduate studies — teaching qualifications”).
- **Pozycja na liście:** „Nauczanie matematyki” z `w_menu: false`, pokazywana tylko jako kafelek.

## Etap 1. Bez automatu i bez wartości zastępczych
1. **Tylko pozycje z listy.** Menu „Studia”, panel hamburgera, pole kierunków na `/studia` i kafelki strony głównej pokazują wyłącznie pozycje z listy, w jej kolejności. Usuń dopisywanie kierunków spoza listy (`pozycjeKierunkow`, `listaKierunkow`, `menu.ts` i inne miejsca).
2. **Kierunek spoza listy:**
   - strona `/studia/<id>` nadal się buduje i jest dostępna pod adresem;
   - budowa wypisuje ostrzeżenie: „Kierunek <nazwa> nie jest na liście w Ustawieniach — nie ma go w menu ani w kafelkach”.
3. **Bez zastępowania pustych pól.** Usuń z kodu wszystkie wartości zastępcze pozycji listy: pełną nazwę zamiast opisu w menu, zdanie z banera zamiast opisu kafelka itp. Strona pokazuje to, co jest na liście.
4. **Migracja (Web-Ustawienia, jeden commit z formularzem).** Wpisz do istniejących pozycji wartości, które strona pokazuje dziś, także te liczone zastępczo (np. opis w menu SIAD i ISIM, PL i EN). Wynik: **menu i kafelki wyglądają identycznie**.
5. **Formularz listy w `.pages.yml` Web-Ustawienia:**
   - pola jak dziś: adres, poziom, nazwa, opis w menu, opis na kafelku, „pokaż w menu”, „pokaż na stronie głównej” (jeśli `na_stronie_glownej` działa w kodzie; inaczej opisz w raporcie) i wersje EN;
   - **wymagane:** nazwa i opis w menu;
   - opisy pól user-friendly (wzór: formularze Web-Studia): gdzie dane pole widać na stronie, z przykładem;
   - usuń z opisu listy zdania o automacie i pustych polach. Dopisz: „Nowy kierunek pojawi się w menu i kafelkach dopiero po dodaniu go tutaj”.
6. **Dokumentacja:**
   - zaktualizuj komentarze w `kierunki.ts` i `menu.ts`;
   - zaktualizuj `dok/sciagawka-edytora.md`;
   - PDF dla redaktorów (`Web-Podglad/dla-redaktorow/Mapa-CMS-IM-UWr.pdf`, strona 2, „Jak dodać nowy kierunek”, kroki 3–4): kierunek pojawia się w menu dopiero po dopisaniu na listę w Ustawieniach, co robi administrator. Jeśli nie znajdziesz źródła PDF, wypisz w raporcie zdania do podmiany.

## Etap 2. Studia podyplomowe jako kierunek
1. **Przeniesienie pliku w Web-Studia:** `src/content/strony/studia/podyplomowe.md` → `src/content/kierunki/podyplomowe.md`. Adres zostaje `/studia/podyplomowe`.
   - Plik dostaje format kierunku: jawny Markdown, baner w tym samym wpisie (nadtytuł, zdanie pod nazwą, hasło, liczby PL/EN) z dzisiejszych pól.
   - Tekst i komentarze `<!-- … -->` zostają bez zmian.
   - Pliki w `public/pliki/studia/podyplomowe/` bez zmian.
2. **Jedna pozycja na liście.** „Nauczanie matematyki” dostaje „pokaż w menu”, a ręczny link usuń z `nawigacja.json`.
   - **Menu ma wyglądać jak dziś:** „Studia podyplomowe — kwalifikacje do nauczania”.
   - Jeśli lista nie pozwala mieć innej nazwy w menu niż na kafelku, zaproponuj w raporcie rozwiązanie (np. osobne pole „nazwa w menu”) ze zrzutem. Nie zmieniaj wtedy nazwy na kafelku bez decyzji właściciela.
3. **Wygląd strony.** Szablon kierunku może się różnić od zwykłej strony (baner, spis, liczby). Każdą różnicę pokaż na zrzucie przed/po (PL i EN, komputer i telefon) i opisz. Ewentualne poprawki tylko po decyzji właściciela.
4. **Odwołania.** Sprawdź linki do `/studia/podyplomowe` (adres bez zmian), mapę strony, okruszki, „Następna strona w dziale” i kafelek specjalności „Nauczycielska”, jeśli linkuje.

## Odbiór lokalny
- **Porównanie HTML przed i po:** menu „Studia”, panel hamburgera, `/studia`, strona główna (kafelki), 4 kierunki PL i EN. **0 różnic.**
- **Wyjątek:** `/studia/podyplomowe` PL i EN, gdzie różnice są tylko zgłoszone i pokazane na zrzutach.
- **Test automatu:** lokalnie dodaj plik kierunku spoza listy. Nie pojawia się w menu ani w kafelkach, budowa wypisuje ostrzeżenie, a strona pod adresem działa. Po teście plik usuń.
- **Kontrole:** `sprawdz_pola_cms.py` (Web-Ustawienia, Web-Studia) 0 problemów; `skrypty/sprawdz_tresci.py` OK; `astro check` bez nowych błędów.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Menu, hamburger, pole kierunków i kafelki pokazują tylko pozycje z listy; kierunek spoza listy ma stronę, ale nie pojawia się sam.
- [ ] W kodzie nie ma wartości zastępczych dla pozycji listy; lista ma wszystko wpisane jawnie; wygląd bez zmian.
- [ ] Studia podyplomowe są kierunkiem z jedną pozycją na liście; ręczny link zniknął z menu; menu wygląda jak dziś.
- [ ] Formularz listy z jasnymi opisami; ściągawka i PDF (albo lista zdań do podmiany) zaktualizowane.
- [ ] Kontrola zmian redaktorów przed i po pushu w raporcie: wszystkie zapisy redaktorów zachowane. Przegląd z następnego dnia zrobiony.
