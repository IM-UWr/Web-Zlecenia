# Zlecenie 55 (19.11.2026): portrety w sylwetkach „Warto wiedzieć”: wybór, pobranie, kadr 4:5, wyostrzenie, podłączenie; źródła na stronie „O stronie”

**Skąd to zlecenie.** Właściciel ma zestawienie kandydatów na portrety 18 osób z „Warto wiedzieć” (`portrety_matematykow_IM_UWr.md`, 19.11; dane w załączniku A, kontakty w załączniku B). Dziś 17 sylwetek ma portret zastępczy, a Tabisz ma zdjęcie 240×240 wgrane przez redaktora.

**Decyzja właściciela (19.11, 10:34):** „Możesz napisać zlecenie na wybranie najładniejszych zdjęć, pobranie, wykadrowanie, potencjalne wyostrzenie i podłączenie ich do sylwetek. A następnie zaktualizowanie o stronie?”

**Decyzja właściciela (19.11, 10:49):** „Zdjęcia bez licencji wchodzą na stronę, załatwię licencje później”.

**Decyzje domyślne** (zmiana na prośbę właściciela):
- **Wybór:** dla każdej osoby najładniejszy wariant według kryteriów z etapu 2. Przy porównywalnej jakości wygrywa wariant z wolną licencją albo w domenie publicznej. Tylko źródła z załącznika A, bez szukania nowych.
- **Prawa (decyzja z 10:49):** zdjęcia bez jawnej licencji (Muzeum UWr, PAN, PŁ, PWr, strona domowa, archiwum prywatne) też wchodzą. Licencje załatwia później właściciel: każde takie zdjęcie trafia do raportu na listę „zgody przed startem” dla niego (załącznik B). Osoby żyjące akceptują zdjęcie razem z tekstem sylwetki (robią to redaktorzy przed startem, decyzja z 19.11, 00:37). Opis pola „Zdjęcie” mówi „tylko z prawem do publikacji”, więc ta lista jest obowiązkowa.
- **Format:** portret pionowy 4:5, plik 600×750 px. Strona pokazuje go w ramce 4:5 o szerokości do 200 px (punkt „Stan dziś”), więc to zapas 3×.
- **Wyostrzanie:** klasyczne (etap 3). Generatywne „poprawianie twarzy” jest zakazane.
- **Znaki wodne, pieczątki, podpisy na zdjęciu:** nie usuwamy ich i nie retuszujemy. Kadr może je ominąć, jeśli leżą poza nim.
- **Za małe źródło:** kadr 4:5 w źródle musi mieć co najmniej 200 px wysokości. Poniżej zostaje portret zastępczy, a osoba trafia do raportu („potrzebny większy oryginał”). Według zestawienia dotyczy to Bożejki (120×160). Wolibner nie ma żadnego pliku.
- **Tabisz:** zdjęcie redaktora zastępuje nowy kadr. Jeśli `tabisz-1.jpg` to to samo zdjęcie co profil IM UWr (wariant 18), robisz kadr z większego z dwóch plików. Stare pliki `tabisz.jpg` i `tabisz-1.jpg` zostają w repozytorium.
- **Podpis pod portretem:** krótki („Fot. Konrad Jacobs / MFO, CC BY-SA 2.0 DE”, „Fot. Archiwum UWr”), a pełny opis z linkami i licencją jest na stronie „O stronie”. Strona sama zdejmuje „Fot.” wpisane na początku pola, żeby nie wyszło „Fot. Fot.” (etap 5).
- **Kolor:** zdjęcia barwne zostają barwne. Czarno-białe z zażółceniem skanu dostają neutralną szarość. Bez koloryzowania.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- Raport `RAPORT-ZLECENIE-55.md`, zrzuty `raport-zrzuty/z55-*`. Bez subagentów.
- **Pliki robocze poza repozytoriami:** `.przekazanie\robocze\55-portrety\`, czyli oryginały, `zrodla.json`, `kadry.json`, skrypt `portrety.py` i arkusz porównawczy. Oryginałów nie commituj nigdzie (rozmiar i prawa). Do repozytorium idą tylko gotowe pliki 600×750.
- **Repozytoria:**
  - **Web-Core:** podpis (etap 5), opis pól w `skrypty/migracja/formularze_40.mjs`, ściągawka;
  - **Web-Instytut:** pliki portretów, dwie linie w każdej podłączanej sylwetce, dwa opisy pól w `.pages.yml`;
  - **Web-Ustawienia:** `src/content/strony/o-stronie.md`.
- **Ochrona zmian redaktorów** (jak w zleceniach 31, 40, 47, 52–54). Redaktorzy właśnie edytują sylwetki.
  - Pracuj od świeżego `main`, zwykłym commitem, bez force-push. Bazą jest HEAD zanotowany na początku pracy.
  - Zmiany robi skrypt w miejscu, linia po linii. Nie zapisuj całego YAML od nowa (Pages CMS formatuje pliki po swojemu, np. Tabisz).
  - Tuż przed pushem zrób `git fetch` i `git log <baza>..origin/main`. Jeśli redaktor zmienił któryś z plików, uruchom skrypt jeszcze raz na świeżym `main`.
  - Kontrola przed pushem i po nim: w każdej sylwetce zmieniły się tylko linie `obraz` i `obraz_zrodlo` w `karta`, a w `o-stronie.md` tylko nowy fragment z etapu 6. Wynik wpisz do raportu.
  - Push zrób wieczorem albo po wiadomości właściciela do redaktorów („zapiszcie i zamknijcie CMS na 15 minut”).
- **Kolejność:**
  - **po zleceniu 53**, bo oba zmieniają `src/views/SylwetkaWW.astro`;
  - z 54 w dowolnej kolejności, bo zmienia inne linie tych samych plików Web-Instytut (przed pushem rebase i ponowny skrypt);
  - pushe: Web-Core, potem Web-Instytut, potem Web-Ustawienia.

## Stan dziś (Web-Core `b3ece9f` / `main` z 19.11, 00:24; Web-Instytut `d6b936d`; Web-Ustawienia `1fb08e6`)

- **Sylwetki** (`Web-Instytut/src/content/warto_wiedziec/sylwetki/*.md`, 18 plików):
  - 17 ma w `karta:` linie `  obraz: ""` i `  obraz_zrodlo: ""` (zwykle linie 24–25);
  - Tabisz ma `  obraz: /pliki/warto-wiedziec/tabisz-1.jpg` (240×240, 8098 B; `tabisz.jpg` to ten sam plik), bez linii `obraz_zrodlo`, a YAML jest sformatowany przez Pages CMS.
- **Formularz** (`Web-Instytut/.pages.yml`, `ww_sylwetki` → `karta`):
  - „Zdjęcie” (`obraz`): typ `image`, media `public/pliki/warto-wiedziec`, opis „Portret, tylko z prawem do publikacji. Puste = sylwetka zastępcza.”;
  - „Źródło zdjęcia” (`obraz_zrodlo`): opis z przykładem „Fot. Jan Kowalski, CC BY-SA 4.0”;
  - te same teksty są w `Web-Core/skrypty/migracja/formularze_40.mjs` (ok. linii 264–265).
- **Wyświetlanie** (Web-Core):
  - `portretHtml` (`src/lib/wartoWiedziec.ts`) daje `<img alt="">` w `.ww2-portret`;
  - `src/styles/warto-wiedziec.css`: `aspect-ratio: 4 / 5`, `object-fit: cover`, `object-position: 50% 30%`;
  - strona osoby: kolumna portretu 200 px (`.ww2-prof-l`), zdjęcie bez filtra;
  - siatka sylwetek: kolumny od 132 px (mała siatka od 112 px). Zdjęcie jest szare z tonem złota, a kolor wraca po najechaniu;
  - mini portret w `:::laureaci` (`.ww2-mini`): kółko 30 px, kwadrat z obrazu 4:5 przy `object-position 50% 30%`;
  - pole `obraz` służy też jako obraz strony (`Podstrona obraz=…`, podgląd linku).
- **Podpis:** `SylwetkaWW.astro` wypisuje `{T('Fot.', 'Photo:')} {w.obraz_zrodlo}` tylko na stronie osoby i tylko przy zdjęciu. Pole wpisane zgodnie z przykładem z CMS dałoby „Fot. Fot. …”.
- **„O stronie”** (`Web-Ustawienia/src/content/strony/o-stronie.md`):
  - PL w treści, EN w `tresc_en`;
  - sekcja `## Źródła ilustracji {#źródła-ilustracji}` (EN `## Image sources {#image-sources}`) ma 3 punkty: szkice patronów, podpisy i zdjęcie kampusu („fragment, wyostrzony”).

## Docelowo

### Etap 1. Pobranie (oryginały do `.przekazanie\robocze\55-portrety\oryginaly\`)
- Pobierz każdy wariant z załącznika A (link „Plik”). Nazwa pliku: `<slug>-<wariant>.<rozszerzenie>`, np. `edward-marczewski-2b.jpg`.
- **Jeśli link do pliku nie działa** (404, blokada, wygasły link podręczny, np. 8b), otwórz „Stronę źródłową” i weź z niej to samo zdjęcie w największej dostępnej wersji. Inne zdjęcie albo inne źródło nie wchodzi: wariant odpada, zapisz to w raporcie.
- **Tożsamość:** sprawdź na stronie źródłowej, że zdjęcie przedstawia właściwą osobę. Zestawienie ostrzega przed pomyłkami: ojciec Rylla-Nardzewskiego oraz fizyk André Krzywicki.
- **`zrodla.json`:** dla każdego wariantu osoba, wariant, URL pliku, strona źródłowa, data pobrania, sha256 i rzeczywiste wymiary. Rozbieżności z zestawieniem (wymiary, autor albo licencja na karcie źródła) wpisz do raportu.

### Etap 2. Wybór wariantu (osoby z dwoma wariantami: 2, 3, 4, 8, 13, 14)
Kryteria, w tej kolejności:
1. twarz wyraźna, ostra i dobrze oświetlona, en face albo trzy czwarte;
2. rozmiar: wysokość kadru 4:5 w pikselach źródła (im bliżej 750, tym lepiej; poniżej 200 wariant odpada);
3. bez znaku wodnego, mocnego cienia na twarzy i przesłonięć w obrębie kadru;
4. portret pasuje do siatki: popiersie, spokojne tło, nie scena ani tablica;
5. przy porównywalnej jakości: wolna licencja albo domena publiczna przed wariantem bez licencji.

**Arkusz porównawczy** `raport-zrzuty/z55-wybor.html` (i zrzut PNG): jeden wiersz na osobę. W wierszu:
- wszystkie warianty, każdy z wymiarami i licencją;
- zaznaczony kadr na wybranym wariancie;
- gotowy plik 600×750 i jego podgląd 200×250;
- przy powiększeniu ponad 2× wariant B, jeśli powstał (etap 3).

Na końcu arkusza: siatka wszystkich portretów 4:5 obok siebie, w kolorze i w szarości jak na stronie. Na niej widać, czy kadry są równe. Właściciel może przy odbiorze napisać „dla X weź wariant b”, a skrypt odtworzy wynik z `kadry.json`.

### Etap 3. Kadr i obróbka (`portrety.py`, ustawienia w `kadry.json`, wynik powtarzalny z oryginałów)
**Kadr 4:5, jednakowy dla wszystkich**, żeby siatka była równa:
- oczy na 36–40% wysokości kadru od góry;
- głowa (od czubka włosów do brody) zajmuje 42–52% wysokości kadru; różnica między osobami jest jak najmniejsza;
- nad głową 6–12% wolnego miejsca. Czubka głowy ani brody nie ucinamy;
- twarz na środku w poziomie, a przy półprofilu przesunięta o 5–8% w stronę tyłu głowy, żeby przed twarzą było więcej miejsca;
- kwadrat od 6% wysokości w dół (mini portret 30 px) mieści całą twarz;
- prostowanie do ±3°, jeśli zdjęcie jest wyraźnie krzywe;
- jeśli źródło jest ciaśniejsze (np. kwadrat 240 px), głowa może być większa niż 52%. Tła i marginesów nie dorabiamy.

`kadry.json`: dla każdej osoby wariant, prostokąt w źródle (x, y, szerokość, wysokość), obrót i ustawienia obróbki.

**Obróbka, w tej kolejności:**
1. **Raster druku i szum:** tylko tam, gdzie je widać (np. Steinhaus, reprodukcja z księgi): lekkie odszumienie przed skalowaniem. Sprawdź mory przy 100% i 200%.
2. **Tonalność:** poziomy z obcięciem najwyżej 0,5% na końcach, ewentualnie gamma. Czarno-białe z barwnym nalotem zamień na neutralną szarość. Barwne zostają barwne, z korektą balansu bieli tylko przy wyraźnym zafarbie.
3. **Skalowanie** do 600×750 metodą Lanczos. Współczynnik = 750 / wysokość kadru w źródle; wpisz go do raportu. Powyżej 3× oznacz zdjęcie „słaba jakość, potrzebny większy oryginał”.
4. **Wyostrzenie** (unsharp mask) po skalowaniu:
   - przy pomniejszaniu łagodne (np. promień 0,6–0,8 px, siła 40–60%, próg 2);
   - przy powiększaniu mocniejsze (np. promień 1–1,5 px, siła 60–100%);
   - bez obwódek (halo) wokół konturów, bez wzmacniania szumu, ziarna skanu i znaku wodnego;
   - oceniaj przy 100% i 200%.
5. **Zapis:** JPEG, jakość ok. 85, progresywny, sRGB, bez EXIF i innych metadanych, najwyżej 150 KB.

**Wariant B (opcjonalnie), tylko przy powiększeniu ponad 2×:**
- Real-ESRGAN z ogólnym modelem `realesrgan-x4plus` (nie `anime`), np. przenośny `realesrgan-ncnn-vulkan` w `.przekazanie\robocze\`, bez instalacji w systemie. Jeśli się nie uruchomi, pomiń wariant B i napisz to w raporcie.
- Wynik przechodzi kroki 3–5 i trafia do arkusza obok wariantu A.
- Domyślnie wygrywa A. B wybierz tylko wtedy, gdy jest wyraźnie lepszy i nie zmienia rysów twarzy; uzasadnij to w raporcie.

**Zakazy:** modele „naprawy twarzy” (GFPGAN, CodeFormer i podobne), inpainting, usuwanie znaków wodnych, pieczątek i podpisów, retusz rysów twarzy, koloryzowanie.

### Etap 4. Podłączenie do sylwetek (Web-Instytut)
- **Pliki:** `public/pliki/warto-wiedziec/portrety/<slug>.jpg`, gdzie `slug` to nazwa pliku sylwetki.
- **W sylwetce zmieniają się tylko dwie linie w `karta:`:**
  - `  obraz: /pliki/warto-wiedziec/portrety/<slug>.jpg`;
  - `  obraz_zrodlo: "<podpis z załącznika A>"`. U Tabisza tej linii nie ma: dopisz ją zaraz pod `obraz:`, z tym samym wcięciem.
- **Gdy na świeżym `main` linia ma inną wartość niż oczekiwana**, nie nadpisuj jej. Oczekiwane wartości: `obraz: ""` i `obraz_zrodlo: ""`, a u Tabisza `obraz: /pliki/warto-wiedziec/tabisz-1.jpg`. Inna wartość znaczy, że redaktor wstawił zdjęcie albo źródło. Wypisz to w raporcie i zostaw do decyzji właściciela.
- **Bez zmian:** Wolibner i każda osoba poniżej progu 200 px (domyślnie Bożejko). Zostaje portret zastępczy.
- Żadnych innych zmian w plikach sylwetek, także w `opublikowany` i `dodano`.

### Etap 5. Podpis i opisy pól
- **`SylwetkaWW.astro`:** zanim wypiszesz `obraz_zrodlo`, zdejmij z jego początku „Fot.”, „Fot:”, „Foto:”, „Photo:” albo „Photo” (bez względu na wielkość liter, razem ze spacjami). Prefiks `T('Fot.', 'Photo:')` zostaje, więc zawsze jest dokładnie jeden. Dodaj komentarz z odwołaniem do zlecenia 55.
- **Opis pola „Źródło zdjęcia”** (`.pages.yml` Web-Instytut i `formularze_40.mjs`, ten sam tekst):
  > Krótko, bez „Fot.” (strona dopisuje je sama): autor albo instytucja i licencja, np. „Konrad Jacobs / MFO, CC BY-SA 2.0 DE” albo „Archiwum UWr”. Pokazuje się drobno pod portretem na stronie osoby. Pełny opis z linkiem i licencją dopisz na stronie „O stronie” (Web-Ustawienia). Puste = bez podpisu.
- **Opis pola „Zdjęcie”** (w tych samych dwóch miejscach):
  > Portret pionowy 4:5, najlepiej 600×750 px (co najmniej 400×500), oczy na ok. 2/5 wysokości od góry. Tylko z prawem do publikacji. Puste = sylwetka zastępcza.
- **`.pages.yml`:** zmień tylko te dwie linie `description`, bez generatora, bo właściciel edytuje ten plik ręcznie. Opisy z cudzysłowem albo dwukropkiem weź w cudzysłów. Plik ma się parsować, a `sprawdz_pola_cms.py` ma dać 0 problemów.
- **Ściągawka** (`dok/sciagawka-edytora.md`, część „Warto wiedzieć”, punkt „Sylwetka”), zdanie: „Portret: 4:5, najlepiej 600×750 px; »Źródło zdjęcia« krótko, bez »Fot.«; pełne źródło z linkiem i licencją na stronie »O stronie«.”

### Etap 6. „O stronie” (Web-Ustawienia, PL w treści i EN w `tresc_en`)
- W sekcji „Źródła ilustracji” / „Image sources”, po punkcie o zdjęciu kampusu, dodaj śródtytuł:
  - PL: `### Portrety w „Warto wiedzieć” {#portrety}`;
  - EN: `### Portraits in “Did you know” {#portrety}`.
- Pod nim jedno zdanie:
  - PL: „Portrety na stronach sylwetek, w kolejności nazwisk. Zdjęcia na licencjach CC BY-SA są tu udostępniane w zmienionej wersji na tej samej licencji.”
  - EN: zdanie o tej samej treści.
- **Lista:** jedna linia na osobę ze zdjęciem, w kolejności nazwisk, według wzoru:

  `- **Imię Nazwisko** — <autor albo „autor nieznany”, jeśli źródło tak podaje>, <opis i rok, jeśli są w załączniku A>, [<serwis albo instytucja>](<strona źródłowa>), <licencja>; <zmiany>.`

  - **Licencja:**
    - CC jako link do deed, na stronie PL wersja `deed.pl`, na EN `deed.en`: `https://creativecommons.org/licenses/by-sa/2.0/de/…`, `…/by-sa/2.5/…`, `…/by-sa/3.0/…`, `…/by-sa/3.0/pl/…`;
    - domena publiczna: „domena publiczna” / „public domain”;
    - bez licencji: nic nie wpisuj.
  - **Zmiany:** „kadr” / „kadr, wyostrzenie” / „kadr, powiększenie i wyostrzenie” (EN „cropped” / „cropped and sharpened” / „cropped, enlarged and sharpened”), zgodnie z tym, co naprawdę zrobił skrypt.
  - **Nigdy żadnych wypełniaczy** typu „[autor do ustalenia]”. Brakujący autor po prostu nie występuje, a sprawa trafia do raportu.
  - Linie generuj z `zrodla.json` i `kadry.json`, a nie ręcznie.
- Pozostałe sekcje i istniejące `{#id}` bez zmian. `sprawdz-jawny-markdown.mjs` (Web-Ustawienia) ma przejść.

## Odbiór lokalny
- **Budowa PL i EN**, porównanie HTML przed i po. Dozwolone różnice:
  - portret i podpis na stronach osób ze zdjęciem;
  - portrety w siatkach sylwetek (lista „Warto wiedzieć”, „Inne sylwetki”, „Sylwetki laureatów”, „Ludzie w tej historii”), mini portrety w `:::laureaci` i karty „Warto wiedzieć” na stronie głównej;
  - obraz strony (podgląd linku) na stronach osób;
  - „O stronie”;
  - indeks wyszukiwarki.

  Każdą inną różnicę zgłoś.
- **Zrzuty:**
  - lista „Warto wiedzieć” (siatka sylwetek): 1920×1080 w trybie jasnym i ciemnym oraz 390 px;
  - strony osób przy 1920×1080 i 390 px: Steinhaus, Knaster, Biler, Tabisz i osoba z największym powiększeniem;
  - Medal UWr z mini portretami laureatów;
  - strona główna z kartą „Warto wiedzieć” z portretem;
  - „O stronie” PL i EN, z widocznym fragmentem o portretach.
- **Kontrole:**
  - każdy plik ma 600×750, najwyżej 150 KB i nie ma EXIF;
  - w `dist` nigdzie nie ma „Fot. Fot.” ani „Photo: Photo”;
  - linki z „O stronie” do stron źródłowych odpowiadają (wystarczy kod HTTP);
  - `astro check` bez nowych błędów, testy zielone;
  - `sprawdz_tresci.py`, `sprawdz_pola_cms.py`, `sprawdz-jawny-markdown.mjs` (Web-Instytut, Web-Ustawienia) bez problemów;
  - konsola czysta.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Każda osoba z użytecznym źródłem ma portret 600×750 (4:5) z równym kadrem: oczy na tej samej wysokości, podobna wielkość głowy, cała twarz także w mini portrecie.
- [ ] Wybór wariantów i obróbka są w arkuszu `z55-wybor.html`, a wynik da się odtworzyć z oryginałów (`portrety.py` i `kadry.json`).
- [ ] Bez generatywnej naprawy twarzy, usuwania znaków wodnych i koloryzowania.
- [ ] W sylwetkach zmieniły się tylko `karta.obraz` i `karta.obraz_zrodlo`. Zapisy redaktorów są zachowane (kontrola przed pushem i po nim).
- [ ] Pod portretem jest jeden „Fot.”/„Photo:” i krótki podpis. Opisy pól „Zdjęcie” i „Źródło zdjęcia” są w CMS i w generatorze zgodne, a ściągawka mówi to samo.
- [ ] „O stronie” (PL i EN) ma źródło, licencję i zmiany każdego portretu, bez wypełniaczy.
- [ ] Raport ma listę „zgody przed startem”.

## Do raportu
- **Tabela osób:** wybrany wariant, wymiary źródła, prostokąt kadru, współczynnik skali, wariant A/B, rozmiar pliku, status praw (wolna licencja / domena publiczna / brak licencji).
- **Odrzucone warianty** z powodem. Osoby bez zdjęcia (Wolibner, osoby poniżej progu) i zdjęcia „słaba jakość”.
- **Rozbieżności** z zestawieniem: wymiary, autor (np. pisownia „Czerwńska” na karcie Commons w wariancie 13a), licencja.
- **Zgody przed startem:** dla każdego wybranego zdjęcia bez wolnej licencji osoba, wariant, do kogo pisać (załącznik B) i o co prosić. Prośba obejmuje zgodę na publikację w wersji wykadrowanej i wyostrzonej, autora zdjęcia i, gdzie warto, większy skan. Osobno osoby żyjące (Krzywicki, Duda, Narkiewicz, Biler, Bożejko, Rolski, Tabisz): zgoda na wizerunek razem z akceptacją tekstu.
- **Propozycja:** jedno pismo do Archiwum UWr o większe skany i prawa (Marczewski, Knaster, Ślebodziński, Hartman, Wolibner, ewentualnie Perkal z inwentarza). Tylko tekst do decyzji właściciela, bez wysyłania.
- **Nieużywane pliki** w `public/pliki/warto-wiedziec/` (`tabisz.jpg`, `tabisz-1.jpg`): tylko lista, bez usuwania.

## Załącznik A: kandydaci

Kolumna „Podpis” to wartość pola „Źródło zdjęcia”, bez „Fot.”. „Opis” to dane do wiersza na stronie „O stronie”.

| Sylwetka (`slug`) | Wariant | Plik | Strona źródłowa | Autor / prawa | Licencja | Wymiary | Podpis | Opis i uwagi |
|---|---|---|---|---|---|---|---|---|
| `hugo-steinhaus` | 1 | https://upload.wikimedia.org/wikipedia/commons/3/36/Hugo_Steinhaus.jpg | https://commons.wikimedia.org/wiki/File:Hugo_Steinhaus.jpg | autor nieznany | domena publiczna (PD-Poland według Commons) | 1659×2481 | Wikimedia Commons | reprodukcja z księgi pamiątkowej, 1968; faktura druku |
| `edward-marczewski` | 2a | https://upload.wikimedia.org/wikipedia/commons/4/4d/Edward_Marczewski.jpg | https://commons.wikimedia.org/wiki/File:Edward_Marczewski.jpg | Konrad Jacobs, Archives of the Mathematisches Forschungsinstitut Oberwolfach | CC BY-SA 2.5 | 285×400 | Konrad Jacobs / MFO, CC BY-SA 2.5 | Wrocław, 1967; półprofil, mała twarz |
| `edward-marczewski` | 2b | https://mbd.muzeum.uwr.edu.pl/assets/uploads/s467/5d53b-marczewski_www.jpg | https://mbd.muzeum.uwr.edu.pl/dzieje-uniwersytetu/profesorowie-po-1945-r/edward-marczewski | autor niepodany; ze zbiorów Archiwum UWr (Muzeum UWr) | brak jawnej licencji | 467×570 | Archiwum UWr | lepsza kompozycja |
| `bronislaw-knaster` | 3a | https://upload.wikimedia.org/wikipedia/commons/b/b6/Bronislaw_Knaster.jpeg | https://commons.wikimedia.org/wiki/File:Bronislaw_Knaster.jpeg | Konrad Jacobs / MFO | CC BY-SA 2.0 DE | 365×270 | Konrad Jacobs / MFO, CC BY-SA 2.0 DE | półprofil, znak wodny |
| `bronislaw-knaster` | 3b | https://mbd.muzeum.uwr.edu.pl/assets/uploads/s467/3c39f-knaster_bronislaw-www.jpg | https://mbd.muzeum.uwr.edu.pl/dzieje-uniwersytetu/profesorowie-po-1945-r/bronisaw-knaster | autor niepodany; ze zbiorów Archiwum UWr (Muzeum UWr) | brak jawnej licencji | 467×570 | Archiwum UWr | dobra kompozycja portretowa |
| `wladyslaw-slebodzinski` | 4a | https://upload.wikimedia.org/wikipedia/commons/1/17/W%C5%82adys%C5%82aw_%C5%9Alebodzi%C5%84ski.jpg | https://commons.wikimedia.org/wiki/File:W%C5%82adys%C5%82aw_%C5%9Alebodzi%C5%84ski.jpg | autor nieznany; kolekcja rodzinna | domena publiczna według Commons (PD-Poland; podstawa niepełna) | 502×634 | Wikimedia Commons | 4 lipca 1938; na „O stronie” napisz „oznaczone w Wikimedia Commons jako domena publiczna” |
| `wladyslaw-slebodzinski` | 4b | https://mbd.muzeum.uwr.edu.pl/assets/uploads/s467/5b1dd-slebodzinski_www.jpg | https://mbd.muzeum.uwr.edu.pl/dzieje-uniwersytetu/profesorowie-po-1945-r/wadysaw-lebodziski | autor niepodany; ze zbiorów Archiwum UWr (Muzeum UWr) | brak jawnej licencji | 467×570 | Archiwum UWr | późniejszy portret en face, okulary |
| `witold-wolibner` | — | brak pliku | https://archiw.uwr.edu.pl/wp-content/uploads/sites/114/2025/04/Album_XX_Fotografie_inwentarz.pdf | Archiwum UWr | — | — | — | portret zastępczy; skan: Album Dwudziestolecia UWr 1945–1965, poz. 334, s. 25, zdjęcie 35 |
| `julian-perkal` | 6 | https://ptb.up.poznan.pl/sites/default/files/styles/large/public/2022-09/memoriesPerkal.jpg?itok=JPUpe_UR | https://ptb.up.poznan.pl/index.php/wspomnienia_1 | autor niepodany; Polskie Towarzystwo Biometryczne | brak jawnej licencji | 211×301 | Polskie Towarzystwo Biometryczne | małe; sprawdź, czy strona źródłowa ma większą wersję |
| `stanislaw-hartman` | 7 | https://mbd.muzeum.uwr.edu.pl/assets/uploads/profesorowie/5e705-hartman_stanislaw.jpg | https://mbd.muzeum.uwr.edu.pl/dzieje-uniwersytetu/profesorowie-po-1945-r/stanisaw-hartman | autor niepodany; ze zbiorów Archiwum UWr (Muzeum UWr) | brak jawnej licencji | 667×1000 | Archiwum UWr | sam portret ok. 400×550 w skanie, szerokie marginesy |
| `czeslaw-ryll-nardzewski` | 8a | https://opc.mfo.de/photoNormal?id=3616 | https://opc.mfo.de/detail?photo_id=3616 | Konrad Jacobs, Archives of the Mathematisches Forschungsinstitut Oberwolfach | CC BY-SA 2.0 DE (mała wersja ze znakiem wodnym) | 307×400 | Konrad Jacobs / MFO, CC BY-SA 2.0 DE | Warszawa, 1977; mocny cień, znak wodny |
| `czeslaw-ryll-nardzewski` | 8b | https://crn.pwr.edu.pl/files/cache/286/en/17/1811157/cGBUKOTtQKxVvAkxuREFBPF0WUXJ9WkFABWdbEwMZWGFBVgo7RgMpVjlDEXRKEEMAFkhRP25BTw82LAUTXEZCfFIGT3FIGT3xIGywVbxIQPQ4CRA9AUF9qP09XQAcmGQJeQAH5UA5YNg/portret.webp | https://crn.pwr.edu.pl/en/ryll-nardzewski-center/legacy | autor niepodany; Centrum Rylla-Nardzewskiego, Politechnika Wrocławska | brak jawnej licencji | 387×439 | Centrum Rylla-Nardzewskiego PWr | en face; link do pliku może wygasnąć (etap 1) |
| `kazimierz-urbanik` | 9 | https://upload.wikimedia.org/wikipedia/commons/9/9f/1981-02-27_uczestnicy_Urbanik001.jpg | https://commons.wikimedia.org/wiki/File:1981-02-27_uczestnicy_Urbanik001.jpg | Ryszard Świtacz; archiwum Henryka Zielińskiego | CC BY-SA 3.0 | 569×989 | Ryszard Świtacz, CC BY-SA 3.0 | 27 lutego 1981 |
| `jan-mycielski` | 10 | https://uwr.edu.pl/wp-content/uploads/2025/01/Jan.jpg | https://uwr.edu.pl/en/professor-jan-mycielski-passed-away/ | archiwum prywatne, za Uniwersytetem Wrocławskim | brak jawnej licencji | 591×902 | archiwum prywatne / UWr | portret przy książkach |
| `andrzej-hulanicki` | 11 | https://upload.wikimedia.org/wikipedia/commons/c/c2/Andrzej_Hulanicki.jpg | https://commons.wikimedia.org/wiki/File:Andrzej_Hulanicki.jpg | Konrad Jacobs / MFO | CC BY-SA 2.0 DE | 265×400 | Konrad Jacobs / MFO, CC BY-SA 2.0 DE | portret z tułowiem; po kadrze mały |
| `andrzej-krzywicki` | 12 | https://math.uni.wroc.pl/sites/default/files/styles/240x240/public/pictures/picture-234-1456484753.jpg?itok=ah4xvBNE | https://math.uni.wroc.pl/users/krzywick | autor niepodany; Instytut Matematyczny UWr | brak jawnej licencji | 240×240 | IM UWr | matematyk z Wrocławia, nie fizyk André Krzywicki |
| `roman-duda` | 13a | https://upload.wikimedia.org/wikipedia/commons/0/03/Senatorowie_I_kadencji_2014_%28Romand_Duda_cropped%29.jpg | https://commons.wikimedia.org/wiki/File:Senatorowie_I_kadencji_2014_(Romand_Duda_cropped).jpg | autor jak na karcie Commons („Katarzyna Czerwńska”), Kancelaria Senatu RP | CC BY-SA 3.0 PL | 213×298 | `<autor z karty> / Kancelaria Senatu, CC BY-SA 3.0 PL` | 2014; bardzo małe |
| `roman-duda` | 13b | https://www.cmf.p.lodz.pl/sites/cmf/files/styles/fix_max_1300x1300/public/2025-07/dudaMatematyk.png | https://www.cmf.p.lodz.pl/aktualnosci/profesor-roman-duda-90-lat-zycia-z-matematyka | autor niepodany; Centrum Nauczania Matematyki i Fizyki Politechniki Łódzkiej | brak jawnej licencji | 1011×719 | Politechnika Łódzka | najlepsza jakość |
| `wladyslaw-narkiewicz` | 14a | https://upload.wikimedia.org/wikipedia/commons/9/99/Wladyslaw_Narkiewicz.jpg | https://commons.wikimedia.org/wiki/File:Wladyslaw_Narkiewicz.jpg | Konrad Jacobs / MFO | CC BY-SA 2.0 DE | 278×400 | Konrad Jacobs / MFO, CC BY-SA 2.0 DE | 1976, postać siedząca, mała twarz |
| `wladyslaw-narkiewicz` | 14b | https://cs.uwaterloo.ca/~shallit/MMF/narkiewicz.jpg | https://cs.uwaterloo.ca/~shallit/mmf.html | autor niepodany; galeria Jeffreya Shallita, University of Waterloo | brak jawnej licencji | 400×510 | galeria J. Shallita, University of Waterloo | Colloque Mendès France, Bordeaux 2000; przy tablicy |
| `piotr-biler` | 15 | https://pan.pl/app/uploads/2023/12/Biler_Piotr_03-1024x683.jpg | https://pan.pl/czlonkowie/piotr-biler/ | autor niepodany; Polska Akademia Nauk | brak jawnej licencji | 1024×683 | PAN | jasny portret, dobry zapas |
| `marek-bozejko` | 16 | https://www.math.uni.wroc.pl/sites/default/files/styles/120x160/public/bozejko_0.jpg?itok=KnbMaYBf | https://www.math.uni.wroc.pl/sukcesy | autor niepodany; Instytut Matematyczny UWr | brak jawnej licencji | 120×160 | IM UWr | poniżej progu: domyślnie bez zdjęcia |
| `tomasz-rolski` | 17 | https://www.math.uni.wroc.pl/~rolski/Images/PIC00007.jpg | https://www.math.uni.wroc.pl/~rolski/ | autor niepodany; strona domowa Tomasza Rolskiego | brak jawnej licencji | 1280×1024 | ze strony T. Rolskiego | duży zapas |
| `krzysztof-tabisz` | 18 | https://www.math.uni.wroc.pl/sites/default/files/styles/240x240/public/pictures/picture-129-1431991755.jpg?itok=EpIZGWVA | https://www.math.uni.wroc.pl/users/tabisz | autor niepodany; Instytut Matematyczny UWr | brak jawnej licencji | 240×240 | IM UWr | porównaj z `tabisz-1.jpg` (Web-Instytut) |

**Oberwolfach (warianty 2a, 3a, 8a, 11, 14a).** Regulamin [Oberwolfach Photo Collection](https://opc.mfo.de/terms_of_use) daje CC BY-SA 2.0 DE dla małych wersji ze znakiem wodnym. Pełna rozdzielczość i pliki bez znaku wodnego wymagają zgody MFO (photos@mfo.de). Pliki z Wikimedia Commons oceniamy według ich kart. Większych wersji z MFO nie pobieraj.

## Załącznik B: kontakty do zgód (do raportu, nic nie wysyłaj)
- **Marczewski, Knaster, Ślebodziński (4b), Hartman:** Archiwum UWr, auw@uwr.edu.pl. Ustalić fotografa, prawo do publikacji i większy skan.
- **Wolibner:** Archiwum UWr, auw@uwr.edu.pl; *Album Dwudziestolecia UWr 1945–1965*, poz. 334, s. 25, zdjęcie 35. Najpierw skan.
- **Ślebodziński (4a, Commons):** wyjaśnić podstawę domeny publicznej z użytkownikiem Wtslebo albo z rodziną.
- **Perkal:** Polskie Towarzystwo Biometryczne, katarzyna.ambrozy-deregowska@up.poznan.pl (oryginał i prawa). Alternatywnie Archiwum UWr, inwentarz poz. 221, s. 24, zdjęcie 21.
- **Ryll-Nardzewski (8b):** Centrum Rylla-Nardzewskiego, crn@pwr.edu.pl (autor, większy plik).
- **Mycielski:** redakcja UWr albo webmaster@math.uni.wroc.pl (kontakt do osoby z prawami do zdjęcia z archiwum prywatnego).
- **Krzywicki:** Andrzej.Krzywicki@math.uni.wroc.pl albo webmaster@math.uni.wroc.pl (oryginał i potwierdzenie praw).
- **Duda (13b):** Centrum Nauczania Matematyki i Fizyki PŁ, cmf@adm.p.lodz.pl (autor i zgoda).
- **Narkiewicz (14b):** Jeffrey Shallit, galeria University of Waterloo (autor i zgoda uprawnionego).
- **Biler:** Polska Akademia Nauk, media@pan.pl (wskazać zdjęcie z profilu członka PAN).
- **Bożejko:** Marek.Bozejko@math.uni.wroc.pl albo webmaster@math.uni.wroc.pl (przede wszystkim większe zdjęcie).
- **Rolski:** rolski@math.uni.wroc.pl (autor, zgoda na publikację i kadr).
- **Tabisz:** Krzysztof.Tabisz@math.uni.wroc.pl albo webmaster@math.uni.wroc.pl (większy oryginał i potwierdzenie praw).
- **Oberwolfach:** photos@mfo.de, tylko gdyby właściciel chciał większych plików Jacobsa.
