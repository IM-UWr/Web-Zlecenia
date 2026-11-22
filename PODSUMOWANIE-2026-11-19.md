# Podsumowanie dnia — 19.11.2026 (praca samodzielna: zlecenia 53 → 54 → 55 → 42)

Na starcie (11:15) żadne z czterech zleceń nie było zaczęte: dziennik kończył się na 52, nie było raportów ani gałęzi z tymi numerami, a stash był bez związku. Zlecenia 51 nie wykonywałem (zastąpione przez 53). Pracowałem w folderze Web-Core; Web-Core-B i tresci-B są nietknięte. Klony treści do pracy: `..\tresci-C`. Żadnych wiadomości ani e-maili nie wysłałem.

## Stan zleceń

| Zlecenie | Stan | Push (repozytorium: commity, godzina) | Podgląd | Raport |
|---|---|---|---|---|
| 53 — autokorekta nagłówków WW, „Zobacz też”, sylwetki opublikowane | **wypchnięte** | Web-Core `b3ece9f8..9c45eb80` 11:36; Web-Instytut `d6b936d..645a832` 11:37 | 44507399240 sukces | `RAPORT-ZLECENIE-53.md` |
| 54 A — styl tekstu WW i źródła | **wypchnięte** | Web-Instytut `645a832..a255edb` 11:46; Web-Core `9c45eb80..f12aeb15` 11:47 | 44508857543 sukces | `RAPORT-ZLECENIE-54.md` |
| 54 B — seminarium wydziałowe znów „Wydarzenie” | **wypchnięte** | Web-Core `f12aeb15..6193ddfd` 11:57; Web-Aktualnosci `eee693e..d9e2f3e` 11:57 | 44510538471 sukces | jw. |
| 55 — portrety sylwetek | **wypchnięte** | Web-Core `6193ddfd..67ac130f` 12:36; Web-Instytut `a255edb..e88a088` 12:38; Web-Ustawienia `1fb08e6..fd49210` 12:40 | 44516354462, 44516690637, 44517040880 sukces | `RAPORT-ZLECENIE-55.md`, `raport-zrzuty/z55-wybor.html` |
| 42 — osoby ze spisu pracowników | **wypchnięte** (etap 0 bez nowych wątpliwości, bez STOP) | Web-Core `67ac130f..608d6337` 13:46; Web-Pracownicy `ff4aec1..19c92b2` 13:49; Web-Instytut `e88a088..d14657e` 13:51; Web-Nauka `51626f2..2db3479` 13:54; 9 × Web-Sem-* 13:56–14:13; Web-Studia `e7e297e..608f1dc` 14:16 (pełna tabela w raporcie) | 14 przebiegów: 13 sukces, jeden anulowany przez kolejkę (po Prawdopodobieństwie), objęty następnym | `RAPORT-ZLECENIE-42.md` | `RAPORT-ZLECENIE-42.md` |

Żadne zlecenie nie zostało zatrzymane. Wszystkie pushe to zwykłe fast-forwardy z gałęzi `praca/NN-…` na `main`, bez force-push i bez revertów. Warunki pushu były spełnione za każdym razem:
- budowa PL i EN;
- testy i kontrole ze zleceń;
- porównanie HTML przed i po bez niewyjaśnionych różnic;
- fetch, rebase i budowa tuż przed pushem;
- ochrona zmian redaktorów (0 zapisów redaktorów od bazy w każdym repozytorium, kontrola przed i po);
- cisza: ostatni zapis redaktora był zawsze starszy niż 20 minut, więc nigdzie nie trzeba było czekać.

Gałęzie robocze zostają lokalnie (nie wypychane).

## Decyzje podjęte domyślnie (szczegóły w raportach)

- **Wszystkie zlecenia:** push bez Twojego „push” i bez wiadomości do redaktorów. Zamiast „wieczorem” obowiązywała cisza 20 min (polecenie z rana).
- **53:**
  - baner listy w budowie publicznej mówi „18 sylwetek”, nie „17”, bo żadna sylwetka nie jest już TBA;
  - zasada „osoba żyjąca = szkic” w opisie kolekcji i ściągawce zostaje. **Pytanie do Ciebie:** zostawić czy zmienić na „przed publikacją redaktor uzyskuje akceptację”?
- **54 A:**
  - skrypt zapisany do `.przekazanie\zlecenia\zlecenie54.py` bez poprawek, `--sprawdz` pasował;
  - pilnowanie stylu przez ostrzeżenia, nie automatyczne zdejmowanie pogrubień (rekomendacja w raporcie).
- **54 B:**
  - tytuły dwóch wpisów zmienione według tabeli B5;
  - scenariusz 12 symulatora napisany od nowa zamiast cofania `5dd156f5`;
  - opis pola „Rodzaj” bez cudzysłowu YAML.
- **55:**
  - warianty 2b, 3b, **4a** (Ślebodziński, domena publiczna według Commons), 8b, 13b, 14b;
  - Hulanicki z powiększeniem ×3,57 zamiast portretu zastępczego;
  - oryginały z Commons przez `thumb.php`, Steinhaus z miniatury 1280 px (Wikimedia zwracała 429);
  - wariant B (Real-ESRGAN) pominięty, bo wymagałby pobrania i uruchomienia zewnętrznego programu;
  - podpisy dokładnie z załącznika A;
  - ewentualne zmiany wieczorem przez `kadry.json` (instrukcja w raporcie 55).
- **42:**
  - nazwy pól `…_ze_spisu` / `…_spoza`, w władzach `osoba` z grupą „Inne dane niż w spisie”;
  - wartość pola „ze spisu” to ścieżka pliku katalogu (jak w Studiach);
  - stare pola tekstowe strona dalej czyta;
  - kierownicy grantów na listach z aktualnym tytułem i pełnym imieniem ze spisu;
  - koordynatorzy w kolejności: ze spisu, potem spoza;
  - nikogo nie oznaczyłem jako byłego pracownika (`pracuje: true` u wszystkich 128 osób);
  - usuwanie osób w CMS wyłączone;
  - byli pracownicy na liście wyboru z dopiskiem „(były pracownik)”, bez sortowania, bo Pages CMS go nie ma;
  - automat katalogu wyłączony zmienną do czasu ustawienia kluczy;
  - z katalogu Web-Studia usunięty nieaktualny duplikat (bez odwołań).

## Co obejrzeć na Podglądzie (https://im-uwr.github.io/Web-Podglad/)

- 53/54 A: https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/krzysztof-tabisz/ (i `/en/instytut/warto-wiedziec/krzysztof-tabisz/`), https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/marek-bozejko/ i https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/tomasz-rolski/ (sekcja „Zobacz też”, rozwiń „Źródła”), https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/bronislaw-knaster/
- 54 B: https://im-uwr.github.io/Web-Podglad/aktualnosci/2026-11-10-seminarium-wydzialowe-problem-milenijny/ i https://im-uwr.github.io/Web-Podglad/kalendarz/#archiwum
- 55: https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/ (lista z portretami), https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/hugo-steinhaus/, https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/andrzej-hulanicki/ (największe powiększenie), https://im-uwr.github.io/Web-Podglad/instytut/warto-wiedziec/wladyslaw-slebodzinski/ (wariant 4a), https://im-uwr.github.io/Web-Podglad/o-stronie/#portrety (i `/en/o-stronie/#portrety`); arkusz wyboru lokalnie: `raport-zrzuty\z55-wybor.html`
- 42:
  - https://im-uwr.github.io/Web-Podglad/instytut/zaklady/geometria/ (lista grantów: kierownicy z imieniem i tytułem ze spisu)
  - https://im-uwr.github.io/Web-Podglad/nauka/granty/2025-2024-53-n-st1-02294/ (grant z przykładu z 13.11: ma teraz zakład)
  - https://im-uwr.github.io/Web-Podglad/seminaria/topologia/ i https://im-uwr.github.io/Web-Podglad/seminaria/analiza-harmoniczna/ (koordynatorzy: ze spisu, potem spoza)
  - https://im-uwr.github.io/Web-Podglad/instytut/wladze/ (bez zmian w wyglądzie)
  - w CMS: formularz grantu (Web-Nauka), zakładu i władz (Web-Instytut), seminarium, osoby (Web-Pracownicy: pole „Pracuje w Instytucie”, brak przycisku usuwania) — lista wyboru osób i jej wygląd (patrz „Rzeczy do sprawdzenia w CMS” w raporcie 42)

## Przegląd zapisów redaktorów — jutro (20.11), 24 h po pushach

Skrypt (tylko czyta): `sh ../tresci-C/przeglad-24h.sh` (Git Bash, w folderze Web-Core). Dla każdego repozytorium wypisuje zapisy na `main` po pushu i „podejrzane” linie, czyli ślady formularza otwartego przed pushem i zapisanego po nim. Znalezione poprawić osobnym commitem z wartością z historii.

| Repozytorium | Pushe 19.11 | Przegląd od | Na co patrzeć |
|---|---|---|---|
| Web-Instytut | 11:37 (53), 11:46 (54 A), 12:38 (55), 13:51 (42) | 20.11, 13:51 (całość od 11:37) | 53: `opublikowany: false` albo „Do pobrania” z powrotem w 6 sylwetkach; 54 A: pogrubienia i myślniki z powrotem w sylwetkach (przy zapisie starą kartą); 55: zniknięte `obraz` / `obraz_zrodlo` w 16 sylwetkach; 42: stare `karta.kierownik`, `imie_nazwisko`, `sekretariat.osoby` z powrotem albo zniknięte `kierownik_ze_spisu`, `osoba`, `osoby_ze_spisu` |
| Web-Aktualnosci | 11:57 (54 B) | 20.11, 11:57 | stary rodzaj „Seminarium wydziałowe” w nowych wpisach |
| Web-Ustawienia | 12:40 (55) | 20.11, 12:40 | fragment `#portrety` w „O stronie” bez zmian |
| Web-Pracownicy | 13:49 (42) | 20.11, 13:49 | czy każdy `pracuje: false` jest celowy; brak usuniętych plików |
| Web-Nauka | 13:54 (42) | 20.11, 13:54 | stare `kierownik:` z powrotem albo zniknięte `kierownik_ze_spisu` / `kierownik_spoza` |
| Web-Sem-* (9) | 13:56–14:13 (42) | 20.11, od 14:13 | stare `prowadzacy:` z powrotem albo zniknięte `prowadzacy_ze_spisu` / `prowadzacy_spoza` |
| Web-Studia | 14:16 (42) | 20.11, 14:16 | opiekunowie specjalności bez zmian (pole `osoba`) |

## Zgody na zdjęcia (zlecenie 55; nic nie wysłano)

Prośba do każdego adresata: zgoda na publikację zdjęcia w wersji wykadrowanej i wyostrzonej, autor zdjęcia do podpisu i (gdzie warto) większy skan. Adresy kontaktowe są w `RAPORT-ZLECENIE-55.md`, sekcja „Zgody przed startem”, razem z gotowym pismem do Archiwum UWr.

| Osoba | Wariant | Do kogo |
|---|---|---|
| Edward Marczewski | 2b | Archiwum UWr (jedno pismo dla Marczewskiego, Knastera, Hartmana, Ślebodzińskiego, Wolibnera, Perkala) |
| Bronisław Knaster | 3b | Archiwum UWr |
| Stanisław Hartman | 7 | Archiwum UWr (też skan samej fotografii) |
| Władysław Ślebodziński | 4a | użytkownik Commons albo rodzina (podstawa domeny publicznej) |
| Julian Perkal | 6 | PTB albo Archiwum UWr |
| Czesław Ryll-Nardzewski | 8b | Centrum Rylla-Nardzewskiego (PWr) |
| Jan Mycielski | 10 | redakcja UWr albo webmaster IM |
| Andrzej Krzywicki | 12 | osoba sama albo webmaster IM (większy oryginał) |
| Roman Duda | 13b | CNMiF PŁ |
| Władysław Narkiewicz | 14b | J. Shallit / galeria University of Waterloo |
| Piotr Biler | 15 | PAN (biuro prasowe) |
| Tomasz Rolski | 17 | osoba sama |
| Krzysztof Tabisz | 18 | osoba sama albo webmaster IM |

- **Osoby żyjące:** Krzywicki, Duda, Narkiewicz, Biler, Rolski, Tabisz. Zgodę na wizerunek załatwiają redaktorzy razem z akceptacją tekstu, przed startem strony.
- **Bez zgody** (wolna licencja albo domena publiczna): Steinhaus, Urbanik, Hulanicki.
- **Bożejko:** nie ma dziś zdjęcia, trzeba poprosić o nie.
- **Wolibner:** najpierw skan z Archiwum UWr.
- **Większe pliki Jacobsa:** tylko jeśli ich chcesz, wtedy zgoda MFO.

## Klucze automatu katalogu pracowników (zlecenie 42) — co kliknąć

Do czasu tych kroków katalog odświeżam ręcznie skryptem (`node skrypty/synchronizuj-katalog-pracownikow.mjs <Web-Pracownicy> <repo…>` w Web-Core). Dziś zrobione dla 12 repozytoriów.

1. Aplikacja powiadomień organizacji (ta z `powiadom.yml`): Settings → Developer settings → GitHub Apps → aplikacja → Permissions → Repository permissions → **Contents: Read and write**. Jeśli trzeba, w Installed GitHub Apps kliknij **Accept new permissions**. Najpewniej to już jest, bo wymaga tego sygnał do Web-Core.
2. IM-UWr → Settings → GitHub Apps → aplikacja → Configure → Repository access → dodaj **Web-Instytut, Web-Nauka, Web-Studia i 9 × Web-Sem-*** (Analiza-Harmoniczna, Dydaktyka, Dyskretna-Analiza-Harmoniczna, Geometria, Prawdopodobienstwo, Rownania-Rozniczkowe, Statystyka, Teoria-Modeli, Topologia) → Save.
3. IM-UWr/Web-Pracownicy → Settings → Secrets and variables → Actions → Variables → New repository variable: **`KATALOG_PRACOWNIKOW` = `wlaczony`**.
4. Próba: Web-Pracownicy → Actions → „Katalog pracowników w CMS” → Run workflow z zaznaczonym „Tylko pokaż, co by się zmieniło”. Oczekiwany wynik: zielony przebieg, 12 × „katalog 128 osób, zmian: 0”.

Od tej chwili automat działa sam: po każdej zmianie spisu, codziennie o 4:17 i ręcznie. Szczegóły i objawy braków są w `RAPORT-ZLECENIE-42.md`.

## Do Twojej decyzji (zebrane z raportów)

- **53:** zasada „osoba żyjąca = szkic”: zostaje czy zmienić?
- **54:**
  - pilnowanie stylu: ostrzeżenia (rekomendacja) czy automatyczne zdejmowanie pogrubień?
  - zajawka pod tytułem w 8 wierszach wydarzeń w Kalendarzu?
- **55:**
  - Ślebodziński 4a czy 4b?
  - Hulanicki: zostaje czy portret zastępczy?
  - wysłać pismo do Archiwum UWr?
- **42:**
  - które osoby odznaczyć jako byłych pracowników? Lista 23 emerytów jest w raporcie. Uwaga: odznaczenie usuwa osobę też z grupy „Emeryci” na stronie;
  - czy kolumna „ze spisu” w widoku listy CMS (ścieżka pliku) przeszkadza;
  - PDF-y dla redaktorów: lista zmian w raporcie, do następnego generowania.
