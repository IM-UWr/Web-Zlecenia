# Sylwetki „Warto wiedzieć”: baner z liczbami i figurką, portret opływany tekstem

Prototyp z 18.11.2026 według decyzji właściciela z 18.11 (23:06) i (23:26). Ten opis służy do napisania zlecenia dla kodu Astro (Web-Core).

- Prototyp: `/home/claude/ww-baner/proto/`. Lista to `index.html`, sylwetki to `<id>/index.html`. Folder działa samodzielnie, ma 7,5 MB.
- Budowa: `python3 /home/claude/ww-baner/buduj.py`. Skrypt czyta z `pod47`, `liczby/*.json` i `instytut.json`, a style bierze z `ww-baner.css`.
- Zrzuty: `/home/claude/ww-baner/zrzuty/`.
- Narzędzia: `narz/zrzuty.py`, `narz/sprawdz.py` (kontrola 18 stron × 14 szerokości) i `narz/prog.py` (zapas między tytułem a figurką).

Wszystkie wartości CSS poniżej są w `ww-baner.css`. Ten plik jest dołączany po stylach strony. W Web-Core te reguły trzeba przenieść do plików, które podaję przy każdej zmianie.

---

## 1. Baner: trzy liczby pod hasłem (styl Pracowników)

### DOM

Przed zmianą: `<div class="z-nagl z-nagl-pod" data-dzial="instytut">`. W `.z-tyt` jest `.z-tyt-g` (sygnet, ścieżka, h1, podpis) i `p.z-haslo`. Nie ma liczb ani znaku.

Po zmianie (sylwetka z hasłem i liczbami):
```html
<div class="z-nagl z-nagl-pod z-liczbami z-ck-losuje z-znak-sam" data-dzial="instytut" data-ck="<id figurki z budowania>" data-pagefind-ignore>
  <div class="z-foto">…</div>
  <div class="z-tyt">
    <div class="z-tyt-g">…sygnet, ← Warto wiedzieć, <h1>, mały podpis…</div>
    <p class="z-haslo">Współtwórca szkoły lwowskiej i wrocławskiej, mistrz aforyzmu</p>
    <div class="z-slot"><ul class="pt-liczby" data-pagefind-ignore>
      <li><span class="n">1945</span>pierwszy dziekan</li>
      <li><span class="n">1946</span>Nowa Księga Szkocka</li>
      <li><span class="n">20</span>doktorów</li>
    </ul></div>
  </div>
  <svg class="z-znak" viewBox="0 0 200 240" aria-hidden="true" focusable="false">…ścieżki…</svg>
  <script>…losowanie figurki (pkt 2)…</script>
  <script>…DOPASUJ z NaglowekZ.astro + wstawka z pkt 5…</script>
</div>
```

### W Web-Core

`SylwetkaWW.astro` podaje liczby do banera tak jak Pracownicy:
```astro
<Fragment slot="baner"><LiczbyBanera lang={lang} pozycje={liczby} /></Fragment>
```
Liczby mają typ `Napis`: `{ n, pl, en }`. `LiczbyBanera` już dziś:
- wstawia twarde spacje po jednoliterowych wyrazach (`bezSierotek`),
- pomija puste pozycje.

`NaglowekZ` sam dodaje klasę `z-liczbami`, gdy jest i hasło (pole „podpis” sylwetki), i lista `.pt-liczby`. Dlatego `hasloBezLiczb` może zostać.

### Skąd liczby

Prototyp czyta liczby z `/home/claude/ww-baner/liczby/<id>.json`, z pól `liczby[].n` i `liczby[].podpis`. Pole `podpis_en` jest gotowe na stronę EN.

W Web-Core potrzebne jest pole w danych sylwetki (pytanie 1). Proponuję listę `baner` we frontmatterze: 3 pozycje `{n, podpis, podpis_en}`, edytowalne w CMS.

- Gdy pliku liczb nie ma, `buduj.py` bierze tymczasowo 3 pierwsze punkty `:::w-skrocie`. Podpis jest wtedy ucięty do całych słów (najwyżej 20 znaków) z „…”. W tym przebiegu nie było to potrzebne: 17 stron ma liczby z JSON-a, Tabisz nie ma bloku.
- Twarde spacje: `buduj.py` robi to samo co `bezSierotek`. Przykład: „doktorat u Hartmana” łamie się na telefonie jako „doktorat / u Hartmana”.

### Blok „W skrócie” znika z treści

Z treści znika `div.ww2-prof-tr` z `dl.ww2-skrot`. W `SylwetkaWW.astro` usuwamy linię z `tresc?.skrot`. Style `dl.ww2-skrot` w `warto-wiedziec.css` stają się zbędne (pytanie 2: co z blokiem `:::w-skrocie` w plikach .md).

### CSS liczb

Bez zmian, bo to style Pracowników:
- komputer: `zalozyciele.css`, `.z-slot .pt-liczby`. Jeden rząd z kreską `border-top: 1px solid rgb(255 255 255 / .2)`, liczba `.n` 22–30 px, podpis 13–14 px, `nowrap`, odstęp 34 px;
- telefon: `zal-telefon.css`, siatka 3 kolumn, `.n` 26 px, podpis 12 px. Podpis łamie się równo (`text-wrap: balance` jest już w stylach telefonu).

### Sprawdzone (`narz/sprawdz.py`)

Na 1920, 1600, 1440, 1366, 1280, 1180, 1100 i 1024 px wszystkie trzy pozycje mieszczą się w rzędzie na wszystkich 17 stronach:
- nie ma `aria-hidden` ani `z-bez-liczb`,
- liczby nie nachodzą na figurkę.

Najdłuższe rzędy (Mycielski, Perkal, Hartman, Narkiewicz) przy 1024 px mają ok. 630 px na ok. 700 px dostępnych (od lewej krawędzi tytułu do figurki minus 20 px).

Na telefonie (390 px) dłuższe podpisy łamią się na 2 linie, np. „aksjomat / determinacji”, „Nagroda / Kuratowskiego”, „pierwszy / dziekan WMI”. Wygląda to porządnie. Podpisów nie zmieniałem.

---

## 2. Baner: figurka z puli Instytutu, losowana, bez opisu

### DOM

Za `.z-tyt` stoi sam `svg.z-znak`, a zaraz za nim skrypt losowania. **Nie ma `p.z-znak-opis`** (bez tytułu i bez zdania).

Klasy na `.z-nagl`:
- `z-znak-sam`: znacznik figurki bez opisu (na nim opierają się reguły z pkt 5);
- `z-ck-losuje`: istniejąca reguła `html.js .z-nagl-pod.z-ck-losuje .z-znak { visibility: hidden }` ukrywa figurkę do końca losowania, więc stała figurka z budowania nie mignie;
- `data-ck`: id figurki stałej.

### Wygląd

Bez zmian, wszystko z Pracowników:
- komputer:
  - z liczbami (`.z-nagl-pod.z-liczbami .z-znak`): `width = height = var(--zn)`, `--zn: clamp(120px, 200·jn, 200px)`, `top: calc(var(--gora) + 34px)`, `right: var(--znak-p)`, `--znak-p: max(16px, var(--marg) - 90px)`;
  - bez liczb (Tabisz): `.725·zn × .85·zn`, `top: gora + 10px`;
  - kreski: `stroke-width` 1,3 px, grube 2 px z cieniem;
  - po najechaniu figurka rysuje się od nowa (bez zmian);
- telefon (`zal-telefon.css`): 104 × 130 px w prawym górnym rogu, `opacity: .7`, w tle pod tekstem (`z-index: 0`), tak jak na innych podstronach.

### Losowanie przy każdym wejściu

Skrypt w linii za svg, uruchamiany zanim strona się narysuje (`ZNAK_JS` w `buduj.py`):

1. Pula to karty z `src/data/ciekawostki/instytut.json` bez `ukryta: true` i bez `stan: "odpada"` (`pulaDzialu('instytut')`). Dziś to 25 kart, te same co na Pracownikach. Dane w linii: `[[id, waga, [[d, gruba?], …]], …]`. Ścieżki są skrócone przez `kompaktD`, a `ulubiona` ma wagę 3.
2. Z kandydatów wypadają:
   - figurka z poprzedniej sylwetki w tej wizycie (`sessionStorage["im-ww-znak"]`);
   - ciekawostka, którą w tej wizycie pokazuje lista „Warto wiedzieć” (`sessionStorage["im-ciek-zestaw"].instytut["/instytut/warto-wiedziec"]`, zestaw z NaglowekZ).
   
   Gdy nic nie zostaje, losowanie idzie z całej puli.
3. Wybór jest ważony: `r = Math.random() · Σwag` i pierwsza karta, przy której suma przekroczy `r`.
4. Gdy wylosowana karta jest inna niż `data-ck`, ścieżki svg są podmieniane (`path`, `pathLength="1"`, klasa `gruba`), a `data-ck` dostaje nowe id.
5. Id trafia do `sessionStorage["im-ww-znak"]`. Na koniec (`finally`) skrypt zdejmuje `z-ck-losuje`.
6. Bez `sessionStorage`, np. w trybie prywatnym z blokadą: zwykłe losowanie bez wykluczeń.

Wynik w kontroli: 25 różnych figurek na 252 wejściach.

Wczytywanie z wyprzedzeniem (speculation rules, prerender): losowanie odbywa się w momencie wczytania w tle. To nadal „przy każdym wejściu”, ale wykluczenie „poprzedniej” może wtedy dotyczyć innej strony. Nie warto tego komplikować (pytanie 4).

### Bez JS: stała figurka

```ts
// FNV-1a 32-bit po UTF-8 id osoby (slug), modulo długość puli (kolejność z instytut.json po filtrze)
function fnv1a(s: string) { let h = 0x811c9dc5; for (const b of new TextEncoder().encode(s)) { h ^= b; h = Math.imul(h, 0x01000193) >>> 0; } return h; }
const stala = pula[fnv1a(slug) % pula.length];
```

Zdarzają się powtórzenia (np. `biblioteka-1945` u trzech osób), ale bez JS to nie przeszkadza. Alternatywa bez powtórzeń to kolejna karta wg pozycji osoby na liście, jak `ukladStaly` (pytanie 5).

### W Web-Core (`NaglowekZ.astro`)

Nowy prop, np. `znak: 'ciekawostka' | 'sam'` albo `znakSam?: boolean`. Przy `znakSam`:
- pula Instytutu bez listy stron działu;
- stała figurka po `fnv1a(slug)`;
- svg bez `p.z-znak-opis`;
- skrypt jak wyżej zamiast `CK`;
- klasa `z-znak-sam`.

`NaglowekStrony` przekazuje dziś `znak={zMenuDzialuZ}`, czyli tylko strony z menu działu. Sylwetka potrzebuje osobnej ścieżki, np. prop z `Podstrona` / `SylwetkaWW`.

Skrypt `DOPASUJ` działa bez opisu bez zmian, bo `dod` jest `null`. Granicą tytułu, hasła i liczb jest lewa krawędź figurki: 40 px dla tytułu i hasła, 20 px dla liczb.

Rozmiar: dane puli w linii zajmują ok. 52 KB na stronę (bez kompresji). Na Pracownikach ciekawostki zajmują ok. 56 KB (pytanie 6).

---

## 3. Treść: portret opływany tekstem

### DOM

Przed zmianą (siatka 200 px | „W skrócie”):
```html
<div class="ww2-prof"> <div class="ww2-prof-l">portret, p.ww2-prof-lata, [p.ww2-prof-zrodlo]</div> <div class="ww2-prof-tr">dl.ww2-skrot</div> </div>
[RamkiWW: .ww2-bledy / .ww2-tba]
<div class="ww2-wstep ww2-tresc"><div class="prose">…</div></div>
<section id="…">…
```

Po zmianie `.ww2-prof` obejmuje portret i wstęp (albo ramkę TBA), a `.ww2-prof-tr` znika:
```html
<div class="ww2-prof">
  <div class="ww2-prof-l">portret, p.ww2-prof-lata, [p.ww2-prof-zrodlo]</div>   ← float: left
  [RamkiWW: .ww2-bledy / .ww2-tba / „Translation in preparation”]
  <div class="ww2-wstep ww2-tresc"><div class="prose">…</div></div>
</div>
<section id="…">…
```
W `SylwetkaWW.astro` trzeba przenieść `<RamkiWW …/>` i blok wstępu do środka `div.ww2-prof` i usunąć `div.ww2-prof-tr`.

### CSS

Zamiast reguł `.ww2-prof` i `.ww2-prof-l` w `warto-wiedziec.css`:
```css
.z-ww2-os .ww2-prof { display: flow-root; margin: 0 0 40px; }              /* było: grid 200px 1fr, gap 28, margin 0 0 30px */
.z-ww2-os .ww2-prof > .ww2-prof-l { float: left; position: static; width: 200px; margin: 7px 28px 16px 0; }  /* było: sticky */
body .tresc .ww2-prof > .ww2-wstep { margin: 0; }                           /* odstęp 40 px przejmuje .ww2-prof */
body .tresc .ww2-prof > .ww2-wstep p { text-wrap: pretty; }
.z-ww2-os .ww2-prof :is(.prose ul, .prose ol, .prose blockquote, .prose figure) { display: flow-root; }
.z-ww2-os .ww2-prof > .ww2-tba { display: flow-root; margin: 7px 0 0; }    /* było: margin 1.5rem 0 2rem */
@media (max-width: 1023px) { .z-ww2-os .ww2-prof > .ww2-prof-l { width: 160px; margin: 7px 24px 14px 0; } }
@media (max-width: 560px)  { .z-ww2-os .ww2-prof > .ww2-prof-l { width: 110px; margin: 7px 14px 12px 0; } }
```
Selektory lat i źródła zdjęcia (`.ww2-prof p.ww2-prof-lata`, `.ww2-prof p.ww2-prof-zrodlo`) zostają bez zmian. Ich wartości też: 14 px, a na ≤ 560 px 12,5 px.

Siatkowe reguły `.ww2-prof { grid-template-columns … }` w `@media (max-width: 1023px)` i `(max-width: 560px)` do usunięcia.

### Wartości i dlaczego

- **Góra:** portret jest 7 px niżej niż góra bloku. Pierwsza linia wstępu ma 18 px przy wysokości 28,8 px (Manrope), więc górna krawędź wielkich liter wypada ok. 8 px pod górą linii. Dzięki temu góra portretu i góra liter są na jednej wysokości.

  Pomiar: portret na y = 381, pudełko akapitu na 374, a wielkie litery zaczynają się na ok. 382 (1366 px).
- **Odstęp z prawej:** 28 px na komputerze (tyle samo co dawny `gap`), 24 px na tablecie, 14 px na telefonie. Odstęp pod spodem: 16, 14 i 12 px, liczone od linii z latami.
- **Szerokości portretu:** 200 px (≥ 1024), 160 px (561–1023), 110 px (≤ 560). Dawniej było 200, 136 i 96 px.
- **Szerokość kolumny obok portretu:** wstęp ma `max-width: 43.92em`, czyli 790 px przy 18 px. Obok portretu zostaje ok. 560 px przy 1366 i 1920 px, ok. 400 px przy 1024 px i ok. 234 px przy 390 px.
- **`text-wrap: pretty`** we wstępie: mniej sierotek i bardzo krótkich linii w zwężonej kolumnie. Przeglądarki bez tej funkcji łamią tekst zwyczajnie.
- **Listy, cytaty i rysunki** we wstępie dostają `flow-root`. Stoją wtedy obok portretu, a nie pod nim, więc punktory i ramki nie chowają się pod portretem. Dziś żaden wstęp ich nie ma, to zabezpieczenie.

### Nagłówki h2 obok portretu: decyzja

Przy krótkim wstępie (Bożejko 410 znaków, Narkiewicz 429) przy 1366–1920 px nagłówek pierwszej sekcji wypadał wcięty obok dołu portretu. Tekst sekcji zaczynał się już od lewej krawędzi, pod portretem. Wyglądało to nieporządnie: zrzut `zrzuty/wariant-odrzucony-h2-obok-portretu-bozejko-1366.png`.

Dlatego **portret opływa tylko wstęp (albo ramkę TBA)**. `.ww2-prof` jako `flow-root` obejmuje oba elementy. Każda sekcja z nagłówkiem h2 zaczyna się na pełnej szerokości, 40 px pod niższym z dwóch: końcem wstępu albo dołem portretu z latami (+16 px). Stąd od linii z latami do nagłówka jest ok. 56 px.

Przy długim wstępie (np. Steinhaus przy 1024 px, Ryll-Nardzewski przy 1366 px) tekst wstępu przechodzi pod portret na pełną szerokość. To zwykłe opływanie.

### Telefon: decyzja

Portret **zostaje opływany**, ma 110 px szerokości. Sprawdziłem 3 warianty przy 390 px (`zrzuty/wariant-telefon-*.png`):
- 120 px: przy 120 px w wąskiej kolumnie zdarzały się linie z jednym słowem, np. „należy do”, „najwybitniejszych”;
- 110 px z `text-wrap: pretty`: kolumna ma ok. 234 px, ok. 22–26 znaków w linii, czyta się dobrze;
- portret wyśrodkowany nad tekstem: porządny, ale o ok. 170 px przesuwa wstęp w dół i zostawia puste pola po bokach.

Napis „Zdjęcie” na placeholderze jest ukryty przy ≤ 560 px, jak dotąd.

---

## 4. Tabisz (TBA)

- Baner bez liczb (sylwetka nie ma hasła ani liczb), z figurką: `z-nagl z-nagl-pod z-ck-losuje z-znak-sam`, bez `z-liczbami`. Wymiary figurki są jak na podstronie bez liczb.
- Ramka `.ww2-tba` stoi w `.ww2-prof` obok portretu. Ma `flow-root` i `margin-top: 7px`, więc jej górna krawędź jest na wysokości góry portretu.
- „Inne sylwetki” zaczynają się pod portretem, 56 px pod nim.
- Placeholder bez lat, bo pole „Lata” jest puste. Jak dotąd.

---

## 5. Imię i nazwisko w jednej linii (decyzja 18.11, 23:26)

**Zasada (komputer, ≥ 1024 px):** tytuł sylwetki nigdy się nie łamie. Jeśli przy danej szerokości okna imię i nazwisko z figurką po prawej się nie mieści, **figurka znika**. Nie łamiemy imienia, żeby utrzymać symbol.

### CSS

W widoku komputera, czyli w media query komputera `(min-width: 1024px) and (min-height: 501px), (min-width: 1024px) and (pointer: fine)`:
```css
.z-nagl-pod.z-znak-sam h1 { white-space: nowrap; }                 /* wygrywa z text-wrap: balance z .z-nagl-pod h1 */
.z-nagl-pod.z-znak-sam.z-znak-brak .z-znak { display: none; }
html:not(.js) .z-nagl-pod.z-znak-sam .z-tyt-g { max-width: none; }   /* bez JS nie ma rezerwy 570–676 px na opis, którego tu nie ma */
html:not(.js) .z-nagl-pod.z-znak-sam .z-haslo { max-width: calc(100% - max(0px, var(--zn) - var(--marg) + var(--znak-p)) - 40px); }
html:not(.js) .z-nagl-pod.z-znak-sam.z-tyt-dlugi-bez-js .z-znak { display: none; }
html:not(.js) .z-nagl-pod.z-znak-sam.z-tyt-dlugi-bez-js .z-haslo { max-width: none; }
```

### JS: wstawka do `DOPASUJ`

Wstawka idzie do `DOPASUJ` w `NaglowekZ.astro` (`DOPASUJ_ZNAK` w `buduj.py`), w funkcji `dopasuj()` tuż przed `if(dod)…; var zaDlugi=uklad();`:
```js
var zs=n.classList.contains('z-znak-sam')&&n.querySelector('.z-znak');
if(zs){n.classList.remove('z-znak-brak');if(!tel&&h1){h1.style.fontSize='';h1.style.maxWidth='';
  var zr=zs.getBoundingClientRect(),q=document.createRange();q.selectNodeContents(h1);
  if(zr.width&&h1.getBoundingClientRect().left+q.getBoundingClientRect().width+40>zr.left)n.classList.add('z-znak-brak')}}
```

Jak to działa:
- Pomiar to rzeczywista szerokość tekstu tytułu w jednej linii (zakres tekstu, `nowrap`) przy stopniu z CSS, bez stylu z poprzedniego dopasowania. Porównanie: lewa krawędź tytułu + szerokość + 40 px względem lewej krawędzi figurki. Odstęp 40 px jest ten sam co w `DOPASUJ`.
- Pozycja figurki nie zależy od tytułu, więc wynik się nie waha.
- Pomiar biegnie przy wczytaniu, przy każdej zmianie rozmiaru okna (rAF) i po wczytaniu krojów. To te same wyzwalacze co `DOPASUJ`.
- Klasa jest zdejmowana i dodawana w jednym przebiegu skryptu, przed malowaniem, więc nic nie miga ani nie skacze.
- Po schowaniu figurki `uklad()` liczy granice tytułu, hasła i liczb do prawego marginesu, bo figurka ma 0 × 0.
- Zabezpieczenie: gdyby tytuł nie mieścił się nawet bez figurki, działa istniejąca pętla `DOPASUJ`, która zmniejsza stopień o 4 px do 44 px. Tytuł zostaje w jednej linii. Test w punkcie „Pomiary”.
- **Telefon:** bez zmian. Wstawka zdejmuje klasę, a figurka stoi w tle za tytułem i hasłem (`opacity .7`), jak na innych podstronach, np. Struktura i zakłady. Tytuł na telefonie łamie się jak dotąd (`text-wrap: balance`, 30 px).

### Pomiary (`narz/prog.py`, szerokości 1024–1920 co 8 px, plus 1499 i 1500)

- Stopień tytułu: `clamp(40px, 58·100vw/1368, 58px)`, czyli 43,4 px przy 1024 i 58 px od 1368. Najciaśniej jest zawsze przy 1024 px.
- Granica: tytuł mieści się obok figurki przy każdej szerokości ≥ 1024 px, jeśli ma najwyżej **15,6 em** (baner z liczbami; bez liczb 16,6 em). Przy 1024 px to 678 px na tytuł o stopniu 43,4 px.
- Najdłuższe obecne nazwiska:

  | Osoba | Szerokość | Zapas przy 1024 px |
  |---|---|---|
  | Czesław Ryll-Nardzewski | 11,49 em | 180 px |
  | Władysław Ślebodziński | 11,10 em | 197 px |
  | Władysław Narkiewicz | 10,32 em | 231 px |

  Najkrótsze: Piotr Biler, 4,75 em, zapas 473 px.
- **Wynik: dziś przy żadnej sylwetce i żadnej szerokości figurka nie znika.** Wszystkie tytuły są w jednej linii, bez zmniejszania stopnia.
- Test sztucznie długiego tytułu „Czesław Ryll-Nardzewski-Kowalski von Zielińskich” (`zrzuty/test-sztucznie-dlugie-nazwisko-*.png`): figurka znika przy 1024, 1366 i 1920 px. Tytuł zostaje w jednej linii; przy 1366 i 1920 px pętla zmniejsza go do 45,9 i 50 px.

### Bez JS

Tytułu nie da się zmierzyć, a próg szerokości dla najdłuższego obecnego nazwiska wypada poniżej 1024 px. Reguła z progiem byłaby więc dziś martwa.

Zamiast niej zabezpieczenie na przyszłość: przy budowaniu tytuł dłuższy niż **28 znaków** dostaje klasę `z-tyt-dlugi-bez-js`, a bez JS jego figurka znika na komputerze. Brygada ma ok. 0,43–0,52 em na znak, więc granica 15,6 em to ok. 30 znaków. Dziś żadna sylwetka nie ma takiej klasy, bo najdłuższy tytuł ma 23 znaki.

Zrzuty bez JS: `zrzuty/bez-js-czeslaw-ryll-nardzewski-*.png`. Stała figurka, tytuł w jednej linii.

---

## 6. Bez zmian

Spis „Na tej stronie”, sekcje treści, „W »Warto wiedzieć«”, zwinięte „Źródła”, „Inne sylwetki”, stopka, pasek „Podgląd — ta strona nie jest jeszcze opublikowana” i etykieta SZKIC. Lista „Warto wiedzieć” też jest bez zmian: ma swój baner z ciekawostką.

## 7. Tylko w prototypie (nie do Web-Core)

- Usunięte:
  - plakietka stanu budowy Podglądu (`podglad/stan-budowy.css` i `.js`, `div#stan-budowy`, który odpytuje API GitHuba; razem z nią dymek „Szkic: … Włącz »Opublikowane«”);
  - reguły `speculationrules`, bo ich wzorce `/Web-Podglad/*` nie pasują do prototypu.
- Pagefind nie był wczytywany. Formularz szukania w menu prowadzi do `https://im-uwr.github.io/Web-Podglad/szukaj`.
- Adresy są względne:
  - lista ↔ sylwetki: `<id>/index.html` i `../index.html#sylwetki`;
  - zasoby: `_astro/`, `pliki/` i `favicon.svg`. Kopiowane są tylko używane pliki (195): CSS, JS z importami, kroje, w tym KaTeX z arkusza, zdjęcia banera i kart listy;
  - `url()` w zmiennej CSS w atrybucie `style` (`--logo`) liczy się względem `_astro/`;
  - wszystko inne prowadzi do `https://im-uwr.github.io/Web-Podglad/…`, także wpisy „Warto wiedzieć”, które nie są sylwetkami, wersja EN i PDF-y.
- Sprawdzone: serwer na innym porcie i w podkatalogu (`/proto/…`). Wszystkie 1065 odwołań lokalnych istnieją, a w konsoli nie ma błędów ani ostrzeżeń (18 stron × 14 szerokości). Otwarcie przez `file://` nie wczyta skryptów modułowych (CORS), więc prototyp jest przeznaczony na serwer HTTP.

## 8. Pytania i rzeczy do decyzji

1. **Gdzie trzymać liczby banera w Web-Core?** Proponuję pole w frontmatterze sylwetki, np. `baner: [{n, podpis, podpis_en}] × 3`, z polem w CMS (Warto wiedzieć → Sylwetki). Alternatywa: zostawić blok `:::w-skrocie` jako źródło z nowymi krótkimi podpisami (≤ 20 znaków), ale pola formularza są czytelniejsze. EN: `podpis_en` jest w plikach JSON, a strona EN jest poza prototypem.
2. **Co z blokiem `:::w-skrocie` w plikach .md** (długie podpisy, linki do MGP)? Opcje: usunąć po przeniesieniu liczb, zostawić jako notatkę redakcyjną (niewidoczną) albo dalej parsować z ramką `.ww2-bledy` na Podglądzie. Jeśli zniknie, do usunięcia są też walidacja w `ww.mjs` i style `dl.ww2-skrot`.
3. **Figurka na telefonie zachodzi na tytuł i hasło** (w tle, `opacity .7`), bo hasła sylwetek są długie (2 linie). Tak działają też inne podstrony, np. Struktura i zakłady. Czy zostawić, czy na telefonie zwęzić tytuł i hasło sylwetki o ok. 100 px? Tytuł częściej łamałby się wtedy na 2 linie.
4. **Wykluczenia w losowaniu:** prototyp nie pokazuje 2 razy z rzędu tej samej figurki i nie pokazuje ciekawostki, która jest w tej wizycie na liście „Warto wiedzieć”. Czy to zostawić, czy losować całkiem swobodnie?
5. **Figurka bez JS:** skrót FNV-1a (stała dla osoby, możliwe powtórzenia) czy kolejne karty wg pozycji na liście (bez powtórzeń, ale zmieniają się po dodaniu sylwetki)?
6. **Dane puli w linii:** ok. 52 KB na każdej sylwetce (jak na Pracownikach). Można je przenieść do jednego pliku JS w pamięci przeglądarki, ale wtedy figurka pojawi się po jego wczytaniu, z krótkim odstępem.
7. **Zapas tytułu:** granica 40 px między tytułem a figurką (jak w `DOPASUJ`). Czy figurka ma znikać dopiero, gdy tytuł nie mieści się w pełnym stopniu? Tak jest teraz: bez zmniejszania tytułu, żeby zatrzymać figurkę.
8. **Odstęp od lat do pierwszego nagłówka:** przy krótkim wstępie wynosi ok. 56 px (16 + 40), a od tekstu do nagłówka 40 px. Ewentualnie można zmniejszyć dolny margines portretu do 12 px.
9. **Wstęp przy 1366–1920 px ma obok portretu ok. 560 px szerokości** (`max-width: 43.92em` liczone od lewej krawędzi kolumny). Czy w części obok portretu poszerzyć wstęp do prawej krawędzi kolumny treści (do ok. 720 px)? Linie byłyby wtedy dłuższe niż pod portretem.
