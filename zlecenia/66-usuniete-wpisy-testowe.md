# Zlecenie 66 (22.11.2026): usunięte wpisy testowe — WYKONANE

> Zapis po fakcie (changelog). Claude Code, 22.11.2026, ok. 23:30–23:40.

**Decyzja właściciela:** „wywal wszystkie wpisy testowe. Umiesz je rozpoznać?”

## Jak rozpoznane
- Pierwotna lista: `dok/start-strony.md`, punkt 2 (8 wpisów i 4 zdjęcia z 6.11).
- Skan wszystkich 17 repozytoriów z `tresci.json` (stan main):
  - nazwy plików z „test”;
  - teksty „TEST:”, „Prelegent testowy”, „Dane testowe”, „Mister Test”, „Testowe:”, „testing the website”, „lorem”, „placeholder” i podobne.
- Fałszywe trafienia zostały, bo to prawdziwe treści:
  - 81 plików `test-*.pdf` w Web-Studia (zadania egzaminacyjne);
  - czasopismo „TEST” w publikacjach 2015;
  - „testowanie hipotez” w opisach specjalności;
  - liczby rzymskie XXX.
- Przed usunięciem sprawdzone, że nic nie odwołuje się do usuwanych plików i że repozytoria mają tylko gałąź main.

## Co usunięto (po pełnych ścieżkach)
- 8 referatów testowych: tytuł „TEST: …”, prelegent „Prelegent testowy”, sala „TEST”, terminy 9–13.11.2026:
  - Analiza harmoniczna 3dc3a28;
  - Dydaktyka c928a13;
  - Dyskretna analiza harmoniczna ad2662e;
  - Geometria be54b69;
  - Prawdopodobieństwo b74daf4;
  - Statystyka 51150a0;
  - Teoria modeli 1137bd9;
  - Topologia 008e9a4.
- Web-Aktualnosci c0c03bc: 4 zdjęcia `public/pliki/aktualnosci/test-*.jpg`. Same aktualności testowe zniknęły wcześniej, a zdjęcia zostały bez odwołań.
- Pliki zostają w historii repozytoriów.
- `dok/start-strony.md`, punkt 2: odnotowane jako zrobione.

## Sprawdzenie
- Podgląd: przebieg 45078423921, success, ze wszystkimi 9 nowymi commitami.
- Na stronach `/seminaria/statystyka`, `/seminaria/dydaktyka`, `/seminaria/topologia`, `/seminaria`, `/kalendarz` i na stronie głównej: 0 trafień „Prelegent testowy”, „TEST: ” i „sala TEST”.
