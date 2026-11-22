# Zlecenie 32: menu z hamburgera na komputerze jako zwarta lista pod przyciskiem, nie panel na całą wysokość; orzeł UWr prowadzi do UWr (17.11.2026)

**Decyzja właściciela (17.11, 21:43):** „hamburger w wersji PC na całą wysokość okna jest za duży. Zrobimy mniejszy, pojawiający się przy hamburger menu, a nie na całą wysokość z prawej. I zajmuje tyle miejsca, ile zajmuje tekst, nie rozciąga się sztucznie.”

**Dopisane 17.11, 21:50 (punkt 8):** „Orzełek w navbarze prowadzi na stronę wydziału, a nie na stronę UWr.”

**Dopisane 18.11, 11:36 (punkt 9, po obejrzeniu wyniku):** „Aktualności i Rekrutacja są troszkę za ciasno. Zrób im taki sam odstęp separatorów co przy pozostałych.” Jeśli punkty 1–8 są już zrobione, dołóż punkt 9 osobnym commitem.

**Zakres:**
- **Punkty 1–7:** tylko komputer, czyli warunek `@media (min-width: 1024px) and (min-height: 501px), (min-width: 1024px) and (pointer: fine)` w `src/styles/zal-menu.css`.
- **Telefon (< 1024 px):** bez zmian. Wysuwany panel spod nagłówka zostaje, jak w zleceniu 18.
- **Punkt 8:** okładka i pasek menu.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push na `main` dopiero po „push” właściciela.
- Raport `RAPORT-ZLECENIE-32.md`, zrzuty `raport-zrzuty/z32-*`.
- Bez subagentów.

## Stan dziś
- **Pliki panelu:**
  - komponent `src/components/zal/PanelMenu.astro`, ten sam na okładce i przy pasku menu;
  - style `src/styles/zal-menu.css`;
  - otwieranie `src/scripts/zal/menu.ts`.
- **Przyciski:** `.z-burger[data-z-menu-otworz]` w `PasekMenu.astro` (linia 59) i w `Okladka.astro` (linia 157).
- **Na komputerze** (`zal-menu.css`, ok. linii 74–145):
  - `.z-menu` ma `position: absolute` (przy pasku `fixed`) oraz `top: 0; right: 0; bottom: 0`, czyli zajmuje całą wysokość okna przy prawej krawędzi;
  - szerokość `min(610 → 670 px, 100vw − 64px)`, `display: flex; flex-direction: column`;
  - sekcje mają `flex: 1 0 auto`, więc dzielą wolną wysokość między siebie i panel rozciąga się sztucznie;
  - wielkości (`--mw`, `--m-h2`, `--m-l`, `--m-g`, `--m-s`) rosną z wysokością okna, żeby zapełnić wysokość;
  - krzyżyk `.z-zamknij` stoi 24 px od górnej i prawej krawędzi, a pole „Szukaj” jest w jednym rzędzie z nim.

## Docelowo (komputer)
1. **Zwarta lista pod przyciskiem.**
   - Panel otwiera się tuż pod hamburgerem, który go otworzył: górna krawędź 8 px pod dolną krawędzią przycisku, prawa krawędź równo z prawą krawędzią przycisku.
   - Gdyby się nie mieścił, przesuwa się w lewo, ale zostaje co najmniej 16 px od krawędzi okna.
   - Działa tak samo przy pasku menu (`fixed`, pod paskiem) i na okładce (pod hamburgerem w rogu okładki).
2. **Wielkość według treści, bez rozciągania.**
   - Bez `bottom: 0` i bez `flex: 1 0 auto` w sekcjach: sekcje leżą jedna pod drugą ze stałymi odstępami, a wysokość panelu to wysokość jego treści.
   - Szerokość według treści: tyle, ile potrzebuje najdłuższy wiersz, z górnym limitem.
     - Proponowany limit to `min(560px, 100vw − 32px)`. Dobierz go na zrzutach tak, żeby linki działu łamały się najwyżej w 2–3 wierszach.
     - Bez sztucznego minimum ponad potrzebę treści.
     - Panel nie może się zwężać i rozszerzać przy rozwijaniu działów.
   - Zabezpieczenie na niskim oknie:
     - `max-height` = wysokość okna minus góra panelu minus 16 px;
     - powyżej tej wysokości przewijanie wewnątrz panelu (`overscroll-behavior: contain`).
3. **Stałe wielkości, bez skalowania z wysokością okna.** Usuń zależność od `--mw` na komputerze. Wartości: jak dziś przy pełnej skali, ale wpisane wprost. Jeśli lista wychodzi za duża, zmniejsz o jeden stopień i opisz to w raporcie.
4. **Bez zmian w treści i zachowaniu:**
   - pole „Szukaj” na górze;
   - cztery działy z sygnetem patrona, zwijane: jeden otwarty naraz, przy otwarciu rozwinięty dział bieżącej strony;
   - na dole „Aktualności” i „Rekrutacja ↗” (wysokość wierszy: punkt 9);
   - wersja jasna (`.z-menu-jasny`);
   - Esc i kliknięcie obok zamykają listę, fokus wraca na przycisk, `aria-expanded` na przycisku.
5. **Krzyżyk:**
   - zostaje (dostępność) jako mały przycisk w prawym górnym rogu listy, w jednym rzędzie z polem „Szukaj”, jak dziś, tylko w mniejszej skali;
   - ponowne kliknięcie hamburgera też zamyka listę;
   - jeśli wyjdzie lepiej bez krzyżyka (hamburger zmienia się wtedy w ×), zaproponuj to w raporcie ze zrzutem, ale nie wdrażaj bez decyzji.
6. **Wygląd i ruch:**
   - tło i rozmycie jak dziś (granat 96% z blur, w jasnej wersji jasne), zaokrąglenie 8 px, cień dookoła zamiast cienia w lewo;
   - bez przyciemniania strony;
   - otwieranie: krótkie pojawienie się (ok. 0,18 s, przezroczystość i przesunięcie 6–8 px w dół); przy `prefers-reduced-motion` bez ruchu;
   - rozwijanie działu: płynna zmiana wysokości listy, tą samą techniką grid-rows co dziś.
7. **Kod:**
   - zmiany głównie w `zal-menu.css`;
   - w `menu.ts` liczenie pozycji przy otwarciu i przy zmianie rozmiaru okna, np. zmienne `--menu-x` i `--menu-y` z `getBoundingClientRect()` przycisku;
   - usuń martwe już reguły pełnej wysokości (`--mw` itd.) i zaktualizuj komentarze w nagłówkach plików.

## 8. Orzeł UWr prowadzi do UWr (okładka i pasek menu)
**Stan dziś:**
- **Okładka** (`src/components/zal/Okladka.astro`, ok. linii 144–150):
  - orzeł UWr (`.z-okl-logo`) i nazwa wydziału to **jeden** link `.z-okl-marka`;
  - prowadzi do `WMI_ADRES` = `https://wmi.uwr.edu.pl/` (`src/lib/i18n.ts`, linia 234), więc orzeł prowadzi na stronę wydziału.
- **Pasek menu na podstronach** (`src/components/zal/PasekMenu.astro`, linie 40–43): orzeł (`.z-logo`, `aria-hidden`) i „Instytut Matematyczny / Wydział…” to jeden link `.z-marka` do strony głównej Instytutu.
- **Nagłówek telefonu** (`src/components/Naglowek.astro`, linie 20 i 26): orzeł prowadzi już do `https://uwr.edu.pl/` (EN: `https://uwr.edu.pl/en/`). To wzór.

**Docelowo, jedna reguła wszędzie:**
- orzeł prowadzi do UWr;
- nazwa Wydziału prowadzi do strony Wydziału;
- nazwa Instytutu prowadzi do strony głównej Instytutu.

Jak to zrobić:
- **Okładka:** rozdziel link na dwa.
  - Orzeł → `https://uwr.edu.pl/` (EN: `/en/`), z `aria-label` „Uniwersytet Wrocławski — strona główna” (klucz `uwrStronaGlowna` z i18n, jak w `Naglowek.astro`).
  - Nazwa wydziału → `WMI_ADRES` jak dziś.
  - Oba linki z dopiskiem `sr-only` „(inna strona)” dla czytników, bez widocznej strzałki ↗ (wyjątek z zalecenia 23 zostaje).
- **Pasek menu:** orzeł jako osobny link do UWr, jak wyżej; napis „Instytut Matematyczny” → strona główna Instytutu jak dziś.
- **Wygląd bez zmian:** ten sam układ i odstępy. Obszary kliknięcia orła i napisu nie mogą na siebie nachodzić. Przy najechaniu każdy link podświetla się osobno.
- **Adres UWr w jednym miejscu:** np. `UWR_ADRES` obok `WMI_ADRES` w `src/lib/i18n.ts`. Użyj go też w `Naglowek.astro` zamiast wpisanego tam adresu.

## 9. Równe odstępy przy „Aktualności” i „Rekrutacja” (komputer; dopisane 18.11, 11:36)
**Stan (zrzut właściciela z nowej listy, 18.11):** odległość między separatorami przy wierszach działów to ok. 85 px. Przy „Aktualności” i „Rekrutacja ↗” jest to ok. 58 px, więc te dwa wiersze są wyraźnie ciaśniejsze.

**Docelowo:**
- wiersze „Aktualności” i „Rekrutacja ↗” mają taką samą wysokość jak zwinięty wiersz działu, czyli separatory leżą w równych odstępach przez całą listę;
- tekst wyśrodkowany w pionie; wyrównanie w poziomie bez zmian (równo z nazwami działów); wielkość liter bez zmian;
- wysokość wiersza z jednej zmiennej CSS (np. `--menu-wiersz`) dla działów i obu linków, nie wpisana osobno dwa razy;
- obszar kliknięcia linku obejmuje cały wiersz, nie tylko napis;
- tak samo w wersji jasnej (`.z-menu-jasny`), przy pasku menu i na okładce;
- telefon bez zmian.

## Odbiór lokalny
- **Zrzuty przed/po na komputerze:**
  - rozdzielczości: 1536×864 (domyślny ekran właściciela, skala 1,25), 1920×1080, 1280×720 i 1024×768;
  - w każdej trzy stany: wszystkie działy zwinięte, dział bieżącej strony rozwinięty, wersja jasna;
  - osobno przy pasku menu (podstrona) i na okładce (strona główna).
- **Sprawdź na zrzutach:**
  - góra listy 8 px pod przyciskiem, prawa krawędź równo z przyciskiem;
  - wysokość równa treści: przy zwiniętych działach dół listy wysoko nad dołem okna;
  - brak pustych pasów między sekcjami;
  - przewijanie wewnątrz tylko na niskim oknie (1024×768 i 1280×720 z rozwiniętym działem).
- **Klawiatura:**
  - Tab przechodzi po liście w kolejności;
  - Esc zamyka listę i wraca na hamburger;
  - Tab za ostatnim elementem nie ucieka za listę albo lista się zamyka; opisz, co wybrałeś.
- **Punkt 8:**
  - na okładce i na pasku (PL i EN) orzeł prowadzi do uwr.edu.pl, nazwa wydziału do wmi.uwr.edu.pl, a nazwa Instytutu na stronę główną;
  - Tab trafia na każdy link osobno;
  - wygląd przed/po bez różnic poza podświetleniem przy najechaniu.
- **Punkt 9:** na zrzutach przy zwiniętych działach odległości między kolejnymi separatorami są równe (±1 px) dla wszystkich sześciu wierszy, w każdej z czterech rozdzielczości.
- **Telefon:** menu bez zmian. Porównanie pikselowe 390 px i 768 px przed/po daje 0 różnic, poza punktem 8, gdyby dotknął okładki na telefonie.
- **Kontrole:** konsola bez błędów, `astro check` bez nowych błędów.
- **Stop:** raport ze zrzutami i czekanie na „push”.

## Kryteria odbioru
- [ ] Na komputerze menu otwiera się jako zwarta lista pod hamburgerem (pasek i okładka), a nie jako panel na całą wysokość.
- [ ] Wysokość i szerokość wynikają z treści; sekcje się nie rozciągają; na niskim oknie przewijanie wewnątrz.
- [ ] Stałe wielkości liter i sygnetów, niezależne od wysokości okna.
- [ ] Treść, zwijanie działów, wersja jasna, Esc, kliknięcie obok i fokus działają jak dotąd.
- [ ] Orzeł UWr prowadzi do uwr.edu.pl na okładce, pasku i telefonie; nazwa wydziału do strony wydziału; adres UWr w jednym miejscu kodu.
- [ ] „Aktualności” i „Rekrutacja ↗” mają tę samą wysokość wiersza co działy; separatory w równych odstępach.
- [ ] Telefon: 0 różnic w menu na zrzutach.
- [ ] Raport ze zrzutami przed/po w czterech rozdzielczościach.
