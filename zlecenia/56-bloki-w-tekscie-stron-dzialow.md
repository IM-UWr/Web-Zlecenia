# Zlecenie 56 (20.11.2026): bloki `:::` w tekście stron działów (Popularyzacja, Instytut, Studia, Nauka)

**Skąd to zlecenie.** Piotr (pborod) redaguje Popularyzację. 19–20.11 wstawił do „Strony działu Popularyzacja” blok `:::linki` („Program Spotkań”) i blok `:::kafelki` (4 obozy). Plik: Web-Popularyzacja, `src/data/popularyzacja.md`, commit `ee5a24f`.
- Markdown jest poprawny. To ten sam blok co w sekcji „Obozy” na `/popularyzacja/uczniowie`, gdzie kafelki wyglądają dobrze.
- Jest też zgodny z opisem pola „Treść” w CMS: „Specjalne układy otwieraj znacznikiem, np. :::kafelki”.
- Na `/popularyzacja` kafelki wychodzą jako goły tekst. Tytuł jest sklejony z opisem, „Kiedy / zima” wygląda jak wcięta lista, a link nie ma wyglądu linku z kafelka.

**Decyzja właściciela (20.11, 21:53):** „czy możemy wdrożyć fix, żeby kafelki zaczęły działać?”. Chodzi o wersję ostrożną, omówioną o 21:51. Zmienia się tylko wygląd bloków. To, co dziś jest w tekstach działów, wygląda tak samo jak przed poprawką.

## Diagnoza (20.11)
Lokalny build: Web-Core `608d6337`, treści z `main` wszystkich repozytoriów.
- **Parser działa.** `danePopularyzacji()` (`src/lib/widoki/popularyzacja.ts`) i `stronaDzialu()` (`src/lib/tekstyStron.ts`; Instytut, Studia, Nauka) renderują tekst z włączonymi blokami. HTML jest poprawny: `ul.linki`, `ul.dwa`, `dl.para`, `p.akcja`.
- **Brakuje stylów.** `src/components/zal/TrescDzialu.astro` wstawia ten HTML do `section.z-dz-tresc > div`, bez klasy `.tresc`.
  - Wszystkie style bloków w `src/styles/zal-tresc.css` działają tylko wewnątrz `.tresc`.
  - Wygląd bloków z Markdownu na podstronach daje `.tresc .prose`. Przykład: na `/popularyzacja/uczniowie` struktura to `div.z-pd-tresc.tresc > div.prose`.
  - `zal-dzialy.css` stylizuje w `.z-dz-tresc` tylko `h2` i `p`.
- **Zakładki.** `src/scripts/tresc-zakladki.ts` ładują tylko `Podstrona.astro`, `Kierunek.astro` i `Specjalnosc.astro`. Na stronie działu `:::zakladki` by się nie przełączały (selektor `.tresc .tresc-taby[role="tablist"]`).
- **Zasięg (skan całego `dist`):** bloki poza `.tresc` są dziś tylko na `/popularyzacja` (PL). Teksty Studiów, Instytutu i Nauki to same akapity.
- **Ostatnie sukcesy:** strona wycina `## Ostatnie sukcesy {#sukcesy}` z tekstu Instytutu, zanim tekst trafi do `TrescDzialu`. Sekcja `z-dz-sukcesy` leży poza `.z-dz-tresc`, więc ta poprawka jej nie dotyczy.
- **Opisy w CMS:** opisy pola „Treść” stron działów (Web-Popularyzacja, Web-Studia, Web-Instytut, Web-Nauka) zapowiadają bloki (`:::kafelki`, `:::etapy`, `:::zakladki`). Opisy zostają bez zmian, poprawiamy stronę.

## Zasady pracy
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- **Tylko Web-Core:** `TrescDzialu.astro` i style działów (`zal-dzialy.css`, ewentualnie `zal-tresc.css`).
- **Repozytoriów treści nie zmieniasz.** Plik Piotra zostaje bez zmian.
- **Treści testowe** wpisujesz tylko do lokalnej nakładki `src/data/*.md`, którą git pomija. Na koniec `python3 skrypty/pobierz_tresci.py` przywraca nakładkę z `main`.
- Raport `RAPORT-ZLECENIE-56.md`, zrzuty `raport-zrzuty/z56-*`. Bez subagentów.
- **Kolejność:** jeśli inne otwarte zlecenie zmienia `TrescDzialu.astro` albo `zal-dzialy.css`, to zlecenie robisz po nim.

## Docelowo
1. **Bloki jak na podstronach.** Dotyczy to bloków z `BLOKI` w `src/plugins/remark-jawne-bloki.mjs`, które wolno stawiać na zwykłej stronie: `kafelki`, `etapy`, `kontakty`, `linki`, `pliki`, `pytania`, `ramka`, `zakladki`, `tabela`, `kreski`, `tematy`, `pary`.
   - W tekście każdej z czterech stron działów taki blok wygląda i działa jak w treści podstrony (wzorzec: `/popularyzacja/uczniowie`).
   - Obowiązuje to w PL i EN, na komputerze i telefonie, w trybie jasnym i ciemnym.
   - Zakładki się przełączają, bo skrypt jest ładowany na stronach działów.
   - Na telefonie kafelki i linki stoją w jednej kolumnie, jak na podstronach.
2. **To, co dziś jest w tekstach działów, zostaje bez zmian:**
   - akapity: stopień, interlinia, kolor, szerokość i odstępy (na telefonie 15,5 px / 1,62);
   - pierwszy akapit `p.wst` i linki w akapitach;
   - nagłówek „O …” i „W skrócie”;
   - pas grup i sekcje pod tekstem (Dla kogo, Ostatnie sukcesy, kontakt…).
3. **Elementy, których w tych tekstach dziś nie ma,** wyglądają jak w treści podstrony. Chodzi o zwykłe listy, tabele, `###`, cytaty `>` i każde `##` inne niż `{#sukcesy}`.

**Wskazówka (nie przepis):**
- Opakuj sam HTML z Markdownu tak jak na podstronach, np. `<div class="tresc …"><div class="prose">…</div></div>` pod nagłówkiem „O …”.
- W `zal-dzialy.css` przywróć dotychczasowe wartości akapitów i linków w akapitach.
- Uważaj na moc selektorów: `body .tresc .prose p` (0,2,2) wygrywa z `.z-dz .z-dz-tresc p` (0,2,1), a `.tresc` ustawia na telefonie 16 px / 1,65.
- Przeczytaj `src/plugins/postcss-tresc-telefon.mjs`. Dotyczy tylko `.z-pd`, ale sprawdź, czy nic nie zmienia na stronach działów.
- Sprawdź klasę `wst`. Strona nadaje ją przez `.replace(/<p>/, '<p class="wst">')` w `popularyzacja.ts` i odpowiednikach. Gdy tekst zaczyna się od bloku, klasa może trafić do akapitu wewnątrz bloku. Jeśli tak jest, popraw to tak, żeby `wst` dostawał tylko akapit stojący bezpośrednio w tekście.

## Odbiór lokalny
- **Porównanie HTML przed i po**, PL i EN, dla `/instytut`, `/studia`, `/nauka` i `/popularyzacja` z treściami z `main`.
  - Jedyne różnice to opakowanie tekstu i ewentualnie skrypt zakładek. Każda inna różnica to błąd.
  - Pozostałe strony w `dist` bez zmian, poza nazwami plików CSS/JS i indeksem wyszukiwarki.
- **Zrzuty pikselowe** `/instytut`, `/studia` i `/nauka`, przed i po: 1920×1080, 1440×900, 1024 i 390 px, w trybie jasnym i ciemnym. Mają wyjść identyczne. Liczbę różniących się pikseli wpisz do raportu.
- **Popularyzacja:**
  - zrzuty sekcji „O popularyzacji” przed i po: 1920, 1440 i 390 px, jasny i ciemny; obok zrzut „Obozy” z `/popularyzacja/uczniowie`;
  - obliczone style (`getComputedStyle`) tytułu, opisu, `dl.para` i linku w kafelku mają być równe tym z `/popularyzacja/uczniowie`;
  - akapity i link „Kalejdoskopu matematycznego” wyglądają jak przed poprawką.
- **Wszystkie bloki:**
  - w lokalnej nakładce dopisz do `src/data/studia.md` próbkę każdego bloku z punktu 1, w polskiej treści i w `tresc_en`; przykłady weź z `dok/sciagawka-edytora.md`;
  - zrób zrzuty na komputerze i telefonie;
  - sprawdź zakładki myszą i klawiaturą oraz rozwijanie pytań;
  - potem przywróć nakładkę (`pobierz_tresci.py`) i sprawdź, że `git status` w Web-Core nie pokazuje treści.
- **Kontrole:**
  - `astro check` bez nowych błędów;
  - testy wtyczek zielone (`src/plugins/*.test.mjs`);
  - `sprawdz_tresci.py` OK;
  - konsola czysta.
- **Stop:** raport i czekanie na „push”. Push dotyczy tylko Web-Core.

## Kryteria odbioru
- [ ] Na `/popularyzacja` kafelki i lista linków od Piotra wyglądają jak na `/popularyzacja/uczniowie`: na komputerze i telefonie, w trybie jasnym i ciemnym.
- [ ] Każdy blok z punktu 1 działa w tekście stron działów, a zakładki się przełączają.
- [ ] Na `/instytut`, `/studia` i `/nauka` zrzuty przed i po są identyczne, a HTML różni się tylko opakowaniem.
- [ ] Na wszystkich czterech stronach bez zmian zostały akapity, `p.wst`, linki w akapitach, „O …”, „W skrócie” i sekcje pod tekstem.
- [ ] Repozytoria treści są bez zmian. W Web-Core zmieniły się tylko pliki kodu.

## Do raportu
- Opis rozwiązania i lista zmienionych plików.
- Wyniki porównań: HTML, piksele i obliczone style.
- **Uwagi dla właściciela** (bez zmian w treściach):
  - w pliku Piotra na górze Treści i Treści EN jest komentarz z migracji `<!-- Zwykłe akapity Markdown. … -->`. Jest sprzeczny z opisem pola, więc właściciel zdecyduje, czy redaktor może go usunąć;
  - we wstępie Piotra pojedyncze Entery sklejają trzy zdania w jeden akapit, a cudzysłów ma postać "…" zamiast „…”.
