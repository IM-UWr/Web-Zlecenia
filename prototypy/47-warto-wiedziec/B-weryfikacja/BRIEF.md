# Brief: sylwetka do „Warto wiedzieć” (strona Instytutu Matematycznego UWr)

Piszesz tekst sylwetki jednej osoby do nowej grupy „Sylwetki” w dziale „Warto wiedzieć” na nowej stronie Instytutu Matematycznego Uniwersytetu Wrocławskiego. Tekst przeczyta student, pracownik albo gość strony. Ma być rzetelny, ciepły i instytucjonalny, jak noty biograficzne, które dla Instytutu napisał Grzegorz.

## 1. Wzór — przeczytaj OBA przed pisaniem
- `/home/claude/sylwetki/marekbozejkonotabiograficzna.txt`
- `/home/claude/sylwetki/tomaszrolskinotabiograficzna.txt`

Weź z nich ton, sposób prowadzenia narracji i budowę: akapit wstępny („kim był/jest i dlaczego ważny”), potem 4–6 sekcji z nagłówkami, np.:
- Droga naukowa (prozą, NIE w punktach)
- Najważniejsze osiągnięcia (każde twierdzenie/wynik: nazwa + jedno zdanie, o co w nim chodzi, zrozumiałe dla studenta)
- Uczniowie i szkoła
- We Wrocławiu / w Instytucie (wkład w Instytut, funkcje, seminaria, czasopisma)
- Nagrody i upamiętnienie

Nazwy sekcji dobierz do osoby. **Bez osi czasu, bez list dat w punktach** (to będzie później) — sama proza.

## 2. Długość
700–1300 słów. Krócej, jeśli źródeł jest mało — nie lej wody, nie dopisuj ogólników.

## 3. Format pliku wyjściowego
Zapisz do `/home/claude/sylwetki/<id>.md` (id podany w zleceniu):

```markdown
---
tytul: "Imię Nazwisko"
lata: "1887–1972"
podpis: "Jedna linijka pod nazwiskiem w banerze, do 70 znaków"
zajawka: "1–2 zdania na kartę na liście i do losowania na stronie głównej (do 220 znaków)."
rocznica_urodzin: "MM-DD"   # tylko jeśli data urodzenia jest pewna (2 źródła), inaczej usuń linię
---

<!-- W SKRÓCIE: każdy punkt: **duża liczba lub rok** — krótki podpis. 3–5 punktów. -->
:::w-skrocie

- **1887–1972** — lata życia
- **1931** — pochodna Liego
- **20** — wypromowanych doktorów

:::

Akapit wstępny…

## Droga naukowa {#droga}

Tekst…

## Najważniejsze osiągnięcia {#osiagniecia}

Tekst…

## Źródła {#zrodla}

- [Tytuł strony](URL) — co z niego wzięto
```

- W „W skrócie” tylko rzeczy pewne i konkretne (lata, rok kluczowego wyniku, liczba doktorów z Mathematics Genealogy Project z dopiskiem w podpisie, funkcja z latami).
- Linki do innych sylwetek i wpisów: przy **pierwszym** wspomnieniu osoby z listy niżej zrób link `[Hugo Steinhaus](/instytut/warto-wiedziec/hugo-steinhaus)`. Tylko raz na osobę. Tak samo do wpisów, jeśli naturalnie pasują.
  - Sylwetki (id): `wladyslaw-slebodzinski`, `hugo-steinhaus`, `bronislaw-knaster`, `edward-marczewski`, `witold-wolibner`, `stanislaw-hartman`, `czeslaw-ryll-nardzewski`, `kazimierz-urbanik`, `andrzej-hulanicki`, `andrzej-krzywicki`, `marek-bozejko`, `tomasz-rolski`.
  - Wpisy (id): `pierwsze-wyklady` (15.11.1945), `nowa-ksiega-szkocka` (1946), `taksonomia-wroclawska` (1951), `aksjomat-determinacji` (1962, Mycielski i Steinhaus), `trzech-rektorow` (Marczewski, Urbanik, Duda), `zywa-ges` (Mazur, Enflo 1972), `probability-and-mathematical-statistics` (1980).

## 4. Źródła i fakty — zasady twarde
- Szukaj w sieci (WebSearch, WebFetch): polska i angielska Wikipedia, MacTutor (St Andrews), wspomnienia i nekrologi w „Wiadomościach Matematycznych” / „Colloquium Mathematicum”, Encyklopedia PWN, strony UWr / IM PAN / PAN, Mathematics Genealogy Project, Polski Słownik Biograficzny, Internetowy Polski Słownik Biograficzny, archiwalne strony Instytutu.
- Dane z naszej strony (lokalnie, możesz czytać):
  - ciekawostki patronów: `/home/claude/repo/Web-Core/src/data/ciekawostki/{instytut,nauka,studia,popularyzacja}.json` (Marczewski, Ślebodziński, Knaster, Steinhaus) — pomocnicze, same też „do weryfikacji”;
  - tekst „O Instytucie”: `/home/claude/repo/Web-Instytut/src/data/instytut.md`;
  - historyczne nagrody pracowników: `/home/claude/repo/Web-Nauka/src/content/strony/nauka/sukcesy/historia.md`.
- **Każdy fakt w tekście musi mieć źródło.** Daty, funkcje, nazwy twierdzeń i nagrody — najlepiej z dwóch niezależnych źródeł. Gdy źródła się różnią — opisz to w pliku weryfikacji, a w tekście użyj wersji pewniejszej albo pomiń.
- **Niczego nie wymyślaj.** Żadnych anegdot bez źródła, żadnych „prawdopodobnie”. Lepiej krótszy tekst.
- **Pisz własnymi słowami.** Nie przepisuj zdań ze źródeł (także z Wikipedii) i nie parafrazuj ich zdanie po zdaniu. Najwyżej jeden krótki cytat (do 15 słów, np. słynny aforyzm) w cudzysłowie i z autorem.
- Osoba żyjąca: tylko fakty publiczne i zawodowe, ton neutralny; zaznacz w pliku weryfikacji „osoba żyjąca — tekst do akceptacji przez nią”.
- **Zdjęć nie szukaj, nie pobieraj i nie linkuj.** Zdjęcia dostarczy Instytut.
- Polszczyzna poprawna, polskie cudzysłowy „…”, półpauza w zakresach lat (1957–1962).

## 5. Plik weryfikacji
Zapisz też `/home/claude/sylwetki/<id>-weryfikacja.md`:
- tabela: fakt → źródło (źródła);
- rozbieżności między źródłami;
- czego nie udało się potwierdzić (i co pominięto);
- pytania do Instytutu (np. archiwum, rodzina, uczniowie).

## 6. Odpowiedź końcowa (krótka, do 120 słów)
Ścieżki obu plików, liczba słów tekstu i 3–6 punktów „do sprawdzenia”. Bez wklejania tekstu sylwetki.
