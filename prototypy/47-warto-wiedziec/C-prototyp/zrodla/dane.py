# Przykładowe wpisy „Warto wiedzieć” do prototypu (18.11.2026).
# Fakty: teksty istniejących wpisów z Web-Instytut, tekst „O Instytucie” z obecnej strony /instytut
# i aktualności z Web-Aktualnosci. Laureaci: z aktualności (rok = rok daty aktualności).

LIVE = 'https://im-uwr.github.io/Web-Podglad'

GRUPY = [
    ('sylwetki', 'Sylwetki'),
    ('nagrody', 'Nagrody i wyróżnienia'),
    ('historie', 'Historie'),
]

def akt(slug):
    return f'{LIVE}/aktualnosci/{slug}'

WPISY = [
    # ---------------------------------------------------------------- Historia
    dict(id='pierwsze-wyklady', osoby=['hugo-steinhaus','edward-marczewski','bronislaw-knaster','wladyslaw-slebodzinski'], grupa='historia', rok=1945,
         tytul='Pierwsze wykłady matematyki we Wrocławiu',
         zajawka='15 listopada 1945 roku ruszyły wykłady na polskim Uniwersytecie we Wrocławiu. Matematykę budowało od podstaw czterech pionierów: Steinhaus, Marczewski, Knaster i Ślebodziński.',
         rocznica='11-15', stan='ulubiona',
         tresc='''Instytut Matematyczny wyrasta z tradycji przedwojennych szkół matematycznych: lwowskiej i warszawskiej. Wykłady na polskim Uniwersytecie we Wrocławiu ruszyły **15 listopada 1945 roku**, a wrocławską matematykę budowało od podstaw czterech pionierów: **Hugo Steinhaus**, **Edward Marczewski**, **Bronisław Knaster** i **Władysław Ślebodziński**.

Tak narodziła się wrocławska szkoła matematyczna, a Wrocław szybko stał się jednym z najważniejszych ośrodków matematycznych w Polsce.'''),
    dict(id='nowa-ksiega-szkocka', osoby=['hugo-steinhaus'], grupa='historia', rok=1946,
         tytul='Nowa Księga Szkocka',
         zajawka='W 1946 roku Hugo Steinhaus wpisał pierwsze zagadnienie do Nowej Księgi Szkockiej — wrocławskiej kontynuacji słynnego lwowskiego zbioru problemów.',
         stan='ulubiona',
         tresc='''W 1946 roku **Hugo Steinhaus** wpisał pierwsze zagadnienie do **Nowej Księgi Szkockiej** — kontynuacji słynnego lwowskiego zbioru problemów, nazwanego od Kawiarni Szkockiej, w której spotykali się matematycy lwowscy.

Nowa Księga Szkocka jest przechowywana w bibliotece Wydziału Matematyki i Informatyki, którego częścią jest Instytut.'''),
    dict(id='trzech-rektorow', osoby=['edward-marczewski', 'kazimierz-urbanik', 'roman-duda'], grupa='historia', rok=1953,
         tytul='Czterech rektorów-matematyków',
         zajawka='Czterech matematyków z Instytutu kierowało Uniwersytetem Wrocławskim jako rektorzy: Marczewski, Urbanik, Łukaszewicz i Duda.',
         tresc='''Czterech matematyków z naszego Instytutu kierowało Uniwersytetem Wrocławskim jako rektorzy:

- [Edward Marczewski](/instytut/warto-wiedziec/edward-marczewski) — 1953–1957,
- [Kazimierz Urbanik](/instytut/warto-wiedziec/kazimierz-urbanik) — 1975–1981,
- Józef Łukaszewicz — 1981–1982, uczeń Hugona Steinhausa i jeden z autorów taksonomii wrocławskiej,
- [Roman Duda](/instytut/warto-wiedziec/roman-duda) — 1995–1999.'''),
    dict(id='zywa-ges', grupa='historia', rok=1972,
         tytul='Żywa gęś dla Pera Enflo',
         zajawka='W Księdze Szkockiej Stanisław Mazur obiecał za rozwiązanie jednego z problemów żywą gęś. Per Enflo odebrał nagrodę w 1972 roku.',
         stan='ulubiona',
         tresc='''Lwowska Księga Szkocka słynęła z nagród za rozwiązania problemów. **Stanisław Mazur** obiecał za jeden z nich **żywą gęś**. Problem rozwiązał szwedzki matematyk **Per Enflo**, który odebrał nagrodę w 1972 roku.

Tę tradycję kontynuuje Nowa Księga Szkocka, prowadzona we Wrocławiu od 1946 roku.'''),
    dict(id='wyklad-tao', grupa='historia', rok=2017, istniejacy=True,
         tytul='Wykład Terence’a Tao we Wrocławiu',
         zajawka='6 września 2017 r. laureat Medalu Fieldsa Terence Tao wygłosił we Wrocławiu otwarty wykład The Erdős discrepancy problem. Według szacunków przyszło ponad pół tysiąca osób.',
         obraz='tao', obraz_opis='Pełna sala podczas wykładu Terence’a Tao, 6 września 2017 r.',
         link='https://www.youtube.com/watch?v=_TWzrNhYNXc', link_etykieta='Obejrzyj wykład na YouTube',
         rocznica='09-06', stan='ulubiona',
         tresc='''Laureat Medalu Fieldsa prof. **Terence Tao** (UCLA) wygłosił 6 września 2017 r. otwarty wykład popularnonaukowy *The Erdős discrepancy problem*. Wykład był częścią konferencji [Analysis and Applications](/nauka/konferencje#rok-2017) na cześć Profesora Eliasa M. Steina, zorganizowanej w naszym Instytucie w dniach 4–8 września 2017 r. Wśród jej uczestników było czterech medalistów Fieldsa: Jean Bourgain, Charles Fefferman, Elon Lindenstrauss i Terence Tao.

Wykład odbył się w sali IICDEF na Wydziale Chemii UWr, a sala pękała w szwach: szacujemy, że przyszło ponad pół tysiąca osób — uczniów i studentów, zawodowych matematyków i amatorów-pasjonatów. Poprzedził go wykład wprowadzający prof. Pawła Strzeleckiego z Uniwersytetu Warszawskiego *Szeregi Fouriera: jak z prostych cegiełek budować dowolne funkcje?*.

Nagranie wykładu jest dostępne na [kanale YouTube Instytutu](https://www.youtube.com/channel/UCO0NMxdgMe2ZISJAbEcKH4w).'''),

    # ---------------------------------------------------------------- Odkrycia i publikacje
    dict(id='taksonomia-wroclawska', osoby=['hugo-steinhaus'], grupa='odkrycia', rok=1951,
         tytul='Taksonomia wrocławska',
         zajawka='Metoda klasyfikacji oparta na najkrótszym dendrycie łączącym punkty zbioru — jedno z wczesnych, niezależnych rozwiązań problemu minimalnego drzewa rozpinającego.',
         tresc='''Na seminarium zastosowań Hugona Steinhausa powstała **taksonomia wrocławska** — metoda klasyfikacji oparta na najkrótszym dendrycie łączącym punkty zbioru. Opublikowali ją w 1951 roku **Florek, Łukaszewicz, Perkal, Steinhaus i Zubrzycki**.

To jedno z wczesnych, niezależnych rozwiązań problemu, który dziś nazywa się problemem minimalnego drzewa rozpinającego.'''),
    dict(id='aksjomat-determinacji', osoby=['hugo-steinhaus'], grupa='odkrycia', rok=1962,
         tytul='Aksjomat determinacji',
         zajawka='W 1962 roku Jan Mycielski i Hugo Steinhaus zaproponowali aksjomat determinacji.',
         tresc='''W 1962 roku **Jan Mycielski** i **Hugo Steinhaus** zaproponowali **aksjomat determinacji** — aksjomat teorii mnogości mówiący o grach nieskończonych.'''),
    dict(id='probability-and-mathematical-statistics', grupa='odkrycia', rok=1980,
         tytul='Probability and Mathematical Statistics',
         zajawka='W 1980 roku wrocławscy probabiliści założyli czasopismo Probability and Mathematical Statistics.',
         tresc='''**Kazimierz Urbanik** kierował pierwszą w polskiej matematyce katedrą rachunku prawdopodobieństwa. W 1980 roku wrocławscy probabiliści założyli czasopismo **Probability and Mathematical Statistics**.

To niejedyne czasopismo związane z Wrocławiem: czwórka pionierów założyła „Colloquium Mathematicum”, którego redakcja do dziś mieści się w Instytucie, a w 1948 roku we Wrocławiu wznowiono wydawanie lwowskich „Studia Mathematica”.'''),
    dict(id='annals', grupa='odkrycia', rok=2022, istniejacy=True,
         tytul='Artykuł w Annals of Mathematics',
         zajawka='Prof. Mariusz Mirek wraz z Benem Krause i Terencem Tao opublikował artykuł w Annals of Mathematics — najbardziej prestiżowym czasopiśmie matematycznym na świecie.',
         link='https://annals.math.princeton.edu/2022/195-3/p04', link_etykieta='Artykuł na stronie Annals of Mathematics',
         stan='ulubiona',
         tresc='''Prof. **Mariusz Mirek** z naszego Instytutu jest — wraz z **Benem Krause** i **Terencem Tao** — współautorem artykułu *Pointwise ergodic theorems for non-conventional bilinear polynomial averages*, opublikowanego w czasopiśmie **Annals of Mathematics**, najbardziej prestiżowym czasopiśmie matematycznym na świecie.

Jest to wydarzenie tak ważne, że poświęcono mu [specjalny artykuł](https://www.math.uni.wroc.pl/~pborod/preprints/mirek.pdf) w *Przeglądzie Uniwersyteckim*.

Za tę pracę autorzy otrzymali nagrodę [ICCM Best Paper Award in Mathematics 2023](/aktualnosci/2023-11-25-mariusz-mirek-z-nagroda-best-paper-award-in-mathematics-2023).

## Dane bibliograficzne

B. Krause, M. Mirek, T. Tao, *Pointwise ergodic theorems for non-conventional bilinear polynomial averages*, Annals of Mathematics **195** (2022), nr 3, s. 997–1109, DOI: [10.4007/annals.2022.195.3.4](https://doi.org/10.4007/annals.2022.195.3.4).'''),

    # ---------------------------------------------------------------- Nagrody i wyróżnienia
    dict(id='stypendium-steinhausa', grupa='nagrody', rok=None, kolejnosc=60,
         tytul='Stypendium im. Hugona Steinhausa',
         zajawka='Stypendium Wrocławskiego Centrum Akademickiego w zakresie nauk matematycznych. Otrzymało je już dziesięcioro doktorantów naszego Instytutu.',
         lista_tytul='Laureaci z Instytutu',
         laureaci=[
             (2026, 'Dominik Gdesz', '2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza', '2026-11-11', None),
             (2025, 'Piotr Błaszkiewicz', '2025-11-05-stypendium-im-steinhausa-dla-piotra-blaszkiewicza', '2025-11-05', None),
             (2024, 'Maciej Korpalski', '2024-11-14-stypendium-im-steinhausa-dla-macieja-korpalskiego', '2024-11-14', None),
             (2022, 'Daniel Danielski', '2022-11-16-stypendium-im-steinhausa-dla-daniela-danielskiego', '2022-11-16', None),
             (2021, 'Szymon Cygan', '2021-11-16-stypendium-im-steinhausa-dla-szymona-cygana', '2021-11-16', None),
             (2019, 'Edyta Kania', '2019-11-14-stypendium-im-steinhausa-dla-edyty-kani', '2019-11-14', None),
             (2018, 'Agnieszka Hejna', '2018-11-12-stypendium-im-steinhausa-dla-agnieszki-hejny', '2018-11-12', None),
             (2017, 'Piotr Dyszewski', '2017-11-14-stypendium-im-steinhausa-dla-piotra-dyszewskiego', '2017-11-14', None),
             (2016, 'Daniel Hoffmann', '2016-11-13-stypendium-im-steinhausa-dla-daniela-hoffmanna', '2016-11-13', None),
             (2015, 'Grzegorz Świderski', '2015-01-01-stypendium-im-hugona-steinhausa-dla-grzegorza-swiderskiego', '2015-01-01', None),
         ],
         tresc='''Stypendium jest częścią **Studenckiego Programu Stypendialnego**, który prowadzi Wrocławskie Centrum Akademickie; w zakresie nauk matematycznych nosi imię [**Hugona Steinhausa**](w-hugo-steinhaus.html), jednego z czterech pionierów wrocławskiej matematyki.'''),
    dict(id='pka', grupa='nagrody', rok=None, kolejnosc=20, istniejacy=True,
         tytul='Wyróżniająca ocena PKA dla kierunku matematyka',
         zajawka='Kierunek matematyka ma od kilkunastu lat ocenę wyróżniającą Polskiej Komisji Akredytacyjnej i jej Certyfikat Jakości Kształcenia.',
         obraz='pka', obraz_opis='Certyfikat Jakości Kształcenia Polskiej Komisji Akredytacyjnej dla kierunku matematyka, 6 grudnia 2018 r.',
         tresc='''Prezydium **Polskiej Komisji Akredytacyjnej**, po dokonaniu oceny programowej kierunku **matematyka** prowadzonego na Wydziale Matematyki i Informatyki Uniwersytetu Wrocławskiego na poziomie studiów pierwszego i drugiego stopnia o profilu ogólnoakademickim, uchwałą nr 744/2018 z 6 grudnia 2018 r. przyznało kierunkowi ocenę **wyróżniającą**. Potwierdza to Certyfikat Jakości Kształcenia PKA.

Kierunek matematyka otrzymał ocenę wyróżniającą już wcześniej: uchwałą nr 280/2010 z 25 marca 2010 r. Prezydium Państwowej Komisji Akredytacyjnej uznało, że kształcenie na kierunku matematyka na Wydziale Matematyki i Informatyki UWr (studia pierwszego i drugiego stopnia oraz jednolite studia magisterskie) zasługuje na ocenę wyróżniającą.'''),
    dict(id='nagroda-ptm-steinhausa', grupa='nagrody', rok=None, kolejnosc=50,
         tytul='Nagroda Główna PTM im. Hugona Steinhausa',
         zajawka='Nagroda Polskiego Towarzystwa Matematycznego za całokształt dorobku w dziedzinie zastosowań matematyki. Otrzymała ją prof. Małgorzata Bogdan.',
         obraz='bogdan', obraz_opis='Prof. Małgorzata Bogdan',
         lista_tytul='Laureaci z Instytutu',
         laureaci=[(2021, 'prof. Małgorzata Bogdan (za rok 2020)', '2021-03-19-nagroda-ptm-im-steinhausa-dla-prof-malgorzaty-bogdan', '2021-03-19', None)],
         tresc='''**Nagrodę Główną Polskiego Towarzystwa Matematycznego im. Hugona Steinhausa** PTM przyznaje za całokształt dorobku w dziedzinie zastosowań matematyki.

Za rok 2020 otrzymała ją prof. **Małgorzata Bogdan** z naszego Instytutu.'''),
    dict(id='kategoria-a-plus', grupa='nagrody', rok=None, kolejnosc=10,
         tytul='Kategoria A+ dla matematyki',
         zajawka='Dyscyplina matematyka na Uniwersytecie Wrocławskim ma najwyższą kategorię naukową A+ — otrzymała ją w dwóch kolejnych ewaluacjach.',
         obraz='aplus', obraz_opis='Decyzja Ministra Nauki i Szkolnictwa Wyższego z 31 lipca 2026 r.',
         tresc='''Kategoria naukowa to ocena, którą ministerstwo co kilka lat wystawia każdej dyscyplinie na każdej uczelni; **A+** jest najwyższa.

Dyscyplina **matematyka** na Uniwersytecie Wrocławskim otrzymała ją w dwóch kolejnych ewaluacjach:

- za lata **2017–2021** — po uwzględnieniu odwołania ([aktualność](/aktualnosci/2023-02-15-matematyka-na-a-plus)),
- za lata **2022–2025** — decyzją Ministra Nauki i Szkolnictwa Wyższego z 31 lipca 2026 r. ([aktualność](/aktualnosci/2026-08-03-kategoria-naukowa-a-plus)).'''),
    dict(id='medal-sierpinskiego', grupa='nagrody', rok=None, kolejnosc=40,
         tytul='Medal im. Wacława Sierpińskiego',
         zajawka='Jedno z najważniejszych wyróżnień matematycznych w Polsce, przyznawane od 1974 roku przez UW i PTM. Otrzymał je prof. Tadeusz Januszkiewicz.',
         obraz='sierpinski', obraz_opis='Prof. Tadeusz Januszkiewicz',
         lista_tytul='Laureaci z Instytutu',
         laureaci=[(2026, 'prof. Tadeusz Januszkiewicz', '2026-05-29-medal-sierpinskiego-dla-prof-tadeusza-januszkiewicza', '2026-05-29', None)],
         tresc='''**Medal im. Wacława Sierpińskiego** jest przyznawany od 1974 roku przez Uniwersytet Warszawski oraz Polskie Towarzystwo Matematyczne i należy do najważniejszych i najbardziej prestiżowych wyróżnień matematycznych w kraju. W 2026 roku otrzymał go prof. **Tadeusz Januszkiewicz**.'''),
    dict(id='medal-uniwersytetu', grupa='nagrody', rok=None, kolejnosc=30, istniejacy=True,
         tytul='Medal Uniwersytetu Wrocławskiego',
         zajawka='Medal przyznawany przez Senat w uznaniu szczególnych zasług dla Uniwersytetu. Otrzymali go profesorowie Marek Bożejko i Tomasz Rolski.',
         obraz='ceremonia', obraz_opis='Uroczystość wręczenia Medalu Uniwersytetu, 13 listopada 2026 r.',
         dodano='2026-11-13',
         lista_tytul='Laureaci z Instytutu',
         laureaci=[
             (2026, 'prof. Marek Bożejko', '2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego', '2026-11-13', 'marek-bozejko'),
             (2026, 'prof. Tomasz Rolski', '2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego', '2026-11-13', 'tomasz-rolski'),
         ],
         tresc='''**Medal Uniwersytetu Wrocławskiego** przyznaje Senat Uczelni w uznaniu szczególnych zasług dla Uniwersytetu.

Podczas uroczystych obchodów Święta Uniwersytetu Wrocławskiego 13 listopada 2026 r. medale otrzymali dwaj wybitni matematycy, profesorowie **Marek Bożejko** i **Tomasz Rolski** — w uznaniu ich osiągnięć naukowych, wieloletniej działalności akademickiej i wkładu w rozwój i międzynarodową renomę wrocławskiego ośrodka matematycznego.

- [Nota biograficzna profesora Marka Bożejki](https://im-uwr.github.io/Web-Podglad/pliki/aktualnosci/marekbozejkonotabiograficzna.pdf)
- [Nota biograficzna profesora Tomasza Rolskiego](https://im-uwr.github.io/Web-Podglad/pliki/aktualnosci/tomaszrolskinotabiograficzna.pdf)'''),

]

# ======================================================================== Sylwetki
# typ='osoba': portret (zdjęcie / szkic patrona / monogram), linijka pod nazwiskiem, „W skrócie”, oś życia
# (lista numerowana z pogrubionym początkiem = oś kroków, jak w parserze strony), sekcje treści.
# Założyciele: opis z banera działu, sala, ciekawostki z src/data/ciekawostki/<dział>.json (Web-Core).
# Bożejko i Rolski: noty biograficzne (PDF) z aktualności z 13.11.2026.

ZALOZYCIELE = [
    dict(id='wladyslaw-slebodzinski', tytul='Władysław Ślebodziński', lata='1884–1972', ur=1884, dzial='nauka', dzial_nazwa='Nauka', sala='WS',
         podpis='Geometra różniczkowy, twórca pochodnej Liego',
         zajawka='Geometra różniczkowy. W 1931 roku wprowadził pochodną Liego, dziś jedno z podstawowych narzędzi geometrii.',
         skrot_extra=[('1931', 'pochodna Liego')],
         tresc_extra=''),
    dict(id='hugo-steinhaus', tytul='Hugo Steinhaus', lata='1887–1972', ur=1887, dzial='popularyzacja', dzial_nazwa='Popularyzacja', sala='HS',
         podpis='Współtwórca szkoły lwowskiej i wrocławskiej',
         zajawka='Współtwórca szkoły lwowskiej i wrocławskiej, mistrz matematycznego aforyzmu i popularyzacji. „Między duchem a materią pośredniczy matematyka”.',
         skrot_extra=[('1946', 'pierwsze zagadnienie w Nowej Księdze Szkockiej')],
         tresc_extra='W 1946 roku wpisał pierwsze zagadnienie do [Nowej Księgi Szkockiej](w-nowa-ksiega-szkocka.html). Na jego seminarium zastosowań powstała [taksonomia wrocławska](w-taksonomia-wroclawska.html), a z Janem Mycielskim zaproponował [aksjomat determinacji](w-aksjomat-determinacji.html).'),
    dict(id='bronislaw-knaster', tytul='Bronisław Knaster', lata='1893–1980', ur=1893, dzial='studia', dzial_nazwa='Studia', sala='B',
         podpis='Topolog, który wychował pokolenia matematyków',
         zajawka='Topolog, autor twierdzenia Knastera–Tarskiego o punkcie stałym. Wychował pokolenia wrocławskich matematyków.',
         skrot_extra=[('Sala B', 'sala wykładowa jego imienia')],
         tresc_extra='Sala wykładowa **B** w gmachu Instytutu nosi imię Bronisława Knastera.'),
    dict(id='edward-marczewski', tytul='Edward Marczewski', lata='1907–1976', ur=1907, dzial='instytut', dzial_nazwa='Instytut', sala='EM',
         podpis='Pierwszy dyrektor Instytutu, rektor Uniwersytetu',
         zajawka='Współtwórca wrocławskiej matematyki, pierwszy dyrektor Instytutu i rektor Uniwersytetu w latach 1953–1957. Zabiegał o budowę gmachu Instytutu.',
         skrot_extra=[('1953–1957', 'rektor Uniwersytetu Wrocławskiego')],
         tresc_extra='''Był rektorem Uniwersytetu w latach 1953–1957 — pierwszym z [trzech rektorów-matematyków](w-trzech-rektorow.html).

Gmach Instytutu przy placu Grunwaldzkim 2 powstał m.in. dzięki jego staraniom — w miejscu, gdzie pod koniec wojny on sam jako robotnik przymusowy budował pas startowy dla oblężonej Festung Breslau. Instytut mieści się w nim od końca lat sześćdziesiątych.'''),
]

for z in ZALOZYCIELE:
    WPISY.append(dict(id=z['id'], grupa='sylwetki', typ='osoba', zalozyciel=True, rok=1945, sort=z['ur'],
                      tytul=z['tytul'], lata=z['lata'], podpis=z['podpis'], zajawka=z['zajawka'], szkic=z['dzial'],
                      dzial=z['dzial'], dzial_nazwa=z['dzial_nazwa'], sala=z['sala'], skrot_extra=z['skrot_extra'],
                      tresc=z['tresc_extra'], stan='ulubiona'))

WPISY.append(dict(
    id='marek-bozejko', grupa='sylwetki', typ='osoba', rok=1969, sort=1946,
    tytul='Marek Bożejko', lata='ur. 1946', portret='bozejko',
    podpis='Twórca wrocławskiej szkoły nieprzemiennej analizy harmonicznej',
    zajawka='Twórca wrocławskiej szkoły nieprzemiennej analizy harmonicznej i probabilistyki nieprzemiennej, współautor teorii q-zdeformowanej przestrzeni Focka.',
    dodano='2026-11-18', rocznica='09-09', rocznica_rok=1946, rocznica_typ='urodziny',
    pracownik='http://www.math.uni.wroc.pl/~bozejko/', zaklad='Zakład Analizy Matematycznej',
    nota='https://im-uwr.github.io/Web-Podglad/pliki/aktualnosci/marekbozejkonotabiograficzna.pdf',
    skrot=[('1973', 'doktorat w IM PAN'), ('72', 'publikacje naukowe'), ('1800+', 'cytowań'), ('9', 'wypromowanych doktorów')],
    os=[
        ('1946', 'urodził się w Bielawie', '9 września.'),
        ('1969', 'absolwent Uniwersytetu Wrocławskiego', 'Studia matematyczne.'),
        ('1973', 'doktorat w IM PAN', 'Rozprawa „Zbiory Sidona w nieprzemiennej analizie harmonicznej”, promotor prof. Stanisław Hartman.'),
        ('1980', 'habilitacja', ''),
        ('1984', 'twierdzenie Bożejki–Fendlera', 'Z Gero Fendlerem; w tym samym roku Nagroda Główna PTM im. Stefana Banacha.'),
        ('1991', 'przestrzeń Focka z Rolandem Speicherem', 'Artykuł w Communications in Mathematical Physics; profesor zwyczajny.'),
        ('2000', 'Międzynarodowa Nagroda Humboldta', 'Współpraca z Michaelem Leinertem w Heidelbergu.'),
        ('2011', 'rozkład normalny ⊞-nieskończenie podzielny', 'Advances in Mathematics, z Belinschim, Lehnerem i Speicherem.'),
        ('2012', 'Nagroda Ministra Nauki', 'Za całokształt dorobku naukowego.'),
        ('2026', 'Medal Uniwersytetu Wrocławskiego', '13 listopada, podczas Święta Uniwersytetu.'),
    ],
    tresc='''## Najważniejsze osiągnięcia

**Nieprzemienna analiza harmoniczna.** Już w pracy doktorskiej przeniósł ważne własności zbiorów Sidona z grup przemiennych na nieprzemienne, a w badaniach nad zbiorami Λ(p) uzyskał optymalne stałe w nierównościach operatorowych.

**Twierdzenie Bożejki–Fendlera** (1984, z Gero Fendlerem): równoważność mnożników Herza–Schura i całkowicie ograniczonych mnożników algebry Fouriera grupy lokalnie zwartej — dziś klasyczny wynik analizy harmonicznej i teorii operatorów.

**Przestrzenie Focka i procesy q-Gaussowskie.** Najbardziej znane odkrycie, wspólne z Rolandem Speicherem (1991): model interpolujący między statystyką bozonową i fermionową, który zapoczątkował badania nad q-Gaussowskimi algebrami von Neumanna.

**Wolna probabilistyka.** Z Michaelem Leinertem i Rolandem Speicherem rozwinął teorię warunkowo wolnej niezależności (1996), a w 2011 roku — z Belinschim, Lehnerem i Speicherem — wykazał, że rozkład Gaussa jest nieskończenie podzielny także względem wolnego splotu.

## Szkoła i uczniowie

Od początku lat dziewięćdziesiątych prowadzi we Wrocławiu seminarium z dyskretnej analizy harmonicznej i probabilistyki nieprzemiennej. Wypromował dziewięciu doktorów, z których trzech jest już profesorami; z jego kierunkami badań związani są m.in. Wojciech Młotkowski, Ryszard Szwarc, Janusz Wysoczański, Anna Wysoczańska-Kula i Wiktor Ejsmont.

Zainicjował cykl międzynarodowych konferencji *Workshop: Noncommutative Harmonic Analysis*; dwudziesta edycja odbyła się w 2025 roku w Będlewie.'''))

WPISY.append(dict(
    id='tomasz-rolski', grupa='sylwetki', typ='osoba', rok=1969, sort=1947,
    tytul='Tomasz Rolski', lata='dyrektor Instytutu 1996–2002', portret=None, monogram='TR',
    podpis='Probabilista: teoria kolejek, ryzyka i matematyka ubezpieczeniowa',
    zajawka='Jeden z najwybitniejszych polskich specjalistów od procesów stochastycznych; twórca wrocławskiej grupy probabilistyki stosowanej i dyrektor Instytutu w latach 1996–2002.',
    dodano='2026-11-18',
    pracownik='http://www.math.uni.wroc.pl/~rolski/', zaklad='Zakład Teorii Prawdopodobieństwa',
    nota='https://im-uwr.github.io/Web-Podglad/pliki/aktualnosci/tomaszrolskinotabiograficzna.pdf',
    skrot=[('ok. 90', 'prac naukowych i 3 książki'), ('5000+', 'cytowań (Google Scholar)'), ('8', 'wypromowanych doktorów'), ('1996–2002', 'dyrektor Instytutu')],
    os=[
        ('1969', 'absolwent Uniwersytetu Wrocławskiego', 'Studia matematyczne.'),
        ('1973', 'doktorat', ''),
        ('1976–1977', 'Uniwersytet Oksfordzki', 'Pierwszy z wielu zagranicznych pobytów badawczych.'),
        ('1981', 'hipoteza Rossa', '„Queues with non-stationary input stream: Ross’s conjecture”, Advances in Applied Probability.'),
        ('1983', 'habilitacja', ''),
        ('1992', 'tytuł profesora', ''),
        ('1996–2002', 'dyrektor Instytutu Matematycznego', 'Reforma studiów i nowe specjalności.'),
        ('1999', 'Stochastic Processes for Insurance and Finance', 'Wiley, z Schmidlim, Schmidtem i Teugelsem.'),
        ('2005–2008', 'dziekan Wydziału Matematyki i Informatyki', ''),
        ('2025', 'Lectures on Monte Carlo Theory', 'Springer, z Pawłem Lorkiem.'),
        ('2026', 'Medal Uniwersytetu Wrocławskiego', '13 listopada, podczas Święta Uniwersytetu.'),
    ],
    tresc='''## Najważniejsze osiągnięcia

**Hipoteza Rossa.** Czy bardziej zmienny napływ zgłoszeń przy tym samym średnim natężeniu pogarsza obsługę w systemie kolejkowym? W 1981 roku uzyskał zasadniczy wynik porównawczy dla systemów z niestacjonarnym napływem, a w kolejnych pracach (z Nicole Bäuerle i Naoto Miyoshim) rozstrzygnął dalsze postacie hipotezy.

**Modele fluidowe.** Metody opisu przepływu danych i przeciążeń w sieciach teleinformatycznych: asymptotyki rzadkich zdarzeń przez zmianę miary, teorię dużych odchyleń i teorię ekstremów — m.in. z Zbigniewem Palmowskim, Krzysztofem Dębickim i Tonem Diekerem.

**Teoria ryzyka i matematyka ubezpieczeniowa.** Modele ruiny, rezerw i ryzyka w zmiennym otoczeniu, także we współpracy z Sørenem Asmussenem. Monografia *Stochastic Processes for Insurance and Finance* (1999) jest klasycznym opracowaniem tej dziedziny.

## Szkoła i uczniowie

Stworzył we Wrocławiu silną grupę probabilistyki stosowanej. Wypromował ośmioro doktorów: Jacka Leśkowa, Ryszarda Szekliego, Bartłomieja Błaszczyszyna, Zbigniewa Palmowskiego, Krzysztofa Dębickiego, Zbigniewa Puchałę, Sandipa Godbolego i Agatę Ilnicką.

## Dyrektor i reformator

Jako dyrektor Instytutu (1996–2002) współtworzył reformę studiów matematycznych: nowe specjalności — matematyka w ekonomii i ubezpieczeniach, matematyka z informatyką, biomatematyka — i indywidualne ścieżki kształcenia. Liczba studentów matematyki na Uniwersytecie wzrosła ponad dwukrotnie. Był też zastępcą dyrektora (1988–1991), członkiem Senatu (2002–2005) i dziekanem Wydziału Matematyki i Informatyki (2005–2008).'''))

# ======================================================================== Sylwetki z plików Markdown (18.11, 14:00)
# Teksty prozą w stylu not Grzegorza: /home/claude/sylwetki/<id>.md (frontmatter + :::w-skrocie + sekcje ##).
# Jeśli plik istnieje, zastępuje wpis osoby powyżej (założyciele: zamiast „Życia w ciekawostkach”).
import os as _os, re as _re
SYLW_DIR = '/home/claude/sylwetki'
OSOBY = [
    # id, sortowanie (rok urodzenia), portret: ('szkic', dział) / ('foto', plik) / None = monogram
    ('wladyslaw-slebodzinski', 1884, ('szkic', 'nauka')),
    ('hugo-steinhaus', 1887, ('szkic', 'popularyzacja')),
    ('bronislaw-knaster', 1893, ('szkic', 'studia')),
    ('witold-wolibner', 1902, None),
    ('edward-marczewski', 1907, ('szkic', 'instytut')),
    ('julian-perkal', 1913, None),
    ('stanislaw-hartman', 1914, None),
    ('czeslaw-ryll-nardzewski', 1926, None),
    ('kazimierz-urbanik', 1930, None),
    ('jan-mycielski', 1932, None),
    ('andrzej-hulanicki', 1933, None),
    ('andrzej-krzywicki', 1928, None),
    ('roman-duda', 1935, None),
    ('wladyslaw-narkiewicz', 1936, None),
    ('marek-bozejko', 1946, ('foto', 'bozejko')),
    ('tomasz-rolski', 1947, None),
    ('piotr-biler', 1958, None),
    ('krzysztof-tabisz', 1955, None),
]
# sylwetki bez pliku: nazwa i lata do karty „TBA” (do czasu, aż redakcja wpisze tekst w CMS)
NAZWY_TBA = {'piotr-biler': ('Piotr Biler', ''), 'krzysztof-tabisz': ('Krzysztof Tabisz', '')}

def _wczytaj(id_):
    p = _os.path.join(SYLW_DIR, id_ + '.md')
    if not _os.path.isfile(p):
        return None
    t = open(p, encoding='utf-8').read()
    m = _re.match(r'---\n(.*?)\n---\n', t, _re.S)
    front = {}
    for l in m.group(1).split('\n'):
        k, _, v = l.partition(':')
        v = v.split('#')[0].strip() if not v.strip().startswith('"') else v.strip()
        front[k.strip()] = v.strip().strip('"')
    body = t[m.end():]
    skrot = []
    sm = _re.search(r'(?:<!--[^>]*-->\s*)?:::w-skrocie\s*\n(.*?)\n:::\s*\n', body, _re.S)
    if sm:
        for l in sm.group(1).split('\n'):
            x = _re.match(r'\s*-\s*\*\*(.+?)\*\*\s*[—–-]\s*(.+)', l)
            if x:
                skrot.append((x.group(1).strip(), x.group(2).strip()))
        body = body[:sm.start()] + body[sm.end():]
    return front, skrot, body.strip()

def _inicjaly(t):
    cz = [c for c in _re.split(r'[\s-]+', t) if c]
    return (cz[0][0] + cz[-1][0]).upper()

_po_id = {w['id']: w for w in WPISY}
for _id, _ur, _por in OSOBY:
    r = _wczytaj(_id)
    if not r:
        if _id not in NAZWY_TBA:
            continue
        _n, _l = NAZWY_TBA[_id]
        r = ({'tytul': _n, 'lata': _l, 'podpis': '', 'zajawka': ''}, [], '')
    front, skrot, body = r
    stary = _po_id.get(_id, {})
    w = dict(id=_id, grupa='sylwetki', typ='osoba', md=True, rok=None, sort=_ur,
             tytul=front.get('tytul', ''), lata=front.get('lata', ''), podpis=front.get('podpis', ''),
             zajawka=front.get('zajawka', ''), skrot=skrot, tresc_md=body,
             stan=stary.get('stan'), dodano=front.get('dodano') or stary.get('dodano'))
    # zasada z 18.11 (14:22): mało informacji = TBA; w CMS to po prostu pusta „Treść” sylwetki
    _proza = _re.split(r'(?m)^## Źródła', body)[0].strip()
    if not _proza or front.get('tba', '').lower() in ('true', 'tak'):
        w.update(tba=True, podpis=w['podpis'] or 'Sylwetka w przygotowaniu', zajawka=w['zajawka'] or 'TBA — sylwetka w przygotowaniu.')
    if front.get('rocznica_urodzin'):
        w.update(rocznica=front['rocznica_urodzin'], rocznica_rok=_ur, rocznica_typ='urodziny')
    if _por and _por[0] == 'szkic':
        w.update(szkic=_por[1], dzial=_por[1], zalozyciel=True)
    elif _por and _por[0] == 'foto':
        w.update(portret=_por[1])
    else:
        w.update(monogram=_inicjaly(w['tytul']))
    if _id in _po_id:
        WPISY[WPISY.index(_po_id[_id])] = w
    else:
        WPISY.append(w)


# 18.11 (18:20): Historia + Odkrycia i publikacje = jedna grupa „Historie” (oś czasu na liście)
for _w in WPISY:
    if _w['grupa'] in ('historia', 'odkrycia'):
        _w['grupa'] = 'historie'
