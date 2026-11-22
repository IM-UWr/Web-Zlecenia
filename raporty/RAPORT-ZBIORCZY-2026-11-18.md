# Podsumowanie pracy samodzielnej (okno Web-Core), 18.11.2026 (stan 18:10; treści wypchnięte 16:48–17:17 i etap 3 o 18:03, przed wieczorem na Twoje polecenie)

Szczegóły w raportach: `RAPORT-ZLECENIE-31.md`, `RAPORT-ZLECENIE-39.md`, `RAPORT-ZLECENIE-33.md`, `RAPORT-ZLECENIE-40-0.md` (+ `RAPORT-ZLECENIE-40-0-pola.md`), lokalnie w Web-Core.

Kolejka okna: 31 → 39 → 33 → 40 (etap 0). Po wznowieniu o 11:00: fetch we wszystkich repozytoriach, nic nie było w połowie, zapisów redaktorów od nocy nie było.

## Co wypchnięte

| Zlecenie | Repozytorium | Commity na `main` | Podgląd po pushu |
|---|---|---|---|
| 31 | Web-Core | `6bf211e6..e3625870` (f339be95, d7e2275c, 2c2caa79, adc16bf4, 6851dc9b, b38f511b, e3625870) | zielony |
| 31 | 16 repozytoriów treści | Web-Aktualnosci `cc6a7b0..7f0bd01`, Web-Instytut `dcdebe8..3f9689a`, Web-Nauka `40ae8a0..498bc8d`, Web-Popularyzacja `45045d1..0f76f88`, Web-Pracownicy `d646aa7..5bcaf22`, Web-Studia `9a5d3e5..b76a2c6`, Web-Ustawienia `c02dc1c..3f6bca2`, 9× Web-Sem-* (zakresy w raporcie 31) | zielony |
| 39 | Web-Ustawienia | `3f6bca2..5ecbef7` (lista i formularz), `5ecbef7..f145d85` (podyplomowe w menu z listy) | zielony |
| 39 | Web-Core | `4511613b..0fa6731b` | zielony (run 44212184796) |
| 39 | Web-Studia | `b76a2c6..b2a7c09` (podyplomowe jako kierunek) | zielony (run 44212524231) |
| 33 | Web-Core | `b7192769..6e370e19` (c70fc69b część A, cd35ea53 migracja i kontrole, 6e370e19 część B z B3 i B4) | zielony (run 44294422959) |
| 33 | Web-Podglad | `f11ae37..e64e6a8` (`PODGLAD=1`, adnotacje błędów, `pipefail`) | zielony (run 44294700774); plakietka działa na żywo |
| 33 (decyzje 18.11) | Web-Core | `00fff0a8..fb54f3f5` (wiersz szkicu strony działu, żółty pasek pod menu, dymek tylko przy zmianie strony, link do formularza zakładu i „Warto wiedzieć”) | zielony (run 44304735795) |
| 39 (PDF) | Web-Core, Web-Podglad | `fb54f3f5..5772282f` (źródło HTML i skrypt PDF), Web-Podglad `e64e6a8..f2fe4af` (nowy PDF „Mapa CMS”), oba `[skip ci]` | bez przebudowy |
| 33 | 6 repozytoriów treści | 16:48–16:49, przed wieczorem na Twoje polecenie: Web-Aktualnosci `e4c9c62..46d7f90`, Web-Instytut `311faae..b2de465`, Web-Nauka `498bc8d..e85c60a`, Web-Popularyzacja `0f76f88..72e08cd`, Web-Pracownicy `5bcaf22..4015203`, Web-Studia `b2a7c09..f31a027`; kontrola po pushu OK w każdym | zielony (run 44340270000) |
| 40, etap 1 | Web-Core | `a0e32c28..0cda774c` (`maTresc()`, jawne `{#sukcesy}`, limity linii w jawnych Stronach, skrypty migracji i kontroli) | zielony (run 44309660047) |
| 40, etap 1 | Web-Instytut | `b2de465..88d8f50` (16:52; jawny Markdown 13 plików, formularze); kontrola po OK | zielony (run 44341742516) |
| 40, etap 2 | Web-Core | `0cda774c..91b5beb8` (strony konferencji z opisem i linki do nich, opis formularzy Nauki) | zielony (run 44318714781) |
| 40, etap 2 | Web-Nauka | `e85c60a..b01f1ec` (16:55; jawny Markdown 7 plików, formularze, szablony); kontrola po OK | zielony (run 44341742516) |
| 40, etap 4 | Web-Core | `23050dd2..641cf76e` (tylko skrypt formularzy; po rebase na zlecenie 44) | zielony (run 44319917747) |
| 40, etap 5 | Web-Core | `641cf76e..0b239768` (tylko skrypt formularzy: wzór dla 9 seminariów) | zielony (run 44321214003) |
| 40, etap 5 | 9× Web-Sem-* | 17:00–17:01 (tylko `.pages.yml`; zakresy w raporcie 40-5); kontrola po OK w każdym | zielony (run 44342490266) |
| 40, etap 4 | Web-Pracownicy | `4015203..ff4aec1` (16:57; jawny Markdown 1 pliku, formularze); kontrola po OK | zielony (run 44341742516) |
| 40, etap 6 | Web-Core | `057513dc..1ab56e50` (część 1/2: ikony Facebooka i YouTube w stopce; skrypty formularzy i kontroli; po rebase na zlecenie 43 z drugiego okna) | zielony (run 44324807301) |
| 40, etap 6 | Web-Ustawienia + Web-Core część 2/2 | Web-Ustawienia `f145d85..05080a9` (17:06; formularze, decyzje 1a, strony ze stopki w jawnym Markdownie), zaraz po nim Web-Core `d436ab69..5131ebf2` (17:08; zdjęcia i kadry nagłówków działów z CMS, po rebase na zlecenie 43 z drugiego okna); HTML przed/po 0 różnic | zielony (run 44343845368) |
| 40, etap 7 | Web-Core | `1ab56e50..3e81655e` (skrypt formularzy Studiów i Popularyzacji, `--pomin` dla pól w listach), `3e81655e..add78d45` (opisy hasła i opisu Stron); tylko skrypty | zielony (run 44326729373 dla `3e81655e`; `add78d45`: run 44327594862) |
| 40, etap 7 | Web-Core | `910853ea..b43b0aa8` (skrypt formularzy Popularyzacji z polem „Opublikowane” ze zlecenia 33; bez tego skrypt zatrzymałby się na nowym układzie pól) | zielony (run 44340270000) |
| 40, etap 7 | Web-Studia, Web-Popularyzacja | Web-Studia `f31a027..a8964db`, Web-Popularyzacja `72e08cd..0993e8e` (17:14; porządek pól w formularzach, w Studiach usunięte `etykieta_krotka` z 4 kierunków); HTML Studiów przed/po 0 różnic; kontrola po OK | zielony (run 44344905430) |
| 40, dokumentacja | Web-Core | `add78d45..910853ea` (`dok/jawny-markdown.md`, `dok/sciagawka-edytora.md`, źródło PDF „Mapa CMS”; tylko `dok/`) | bez przebudowy (`dok/**` pomijane przez przekaźnik Podglądu) |
| 40, dokumentacja | Web-Podglad | `6abb1bb..da76859` (17:17; PDF „Mapa CMS”, 2 strony, `[skip ci]`, na commicie drugiego okna) | bez przebudowy |
| 40, etap 3 | Web-Core | `5131ebf2..0951f7b4` (tylko skrypt formularzy Aktualności, Obron i Stron) | zielony (run 44353459620) |
| 40, etap 3 | Web-Aktualnosci | `422bb59..56caf58` (18:03, zaraz po zleceniu 44 z drugiego okna — Twoja decyzja „Przygotuj teraz”; jawny Markdown 3 Stron z `kariera.md`, formularze, szablony aktualności i obrony); HTML przed/po 0 różnic; kontrola po OK | zielony (run 44354449898) |
| 40, dokumentacja (etap 3) | Web-Core, Web-Podglad | `0951f7b4..02a2e8aa` (tylko `dok/`: bez wyjątku dla Stron Aktualności, Kariera, szablony aktualności i obrony); PDF `da76859..5b4e8f2` (`[skip ci]`, 2 strony) | bez przebudowy |

Każdy push w trybie samodzielnym spełniał trzy warunki:
- wszystkie kontrole ze zlecenia przeszły;
- kontrola redaktorów nie znalazła utraconej zmiany;
- tuż przed pushem był `fetch` i `rebase`, a po rebase powtórzona budowa.

Nie było force-pusha ani odrzuconego pusha. Strona na żywo jest zgodna z lokalną budową. Po każdej serii pushy sprawdziłem w logu Podglądu, że budowa wzięła właśnie wypchnięte SHA.

Treści (33 i 40) wypchnąłem o 16:48–17:17, a nie w oknie wieczornym, na Twoje polecenie („Dobra, zgadzam sie wrażamy teraz”). Kolejność: 33 → 40.1 → 40.2 → 40.4 → 40.5 → Web-Ustawienia → część 2 Web-Core → 40.7 → PDF. W chwili każdego pushu od bazy nie było żadnego zapisu redaktora.

Zlecenie 33: przed pushem Web-Core był rebase na zlecenia 32 (punkt 9) i 34 z drugiego okna. Po rebase: budowa identyczna z `origin/main` (poza znacznikami czasu), test plakietki 57 OK, `astro check` 0 błędów.

## Czego nie wypchnąłem i dlaczego
- Nic z zakolejkowanego nie czeka. Etap 3 (Web-Aktualnosci) poszedł o 18:03, zaraz po zleceniu 44 drugiego okna (szczegóły w `RAPORT-ZLECENIE-40-3.md`); dokumentacja i PDF bez wyjątku „Strony Aktualności w dawnym formacie”.

Dwie poprawki w trakcie serii (szczegóły w raporcie 40-7):
- skrypt formularzy Popularyzacji zakładał układ pól sprzed zlecenia 33; po dodaniu „Opublikowane” zatrzymałby się. Poprawka `b43b0aa8` przed pushem 40.7, sprawdzona na stanie po 33;
- pierwszy przebieg pushu 40.7 (17:10) zatrzymał się na kontroli redaktorów: bazą był commit sprzed 33, więc moją zmianę `.pages.yml` z 33 kontrola uznała za zapis redaktora. Nic nie zostało wypchnięte. Bazą jest teraz commit zlecenia 33 na `main`; drugi przebieg (17:11) przeszedł, a jego commity są takie same jak sprawdzone wcześniej.

## Decyzje przyjęte samodzielnie (zlecenie 39)
1. **Osobne wymagane pole „Nazwa w menu” (`nazwa_menu`, PL/EN)** na liście kierunków. Przyjąłem tę rekomendację, bo zlecenie ją przewiduje; dzięki temu kafelek „Nauczanie matematyki” zostaje, a menu pokazuje „Studia podyplomowe”.
2. **Liczby na `/studia` liczą tylko kierunki z listy.** Przyjąłem, bo zlecenie każe usunąć automat „spoza listy”.
3. **Studia podyplomowe nie liczą się do kierunków ani stopni.** Przyjąłem, bo inaczej liczba kierunków zmieniłaby się z 3 na 4.
4. **Kolejność pushy: lista w Web-Ustawienia przed Web-Core,** wbrew „najpierw Web-Core”. Przyjąłem, bo nowy kod ze starą listą dałby puste nazwy w menu, a stary kod z nową listą jest sprawdzony: 0 różnic.

## Decyzje przyjęte samodzielnie (zlecenie 33; uzasadnienia w raporcie 33)
5. Pole `opublikowany` pod parą tytuł / tytuł EN; istniejące klucze w plikach zostają na swoich miejscach.
6. Wynik z API w `localStorage` (wspólny dla kart) zamiast `sessionStorage`, bo odpowiedź 304 też zmniejsza limit API; `per_page=10` zamiast 5.
7. Stały żółty wiersz szkicu; link do CMS tylko z formularzy z przełącznikiem; strony prawne bez przełącznika.
8. Strona działu jako szkic zostaje przy fladze, bez tekstu z pliku (Twoja propozycja z nocnego pytania; do potwierdzenia).
9. Kolejność pushy w 33: kod i workflow w dzień, treści wieczorem (ostatecznie o 16:48, na Twoje polecenie).
10. Naprawiony brak `pipefail` w `podglad.yml` (zlecenie 41): nieudana budowa mogła opublikować niepełną stronę.

## Decyzje przyjęte samodzielnie (zlecenie 40, seria pushy 18.11)
11. Baza kontroli redaktorów w 40.7 = commit zlecenia 33 na `main` (nie stan sprzed 33). Przyjąłem, bo zapisy redaktorów sprzed tego commitu sprawdziła już kontrola zlecenia 33 (0 zapisów), a inaczej kontrola zatrzymywała się na moim własnym commicie.
12. PDF „Mapa CMS” wypchnięty na commit drugiego okna w Web-Podglad (`6abb1bb`), bez przebudowy (`[skip ci]`). Przyjąłem, bo zmienia tylko plik PDF.

## Pytania do Ciebie: odpowiedziane 18.11, ok. 13:05
- **39:** SIAD zostaje regułą; podyplomowe zostają na szablonie kierunku; poprawiony PDF robię ja.
- **33:** przełącznik w zakładach i „Warto wiedzieć”; wiersz szkicu strony działu na plakietce; żółty pasek pod menu; dymek tylko przy zmianie otwartej strony.
- **40:** rekomendacje 1a zatwierdzone; Facebook i YouTube jako ikony w stopce; hasło bez liczb ukryte; konferencje z opisem dostają własną stronę; Treść po polach identyfikujących wpis, EN pod PL; `maTresc()`, a potem opisy i szablony z raportu.

Szczegóły w sekcjach „Decyzje właściciela” raportów 33, 39 i 40-0.

## Pytania otwarte (zlecenie 40, etapy 1–7; szczegóły w raportach 40-1…40-7)
1. **40-1:** przywrócić limity linii (krótkie komórki tabel) na Stronach Studiów? Ukryć „Źródła (nie wyświetlają się)” w „Warto wiedzieć” i we Władzach, jak „Do uzupełnienia”?
2. **40-2:** zostaje poprawione brzmienie szablonu projektu? Dodać pole „Opis EN” konferencji?
3. **40-5, 40-6:** lista 1c (`do_uzupelnienia` w 8 seminariach; `partnerzy`, `baner.podpis_telefon(_en)` w Web-Ustawienia) — dziś ukryte, usunąć całkiem?
4. **40-6:** usunąć nieużywane pliki zdjęć po usuniętych polach (`kampus-zmierzch-1200.jpg`, `instytut-telefon.jpg`)? Kadr nagłówka z CMS także na podstronach (zmieni wygląd podstron Instytutu i Nauki)?
5. **40-7:** nadtytuł kierunku (decyzja „podłączyć `podtytul_en`”, ale nagłówek nie pokazuje nadtytułu w żadnym języku): pokazać w obu językach czy zostawić? Hasło na 9 Stronach Studiów bez liczb: pokazywać czy zostawić?

## Co sprawdzić następnego dnia
- **Zapisy redaktorów z 24 godzin po pushu (31), do 19.11, ok. 01:25.** W 16 repozytoriach treści sprawdzić, czy nikt nie usunął:
  - pola `termin` ani `pozycja`;
  - przemianowanych wpisów z 16.11.

  Sprawdzić też, czy nikt nie przywrócił `wydarzenie_*`.
- **Zapisy redaktorów z 24 godzin po pushu (39), do 19.11, ok. 02:00:**
  - w Web-Studia nie powstał z powrotem `src/content/strony/studia/podyplomowe.md` (stary formularz „Strony” otwarty przed pushem);
  - w Web-Ustawienia lista kierunków ma nowe pola (`nazwa_menu`, jawne `w_menu` i `na_stronie_glownej`).
- **Test w CMS (31):** termin wydarzenia („Add an item”), czerwony komunikat przy pozycji galerii lub załącznika bez pliku, nazwa pliku nowej aktualności z tytułu.
- **Test w CMS (39):**
  - Web-Ustawienia → Strona główna i kontakt → „Kierunki w menu „Studia” i kafelki na stronie głównej”: otwarcie i zapis bez zmian (pusty diff); nowa pozycja wymaga adresu, nazwy i opisu w menu oraz nazwy na kafelku;
  - Web-Studia → Kierunki → „Studia podyplomowe”: otwarcie i zapis bez zmian.
- **33, po pushu treści (16:49), do 19.11, ok. 16:50:**
  - zapisy redaktorów z 24 godzin w 6 repozytoriach: czy żaden formularz otwarty przed pushem nie usunął `opublikowany` ani nie przywrócił „Uwzględniaj w zestawieniach” (Web-Studia);
  - test w CMS: nowa Strona startuje z zaznaczonym „Opublikowane”; po odznaczeniu na Podglądzie widać szkic z żółtym wierszem i działającym linkiem do formularza;
  - pierwsza nieudana budowa: czy czerwony pasek pokazuje komunikat z linkiem „Popraw w CMS”.
- **40, etap 1, po pushu treści Web-Instytut (16:52), do 19.11, ok. 16:55:**
  - zapisy redaktorów z 24 godzin: czy żaden formularz otwarty przed pushem nie usunął `format_tresci` ani `{#id}`;
  - test w CMS: Strona i strona działu (otwarcie, zapis bez zmian, drobna zmiana); nowy zakład i nowa pozycja „Warto wiedzieć” startują z szablonem Treści.
- **40, etap 2, po pushu treści Web-Nauka (16:55), do 19.11, ok. 16:55:**
  - zapisy redaktorów z 24 godzin: jak w etapie 1 (`format_tresci`, `{#id}`, `{#czasopisma}`);
  - test w CMS: konferencja i projekt (otwarcie istniejącego bez opisu wstawi szablon; zapis z samym szablonem nie tworzy strony konferencji); nowa konferencja i nowy projekt z szablonem;
  - Podgląd: strona konferencji z opisem, np. `/nauka/konferencje/2018-winter-school-in-abstract-analysis-2018`, i link do niej z listy.
- **40, etap 4, po pushu Web-Pracownicy (16:57), do 19.11, ok. 17:00:**
  - zapisy redaktorów z 24 godzin: czy nikt nie usunął `format_tresci`;
  - test w CMS: Strony → Pracownicy i dowolna osoba (otwarcie, zapis bez zmian: pusty diff).
- **40, etap 5, po pushu 9 seminariów (17:01), do 19.11, ok. 17:00:**
  - zapisy redaktorów z 24 godzin;
  - test w CMS: opis seminarium (zapis bez zmian); istniejący referat bez streszczenia (otwarcie wstawi szablon, zapis z samym szablonem nie pokazuje ramki streszczenia — potwierdzić na Podglądzie); nowy referat z szablonem.
- **40, etap 6, po pushu Web-Ustawienia (17:06), do 19.11, ok. 17:10:**
  - zapisy redaktorów z 24 godzin (formularze Ustawień ma tylko właściciel; strony ze stopki: `format_tresci`, `{#id}`);
  - test w CMS: Strona główna i kontakt (widać Nagłówki działów, Facebook, YouTube; zapis bez zmian); Deklaracja/Prywatność/O stronie (zapis bez zmian usuwa tylko linię `opublikowany: true` — bez wpływu na stronę);
  - Podgląd: ikony w stopce (PL, EN, telefon), nagłówki działów bez zmian.
- **40, etap 3, po pushu Web-Aktualnosci (18:03), do 19.11, ok. 18:05:**
  - zapisy redaktorów z 24 godzin: czy formularz otwarty przed pushem nie usunął `format_tresci` ze Stron Aktualności, Kariery i Obron;
  - test w CMS: Aktualności (zapis bez zmian; nowa aktualność z szablonem), Obrony (otwarcie istniejącej obrony wstawi szablon, zaproszenie zostaje), Strony (zapis bez zmian).
- **40, etap 7, po pushu Web-Studia i Web-Popularyzacja (17:14), do 19.11, ok. 17:15:**
  - zapisy redaktorów z 24 godzin: czy formularz Kierunków otwarty przed pushem nie przywrócił `etykieta_krotka`;
  - test w CMS: Studia → Kierunki i Popularyzacja → Strony (otwarcie, pola EN pod polskimi, zapis bez zmian: pusty diff).
- **Wspólne klony `tresci`:**
  - przed `pull` w `tresci/Web-Aktualnosci` porzucić lokalny commit `b7a307a` (opis w raporcie 31);
  - po dzisiejszych pushach wszystkie klony `tresci` są w tyle za `main`, potrzebny zwykły `pull` (Web-Aktualnosci: najpierw porzucić `b7a307a`).

## Stan lokalny
- **Web-Core:**
  - gałąź `praca/33-opublikowane` = `origin/main` (`02a2e8aa`); poza commitami nieśledzone tylko `.claude/`, `Claude outputs/`, `skrypty/test-edytora/package-lock.json` (nie moje);
  - nakładka `src/content` i `src/data` = treści z `main` po zleceniu 39 (wpisy testowe szkiców przywrócone);
  - lokalny `.tresci/pochodzenie.json` z testów plakietki (ignorowany przez git).
- **Kopia robocza treści 40.1:** `tresci-z40\Web-Instytut` (gałąź `praca/40-instytut`, commit `88d8f50` na commicie zlecenia 33).
- **Kopia robocza treści 40.2:** `tresci-z40\Web-Nauka` (gałąź `praca/40-nauka`, commit `b01f1ec` na commicie zlecenia 33).
- **Kopie robocze treści 40.5:** `tresci-z40\Web-Sem-*` (gałąź `praca/40-seminaria`, po jednym commicie na świeżym `main`).
- **Kopia robocza treści 40.6:** `tresci-z40\Web-Ustawienia` (gałąź `praca/40-ustawienia`, commit `05080a9` na `f145d85`); łatka części 2 Web-Core: `scratchpad/naglowek40.patch`. Pomocniczy worktree `scratchpad/ust-baza` (stan bazy, do kontroli ujemnej).
- **Kopie robocze treści 40.7:** `tresci-z40\Web-Studia` i `tresci-z40\Web-Popularyzacja`, gałąź `praca/40-etap7-1710` (`a8964db`, `0993e8e` = `main`; formularze nałożone od nowa na `main` po 33). Stare gałęzie `praca/40-studia` i `praca/40-popularyzacja` zostały nietknięte.
- **Kopia robocza treści 40.4:** `tresci-z40\Web-Pracownicy` (gałąź `praca/40-pracownicy`, commit `ff4aec1` na commicie zlecenia 33).
- **Kopie robocze treści 33:** `tresci-z33\*` (gałąź `praca/33-opublikowane`, po jednym commicie migracji); Web-Podglad: `podglad-z33\Web-Podglad` = `origin/main`.
- **Kopie robocze treści:**
  - `tresci-z31\*` (gałąź `praca/31-galeria-daty-nazwy`) i `tresci-z39\{Web-Ustawienia,Web-Studia}` (gałąź `praca/39-kierunki`): lokalne, niewypchnięte, równe `main` z chwili pushu;
  - folderów nie usuwałem.
- **Kopia robocza treści 40.3:** `tresci-z40\Web-Aktualnosci` (worktree `tresci/Web-Aktualnosci`), gałąź `praca/40-aktualnosci-1801` = `main` (`56caf58`); pierwszy commit `f91eac2` na gałęzi `praca/40-aktualnosci` (sprzed 44) nietknięty.
- Wszystkie kopie robocze 33 i 40 (etapy 1–7) są równe `main` z chwili pushu; nic lokalnego nie czeka.
- Zaplanowanych zadań wieczornych w tej sesji już nie ma (push zrobiony wcześniej), więc nic nie uruchomi się drugi raz.
- Raporty i zrzuty są tylko lokalnie (ignorowane przez `.gitignore`).
