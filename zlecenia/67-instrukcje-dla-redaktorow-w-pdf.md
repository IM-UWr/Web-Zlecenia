# Zlecenie 67 (22–23.11.2026): instrukcje dla redaktorów w PDF pod stałymi linkami — WYKONANE

> Zapis po fakcie (changelog). Claude Code, 22.11.2026 ok. 23:50 – 23.11.2026 ok. 0:10.

**Decyzje właściciela:**
- „Czy możesz oba pliki zrobić w pdf i wrzucić je na linki takie, że osoba, która kliknie na link, od razu widzi pdf, a nie githuba”;
- „I za każdym razem, gdy będę cię prosił o aktualizację mapy i readme, będziesz edytował dokładnie te pliki”;
- „Z innych miejsc je wszędzie pousuwaj”.

## Stałe adresy
- Mapa CMS: https://im-uwr.github.io/Web-Podglad/dla-redaktorow/Mapa-CMS-IM-UWr.pdf
- Ściągawka edytora: https://im-uwr.github.io/Web-Podglad/dla-redaktorow/Sciagawka-edytora-IM-UWr.pdf

Serwer zwraca `Content-Type: application/pdf` bez `Content-Disposition`, więc przeglądarka od razu otwiera plik.

## Co zrobiono
- Web-Core 1a791362:
  - PDF-y leżą w `public/dla-redaktorow/`, więc Podgląd buduje je razem ze stroną. Po starcie nowej strony będą pod tą samą ścieżką na jej adresie.
  - `skrypty/pdf-dla-redaktorow.mjs` robi oba pliki (domyślnie do `public/dla-redaktorow/`):
    - mapę z `dok/dla-redaktorow/mapa-cms.html`, dokładnie 2 strony;
    - ściągawkę z `dok/sciagawka-edytora.md` (Markdown z GFM, kolory jak w mapie, nagłówek z datą, numery stron; teraz 8 stron).
  - README, sekcja „Dla redaktorów”: linki do obu PDF-ów.
- Kopie usunięte:
  - Web-Podglad 321a0a0: `dla-redaktorow/Mapa-CMS-IM-UWr.pdf` usunięty, README ma stałe linki;
  - Web-Core: stara mapa `dok/mapa-redakcyjna-IM-UWr.pdf` z 9.11 (git rm);
  - lokalna kopia `Web-Core/Claude outputs/Mapa-CMS-IM-UWr.pdf` z 7.11, poza gitem: do Kosza.

  `Czat-AI-formatowanie-tresci.pdf` to inny dokument i został na miejscu. Kopie mapy w starych klonach Web-Podglad (`podglad-z33`, `tresci-B`, `tresci-C`) i w `Web-Core-B` znikną przy porządkach w folderze Github (osobny przegląd, czeka na decyzję właściciela).

## Zasada na przyszłość
„Aktualizacja mapy” albo „aktualizacja readme/ściągawki” oznacza:
1. edycję źródła (`mapa-cms.html` albo `sciagawka-edytora.md`);
2. `node skrypty/pdf-dla-redaktorow.mjs`;
3. commit tych samych dwóch plików w `public/dla-redaktorow/`.

Nazwy i adresy plików się nie zmieniają, a kopii nie ma nigdzie indziej.

## Sprawdzenie
- PDF-y: mapa 2 strony (bez wychodzenia treści poza stronę), ściągawka 8 stron (podgląd stron 1 i 8: nagłówek, tabele, stopka z numerem).
- Pliki w repozytorium są bajt w bajt takie jak wygenerowane (sha1). Git dla Windows pokazuje różnice w PDF-ach jako tekst (atrybut `diff=astextplain`), ale ich nie zmienia.
- Podgląd 45080966245 success. Oba adresy: 200, `application/pdf`, rozmiary zgodne (191530 i 278304 bajtów).
