# Raport: zlecenie 40, etap 1 — Web-Instytut (18.11.2026)

## Stan
> **Aktualizacja 18.11, 17:20:** Web-Instytut wypchnięte 18.11 o 16:52 (przed wieczorem, na Twoje polecenie) — wynik w „Push treści”.

- **Web-Core: wypchnięte** `a0e32c28..0cda774c` (po rebase na zlecenie 36 z drugiego okna). **Podgląd zielony**: run 44309660047 zbudował stronę z `0cda774c`.
- **Web-Instytut: commit gotowy, push wieczorem** (okno pusha z sekcji „Ochrona zmian redaktorów”), zaplanowany na **20:41, po pushu treści zlecenia 33 (20:07)**. Skrypt: `push40_instytut.sh` w scratchpadzie. Wynik dopiszę w sekcji „Push treści”.
  - Klon roboczy: `tresci-z40/Web-Instytut`, gałąź lokalna `praca/40-instytut`, commit `88d8f50` na commicie zlecenia 33 (`b2de465`, jeszcze niewypchniętym).
  - **Baza** (świeży `main` na początku pracy): `311faae`. O 14:05 brak zapisów redaktorów od bazy.

## Co zrobiłem

### Web-Core (jeden commit `0cda774c`)
1. **`maTresc()`** (decyzja 18.11: „najpierw maTresc, potem szablony”): Treść z samym komentarzem `<!-- … -->` liczy się jak pusta. Zastąpiłem nią wszystkie miejsca z raportu 40-0, sekcja 4:
   - granty (własna strona), obrony (automatyczne zaproszenie), referaty i opisy seminariów (ramka streszczenia);
   - „Warto wiedzieć” (podstrona, link, mapa strony), drugi ekran okładki, szkice, Nauka;
   - powiadomienia o seminariach: streszczenie bez komentarzy (`bezKomentarzy()`).
2. **Jawny tryb strony działu i stron z listą:** sekcja przenoszona w inne miejsce strony działa po jawnym id, np. `## Ostatnie sukcesy {#sukcesy}` na `/instytut`, a nie po nazwie nagłówka (`src/lib/tekstyStron.ts`). Ta sama reguła obsłuży `{#czasopisma}` w Nauce (etap 2).
3. **Limity linii w jawnych Stronach** (`src/lib/widoki/strona.ts`): krótkie komórki tabel dostają `data-limit-linii` dla tekstu polskiego, jak w dawnym formacie. Bez tego 2 strony infrastruktury informatycznej traciły znacznik w tabelach, czyli zmieniłby się pomiar układu w `Podstrona.astro`. Strony Studiów zostają bez limitów, tak jak od początku jawnego formatu (zob. pytanie 1).
4. **Skrypty:**
   - `skrypty/jawny-markdown-repo.mjs` (nowy): migracja Stron i strony działu dowolnego repozytorium. Dopisuje `{#id}` z dzisiejszym id, liczonym tym samym silnikiem co budowa; dodaje komentarz `UKŁAD JAWNY` i `format_tresci: jawne`. Sam sprawdza, że tekst i pozostałe pola się nie zmieniają; inaczej przerywa.
   - `skrypty/migracja/formularze_40.mjs` (nowy): opis formularzy per repozytorium (kolejność, opisy, ukryte pola, szablony). Uruchomiony drugi raz nic nie zmienia.
   - `skrypty/sprawdz-jawny-markdown.mjs`: uogólniony na każde repozytorium (Studia bez zmian w sprawdzeniach).
   - `skrypty/migracja/kontrola_redaktorow.py`: `--jawne` (Treść porównywana jako tekst po migracji: bez komentarzy i `{#id}`) i kilka `--dopisane`.
5. `dok/jawny-markdown.md`: sekcja „Pozostałe działy (zlecenie 40)”. Pełna aktualizacja dokumentów i PDF-ów na koniec zlecenia.

### Web-Instytut (jeden commit `88d8f50`: `.pages.yml` i dane)
- **12 Stron i `src/data/instytut.md` → jawny Markdown.**
  - `{#id}` przy wszystkich 64 nagłówkach `##` (PL i EN); adresy sekcji bez zmian, np. `{#sieć-eduroam}`, `{#mathematical-institute}`.
  - Komentarz `<!-- UKŁAD JAWNY: … -->` na początku Treści i Treści EN, jak w Studiach.
  - `## Ostatnie sukcesy {#sukcesy}` / `## Recent achievements {#sukcesy}` z komentarzem `<!-- SUKCESY: … -->`.
  - Tekst bez zmian. Bloków `:::` nie było potrzeba: Strony Instytutu nie miały włączonych „Bloków wzorca”.
- **Formularze** (zatwierdzony projekt z raportu 40-0):

| Formularz | Kolejność | Inne zmiany |
|---|---|---|
| Strona działu | tytuł, tytuł EN, Opublikowane → Treść, Treść EN → wstęp, hasło, „W skrócie”, godziny | ściągawka jawnego Markdownu przy Treści i Treści EN (z regułą `{#sukcesy}`); ukryte `format_tresci` (domyślnie `jawne`); opis pola hasła |
| Zakłady | nazwa, nazwa EN, Opublikowane → Treść, Treść EN → karta (pola EN pod polskimi) → kolejność | opis formularza „co to i gdzie widać”; ściągawka zwykłego Markdownu; **szablon Treści** `<!-- TEKST: Czym zajmuje się zakład. Skład i seminaria strona dopisze sama. -->`; opis pola „Kolejność” |
| Strony | tytuł, tytuł EN, Opublikowane → Treść, Treść EN → opis, hasło, liczby, prawy pasek | ściągawka jawnego Markdownu; ukryte `format_tresci` i dawne „Bloki wzorca”; opis pola „Krótki opis” |
| „Warto wiedzieć” | tytuł, tytuł EN, Opublikowane → Treść, Treść EN → karta → reszta | opis formularza; ściągawka; **szablon Treści** `<!-- TEKST: Pusta Treść = sama zajawka bez własnej strony. -->` |
| Władze | bez zmian | ukryte `do_uzupelnienia`, `haslo`, `haslo_en` (decyzje 18.11; wartości zostają w pliku); opisy pól „Imię i nazwisko”, „Zdjęcie” |

## Kontrole
- **Porównanie HTML całej strony** (889 plików: HTML, ICS, XML, JSON; ścisłe, bez hashy plików `_astro` i znaczników czasu), po rebase na `a0e32c28`:
  - kod `origin/main` → nowy kod, te same dane: **0 różnic**;
  - nowy kod: dane Web-Instytut przed migracją → po migracji: **0 różnic** (PL i EN).
  - Pierwsza próba pokazała 2 strony z różnicą (`data-limit-linii` w tabelach, punkt 3 wyżej). Po poprawce 0. Zrzutów nie robiłem, bo nie było różnic.
- **Szablony Treści** (osobna budowa z testowymi wpisami: pusta Treść i Treść z samym komentarzem):
  - „Warto wiedzieć”: ani pusta Treść, ani sam komentarz nie dają podstrony ani wpisu w mapie strony; karta prowadzi do linku. Zachowanie identyczne.
  - Zakład: strony identyczne poza niewidocznym komentarzem w źródle HTML (`.zk-opis`). Na stronie bez zmian.
  - Istniejące wpisy: wszystkie 9 zakładów i 4 pozycje „Warto wiedzieć” mają Treść, więc CMS nie wstawi im szablonu przy otwarciu.
- `sprawdz_pola_cms.py`: **0 problemów** (724 pliki, 16 repozytoriów, Web-Instytut z klonu roboczego).
- `sprawdz-jawny-markdown.mjs`: **OK** dla Web-Instytut (13 plików, 64 nagłówki `##`, wszystkie z `{#id}`). Dla porównania Web-Studia i Web-Popularyzacja też OK.
- `astro check`: **0 błędów, 0 ostrzeżeń** (8 podpowiedzi, jak wcześniej). `npm run test:jawne`: **47/47**.
- `kontrola_redaktorow.py`:
  - `po` na commicie (b2de465 → 88d8f50): zmienione tylko `body` (13), `tresc_en` (12), `format_tresci` (13) i `.pages.yml`. Wynik „OK, tylko zmiany z migracji”.
  - Bez `--jawne` ta sama kontrola zgłasza wszystkie 13 plików (kontrola działa).
  - `przed`: 0 zapisów od bazy.

## Przyjąłem sam (zlecenie przewiduje domyślne albo moją rekomendację)
- **Ukryłem dawne „Bloki wzorca” w Stronach Instytutu** (`hidden: true`). W jawnym formacie strona ich nie czyta; układ wskazują bloki `:::`. Wartości zostają w plikach. Zlecenie każe ukrywać pola techniczne; usunięcie zostawiam Tobie.
- **Etykieta „Wstęp pod tytułem” na stronie działu → „Opis strony dla Google”**, bo nowy nagłówek tego pola nie pokazuje (trafia tylko do opisu dla wyszukiwarek, `NaglowekStrony.astro`). Podobnie „Krótki opis (pod tytułem i w Google)” w Stronach → „Krótki opis (Google i podgląd linku)”.
- **„Opublikowane” pod parą tytuł / tytuł EN**, jak w zleceniu 33 i w Studiach. Treść zaraz pod nim.
- **Komentarze w Treści EN po polsku**, jak w Studiach (są dla redaktorów).
- **Kontrola przed pushem treści 40.1: baza = commit zlecenia 33 na `main`.** Zapisy redaktorów sprzed niego sprawdza kontrola zlecenia 33; jeśli 33 się nie wypchnie, skrypt 40.1 zatrzymuje się (STOP).
- **Skrypt formularzy w Web-Core** (`skrypty/migracja/`), z opisem per repozytorium. Kolejne etapy dopiszą swoje opisy w tym samym pliku.

## Pytania do Ciebie
1. **Strony Studiów bez limitów linii.** Od migracji Studiów do jawnego formatu krótkie komórki tabel na ich Stronach nie mają `data-limit-linii` (dawny format je miał). Przywrócić? To zmiana wyglądu Studiów (pomiar układu), więc w tym zleceniu jej nie robię.
2. **„Źródła (nie wyświetlają się)”** w „Warto wiedzieć” i we Władzach to też notatki dla redakcji, jak „Do uzupełnienia”. Ukryć je tak samo?

## Push treści (wieczorem)
Poprawki skryptu `push40_instytut.sh` przed uruchomieniem (znalezione przy etapach 2 i 4):
- warunek „zlecenie 33 jest już na main” zawsze kończył się STOP: Git Bash zamieniał `origin/main:.pages.yml` na ścieżkę Windows; teraz `MSYS_NO_PATHCONV=1` w tym jednym poleceniu, sprawdzone na commicie 33;
- warunek porównania HTML liczył pustą listę `[]` jako różnicę; poprawiony i sprawdzony na pustej i niepustej liście.

**Wynik (18.11, 16:50–16:53, przed wieczorem na polecenie właściciela: „Dobra, zgadzam sie wrażamy teraz”):**
- baza = commit zlecenia 33 na `main` (`b2de465`, wypchnięty o 16:49); `origin/main` = baza, więc commit `88d8f50` poszedł bez ponownej migracji;
- `sprawdz-jawny-markdown`: OK (13 wpisów, 64 nagłówki `##`, wszystkie z `{#id}`); `sprawdz_pola_cms.py`: 0 problemów;
- kontrola redaktorów przed: 0 zapisów od bazy; porównanie HTML całej strony: **0 różnic** w 925 plikach;
- **wypchnięte `b2de465..88d8f50`**; kontrola po pushu: OK;
- Podgląd: **zielony** — przebieg 44341742516 zbudował stronę z `88d8f50` (wcześniejszy przebieg anulowała kolejka Podglądu, zostaje najnowszy).

## Następnego dnia (19.11)
- Test w CMS z Tobą:
  - otwarcie formularza Strony i strony działu;
  - zapis bez zmian (diff pusty albo kosmetyka kolejności pól);
  - zapis z drobną zmianą;
  - nowy zakład i nowa pozycja „Warto wiedzieć” z szablonem.
- Przegląd zapisów redaktorów z 24 h po pushu: czy żaden nie usunął `format_tresci` ani nie przywrócił starej postaci.
