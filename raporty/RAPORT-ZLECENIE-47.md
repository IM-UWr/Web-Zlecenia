# Raport: zlecenie 47, „Warto wiedzieć” pod Instytutem (18.11.2026)

**Status:** zrobione lokalnie, **nic nie wypchnięte**. Czeka na „push” razem ze zleceniami 48 i 46 (jedno STOP na końcu serii). Test w CMS z właścicielem po pushu (lista niżej).

| Repozytorium | Gałąź lokalna | Commit(y) | Baza (HEAD main na starcie) |
|---|---|---|---|
| Web-Core (worktree `Web-Core-B`) | `praca/47-warto-wiedziec`; poprawka po pytaniu 1 na szczycie serii (`praca/46-zajawka`) | `1e479c91`, `4e1d4c62` | `3cde30e0` (origin/main) |
| Web-Instytut (`tresci-B`) | `praca/47-warto-wiedziec` | `ef36a18`, `b5e9faa` | `013024d` |
| Web-Ustawienia (`tresci-B`) | `praca/47-warto-wiedziec` | `50d5cde` | `fb4bbfc` |

Warunki ze zlecenia sprawdzone na świeżym `origin/main` (git fetch): zlecenia 33 i 40 są na `main` (przełącznik „Opublikowane”, `widoczny()`, `formularze_40.mjs`, jawny Markdown).

Budowy: „przed” = `tresci-B/z47-przed` (origin/main + klony na bazie), „po” = `tresci-B/z47-po` (gałąź 47 + klony z migracją), „test” = `tresci-B/z47-test` (jak „po”, ale „Dodano” = 18.11.2026 u Bożejki, Rolskiego i Bilera — tylko na czas budowy), „flaga” = `tresci-B/z47-flaga` (`TYLKO_OPUBLIKOWANE=1`, tylko lokalnie; flagi nigdzie nie ustawiałem).

## Co jest zrobione

**Treści (Web-Instytut), skrypt `skrypty/migracja/warto_wiedziec_47.py`** (idempotentny, ze STOP przy konflikcie z redaktorem):
- 18 sylwetek, 6 nagród, 9 historii z załącznika A w `src/content/warto_wiedziec/{sylwetki,nagrody,historie}/` (pliki znak w znak z załącznikiem, poza czterema przeniesionymi niżej);
- cztery dzisiejsze wpisy przeniesione `git mv` i scalone trójstronnie (`git merge-file`: baza `88d8f50`, „nasza” = main, „ich” = załącznik A), więc zmiany redaktorów i tłumaczenia EN zostają: Annals i Tao → `historie/`, PKA → `nagrody/`, tekst listy → `strony/instytut/warto-wiedziec.md`. Od `88d8f50` do bazy nikt tych plików nie zmieniał, więc scalenie dało dokładnie pliki z załącznika plus EN;
- stary wpis o medalach (`medale-uniwersytetu-dla-…`) usunięty `git rm`; zastępuje go nagroda `medal-uniwersytetu.md`, stary adres przekierowuje;
- `src/data/instytut.md`: „4 rektorów” (PL i EN, opis z Łukaszewiczem);
- `--ustawienia`: w menu Instytutu (Web-Ustawienia `nawigacja.json`) „Warto wiedzieć” pierwszą pozycją grupy „Więcej”, nowy opis grupy;
- `--dodano RRRR-MM-DD`: pole „Dodano” u Bożejki, Rolskiego i Bilera (tylko gdy puste). **Uruchamiam w dniu pusha Web-Instytut** (zlecenie: „dzień pusha”); teraz w plikach jest `dodano: ""`.

**Kod (Web-Core):**
- trzy kolekcje `ww_sylwetki`, `ww_nagrody`, `ww_historie` (`src/content.config.ts`), wspólny moduł `src/lib/wartoWiedziec.ts` (płaski adres `/instytut/warto-wiedziec/<plik>`, widoczność, powiązania, losowanie) i czyste funkcje `src/lib/ww.mjs` (`parsujLata`, `:::w-skrocie`, `:::laureaci`, powiązania z linków, rocznice, wybór na stronę główną);
- strony `src/pages/{,en/}instytut/warto-wiedziec/` (lista i wpis), widoki `ListaWartoWiedziec.astro`, `SylwetkaWW.astro`, `WartoWiedziecWpis.astro`, komponenty `src/components/ww/`, style `src/styles/warto-wiedziec.css`;
- przekierowania ze starych adresów `/warto-wiedziec/…` (PL i EN, z kotwicą) na nowe;
- lista: baner (hasło + „81 lat · 17 sylwetek · 4 rektorów UWr”, liczby liczone z treści), wstęp, siatka sylwetek, nagrody, oś czasu historii; bez przełącznika widoków i wyszukiwarki; bez „Następnej strony w dziale” (zostaje „Zgłoś błąd”);
- sylwetka: placeholder, lata raz pod portretem (`parsujLata`), „W skrócie” z linkami, sekcje z Treści, „Do pobrania”, „W »Warto wiedzieć«” tylko z nagrodami i historiami, zwinięte „Źródła”, 4 losowe „Inne sylwetki”, TBA przy pustej Treści;
- jawne bloki `:::w-skrocie` i `:::laureaci` (`remark-jawne-bloki.mjs`, `rehype-bloki.mjs`): licznik laureatów, mini portrety, złe linie pomijane (ostrzeżenie w logu, budowa idzie dalej);
- oś czasu (`src/lib/wwSkrypty.ts`, `OS_JS`): rozsuwanie punktów, panel stałej wysokości, mysz, dotyk, klawiatura, start od rocznicy w ±7 dni, inaczej od najstarszej; bez JS lista;
- strona główna (`DrugiEkran.astro`, `GLOWNA_JS`): 4 miejsca na komputerze, 3 na telefonie; rocznica ±7 dni, „Zawsze pokazuj”, „Nowa sylwetka” (30 dni od „Dodano”), losowanie z wagami (ulubione ×3); bez laureatów i TBA; mała twarz przy sylwetce;
- „Nowe” na liście przez 30 dni od „Dodano”, znika samo (liczone przy budowie i w przeglądarce);
- szkice: osoby żyjące (Bożejko, Biler, Duda, Krzywicki, Narkiewicz, Rolski) mają `opublikowany: false`: na Podglądzie z etykietą „szkic”, przy `TYLKO_OPUBLIKOWANE=1` znikają z siatki, liczb, „Innych sylwetek”, strony głównej, mapy strony i wyszukiwarki; linki do nich stają się tekstem;
- Podgląd: plakietka stanu budowy i link „Edytuj w CMS” prowadzą do właściwego formularza (`ww_sylwetki`/`ww_nagrody`/`ww_historie`, `podglad.ts`, `test-stanu-budowy.mjs`);
- poprawki: Marczewski rektor 1953–1957 (`patroni.ts`, `dok/en/TLUMACZENIA.md`), „4 rektorów” na stronie Instytutu;
- EN: interfejs przetłumaczony (tabela w `dok/en/TLUMACZENIA.md`), pusta Treść EN daje ramkę „Translation in preparation”.

**CMS (Web-Instytut `.pages.yml`, przez `skrypty/migracja/formularze_40.mjs`):** grupa „Warto wiedzieć” (`type: group`) z trzema formularzami: Sylwetki, Nagrody i wyróżnienia, Historie. Formularze według wzoru Studiów (opisy, przykłady), `dodano` z `default: ""`, nazwa pliku z tytułu (`{primary}`), szablony Treści (sylwetka = komentarze → TBA). Pola opisane w `.przekazanie/pola-do-cms.md` (zlecenie 47).

**Kontrole treści:** `sprawdz_tresci.py` (nowe ostrzeżenia dla WW: data „Dodano”, rocznice MM-DD, rok historii, pole „Lata”, duplikat nazwy pliku w grupach), `sprawdz-jawny-markdown.mjs` (grupa WW, złe linie bloków), `skrypty/szerokosci/pomiar.cjs` (dwie nowe strony).

**Dokumentacja:** `dok/sciagawka-edytora.md` (nowa sekcja „Warto wiedzieć”, tabela „Gdzie co jest”, jawny Markdown, „Szkic”), `dok/jawny-markdown.md` (bloki `:::w-skrocie`, `:::laureaci`), `dok/dla-redaktorow/mapa-cms.html` (grupa trzech formularzy), `dok/en/TLUMACZENIA.md`.

## Poprawki w trakcie odbioru
- **Oś czasu, dotyk:** w prototypie pierwsze stuknięcie od razu przechodziło do strony, bo fokus (między `pointerdown` a `click`) sam przełączał kartę i porównanie „czy ten punkt jest pokazany” zawsze wychodziło „tak”. Teraz stan sprzed dotknięcia jest zapamiętany przy `pointerdown`: pierwsze stuknięcie pokazuje kartę, drugie przechodzi.
- **Strona główna, etykieta „szkic” (Podgląd):** w rzędzie „Warto wiedzieć” etykieta dostawała styl roku (duża czcionka) i rozciągała się na wysokość wiersza. Teraz wygląda jak w innych miejscach i stoi przy tytule.
- **Formularz „Historie”:** Pages CMS nie sprawdza pól w całkiem pustej, niewymaganej grupie, więc historia bez roku przechodziła zapis (wykryła to symulacja). Grupa „Karta” ma teraz `required: true` i rok jest wymagany zawsze.
- **Laureat „prof. [sylwetka]”:** cały napis („prof. Marek Bożejko”) jest linkiem z mini portretem, jak w prototypie (test w `ww.test.mjs`).

## Odstępstwa od zlecenia i powody
1. **„Dodano” ustawiam w dniu pusha**, nie teraz (zlecenie: dzień pusha Web-Instytut). Do tego czasu „Nowa sylwetka” i „Nowe” sprawdzone na budowie testowej z datą 18.11.
2. **Bez JS ciekawostka na „Infrastrukturze informatycznej” jest inna** (Wymiar i miara zamiast Odległości Marczewskiego–Steinhausa): stały przydział ciekawostek idzie za kolejnością menu działu, a nowa pozycja w „Więcej” przesuwa przydział na stronach po niej. Z JS ciekawostki i tak się losują. Nie zmieniałem algorytmu.
3. **Strona główna EN** losuje tylko wpisy z Treścią EN (tak liczy się „ma stronę” w wersji angielskiej). Dziś to 3 wpisy: Annals, Tao, PKA; Steinhaus 14.01 pojawi się w EN dopiero po tłumaczeniu.
4. **„Ulubione ×3” w 100 losowaniach wyszło ×2,5:** waga to 3, ale losowanie jest bez powtórzeń w 4 miejscach, a część miejsc zajmują rocznice i „Nowa sylwetka”, więc w zliczeniu wychodzi trochę mniej niż 3. Przy jednym miejscu byłoby ×3.
5. **Oś na telefonie (390 px):** pola dotyku punktów mają 30 px, a odstęp środków 24 px, więc pola nachodzą na siebie o 6 px. Tak jest w prototypie (punkty muszą się zmieścić w torze 358 px); stuknięcie trafia w bliższy punkt.
6. **Napis „Zdjęcie” na placeholderze** tylko na Podglądzie (po polsku, dla redaktora); na stronie publicznej sam placeholder.

## Pytania do właściciela
1. **Cztery historie bez „Ludzie w tej historii”**: Pierwsze wykłady, Nowa Księga Szkocka, Taksonomia wrocławska, Aksjomat determinacji. Prototyp brał osoby z pola `osoby`, którego zlecenie nie przenosi (powiązania mają wynikać z linków), a w Treści tych historii nazwiska są pogrubione, nie podlinkowane. Czy zamienić pogrubienia na linki do sylwetek (to zmiana treści, redakcyjna)? Na razie zostawiłem tekst jak w załączniku A.
   **Decyzja właściciela (18.11, ok. 22:30): tak — zrobione.** `warto_wiedziec_47.py` (lista `LINKI_HISTORII`, Web-Core `4e1d4c62`) zamienia pogrubione nazwiska osób z sylwetką na linki `[**…**](/instytut/warto-wiedziec/<sylwetka>)`: Pierwsze wykłady — Steinhaus, Marczewski, Knaster, Ślebodziński; Nowa Księga Szkocka — Steinhaus; Taksonomia wrocławska — Perkal i Steinhaus w pogrubionej liście autorów (Florek, Łukaszewicz i Zubrzycki nie mają sylwetek); Aksjomat determinacji — Mycielski i Steinhaus. Web-Instytut `b5e9faa`, po jednej linii na historię. Skrypt jest idempotentny: historię już dopisaną bez linków uzupełnia. Pełna migracja od bazy `013024d` na czystej kopii daje to samo drzewo co gałąź; jedyna różnica to miejsce klucza `required: true` w grupie „Karta” w `.pages.yml` (ten sam YAML).
   Budowa (`tresci-B/z47p1`) względem wyniku 46: zmienia się tylko 20 stron — 4 historie (pod tekstem „Ludzie w tej historii” / „People in this story”, w spisie „Na tej stronie”) i 6 sylwetek (Steinhaus, Marczewski, Knaster, Ślebodziński, Perkal, Mycielski; w „W »Warto wiedzieć«” dochodzą te historie), PL i EN; plus indeks Pagefind. Linki wewnętrzne: 0 zepsutych. Zrzuty: `raport-zrzuty/z47-zrzuty/z47-historia-*-ludzie-{1920,390}.png`, konsola czysta.
2. **Rolski, „Lata: xxxx”:** ostrzeżenie w logu i w `sprawdz_tresci.py` zgodnie ze zleceniem; czeka na dane od Instytutu.
3. Punkt „pas startowy” w `instytut.md` (decyzja CZEKA): nie ruszałem.

## Odbiór lokalny

**Porównanie HTML przed/po** (całe `dist`, PL i EN, te same klony treści; `raport-zrzuty/z47-html.txt`, skrypt `raport-zrzuty/z47-skrypt/html47.py`): 912 wspólnych plików, 68 nowych (strony `/instytut/warto-wiedziec…` PL i EN), 0 usuniętych. Różnice:
- 769 plików różni się tylko pozycją „Warto wiedzieć” w menu;
- stare adresy `/warto-wiedziec/…` (8 stron + medale PL i EN): przekierowania na nowe adresy;
- strona główna PL i EN: nowy rząd „Warto wiedzieć”;
- strona Instytutu PL i EN: „4 rektorów”, karta grupy „Więcej”, notka Marczewskiego;
- „Kontakt” PL i EN: „Następna strona w dziale” prowadzi teraz do „Warto wiedzieć” (następna pozycja menu);
- „Struktura”, „Władze”, „Pracownicy” i „Kontakt”: w skrypcie ciekawostek lista stron działu ma nową pozycję (z menu);
- „Infrastruktura informatyczna” PL i EN: inna ciekawostka bez JS (odstępstwo 2);
- `sitemap.xml`: nowe adresy; pliki `kalendarz/*.ics` i `seminaria/powiadomienia.json`: tylko znacznik czasu budowy (`DTSTAMP`, `wygenerowano`; sprawdzone bez tych linii: identyczne).

Poza tym bez różnic.

**Testy jednostkowe** (`npm run test:jawne`, w tym nowy `src/plugins/ww.test.mjs`): 76/76. Pokrywają: `parsujLata` (przykłady z punktu 5, `xxxx`, pusto), `:::w-skrocie` (link w podpisie, pominięcie lat życia, zła linia), `:::laureaci` (z linkiem do sylwetki, bez, bez części po ` — `, zła linia, licznik, link do szkicu przy fladze, „prof. [sylwetka]”), powiązania z linków, duplikat nazwy pliku.

**Oś czasu i strona główna** (Playwright, Edge, `Europe/Warsaw`, `page.clock.setFixedTime`; `raport-zrzuty/z47-skrypt/testy47.mjs`, budowa testowa): 36/36 OK.
- 9 punktów bez nakładania przy 1920, 1366, 1024 (odstęp środków ≥ 30 px) i 390 px (≥ 24 px), wszystkie w torze; panel stałej wysokości;
- mysz (najechanie), klawiatura (strzałki z zawijaniem), dotyk (pierwsze stuknięcie pokazuje kartę, drugie przechodzi);
- start 18.11 → 1945 (rocznica pierwszych wykładów 15.11), 1.03.2027 → 1945 (najstarsze), 4.09.2027 → 2017 (Tao); bez JS lista 9 wydarzeń;
- strona główna 18.11.2026: Marczewski „119. urodziny · 15 listopada”, 1945 „81 lat temu · 15 listopada”, Bożejko „Nowa sylwetka”, czwarta losowa; telefon: te same trzy;
- 14.01.2027: Steinhaus „140. urodziny · 14 stycznia”; 20.12.2026: bez „Nowa sylwetka” (minęło 30 dni);
- 100 losowań: ulubione średnio ×2,8 częściej (odstępstwo 4); w puli nigdy TBA (Tabisz) ani nagrody z laureatami;
- konsola czysta na wszystkich stronach testu.

**Budowa z `TYLKO_OPUBLIKOWANE=1`** (`tresci-B/z47-flaga`, tylko lokalnie): 6 szkiców osób żyjących znika z siatki, liczb („11 sylwetek”), „Innych sylwetek”, strony głównej, mapy strony i wyszukiwarki (Pagefind); linki do nich w laureatach i tekstach innych sylwetek są zwykłym tekstem (`[szkice]` w logu).

**Zrzuty** (`raport-zrzuty/z47-zrzuty/`, 112 plików; tryb jasny i ciemny; 1920×1080, 1366×768, 1024×768, 390×844; budowa testowa): lista, Steinhaus, Bożejko (z „Do pobrania” i „szkicem”), Rolski („xxxx”), Tabisz (TBA), Stypendium Steinhausa, Medal UWr, Pierwsze wykłady, EN Annals, EN Steinhaus („Translation in preparation”), strona główna, menu Instytutu. Konsola czysta.

**Kontrole:**
- `astro check`: 0 błędów, 0 ostrzeżeń (4 podpowiedzi, jak przed zmianą);
- `sprawdz_pola_cms.py ../tresci-B`: 756 plików w 16 repozytoriach, 0 problemów;
- `sprawdz_tresci.py`: 597 plików, 1 ostrzeżenie: Rolski „Lata: nie data („xxxx”)” (zgodnie ze zleceniem; to samo w logu budowy);
- `sprawdz-jawny-markdown.mjs`: Web-Instytut OK (33 wpisy „Warto wiedzieć”, 0 złych linii bloków), Web-Ustawienia OK; 2 nagłówki bez `{#id}` („Dane bibliograficzne” w Annals, PL i EN) są tam od bazy;
- **linki**: lychee nie jest zainstalowany na tym komputerze, więc jak w zleceniu 45 własne sprawdzenie plików i kotwic z `.github/qa/qa.py` (to samo, co QA w Actions robi obok lychee): 0 zepsutych linków wewnętrznych przed i po (797 → 865 stron); 11 nieistniejących kotwic, te same co przed; noty PDF `/pliki/aktualnosci/marekbozejkonotabiograficzna.pdf` i `…/tomaszrolskinotabiograficzna.pdf` istnieją.

**Symulacja zapisu w CMS** (`skrypty/test-edytora/formularz.mjs ../tresci-B`, log `tresci-B/z47-formularz.log`):
- scenariusz 10a (nowa sylwetka z szablonu „Władysław Żółkiewski Test”): nazwa pliku `wladyslaw-zolkiewski-test.md`, Treść = same komentarze (TBA), „Dodano” puste, „Opublikowane” zaznaczone — OK;
- 10b (historia bez roku i z rokiem „19xx”): zapis zablokowany — OK (po poprawce `required: true`);
- 10c (dopisanie laureata do Medalu UWr): licznik 2 → 3, poza Treścią bez zmian — OK;
- zapis bez zmian wszystkich 756 plików: wszystkie 33 wpisy „Warto wiedzieć”, `instytut.md` i `nawigacja.json` bez różnic; bloki `:::w-skrocie`, `:::laureaci`, `:::pliki` przeżywają zapis znak w znak. Skrypt zgłasza 6 różnic w plikach spoza zlecenia (5 obron i 1 grant dostają szablon Treści przy pierwszym zapisie) — znane działanie ze zlecenia 40 (raport 40-3, opisane też w raporcie 45).

## Test w CMS z właścicielem (po pushu)
1. Web-Instytut: w menu CMS grupa „Warto wiedzieć” z trzema formularzami: Sylwetki, Nagrody i wyróżnienia, Historie.
2. Otworzyć sylwetkę Steinhausa i zapisać bez zmian: w GitHub brak commita albo commit bez zmian w pliku.
3. Nowa sylwetka (np. „Test Testowy”): nazwa pliku `test-testowy.md`, „Dodano” puste, Podgląd pokazuje TBA; potem usunąć plik.
4. Medal Uniwersytetu: dopisać linię laureata w bloku `:::laureaci`, zapisać; na Podglądzie licznik +1; potem cofnąć.
5. Historia bez roku: CMS nie pozwala zapisać („Wpisz rok, np. 1946”).
6. Podgląd: na wpisie-szkicu (np. Bożejko) plakietka stanu budowy prowadzi do formularza „Sylwetki”.

## Push (zrobię po „push”)
1. Web-Core: rebase serii 47–48–46 na `origin/main`, push `main`.
2. Web-Instytut: kontrola zapisów redaktorów od `013024d` (`git log 013024d..origin/main`). Jeśli przybyły w plikach migracji, ponowię `warto_wiedziec_47.py` i `formularze_40.mjs` na świeżym `main` (skrypt scala trójstronnie i zatrzymuje się przy konflikcie). Przed pushem `--dodano <dzień pusha>`, potem push i kontrola pole po polu.
3. Web-Ustawienia: tak samo od `fb4bbfc` (menu przez `--ustawienia`).
4. Następnego dnia przegląd zapisów redaktorów z 24 h.

## Push (18.11.2026, po „push” właściciela)
- **Web-Core:** `3cde30e0..4e1d4c62` (seria 47 → 48 → 46 → poprawka 47, przewinięcie, bez rebase — `origin/main` się nie ruszył).
- **Web-Instytut:** kontrola zapisów redaktorów od bazy `013024d` tuż przed pushem: 0 nowych commitów, więc migracja bez powtórki. `--dodano 2026-11-18` (Bożejko, Rolski, Biler; commit `5f68249`, 3 linie). Push `013024d..5f68249`. Po pushu `origin/main` = gałąź; zmiana od bazy = tylko commity zlecenia (38 plików), 0 zapisów redaktorów po drodze, 0 nowych po pushu.
- **Web-Ustawienia:** od bazy `fb4bbfc` 0 nowych; push `fb4bbfc..50d5cde` (`nawigacja.json`, „Warto wiedzieć” w grupie „Więcej”); po pushu 0 nowych.
- Pole po polu: od bazy nie było zapisów redaktorów, więc nie było czego scalać. Pliki zmienione migracją (cztery przeniesione wpisy, `instytut.md`) mają dane jak w odbiorze lokalnym. „Dodano” zmienia tylko wartość `dodano` w trzech plikach.
- Do zrobienia: test w CMS z właścicielem (lista wyżej), jutro przegląd zapisów redaktorów z 24 h.
