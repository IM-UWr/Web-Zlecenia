#!/usr/bin/env python3
# Zlecenie 54 — zmiany w Treści „Warto wiedzieć” (Web-Instytut). Uruchom z katalogu repozytorium Web-Instytut:
#   python zlecenie54.py --sprawdz   (tylko kontrola, nic nie zapisuje)
#   python zlecenie54.py             (zapis w miejscu)
# Każde "bylo" musi wystąpić w pliku dokładnie raz; inaczej STOP bez zapisu czegokolwiek.
import re, sys, os, glob
KAT = os.path.join('src', 'content', 'warto_wiedziec')
ZAMIANY = [
    ("A01", "sylwetki/andrzej-hulanicki.md",
     "Andrzej Hulanicki należał do najbardziej cenionych",
     "Prof. Andrzej Hulanicki należał do najbardziej cenionych"),
    ("A02", "sylwetki/andrzej-krzywicki.md",
     "Prof. dr hab. Andrzej Krzywicki należy",
     "Prof. Andrzej Krzywicki należy"),
    ("A03", "sylwetki/bronislaw-knaster.md",
     "Bronisław Knaster był jednym z czterech profesorów",
     "Prof. Bronisław Knaster był jednym z czterech profesorów"),
    ("A04", "sylwetki/czeslaw-ryll-nardzewski.md",
     "Czesław Ryll-Nardzewski był jednym z najbardziej wszechstronnych",
     "Prof. Czesław Ryll-Nardzewski był jednym z najbardziej wszechstronnych"),
    ("A05", "sylwetki/edward-marczewski.md",
     "Edward Marczewski należał do czwórki",
     "Prof. Edward Marczewski należał do czwórki"),
    ("A06", "sylwetki/hugo-steinhaus.md",
     "Hugo Steinhaus należy do najważniejszych",
     "Prof. Hugo Steinhaus należy do najważniejszych"),
    ("A07", "sylwetki/jan-mycielski.md",
     "Jan Mycielski jest jednym z tych wychowanków",
     "Prof. Jan Mycielski jest jednym z tych wychowanków"),
    ("A08", "sylwetki/julian-perkal.md",
     "Julian Perkal należał do pokolenia",
     "Prof. Julian Perkal należał do pokolenia"),
    ("A09", "sylwetki/kazimierz-urbanik.md",
     "Kazimierz Urbanik należał do pokolenia",
     "Prof. Kazimierz Urbanik należał do pokolenia"),
    ("A10", "sylwetki/piotr-biler.md",
     "Piotr Biler jest matematykiem Instytutu",
     "Prof. Piotr Biler jest matematykiem Instytutu"),
    ("A11", "sylwetki/roman-duda.md",
     "Profesor Roman Duda łączy",
     "Prof. Roman Duda łączy"),
    ("A12", "sylwetki/stanislaw-hartman.md",
     "Stanisław Hartman należał do grona",
     "Prof. Stanisław Hartman należał do grona"),
    ("A13", "sylwetki/witold-wolibner.md",
     "Witold Wolibner należał do pierwszego pokolenia",
     "Prof. Witold Wolibner należał do pierwszego pokolenia"),
    ("A14", "sylwetki/wladyslaw-narkiewicz.md",
     "Prof. dr hab. Władysław Narkiewicz jest",
     "Prof. Władysław Narkiewicz jest"),
    ("A15", "sylwetki/wladyslaw-slebodzinski.md",
     "Władysław Ślebodziński był geometrą",
     "Prof. Władysław Ślebodziński był geometrą"),
    ("A16", "sylwetki/stanislaw-hartman.md",
     "prof. Jurek przekazał",
     "Jurek przekazał"),
    ("T01", "sylwetki/krzysztof-tabisz.md",
     "**Dr Krzysztof Tabisz (ur. 1950)** – matematyk, wieloletni nauczyciel akademicki Uniwersytetu Wrocławskiego, działacz społeczny i opozycyjny, zasłużony organizator życia akademickiego.",
     "Dr Krzysztof Tabisz jest matematykiem, wieloletnim nauczycielem akademickim Uniwersytetu Wrocławskiego, działaczem społecznym i opozycyjnym oraz zasłużonym organizatorem życia akademickiego."),
    ("T02", "sylwetki/krzysztof-tabisz.md",
     "pod kierunkiem prof. Andrzeja Krzywickiego",
     "pod kierunkiem [Andrzeja Krzywickiego](/instytut/warto-wiedziec/andrzej-krzywicki)"),
    ("T03", "sylwetki/krzysztof-tabisz.md",
     "biografii dr. Krzysztofa Tabisza",
     "biografii Krzysztofa Tabisza"),
    ("T04", "sylwetki/krzysztof-tabisz.md",
     "obywatelską dr Krzysztof Tabisz otrzymał",
     "obywatelską Krzysztof Tabisz otrzymał"),
    ("T05", "sylwetki/krzysztof-tabisz.md",
     "Wrocławskim, dr Krzysztof Tabisz zabrał",
     "Wrocławskim, Krzysztof Tabisz zabrał"),
    ("T06", "sylwetki/krzysztof-tabisz.md",
     "**Dr Krzysztof Tabisz (born in 1950)** is a mathematician",
     "Dr Krzysztof Tabisz is a mathematician"),
    ("T07", "sylwetki/krzysztof-tabisz.md",
     "  Dr Krzysztof Tabisz began working",
     "  Krzysztof Tabisz began working"),
    ("T08", "sylwetki/krzysztof-tabisz.md",
     "supervised by Professor Andrzej Krzywicki.",
     "supervised by Andrzej Krzywicki."),
    ("T09", "sylwetki/krzysztof-tabisz.md",
     "part of Dr Krzysztof Tabisz's biography",
     "part of Krzysztof Tabisz's biography"),
    ("T10", "sylwetki/krzysztof-tabisz.md",
     "contributions, Dr Krzysztof\n",
     "contributions, Krzysztof\n"),
    ("T11", "sylwetki/krzysztof-tabisz.md",
     "  Dr Krzysztof Tabisz spoke on behalf",
     "  Krzysztof Tabisz spoke on behalf"),
    ("T12", "sylwetki/krzysztof-tabisz.md",
     "  zajawka: Dr Krzysztof Tabisz – matematyk, wieloletni",
     "  zajawka: Matematyk, wieloletni"),
    ("T13", "sylwetki/krzysztof-tabisz.md",
     "  zajawka_en: Dr Krzysztof Tabisz is a mathematician, long-serving",
     "  zajawka_en: Mathematician, long-serving"),
    ("B01", "sylwetki/marek-bozejko.md",
     "Prof. dr hab. Marek Bożejko należy",
     "Prof. Marek Bożejko należy"),
    ("B02", "sylwetki/marek-bozejko.md",
     "[prof. Stanisława Hartmana](/instytut/warto-wiedziec/stanislaw-hartman); recenzentami byli [prof. Andrzej Hulanicki](/instytut/warto-wiedziec/andrzej-hulanicki) i [prof. Czesław Ryll-Nardzewski](/instytut/warto-wiedziec/czeslaw-ryll-nardzewski)",
     "[Stanisława Hartmana](/instytut/warto-wiedziec/stanislaw-hartman); recenzentami byli [Andrzej Hulanicki](/instytut/warto-wiedziec/andrzej-hulanicki) i [Czesław Ryll-Nardzewski](/instytut/warto-wiedziec/czeslaw-ryll-nardzewski)"),
    ("B03", "sylwetki/marek-bozejko.md",
     "Prace Profesora uzyskały",
     "Jego prace uzyskały"),
    ("B04", "sylwetki/marek-bozejko.md",
     "Już w pracy doktorskiej Profesor rozszerzył",
     "Już w pracy doktorskiej Bożejko rozszerzył"),
    ("B05", "sylwetki/marek-bozejko.md",
     "jest artykuł *On Λ(p) Sets with Minimal Constant in Discrete Noncommutative Groups* (1975)",
     "jest artykuł [*On Λ(p) Sets with Minimal Constant in Discrete Noncommutative Groups*](https://www.ams.org/journals/proc/1975-051-02/S0002-9939-1975-0390658-3) (1975)"),
    ("B06", "sylwetki/marek-bozejko.md",
     "Już na tym etapie badań Profesor wykazał",
     "Już na tym etapie badań wykazał"),
    ("B07", "sylwetki/marek-bozejko.md",
     "Profesor prowadził następnie badania",
     "Bożejko prowadził następnie badania"),
    ("B08", "sylwetki/marek-bozejko.md",
     "W pracy *Positive Definite Bounded Matrices and a Characterization of Amenable Groups* (1985) Profesor podał ponadto",
     "W pracy [*Positive Definite Bounded Matrices and a Characterization of Amenable Groups*](https://www.ams.org/proc/1985-095-03/S0002-9939-1985-0806070-2/) (1985) podał ponadto"),
    ("B09", "sylwetki/marek-bozejko.md",
     "W fundamentalnym artykule *An Example of a Generalized Brownian Motion* (Communications",
     "W fundamentalnym artykule [*An Example of a Generalized Brownian Motion*](https://doi.org/10.1007/BF02100275) (Communications"),
    ("B10", "sylwetki/marek-bozejko.md",
     "dotyczących grup Coxetera, zdeformowanych relacji komutacji oraz interpolacji między strukturami bozonowymi i fermionowymi.",
     "dotyczących [grup Coxetera, zdeformowanych relacji komutacji](https://eudml.org/doc/165244) oraz [interpolacji między strukturami bozonowymi i fermionowymi](https://eudml.org/doc/174879)."),
    ("B11", "sylwetki/marek-bozejko.md",
     "Profesor wniósł ważny wkład",
     "Bożejko wniósł ważny wkład"),
    ("B12", "sylwetki/marek-bozejko.md",
     "w artykule *Convolution and Limit Theorems for Conditionally Free Random Variables* (1996)",
     "w artykule [*Convolution and Limit Theorems for Conditionally Free Random Variables*](https://msp.org/pjm/1996/175-2/p04.xhtml) (1996)"),
    ("B13", "sylwetki/marek-bozejko.md",
     "w pracy *Generalized q-Deformed Gaussian Random Variables* (2006)",
     "w pracy [*Generalized q-Deformed Gaussian Random Variables*](https://impan.pl/en/publishing-house/banach-center-publications/all/73/0/86545/generalized-q-deformed-gaussian-random-variables) (2006)"),
    ("B14", "sylwetki/marek-bozejko.md",
     "Rolandem Speicherem Profesor udowodnił",
     "Rolandem Speicherem Bożejko udowodnił"),
    ("B15", "sylwetki/marek-bozejko.md",
     "w artykule *The Normal Distribution Is ⊞-Infinitely Divisible* (Advances",
     "w artykule [*The Normal Distribution Is ⊞-Infinitely Divisible*](https://arxiv.org/abs/0910.4263) (Advances"),
    ("B16", "sylwetki/marek-bozejko.md",
     "badał wolną nieskończoną podzielność rozkładów Meixnera.",
     "badał [wolną nieskończoną podzielność rozkładów Meixnera](https://digilab.uwr.edu.pl/en/dlibra/publication/113063/on-free-infinite-divisibility-for-classical-meixner-distribution-bozejko-marek-hasebe-takahiro)."),
    ("B17", "sylwetki/marek-bozejko.md",
     "Profesor kontynuuje rozpoczęty",
     "Bożejko kontynuuje rozpoczęty"),
    ("B18", "sylwetki/marek-bozejko.md",
     "Przykładem jest praca *The Double Fock Space of Type B* (2023)",
     "Przykładem jest praca [*The Double Fock Space of Type B*](https://www.imath.kyiv.ua/~sigma/2023/040/) (2023)"),
    ("B19", "sylwetki/marek-bozejko.md",
     "Międzynarodową Nagrodę Humboldta (2000)",
     "Międzynarodową [Nagrodę Humboldta](https://www.humboldt-foundation.de/en/connect/explore-the-humboldt-network/singleview/1071941/prof-dr-marek-bozejko) (2000)"),
    ("B20", "sylwetki/marek-bozejko.md",
     "jest Medal Uniwersytetu Wrocławskiego, wręczony Profesorowi 13 listopada 2026 roku podczas",
     "jest [Medal Uniwersytetu Wrocławskiego](/instytut/warto-wiedziec/medal-uniwersytetu), [wręczony mu 13 listopada 2026 roku](/aktualnosci/2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego) podczas"),
    ("B21", "sylwetki/marek-bozejko.md",
     "O międzynarodowej pozycji Profesora świadczą",
     "O jego międzynarodowej pozycji świadczą"),
    ("B22", "sylwetki/marek-bozejko.md",
     "prowadzi we Wrocławiu seminarium poświęcone dyskretnej analizie harmonicznej i probabilistyce nieprzemiennej.",
     "prowadzi we Wrocławiu [seminarium poświęcone dyskretnej analizie harmonicznej i probabilistyce nieprzemiennej](/seminaria/dyskretna-analiza-harmoniczna)."),
    ("B23", "sylwetki/marek-bozejko.md",
     "Profesor jest również inicjatorem i głównym organizatorem cyklu międzynarodowych konferencji *Workshop: Noncommutative Harmonic Analysis*.",
     "Bożejko jest również inicjatorem i głównym organizatorem cyklu międzynarodowych konferencji [*Workshop: Noncommutative Harmonic Analysis*](https://math.uni.wroc.pl/analiza/workshops.html)."),
    ("B24", "sylwetki/marek-bozejko.md",
     "pod nazwą *Noncommutative Probability, Operator Algebras and Related Topics, with Applications*, odbyła",
     "pod nazwą [*Noncommutative Probability, Operator Algebras and Related Topics, with Applications*](https://sites.google.com/impan.pl/20thworkshop), odbyła"),
    ("B25", "sylwetki/marek-bozejko.md",
     "Profesor kierował sześcioma",
     "Bożejko kierował sześcioma"),
    ("B26", "sylwetki/marek-bozejko.md",
     "w europejskim projekcie Transfer of Knowledge.",
     "w europejskim projekcie [Transfer of Knowledge](https://cordis.europa.eu/project/id/13389/reporting)."),
    ("B27", "sylwetki/marek-bozejko.md",
     "redaktorem pomocniczym Probability and Mathematical Statistics.",
     "redaktorem pomocniczym [Probability and Mathematical Statistics](https://www.math.uni.wroc.pl/~pms/)."),
    ("B28", "sylwetki/marek-bozejko.md",
     "Redagował pięć tomów konferencyjnych serii Banach Center Publications.",
     "Redagował pięć tomów konferencyjnych serii Banach Center Publications ([43](https://digilab.uwr.edu.pl/en/dlibra/publication/115345/quantum-probability), [73](https://www.impan.pl/en/publishing-house/banach-center-publications/all/73), [78](https://www.impan.pl/en/publishing-house/banach-center-publications/all/78), [89](https://www.impan.pl/en/publishing-house/banach-center-publications/all/89), [96](https://www.impan.pl/en/publishing-house/banach-center-publications/all/96))."),
    ("B29", "sylwetki/marek-bozejko.md",
     "Wrocławskiego Profesor stworzył rozpoznawalną",
     "Wrocławskiego Bożejko stworzył rozpoznawalną"),
    ("B30", "sylwetki/marek-bozejko.md",
     "Wypromował dziewięciu doktorów",
     "Wypromował [dziewięciu doktorów](https://mathgenealogy.org/id.php?id=123351)"),
    ("B31", "sylwetki/marek-bozejko.md",
     "szeroka perspektywa: Profesor przedstawia",
     "szeroka perspektywa: Bożejko przedstawia"),
    ("B32", "sylwetki/marek-bozejko.md",
     "Profesor inspiruje studentów",
     "Inspiruje studentów"),
    ("B33", "sylwetki/marek-bozejko.md",
     "Osiemdziesiąte urodziny prof. Marka Bożejki",
     "Osiemdziesiąte urodziny Marka Bożejki"),
    ("R01", "sylwetki/tomasz-rolski.md",
     "lata: \"xxxx\"",
     "lata: \"ur. 1946\""),
    ("R02", "sylwetki/tomasz-rolski.md",
     "Profesor dr hab. Tomasz Rolski jest",
     "Prof. Tomasz Rolski jest"),
    ("R03", "sylwetki/tomasz-rolski.md",
     "Dorobek profesora Rolskiego uzyskał",
     "Jego dorobek uzyskał"),
    ("R04", "sylwetki/tomasz-rolski.md",
     "wyników profesora Rolskiego należą",
     "wyników Rolskiego należą"),
    ("R05", "sylwetki/tomasz-rolski.md",
     "W artykule *Queues with non-stationary input stream: Ross’s conjecture* (Advances",
     "W artykule [*Queues with non-stationary input stream: Ross’s conjecture*](https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/queues-with-nonstationary-input-stream-rosss-conjecture/4218BA71795B7AD9A6C213C9074364FC) (Advances"),
    ("R06", "sylwetki/tomasz-rolski.md",
     "praca *A monotonicity result for the work-load in Markov-modulated queues* (Journal",
     "praca [*A monotonicity result for the workload in Markov-modulated queues*](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/monotonicity-result-for-the-workload-in-markovmodulated-queues/A5C06FA9AF5A54AFA5D0C9E8A36643B6) (Journal"),
    ("R07", "sylwetki/tomasz-rolski.md",
     "z Naoto Miyoshim, *Ross type conjectures on monotonicity of queues* (2004)",
     "z Naoto Miyoshim, [*Ross-type conjectures on monotonicity of queues*](https://iaorifors.com/paper/47199) (Australian & New Zealand Journal of Statistics, 2004)"),
    ("R08", "sylwetki/tomasz-rolski.md",
     "Hipoteza Rossa, sformułowana w 1978 r.,",
     "Hipoteza Rossa, [sformułowana w 1978 r.](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/average-delay-in-queues-with-nonstationary-poisson-arrivals/267BF6FF86F585CF37F1790EF43544B2),"),
    ("R09", "sylwetki/tomasz-rolski.md",
     "W pracy z 1981 r. profesor Rolski wykazał",
     "W pracy z 1981 r. Rolski wykazał"),
    ("R10", "sylwetki/tomasz-rolski.md",
     "Profesor Rolski rozwijał metody",
     "Rolski rozwijał metody"),
    ("R11", "sylwetki/tomasz-rolski.md",
     "prace *A technique for exponential change of measure for Markov processes* (ze",
     "prace [*A technique for exponential change of measure for Markov processes*](https://digilab.uwr.edu.pl/dlibra/publication/116593/a-technique-for-exponential-change-of-measure-for-markov-processes-palmowski-zbigniew-rolski-tomasz) (ze"),
    ("R12", "sylwetki/tomasz-rolski.md",
     "oraz *Quasi-product forms for Lévy-driven fluid networks* (z",
     "oraz [*Quasi-product forms for Lévy-driven fluid networks*](https://pubsonline.informs.org/doi/abs/10.1287/moor.1070.0259) (z"),
    ("R13", "sylwetki/tomasz-rolski.md",
     "współpracownikami profesora Rolskiego w tej",
     "współpracownikami Rolskiego w tej"),
    ("R14", "sylwetki/tomasz-rolski.md",
     "Zainteresowania profesora Rolskiego obejmują",
     "Zainteresowania Rolskiego obejmują"),
    ("R15", "sylwetki/tomasz-rolski.md",
     "W szczególności profesor Rolski badał",
     "W szczególności Rolski badał"),
    ("R16", "sylwetki/tomasz-rolski.md",
     "monografia *Stochastic Processes for Insurance and Finance* (Wiley, 1999; wznowienie w 2009 r.)",
     "monografia [*Stochastic Processes for Insurance and Finance*](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/stochastic-processes-for-insurance-and-finance-978-0-471-95925-0) (Wiley, 1999; [wznowienie w 2009 r.](https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0470743638.html))"),
    ("R17", "sylwetki/tomasz-rolski.md",
     "Należy do najczęściej cytowanych prac profesora Rolskiego.",
     "Należy do jego najczęściej cytowanych prac."),
    ("R18", "sylwetki/tomasz-rolski.md",
     "jest *Lectures on Monte Carlo Theory* (Springer, 2025)",
     "jest [*Lectures on Monte Carlo Theory*](https://link.springer.com/978-3-032-01189-3) (Springer, 2025)"),
    ("R19", "sylwetki/tomasz-rolski.md",
     "zdolność profesora Rolskiego do",
     "zdolność Rolskiego do"),
    ("R20", "sylwetki/tomasz-rolski.md",
     "Profesor Rolski stworzył we Wrocławiu",
     "Rolski stworzył we Wrocławiu"),
    ("R21", "sylwetki/tomasz-rolski.md",
     "Wypromował ośmioro doktorów:",
     "Wypromował [ośmioro doktorów](https://www.mathgenealogy.org/id.php?id=84593):"),
    ("R22", "sylwetki/tomasz-rolski.md",
     "Profesor Rolski był jednym z głównych",
     "Rolski był jednym z głównych"),
    ("R23", "sylwetki/tomasz-rolski.md",
     "Profesor Rolski łączył wysokie",
     "Rolski łączył wysokie"),
    ("R24", "sylwetki/tomasz-rolski.md",
     "Profesor Rolski pełnił wiele",
     "Rolski pełnił wiele"),
    ("R25", "sylwetki/tomasz-rolski.md",
     "profesor Tomasz Rolski odebrał Medal Uniwersytetu Wrocławskiego,",
     "Tomasz Rolski odebrał [Medal Uniwersytetu Wrocławskiego](/instytut/warto-wiedziec/medal-uniwersytetu),"),
]
ZRODLA = {
    'sylwetki/marek-bozejko.md': "## Źródła {#zrodla}\n\n<!-- ŹRÓDŁA: Jeden punkt = jedno źródło: [tytuł](link) — co z niego wzięto. Na stronie sekcja jest zwinięta; zostaw {#zrodla}. -->\n- [Nota biograficzna prof. Marka Bożejki (PDF)](/pliki/aktualnosci/marekbozejkonotabiograficzna.pdf) — tekst sylwetki to nota z niewielkimi zmianami redakcyjnymi; autor: Grzegorz (do uzupełnienia nazwiskiem)\n- [Mathematics Genealogy Project: Marek Bożejko](https://mathgenealogy.org/id.php?id=123351) — doktorat (1973, promotor Stanisław Hartman, tytuł angielski „Sidon Sets in Noncommutative Groups”), 9 wypromowanych doktorów z latami promocji (J. Wysoczański i W. Młotkowski 1990, J. Krawczyk 1993, A. Buchholz 1999, P. Śniady 2001, I. Królak 2002, Ł. Wojakowski 2004, A. Krystek 2006, W. Ejsmont 2013), 12 potomków (stan na 19.11.2026).\n- [R. Duda, A. Weron, „Wrocławska szkoła matematyczna”, „Wiadomości Matematyczne” 42 (2006)](https://yadda.icm.edu.pl/baztech/element/bwmeta1.element.baztech-bc45390f-a74e-48aa-80c4-7d6fec3d7108/c/WiadMat_2006_1_6.pdf) — rok urodzenia (1946), doktorat 1973 u S. Hartmana, habilitacja 1980, profesura 1990, IM UWr; doktorat W. Młotkowskiego (1990) pod kierunkiem Bożejki; udział w rozwoju analizy harmonicznej i probabilistyki kwantowej.\n- [„Wrocławska szkoła matematyczna”, seria „Wrocławskie środowisko akademickie” (Dzieło 23)](https://dbc.wroc.pl/Content/1789/PDF/Dzielo%2023%20Wroc%C5%82awska%20Szko%C5%82a%20Matematyczna.pdf) — dr 1973, dr hab. 1980, prof. nadzw. 1990 (drzewo genealogiczne, s. 337); analiza harmoniczna, grupy topologiczne, probabilistyka kwantowa (s. 333–334).\n- [Archiwum UWr: wykaz habilitacji 1945–2015 (Wydział Matematyki, Fizyki i Chemii)](https://archiw.uwr.edu.pl/wp-content/uploads/sites/114/2023/01/hab_matfizchem_1945-2015.pdf) — habilitacja: uchwała z 21.05.1980, rozprawa „Zbiory lakunarne w nieprzemiennej analizie harmonicznej”.\n- [Archiwum UWr: wykaz doktoratów 1945–2015 (Wydział Matematyki, Fizyki i Chemii)](https://archiw.uwr.edu.pl/wp-content/uploads/sites/114/2023/01/DR_mat_fiz_chem_1945-2015.pdf) — doktoraty pod kierunkiem M. Bożejki z datami obron: J. Krawczyk (1993), A. Buchholz (1999), P. Śniady (2001), Ł. Wojakowski (2004), A. Krystek (2006), W. Ejsmont (2013).\n- [Fundacja Humboldta: Prof. Dr. Marek Bozejko](https://www.humboldt-foundation.de/en/connect/explore-the-humboldt-network/singleview/1071941/prof-dr-marek-bozejko) — Humboldt Research Award (rok 2001), gospodarz: prof. Michael Leinert, Uniwersytet w Heidelbergu.\n- [OpenAlex: Marek Bożejko](https://openalex.org/authors/A5007315110) — 72 prace, 2286 cytowań, indeks h = 21 (stan na 19.11.2026), prace z lat 2023–2025.\n- [Instytut Matematyczny UWr: prof. dr hab. Marek Bożejko](https://math.uni.wroc.pl/users/bozejko) — wykaz publikacji z lat 1972–2014 (według MathSciNet): artykuły w Comm. Math. Phys., J. Funct. Anal., Math. Ann., J. reine angew. Math., Adv. Math. i Trans. Amer. Math. Soc., praca z G. Fendlerem w Boll. Un. Mat. Ital. (1984).\n- [WMiI UWr: Emerytowani członkowie Rady Wydziału](https://wmi.uwr.edu.pl/emerytowani-czlonkowie-rady-wydzialu/) — status emeryta.\n- [20th Workshop: Noncommutative Probability, Operator Algebras and Related Topics, with Applications](https://sites.google.com/impan.pl/20thworkshop) — nazwa, termin (6–12.07.2025) i miejsce (Będlewo); cykl organizowany od 1997 roku, w Będlewie od 2004 roku.\n- [20th Workshop: komitet organizacyjny](https://sites.google.com/impan.pl/20thworkshop/organizing-committee) — M. Bożejko, W. Ejsmont, R. Lenczewski, W. Młotkowski, M. Tobolski, A. Wysoczańska-Kula, J. Wysoczański.\n- [IM UWr: Workshops — aims and history](https://math.uni.wroc.pl/analiza/workshops.html) — edycje 7–18 (2004–2018) z tytułami, nazwa „Noncommutative Harmonic Analysis”, Będlewo.\n- [14th Workshop: Non-Commutative Harmonic Analysis (2011)](https://www.impan.pl/BC/Arch/2011/14NCHA.html) — M. Bożejko w komitecie organizacyjnym; Joachim Cuntz w komitecie naukowym i wśród wykładowców.\n- [Banach Center Publications 78: wstęp do tomu](https://www.impan.pl/shop/media/volume_intro/bc78-0-001.pdf) — 9. warsztaty (Będlewo 2006), organizatorzy (M. Bożejko, A. Krystek, W. Młotkowski, J. Wysoczański), finansowanie m.in. z projektu Marie Curie Transfer of Knowledge MTKD-CT-2004-013389.\n- [CORDIS: HANAP — Harmonic analysis, nonlinear analysis and probability](https://cordis.europa.eu/project/id/13389/reporting) — projekt Transfer of Knowledge koordynowany przez UWr, 1.09.2005–31.08.2009, jeden z obszarów: „non-commutative probability”.\n- [Probability and Mathematical Statistics: Editorial Board](https://www.math.uni.wroc.pl/~pms/) — M. Bożejko jako Associate Editor.\n- [DigiLab UWr: Banach Center Publications 43, „Quantum Probability” (1998)](https://digilab.uwr.edu.pl/en/dlibra/publication/115345/quantum-probability) — redaktorzy: R. Alicki, M. Bożejko, W. A. Majewski.\n- [Banach Center Publications 73: Quantum Probability (2006)](https://www.impan.pl/en/publishing-house/banach-center-publications/all/73) — redaktorzy: M. Bożejko, W. Młotkowski, J. Wysoczański.\n- [Banach Center Publications 78: Noncommutative Harmonic Analysis with Applications to Probability (2007)](https://www.impan.pl/en/publishing-house/banach-center-publications/all/78) — redaktorzy: M. Bożejko, A. Krystek, W. Młotkowski, J. Wysoczański.\n- [Banach Center Publications 89: Noncommutative Harmonic Analysis with Applications to Probability II (2010)](https://www.impan.pl/en/publishing-house/banach-center-publications/all/89) — redaktorzy: M. Bożejko, A. Krystek, Ł. Wojakowski.\n- [Banach Center Publications 96: Noncommutative Harmonic Analysis with Applications to Probability III](https://www.impan.pl/en/publishing-house/banach-center-publications/all/96) — redaktorzy: M. Bożejko, A. Krystek, Ł. Wojakowski.\n- [Aktualności: Medale Uniwersytetu dla profesorów Marka Bożejki i Tomasza Rolskiego](/aktualnosci/2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego) — Medal UWr wręczony podczas Święta Uniwersytetu (13.11.2026).\n- [Sukcesy — historia](/nauka/sukcesy/historia) — Nagroda Główna PTM im. Stefana Banacha (1984), Nagroda Ministra Nauki za całokształt dorobku naukowego (2012).\n- [Seminarium „Dyskretna analiza harmoniczna i niekomutatywna probabilistyka”](/seminaria/dyskretna-analiza-harmoniczna) — seminarium prowadzone przez R. Szwarca i M. Bożejkę.\n- [Grant NCN 2016/21/B/ST1/00628 „Nieprzemienna probabilistyka z zastosowaniami”](/nauka/granty/2017-2016-21-b-st1-00628) — kierownik M. Bożejko, od 2017 roku.\n- [Grant BWZ/184/JSK/JSPS/08 „Nieprzemienna analiza harmoniczna na strukturach dyskretnych z zastosowaniem do probabilistyki”](/nauka/granty/2008-bwz-184-jsk-jsps-08) — współpraca z JSPS (Japonia), kierownik M. Bożejko, 2008–2009.\n- [M. Bożejko, „On Λ(p) sets with minimal constant in discrete noncommutative groups”, Proc. Amer. Math. Soc. 51 (1975)](https://www.ams.org/journals/proc/1975-051-02/S0002-9939-1975-0390658-3) — dane bibliograficzne; minimalne stałe dla zbiorów Λ(2n), nowy dowód twierdzenia Leinerta o zbiorach Λ(∞).\n- [I. Vergara, „An invitation to weak amenability, after Cowling and Haagerup”, arXiv 2024](https://arxiv.org/abs/2404.05513) — twierdzenie Bożejki–Fendlera (mnożniki Herza–Schura a całkowicie ograniczone mnożniki algebry Fouriera grupy lokalnie zwartej) pod tą nazwą; odsyłacz do pracy w Boll. Un. Mat. Ital. (1984).\n- [M. Bożejko, „Positive definite bounded matrices and a characterization of amenable groups”, Proc. Amer. Math. Soc. 95 (1985)](https://www.ams.org/proc/1985-095-03/S0002-9939-1985-0806070-2/) — dane bibliograficzne; grupa dyskretna jest średniowalna wtedy i tylko wtedy, gdy algebra mnożników Herza–Schura B₂(G) pokrywa się z B(G).\n- [M. Bożejko, R. Speicher, „An example of a generalized Brownian motion”, Comm. Math. Phys. 137 (1991)](https://doi.org/10.1007/BF02100275) — dane bibliograficzne; zdeformowane relacje komutacji z parametrem z przedziału [−1, 1], uogólniony rozkład Gaussa.\n- [M. Bożejko, R. Speicher, „Completely positive maps on Coxeter groups, deformed commutation relations, and operator spaces”, Math. Ann. 300 (1994)](https://eudml.org/doc/165244) — praca z 1994 roku (grupy Coxetera, zdeformowane relacje komutacji).\n- [M. Bożejko, R. Speicher, „Interpolations between bosonic and fermionic relations given by generalized Brownian motions”, Math. Z. 222 (1996)](https://eudml.org/doc/174879) — praca z 1996 roku (interpolacja między relacjami bozonowymi i fermionowymi).\n- [M. Bożejko, M. Leinert, R. Speicher, „Convolution and limit theorems for conditionally free random variables”, Pacific J. Math. 175 (1996)](https://msp.org/pjm/1996/175-2/p04.xhtml) — dane bibliograficzne, współautorzy; warunkowo wolny produkt i splot, warunkowo wolne rozkłady Gaussa i Poissona.\n- [M. Bożejko, H. Yoshida, „Generalized q-deformed Gaussian random variables”, Banach Center Publ. 73 (2006)](https://impan.pl/en/publishing-house/banach-center-publications/all/73/0/86545/generalized-q-deformed-gaussian-random-variables) — dane bibliograficzne; dwa parametry deformacji, wzory Wicka.\n- [S. T. Belinschi, M. Bożejko, F. Lehner, R. Speicher, „The normal distribution is ⊞-infinitely divisible”, Adv. Math. 226 (2011), arXiv](https://arxiv.org/abs/0910.4263) — współautorzy; wolna nieskończona podzielność rozkładu normalnego i podrodziny rozkładów Askeya–Wimpa–Kerova; DOI 10.1016/j.aim.2010.10.025.\n- [M. Bożejko, T. Hasebe, „On free infinite divisibility for classical Meixner distributions”, Probab. Math. Statist. 33 (2013)](https://digilab.uwr.edu.pl/en/dlibra/publication/113063/on-free-infinite-divisibility-for-classical-meixner-distribution-bozejko-marek-hasebe-takahiro) — wolna nieskończona podzielność rozkładów Meixnera.\n- [M. Bożejko, W. Ejsmont, „The Double Fock Space of Type B”, SIGMA 19 (2023)](https://www.imath.kyiv.ua/~sigma/2023/040/) — dane bibliograficzne; konstrukcja zgodna z kombinatoryką inwersji w grupie hiperoktaedralnej.\n",
    'sylwetki/tomasz-rolski.md': "## Źródła {#zrodla}\n\n<!-- ŹRÓDŁA: Jeden punkt = jedno źródło: [tytuł](link) — co z niego wzięto. Na stronie sekcja jest zwinięta; zostaw {#zrodla}. -->\n- [Nota biograficzna prof. Tomasza Rolskiego (PDF)](/pliki/aktualnosci/tomaszrolskinotabiograficzna.pdf) — tekst sylwetki to nota z niewielkimi zmianami redakcyjnymi; autor: Grzegorz (do uzupełnienia nazwiskiem)\n- [Tomasz Rolski — Curriculum Vitae (strona domowa, IM UWr)](https://www.math.uni.wroc.pl/~rolski/rolski-cv.html) — magisterium (1969), doktorat (1973), habilitacja (1983), tytuł profesora (1992), profesor zwyczajny od 1997, zastępca dyrektora IM (1988–1991), dyrektor IM (1996–2002), senator UWr (2002–2005), dziekan WMI (2005–2008), profesura wizytująca (Case Western 1988, UNC 1992–1993, Tokyo Institute of Technology 1999–2000), pobyty naukowe (Oxford 1976–1977, ANU, Cornell, UNC, Oberwolfach, Heriot-Watt w Edynburgu, Instytut Mittag-Lefflera), lista ośmiorga doktorów.\n- [Tomasz Rolski — strona domowa](https://www.math.uni.wroc.pl/~rolski/) — zainteresowania badawcze: procesy stochastyczne, porządki stochastyczne, modele fluidowe, kolejki, teoria ryzyka, procesy gaussowskie i punktowe, ubezpieczenia na życie.\n- [Tomasz Rolski — Publications (strona domowa)](https://www.math.uni.wroc.pl/~rolski/publications.html) — współautorzy (Asmussen, Daley, V. Schmidt, Teugels, Schmidli, Miyazawa, Aldous, Mandjes, Palmowski, Dębicki, Dieker, Bäuerle, Miyoshi, Błaszczyszyn), czasopisma (AAP, AnnAP, SPA, PTRF, MOR, Bernoulli), modele fluidowe (gaussowskie, on-off, semi-Markowa, sieci Lévy’ego), ryzyko w środowisku okresowym i markowskim, ekstrema wielowymiarowych ruchów Browna, supremum ułamkowego ruchu Browna.\n- [R. Duda, A. Weron, „Wrocławska szkoła matematyczna”, „Wiadomości Matematyczne” 42 (2006)](https://yadda.icm.edu.pl/baztech/element/bwmeta1.element.baztech-bc45390f-a74e-48aa-80c4-7d6fec3d7108/c/WiadMat_2006_1_6.pdf) — rok urodzenia (1946, s. 94), doktorat 1973 (promotor J. Łukaszewicz), habilitacja 1983, profesura 1992, teoria kolejek i matematyka ubezpieczeniowa, doktoraty Leśkowa i Szekliego (1987) i ich habilitacje.\n- [Mathematics Genealogy Project: Tomasz Rolski](https://www.mathgenealogy.org/id.php?id=84593) — doktorat (UWr 1973, promotor J. Łukaszewicz), 8 doktorów, 26 potomków (stan na 19.11.2026), nazwiska doktorów.\n- [zbMATH Open: Rolski, Tomasz](https://zbmath.org/authors/rolski.tomasz) — 91 publikacji w bazie (stan na 19.11.2026), główne działy: 60 (rachunek prawdopodobieństwa) i 90 (badania operacyjne).\n- [OpenAlex: Tomasz Rolski](https://openalex.org/A5030111068) — najczęściej cytowana praca: „Stochastic Processes for Insurance and Finance”; 4710 cytowań w tej bazie (stan na 18.11.2026).\n- [Wydział Matematyki i Informatyki UWr: History of the Faculty](https://wmi.uwr.edu.pl/en/english-history/) — dziekan WMI w latach 2005–2008 (po R. Szeklim, przed P. Bilerem).\n- [Uniwersytet Wrocławski: Święto Uniwersytetu Wrocławskiego 2026](https://uwr.edu.pl/swieto-uniwersytetu-wroclawskiego-2026/) — wręczenie Medalu UWr m.in. prof. Tomaszowi Rolskiemu, 13 listopada 2026, Aula Leopoldyńska.\n- [Statut Uniwersytetu Wrocławskiego, tekst jednolity (BIP UWr)](https://bip.uni.wroc.pl/download/attachment/47303/obwieszczenie-z-dnia-06022025-r-w-sprawie-ogloszenia-tekstu-jednolitego-uchwaly-nr-102-2019-w-sprawie-uchwalenia-statutu-uwr.pdf) — Medal nadaje Senat; Uniwersytet honoruje nim szczególnie zasłużonych pracowników (§ 229–231).\n- [Aktualności: Medale Uniwersytetu dla profesorów Marka Bożejki i Tomasza Rolskiego](/aktualnosci/2026-11-13-medale-uniwersytetu-dla-profesorow-bozejki-i-rolskiego) — medal przyznany przez Senat w uznaniu szczególnych zasług dla Uczelni.\n- [Wikipedia (ang.): Ross’s conjecture](https://en.wikipedia.org/wiki/Ross%27s_conjecture) — hipoteza Rossa (1978) i jej dowód przez Rolskiego (1981).\n- [S. M. Ross, „Average delay in queues with non-stationary Poisson arrivals”, Journal of Applied Probability 15 (1978)](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/average-delay-in-queues-with-nonstationary-poisson-arrivals/267BF6FF86F585CF37F1790EF43544B2) — sformułowanie hipotezy (1978): mniej regularny napływ zwiększa średnie opóźnienie.\n- [T. Rolski, „Queues with non-stationary input stream: Ross’s conjecture”, Advances in Applied Probability 13 (1981)](https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/queues-with-nonstationary-input-stream-rosss-conjecture/4218BA71795B7AD9A6C213C9074364FC) — dane bibliograficzne; wynik: przy podwójnie stochastycznym napływie Poissona średnie opóźnienie jest nie mniejsze niż w kolejce M/G/1 o tym samym natężeniu.\n- [N. Bäuerle, T. Rolski, „A monotonicity result for the workload in Markov-modulated queues”, Journal of Applied Probability 35 (1998)](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/monotonicity-result-for-the-workload-in-markovmodulated-queues/A5C06FA9AF5A54AFA5D0C9E8A36643B6) — dane bibliograficzne; monotoniczność obciążenia w kolejkach sterowanych łańcuchem Markowa (porządek wypukły rosnący).\n- [N. Miyoshi, T. Rolski, „Ross-type conjectures on monotonicity of queues”, Australian & New Zealand Journal of Statistics 46 (2004)](https://iaorifors.com/paper/47199) — dane bibliograficzne; uogólnienia hipotezy Rossa przy założeniach porządku kierunkowo wypukłego (idcx).\n- [Z. Palmowski, T. Rolski, „A technique for exponential change of measure for Markov processes”, Bernoulli 8 (2002) (Repozytorium UWr)](https://digilab.uwr.edu.pl/dlibra/publication/116593/a-technique-for-exponential-change-of-measure-for-markov-processes-palmowski-zbigniew-rolski-tomasz) — dane bibliograficzne.\n- [K. Dębicki, A. B. Dieker, T. Rolski, „Quasi-product forms for Lévy-driven fluid networks”, Mathematics of Operations Research 32 (2007)](https://pubsonline.informs.org/doi/abs/10.1287/moor.1070.0259) — dane bibliograficzne (DOI 10.1287/moor.1070.0259).\n- [Springer: T. Rolski, „Stationary Random Processes Associated with Point Processes”, Lecture Notes in Statistics 5 (1981)](https://rd.springer.com/chapter/10.1007/978-1-4684-6268-5_2) — pierwsza monografia (1981).\n- [Wiley-VCH: „Stochastic Processes for Insurance and Finance” (1999)](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/stochastic-processes-for-insurance-and-finance-978-0-471-95925-0) — współautorzy (Schmidli, Schmidt, Teugels), Wiley 1999, XVIII + 654 strony, spis treści (szkody, procesy ryzyka i odnowy, łańcuchy Markowa, martyngały, procesy punktowe, modele dyfuzyjne).\n- [Wiley: „Stochastic Processes for Insurance and Finance”, wydanie w miękkiej oprawie (2009)](https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0470743638.html) — wznowienie z marca 2009.\n- [B. Błaszczyszyn, T. Rolski, „Podstawy matematyki ubezpieczeń na życie” (fragment: strona tytułowa i spis treści)](https://ebookpoint.pl/pobierz-fragment/podstawy-matematyki-ubezpieczen-na-zycie-bartlomiej-blaszczyszyn-tomasz-rolski,e_1gco/pdf) — autorzy, WNT, Warszawa 2004.\n- [Komisja Egzaminacyjna dla Aktuariuszy: wykaz zalecanej literatury (2018)](https://www.knf.gov.pl/knf/pl/komponenty/img/Wykaz_zalecanej_literatury_oraz_aktow_prawnych2018.pdf) — „Podstawy matematyki ubezpieczeń na życie” na liście lektur do egzaminu aktuarialnego (matematyka ubezpieczeń na życie).\n- [Springer: P. Lorek, T. Rolski, „Lectures on Monte Carlo Theory” (2025)](https://link.springer.com/978-3-032-01189-3) — współautor, Springer 2025, XVI + 632 strony, zakres (liczby pseudolosowe, MCMC, optymalizacja stochastyczna, uzasadnienia teoretyczne, kod w Pythonie).\n- [Lehmanns: „Lectures on Monte Carlo Theory” — spis treści](https://www.lehmanns.ch/shop/mathematik-informatik/80516542-9783032011893-lectures-on-monte-carlo-theory) — rozdziały: generatory, generowanie zmiennych losowych, analiza wyników symulacji, redukcja wariancji, MCMC, optymalizacja stochastyczna, symulacja kolejek.\n",
}

SPRAWDZ = '--sprawdz' in sys.argv
pliki = {}
def czytaj(p):
    if p not in pliki:
        with open(os.path.join(KAT, p), encoding='utf-8', newline='') as f: pliki[p] = f.read()
    return pliki[p]
def eol(t): return '\r\n' if '\r\n' in t else '\n'
bledy = []

# 0. Zlecenie 53 musi być wykonane (bez „Do pobrania” u Bożejki i Rolskiego)
for p in ZRODLA:
    if '## Do pobrania {#do-pobrania}' in czytaj(p): bledy.append(f'{p}: jest jeszcze „Do pobrania” — najpierw zlecenie 53')

# 1. Zamiany tekstu
for id_, p, bylo, ma in ZAMIANY:
    t = czytaj(p); e = eol(t); b = bylo.replace('\n', e); n = t.count(b)
    if n != 1: bledy.append(f'{id_} {p}: „bylo” występuje {n}×'); continue
    pliki[p] = t.replace(b, ma.replace('\n', e))

# 2. „Źródła” Bożejki i Rolskiego: od „## Źródła {#zrodla}” do końca pliku
for p, nowe in ZRODLA.items():
    t = czytaj(p); e = eol(t)
    if t.count('## Źródła {#zrodla}') != 1: bledy.append(f'{p}: nie ma jednej sekcji „## Źródła {{#zrodla}}”'); continue
    pliki[p] = t[:t.find('## Źródła {#zrodla}')] + nowe.replace('\n', e)

if bledy:
    print('STOP, nic nie zapisano:'); [print(' -', b) for b in bledy]; sys.exit(1)

# 3. Pogrubienia: zostają tylko wstępy wyliczeń (**Hasło.** / **Hasło:** na początku akapitu)
#    i lata laureatów (**2026** na początku punktu listy). Komentarze <!-- … --> bez zmian.
PARA = re.compile(r'(?:^|\n[ \t\r]*\n)[ \t]*$')
PUNKT = re.compile(r'(?:^|\n)[ \t]*- $')
def pogrubienia(t):
    out, poz, usun, zost = [], 0, 0, 0
    kom = [(m.start(), m.end()) for m in re.finditer(r'<!--.*?-->', t, re.S)]
    for m in re.finditer(r'\*\*(.+?)\*\*', t, re.S):
        if any(a <= m.start() < b for a, b in kom): continue
        przed, w = t[:m.start()], m.group(1)
        if (PARA.search(przed) and re.search(r'[.:]\)?$', w.strip())) or (PUNKT.search(przed) and re.fullmatch(r'\d{4}', w)):
            zost += 1; continue
        out += [t[poz:m.start()], w]; poz = m.end(); usun += 1
    out.append(t[poz:])
    return ''.join(out), usun, zost
for sciezka in sorted(glob.glob(os.path.join(KAT, '*', '*.md'))):
    p = os.path.relpath(sciezka, KAT).replace(os.sep, '/')
    t2, u, z = pogrubienia(czytaj(p))
    if u: pliki[p] = t2
    if u or z: print(f'pogrubienia {p}: usunięte {u}, zostają {z}')

zmienione = 0
for p, t in pliki.items():
    with open(os.path.join(KAT, p), encoding='utf-8', newline='') as f: stare = f.read()
    if t != stare:
        zmienione += 1
        if not SPRAWDZ:
            with open(os.path.join(KAT, p), 'w', encoding='utf-8', newline='') as f: f.write(t)
print(('SPRAWDZENIE: do zmiany ' if SPRAWDZ else 'Zapisano ') + f'{zmienione} plików, {len(ZAMIANY)} zamian, 2 sekcje „Źródła”.')
