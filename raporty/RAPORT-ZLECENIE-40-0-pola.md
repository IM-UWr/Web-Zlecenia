# Zlecenie 40, etap 0 — wszystkie pola formularzy (załącznik do RAPORT-ZLECENIE-40-0.md)

Stan: `origin/main` repozytoriów treści z 18.11.2026, ok. 12:30 (przed pushem treści ze zlecenia 33, więc bez pola `opublikowany` tam, gdzie dopiero dojdzie).

Kolumny:
- **z treścią** = w ilu plikach pole ma niepustą wartość / ile plików ma formularz;
- **widać** = ile wartości tekstowych da się znaleźć w zbudowanej stronie (Podgląd, PL i EN) / ile ich jest;
- **kategoria**: „używane” = nazwę pola czyta kod strony (i dla kolekcji jest w schemacie). Przy nazwach ogólnych (`opis`, `adres`) to przybliżenie, które sprawdzę dokładnie w etapie danego repozytorium.

Web-Sem-*: 9 repozytoriów ma ten sam układ. Tabela pokazuje Web-Sem-Topologia, a różnice w danych opisuje raport.

## Web-Aktualnosci — aktualnosci

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 167/167 | 167/167 | używane |  |
| `data` | date |  | 167/167 |  | używane |  |
| `rodzaj` | select |  | 167/167 | 167/167 | używane |  |
| `termin.dzien` | date |  | 12/167 |  | używane |  |
| `termin.godzina` | string |  | 9/167 | 9/9 | używane |  |
| `termin.dzien_konca` | date |  | 3/167 |  | używane |  |
| `termin.godzina_konca` | string |  | 7/167 | 7/7 | używane |  |
| `termin.miejsce` | string |  | 12/167 | 12/12 | używane |  |
| `termin.pozycja` | boolean | tak | 1/167 |  | techniczne (ukryte) |  |
| `body` | code |  | 167/167 | 167/167 | używane |  |
| `tresc_en` | code |  | 167/167 | 167/167 | używane |  |
| `dla` | select |  | 151/167 | 256/256 | używane |  |
| `zajawka` | text |  | 164/167 | 164/164 | używane |  |
| `zdjecie` | image |  | 96/167 | 61/96 | używane |  |
| `zdjecie_opis` | string |  | 94/167 | 94/94 | używane |  |
| `zdjecie_opis_en` | string |  | 94/167 | 94/94 | używane |  |
| `galeria.plik` | image |  | 1/167 | 2/2 | używane |  |
| `galeria.podpis` | string |  | 1/167 | 2/2 | używane |  |
| `galeria.pozycja` | boolean | tak | 0/167 |  | techniczne (ukryte) |  |
| `album` | string |  | 0/167 |  | używane |  |
| `zalaczniki.nazwa` | string |  | 10/167 | 14/14 | używane |  |
| `zalaczniki.nazwa_en` | string |  | 9/167 | 12/12 | używane |  |
| `zalaczniki.plik` | file |  | 10/167 | 11/14 | używane |  |
| `zalaczniki.pozycja` | boolean | tak | 0/167 |  | techniczne (ukryte) |  |
| `zaklad` | select |  | 75/167 | 75/75 | używane |  |
| `tytul_en` | string |  | 165/167 | 165/165 | używane |  |
| `zajawka_en` | text |  | 163/167 | 163/163 | używane |  |

## Web-Aktualnosci — obrony

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `kandydat` | string |  | 5/5 | 5/5 | używane |  |
| `tytul_rozprawy` | string |  | 5/5 | 5/5 | używane |  |
| `termin` | date |  | 5/5 |  | używane |  |
| `miejsce` | string |  | 5/5 | 5/5 | używane |  |
| `body` | code |  | 0/5 |  | używane |  |
| `tresc_en` | code |  | 0/5 |  | używane |  |
| `zdjecie` | image |  | 0/5 |  | używane |  |
| `zdjecie_opis` | string |  | 0/5 |  | używane |  |
| `zdjecie_opis_en` | string |  | 0/5 |  | używane |  |
| `promotorzy` | string |  | 0/5 |  | używane |  |
| `data_ogloszenia` | date |  | 1/5 |  | używane |  |
| `w_aktualnosciach` | boolean |  | 5/5 |  | używane |  |
| `zawiadomienie` | file |  | 5/5 | 5/5 | używane |  |
| `rozprawa` | file |  | 5/5 | 5/5 | używane |  |
| `streszczenie_pl` | file |  | 5/5 | 5/5 | używane |  |
| `streszczenie_en` | file |  | 5/5 | 5/5 | używane |  |
| `recenzje.recenzent` | string |  | 5/5 | 15/15 | używane |  |
| `recenzje.plik` | file |  | 5/5 | 15/15 | używane |  |
| `recenzje.pozycja` | boolean | tak | 0/5 |  | techniczne (ukryte) |  |
| `bip` | string |  | 0/5 |  | używane |  |
| `zaklad` | select |  | 0/5 |  | używane |  |

## Web-Aktualnosci — strony

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 2/2 | 2/2 | używane |  |
| `body` | code |  | 1/2 | 1/1 | używane |  |
| `tytul_en` | string |  | 2/2 | 2/2 | używane |  |
| `tresc_en` | code |  | 1/2 | 1/1 | używane |  |
| `opis` | text |  | 2/2 | 2/2 | używane |  |
| `opis_en` | text |  | 2/2 | 2/2 | używane |  |
| `haslo` | string |  | 2/2 | 2/2 | używane |  |
| `haslo_en` | string |  | 2/2 | 2/2 | używane |  |
| `haslo_podstron` | string |  | 1/2 | 1/1 | używane |  |
| `haslo_podstron_en` | string |  | 1/2 | 1/1 | używane |  |
| `liczby.n` | string |  | 0/2 |  | używane |  |
| `liczby.n_en` | string |  | 0/2 |  | używane |  |
| `liczby.etykieta` | string |  | 0/2 |  | używane |  |
| `liczby.etykieta_en` | string |  | 0/2 |  | używane |  |
| `liczby.pozycja` | boolean | tak | 0/2 |  | techniczne (ukryte) |  |
| `pasek_boczny` | select |  | 0/2 |  | używane |  |
| `bloki` | boolean |  | 0/2 |  | używane |  |

## Web-Instytut — strona-dzialu

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `wstep` | text |  | 1/1 | 1/1 | używane |  |
| `wstep_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 1/1 | używane |  |
| `haslo_en` | string |  | 1/1 | 1/1 | używane |  |
| `o_instytucie_fakty.wartosc` | string |  | 1/1 | 4/4 | używane |  |
| `o_instytucie_fakty.wartosc_en` | string |  | 1/1 | 3/3 | używane |  |
| `o_instytucie_fakty.opis` | string |  | 1/1 | 4/4 | używane |  |
| `o_instytucie_fakty.opis_en` | string |  | 1/1 | 4/4 | używane |  |
| `o_instytucie_fakty.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `kontakt_godziny` | string |  | 0/1 |  | używane |  |
| `kontakt_godziny_en` | string |  | 0/1 |  | używane |  |

## Web-Instytut — zaklady

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `nazwa` | string |  | 9/9 | 9/9 | używane |  |
| `body` | code |  | 9/9 | 9/9 | używane |  |
| `tresc_en` | code |  | 9/9 | 9/9 | używane |  |
| `karta.nazwa_krotka` | string |  | 9/9 | 9/9 | używane |  |
| `karta.kierownik` | string |  | 9/9 | 9/9 | używane |  |
| `karta.telefon` | string |  | 0/9 |  | używane |  |
| `karta.opis` | text |  | 9/9 | 9/9 | używane |  |
| `karta.haslo` | string |  | 9/9 | 9/9 | używane |  |
| `karta.obszary` | string |  | 9/9 | 41/41 | używane |  |
| `karta.strona` | string |  | 0/9 |  | używane |  |
| `karta.zdjecie` | image |  | 0/9 |  | używane |  |
| `karta.zdjecie_opis` | string |  | 0/9 |  | używane |  |
| `karta.zdjecie_opis_en` | string |  | 0/9 |  | używane |  |
| `karta.nazwa_krotka_en` | string |  | 9/9 | 9/9 | używane |  |
| `karta.opis_en` | text |  | 9/9 | 9/9 | używane |  |
| `karta.haslo_en` | string |  | 9/9 | 9/9 | używane |  |
| `karta.obszary_en` | string |  | 9/9 | 41/41 | używane |  |
| `nazwa_en` | string |  | 9/9 | 9/9 | używane |  |
| `kolejnosc` | number |  | 9/9 |  | używane |  |

## Web-Instytut — strony

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 12/12 | 12/12 | używane |  |
| `body` | code |  | 11/12 | 11/11 | używane |  |
| `tytul_en` | string |  | 12/12 | 12/12 | używane |  |
| `tresc_en` | code |  | 11/12 | 11/11 | używane |  |
| `opis` | text |  | 12/12 | 12/12 | używane |  |
| `opis_en` | text |  | 12/12 | 12/12 | używane |  |
| `haslo` | string |  | 4/12 | 3/4 | używane |  |
| `haslo_en` | string |  | 4/12 | 3/4 | używane |  |
| `liczby.n` | string |  | 0/12 |  | używane |  |
| `liczby.n_en` | string |  | 0/12 |  | używane |  |
| `liczby.etykieta` | string |  | 0/12 |  | używane |  |
| `liczby.etykieta_en` | string |  | 0/12 |  | używane |  |
| `liczby.pozycja` | boolean | tak | 0/12 |  | techniczne (ukryte) |  |
| `pasek_boczny` | select |  | 10/12 | 10/10 | używane |  |
| `bloki` | boolean |  | 0/12 |  | używane |  |

## Web-Instytut — warto_wiedziec

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 4/4 | 4/4 | używane |  |
| `body` | code |  | 4/4 | 4/4 | używane |  |
| `tresc_en` | code |  | 4/4 | 4/4 | używane |  |
| `karta.rok` | string |  | 4/4 | 4/4 | używane |  |
| `karta.zajawka` | text |  | 4/4 | 4/4 | używane |  |
| `karta.zajawka_en` | text |  | 4/4 | 4/4 | używane |  |
| `karta.obraz` | image |  | 3/4 | 3/3 | używane |  |
| `karta.obraz_opis` | string |  | 3/4 | 3/3 | używane |  |
| `karta.obraz_opis_en` | string |  | 2/4 | 2/2 | używane |  |
| `karta.link` | string |  | 2/4 | 1/2 | używane |  |
| `karta.link_etykieta` | string |  | 2/4 | 2/2 | używane |  |
| `karta.link_etykieta_en` | string |  | 2/4 | 2/2 | używane |  |
| `tytul_en` | string |  | 3/4 | 3/3 | używane |  |
| `dzial` | select |  | 4/4 | 4/4 | używane |  |
| `na_glownej` | boolean |  | 4/4 |  | używane |  |
| `zawsze` | boolean |  | 1/4 |  | używane |  |
| `kolejnosc` | number |  | 3/4 |  | używane |  |
| `zrodla` | string |  | 3/4 | 12/12 | używane |  |

## Web-Instytut — wladze

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `wstep` | text |  | 1/1 | 1/1 | używane |  |
| `wstep_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | hasło: nowy nagłówek pokazuje je tylko przy liczbach w banerze |
| `haslo_en` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. |
| `osoby.rola` | string |  | 1/1 | 5/5 | używane |  |
| `osoby.imie_nazwisko` | string |  | 1/1 | 5/5 | używane |  |
| `osoby.zakres` | text |  | 1/1 | 1/1 | używane |  |
| `osoby.dyzur` | string |  | 0/1 |  | używane |  |
| `osoby.zdjecie` | image |  | 1/1 | 2/5 | używane |  |
| `osoby.rola_en` | string |  | 1/1 | 5/5 | używane |  |
| `osoby.zakres_en` | text |  | 1/1 | 1/1 | używane |  |
| `osoby.dyzur_en` | string |  | 0/1 |  | używane |  |
| `osoby.stopien` | string |  | 0/1 |  | używane |  |
| `osoby.email` | string |  | 0/1 |  | używane |  |
| `osoby.pokoj` | string |  | 0/1 |  | używane |  |
| `osoby.strona` | string |  | 0/1 |  | używane |  |
| `osoby.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `wydzial.tytul` | string |  | 1/1 | 1/1 | używane |  |
| `wydzial.tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `wydzial.opis` | string |  | 1/1 | 1/1 | używane |  |
| `wydzial.opis_en` | string |  | 1/1 | 1/1 | używane |  |
| `wydzial.osoby.rola` | string |  | 1/1 | 2/2 | używane |  |
| `wydzial.osoby.imie_nazwisko` | string |  | 1/1 | 2/2 | używane |  |
| `wydzial.osoby.email` | string |  | 1/1 | 2/2 | używane |  |
| `wydzial.osoby.dyzur` | string |  | 1/1 | 1/1 | używane |  |
| `wydzial.osoby.zdjecie` | image |  | 1/1 | 0/2 | używane |  |
| `wydzial.osoby.zakres` | text |  | 0/1 |  | używane |  |
| `wydzial.osoby.pokoj` | string |  | 0/1 |  | używane |  |
| `wydzial.osoby.rola_en` | string |  | 1/1 | 2/2 | używane |  |
| `wydzial.osoby.dyzur_en` | string |  | 1/1 | 1/1 | używane |  |
| `wydzial.osoby.zakres_en` | text |  | 0/1 |  | używane |  |
| `wydzial.osoby.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `wydzial.link.etykieta` | string |  | 1/1 | 1/1 | używane |  |
| `wydzial.link.etykieta_en` | string |  | 1/1 | 1/1 | używane |  |
| `wydzial.link.adres` | string |  | 1/1 | 1/1 | używane |  |
| `sekretariat.nazwa` | string |  | 1/1 | 1/1 | używane |  |
| `sekretariat.opis` | string |  | 0/1 |  | używane |  |
| `sekretariat.email` | string |  | 1/1 | 1/1 | używane |  |
| `sekretariat.telefony` | string |  | 1/1 | 2/2 | używane |  |
| `sekretariat.adres` | string |  | 1/1 | 1/1 | używane |  |
| `sekretariat.pokoj` | string |  | 0/1 |  | używane |  |
| `sekretariat.godziny` | string |  | 0/1 |  | używane |  |
| `sekretariat.osoby` | string |  | 1/1 | 2/2 | używane |  |
| `sekretariat.nazwa_en` | string |  | 1/1 | 1/1 | używane |  |
| `sekretariat.opis_en` | string |  | 0/1 |  | używane |  |
| `sekretariat.adres_en` | string |  | 1/1 | 1/1 | używane |  |
| `sekretariat.godziny_en` | string |  | 0/1 |  | używane |  |
| `kadencja` | code |  | 1/1 | 1/1 | używane |  |
| `kadencja_en` | text |  | 1/1 | 1/1 | używane |  |
| `rada.tytul` | string |  | 1/1 | 1/1 | używane |  |
| `rada.opis` | code |  | 1/1 | 1/1 | używane |  |
| `rada.tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `rada.opis_en` | text |  | 1/1 | 1/1 | używane |  |
| `linki.etykieta` | string |  | 1/1 | 4/4 | używane |  |
| `linki.adres` | string |  | 1/1 | 4/4 | używane |  |
| `linki.etykieta_en` | string |  | 1/1 | 4/4 | używane |  |
| `linki.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `zrodla` | string |  | 1/1 | 9/9 | używane |  |
| `do_uzupelnienia` | string |  | 1/1 | 0/5 | z treścią, nieużywane |  |

## Web-Nauka — strona-dzialu

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `wstep` | text |  | 1/1 | 1/1 | używane |  |
| `wstep_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 1/1 | używane |  |
| `haslo_en` | string |  | 1/1 | 1/1 | używane |  |
| `badania_fakty.wartosc` | string |  | 1/1 | 3/3 | używane |  |
| `badania_fakty.wartosc_en` | string |  | 1/1 | 1/1 | używane |  |
| `badania_fakty.opis` | string |  | 1/1 | 4/4 | używane |  |
| `badania_fakty.opis_en` | string |  | 1/1 | 4/4 | używane |  |
| `badania_fakty.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |

## Web-Nauka — konferencje

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 61/61 | 61/61 | używane |  |
| `poczatek` | date |  | 61/61 |  | używane |  |
| `koniec` | date |  | 61/61 |  | używane |  |
| `miejsce` | string |  | 61/61 | 61/61 | używane |  |
| `body` | code |  | 17/61 | 5/17 | z treścią, niewidoczne | opis konferencji: lista konferencji go nie pokazuje |
| `tytul_en` | string |  | 9/61 | 9/9 | używane |  |
| `strona` | string |  | 54/61 | 54/54 | używane |  |
| `organizatorzy` | string | tak | 0/61 |  | techniczne (ukryte) |  |
| `zaklad` | select |  | 45/61 | 45/45 | używane |  |
| `zdjecie` | image |  | 0/61 |  | używane |  |
| `odwolana` | boolean |  | 9/61 |  | używane |  |

## Web-Nauka — granty

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 94/94 | 94/94 | używane |  |
| `rodzaj` | select |  | 94/94 | 83/83 | używane |  |
| `rok_od` | number |  | 92/94 |  | używane |  |
| `rok_do` | number |  | 92/94 |  | używane |  |
| `body` | code |  | 0/94 |  | używane |  |
| `tytul_en` | string |  | 87/94 | 87/87 | używane |  |
| `kod` | string |  | 93/94 | 93/93 | używane |  |
| `program` | string |  | 7/94 | 7/7 | używane |  |
| `kierownik` | string |  | 94/94 | 94/94 | używane |  |
| `wykonawcy` | string |  | 20/94 | 20/20 | używane |  |
| `kwota` | string |  | 0/94 |  | używane |  |
| `zaklad` | select |  | 79/94 | 79/79 | używane |  |
| `strona` | string |  | 0/94 |  | używane |  |

## Web-Nauka — publikacje

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `lata.rok` | number |  | 1/1 |  | używane |  |
| `lata.plik` | file |  | 1/1 | 11/11 | używane |  |
| `lata.link` | string |  | 0/1 |  | używane |  |
| `lata.uwagi` | string |  | 0/1 |  | używane |  |
| `lata.uwagi_en` | string |  | 0/1 |  | używane |  |
| `lata.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `czasopisma.nazwa` | string |  | 1/1 | 3/3 | używane |  |
| `czasopisma.opis` | text |  | 1/1 | 3/3 | używane |  |
| `czasopisma.opis_en` | text |  | 1/1 | 3/3 | używane |  |
| `czasopisma.wydawca` | string |  | 1/1 | 3/3 | używane |  |
| `czasopisma.wydawca_en` | string |  | 1/1 | 3/3 | używane |  |
| `czasopisma.wsparcie` | string |  | 1/1 | 1/1 | używane |  |
| `czasopisma.wsparcie_en` | string |  | 1/1 | 1/1 | używane |  |
| `czasopisma.redakcja` | string |  | 1/1 | 1/1 | używane |  |
| `czasopisma.redakcja_en` | string |  | 1/1 | 1/1 | używane |  |
| `czasopisma.kontakt` | string |  | 1/1 | 1/1 | używane |  |
| `czasopisma.issn` | string |  | 1/1 | 3/3 | używane |  |
| `czasopisma.eissn` | string |  | 1/1 | 2/2 | używane |  |
| `czasopisma.adres` | string |  | 1/1 | 3/3 | używane |  |
| `czasopisma.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `archiwum` | text |  | 1/1 | 1/1 | używane |  |
| `archiwum_en` | text |  | 1/1 | 1/1 | używane |  |
| `zrodla` | string | tak | 1/1 | 5/5 | techniczne (ukryte) |  |
| `do_uzupelnienia` | string | tak | 1/1 | 2/3 | techniczne (ukryte) |  |

## Web-Nauka — publikacje-wykazy

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `rok` | number |  | 23/23 |  | używane |  |
| `uwagi` | text |  | 10/23 | 10/10 | używane |  |
| `uwagi_en` | text |  | 10/23 | 10/10 | używane |  |
| `pochodzenie` | select |  | 23/23 | 23/23 | używane |  |
| `zrodla` | string | tak | 23/23 | 23/23 | techniczne (ukryte) |  |
| `grupy.naglowek` | string |  | 2/23 | 14/14 | używane |  |
| `grupy.naglowek_en` | string |  | 2/23 | 14/14 | używane |  |
| `grupy.rok_wydania` | number |  | 2/23 |  | używane |  |
| `grupy.prace.autorzy` | string |  | 23/23 | 2165/2165 | używane |  |
| `grupy.prace.tytul` | string |  | 19/23 | 1818/1821 | używane |  |
| `grupy.prace.zrodlo` | string |  | 19/23 | 1825/1825 | używane |  |
| `grupy.prace.opis` | string |  | 5/23 | 340/340 | używane |  |
| `grupy.prace.doi` | string |  | 1/23 | 69/69 | używane |  |
| `grupy.prace.if` | string |  | 7/23 | 490/490 | używane |  |
| `grupy.prace.uwagi` | string |  | 5/23 | 299/299 | używane |  |

## Web-Nauka — strony

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 6/6 | 6/6 | używane |  |
| `body` | code |  | 6/6 | 6/6 | używane |  |
| `tytul_en` | string |  | 6/6 | 6/6 | używane |  |
| `tresc_en` | code |  | 6/6 | 6/6 | używane |  |
| `opis` | text |  | 6/6 | 6/6 | używane |  |
| `opis_en` | text |  | 6/6 | 6/6 | używane |  |
| `haslo` | string |  | 6/6 | 6/6 | używane |  |
| `haslo_en` | string |  | 6/6 | 6/6 | używane |  |
| `haslo_podstron` | string |  | 1/6 | 1/1 | używane |  |
| `haslo_podstron_en` | string |  | 1/6 | 1/1 | używane |  |
| `liczby.n` | string |  | 1/6 | 2/2 | używane |  |
| `liczby.n_en` | string |  | 0/6 |  | używane |  |
| `liczby.etykieta` | string |  | 1/6 | 3/3 | używane |  |
| `liczby.etykieta_en` | string |  | 1/6 | 3/3 | używane |  |
| `liczby.pozycja` | boolean | tak | 0/6 |  | techniczne (ukryte) |  |
| `pasek_boczny` | select |  | 0/6 |  | używane |  |
| `bloki` | boolean |  | 0/6 |  | używane |  |

## Web-Popularyzacja — popularyzacja

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `format_tresci` | string | tak | 1/1 | 1/1 | techniczne (ukryte) |  |
| `wstep` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 1/1 | używane |  |
| `o_popularyzacji_fakty.wartosc` | string |  | 1/1 | 4/4 | używane |  |
| `o_popularyzacji_fakty.wartosc_en` | string |  | 1/1 | 4/4 | używane |  |
| `o_popularyzacji_fakty.opis` | string |  | 1/1 | 4/4 | używane |  |
| `o_popularyzacji_fakty.opis_en` | string |  | 1/1 | 4/4 | używane |  |
| `o_popularyzacji_fakty.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `tradycja.rok` | number |  | 1/1 |  | używane |  |
| `tradycja.nazwa` | string |  | 1/1 | 3/3 | używane |  |
| `tradycja.nazwa_en` | string |  | 1/1 | 3/3 | używane |  |
| `tradycja.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `wstep_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo_en` | string |  | 1/1 | 1/1 | używane |  |
| `linki.nazwa` | string |  | 1/1 | 3/3 | używane |  |
| `linki.nazwa_en` | string |  | 1/1 | 3/3 | używane |  |
| `linki.adres` | string |  | 1/1 | 3/3 | używane |  |
| `linki.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |

## Web-Popularyzacja — strony

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 4/4 | 4/4 | używane |  |
| `body` | code |  | 4/4 | 4/4 | używane |  |
| `tytul_en` | string |  | 4/4 | 4/4 | używane |  |
| `tresc_en` | code |  | 4/4 | 4/4 | używane |  |
| `format_tresci` | string | tak | 4/4 | 4/4 | techniczne (ukryte) |  |
| `opis` | text |  | 4/4 | 4/4 | używane |  |
| `opis_en` | text |  | 4/4 | 4/4 | używane |  |
| `haslo` | string |  | 4/4 | 4/4 | używane |  |
| `haslo_en` | string |  | 4/4 | 4/4 | używane |  |
| `pasek_boczny` | select |  | 0/4 |  | używane |  |

## Web-Pracownicy — pracownicy

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `imie_nazwisko` | string |  | 128/128 | 128/128 | używane |  |
| `stopien` | string |  | 121/128 | 73/73 | używane |  |
| `grupa` | select |  | 128/128 | 128/128 | używane |  |
| `funkcja` | string |  | 7/128 | 7/7 | używane |  |
| `funkcja_en` | string |  | 7/128 | 7/7 | używane |  |
| `zaklad` | select |  | 119/128 | 119/119 | używane |  |
| `rok_studiow` | number |  | 17/128 |  | używane |  |
| `email` | string |  | 128/128 | 128/128 | używane |  |
| `telefon` | string |  | 7/128 | 7/7 | używane |  |
| `pokoj` | string |  | 114/128 | 114/114 | używane |  |
| `strona` | string |  | 108/128 | 108/108 | używane |  |

## Web-Pracownicy — strony

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 0/1 |  | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 0/1 |  | używane |  |
| `opis` | text |  | 1/1 | 1/1 | używane |  |
| `opis_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 1/1 | używane |  |
| `haslo_en` | string |  | 1/1 | 1/1 | używane |  |
| `liczby.n` | string |  | 0/1 |  | używane |  |
| `liczby.n_en` | string |  | 0/1 |  | używane |  |
| `liczby.etykieta` | string |  | 0/1 |  | używane |  |
| `liczby.etykieta_en` | string |  | 0/1 |  | używane |  |
| `liczby.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `pasek_boczny` | select |  | 0/1 |  | używane |  |
| `bloki` | boolean |  | 0/1 |  | używane |  |

## Web-Sem-Topologia — seminarium

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `nazwa` | string |  | 1/1 | 1/1 | używane |  |
| `nazwa_en` | string |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 1/1 | używane |  |
| `haslo_en` | string |  | 1/1 | 1/1 | używane |  |
| `prowadzacy` | string |  | 1/1 | 5/5 | używane |  |
| `kontakt` | string |  | 1/1 | 1/1 | używane |  |
| `archiwum` | string |  | 1/1 | 1/1 | używane |  |
| `zaklad` | select |  | 1/1 | 1/1 | używane |  |
| `aktywne` | boolean |  | 1/1 |  | używane |  |
| `do_uzupelnienia` | string |  | 0/1 |  | puste, nieużywane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |

## Web-Sem-Topologia — referaty

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `jezyk` | select |  | 0/1 |  | używane |  |
| `prelegent` | string |  | 1/1 | 1/1 | używane |  |
| `afiliacja` | string |  | 1/1 | 1/1 | używane |  |
| `afiliacja_en` | string |  | 1/1 | 1/1 | używane |  |
| `termin` | date |  | 1/1 |  | używane |  |
| `sala` | string |  | 1/1 | 1/1 | używane |  |
| `sala_en` | string |  | 1/1 | 1/1 | używane |  |
| `pliki.nazwa` | string |  | 0/1 |  | używane |  |
| `pliki.plik` | file |  | 0/1 |  | używane |  |
| `pliki.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |

## Web-Studia — strona-dzialu

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `format_tresci` | string | tak | 1/1 | 1/1 | techniczne (ukryte) |  |
| `wstep` | text |  | 1/1 | 1/1 | używane |  |
| `wstep_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 1/1 | używane |  |
| `haslo_en` | string |  | 1/1 | 1/1 | używane |  |
| `o_studiach_fakty.wartosc` | string |  | 1/1 | 4/4 | używane |  |
| `o_studiach_fakty.wartosc_en` | string |  | 1/1 | 2/2 | używane |  |
| `o_studiach_fakty.opis` | string |  | 1/1 | 4/4 | używane |  |
| `o_studiach_fakty.opis_en` | string |  | 1/1 | 4/4 | używane |  |
| `o_studiach_fakty.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `sekretariat_zakres` | string | tak | 1/1 | 1/1 | techniczne (ukryte) |  |
| `sekretariat_zakres_en` | string | tak | 1/1 | 1/1 | techniczne (ukryte) |  |

## Web-Studia — kierunki

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `nazwa` | string |  | 5/5 | 5/5 | używane |  |
| `nazwa_en` | string |  | 5/5 | 5/5 | używane |  |
| `body` | code |  | 5/5 | 5/5 | używane |  |
| `tresc_en` | code |  | 5/5 | 5/5 | używane |  |
| `format_tresci` | string | tak | 5/5 | 5/5 | techniczne (ukryte) |  |
| `opublikowany` | boolean |  | 2/5 |  | używane |  |
| `baner.podtytul` | string |  | 4/5 | 3/4 | używane |  |
| `baner.opis` | text |  | 5/5 | 5/5 | używane |  |
| `baner.haslo` | string |  | 5/5 | 5/5 | używane |  |
| `baner.liczby.wartosc` | string |  | 5/5 | 11/11 | używane |  |
| `baner.liczby.etykieta` | string |  | 5/5 | 19/19 | używane |  |
| `baner.liczby.etykieta_krotka` | string |  | 4/5 | 5/6 | z treścią, nieużywane |  |
| `baner.liczby.wartosc_en` | string |  | 3/5 | 6/6 | używane |  |
| `baner.liczby.etykieta_en` | string |  | 5/5 | 19/19 | używane |  |
| `baner.liczby.etykieta_krotka_en` | string |  | 4/5 | 3/6 | z treścią, nieużywane |  |
| `baner.liczby.pozycja` | boolean | tak | 0/5 |  | techniczne (ukryte) |  |
| `baner.podtytul_en` | string |  | 4/5 | 2/4 | z treścią, nieużywane |  |
| `baner.opis_en` | text |  | 5/5 | 5/5 | używane |  |
| `baner.haslo_en` | string |  | 5/5 | 5/5 | używane |  |

## Web-Studia — specjalnosci

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `nazwa` | string |  | 6/6 | 6/6 | używane |  |
| `nazwa_en` | string |  | 6/6 | 6/6 | używane |  |
| `body` | code |  | 6/6 | 5/6 | używane |  |
| `tresc_en` | code |  | 5/6 | 5/5 | używane |  |
| `format_tresci` | string | tak | 6/6 | 6/6 | techniczne (ukryte) |  |
| `kierunek` | reference |  | 6/6 |  | używane |  |
| `opiekunowie.osoba` | reference |  | 5/6 |  | używane |  |
| `opiekunowie.rola` | string |  | 2/6 | 3/3 | używane |  |
| `opiekunowie.rola_en` | string |  | 2/6 | 3/3 | używane |  |
| `opiekunowie.pozycja` | boolean | tak | 0/6 |  | techniczne (ukryte) |  |
| `zaklad` | select |  | 4/6 | 4/4 | używane |  |
| `seminaria` | select |  | 4/6 | 7/7 | używane |  |
| `wygaszana` | boolean |  | 6/6 |  | używane |  |
| `bez_podstrony` | boolean |  | 1/6 |  | używane |  |
| `zrodla` | string | tak | 5/6 | 75/80 | techniczne (ukryte) |  |
| `do_uzupelnienia` | string | tak | 5/6 | 25/39 | techniczne (ukryte) |  |
| `opublikowany` | boolean |  | 0/6 |  | używane |  |
| `baner.opis` | text |  | 6/6 | 6/6 | używane |  |
| `baner.opis_en` | text |  | 6/6 | 6/6 | używane |  |
| `baner.haslo` | string |  | 5/6 | 5/5 | używane |  |
| `baner.haslo_en` | string |  | 5/6 | 5/5 | używane |  |
| `baner.skrot` | string |  | 4/6 | 2/2 | używane |  |
| `baner.poziom` | string |  | 5/6 | 5/5 | używane |  |
| `baner.poziom_en` | string |  | 5/6 | 5/5 | używane |  |
| `baner.liczby.n` | string |  | 5/6 | 10/10 | używane |  |
| `baner.liczby.n_en` | string |  | 5/6 | 10/10 | używane |  |
| `baner.liczby.etykieta` | string |  | 5/6 | 15/15 | używane |  |
| `baner.liczby.etykieta_en` | string |  | 5/6 | 15/15 | używane |  |
| `baner.liczby.pozycja` | boolean | tak | 0/6 |  | techniczne (ukryte) |  |

## Web-Studia — przypomnienia

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `przypomnienia.sprawa` | string |  | 1/1 | 3/3 | używane |  |
| `przypomnienia.podpis` | string |  | 1/1 | 3/3 | używane |  |
| `przypomnienia.data` | date |  | 1/1 |  | używane |  |
| `przypomnienia.co_roku` | boolean |  | 1/1 |  | używane |  |
| `przypomnienia.dni_przed` | number |  | 1/1 |  | używane |  |
| `przypomnienia.adres` | string |  | 1/1 | 3/3 | używane |  |
| `przypomnienia.sprawa_en` | string |  | 1/1 | 3/3 | używane |  |
| `przypomnienia.podpis_en` | string |  | 1/1 | 3/3 | używane |  |
| `przypomnienia.uid` | string | tak | 1/1 | 0/3 | techniczne (ukryte) |  |

## Web-Studia — strony

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 14/14 | 14/14 | używane |  |
| `tytul_en` | string |  | 14/14 | 14/14 | używane |  |
| `body` | code |  | 14/14 | 13/13 | używane |  |
| `tresc_en` | code |  | 13/14 | 13/13 | używane |  |
| `format_tresci` | string | tak | 14/14 | 14/14 | techniczne (ukryte) |  |
| `opis` | text |  | 14/14 | 14/14 | używane |  |
| `opis_en` | text |  | 14/14 | 14/14 | używane |  |
| `haslo` | string |  | 13/14 | 4/13 | z treścią, niewidoczne | jw. (widać na 4 z 13 stron) |
| `haslo_en` | string |  | 13/14 | 4/13 | z treścią, niewidoczne | jw. |
| `liczby.n` | string |  | 3/14 |  | używane |  |
| `liczby.n_en` | string |  | 0/14 |  | używane |  |
| `liczby.etykieta` | string |  | 3/14 | 9/9 | używane |  |
| `liczby.etykieta_en` | string |  | 3/14 | 9/9 | używane |  |
| `liczby.pozycja` | boolean | tak | 0/14 |  | techniczne (ukryte) |  |
| `pasek_boczny` | select |  | 0/14 |  | używane |  |
| `opublikowany` | boolean | tak | 13/14 |  | techniczne (ukryte) |  |

## Web-Studia — rok-akademicki

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `dalej` | code |  | 1/1 | 1/1 | używane |  |
| `dalej_en` | code |  | 1/1 | 1/1 | używane |  |
| `format_tresci` | string | tak | 1/1 | 1/1 | techniczne (ukryte) |  |
| `opis` | text |  | 1/1 | 1/1 | używane |  |
| `opis_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 1/1 | używane |  |
| `haslo_en` | string |  | 1/1 | 1/1 | używane |  |

## Web-Studia — kolory-dni

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `aktualnosci.wlaczone` | boolean |  | 1/1 |  | używane |  |
| `aktualnosci.dni_robocze_przed` | number |  | 1/1 |  | używane |  |
| `aktualnosci.tytul` | string |  | 1/1 | 0/1 | używane |  |
| `aktualnosci.tresc` | code |  | 1/1 | 1/1 | używane |  |
| `aktualnosci.tytul_en` | string |  | 1/1 | 0/1 | używane |  |
| `aktualnosci.tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `semestry.nazwa` | string |  | 1/1 | 2/2 | używane |  |
| `semestry.nazwa_en` | string |  | 1/1 | 2/2 | używane |  |
| `semestry.poczatek` | date |  | 1/1 |  | używane |  |
| `semestry.koniec` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.semestr_od` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.semestr_do` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.inauguracja` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.sesja_od` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.sesja_do` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.poprawkowa_od` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.poprawkowa_do` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.przerwy.od` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.przerwy.do` | date |  | 1/1 |  | używane |  |
| `semestry.terminy.przerwy.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `semestry.wolne.od` | date |  | 1/1 |  | używane |  |
| `semestry.wolne.do` | date |  | 1/1 |  | używane |  |
| `semestry.wolne.opis` | string |  | 1/1 | 6/6 | używane |  |
| `semestry.wolne.opis_en` | string |  | 1/1 | 6/6 | używane |  |
| `semestry.wolne.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `semestry.zamiany.data` | date |  | 1/1 |  | używane |  |
| `semestry.zamiany.jak_dzien` | select |  | 1/1 | 1/1 | używane |  |
| `semestry.zamiany.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `semestry.wyjatki.data` | date |  | 0/1 |  | używane |  |
| `semestry.wyjatki.kolor` | select |  | 0/1 |  | używane |  |
| `semestry.wyjatki.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `semestry.pdf` | file |  | 1/1 | 1/1 | używane |  |
| `semestry.uwagi` | text |  | 1/1 | 1/1 | używane |  |
| `semestry.uwagi_en` | text |  | 1/1 | 1/1 | używane |  |

## Web-Studia — katalog-pracownikow

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `imie_nazwisko` | string |  | 129/129 | 129/129 | używane |  |
| `id` | string |  | 129/129 | 129/129 | używane |  |
| `etykieta` | string |  | 129/129 | 129/129 | używane |  |

## Web-Ustawienia — ustawienia

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `baner.zdjecie` | image |  | 1/1 | 1/1 | używane |  |
| `baner.zdjecie_male` | image | tak | 1/1 | 1/1 | z treścią, nieużywane |  |
| `baner.zdjecie_telefon` | image | tak | 1/1 | 0/1 | z treścią, nieużywane |  |
| `baner.opis` | string |  | 1/1 | 1/1 | używane |  |
| `baner.opis_en` | string |  | 1/1 | 1/1 | używane |  |
| `baner.podpis` | string | tak | 1/1 | 0/1 | z treścią, nieużywane |  |
| `baner.podpis_en` | string | tak | 1/1 | 0/1 | z treścią, nieużywane |  |
| `baner.podpis_telefon` | string | tak | 0/1 |  | puste, nieużywane |  |
| `baner.podpis_telefon_en` | string | tak | 0/1 |  | puste, nieużywane |  |
| `baner.kadr` | string | tak | 1/1 | 0/1 | z treścią, nieużywane |  |
| `logo` | image |  | 0/1 |  | używane |  |
| `tlo_strony` | select | tak | 1/1 | 1/1 | techniczne (ukryte) |  |
| `sekcje` | select | tak | 1/1 | 1/1 | techniczne (ukryte) |  |
| `naglowki_podstron.wariant` | select |  | 1/1 | 1/1 | używane |  |
| `naglowki_podstron.zdjecia.instytut.zdjecie` | image |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.instytut.kadr` | string |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.nauka.zdjecie` | image |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.nauka.kadr` | string |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.studia.zdjecie` | image |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.studia.kadr` | string |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.aktualnosci.zdjecie` | image |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.aktualnosci.kadr` | string |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.popularyzacja.zdjecie` | image |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `naglowki_podstron.zdjecia.popularyzacja.kadr` | string |  | 1/1 | 0/1 | z treścią, nieużywane |  |
| `wydarzenia_dni_robocze` | number |  | 1/1 |  | używane |  |
| `wydarzenia_dni_telefon` | number |  | 1/1 |  | używane |  |
| `wstep` | text |  | 1/1 | 1/1 | używane |  |
| `wstep_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string | tak | 1/1 | 0/1 | techniczne (ukryte) |  |
| `haslo_en` | string | tak | 1/1 | 0/1 | techniczne (ukryte) |  |
| `szukaj_haslo` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. (strona wyszukiwania) |
| `szukaj_haslo_en` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. |
| `przyciski.etykieta` | string |  | 1/1 | 2/3 | z treścią, nieużywane |  |
| `przyciski.etykieta_en` | string |  | 1/1 | 2/3 | z treścią, nieużywane |  |
| `przyciski.adres` | string |  | 1/1 | 3/3 | z treścią, nieużywane |  |
| `przyciski.pozycja` | boolean | tak | 0/1 |  | puste, nieużywane |  |
| `studia.tytul` | string |  | 1/1 | 1/1 | używane |  |
| `studia.tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `studia.opis` | string |  | 1/1 | 1/1 | używane |  |
| `studia.opis_en` | string |  | 1/1 | 1/1 | używane |  |
| `studia.rekrutacja` | string |  | 1/1 | 1/1 | używane |  |
| `studia.kierunki.adres` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.nazwa_menu` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.opis_menu` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.nazwa` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.poziom` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.opis` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.w_menu` | boolean |  | 1/1 |  | używane |  |
| `studia.kierunki.na_stronie_glownej` | boolean |  | 1/1 |  | używane |  |
| `studia.kierunki.nazwa_menu_en` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.opis_menu_en` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.nazwa_en` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.poziom_en` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.opis_en` | string |  | 1/1 | 5/5 | używane |  |
| `studia.kierunki.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |
| `kontakt.adres` | string |  | 1/1 | 1/1 | używane |  |
| `kontakt.telefon` | string |  | 1/1 | 1/1 | używane |  |
| `kontakt.email` | string |  | 1/1 | 1/1 | używane |  |
| `facebook` | string | tak | 1/1 | 1/1 | z treścią, nieużywane |  |
| `youtube` | string | tak | 1/1 | 1/1 | z treścią, nieużywane |  |
| `archiwum` | string |  | 1/1 | 1/1 | używane |  |
| `powiadomienia.adres` | string |  | 0/1 |  | używane |  |
| `partnerzy.nazwa` | string |  | 0/1 |  | puste, nieużywane |  |
| `partnerzy.logo` | image |  | 0/1 |  | puste, nieużywane |  |
| `partnerzy.adres` | string |  | 0/1 |  | puste, nieużywane |  |
| `partnerzy.pozycja` | boolean | tak | 0/1 |  | puste, nieużywane |  |

## Web-Ustawienia — skroty

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `kafelki.etykieta` | string |  | 1/1 | 4/4 | używane |  |
| `kafelki.etykieta_en` | string |  | 1/1 | 4/4 | używane |  |
| `kafelki.adres` | string |  | 1/1 | 4/4 | używane |  |
| `kafelki.ikona` | select |  | 1/1 | 4/4 | używane |  |
| `kafelki.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |

## Web-Ustawienia — nawigacja

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `menu.etykieta` | string |  | 1/1 | 6/6 | używane |  |
| `menu.etykieta_en` | string |  | 1/1 | 6/6 | używane |  |
| `menu.adres` | string |  | 1/1 | 6/6 | używane |  |
| `menu.grupy.nazwa` | string |  | 1/1 | 11/11 | używane |  |
| `menu.grupy.nazwa_en` | string |  | 1/1 | 11/11 | używane |  |
| `menu.grupy.opis` | string |  | 1/1 | 11/11 | używane |  |
| `menu.grupy.opis_en` | string |  | 1/1 | 11/11 | używane |  |
| `menu.grupy.kierunki` | boolean |  | 1/1 |  | używane |  |
| `menu.grupy.linki.etykieta` | string |  | 1/1 | 29/29 | używane |  |
| `menu.grupy.linki.etykieta_en` | string |  | 1/1 | 29/29 | używane |  |
| `menu.grupy.linki.opis` | string |  | 1/1 | 29/29 | używane |  |
| `menu.grupy.linki.opis_en` | string |  | 1/1 | 29/29 | używane |  |
| `menu.grupy.linki.adres` | string |  | 1/1 | 29/29 | używane |  |
| `menu.grupy.linki.pozycja` | boolean | tak | 0/1 |  | techniczne (ukryte) |  |

## Web-Ustawienia — deklaracja

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `opis` | text |  | 1/1 | 1/1 | używane |  |
| `opis_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. |
| `haslo_en` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. |
| `pasek_boczny` | select |  | 0/1 |  | używane |  |
| `bloki` | boolean |  | 0/1 |  | używane |  |

## Web-Ustawienia — prywatnosc

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `opis` | text |  | 1/1 | 1/1 | używane |  |
| `opis_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. |
| `haslo_en` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. |
| `pasek_boczny` | select |  | 0/1 |  | używane |  |
| `bloki` | boolean |  | 0/1 |  | używane |  |

## Web-Ustawienia — o-stronie

| pole | typ | ukryte | z treścią | widać | kategoria | uwagi |
|---|---|---|---|---|---|---|
| `tytul` | string |  | 1/1 | 1/1 | używane |  |
| `body` | code |  | 1/1 | 1/1 | używane |  |
| `tytul_en` | string |  | 1/1 | 1/1 | używane |  |
| `tresc_en` | code |  | 1/1 | 1/1 | używane |  |
| `opis` | text |  | 1/1 | 1/1 | używane |  |
| `opis_en` | text |  | 1/1 | 1/1 | używane |  |
| `haslo` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. |
| `haslo_en` | string |  | 1/1 | 0/1 | z treścią, niewidoczne | jw. |
| `pasek_boczny` | select |  | 1/1 | 1/1 | używane |  |
| `bloki` | boolean |  | 0/1 |  | używane |  |
