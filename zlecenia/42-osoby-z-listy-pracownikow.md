# Zlecenie 42: osoby w formularzach CMS wybierane z listy pracowników; osoby, które odeszły (punkt 14 kolejki) (18.11.2026)

**Decyzje właściciela:**
- **13.11 (kolejka, punkt 14):**
  - zamiast wpisywać nazwiska ręcznie, w CMS wybiera się osobę z listy pracowników, a lista sama się aktualizuje po zmianie spisu;
  - osobę spoza spisu da się wpisać ręcznie.
- **18.11, 00:28–00:36: osoby, które odchodzą** („Ok, to ma sens”):
  - **Funkcje bieżące z wyborem ze spisu** (kierownik zakładu, koordynator seminarium, opiekun specjalności, osoba w sekretariacie, dyrekcja Instytutu i władze Wydziału):
    - na Podglądzie w miejscu osoby znacznik „nie przypisano osoby — uzupełnij w CMS”;
    - na stronie publicznej wiersz z tą funkcją znika.
  - **Historia** (kierownik i wykonawcy grantu, promotorzy i recenzenci obrony): nazwisko zostaje jako zwykły tekst, bez linku. Ta osoba naprawdę pełniła tę rolę.
  - **Pliku osoby w spisie nie kasujemy.** Zamiast tego przełącznik „Pracuje w Instytucie”.
- **18.11, 01:49–01:55, przy migracji:**
  - **nikogo nie oznaczamy jako byłego pracownika**: wszyscy w spisie dostają `pracuje: true`, a właściciel sam odznaczy osoby w CMS;
  - **tabela przypisań:** brak przypisań ręcznych (przegląd z 18.11 w etapie 0). Niedopasowane nazwiska idą do „spoza spisu”;
  - etap 0 robisz jako kontrolę. **STOP tylko wtedy, gdy wyjdą przypadki niejednoznaczne albo podejrzane**, których nie było w przeglądzie z 18.11.
- **18.11, 01:54: wybór z listy tylko tam, gdzie coś daje.** Pole dostaje wybór ze spisu tylko wtedy, gdy strona bierze z osoby dane: zakład, tytuł, link, e-mail, telefon, pokój. Gdzie strona pokazuje sam wpisany tekst, zostaje zwykłe wpisywanie (kolumna „Formularz” w tabeli niżej).
- **18.11, 01:58: dyrekcja też automatycznie.**
  - `src/lib/widoki/wladze.ts` już dziś szuka osoby w spisie po dokładnym imieniu i nazwisku i bierze stamtąd stopień, e-mail, pokój i stronę; pola w formularzu tylko je nadpisują.
  - Dyrekcja i władze Wydziału dostają więc wybór ze spisu.
  - Ręcznie zostają rola, zakres obowiązków, dyżur, zdjęcie (spis nie ma zdjęć) i ich wersje EN.
  - Pola nadpisujące (e-mail, pokój, stopień, strona) zostają jako opcjonalne „tylko jeśli inne niż w spisie”. Władze Wydziału mają dziś e-maile `@uwr.edu.pl` zamiast tych ze spisu i nie biorą pokoju ze spisu (`zeSpisuPokoj = false`).

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- **Repozytoria treści:**
  - zasady z kolejki, punkt 3: świeży `main`, zwykły commit, nigdy force-push; najpierw Web-Core, potem treści; `.pages.yml` i dane jednego repozytorium w jednym commicie;
  - do tego sekcja „Ochrona zmian redaktorów” niżej.
- **Kolejka:** okno 1, po zleceniu 40 (formularze przyjazne jak w Studiach) i po 33 (flaga `TYLKO_OPUBLIKOWANE`, czyli tryb strony publicznej).
- Jedno repozytorium treści = osobny commit i osobna kontrola.
- Raport `RAPORT-ZLECENIE-42.md`, zrzuty `raport-zrzuty/z42-*`. Bez subagentów.

## Ochrona zmian redaktorów (obowiązkowo przy każdym pushu do repozytorium treści)
Redaktorzy zapisują w CMS na żywo, także w trakcie tego zlecenia. Ich zmiany nie mogą zginąć.

1. **Migracja na najświeższej wersji.**
   - Tuż przed pushem: `git fetch` i sprawdź, czy na `main` przybyły zapisy redaktorów od chwili, gdy zacząłeś (`git log <baza>..origin/main`). Baza = HEAD zanotowany na początku pracy.
   - Jeśli przybyły, nie doklejaj starego wyniku. Przełącz się na świeży `main` i **uruchom skrypt migracji jeszcze raz** na aktualnych plikach.
   - Konflikty rozwiązuj ręcznie: weź wersję redaktora i nanieś na nią swoją zmianę. Nigdy odwrotnie i nigdy hurtem całych plików (`-X ours`, `checkout --ours/--theirs`).
2. **Kontrola przed pushem** (skrypt, wynik w raporcie):
   - weź każdy zapis redaktora od bazy (autor inny niż Code) i każdy plik, który zmienił;
   - porównaj pole po polu jego wersję z wersją, którą wypychasz;
   - każda wartość wpisana przez redaktora musi być w wyniku: bez zmian albo przeniesiona zgodnie z migracją (nazwisko → identyfikator ze spisu albo pole „spoza spisu”). Inaczej **STOP**.
3. **Kontrola po pushu:** porównanie pole po polu całego repozytorium przed i po. Różnice tylko w polach osób; lista w raporcie.
4. **Okno pusha:** wieczorem albo po wiadomości od właściciela do redaktorów: „zapiszcie i zamknijcie CMS na 15 minut, potem odświeżcie stronę”.
   - Pages CMS przy zapisie sprawdza wersję pliku. Jeśli plik zmienił się od otwarcia formularza, zapis jest odrzucony („File has changed since you last loaded it”) i nic nie zostaje nadpisane. Redaktor traci jednak to, co wpisał, a nie zapisał.
   - Formularz otwarty przed pushem i zapisany po nim działa jeszcze według starej konfiguracji. **Następnego dnia** przejrzyj zapisy redaktorów z 24 godzin po pushu: czy żaden nie przywrócił starych pól tekstowych ani nie usunął nowych. Znalezione popraw osobnym commitem.
5. **Wszystko da się odwrócić:** każdy zapis redaktora to osobny commit. W razie straty przywróć wartość z historii **nowym commitem** (nigdy `reset` ani force-push) i opisz to w raporcie.

## Stan dziś (18.11)

**Dopasowywanie osób w kodzie.** Pola z osobami to zwykły tekst. Strona zgaduje osobę funkcją `osobaGrantu` (`src/lib/tresci.ts`, ok. linii 81–117):
- ostatni wyraz = nazwisko, pierwsza litera = inicjał, dokładna pisownia;
- brak dopasowania oznacza brak linku i brak zakładu.
- Przykład 13.11: grant „Ekstrema fragmentacji…” (`Web-Nauka/src/content/granty/2025-2024-53-n-st1-02294.md`, kierownik „mgr T. Frączek”) nie ma zakładu, bo w spisie ta osoba to „Tamara Mika” (`tamara-mika.yml`).

**Wzór, który już działa:** opiekunowie specjalności w Web-Studia.
- Pole `opiekunowie` → `osoba` jest typu `reference` do kolekcji „Katalog opiekunów (tylko odczyt)” (`katalog-pracownikow`, pliki `_cms/pracownicy/*.yml`: `imie_nazwisko`, `id`, `etykieta`).
- Katalog tworzy ręcznie skrypt `skrypty/synchronizuj-katalog-opiekunow.mjs`. Skrypt **pomija osoby z `opublikowany: false` i kasuje ich pliki z katalogu**, więc odejście osoby osierociłoby odwołania. To trzeba zmienić.
- Ograniczenie Pages CMS (sprawdzone 13.11): `reference` szuka tylko w tym samym repozytorium, a `select` / `reference` nie przyjmują własnej wartości. Stąd kopia katalogu w każdym repozytorium.

**Pola z osobami** (`.pages.yml`; numery linii z 17.11):

| Repozytorium | Pole | Rodzaj | Co strona bierze dziś ze spisu | **Formularz** |
|---|---|---|---|---|
| Web-Nauka | granty → `kierownik` | historia | zakład grantu (gdy pole „Zakład” puste), tytuł ze spisu (`zakladGrantu`, `kierownicyGrantu`) | **wybór + spoza spisu** |
| Web-Instytut | zakłady → `karta.kierownik` | funkcja | link, e-mail, telefon, pokój (`widoki/zaklad.ts`, dokładne imię i nazwisko) | **wybór** |
| Web-Sem-* (9) | `prowadzacy` („Koordynator”) | funkcja | tytuł i link do strony domowej (`widoki/seminarium.ts`) | **wybór + spoza spisu** |
| Web-Instytut | władze → `sekretariat.osoby` | funkcja | e-mail i telefon („dobiorą się same”) | **wybór** |
| Web-Studia | specjalności → `opiekunowie` | funkcja | kontakt i zakład | wybór (już jest) |
| Web-Instytut | władze → `osoby` (dyrekcja) | funkcja | stopień, e-mail, pokój, strona (`widoki/wladze.ts`, dokładne imię i nazwisko; pola formularza nadpisują) | **wybór**; ręcznie: rola, zakres, dyżur, zdjęcie (+EN); opcjonalne nadpisanie danych |
| Web-Instytut | władze → `wydzial.osoby` | funkcja | stopień, e-mail, strona (pokój nie) | **wybór + spoza spisu** (dziekan może być spoza Instytutu); ręcznie jak wyżej; e-mail `@uwr.edu.pl` jako nadpisanie |
| Web-Nauka | granty → `wykonawcy` | historia | nic (sam tekst, `tytulyWJezyku`) | **tekst, bez zmian** |
| Web-Aktualnosci | obrony → `promotorzy`, `recenzje.recenzent` | historia | nic (sam tekst) | **tekst, bez zmian** |

- **Pola „tekst, bez zmian”:** to zlecenie ich nie rusza. Opisy formularzy poprawia zlecenie 40.
- **Dyrekcja i Wydział** (decyzja 01:58): wybór osoby. Pola ręczne i nadpisania zostają (etap 3).
- **Pozostałe pola tekstowe** (poza zakresem): referaty → `prelegent` (głównie goście), publikacje → `autorzy`, konferencje → `organizatorzy` (ukryte), adresy e-mail `kontakt`.
- **Nowe pola z osobami:** jeśli w etapie 0 znajdziesz inne, dopisz je do tabeli z propozycją według tej samej zasady: wybór tylko tam, gdzie strona bierze dane ze spisu.

## Etap 0. Inwentaryzacja (kontrola; STOP tylko przy nowych wątpliwościach, patrz niżej)
1. **Pola.** Pełna lista pól z osobami we wszystkich repozytoriach z `tresci.json`. Dla każdego pola:
   - rodzaj: funkcja czy historia;
   - ile wpisów;
   - ile wartości pasuje jednoznacznie do spisu, ile niejednoznacznie, ile nie pasuje.
2. **Lista niedopasowanych i niejednoznacznych wartości** z plikiem, polem i propozycją (np. „mgr T. Frączek” → `tamara-mika`?). Właściciel odpowiada tabelą przypisań, a resztę migracja zostawi jako „spoza spisu”.
3. **Spis pracowników:**
   - jak dziś oznaczane są osoby, które odeszły (`grupa: emeryt`, `opublikowany: false`, usunięte pliki — sprawdź historię Web-Pracownicy);
   - ile takich osób jest;
   - czy usunięte pliki występują jeszcze w polach osób.
4. **Pages CMS** (kod źródłowy, `fields/core/reference`, `lib/schema.ts`), dwa pytania:
   - co się dzieje przy otwarciu i zapisie wpisu, którego `reference` wskazuje plik spoza katalogu (wartość znika czy zostaje);
   - czy kolejność pozycji na liście wyboru da się ustawić, np. tak, żeby byli pracownicy byli na końcu.

**Przegląd z 18.11, 01:50** (czat, na klonach `main`; dopasowanie jak w `osobaGrantu`, tylko osoby widoczne w spisie). Liczby tylko dla pól z wyborem:
- **Pewne:** 115 wpisów. Kierownicy grantów 81, koordynatorzy seminariów 16, kierownicy zakładów 9, dyrekcja 5, sekretariat 2, władze Wydziału 2.
- **Niejednoznaczne i podejrzane:** 0.
- **Brak w spisie** (→ „spoza spisu”):
  - 14 wpisów kierowników grantów (Kisielewicz ×3, Jasiulis-Gołdyn ×2, Palmowski, Śniady, Więsław, Iwanow, Krupski, Czarna, Kosiński, Celiński, Kotelnykova);
  - 5 koordynatorów seminariów (Krzysztof Stempak, Paweł Krupski, Robert Rałowski, Szymon Żeberski, Adam Nowak (IM PAN)).
- Grant „Ekstrema fragmentacji…” ma już „mgr T. Mika” (poprawione przez redaktora), więc dopasowuje się sam.
- **Pola tekstowe** (wykonawcy, promotorzy, recenzenci) nie są migrowane.
- **Dyrekcja i Wydział:** wybór dostaje osoba. Pola ręczne (rola, zakres, dyżur, zdjęcie) i dotychczasowe nadpisania (e-maile `@uwr.edu.pl` Wydziału) przenieś bez zmian.

**STOP tylko**, gdy Twój etap 0 znajdzie przypadki niejednoznaczne albo podejrzane spoza tego przeglądu. W przeciwnym razie idź dalej z tabelą przypisań z decyzji 18.11.

## Etap 1. Spis pracowników (Web-Pracownicy)
- **Nowe pole** `pracuje` (boolean, `default: true`):
  - etykieta: „Pracuje w Instytucie”;
  - opis: „Po odejściu odznacz. Nie usuwaj osoby — jej nazwisko zostaje przy dawnych grantach i obronach”;
  - opcjonalnie `data_odejscia` (data, `default: ""`).
- **Migracja:** `pracuje: true` wszędzie, także u osób, które według etapu 0 mogły odejść (decyzja 18.11: nikogo nie oznaczamy). Listę takich osób daj w raporcie; właściciel odznaczy je sam w CMS.
- **Kasowanie w CMS:** `operations: delete: false` w kolekcji pracowników, z opisem „Usuwanie wyłączone: odznacz »Pracuje«”. To ustawienie domyślne, do decyzji właściciela przy odbiorze. Pomyłkowe duplikaty usuwa wtedy właściciel na GitHubie.
- **Strona:**
  - spis pracowników, wyszukiwarka i listy zakładów pokazują tylko `pracuje !== false`;
  - strona profilu osoby, która odeszła, nie powstaje.

## Etap 2. Katalog w każdym repozytorium i automat
- **Jeden skrypt** zastępuje `synchronizuj-katalog-opiekunow.mjs`: np. `skrypty/synchronizuj-katalog-pracownikow.mjs`. Zapisuje `_cms/pracownicy/<id>.yml` w każdym repozytorium, które ma pola osób (Web-Instytut, Web-Nauka, 9 × Web-Sem-*, Web-Studia; Web-Aktualnosci nie, bo jego pola zostają tekstem).
  - Pola: `imie_nazwisko`, `id`, `etykieta`, `pracuje`.
  - Etykieta: przy duplikatach nazwisk jak dziś z grupą; przy `pracuje: false` z dopiskiem „(były pracownik)”, na końcu listy, jeśli Pages CMS na to pozwala (etap 0).
  - **Osób nie usuwa z katalogu.** Plik znika tylko wtedy, gdy osoba zniknęła ze spisu i nie występuje w żadnym polu osób w danym repozytorium. Każde takie usunięcie trafia do logu.
- **Automat:** GitHub Action w Web-Pracownicy.
  - Uruchamia się po pushu na `main` (zmiana spisu), raz na dobę jako zapas i ręcznie.
  - Uruchamia skrypt i commituje zmienione katalogi do repozytoriów: zwykły commit, przy odrzuconym pushu `pull --rebase` i ponowienie, bez force-push.
  - Commituje tylko pliki `_cms/pracownicy/`. Redaktorzy ich nie edytują (`readonly`, `create/rename/delete: false`).
- **Uprawnienia:** automat potrzebuje aplikacji GitHub z zapisem do tych repozytoriów, np. istniejącej `im-uwr-strona-powiadomienia`, która dziś ma dostęp tylko do Web-Podglad. **Klucze i dostęp ustawia właściciel.** Wypisz w raporcie dokładnie, co kliknąć. Do czasu ustawienia skrypt da się uruchomić ręcznie.

## Etap 3. Formularze
Tylko pola oznaczone w tabeli jako **wybór**. Pola „tekst, bez zmian” zostają jak są. Pole „wybór + spoza spisu” zamienia się w dwa pola, ustawione obok siebie. Przy „wybór” (kierownik zakładu, sekretariat) wystarczy samo pole „… ze spisu”, chyba że w etapie 0 znajdziesz tam osoby spoza spisu:
- **„… ze spisu”:** `reference` do `katalog-pracownikow`, lista tam, gdzie osób może być kilka.
  - Opis w stylu Studiów: „Wybierz z listy (wpisz nazwisko). Tytuł, link i zakład strona weźmie ze spisu pracowników”.
- **„… spoza spisu”:** tekst, lista.
  - Opis: „Tylko osoby, których nie ma w spisie (np. recenzent z innej uczelni). Wpisz z tytułem: prof. dr hab. Jan Kowalski”.
- **Kolejność na stronie:** najpierw osoby ze spisu, potem spoza.
- **Dyrekcja i władze Wydziału** (lista obiektów):
  - w pozycji pole „Osoba ze spisu” zamiast `imie_nazwisko` (przy Wydziale także „spoza spisu”);
  - pod nim pola ręczne: rola, zakres, dyżur, zdjęcie i wersje EN;
  - na dole zwinięta grupa „Inne dane niż w spisie (zwykle puste)” z polami e-mail, pokój, stopień i strona.
  - Opis grupy: „Wypełnij tylko, jeśli na tej stronie ma być coś innego niż w spisie pracowników (np. e-mail dziekanatu)”.
- **Wzór Web-Studia:** `opiekunowie` (lista obiektów z polem `osoba`) zostaje, ale przechodzi na wspólny katalog i zasady tego zlecenia.

## Etap 4. Migracja danych (skrypt, według „Ochrony zmian redaktorów”)
- **Przeniesienie wartości.** Tekst trafia do „ze spisu” tylko przy pewnym dopasowaniu (pełne imię i nazwisko po zdjęciu tytułów, albo jednoznaczne nazwisko z inicjałem) albo według tabeli przypisań właściciela z etapu 0. Reszta trafia do „spoza spisu” bez zmian.
- **Raport migracji:** dla każdego pola liczby (do spisu / spoza) i lista przypadków niepewnych.
- **Jednorazowość:** skrypt odmawia ponownego uruchomienia na przerobionych plikach. Wyjątek: uruchomienie od nowa na świeżym `main`, punkt 1 „Ochrony”.

## Etap 5. Strona (Web-Core)
- **Osoba ze spisu:**
  - aktualne imię, nazwisko i tytuł ze spisu (zmiana nazwiska niczego nie psuje);
  - link do profilu i zakład (np. zakład grantu z kierownika, jak dziś);
  - zastępuje `osobaGrantu`. Dopasowywanie po nazwisku zostaje tylko dla pól „spoza spisu”, bez linku.
- **Osoba z `pracuje: false`:**
  - **historia:** imię i nazwisko jako zwykły tekst, bez linku, bez dopisku;
  - **funkcja:** traktowana jak brak osoby (niżej).
- **Funkcja bez osoby** (pusta albo tylko osoby, które odeszły):
  - **Podgląd** (domyślna budowa): w miejscu osoby znacznik „nie przypisano osoby — uzupełnij w CMS”, wyraźny, w stylu etykiety „szkic” ze zlecenia 33. Do tego ostrzeżenie w logu budowy, jako adnotacja widoczna w plakietce stanu budowy (zlecenie 33), z linkiem „Popraw w CMS”.
  - **Strona publiczna** (budowa z `TYLKO_OPUBLIKOWANE=1`): wiersz z tą funkcją się nie pokazuje (np. „Kierownik: …” znika, reszta karty zakładu zostaje).
- **Odwołanie do osoby, której nie ma w spisie ani w katalogu:** ostrzeżenie w budowie, a pozycja jest pomijana. Nie powinno się zdarzać, bo plików nie kasujemy.

## Etap 6. Dokumentacja
- Ściągawka (`dok/sciagawka-edytora.md`):
  - „Osoby wybieraj z listy; ręcznie tylko osoby spoza Instytutu”;
  - „Po odejściu pracownika odznacz »Pracuje«, nie usuwaj”.
- PDF-y dla redaktorów: lista zmian w raporcie.

## Odbiór lokalny
- **Porównanie HTML przed i po** wszystkich stron z osobami (zakłady, dyrekcja, seminaria, specjalności, granty, obrony; PL i EN): 0 różnic.
  - Wyjątki: linki i zakłady, które dziś brakowały, a teraz się pojawiły. Lista w raporcie.
- **Test osoby, która odchodzi** (kopia lokalna, np. kierownik jednego zakładu i kierownik jednego grantu ustawieni na `pracuje: false`):
  - Podgląd: zakład ze znacznikiem „nie przypisano osoby”, grant z nazwiskiem bez linku;
  - budowa z `TYLKO_OPUBLIKOWANE=1`: zakład bez wiersza „Kierownik”, grant jak na Podglądzie;
  - osoba znika ze spisu pracowników;
  - w katalogu ma dopisek „(były pracownik)”.
- **Symulacja CMS** (jak w zleceniu 28, etap 6a):
  - stary grant z kierownikiem, który odszedł, otwarty i zapisany bez zmian: odwołanie zostaje;
  - nowy grant: lista wyboru z nazwiskami.
- **Automat:** na gałęzi testowej albo w trybie „na sucho” pokazuje, które pliki katalogów by zmienił.
- **Kontrole:** `sprawdz_pola_cms.py` 0 problemów, `sprawdz_tresci.py` OK (z nowym ostrzeżeniem o funkcji bez osoby), `astro check` bez nowych błędów.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] W polach oznaczonych w tabeli jako „wybór” osobę wybiera się z listy pracowników (a osobę spoza spisu, gdzie przewidziano, wpisuje ręcznie). Pola tekstowe bez zmian. Lista aktualizuje się sama po zmianie spisu (automat albo, do czasu ustawienia kluczy, skrypt).
- [ ] Osoba, która odeszła: znika ze spisu; przy historii zostaje jako tekst bez linku; przy funkcji Podgląd pokazuje „nie przypisano osoby — uzupełnij w CMS”, a strona publiczna ukrywa wiersz.
- [ ] Pliku osoby nie da się usunąć w CMS (albo decyzja właściciela inaczej); katalog nigdy nie kasuje osób, do których są odwołania.
- [ ] Migracja przeniosła wszystkie wartości; wygląd stron bez zmian poza zgłoszonymi poprawkami.
- [ ] Kontrola zmian redaktorów przed i po pushu w raporcie; przegląd z następnego dnia zrobiony.
