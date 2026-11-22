# Raport: zlecenie 55 — portrety sylwetek „Warto wiedzieć” (19.11.2026)

**Stan: zrobione i wypchnięte** (push samodzielny według polecenia z 19.11, po spełnieniu warunków: budowa, kontrole, porównanie HTML, fetch i rebase, budowa po rebase, ochrona zmian redaktorów, cisza).

| Repozytorium | Push | Godzina | Podgląd (GitHub Actions) |
|---|---|---|---|
| Web-Core | `6193ddfd..67ac130f` | 12:36 | run 44516354462 — sukces (1 min 29 s) |
| Web-Instytut | `a255edb..e88a088` | 12:38 | run 44516690637 — sukces (1 min 34 s) |
| Web-Ustawienia | `1fb08e6..fd49210` | 12:40 | run 44517040880 — sukces (1 min 32 s) |

Na żywo (sprawdzone po budowie Podglądu): portrety na liście i stronach osób, podpis „Fot. Wikimedia Commons” / „Fot. IM UWr” (jeden „Fot.”), fragment `#portrety` na „O stronie” PL i EN, plik `pliki/warto-wiedziec/portrety/hugo-steinhaus.jpg` (200, 97 434 B).

**Arkusz wyboru:** `raport-zrzuty/z55-wybor.html` (zrzuty `raport-zrzuty/z55-wybor.png` — cały arkusz, `raport-zrzuty/z55-wybor-siatka.png` — siatka w szarości ze złotem, w kolorze, mini portrety i tryb ciemny). Pliki robocze: `.przekazanie\robocze\55-portrety\` (`oryginaly/`, `zrodla.json`, `kadry.json`, `portrety.py`, `zrodla.py`, `podlacz.py`, `arkusz.py`, `wynik/`). Zmiana wariantu: w `kadry.json` wpisać wariant i plik (dla Ślebodzińskiego 4b czeka gotowy w `warianty_zapasowe`), punkty z podglądu, potem `python portrety.py licz <slug>`, `python portrety.py rob <slug>`, `python podlacz.py <Web-Instytut>` (na świeżym main), `python zrodla.py wstaw <o-stronie.md>`.

## Co zmieniono

- **Web-Core** (`67ac130f`):
  - `src/views/SylwetkaWW.astro`: przed wypisaniem „Źródła zdjęcia” strona zdejmuje z początku „Fot.”, „Fot:”, „Foto:”, „Photo:” i „Photo” (bez względu na wielkość liter, ze spacjami; „Photographer…” i „Fotograf…” zostają). Prefiks `T('Fot.', 'Photo:')` bez zmian. Komentarz z odwołaniem do zlecenia 55.
  - `skrypty/migracja/formularze_40.mjs`: opisy pól „Zdjęcie” i „Źródło zdjęcia” dokładnie jak w zleceniu. Generator uruchomiony na kopii Web-Instytut daje te same dwie linie co ręcznie zmieniony `.pages.yml`.
  - `dok/sciagawka-edytora.md`, punkt „Sylwetka”: zdanie o portrecie 4:5, krótkim „Źródle zdjęcia” i pełnym źródle na „O stronie”.
- **Web-Instytut** (`e88a088`): 16 plików `public/pliki/warto-wiedziec/portrety/<slug>.jpg`. W 16 sylwetkach zmieniły się tylko linie `  obraz:` i `  obraz_zrodlo:` w `karta:` (u Tabisza `obraz_zrodlo` dopisana pod `obraz:`). W `.pages.yml` zmieniły się dwie linie `description` (w cudzysłowie, plik się parsuje). Skrypt `podlacz.py` pracuje linia po linii i nie nadpisuje innych wartości niż oczekiwane; na świeżym main nie było takich przypadków.
- **Web-Ustawienia** (`fd49210`): w „O stronie” po punkcie o zdjęciu kampusu dodany śródtytuł `### Portrety w „Warto wiedzieć” {#portrety}` / `### Portraits in “Did you know” {#portrety}`, zdanie i 16 linii. Linie generuje `zrodla.py` z `zrodla.json` i `kadry.json`. Pozostałe sekcje i `{#id}` bez zmian.

## Tabela osób

Kadr w pikselach źródła. Skala = 750 / wysokość kadru. Wszędzie wariant A (wariant B nie powstał, patrz niżej). USM to promień / siła / próg. Każdy plik ma 600×750, JPEG q85, jest progresywny, bez EXIF i bez innych metadanych, ≤ 150 KB.

| Osoba | Wariant | Źródło (px) | Kadr x, y, szer., wys. | Skala | A/B | Oczy / głowa / nad głową | Obróbka | Plik | Prawa | Podpis |
|---|---|---|---|---|---|---|---|---|---|---|
| Piotr Biler | 15 | 1024×683 | 289, 5, 440, 550 | ×1.364 | A | 38.0% / 48.0% / 11.8% | barwne; USM 1.0/60/2 | 51 124 B | brak licencji | PAN |
| Marek Bożejko | — | 120×160 | — | — | — | — | — | portret zastępczy | — | — |
| Roman Duda | 13b | 1011×719 | 331, 0, 368, 460 | ×1.630 | A | 35.9% / 53.9% / 2.6% | barwne; USM 1.0/60/2 | 49 927 B | brak licencji | Politechnika Łódzka |
| Stanisław Hartman | 7 | 667×1000 | 155, 208, 352, 440 | ×1.705 | A | 45.9% / 79.5% / 3.2% | cz-b → szarość; USM 1.0/60/2 | 65 158 B | brak licencji | Archiwum UWr |
| Andrzej Hulanicki | 11 | 265×400 | 79, 0, 168, 210 | ×3.571 **słaba jakość** | A | 35.7% / 51.4% / 14.8% | cz-b → szarość; USM 1.3/80/3 | 38 735 B | wolna (CC BY-SA 2.0 DE) | Konrad Jacobs / MFO, CC BY-SA 2.0 DE |
| Bronisław Knaster | 3b | 467×570 | 2, 0, 456, 570 | ×1.316 | A | 36.1% / 68.9% / 3.9% | cz-b → szarość; USM 1.0/60/2 | 70 088 B | brak licencji | Archiwum UWr |
| Andrzej Krzywicki | 12 | 240×240 | 19, 0, 192, 240 | ×3.125 **słaba jakość** | A | 35.4% / 76.2% / −4.2% | cz-b → szarość; USM 1.3/80/3 | 44 207 B | brak licencji | IM UWr |
| Edward Marczewski | 2b | 467×570 | 11, 0, 456, 570 | ×1.316 | A | 37.7% / 61.1% / 6.7% | odszumienie 0.7; cz-b → szarość; USM 1.0/50/5 | 101 714 B | brak licencji | Archiwum UWr |
| Jan Mycielski | 10 | 591×902 | 85, 178, 320, 400 | ×1.875 | A | 38.0% / 48.0% / 10.0% | barwne; USM 1.0/60/2 | 76 686 B | brak licencji | archiwum prywatne / UWr |
| Władysław Narkiewicz | 14b | 400×510 | 110, 19, 200, 250 | ×3.000 | A | 36.0% / 49.2% / 13.2% | barwne; USM 1.3/80/3 | 64 105 B | brak licencji | galeria J. Shallita, University of Waterloo |
| Julian Perkal | 6 | 211×301 | 3, 0, 208, 260 | ×2.885 | A | 52.7% / 86.9% / 1.9% | cz-b → szarość; USM 1.3/80/3 | 63 796 B | brak licencji | Polskie Towarzystwo Biometryczne |
| Tomasz Rolski | 17 | 1280×1024 | 264, 144, 704, 880 | ×0.852 | A | 43.2% / 70.6% / 6.2% | barwne; USM 0.7/50/2 | 63 919 B | brak licencji | ze strony T. Rolskiego |
| Czesław Ryll-Nardzewski | 8b | 387×439 | 24, 1, 316, 395 | ×1.899 | A | 38.0% / 51.6% / 9.1% | cz-b → szarość; USM 1.0/60/2 | 60 693 B | brak licencji | Centrum Rylla-Nardzewskiego PWr |
| Hugo Steinhaus | 1 | 1280×1914 (miniatura Commons) | 21, 0, 1184, 1480 | ×0.507 | A | 35.9% / 60.2% / 7.0% | odszumienie 1.6; cz-b → szarość; USM 0.7/50/2 | 97 434 B | domena publiczna | Wikimedia Commons |
| Władysław Ślebodziński | 4a | 502×634 | 2, 0, 500, 625 | ×1.200 | A | 46.7% / 76.0% / 2.4% | cz-b (sepia) → szarość; USM 1.0/60/2 | 90 701 B | domena publiczna według Commons | Wikimedia Commons |
| Krzysztof Tabisz | 18 | 240×240 | 2, 0, 192, 240 | ×3.125 **słaba jakość** | A | 42.9% / 75.0% / 5.0% | barwne; USM 1.3/80/3 | 48 915 B | brak licencji | IM UWr |
| Kazimierz Urbanik | 9 | 569×989 | 70, 0, 364, 455 | ×1.648 | A | 36.0% / 53.6% / 6.2% | cz-b → szarość; USM 1.0/60/2 | 49 812 B | wolna (CC BY-SA 3.0) | Ryszard Świtacz, CC BY-SA 3.0 |
| Witold Wolibner | — | brak pliku | — | — | — | — | — | portret zastępczy | — | — |

Dla wszystkich wybranych zdjęć: poziomy z obcięciem 0,5% (jedna krzywa dla wszystkich kanałów, barwy bez zmian), Lanczos do 600×750, unsharp mask po skalowaniu. Bez naprawy twarzy, inpaintingu, usuwania znaków wodnych, retuszu i koloryzowania. Znak wodny MFO u Hulanickiego leży w prawym dolnym rogu, poza kadrem.

**Kadr.** Gdzie źródło na to pozwala, oczy są na 36–38%, a głowa zajmuje 48–54% kadru (Biler, Duda, Hulanicki, Mycielski, Narkiewicz, Ryll-Nardzewski, Urbanik). **Ciasne źródła** dają większą głowę i niżej położone oczy, a tła ani marginesów nie dorabialiśmy (zlecenie to dopuszcza): Perkal (oczy 52,7%, głowa 87%), Hartman (46/80%, zdjęcie w skanie ma tylko ok. 353×527), Ślebodziński (47/76%), Krzywicki (35/76%, czubek głowy ucięty już w źródle), Tabisz (43/75%), Rolski (43/71%), Knaster (36/69%), Marczewski (38/61%), Steinhaus (36/60%, źródło ciasne w poziomie). **Mini portret** (kwadrat od 6% w dół, czyli do 86% wysokości): broda mieści się u wszystkich poza Perkalem (89%), w kółku 30 px to ok. 1 px; Perkala nie ma w `:::laureaci`. Półprofil: kadr przesunięty o 6,5% szerokości tak, żeby przed twarzą było więcej miejsca (twarz zwrócona w lewo: Steinhaus, Urbanik, Krzywicki, Tabisz; w prawo: Marczewski, Ślebodziński, Hulanicki). Prostowanie nie było potrzebne.

## Wybór wariantów, odrzucone warianty

- **2 Marczewski: 2b.** 2a to półprofil z daleka (głowa ok. 100 px, kadr ok. 210 px) ze znakiem wodnym MFO; 2b to twarz w trzech czwartych z kadrem 570 px (kryteria 1, 2, 4).
- **3 Knaster: 3b.** 3a to półprofil 365×270 (kadr najwyżej 216 px) ze znakiem wodnym MFO (kryteria 1–3).
- **4 Ślebodziński: 4a** (zmiana względem wstępnego 4b). 4a to ostra fotografia z 1938 r. z kadrem 625 px, domena publiczna według Commons. 4b to skan druku z ziarnem (wymagał odszumienia), kadr 570 px, bez licencji. Rozstrzygnęły kryteria 1, 2 i 5. 4b zostaje w `kadry.json` jako zapas: „dla Ślebodzińskiego weź 4b” to zmiana dwóch pól i ponowne uruchomienie skryptów.
- **8 Ryll-Nardzewski: 8b.** 8a ma mocny cień na połowie twarzy i znak wodny MFO; kadr ok. 260 px (kryteria 1, 3).
- **13 Duda: 13b.** 13a ma 213×298, kadr najwyżej 266 px, głowa zajmuje ok. 70%, a w rogu widać głowę innej osoby (kryteria 2, 3).
- **14 Narkiewicz: 14b.** 14a to postać siedząca przy biurku, głowa ok. 80 px, kadr przy głowie 42–52% ma 155–190 px, czyli poniżej progu 200 (kryterium 2). Tablicy z 14b nie widać w kadrze.
- **Bez portretu:** Wolibner (brak pliku), Bożejko (120×160, kadr 4:5 najwyżej 128×160, poniżej progu: potrzebny większy oryginał).
- **Słaba jakość, potrzebny większy oryginał (powiększenie ponad 3×):** Hulanicki ×3,57, Krzywicki ×3,13, Tabisz ×3,13. Na granicy: Narkiewicz ×3,00 i Perkal ×2,89.
- **Wariant B (Real-ESRGAN) nie powstał.** Wymagałby pobrania i uruchomienia zewnętrznego programu (`realesrgan-ncnn-vulkan`), czego dziś nie dało się potwierdzić z właścicielem. Wariant jest opcjonalny, a domyślnie i tak wygrywa A. Dotyczy osób z powiększeniem ponad 2×: Hulanickiego, Krzywickiego, Tabisza, Narkiewicza i Perkala. Jeśli właściciel zechce B, wystarczy dołożyć program do `.przekazanie\robocze\` i dopisać wariant w arkuszu.
- **Tożsamość:** zdjęcia pochodzą ze stron źródłowych dotyczących tych osób. 8b jest ze strony Centrum Rylla-Nardzewskiego poświęconej Czesławowi (nie ojcu). Wariant 12 pochodzi ze strony użytkownika `krzywick` w IM UWr (matematyk z Wrocławia, nie fizyk André Krzywicki).
- **Tabisz:** `tabisz.jpg`, `tabisz-1.jpg` i wariant 18 to ten sam plik (sha256 `4bec6ce1a8f0385d…`, 240×240), więc kadr zrobiony z wariantu 18.

## Pobranie i rozbieżności z zestawieniem

- **Wikimedia (upload.wikimedia.org): HTTP 429** „Too many requests” od rana dla oryginałów, a od 12:14 także dla miniatur (blokada adresu). Strony plików na commons.wikimedia.org działały, więc zgodnie z etapem 1 („ze strony źródłowej, największa wersja”):
  - **Steinhaus:** miniatura Commons 1280×1914 tego samego pliku (oryginał 1659×2481 niedostępny). Kadr i tak jest pomniejszany (×0,51), więc jakość na tym nie traci.
  - **2a, 4a, 11, 13a, 14a:** pobrane przez `commons.wikimedia.org/w/thumb.php` w szerokości oryginału. Wymiary zgadzają się z zestawieniem, ale serwer koduje JPEG ponownie, więc sha256 różni się od oryginału (np. Hulanicki 14 464 B zamiast 12 507 B). Adresy są w `zrodla.json` (`url_uzyty`).
- **8b:** link z zestawienia wygasł (404). Ten sam portret pobrany z aktualnego linku na stronie źródłowej (387×439, jak w zestawieniu).
- **Perkal (6):** plik w stylu „large” to 211×301, czyli tyle samo co oryginał Drupala (`/sites/default/files/2022-09/memoriesPerkal.jpg`). Użyty oryginał, bo jest mniej skompresowany (31 662 B zamiast 14 191 B). Większej wersji strona nie ma.
- **Urbanik (9):** na karcie Commons jako autor figuruje „Ryszard Świtacz - Pracownia Reprografii Biblioteki Uniwersyteckiej we Wrocławiu”, a jako źródło „home archive of Henryk Zieliński” (zestawienie: „Ryszard Świtacz; archiwum Henryka Zielińskiego”). Na „O stronie” są oba.
- **Duda (13a):** autor na karcie to „Katarzyna Czerwńska” (zapewne literówka), licencja CC BY-SA 3.0 pl, data 2014-07-04. Wariant odrzucony.
- **Knaster (3a):** autor na karcie to „Konrad Jacobs, Erlangen”.
- **Hulanicki (11):** data na karcie to „Unknown date”, źródło: Oberwolfach Photo Collection, photo_id 1856. Licencja CC BY-SA 2.0 de, zgodnie z zestawieniem.
- **Ślebodziński (4a):** na karcie autor nieznany, źródło „souvenir in the family collection”, Public domain, 1938-07-04. Zestawienie opisuje podstawę jako niepełną, więc na „O stronie” jest napisane „oznaczone w Wikimedia Commons jako domena publiczna”.
- Pozostałe wymiary zgodne z zestawieniem. Pełne dane (URL, strona, data pobrania, sha256, wymiary, karta Commons) są w `zrodla.json`.

## „O stronie”

16 linii PL i EN w kolejności nazwisk, generowanych z `zrodla.json` i `kadry.json`. Autor pojawia się tylko tam, gdzie podaje go źródło („autor nieznany” u Steinhausa i Ślebodzińskiego, Konrad Jacobs, Ryszard Świtacz). Bez wypełniaczy. Licencje CC są linkami do deed (`deed.pl` / `deed.en`), domena publiczna jest opisana słowami, a przy zdjęciach bez licencji nie ma nic. Zmiany: „kadr, wyostrzenie” (Steinhaus, Rolski, czyli pomniejszone) albo „kadr, powiększenie i wyostrzenie” (pozostali). Odszumienie (Steinhaus, Marczewski) i poziomy nie mają osobnego słowa, bo słownik zmian ze zlecenia ma trzy pozycje.

Nazwy instytucji: „ze zbiorów Archiwum UWr, [Muzeum Uniwersytetu Wrocławskiego]” (EN „from the University of Wrocław Archives, [Museum of the University of Wrocław]”), „[Instytut Matematyczny UWr]”, „[Polska Akademia Nauk]”, „[Polskie Towarzystwo Biometryczne]”, „[Centrum Rylla-Nardzewskiego, Politechnika Wrocławska]”, „[Centrum Nauczania Matematyki i Fizyki Politechniki Łódzkiej]”, „Colloque Mendès France, Bordeaux 2000, [galeria Jeffreya Shallita, University of Waterloo]”, „archiwum prywatne, [Uniwersytet Wrocławski]”, „[strona domowa Tomasza Rolskiego]”.

Linki (21 adresów: strony źródłowe i deed): wszystkie odpowiadają **200** (`linki-ostronie-kody.txt` w katalogu roboczym).

## Kontrole (odbiór lokalny)

- Budowa publiczna PL i EN (`TYLKO_OPUBLIKOWANE=1`): `z55-przed` (origin/main we wszystkich trzech repozytoriach) i `z55-po`, obie przechodzą. Po rebase (bez zmian, main się nie ruszył) budowa `z55-push` jest identyczna z `z55-po` (różnice tylko w znacznikach czasu).
- **HTML przed i po:** 56 plików, wszystkie w dozwolonych miejscach:
  - lista „Warto wiedzieć” i „Inne sylwetki” (także na stronach Bożejki i Wolibnera);
  - strony 16 osób (portret, podpis i `og:image`; u Tabisza zamiast `tabisz-1.jpg`);
  - historie z „Ludźmi w tej historii” (Nowa Księga Szkocka, Stypendium Steinhausa, Aksjomat determinacji, Czterech rektorów, Pierwsze wykłady, Taksonomia wrocławska);
  - Medal UWr (mini portret Rolskiego w `:::laureaci` i karta w „Sylwetkach laureatów”);
  - strona główna (karty „Warto wiedzieć”);
  - „O stronie” PL i EN.

  Do tego 108 plików tylko ze znacznikiem czasu i kolejność w sitemap. Indeks wyszukiwarki pominięty. **Jedna różnica do zgłoszenia:** w `dist/_astro/` przybyło 16 kopii portretów (`<slug>.<hash>.jpg`). Tworzy je budowa z `import.meta.glob` w `src/lib/zdjecia.ts`, czyli tak samo jak dla innych zdjęć z `public/pliki`. Żaden HTML się do nich nie odwołuje. Nieszkodliwe, ok. 1 MB.
- Pliki: 16 × 600×750, 38–102 KB, bez EXIF, ICC, XMP i IPTC — **OK**.
- W `dist` nie ma „Fot. Fot.” ani „Photo: Photo” — **0 wystąpień**. Podpisy: „Fot. …” / „Photo: IM UWr”.
- `astro check`: 0 błędów, 0 ostrzeżeń, 8 podpowiedzi (jak po 53 i 54). `npm run test:jawne`: **84/84**.
- `sprawdz_tresci.py`: OK, 594 pliki. `sprawdz_pola_cms.py ../tresci-C`: 753 pliki, **0 problemów**. `sprawdz-jawny-markdown.mjs`: Web-Instytut OK (33 wpisy WW, złych linii bloków 0), Web-Ustawienia OK (nagłówki bez `{#id}`: 0).
- **Zrzuty** w `raport-zrzuty/z55-zrzuty/` (22 pliki, konsola: 0 błędów i ostrzeżeń):
  - lista: `z55-lista-1920-jasny.png`, `z55-lista-1920-ciemny.png`, `z55-lista-390.png`, `z55-lista-390-cala.png`;
  - osoby przy 1920 i 390: Steinhaus, Knaster, Biler, Tabisz (także EN), Hulanicki (największe powiększenie);
  - Medal: `z55-medal-1920.png`, `z55-medal-390.png`;
  - strona główna: `z55-glowna-1920.png`, `z55-glowna-390.png`;
  - „O stronie”: `z55-o-stronie-1920.png`, `z55-o-stronie-en-1920.png`, `z55-o-stronie-390.png`.

## Ochrona zmian redaktorów

- Bazy: Web-Instytut `a255edb`, Web-Ustawienia `1fb08e6`. W obu tuż przed pushem zrobiony fetch: **0 zapisów od bazy**. Ostatni zapis z Pages CMS w Web-Instytut pochodzi z 18.11, 23:41, więc warunek ciszy był spełniony. Skrypt `podlacz.py` przy powtórnym uruchomieniu na świeżym main daje ten sam wynik (już podłączone pliki nie zmieniają się).
- `kontrola_redaktorow.py przed`: Web-Instytut OK, Web-Ustawienia OK („wszystkie wartości redaktorów są w wyniku”).
- `z55-kontrola.py` (linia po linii, przed pushem i po nim):
  - Web-Instytut: 33 pliki, tylko linie `  obraz:` / `  obraz_zrodlo:` w sylwetkach, dwie linie `description` w `.pages.yml` i 16 portretów — OK;
  - Web-Ustawienia: 1 plik, same dopisane linie fragmentu — OK.
- `kontrola_redaktorow.py po`:
  - Web-Instytut (`--pomin karta.obraz --pomin karta.obraz_zrodlo`): zmienione pole `karta` w 16 plikach, 0 zmian spoza listy. Narzędzie liczy 16 „niedozwolonych” — to 16 plików JPG portretów (sprawdza tylko pliki danych), sprawdzone nazwa po nazwie;
  - Web-Ustawienia: zmienione `body` i `tresc_en` w `o-stronie.md`, czyli zamierzony fragment (narzędzie zna tylko migrację terminów; kontrola linia po linii potwierdza same dopisane linie).
- Przegląd 24 h po pushu: patrz podsumowanie dnia.

## Zgody przed startem (dla właściciela; nic nie wysłano)

Prośba do każdego adresata: zgoda na publikację zdjęcia na stronie IM UWr w wersji wykadrowanej i wyostrzonej, nazwisko autora zdjęcia do podpisu oraz (gdzie warto) większy skan.

| Osoba | Wariant | Do kogo (załącznik B) | O co prosić |
|---|---|---|---|
| Edward Marczewski | 2b | Archiwum UWr, auw@uwr.edu.pl | fotograf, prawo do publikacji, większy skan (jedno pismo, niżej) |
| Bronisław Knaster | 3b | Archiwum UWr, auw@uwr.edu.pl | j.w. |
| Stanisław Hartman | 7 | Archiwum UWr, auw@uwr.edu.pl | j.w.; skan samej fotografii (dziś ok. 353×527 w skanie strony) |
| Władysław Ślebodziński | 4a (Commons) | użytkownik Commons Wtslebo albo rodzina | wyjaśnić podstawę domeny publicznej (zdjęcie z 1938 r., kolekcja rodzinna) |
| Julian Perkal | 6 | PTB, katarzyna.ambrozy-deregowska@up.poznan.pl (albo Archiwum UWr, inwentarz poz. 221, s. 24, zdj. 21) | oryginał i prawa; większy plik (211×301) |
| Czesław Ryll-Nardzewski | 8b | Centrum Rylla-Nardzewskiego, crn@pwr.edu.pl | autor, zgoda, większy plik |
| Jan Mycielski | 10 | redakcja UWr albo webmaster@math.uni.wroc.pl | kontakt do osoby z prawami do zdjęcia z archiwum prywatnego |
| Andrzej Krzywicki | 12 | Andrzej.Krzywicki@math.uni.wroc.pl albo webmaster@math.uni.wroc.pl | oryginał (240×240 to za mało) i potwierdzenie praw |
| Roman Duda | 13b | CNMiF PŁ, cmf@adm.p.lodz.pl | autor i zgoda |
| Władysław Narkiewicz | 14b | Jeffrey Shallit, galeria University of Waterloo | autor i zgoda uprawnionego |
| Piotr Biler | 15 | PAN, media@pan.pl | zgoda na zdjęcie z profilu członka PAN, autor |
| Tomasz Rolski | 17 | rolski@math.uni.wroc.pl | autor, zgoda na publikację i kadr |
| Krzysztof Tabisz | 18 | Krzysztof.Tabisz@math.uni.wroc.pl albo webmaster@math.uni.wroc.pl | większy oryginał i potwierdzenie praw |

**Osoby żyjące** (zgoda na wizerunek razem z akceptacją tekstu sylwetki, przed startem, przez redaktorów): Krzywicki, Duda, Narkiewicz, Biler, Rolski, Tabisz. Bożejko nie ma dziś zdjęcia (prośba o większe zdjęcie: Marek.Bozejko@math.uni.wroc.pl albo webmaster@math.uni.wroc.pl). **Bez zgody** (wolna licencja lub domena publiczna): Steinhaus (PD), Urbanik (CC BY-SA 3.0), Hulanicki (CC BY-SA 2.0 DE). Większe pliki Jacobsa wymagają zgody MFO (photos@mfo.de), tylko jeśli właściciel ich chce. **Wolibner:** najpierw skan z Archiwum UWr (pismo niżej).

## Propozycja pisma do Archiwum UWr (do decyzji właściciela, niewysłane)

> Szanowni Państwo,
>
> Instytut Matematyczny Uniwersytetu Wrocławskiego przygotowuje na swojej stronie internetowej cykl „Warto wiedzieć” — sylwetki matematyków, którzy tworzyli wrocławski ośrodek po 1945 roku. Chcielibyśmy zilustrować je portretami ze zbiorów Archiwum UWr i prosimy o pomoc w trzech sprawach:
>
> 1. **Zgoda na publikację** na stronie Instytutu (w wersji wykadrowanej do portretu 4:5 i lekko wyostrzonej, z podpisem „Fot. Archiwum UWr” i pełnym opisem źródła na stronie „O stronie”) zdjęć prezentowanych w serwisie Muzeum UWr „Dzieje Uniwersytetu — profesorowie po 1945 r.”: prof. Edwarda Marczewskiego, prof. Bronisława Knastera, prof. Władysława Ślebodzińskiego i prof. Stanisława Hartmana.
> 2. **Informacja o autorach** tych fotografii, jeśli jest znana, abyśmy mogli ich podpisać.
> 3. **Skany w większej rozdzielczości** (najlepiej co najmniej 1000 px wysokości samego portretu) tych zdjęć oraz portretów prof. Witolda Wolibnera (Album Dwudziestolecia UWr 1945–1965, poz. 334, s. 25, zdjęcie 35) i, jeśli to możliwe, prof. Juliana Perkala (inwentarz, poz. 221, s. 24, zdjęcie 21).
>
> Chętnie dostosujemy się do zasad i opłat Archiwum. Z góry dziękujemy.
>
> [podpis, Instytut Matematyczny UWr]

## Nieużywane pliki

W `Web-Instytut/public/pliki/warto-wiedziec/` zostały `tabisz.jpg` i `tabisz-1.jpg` (identyczne, 240×240, 8098 B). Po zmianie żaden plik treści się do nich nie odwołuje. Zostają bez usuwania, zgodnie ze zleceniem.

## Decyzje domyślne (do zmiany na prośbę właściciela)

- Warianty: 2b, 3b, **4a**, 8b, 13b, 14b, z uzasadnieniem wyżej i w arkuszu.
- Hulanicki dostał portret mimo powiększenia ×3,57: kadr 210 px jest powyżej progu 200, a zdjęcie jest oznaczone jako „słaba jakość”. Alternatywa to portret zastępczy do czasu większego pliku.
- Oryginały z Commons pobrane przez `thumb.php` w szerokości oryginału, a Steinhaus z miniatury 1280 px (blokada 429).
- Wariant B pominięty.
- Brzmienie linii „O stronie” (nazwy instytucji PL i EN, „ze zbiorów Archiwum UWr”, opis „reprodukcja z księgi pamiątkowej, 1968”) i słownik zmian ograniczony do trzech pozycji.
- Podpisy pod portretem dokładnie z kolumny „Podpis” załącznika A (np. „Fot. ze strony T. Rolskiego”, „Fot. PAN”).

## Uwagi poza zakresem

- Generator `formularze_40.mjs` nadal nie ma zdań „Styl: …” w opisach Treści „Warto wiedzieć” z 54A (patrz raport 54). Ręczny `.pages.yml` jest poprawny, a różnica wyjdzie tylko przy ponownym generowaniu.
- W `kadry.json` brak punktów dla odrzuconych wariantów 2a, 3a, 8a, 13a i 14a: zamiana na nie wymaga odczytania punktów z podglądu (`siatka.py`).
