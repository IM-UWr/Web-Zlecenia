# Zlecenie 59 (22.11.2026): uzupełnienie i poprawki wersji angielskiej — nałożenie gotowych łatek

**Skąd to zlecenie.** Właściciel 22.11, 13:41: „Puść 4 agentów, niech sprawdzą wersję angielską strony i znajdą, czy wszystkie miejsca mają odpowiedni angielski tekst. Jeśli nie, to niech zredagują angielski tekst na podstawie polskiego”. Czterech agentów rozmowy w claude.ai sprawdziło w chmurze wszystkie repozytoria treści i kod (stan `main` z 22.11, ok. 13:45) oraz zbudowaną stronę `/en`. Wynik to gotowe łatki. Rozmowa nałożyła je razem na czyste klony, zbudowała całą stronę (953 strony, tryb Podglądu) i sprawdziła wynik (punkt „Sprawdzone w chmurze” niżej).

**Twoje zadanie:** nałożyć łatki na świeży `main` (z ochroną zmian redaktorów), sprawdzić budowę i strony, zrobić drobny punkt 4 i przygotować do pushu. Tłumaczeń nie przepisuj od nowa. Jeśli coś w tłumaczeniu jest ewidentnie błędne, popraw i zapisz w raporcie.

## Załączniki (`.przekazanie\zlecenia\59-zalaczniki\`)
- `Web-Core.patch` (16 plików kodu i `dok/en/TLUMACZENIA.md`), `Web-Instytut.patch` (47 plików: wszystkie sylwetki, nagrody i historie „Warto wiedzieć” z pełnym EN, strony Instytutu, zakłady, `.pages.yml`), `Web-Studia.patch` (24), `Web-Popularyzacja.patch` (5), `Web-Ustawienia.patch` (5), `Web-Aktualnosci.patch` (26, w tym `.pages.yml`), `Web-Nauka.patch` (20, w tym opisy EN 17 konferencji i `.pages.yml`).
- `bazy-sha.txt`: commity, na które łatki nakładają się czysto (Web-Core `edbd51d`, Web-Instytut `d14657e`, Web-Studia `608f1dc`, Web-Popularyzacja `faf8ca1`, Web-Ustawienia `fd49210`, Web-Aktualnosci `5ed05d3`, Web-Nauka `2db3479`).
- `raport-agent-1.md` … `raport-agent-4.md`: co zmieniono, w którym pliku i dlaczego; decyzje do podjęcia; zauważone błędy w polskich tekstach (polskich tekstów agenci nie zmieniali).
- `KONTEKST.md`: zasady tłumaczenia, według których pracowali agenci (decyzje D1–D20, słownik).

## Zasady pracy
- Jak w `zasady.md`: lokalna gałąź robocza (`praca/59-wersja-angielska`) w każdym zmienianym repozytorium, push według zasad (po „push” właściciela, chyba że właściciel powie inaczej), z kontrolą zapisów redaktorów przed pushem i po nim, jak w zleceniu 42.
- Raport `RAPORT-ZLECENIE-59.md`, wpis w `dziennik.md`. Bez subagentów.
- **Kolejność:** po zleceniach 57 i 58 albo przed nimi, ale nie równolegle. Łatka Web-Core nie dotyka plików z 57 (`ListaObron.astro`, `listaObron.ts`, `ListaKonferencji.astro`) ani z 58 (pasek), więc konfliktów nie powinno być.
- `pobierz_tresci.py` uruchom dopiero po nałożeniu i lokalnym commicie łatek w repozytoriach treści, z `--zrodlo Repo=<katalog klonu>` dla każdego z 6 repozytoriów treści (albo pracuj na nakładce i przenieś zmiany do klonów; ważne, żeby lokalne zmiany nie zostały nadpisane).

## Docelowo
1. **Web-Core najpierw** (nowe pola w schemacie: `galeria[].podpis_en` w aktualnościach, `tresc_en` w konferencjach, `obraz_zrodlo_en` w sylwetkach WW). `git apply --3way` na świeżym `main`. Przy błędach końców linii (CRLF w drzewie roboczym) też `--3way`, bo działa na blobach z indeksu.
2. **Repozytoria treści** (Web-Instytut, Web-Studia, Web-Popularyzacja, Web-Ustawienia, Web-Aktualnosci, Web-Nauka): `git pull` → `git apply --3way <łatka>`.
   - Jeśli redaktor zmienił plik od bazy (`bazy-sha.txt`), zachowaj jego zmiany w polskim tekście i polach, a z łatki weź tylko pola `_en`/`tresc_en`. Wypisz takie pliki w raporcie: jeśli zmienił się polski tekst, angielski może wymagać uzupełnienia.
   - Łatki zmieniają tylko pola EN (i `.pages.yml` w trzech repozytoriach). Nigdzie nie zmieniają polskiego tekstu. Sprawdź to: `git diff` bez zmian w body plików `.md` i polach bez `_en` (wyjątek: przeformatowanie YAML zapisanego przez CMS jako `>-` w kilku aktualnościach — sama wartość bez zmian).
3. **Nowe pola w CMS** (są w łatkach `.pages.yml`; dopisz je też do `.przekazanie\pola-do-cms.md`):
   - Web-Aktualnosci, galeria: „Podpis EN” (`podpis_en`);
   - Web-Nauka, konferencje: „Opis EN” (`tresc_en`, Markdown), zaraz pod opisem;
   - Web-Instytut, Sylwetki, karta: „Źródło zdjęcia EN” (`obraz_zrodlo_en`), pod „Źródłem zdjęcia”.
4. **Drobna poprawka kodu (nie ma jej w łatce):** `src/lib/wartoWiedziec.ts`, `portretHtml()` — napis „Zdjęcie” w portrecie zastępczym (tylko Podgląd) na `/en` ma brzmieć „Photo” (`lang="en"`). Funkcja nie dostaje dziś języka; dodaj parametr albo zrób to w miejscu wywołania, bez zmian na stronach PL.
5. **Nie zmieniaj** wyglądu ani stron polskich, poza poprawkami z punktu 6.
6. **Poprawki polskich tekstów** — sekcja „Błędy w polskich tekstach” niżej (dopisane 22.11, 14:28, na prośbę właściciela).

## Błędy w polskich tekstach (punkt 6; dopisane 22.11, 14:28)
Agenci znaleźli je przy okazji tłumaczenia (szczegóły w `raport-agent-*.md`, sekcje „Błędy w polskim tekście”). Zasady:
- Rób to **po nałożeniu łatek**, osobnym commitem „Poprawki PL” w tych samych gałęziach roboczych.
- Gdy ten sam błąd przeszedł do tekstu EN (np. Drobot, „three books”), popraw też EN.
- Nie zmieniaj nazw plików ani adresów. Nie zmieniaj tytułów publikacji cytowanych w danych (np. `Web-Nauka/src/data/publikacje/2017.json` „Wkład Czesława Ryll-Nardzewskiego…” zostaje, to tytuł pracy).
- Każdą zmianę wypisz w raporcie (plik, było → jest).

### A. Do poprawienia
**„Warto wiedzieć” (Web-Instytut, `src/content/warto_wiedziec/`):**
1. `sylwetki/stanislaw-hartman.md`: „po Stanisławie Drobocie” → „po Stefanie Drobocie”. Pierwszy powojenny wrocławski doktorat z matematyki miał Stefan Drobot (1947), tak jak w sylwetce Ślebodzińskiego. EN: „Stanisław Drobot” → „Stefan Drobot”.
2. `sylwetki/tomasz-rolski.md`: „trzech książek” → „czterech książek”, bo tekst i Źródła wymieniają cztery (1981, 1999, 2004, 2025). EN: „three books” → „four books”.
3. `sylwetki/marek-bozejko.md`: „hiperoctaedralnymi” → „hiperoktaedralnymi”.
4. **Odmiana „Ryll-Nardzewski”** (odmieniają się obie części):
   - „Czesława Ryll-Nardzewskiego” → „Czesława Rylla-Nardzewskiego” w `sylwetki/edward-marczewski.md`, `wladyslaw-narkiewicz.md`, `stanislaw-hartman.md` (Treść) oraz Web-Core `src/data/ciekawostki/studia.json` (notka);
   - „Czesławem Ryll-Nardzewskim” → „Czesławem Ryllem-Nardzewskim” w `stanislaw-hartman.md` (zajawka) i `jan-mycielski.md`;
   - sprawdź `grep` inne formy („Ryll-Nardzewskiemu”, „Ryll-Nardzewskim”…), poza tytułami publikacji.
5. `sylwetki/witold-wolibner.md`: „Laszlo Székelyhidi” → „László Székelyhidi”; w zajawce półpauza „ – ” → pauza „ — ”.
6. `sylwetki/wladyslaw-slebodzinski.md`: „Hugo Steinhausa” → „Hugona Steinhausa”.
7. `historie/wyklad-terencea-tao.md`: „na cześć Profesora Eliasa M. Steina” → „na cześć Eliasa M. Steina”, „prof. Pawła Strzeleckiego” → „Pawła Strzeleckiego”. Styl WW: tytuł ma tylko główna osoba wpisu.
8. `sylwetki/andrzej-krzywicki.md`:
   - **Zajawka:** „Uczeń Witolda Wolibnera, od którego – według monografii… – zaczęła się we Wrocławiu teoria równań różniczkowych…” gramatycznie wskazuje Wolibnera, a Treść mówi o Krzywickim. Przeredaguj tak, żeby jednoznacznie chodziło o Krzywickiego, np. „Według monografii wrocławskich szkół naukowych to od niego zaczęła się we Wrocławiu teoria równań różniczkowych; uczeń Witolda Wolibnera. …”. Najpierw potwierdź to w Treści. Limit ok. 220 znaków, pauza „ — ”.
   - **Źródła:** „Spis pracowników na Podglądzie nowej strony Instytutu” → „Spis pracowników na stronie Instytutu”. EN analogicznie, bez „Preview”.
9. `sylwetki/kazimierz-urbanik.md` (Treść, ok. l. 150): link przy „sesja naukowa „Kazimierz Urbanik (1930–2005)”” prowadzi do PDF wspomnienia (`…/KU.pdf`). Zmień go na stronę sesji `http://www.math.uni.wroc.pl/sesja_Urbanik`, jak w Źródłach. To samo w EN (ok. l. 80).
10. **Tytuły prac kursywą zamiast „…”** w Treści sylwetek Dudy, Bilera, Hartmana, Wolibnera, Narkiewicza i Ślebodzińskiego (styl WW, `claude/instrukcja-dla-czatow.md`):
    - dotyczy tytułów książek, artykułów, wykładów i czasopism w tekście;
    - w Treści EN są już kursywą, więc posłuż się nią jako mapą;
    - nie zmieniaj cytatów ani nazw instytucji, a w Źródłach tytuły źródeł zostają jak są.

**Aktualności (Web-Aktualnosci, `src/content/aktualnosci/`):**
11. `2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu.md`:
    - tytuł „Wykład popularnonaukowy z cyklu MISIU. ” → „Wykład popularnonaukowy z cyklu MISIU” (bez kropki i spacji);
    - „dwóch wykładów - z matematyki” → „dwóch wykładów — z matematyki”;
    - miejsce „sala 25, Instytut Informatyki Uniwersytetu Wrocławskiego” → „sala 25, Instytut Informatyki UWr”.
12. `2026-11-10-seminarium-wydzialowe-problem-milenijny.md`:
    - „prof. Grzegorz Karch … która wygłosi” → „który wygłosi”;
    - `zdjecie_opis` „OpenAI votrex ” → „OpenAI vortex”;
    - załącznik „Slajd z wykładu prof. Grzegorza Karch ” → „Slajd z wykładu prof. Grzegorza Karcha”;
    - miejsce „Instytut Informatyki sala 119” → „sala 119, Instytut Informatyki UWr”.
13. `2026-11-18-nagroda-im-prof-andrzeja-hulanickiego-dla-agnieszki-i-mariusza.md`: „Nagroda im. **Andrzeja Hulanickiego przyznawana** jest” → „**Nagroda im. Andrzeja Hulanickiego** przyznawana jest”; podpis galerii bez spacji na końcu.
14. `2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza.md`: zajawka bez spacji na końcu, z kropką.

**Konferencje (Web-Nauka, `src/content/konferencje/`):**
15. `2020-…`, `2021-…` i `2022-19th-workshop-…`: w polu `tytul` (i w `tytul_en`, jeśli jest) „Noncommucative” → „Noncommutative”. Nazw plików nie zmieniaj.
16. `2019-winter-school-in-abstract-analysis-2019.md`: „Pittisburgh” → „Pittsburgh”.
17. `2021-` i `2022-xxxiv-konferencja-z-historii-matematyki.md`: pogrubienie zamknięte po spacji („…roku. **”) → „…roku.**”, w PL i EN.
18. `2020-xxxiv-konferencja-z-historii-matematyki.md`: „17-21 maja 2021” → „17–21 maja 2021”.
19. `2017-` i `2018-winter-school-…`:
    - „Sao Paulo” → „São Paulo”;
    - przecinek przed „której” („**Winterschool in Abstract Analysis, section Set Theory & Topology**, której”);
    - w tych opisach (także 2019) zakres dat „26 stycznia - 2 lutego” z łącznikiem → „26 stycznia – 2 lutego”.

**Studia (Web-Studia):**
20. `kierunki/matematyka.md` (etapy I stopnia): „**Semestry 1: Podstawy**” → „**Semestr 1: Podstawy**”; „**Semestry 5–6: Przedmioty specjalnościowe.** —” → „**Semestry 5–6: Przedmioty specjalnościowe** —” (bez kropki w pogrubieniu). W EN to samo, jeśli jest.

**Popularyzacja (Web-Popularyzacja):**
21. `strony/popularyzacja/uczniowie.md`:
    - „Uniwerystetem” → „Uniwersytetem”, „postawowej” → „podstawowej”, „Ddla” → „Dla”;
    - „dwóch wykładów - z matematyki” → „ — ”, „kilkanaście godzin - aż” → „kilkanaście godzin — aż”;
    - brakująca kropka po „rozumowań” (akapit o meczach, ok. l. 239).
22. `strony/popularyzacja/nauczyciele.md`: „zagranicą” → „za granicą”.
23. `data/popularyzacja.md`:
    - akapit złamany w trzech liniach i łamanie w środku tekstu linku → jedna linia na akapit;
    - cudzysłowy "…" → „…” (np. ["Kalejdoskop…"]);
    - w kafelku „Dla uczniów” zbędne „ .” na końcu (ok. l. 131).

**Kod (Web-Core), strony PL — wyjątek od „nie zmieniaj stron polskich”:**
24. `src/components/zal/DrugiEkran.astro` (ok. l. 124): „2 referatów w tym tygodniu” → poprawna odmiana: 1 referat, 2–4 referaty, 5+ referatów (`odmiana()` z `i18n.ts`).
25. `src/views/Obrona.astro`: „Promotor” → „Promotorzy” przy dwóch i więcej (jak „Supervisors” w EN).
26. `src/views/Obrona.astro` i `src/components/WierszWydarzenia.astro`: na stronach PL polskie tytuły rozpraw mają dziś `lang="en"`. Daj `lang` według języka tytułu (`langTekstu`), czyli polski tytuł bez `lang="en"`, a angielski z `lang="en"`. Wygląd bez zmian.

**Odpowiedzi właściciela (22.11, 14:56) — też do zrobienia:**
27. `sylwetki/marek-bozejko.md` i `sylwetki/tomasz-rolski.md`: **usuń z Źródeł** (PL i EN) pozycję „[Nota biograficzna prof. … (PDF)](/pliki/aktualnosci/…notabiograficzna.pdf) — tekst sylwetki to nota z niewielkimi zmianami redakcyjnymi; autor: Grzegorz (do uzupełnienia nazwiskiem)” (EN: „… author: Grzegorz (surname to be added)”). Decyzja właściciela: tekst napisał prof. Grzegorz Karch, a źródło ma zniknąć. Pliki PDF w Web-Aktualnosci zostają (są załącznikami aktualności o medalach).
28. `sylwetki/marek-bozejko.md`, „tak jak w źródłach”:
    - Nagroda Humboldta „(2000)” → „(2001)” w PL i EN; to samo w Web-Nauka `strony/nauka/sukcesy/historia.md` („- 2000 Marek Bożejko” pod „Międzynarodowa Nagroda Humboldta” i w EN pod „Humboldt Research Award”);
    - „Habilitował się w 1980 roku, a w 1991 roku został profesorem zwyczajnym.” → „Habilitował się w 1980 roku, a w 1990 roku został profesorem nadzwyczajnym.” EN: „became a full professor in 1991” → „became an extraordinary professor in 1990”.
29. `sylwetki/roman-duda.md`: link przy książce *Historia matematyki w Polsce na tle dziejów nauki i kultury* (2019) prowadzi dziś do artykułu z 2008 r. (bazhum.muzhp.pl, Kwartalnik HNiT 2008). Zamień go w Treści PL i EN na `https://www.ihnpan.pl/a-history-of-polish-mathematics-by-roman-duda/` (strona Instytutu Historii Nauki PAN, wydawcy z 2019 r. razem z ASPRA-JR, z danymi wydania). Pozycji w Źródłach o artykule z 2008 r. nie ruszaj, bo opisuje inny tekst.
30. `sylwetki/witold-wolibner.md`: w EN „born in 1902 in Piotrowo” → „born in 1902 in Piotrowie” (decyzja właściciela: forma jak w źródle; PL bez zmian).
31. Web-Studia `kierunki/matematyka.md`, etap „Semestry 5–6”: na I stopniu **nie ma pracy licencjackiej** (decyzja właściciela). PL: „Przedmioty specjalności, zespołowy projekt specjalnościowy i praca licencjacka.” → „Przedmioty specjalności i zespołowy projekt specjalnościowy.” EN: „Specialisation courses, a team specialisation project and a bachelor's thesis.” → „Specialisation courses and a team specialisation project.” Wzmianek o pracy licencjackiej w starym programie (`egzaminy-i-dyplom.md`, `procedura-dyplomowania.md`, tematy prac na specjalnościach) nie ruszaj.
32. `sylwetki/marek-bozejko.md` (decyzja właściciela 14:58, „jak w źródłach”): w Treści PL „rozkładów Askeya–Wimpa–Kerowa” → „rozkładów Askeya–Wimpa–Kerova”. EN („Askey–Wimp–Kerov”) bez zmian.
33. Web-Aktualnosci `2026-05-12-ksztalcenie-w-krajowej-szkole-administracji-publicznej.md` (decyzja właściciela 14:58: „prowadzi”):
    - zajawka „Krajowa Szkoła Administracji Publicznej prowadziła od 4 maja…” → „…prowadzi od 4 maja…”, czyli tak jak w Treści;
    - `zajawka_en` „From 4 May to 24 July 2026 the National School of Public Administration recruited for…” → „…is recruiting for…”.

### B. Sprawy do właściciela
Wszystkie rozstrzygnięte 22.11, 14:56–14:58 (punkty 27–33; daty `2015-01-01` w 7 aktualnościach zostają). Nie pytaj o nie ponownie. Nowe wątpliwości wpisz do raportu jako pytania.

## Sprawdzone w chmurze (wszystkie łatki razem, budowa `PODGLAD=1`)
- **Strony PL:** 477 plików HTML bez zmian. Wyjątki: `uid` wysp React na 3 stronach (Pracownicy, dwie aktualności z galerią). Dane wysp po rozkodowaniu są identyczne; zmienia się tylko losowy identyfikator.
- **Strony `/en`:** polskie fragmenty z `lang="pl"` (pusty EN) spadły z 431 do 228. Pozostałe są celowe:
  - tytuły rozpraw na obronach z etykietą „Original title:” (D5, D14), także na liście obron i w Kalendarzu;
  - tytuły grantów w oryginale pod angielskim tytułem;
  - tematy prac na specjalnościach (D17);
  - tytuł referatu po polsku;
  - napis „Zdjęcie” (punkt 4).
- **Przykłady do obejrzenia na `/en`:**
  - tytuł MISIU na stronie głównej i w „Upcoming events”;
  - „room 25, Institute of Computer Science, University of Wrocław”;
  - „For: students, PhD students, staff”;
  - obrona z dwoma promotorami: „Supervisors”, „(auxiliary supervisor)”;
  - obrona zdalna: „… online.” bez „in”;
  - `/en/nauka/konferencje/*` z opisem po angielsku;
  - sylwetki WW z pełną treścią i „Photo: University of Wrocław Archives”;
  - Popularyzacja (3 Treści EN napisane od nowa).
- `sprawdz_tresci.py`: OK. W Web-Instytut zostają 2–3 znane wcześniej błędy „brak pliku obrazu /pliki/aktualnosci/…” w `warto_wiedziec/nagrody`, bo obrazy leżą w Web-Aktualnosci (tak samo na czystym `main`).

## Kryteria odbioru
- Wszystkie 7 łatek nałożone. Konflikty i pliki zmienione przez redaktorów wypisane w raporcie, wraz ze sposobem rozwiązania.
- `astro check` 0 błędów, `npm run test:jawne` OK.
- `sprawdz_tresci.py` OK (poza znanymi błędami obrazów WW).
- `sprawdz_pola_cms.py` 0 problemów. `sprawdz-jawny-markdown.mjs` OK dla Web-Studia, Web-Instytut i Web-Ustawienia.
- HTML stron PL przed/po: różnice tylko w `uid` wysp i w miejscach z punktu 6A (cały `dist`; lista w raporcie).
- Poprawki z punktu 6A (1–33) zrobione; lista w raporcie: plik, było → jest.
- Na `/en` przykłady z listy wyżej wyglądają poprawnie: zrzuty 390 px i 1920 px, `raport-zrzuty/z59-*`. Do tego co najmniej jedna sylwetka WW, jedna konferencja, obrona z dwoma promotorami, strona główna, Popularyzacja i Matematyka (etapy studiów).
- Przełącznik języka na stronach z sekcjami (Studia, Instytut, Popularyzacja, WW) trafia w tę samą sekcję w PL i EN, bo `{#id}` są teraz wspólne.
- Formularze CMS z nowymi polami: YAML poprawny i pola w dobrym miejscu (pod polskim odpowiednikiem).

## Decyzje przyjęte domyślnie w tłumaczeniu (do zmiany na prośbę właściciela)
Pełna lista z uzasadnieniem jest w raportach agentów, sekcje „Do decyzji”. Najważniejsze:
- **IM PAN:** „Institute of Mathematics of the Polish Academy of Sciences”. „Mathematical Institute” oznacza tylko IM UWr.
- **Politechnika Wrocławska:** wszędzie „Wrocław University of Science and Technology”, także w kontekstach historycznych (ujednolicone w łatkach, łącznie ze stroną „Sukcesy — historia”).
- **Stanowiska historyczne:**
  - adiunkt → research fellow (w instytutach PAN) albo lecturer (na uczelni);
  - docent → docent;
  - profesor nadzwyczajny → extraordinary professor;
  - profesor zwyczajny → full professor.
- **Polskie tytuły książek i wykładów w tekstach EN:** oryginał kursywą, a w nawiasie tłumaczenie (jak D4).
- **„Admissions (in Polish)”** na stronie głównej i w stopce (D20).
- **Nazwa pracowni:** „Mathematics Education and Outreach Unit”.
- **Wspólne `{#id}`:** w EN ujednolicone do polskich. Stare angielskie kotwice (np. `#forms`) przestały działać, ale strony się otwierają.
- **Zostawione bez zmian:**
  - 7 grantów z tytułem już po angielsku ma puste `tytul_en`, żeby tytuł nie pokazał się dwa razy;
  - grafik tutorni na `/en` pokazuje polskie skróty przedmiotów (propozycja w raporcie agenta 3);
  - apostrofy `'` / `’` niejednolite (89 : 10), bez masowej zamiany.
