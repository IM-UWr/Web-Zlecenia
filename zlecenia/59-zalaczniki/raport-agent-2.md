# Agent 2: raport (Web-Instytut, „Warto wiedzieć”: 9 sylwetek i 9 historii)

> **Uwaga koordynatora (22.11, po raporcie):** w łatce `Web-Instytut.patch` IM PAN jest już wszędzie „Institute of Mathematics of the Polish Academy of Sciences” (nie „Mathematical Institute of…”, jak niżej w „Do decyzji”, p. 3), a Politechnika Wrocławska wszędzie „Wrocław University of Science and Technology” (także w kontekście historycznym, jak u agenta 1; tak samo na stronie „Sukcesy — historia” w Web-Nauka). Wartości `obraz_zrodlo_en` z „Potrzebnych zmian w kodzie”, p. 1, są już wpisane w łatce.


Łatka: `wyniki/2/Web-Instytut.patch` (18 plików, +690/−153). `git apply --check` na czystym klonie przechodzi. `sprawdz_tresci.py` przechodzi bez błędów dla każdego z 18 zmienionych plików. Dla całego repozytorium skrypt zgłasza 3 błędy, które były już na czystym klonie i dotyczą nagród (zakres agenta 1, opis niżej). `sprawdz-jawny-markdown.mjs`: OK, formularze CMS zachowują wszystkie pola.

## Podsumowanie

- **Sprawdzone:** 18 plików, 84 pola EN. Na każdą sylwetkę przypada `tresc_en`, `podpis_en`, `zajawka_en` i 3 × `etykieta_en`, na każdą historię `tytul_en`, `zajawka_en`, `tresc_en` i ewentualnie `obraz_opis_en` oraz `link_etykieta_en`. Pola `n_en` są puste, co jest poprawne, bo liczby to same cyfry.
- **Uzupełnione (EN brakowało): 45 pól.**
  - 8 sylwetek × (`tresc_en`, `podpis_en`, `zajawka_en`). To około 16,7 tys. słów angielskiego tekstu.
  - 7 historii × (`tytul_en`, `zajawka_en`, `tresc_en`).
- **Poprawione (EN był, ale zły): 3 pola.**
  - `krzysztof-tabisz` → `tresc_en`: przetłumaczona od nowa.
  - `wyklad-terencea-tao` → `tresc_en`.
  - `artykul-w-annals-of-mathematics` → `tresc_en`: dopisane tylko komentarze redakcyjne.
- **Zostawione bez zmian (dobre): 36 pól.**
  - `krzysztof-tabisz`: `podpis_en`, `zajawka_en`.
  - 27 × `etykieta_en` w 9 sylwetkach.
  - `artykul-w-annals…`: `tytul_en`, `zajawka_en`, `link_etykieta_en`.
  - `wyklad-terencea-tao`: `tytul_en`, `zajawka_en`, `obraz_opis_en`, `link_etykieta_en`.
- **Kontrola każdego pliku:**
  - YAML wczytuje się przez PyYAML, a wartość `tresc_en` po wczytaniu jest identyczna z przygotowanym tekstem.
  - Te same `## … {#id}` w tej samej kolejności co w polskiej Treści, ta sama liczba nagłówków `##` i akapitów, te same linki (adresy i kolejność), te same komentarze `<!-- … -->` przepisane bez zmian.
  - Bloków `:::` nie ma ani w polskiej, ani w angielskiej Treści. Nie ma linii `# `, nie ma `$`.
  - Treść EN wyrenderowałem pipeline’em remark + `rehype-bloki` (bez budowy strony). Nie zostały żadne surowe `*` ani `](`.

## Tabela zmian

| Plik | Pole | Co zrobiono |
|---|---|---|
| `sylwetki/krzysztof-tabisz.md` | `tresc_en` | **poprawione** (od nowa). Stary EN był niezgodny z przerobioną polską Treścią: inny podział akapitów, „Institute of Mathematics”, tytuł rozprawy przetłumaczony zamiast oryginału, brak linku do Krzywickiego, zdania dodane lub zmienione względem polskiego, nagłówki w Title Case, zapis `>-` łamiący akapity. Teraz: wierne tłumaczenie, `|-`, komentarze. |
| `sylwetki/krzysztof-tabisz.md` | `podpis_en`, `zajawka_en`, 3 × `etykieta_en` | zostawione (dobre) |
| `sylwetki/marek-bozejko.md` | `tresc_en`, `podpis_en`, `zajawka_en` | uzupełnione (pełne tłumaczenie z 39 źródłami) |
| `sylwetki/piotr-biler.md` | `tresc_en`, `podpis_en`, `zajawka_en` | uzupełnione |
| `sylwetki/roman-duda.md` | `tresc_en`, `podpis_en`, `zajawka_en` | uzupełnione |
| `sylwetki/stanislaw-hartman.md` | `tresc_en`, `podpis_en`, `zajawka_en` | uzupełnione |
| `sylwetki/tomasz-rolski.md` | `tresc_en`, `podpis_en`, `zajawka_en` | uzupełnione |
| `sylwetki/witold-wolibner.md` | `tresc_en`, `podpis_en`, `zajawka_en` | uzupełnione |
| `sylwetki/wladyslaw-narkiewicz.md` | `tresc_en`, `podpis_en`, `zajawka_en` | uzupełnione |
| `sylwetki/wladyslaw-slebodzinski.md` | `tresc_en`, `podpis_en`, `zajawka_en` | uzupełnione |
| 8 sylwetek powyżej | `liczby[].etykieta_en` | zostawione (były; uwagi w „Do decyzji”, p. 4) |
| `historie/aksjomat-determinacji.md` | `tytul_en`, `zajawka_en`, `tresc_en` | uzupełnione („The axiom of determinacy”) |
| `historie/czterech-rektorow.md` | `tytul_en`, `zajawka_en`, `tresc_en` | uzupełnione („Four mathematician rectors”) |
| `historie/nowa-ksiega-szkocka.md` | `tytul_en`, `zajawka_en`, `tresc_en` | uzupełnione („The New Scottish Book”) |
| `historie/pierwsze-wyklady.md` | `tytul_en`, `zajawka_en`, `tresc_en` | uzupełnione („The first mathematics lectures in Wrocław”) |
| `historie/probability-and-mathematical-statistics.md` | `tytul_en`, `zajawka_en`, `tresc_en` | uzupełnione. `tytul_en` jest taki sam jak polski (nazwa czasopisma), ale wypełniony, żeby tytuł nie dostawał `lang="pl"`. |
| `historie/taksonomia-wroclawska.md` | `tytul_en`, `zajawka_en`, `tresc_en` | uzupełnione („The Wrocław taxonomy”) |
| `historie/zywa-ges.md` | `tytul_en`, `zajawka_en`, `tresc_en` | uzupełnione („A live goose for Per Enflo”; gęś Mazura zachowana dosłownie) |
| `historie/wyklad-terencea-tao.md` | `tresc_en` | **poprawione**: tytuł wykładu Strzeleckiego w oryginale z tłumaczeniem w nawiasie (D10/D4), a nie samo tłumaczenie; usunięte tytuły innych osób („Professor Elias M. Stein”, „Prof. Paweł Strzelecki”; styl WW); dopisane komentarze redakcyjne |
| `historie/artykul-w-annals-of-mathematics.md` | `tresc_en` | **poprawione** minimalnie: dopisane 2 komentarze redakcyjne. Tekst dobry, zostawiony. |
| `historie/wyklad-terencea-tao.md`, `artykul-w-annals…` | `tytul_en`, `zajawka_en`, `obraz_opis_en`, `link_etykieta_en` | zostawione (dobre) |

## Przyjęte zasady (warto potwierdzić, opis w „Do decyzji”, p. 1–3)

- **Styl WW.** Tytuł „Prof.”/„Dr” tylko w pierwszym zdaniu bohatera, dalej samo nazwisko. Inne osoby bez tytułów, także w opisach źródeł, np. „host: Michael Leinert”. Wyjątek: nazwy źródeł, np. „prof. dr hab. Marek Bożejko”, zostają w oryginale.
- **Tytuły prac po polsku.** Kursywa, oryginał i tłumaczenie w nawiasie, np. *O pojęciu wymiaru* (On the concept of dimension, 1972). Tytuły obcojęzyczne (angielskie, francuskie) zostają bez zmian.
- **Typografia.** „…” → “…”, daty po angielsku („19 November 2026”, „1 September 2005 – 31 August 2009”), „s.” → „p./pp.”, liczby z przecinkiem tysięcy („1,800”, „5,000”; liczby w banerze bez zmian).
- **Linki wewnętrzne** bez `/en`. W źródłach etykiety stron wewnętrznych mają tytuły EN tych stron („Research achievements – historical overview”, „News: University Medals for Professors…”, tytuły grantów z `tytul_en`).

## Potrzebne zmiany w kodzie (dla agenta 3)

1. **`obraz_zrodlo` (Źródło zdjęcia) nie ma wersji EN.** Pola `obraz_zrodlo_en` nie ma w schemacie (`src/content.config.ts:507`, kolekcja `ww_sylwetki`) ani w `.pages.yml` Web-Instytut (karta sylwetki). Na `/en` pod portretem widać np. „Photo: ze strony T. Rolskiego”.
   - Propozycja: dodać `obraz_zrodlo_en` do schematu i do karty w CMS; w `src/views/SylwetkaWW.astro:33` brać `obraz_zrodlo_en ?? obraz_zrodlo` na `/en`.
   - Proponowane wartości:

     | Sylwetka | PL | EN |
     |---|---|---|
     | Rolski | ze strony T. Rolskiego | from T. Rolski’s website |
     | Hartman | Archiwum UWr | University of Wrocław Archives |
     | Duda | Politechnika Łódzka | Lodz University of Technology |
     | Narkiewicz | galeria J. Shallita, University of Waterloo | J. Shallit’s gallery, University of Waterloo |
     | Biler | PAN | Polish Academy of Sciences |
     | Tabisz | IM UWr | Mathematical Institute, University of Wrocław |
     | Ślebodziński | Wikimedia Commons | bez zmian |

   - Dotyczy też sylwetek agenta 1.
2. **Napis „Zdjęcie” w portrecie zastępczym** (`src/lib/wartoWiedziec.ts:185`, `<small lang="pl">Zdjęcie</small>`). Pokazuje się tylko na Podglądzie (`TYLKO_OPUBLIKOWANE`), więc na stronie publicznej go nie ma. Na `/en` można dać „Photo”. Dotyczy Bożejki i Wolibnera, którzy nie mają zdjęcia. Niski priorytet.
3. **Informacyjnie: 3 błędy „brak pliku obrazu” dla całego Web-Instytut.** `sprawdz_tresci.py` zgłasza je dla `nagrody/nagroda-ptm-steinhausa.md`, `kategoria-a-plus.md` i `medal-sierpinskiego.md`, bo obrazy `/pliki/aktualnosci/…` leżą w Web-Aktualnosci/public. Błędy są już na czystym klonie i nie są z mojego zakresu. Skrypt sprawdza obraz tylko w repozytorium wpisu, więc to fałszywy alarm przy kontroli jednego repozytorium.

## Do decyzji właściciela

1. **Kursywa zamiast cudzysłowów w tytułach.**
   - W sylwetkach Dudy, Bilera, Hartmana, Wolibnera, Narkiewicza i Ślebodzińskiego polski tekst podaje tytuły książek, artykułów i wykładów w „…”, choć instrukcja mówi o kursywie. W EN dałem kursywę.
   - Nazwy czasopism w „…” w EN są kursywą; tam, gdzie polski tekst ma je bez wyróżnienia (np. Bożejko, Rolski), zostały bez wyróżnienia.
   - W „Źródłach” tytuły zostały w oryginale, z cudzysłowami “…”.
2. **Etykiety źródeł.**
   - Etykiety opisowe przetłumaczyłem, a właściwe tytuły dokumentów i stron zostawiłem w oryginale. Przykłady: „Archiwum UWr: wykaz habilitacji 1945–2015 (…)” → „University of Wrocław Archives: list of habilitations 1945–2015 (…)”; „strona domowa” → „home page”; „Wikipedia (ang.)” → „Wikipedia”; „Katalog biblioteki ÖAW” → „ÖAW library catalogue”.
   - W źródłach Bożejki i Rolskiego jest nadal szablonowe **„autor: Grzegorz (do uzupełnienia nazwiskiem)”**. W EN: „author: Grzegorz (surname to be added)”. Do uzupełnienia przed startem.
3. **Nazwy.**
   - IM PAN → „Mathematical Institute of the Polish Academy of Sciences”, jak w poleceniu. Inne miejsca strony (zestawienie „Research achievements”, aktualności) mają „Institute of Mathematics of the Polish Academy of Sciences”; oficjalna nazwa IMPAN to „Institute of Mathematics, Polish Academy of Sciences”. Warto ujednolicić w całym serwisie.
   - Nagrody (jak w istniejących tekstach EN):
     - „Nagroda Główna PTM im. Stefana Banacha” → “Stefan Banach Main Prize of the Polish Mathematical Society”; gdy polski tekst nie ma „Główna” (Wolibner) → “Stefan Banach Prize of the Polish Mathematical Society”.
     - Pozostałe: “Kazimierz Kuratowski Prize”, “Stanisław Zaremba Prize”, “Samuel Dickstein Prize”, “Polish Mathematical Society Prize for Young Mathematicians”, “Minister of Science Award for lifetime scientific achievement”, “Wacław Sierpiński Research Prize of Division III of the Polish Academy of Sciences”, “Władysław Orlicz Lecture”, “Humboldt Research Award”, “State Prize” (Państwowa Nagroda Naukowa, jak w ciekawostkach patrona), “Gold Cross of Merit”, “Commander’s Cross of the Order of Polonia Restituta”.
   - Politechnika Wrocławska: w kontekście historycznym “Wrocław University of Technology”, dla dzisiejszych stron “Wrocław University of Science and Technology”.
   - Stanowiska: prof. nadzwyczajny → “extraordinary professor”, prof. zwyczajny → “full professor”, zastępca profesora → “acting professor”.
   - Inne nazwy: “Archbishop’s Charitable Committee” (Tabisz i Duda), “Solidarity Citizens’ Committee”, “Society for Academic Courses (Towarzystwo Kursów Naukowych)”, “Flying University”, “KOR (the Workers’ Defence Committee)”, “Wrocław University Press”.
4. **Podpisy w banerze (istniejące, nie zmieniałem).**
   - „UWr rector” (Duda; tak samo u agenta 1), „PTM president” (Ślebodziński) i „PAS member” (Biler) to skróty mało czytelne po angielsku. Do tego Urbanik ma „Academy member”, a Biler „PAS member”.
   - Propozycja: „University rector”, „Academy member” (spójnie z Urbanikiem); „PTM president” może zostać, bo skrót PTM bywa używany po angielsku.
   - „Chair of Mechanics” (Wolibner) jest wielką literą wbrew zasadzie „małą literą”. Spójne z „Chair of Topology” agenta 1.
5. **Wolibner.**
   - Polski tekst podaje „w Piotrowie”, a mianownik przyjąłem jako „Piotrowo” (wieś w gminie Słupno, powiat płocki). Do potwierdzenia, bo może to być „Piotrów”.
   - Inwentarz Archiwum PAN podaje datę urodzenia 24 września 1902, a tytuł wspomnienia w „Colloquium Mathematicum” 9.IX.1902. Pole `rocznica_urodzin` jest puste, więc rozbieżność nie wpływa na stronę, ale dobrze ją znać.
6. **Tabisz.**
   - Zostawiony `zajawka_en` ma 241 znaków przy limicie ok. 220; jest wierny polskiemu, ale można skrócić.
   - Odznaka: w Treści EN jest “Wrocławska Wolność” (Wrocław Freedom), a w zajawce i banerze samo “Wrocław Freedom”. Jeśli UWr używa oficjalnej nazwy angielskiej, warto ją przyjąć.
7. **Annals:** link do artykułu w *Przeglądzie Uniwersyteckim* (polski PDF) mógłby dostać „(in Polish)” (D20). Nie dopisywałem, bo nazwa czasopisma wskazuje język.

## Błędy w polskim tekście (nie poprawiałem)

1. **Hartman.** „drugi — po Stanisławie Drobocie”: pierwszy powojenny wrocławski doktorat z matematyki miał Stefan Drobot (sylwetka Ślebodzińskiego: „Pierwszym był Stefan Drobot (1947)”). Najpewniej powinno być „Stefanie Drobocie”. W EN zostawiłem wiernie „Stanisław Drobot”; do poprawienia w obu wersjach po potwierdzeniu.
2. **Wolibner.** „Laszlo Székelyhidi” → „László Székelyhidi”. W EN dałem poprawną pisownię.
3. **Wolibner, zajawka.** Jako myślnik jest półpauza „ – ” zamiast pauzy „ — ” używanej na stronie.
4. **Bożejko.**
   - „grupami hiperoctaedralnymi” → „hiperoktaedralnymi”.
   - „Askeya–Wimpa–Kerowa” w tekście, a „Kerova” w źródłach (Kerov).
   - Nagroda Humboldta: tekst podaje 2000 (tak samo „Sukcesy — historia”), a opis źródła Fundacji Humboldta „rok 2001”. Do sprawdzenia.
   - „W 1991 roku został profesorem zwyczajnym”, a w źródłach „profesura 1990” / „prof. nadzw. 1990”. Nie musi to być sprzeczność (inne stanowiska), ale warto sprawdzić.
5. **Duda.** Link przy książce „Historia matematyki w Polsce na tle dziejów nauki i kultury” (2019) prowadzi do artykułu z 2008 roku w „Kwartalniku Historii Nauki i Techniki” („Historia matematyki w Polsce po 1945 r.”). Prawdopodobnie zły adres. W EN link przepisany bez zmian.
6. **Rolski.** „autorem lub współautorem … trzech książek”, a tekst i źródła wymieniają cztery: *Stationary Random Processes…* 1981, *Stochastic Processes for Insurance and Finance* 1999, *Podstawy…* 2004 i *Lectures on Monte Carlo Theory* 2025. Do sprawdzenia, czy „trzech” jest zamierzone.
7. **Tao (historia).** „na cześć Profesora Eliasa M. Steina” i „prof. Pawła Strzeleckiego” to tytuły innych osób wbrew stylowi „Warto wiedzieć”. W EN je usunąłem.
8. **Styl.** Tytuły prac w „…” zamiast kursywy w sylwetkach Dudy, Bilera, Hartmana, Wolibnera, Narkiewicza i Ślebodzińskiego (por. „Do decyzji”, p. 1).
9. **Drobiazg.** Ślebodziński: „Hugo Steinhausa” (gdzie indziej „Hugona Steinhausa”).

## Wpisy testowe

Brak w moim zakresie.
