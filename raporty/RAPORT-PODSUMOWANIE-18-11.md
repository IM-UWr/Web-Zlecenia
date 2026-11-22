# Podsumowanie pracy samodzielnej — okno Web-Core-B (18.11.2026, do 02:06)

Kolejka okna: 38 → 41 → 32 → 34 → 35 → 37 → 36. Zatrzymane na prośbę właściciela w trakcie zlecenia 32. Szczegóły są w `RAPORT-ZLECENIE-38.md`, `RAPORT-ZLECENIE-41.md` i `RAPORT-ZLECENIE-32.md`.

## Wypchnięte (bez force, przed każdym pushem `fetch` i `rebase`)
| Repozytorium | Commit | Zlecenie | Treść |
|---|---|---|---|
| Web-Core | `74781d1` | 38 | skrypt planu i archiwizacji gałęzi |
| Web-Core | `222d5e4` | 38 | usunięte workflowy gałęzi roboczych, archiwa jako znaczniki; na tym commicie stoi znacznik `archiwum/pierwsza-wersja` |
| Web-Core | `6bf211e` | 38 | `main` bez raportów, zrzutów i nieużywanych plików |
| Web-Aktualnosci | `cc6a7b0` | naprawa Podglądu | usunięta pusta pozycja załącznika w `2026-11-16-.md` |
| Web-Podglad | `51c4b95`, `f11ae37` | 41 | szybsza budowa Podglądu (pamięć npm i zdjęć, równoległe klony, przerywanie starej budowy); `actions/cache` v5 |
| Web-Core | `4511613b` | 41 | push kodu na `main` przebudowuje Podgląd |
| Web-Instytut | `0855f0d`, `7ed4d89`, `d720e38`, `311faae` | 41 | test serii zapisów, różnica netto zerowa |
| wszystkie repozytoria | znaczniki `archiwum/…` | 38 | archiwum usuniętych gałęzi (92) |

Podgląd po ostatnim pushu (`4511613b`) był zielony.

## Niewypchnięte i dlaczego
- **Zlecenie 32:** lokalny commit `b2244d3e` na `praca/32-menu` w `Web-Core-B`. Kod jest gotowy i budowa przechodzi, ale odbiór jest niezrobiony (zrzuty „po”, telefon, `astro check`). Następne kroki są w `RAPORT-ZLECENIE-32.md`.
- **Zlecenia 34, 35, 37, 36:** nierozpoczęte.

## Decyzje przyjęte samodzielnie
- **38:**
  - przyjąłem `archiwum/pierwsza-wersja` jako znacznik, nie gałąź, bo kryterium mówi „tylko `main`”;
  - przyjąłem, że `skrypty/migracja/` zostaje na razie na `main`, bo druga sesja używa z niego kontroli redaktorów (zlecenia 39, 33, 40).
- **41:** przyjąłem usunięcie TESTU telefonu z Web-Podglad, bo to wartość domyślna zlecenia.
- **32:** decyzje są w `RAPORT-ZLECENIE-32.md`:
  - limit szerokości 560 px;
  - pełna skala wielkości;
  - Tab za ostatnią pozycją zamyka listę;
  - orzeł przygasa do 75% przy najechaniu.

## Pytania do właściciela
1. **(38)** `skrypty/migracja/`: usunąć cały folder po zleceniu 40, czy przenieść kontrolę redaktorów do `skrypty/` jako narzędzie stałe?
2. **(38)** Pliki „poza grafem, ale zostają”: `markdown-jawne-test.yml` w Web-Podglad, `.github/qa/`, `skrypty/szerokosci/`, `dok/latki/`, `dok/en/`. Zostawić czy usunąć?
3. **(41)** Drugi klucz sortowania (konferencje z tą samą datą, `sitemap.xml`), żeby wynik budowy był zawsze w tej samej kolejności?
4. **(41)** Podnieść `configure-pages`, `upload-pages-artifact` i `deploy-pages` (ostrzeżenia o Node 20) osobnym małym zleceniem?
5. **(32)** Krzyżyk w liście czy hamburger zmieniający się w ×? Na razie zostaje krzyżyk.

## Do sprawdzenia następnego dnia
- **Zapisy redaktorów w Pages CMS po pushu:**
  - przebieg Podglądu powinien trwać ok. 1–1,5 min;
  - przy kilku zapisach z rzędu część przebiegów kończy się jako `cancelled` i tak ma być;
  - zmiana widoczna na Podglądzie.
- **Przebiegi Podglądu z `cron`** (co godzinę) przechodzą.
- **Test w CMS:** jeden zapis w dowolnej kolekcji i sprawdzenie, że Podgląd go pokazuje.

## Lokalne pozostałości (niczego nie kasowałem)
- **`tresci-B`:**
  - `z38-dist-przed` i `z38-dist-po` (po ok. 255 MB) oraz logi `z38-*`;
  - `z32-przed` (budowa „przed” do zlecenia 32; potrzebna do dokończenia odbioru).
- **Gałęzie robocze, niewypchnięte:**
  - `praca/41-*` w `tresci-B/Web-Podglad` i `tresci-B/Web-Instytut`; ich zmiany są na `main`;
  - `praca/32-menu` w `Web-Core-B`.
- **Zrzuty i skrypt zlecenia 32:** `raport-zrzuty/z32-przed/` i `raport-zrzuty/z32-skrypt/` (git-ignored).


## Wznowienie (18.11.2026, ok. 10:15 czasu lokalnego)

### Stan repozytoriów
- `git fetch` w `Web-Core-B` i we wszystkich 23 klonach w `tresci-B`.
- **Nic w połowie:** żadnego rebase, merge ani cherry-pick w toku, wszystkie drzewa czyste.
- **Web-Core:** `origin/main` przesunął się o zlecenie 39 drugiej sesji (`0fa6731b`). `praca/32-menu` przeszła `rebase` bez konfliktów.
- **Klony treści:** przewinięte do `origin/main` (tylko fast-forward):
  - Web-Aktualnosci +3 (zapisy redaktora);
  - Web-Studia +1 i Web-Ustawienia +2 (zlecenie 39 drugiej sesji).
- **Nakładka treści w `Web-Core-B`:** odświeżona przez `pobierz_tresci.py --lokalnie ../tresci-B`.

### Ochrona zmian redaktorów (przegląd po nocy)
- **Zapisy redaktorów od 16.11 we wszystkich repozytoriach treści:** Web-Aktualnosci 32, Web-Instytut 6, Web-Pracownicy 2.
- **W nocy (po 02:10):** jeden redaktor (pborod) dodał o 08:23–08:28 wpis `2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu.md` ze zdjęciem.
  - Wpis jest w nowym formacie (`termin`), bez pól `wydarzenie_*` i bez pustych pozycji list.
  - Później nikt go nie zmieniał.
  - Podgląd po jego zapisach zielony (44266561212, 44267389555).
- **Pliki redaktorów, które ktoś później zmienił:** sprawdziłem pole po polu ostatnią wersję redaktora i obecny `main` (skrypt na js-yaml, bo w systemie nie ma PyYAML). Różnice wynikają tylko z celowych zmian:
  - migracja `wydarzenie_*` → `termin` (zlecenie 31);
  - decyzje właściciela z 31: nazwy plików trzech wpisów z 16.11 oraz „Medale” jako sukces, bez pól wydarzenia;
  - mój commit `cc6a7b0`: usunięta tylko pusta pozycja `{}` w `zalaczniki`. Pozostałe załączniki są identyczne z wersją redaktora.
- **Wpisy `2026-11-17-*.md`:** usunęli je sami redaktorzy w CMS, nic nie zginęło przez nasze pushe.
- **Po moim pushu z 17/18.11:** w żadnym repozytorium treści nie ma pustych pozycji `- {}` ani starych pól `wydarzenie_*`.
- **Strona testowa zlecenia 41** (`test-zlecenie-41`) nie istnieje na `main` Web-Instytut.
- **Wniosek:** żadna zmiana redaktora nie została utracona.
- **Do obejrzenia:** z `cron` Podglądu był w nocy tylko jeden przebieg (04:33). GitHub czasem opuszcza przebiegi z harmonogramu. Zapisy redaktorów i tak uruchamiają budowę same.

## Druga część dnia: 10:15–16:20 (zlecenia 32, 34, 35, 37, 36, 44, 43)

Kolejka okna, w tej kolejności: 32 → 34 → 35 → 37 → 36 → 44 → 43. Wszystkie zlecenia przerobione. Szczegóły w `RAPORT-ZLECENIE-NN.md`. Wpisy w `.przekazanie/dziennik.md` są dopisane; nowe pola CMS zlecenia 44 są w `.przekazanie/pola-do-cms.md`.

### Wypchnięte

Wszystkie pushe zwykłe, bez force. Przed każdym: `fetch`, `rebase` na `origin/main`, ponowna budowa, `astro check`, `npm run test:jawne`. Pięć razy na `main` były już commity drugiej sesji (zlecenia 33, 39, 40): jeden konflikt (35, oczywisty, połączone importy), poza tym rebase czysty.

| Repozytorium | Commit | Zlecenie | Treść | Podgląd |
|---|---|---|---|---|
| Web-Core | `c2c193e0` | 32 | menu na komputerze jako zwarta lista pod hamburgerem; orzeł UWr prowadzi do UWr | [44285963010](https://github.com/IM-UWr/Web-Podglad/actions/runs/44285963010) ✓ |
| Web-Core | `cbca5051` | 32, punkt 9 | „Aktualności” i „Rekrutacja ↗” mają wysokość zwiniętego wiersza | [44290545777](https://github.com/IM-UWr/Web-Podglad/actions/runs/44290545777) ✓ |
| Web-Core | `b7192769` | 34 | tryb ciemny „Granat z krawędzią” | [44293228901](https://github.com/IM-UWr/Web-Podglad/actions/runs/44293228901) ✓ |
| Web-Core | `70e9ab73` | 35 | Szybki dostęp bez dziur i „Ostatnio” | [44298270197](https://github.com/IM-UWr/Web-Podglad/actions/runs/44298270197) ✓ |
| Web-Core | `00fff0a8` | 37 | wpis w Aktualnościach z banerem swojego działu | [44302708750](https://github.com/IM-UWr/Web-Podglad/actions/runs/44302708750) ✓ |
| Web-Core | `a0e32c28` | 36 | okładka na dotyku (wariant A) | [44308419922](https://github.com/IM-UWr/Web-Podglad/actions/runs/44308419922) ✓ |
| Web-Core | `23050dd2` | 44 | „Kariera” jako podstrona Aktualności, termin zgłoszeń | [44319663976](https://github.com/IM-UWr/Web-Podglad/actions/runs/44319663976) ✓ |
| Web-Core | `ee446fee`, `057513dc` | 43, etapy 1 i 3 | plan zajęć na cały rok akademicki (zmiana 1.08); dopisek „(inna strona)” po nazwie Wydziału | [44323847367](https://github.com/IM-UWr/Web-Podglad/actions/runs/44323847367) ✓ |

### Niewypchnięte i dlaczego

- **Zlecenie 44, Web-Aktualnosci:**
  - commit `e2b51a5` (`.pages.yml` z grupą „Termin zgłoszeń” i opisem „Rodzaj”, nowy `src/content/strony/kariera.md`) na lokalnej gałęzi `praca/44-kariera` w `tresci-B/Web-Aktualnosci`;
  - zlecenie każe pushować „wieczorem albo po wiadomości właściciela do redaktorów”;
  - **push zaplanowany w tej sesji na 20:07**, z kontrolami: fetch, nałożenie na ewentualny nowy `.pages.yml` zlecenia 40, `sprawdz_pola_cms.py`, symulacja formularza, Podgląd;
  - jeśli sesja wcześniej się skończy, kroki są w `RAPORT-ZLECENIE-44.md` („Do sprawdzenia jutro”);
  - okno 1 czeka z etapem 3 zlecenia 40 (Web-Aktualnosci) na ten push.
  - **Aktualizacja 17:35: wypchnięte o 16:31 UTC na polecenie użytkownika.**
    - Po rebase na `46d7f90` (zlecenie 33) i z `opublikowany: true` w `kariera.md`: `46d7f90..422bb59`.
    - Kontrole przed pushem: `sprawdz_pola_cms` 0 problemów; symulacja formularza 0 problemów, zapis bez zmian 726/0.
    - Podgląd 44348385389 zielony (`Web-Aktualnosci: main @ 422bb59`); na żywo Kariera z tekstami z `kariera.md`, ramka „(11)”.
- **Zlecenie 43, etap 2** (podtrzymanie harmonogramów GitHub): niewdrożony, czeka na decyzję. *Aktualizacja: wdrożony o 17:00 po decyzji właściciela, patrz sekcja na końcu.* Dokumentacja GitHub nie potwierdza, że wywołanie `enable` zeruje licznik 60 dni, a jedna relacja mówi, że nie pomogło. Zlecenie każe wtedy opisać warianty i czekać. Warianty A–E z rekomendacją A + B są w `RAPORT-ZLECENIE-43.md`.

### Decyzje przyjęte samodzielnie (wybór)

- **44:**
  - hasło Kariery „Praca, staże, stypendia”;
  - „Zakończone” przygaszone kolorem, nie przezroczystością;
  - dopisek terminu także w wierszach list;
  - wpis o nazwie `kariera.md` jest pomijany (adres zajęty przez stronę).
- **43:**
  - semestr nieznany w USOS: bez pobierania, zwykła informacja w logu;
  - poprawiona kolejność dopisku w linku Wydziału na okładce (wymóg etapu 3, którego nie objęło zlecenie 32).
- **32–36:** w raportach zleceń (sekcje „Decyzje”).

### Pytania do właściciela (nowe w drugiej części)

1. **(43)** Etap 2: który wariant podtrzymania harmonogramów? Rekomendacja: A + B (`enable` co tydzień i wzajemna kontrola stanu z czerwonym przebiegiem), bez sekretów i commitów.
2. **(43)** Kolejność dopisku „(inna strona)” w linku Wydziału na okładce telefonu (`Naglowek.astro`) poprawić tak jak na komputerze?
3. **(43)** Przy awarii USOS API brać daty semestrów z poprzedniego pliku (dziś strona otwiera wtedy pierwszą zakładkę)?
4. **(44)** Plik `kariera.md` zostaje (adres `/aktualnosci/kariera`)? Hasło? Nawigacja „nowszy/starszy” we wpisach ofert tylko po ofertach? Wiadomość do redaktorów przed pushem Web-Aktualnosci?
5. **(36)**
   - czas dorysowania 0,3 s i barwienie zostają?
   - powiększyć pola dotyku poniżej 44 px?
   - tablet w pionie?
   - pełna nazwa SIAD na dotyku?
   - efekty najechania tylko przy `hover: hover`?
6. **(37)**
   - na wpisie podświetlać dział wpisu czy „Aktualności”?
   - wyjątek na telefonie?
   - znak i ciekawostka patrona na wpisach?
7. **(35)**
   - `dok/estetyka.md`: odtworzyć?
   - pas 101–115 px po „Zobacz więcej”?
   - skrócić tytuł „Medale Uniwersytetu…”?
8. **(34)** Który pasek przycisków był w pytaniu zlecenia?
9. **(32)** Krzyżyk w liście zostaje (bez zmiany na ×)?

### Do sprawdzenia jutro (19.11)

- **Web-Aktualnosci po pushu** (był o 16:31 UTC, nie o 20:07):
  - przegląd zapisów redaktorów z 24 godzin (czy nikt starym formularzem nie zgubił grupy `zgloszenia`);
  - ✓ strona Kariera z tekstami z `kariera.md` (18.11, 16:35 UTC: Podgląd z `422bb59`; teksty takie same jak domyślne);
  - pierwsza oferta z terminem.
- **Plan zajęć:**
  - przebiegi `plan-zajec.yml` z nowym skryptem (pierwszy 18.11 o 15:47 UTC) zielone, „Bez zmian w USOS”;
  - para 2026/27-Z i 2026/27-L w podsumowaniu przebiegu.
  - **Kontrola 18.11, 16:13 UTC:**
    - częściowo ✓: ręczny przebieg 44341565229 z nowym skryptem zielony; 2026/27-Z i 2026/27-L „bez zmian”, „Plik bez zmian”, bez błędów; wynik taki sam jak ze starym skryptem o 09:14;
    - ✓ przebieg z harmonogramu (kontrola 20:03): przebieg [44368917211](https://github.com/IM-UWr/Web-Core/actions/runs/44368917211), 18:22 UTC, kod `02a2e8aa` z nowym skryptem; zielony. 2026/27-Z (88/300) i 2026/27-L (100/304) „bez zmian”, „Plik bez zmian”, „Bez zmian w USOS — nic do zapisania”, bez błędów i ostrzeżeń. Etap 1 zlecenia 43 sprawdzony do końca.
- **Podgląd na żywo:**
  - link Wydziału na okładce ma dopisek po nazwie;
  - ✓ Kariera z ramką „(11)” na liście Aktualności (18.11, 16:35 UTC);
  - tryb ciemny, okładka na dotyku.
- **Zlecenie 40, etap 3 (okno 1):** nałożony na `.pages.yml` Web-Aktualnosci z grupą `zgloszenia`.

### Lokalne pozostałości (niczego nie kasowałem)

- **`tresci-B`:**
  - budowy zleceń: `z34-*`, `z35-*`, `z36-*`, `z37-*`, `z44-*` (w tym kopia testowa z terminami `z44-test`), `z43-po`, `z43-po2`, `z43-brakL`;
  - logi `z3*-*.log`, `z4*-*.log`.
- **Gałęzie robocze, niewypchnięte:**
  - w `Web-Core-B`: `praca/32-menu`, `praca/32-punkt9`, `praca/34-ciemny`, `praca/35-szybki`, `praca/36-dotyk-okladka`, `praca/37-baner-wpisu`, `praca/44-kariera`, `praca/43-plan-zajec` (ich zmiany są na `main`);
  - `praca/44-kariera` w `tresci-B/Web-Aktualnosci` (wypchnięta jako `422bb59`, równa `main`).
- **Zrzuty i skrypty:** `raport-zrzuty/z3*`, `z4*` (git-ignored).
- **Serwery podglądu:** wyłączone na koniec pracy.

## Zlecenie 43, etap 2 po decyzji właściciela (16:50–17:05)

- **Wypchnięte, zwykły push:**
  - Web-Podglad `f2fe4af0..6abb1bb6`: nowy `podtrzymanie.yml`, komentarz w `podglad.yml`;
  - Web-Core `b43b0aa8..d436ab69`: krok „Harmonogramy” w przekaźniku, zadanie „podtrzymanie” w `plan-zajec.yml`, README.
- **Działa:**
  - przekaźnik przy każdym zapisie w CMS i pushu włącza z powrotem `plan-zajec.yml` i `podglad.yml`, jeśli GitHub je wyłączył (ostrzeżenie w logu);
  - co tydzień (poniedziałek 04:13 i 04:43 UTC) `enable` i wzajemna kontrola; stan inny niż „active” daje czerwony przebieg z opisem.
- **Na GitHubie zielone:** przekaźnik 44341507520 i 44341705470, `plan-zajec.yml` 44341565229, `podtrzymanie.yml` 44341558338, Podgląd 44341742516.
- **Zostaje kliknięcie właściciela:** Actions: Read and write dla aplikacji „IM-UWr strona powiadomienia”. Do tego czasu przekaźnik zostawia ostrzeżenie HTTP 403 i nie włączyłby `podglad.yml`; `plan-zajec.yml` włącza już teraz. Instrukcja: RAPORT-ZLECENIE-43.md i README Web-Core.
- **Decyzje:**
  - workflowów wyłączonych ręcznie nic nie włącza;
  - w Web-Podglad osobny plik, bo plakietka stanu budowy czyta przebiegi `podglad.yml`.
- **Pytanie:** czy wyłączone ręcznie też włączać automatycznie?
- **Do sprawdzenia:** przekaźnik po kliknięciu (204 zamiast ostrzeżenia); 23.11 pierwsze cotygodniowe przebiegi.
- **Lokalne pozostałości:**
  - gałęzie `praca/43-harmonogramy` (Web-Core-B) i `praca/43-podtrzymanie` (tresci-B/Web-Podglad), obie równe `main`;
  - `raport-zrzuty/z43e2-*`.
