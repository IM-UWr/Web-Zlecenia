# Agent 1 — raport (Web-Instytut, „Warto wiedzieć”: 9 sylwetek + wszystkie nagrody), 22.11.2026

## Podsumowanie

- Sprawdzone pliki: 15 (9 sylwetek, 6 nagród). Sprawdzone pola z wersją EN: 73 (`tresc_en`, `podpis_en`, `zajawka_en`, `tytul_en`, `obraz_opis_en`, `etykieta_en` ×27; `n_en` — same liczby, puste celowo).
- **Uzupełnione (brakowało EN): 42 pola**, w tym 13 pełnych `tresc_en` (9 sylwetek, 4 nagrody) — ok. 17,8 tys. słów angielskiego tekstu (bez komentarzy).
- **Poprawione (EN był, ale zły): 4 pola** (2 pliki nagród + 1 etykieta).
- **Zostawione bez zmian (dobre): 31 pól** (26 etykiet liczb banera, `tytul_en`/`obraz_opis_en` medalu UWr, `tytul_en`/`zajawka_en`/`obraz_opis_en` oceny PKA).
- Kontrola każdego pliku: YAML wczytuje się (PyYAML), `tresc_en` po wczytaniu = tekst zamierzony; te same `{#id}` i ta sama liczba linii `:::` co w polskiej Treści; te same adresy linków (porównanie list URL PL/EN); brak `# `; brak łącznika w blokach; ta sama liczba `**`. Dodatkowo obie Treści (PL i EN) wyrenderowane potokiem strony (remark-jawne-bloki + rehype-bloki z `/home/claude/en/build`): bez błędów, bez autokorekty nagłówków, ta sama liczba h2/li/p/a/strong. Całej strony nie budowałem.
- `sprawdz_tresci.py` na kopii roboczej: jedyne 3 „błędy” to `brak pliku obrazu public/pliki/aktualnosci/…` (kategoria-a-plus, medal-sierpinskiego, nagroda-ptm-steinhausa) — są tak samo na czystym klonie (obrazy leżą w Web-Aktualnosci). Po dołożeniu `public/pliki/aktualnosci` z Web-Aktualnosci: „OK — sprawdzono 55 plików”.
- Łatka: `/home/claude/en/wyniki/1/Web-Instytut.patch` — `git apply --check` na czystym klonie OK. Bez commitów.

## Tabela zmian

Ścieżki względem `src/content/warto_wiedziec/`.

| Plik | Pole | Co zrobiono |
|---|---|---|
| sylwetki/andrzej-hulanicki.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione (pełne tłumaczenie, 6 sekcji + źródła) |
| sylwetki/andrzej-krzywicki.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| sylwetki/bronislaw-knaster.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| sylwetki/bronislaw-knaster.md | `liczby[0].etykieta_en` | poprawione: „Chair of Topology” → „chair of topology” (zasada: podpis małą literą, jak PL „katedra topologii”) |
| sylwetki/czeslaw-ryll-nardzewski.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| sylwetki/edward-marczewski.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| sylwetki/hugo-steinhaus.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| sylwetki/jan-mycielski.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| sylwetki/julian-perkal.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| sylwetki/kazimierz-urbanik.md | `podpis_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| sylwetki/* (9 plików) | `etykieta_en` (26 pozostałych) | zostawione — poprawne, do 20 znaków |
| nagrody/kategoria-a-plus.md | `tytul_en`, `zajawka_en`, `obraz_opis_en`, `tresc_en` | uzupełnione |
| nagrody/medal-sierpinskiego.md | `tytul_en`, `zajawka_en`, `obraz_opis_en`, `tresc_en` | uzupełnione |
| nagrody/nagroda-ptm-steinhausa.md | `tytul_en`, `zajawka_en`, `obraz_opis_en`, `tresc_en` | uzupełnione |
| nagrody/stypendium-steinhausa.md | `tytul_en`, `zajawka_en`, `tresc_en` | uzupełnione |
| nagrody/medal-uniwersytetu.md | `zajawka_en` | poprawione: „Its recipients include Professors …” → wierne PL, forma D1 „Prof. X and Prof. Y” |
| nagrody/medal-uniwersytetu.md | `tresc_en` | poprawione: brak pierwszego akapitu i części zdania („w uznaniu osiągnięć…”), data amerykańska „November 13, 2026” (D19), brak opisów plików po „ — ”, brak komentarzy, nagłówek „Biographical notes” → „Recipients’ biographical notes” |
| nagrody/medal-uniwersytetu.md | `tytul_en`, `obraz_opis_en` | zostawione |
| nagrody/wyrozniajaca-ocena-pka.md | `tresc_en` | poprawione drobno: apostrof ’ („master’s”), dopisane komentarze `<!-- … -->` jak w PL; tekst bez zmian |
| nagrody/wyrozniajaca-ocena-pka.md | `tytul_en`, `zajawka_en`, `obraz_opis_en` | zostawione |

Przyjęte nazwy (z istniejących `_en` w repozytoriach): Institute of Mathematics of the Polish Academy of Sciences (IM PAN); Wacław Sierpiński Medal; Hugo Steinhaus Main Prize of the Polish Mathematical Society; Hugo Steinhaus Scholarship, Wrocław Academic Centre, Student Scholarship Programme; A+ research category; Andrzej Hulanicki Award; Wrocław Mathematicians Foundation; Stefan Banach / Stefan Mazurkiewicz / Stanisław Zaremba Prize of the Polish Mathematical Society; Minister of Science Award for lifetime scientific achievement; Prime Minister’s Award; State Prize (second/first class); Władysław Orlicz Lecture; Medical Academy in Wrocław; Wrocław Scientific Society; Polish Academy of Arts and Sciences; Wrocław Branch of the Polish Mathematical Society; Department of Functional Analysis / Differential Equations; Lwów, Lwów School of Mathematics, Scottish Book / New Scottish Book, Wrocław taxonomy, plac Grunwaldzki; Stefan Banach International Mathematical Center, Ryll-Nardzewski Center, Hugo Steinhaus Center (nazwy oficjalne, pisownia „Center”).

## Potrzebne zmiany w kodzie (dla agenta 3)

1. **Źródło zdjęcia sylwetki bez wersji EN.** Pole `obraz_zrodlo` (schemat: `src/content.config.ts:507`, widok: `src/views/SylwetkaWW.astro:33`, typ: `src/lib/wartoWiedziec.ts:41, 132`, CMS: Web-Instytut `.pages.yml:434`) nie ma `obraz_zrodlo_en`, więc na `/en` jest np. „Photo: Archiwum UWr”. Nowego pola nie wpisywałem. Propozycja: dodać `obraz_zrodlo_en` (puste = polskie) albo mapę tłumaczeń w kodzie. Proponowane tłumaczenia dla moich sylwetek: „Archiwum UWr” (Knaster, Marczewski) → „University of Wrocław Archives”; „archiwum prywatne / UWr” (Mycielski) → „private archive / UWr”; „Polskie Towarzystwo Biometryczne” (Perkal) → „Polish Biometric Society”; „Centrum Rylla-Nardzewskiego PWr” (Ryll-Nardzewski) → „Ryll-Nardzewski Center, Wrocław University of Science and Technology”; „IM UWr” (Krzywicki) → „Mathematical Institute, UWr”. Pozostałe (Wikimedia Commons, licencje CC, „Konrad Jacobs / MFO”, „Ryszard Świtacz”) są neutralne.
2. **`sprawdz_tresci.py` (linia 155–156)** zgłasza jako błąd brak obrazu `/pliki/aktualnosci/…` w Web-Instytut, choć plik jest w Web-Aktualnosci (3 nagrody; to samo na czystym klonie). Propozycja: dla ścieżek spoza repozytorium (np. `/pliki/aktualnosci/`) ostrzeżenie zamiast błędu albo szukanie w sąsiednich repozytoriach.

Brakujących pól w schemacie ani w `.pages.yml` dla pozostałych pól nie znalazłem (`podpis_en`, `zajawka_en`, `tytul_en`, `obraz_opis_en`, `etykieta_en`, `tresc_en` są w obu).

## Do decyzji właściciela

1. **IM PAN** (po poprawce koordynatora): wszędzie „Institute of Mathematics of the Polish Academy of Sciences” (w sylwetce Hulanickiego przy pierwszej wzmiance z „(IM PAN)”, dalej „IM PAN”, jak w PL; w Źródłach Urbanika etykieta „IMPAN:”). „Mathematical Institute” zostało tylko dla IM UWr. Pokrewne: Państwowy Instytut Matematyczny (poprzednik IM PAN) → „State Institute of Mathematics” (MacTutor pisze „State Mathematical Institute”); Instytut Matematyczny UW (lata 30.) → opisowo „the mathematical institute of the University of Warsaw”; „Steklov Mathematical Institute” zostawione — to oficjalna nazwa instytutu w Moskwie.
2. **Politechnika Wrocławska** → „Wrocław University of Science and Technology” (dalej „the University of Science and Technology”), także w kontekstach historycznych (1945–1951). Strona „Sukcesy — historia” ma jeszcze „Wrocław University of Technology”. Jej „Instytut Matematyki” → „Institute of Mathematics” (dla odróżnienia od naszego Mathematical Institute).
3. **Stanowiska historyczne** (bez amerykańskich nazw): asystent → assistant, starszy asystent → senior assistant, zastępca asystenta → deputy assistant, adiunkt → research fellow (IM PAN) / lecturer (uczelnia), docent → docent, profesor nadzwyczajny → extraordinary professor, profesor zwyczajny → full professor, aspirantura → doctoral studies, doktor nauk matematycznych (1957) → „Doctor of Mathematical Sciences, at that time the equivalent of the habilitation”.
4. **Tytuły polskich książek, rozpraw i wykładów w tekście:** oryginał kursywą + dosłowne tłumaczenie w nawiasie (jak D4), np. *Czem jest, a czem nie jest matematyka* (What mathematics is and what it is not), *O dendroidach* (On dendroids), *Procesy kaskadowe* (Cascade processes). Czasopisma i książki kursywą (w PL są w „…”). W „Sources” tytuły źródeł w oryginale z angielskimi cudzysłowami “…”, czasopisma kursywą; opisy (nie tytuły) przetłumaczone, np. „Nota pośmiertna redakcji…” → „Obituary note by the editors of…”. Źródeł po polsku nie oznaczałem „(in Polish)” — tytuł w oryginale to pokazuje; jeśli D20 ma obejmować także źródła, to dopisek w kilkudziesięciu pozycjach.
5. **Imiona i transliteracje:** zostawiłem polskie formy imion (Otton Nikodym, Marek Kac — w literaturze angielskiej „Otto Nikodym”, „Mark Kac”); nazwiska rosyjskie w tekście w transliteracji angielskiej (Ladyzhenskaya, Kashin, Steklov), w opisach bibliograficznych źródeł bez zmian (np. „O. A. Ładyżenska”). Wilno → „Wilno (now Vilnius)”.
6. „Wikipedia (ang.)” → „Wikipedia” (bez dopisku), „(niem.)” → „(German)”; „Wikipedia (en)/(pl)” w sylwetce Urbanika zostawione jak w PL.
7. Adresy w tekście bez zmian: „ul. Orłowskiego 15”, „ul. Kopernika 18”, „ul. Bujwida”, „plac Grunwaldzki”.
8. Etykiety banera z polskim skrótem: „PTM president” (Marczewski) — skrót PTM bez rozwinięcia (limit 20 znaków); można „PMS president”, ale reszta strony używa „PTM”. „Biometric Society” (Perkal) to skrót od Polish Biometric Society.
9. Nagroda Steinhausa w aktualnościach (zakres agenta 4) ma „Student Scholarship Program … organized … honorable mention” (pisownia amerykańska) — u mnie „Programme”.

## Błędy i niejasności w polskim tekście (niepoprawione)

1. **Odmiana „Ryll-Nardzewski”:** edward-marczewski.md — „[Czesława Ryll-Nardzewskiego]” (powinno: Czesława Rylla-Nardzewskiego); jan-mycielski.md — „[Czesławem Ryll-Nardzewskim]” (powinno: Czesławem Ryllem-Nardzewskim). Sylwetka Ryll-Nardzewskiego odmienia poprawnie („Rylla-Nardzewskiego”).
2. **andrzej-krzywicki.md, zajawka:** „Uczeń Witolda Wolibnera, od którego – według monografii… – zaczęła się we Wrocławiu teoria równań różniczkowych” — gramatycznie „od którego” wskazuje Wolibnera, a z Treści wynika, że chodzi o Krzywickiego. W EN przetłumaczone zgodnie z Treścią (Krzywicki).
3. **kazimierz-urbanik.md:** link przy „sesja naukowa „Kazimierz Urbanik (1930–2005)”” prowadzi do PDF wspomnienia (KU.pdf), a nie do strony sesji (ta jest w Źródłach: math.uni.wroc.pl/sesja_Urbanik). EN zachowuje ten sam link.
4. **andrzej-krzywicki.md, Źródła:** „Spis pracowników na Podglądzie nowej strony Instytutu” — po starcie strony nieaktualne („Podgląd”).
5. Drobne niespójności stylu Źródeł: jan-mycielski.md używa „ – ” jako separatora (pozostałe „ — ”), andrzej-krzywicki.md i jan-mycielski.md bez kropek na końcu pozycji (EN odwzorowuje PL).
6. Hulanicki (PL): cytowanie „„Master”” i Bożejko „Nota biograficzna prof. Marka Bożejki” bez linku — tylko informacja (nie błąd).

## Wpisy testowe

W moim zakresie brak.
