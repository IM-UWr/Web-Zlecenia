# Zlecenie 62 (22.11.2026): pliki obron w folderach ImieNazwisko — WYKONANE

> Zapis po fakcie (changelog). Claude Code, 22.11.2026, ok. 22:30–23:00.

**Decyzje właściciela:**
- „w obronach, żeby dla redaktorów było intuicyjne, stwórz dla dwóch ostatnich obron 2 foldery nazwane ImieNazwisko i umieść w nim pliki”;
- „czy możemy zrobić, że dodanie nowej obrony (i usunięcie odpowiednio) stworzy folder ImieNazwisko i właduje tam pliki, które doda edytor przez formularz?”

**Ograniczenie Pages CMS** (dokumentacja: pola file/image): `path` to stały „Default browsing folder”, bez wartości z innych pól. Usunięcie wpisu nie usuwa jego plików. Dlatego potrzebny jest automat.

## Co zrobiono (Web-Aktualnosci)
- Obrony Macieja Tadeja (20.10) i Malwiny Mrowińskiej (27.10): po 7 PDF-ów skopiowanych z IM-UWr/Obrony-Archiwum do `Media → obrony → MaciejTadej` i `→ MalwinaMrowinska`. Wpisy wskazują te pliki. Pozostałe 50 obron nadal linkuje do Obrony-Archiwum.
- Automat `.github/workflows/obrony-pliki.yml` + `.github/skrypty/obrony_foldery.py` (testy: `test_obrony_foldery.py`, 4/4). Uruchamia się po każdej zmianie obron na main:
  - pliki z formularza obrony (Pages CMS wgrywa je do `obrony/`) przenosi do `obrony/<ImieNazwisko>/`, np. „Malwina Mrowińska” → `MalwinaMrowinska`, bez polskich znaków i spacji, z łącznikami; poprawia też adresy we wpisie;
  - po zmianie imienia lub nazwiska przenosi pliki do nowego folderu;
  - po usunięciu obrony usuwa jej folder (pliki zostają w historii repozytorium);
  - plik użyty przez dwie obrony kopiuje;
  - przy zajętej nazwie dopisuje `-1`;
  - adresy spoza Media zostawia;
  - po zapisie wysyła sygnał przebudowy do Web-Core (jak `powiadom.yml`).
- Instrukcje: README i mapa CMS („Obrony: pliki dodawaj w formularzu obrony, same trafią do obrony → ImieNazwisko”).

## Commity
Web-Aktualnosci: 3 commity, ostatni 0728d9d. Pierwszy przebieg automatu po pushu (45074764838) zakończył się sukcesem i nie zmienił plików, zgodnie z oczekiwaniem.

## Do sprawdzenia przy pierwszej prawdziwej obronie
Zapis automatu na main wymaga `permissions: contents: write`. Domyślne uprawnienia przepływów w repozytorium to „read”, a `permissions` w pliku je podnosi. Jeśli organizacja to zablokuje, przebieg pokaże błąd w Actions, a pliki zostaną w `obrony/`.
