# Zlecenie 57 (22.11.2026): lista Obron doktorskich jak Konferencje, czyli lata jako sekcje i spis „Na tej stronie”

**Skąd to zlecenie.** 22.11 na listę obron (`/obrony-doktorskie`) trafiło 47 archiwalnych obron ze starej strony (2013–2026). Razem jest 52 obron, a ich PDF-y leżą w repozytorium `IM-UWr/Obrony-Archiwum` (projekt: `claude/obrony-archiwum.md`). Panel „Pokaż” z prawej ma teraz 15 przycisków (Wszystkie, 2026…2013) i pole szukania, a lista „Odbyte obrony” to jeden długi ciąg bez podziału.

**Decyzja właściciela (22.11, 13:33–13:39):**
- „zrób tak jak na pozostałych podstronach, oraz podziel listę latami”, „odbyte zrobić sekcje przy roku”;
- prototyp zaakceptowany: „Bardzo dobrze”;
- „Pole szukaj out. Archiwum out.”;
- stare adresy `?rok=RRRR` prowadzą do sekcji roku: „Dobrze”.

**Prototyp:** https://claude.ai/artifact/KXKgsNSGEwXFQHWvv2xSng (wersja bez przykładowych obron). Zbudowany ze strony Podglądu z 22.11, 12:29Z. Źródło jest w `.przekazanie\prototypy\57-obrony-lata\`: `index.html` i skrypt `build.py`. Wzorem układu jest `src/views/ListaKonferencji.astro`.

## Zasady pracy
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- **Na start pobierz świeże treści:** `python3 skrypty/pobierz_tresci.py`. 22.11 doszło 47 obron, a lokalna nakładka ich nie ma. To zlecenie ma pierwszeństwo przed zakazem z `START-CLAUDE-CODE.md`, tak jak w zleceniu 56.
- **Tylko Web-Core.** Repozytoriów treści nie zmieniasz.
- Raport `RAPORT-ZLECENIE-57.md`, zrzuty `raport-zrzuty/z57-*`. Bez subagentów.
- **Kolejność:** jeśli inne otwarte zlecenie zmienia `ListaObron.astro`, `listaObron.ts` albo `WierszWydarzenia.astro`, to zlecenie robisz po nim.

## Stan dziś (Web-Core `main`, 22.11)
- `src/views/ListaObron.astro` używa `zal/ListaPokaz.astro`:
  - filtr lat (`data-filtr`, `?rok=…`) i pole „Szukaj w obronach”;
  - grupy „Nadchodzące obrony” i „Odbyte obrony” (`h2`, `section.ob-grupa`);
  - pod listą link „Archiwum starej strony” (`ustawienia.archiwum` + `postepowania-w-sprawie-nadania-stopnia-doktora-…`);
  - skrypt filtra na dole pliku;
  - bez spisu „Na tej stronie”, ramka `z-pd-pelna`.
- `src/lib/widoki/listaObron.ts` zwraca `przyszle`, `odbyte`, `lata`, teksty strony i `ustawienia`.
- Wiersz to `WierszWydarzenia.astro` (`zwarty`, `bezRodzaju`, slot z promotorem `.ob-prom`). `poziom` przyjmuje dziś tylko `'h2' | 'h3'`.

## Docelowo
1. **Układ jak w Konferencjach.**
   - `Podstrona` ze spisem (`spis`), `dzial="nauka"`, klasa treści z `.tresc`, bez `ListaPokaz` i bez ramki `z-pd-pelna`.
   - Baner bez zmian: hasło, bez liczb (`hasloBezLiczb`), okruszki „← Nauka”.
   - Tekst nad listą (Treść strony Web-Aktualnosci → Strony → Obrony doktorskie) jest pierwszą sekcją, z `p.wst` na pierwszym akapicie, tak jak w Konferencjach.
2. **Sekcje.**
   - `section#z-nadchodzace` z `h2` „Nadchodzące” (EN „Upcoming”):
     - obrony od najbliższej, bez podziału na lata;
     - gdy nie ma żadnej, sekcja zostaje z napisem „Nie zapowiedziano jeszcze kolejnych obron.” (EN „No upcoming defences announced.”), jak w Konferencjach.
   - `section#z-odbyte` z `h2` „Odbyte” (EN „Past”):
     - w każdym roku `h3 id="rok-RRRR"`: rok, `<span class="sr-only">, </span>` i `<small>` z liczbą;
     - liczba z odmianą: PL „1 obrona / 2 obrony / 5 obron / 22 obrony”, EN „1 defence / 2 defences”;
     - styl roku i liczby jak `h3`/`small` w Konferencjach;
     - w roku obrony od najnowszej.
3. **Spis „Na tej stronie”:** „Nadchodzące” (`#z-nadchodzace`), potem lata od najnowszego (`#rok-RRRR`). Lata wylicza się z danych, bez listy wpisanej na sztywno.
4. **Wiersze bez zmian w wyglądzie:** data, „dzień tygodnia godzina · miejsce”, kandydat Brygadą (cały wiersz klikalny), tytuł rozprawy, linia „Promotor:/Promotorzy:”.
   - Nagłówek wiersza to `h4`, bo stoi pod `h3` roku. Dodaj `'h4'` do `poziom` w `WierszWydarzenia.astro`. Inne użycia komponentu się nie zmieniają.
   - Pilnuj, żeby `.tresc` nie zmieniła wiersza: marginesy, `max-width` akapitów, krój i stopień `h4`. Wiersz ma wyglądać jak dziś na liście obron. Porównaj obliczone style.
5. **Usunąć:** panel „Pokaż” (filtr lat i pole szukania), skrypt filtra, napis „Brak obron spełniających…” i link „Archiwum starej strony”.
   - Klucze i18n, które przestaną być używane (np. `archiwumObron`), usuń tylko wtedy, gdy nic innego ich nie używa.
   - Nie usuwaj `ustawienia.archiwum`, jeśli korzysta z niego stopka albo inne miejsca.
6. **Stare adresy `?rok=RRRR`:** krótki skrypt na stronie.
   - Jeśli jest `?rok=RRRR` i istnieje `#rok-RRRR`, podmień adres na `…/obrony-doktorskie/#rok-RRRR` (`history.replaceState`, bez przeładowania) i przewiń do sekcji.
   - Nieznany rok: zostaje góra strony, a `?rok` znika z adresu.
   - Bez JS: cała strona jak zwykle.
7. **Komentarz na górze `ListaObron.astro`** opisuje nowy układ (zlecenie 57), tak jak w `ListaKonferencji.astro`.
8. **PL i EN** (`/en/obrony-doktorskie`), komputer i telefon, tryb jasny i ciemny. Na telefonie spis zwija się jak w Konferencjach.

**Wskazówka (nie przepis):** dane do sekcji możesz dodać w `daneListyObron()`, np. `lata: { rok, lista }[]` dla odbytych, jak w `daneListyKonferencji()`. Strona obrony (`Obrona.astro`), kalendarz, Aktualności i licznik „doktoraty w ostatnim roku” w Nauce zostają bez zmian.

## Odbiór lokalny
- Build z treściami z `main` (52 obrony, 0 nadchodzących). Do sprawdzenia Nadchodzących dopisz w lokalnej nakładce 2–4 testowe obrony z przyszłą datą, a na koniec przywróć nakładkę (`pobierz_tresci.py`).
- **Zrzuty** `/obrony-doktorskie` i `/en/obrony-doktorskie`:
  - 1920×1080, 1440×900, 1024 i 390 px, jasny i ciemny;
  - góra strony, Nadchodzące (pusta i z testowymi), przejście 2026/2025 i koniec listy (2013);
  - obok zrzut `/nauka/konferencje` w tych samych miejscach.
- **Spis:** klik w każdy rok przewija do `h3`, a znacznik spisu podąża za przewijaniem. Sprawdź myszą i klawiaturą.
- **`?rok=2015`** ląduje na `#rok-2015`, a `?rok=1999` na górze strony. W adresie nie zostaje `?rok`.
- **Wiersz:** obliczone style (`getComputedStyle`) daty, etykiety, kandydata, tytułu i promotora są równe tym sprzed zmiany, na komputerze i telefonie.
- **Kontrole:**
  - `astro check` bez nowych błędów;
  - `sprawdz_tresci.py` OK;
  - konsola czysta;
  - indeks wyszukiwarki obejmuje obrony jak dotąd;
  - `sitemap.xml` bez zmian poza datami.
- **Reszta `dist` bez zmian** poza `/obrony-doktorskie` (PL i EN), nazwami plików CSS/JS i indeksem wyszukiwarki. Inne użycia `WierszWydarzenia` (Kalendarz, wpis aktualności) mają ten sam HTML.
- **Stop:** raport i czekanie na „push”. Push dotyczy tylko Web-Core.

## Kryteria odbioru
- [ ] Na `/obrony-doktorskie` po prawej jest spis „Na tej stronie”: Nadchodzące, 2026…2013. Nie ma panelu „Pokaż” ani pola szukania.
- [ ] Odbyte są podzielone na lata (`h3#rok-RRRR` z liczbą obron w poprawnej odmianie PL i EN). Kolejność: lata od najnowszego, w roku od najnowszej obrony.
- [ ] Nadchodzące są na górze, od najbliższej. Bez obron sekcja pokazuje „Nie zapowiedziano jeszcze kolejnych obron.”
- [ ] Nie ma linku „Archiwum starej strony”.
- [ ] Wiersze wyglądają jak przed zmianą, łącznie z linią promotora.
- [ ] `?rok=RRRR` prowadzi do sekcji roku.
- [ ] Inne strony bez zmian. Repozytoria treści bez zmian.

## Do raportu
- Lista zmienionych plików i opis rozwiązania.
- Zrzuty i wyniki porównań (style wiersza, HTML innych użyć `WierszWydarzenia`).
- **Uwagi dla właściciela** (poza zakresem, bez zmian):
  - tytuł rozprawy jest zawsze oznaczany jako angielski (`lang="en"` w `WierszWydarzenia.astro` dla `rodzaj === 'obrona'`, w `obrona.ts` i w banerze strony obrony), a ok. 34 tytuły archiwalne są po polsku;
  - dopisek „(promotor pomocniczy)” / „(kopromotor)” w polu promotorów zostaje po polsku na stronach EN.
