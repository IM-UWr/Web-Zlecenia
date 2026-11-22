// Zlecenie 25 — PROTOTYP (CSS i pomiar wstrzyknięte w zbudowany podgląd; wzór zachowania, nie kod do skopiowania 1:1).

/* Krok 1 (pole „Na tej stronie” ustępuje) i krok 2 (łamanie tylko między słowami) — tak symulowano w prototypie: */
const CSS_PROTOTYPU = `
.z-pd:not(.z-pd-pelna) { grid-template-columns: minmax(0, 1fr) !important; }   /* przy wdrożeniu: pole zwija się nad treścią jak na telefonie, nie znika */
.z-pd > .z-spis, .z-pd > .z-pd-prawa { display: none !important; }
.z-pl .pl-w > span { overflow-wrap: normal !important; }                       /* Plan zajęć: bez łamania w środku słowa */
.tresc .kontakty { grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)) !important; gap: 0 32px !important; }
.tresc .kontakty * { overflow-wrap: normal !important; word-break: normal !important; }`;
// E-mail łamany tylko przed „@” (w prototypie skryptem; przy wdrożeniu przy budowie strony):
const WBR = () => document.querySelectorAll('.tresc .kontakty a[href^="mailto:"]').forEach((a) => { a.innerHTML = a.textContent.replace('@', '<wbr>@'); });

/* Pomiar: liczba linii pozycji = liczba różnych górnych krawędzi prostokątów tekstu (komórki siatki rozciągają się do
   wysokości wiersza, więc nie liczyć z wysokości elementu). W Planie zajęć osoby w jednej komórce są rozdzielone <br> —
   liczyć osobno każdą osobę. Tekst tylko dla czytnika (.sr-only, prostokąty ≤ 2 px) pominąć. */
function liczLinie(el) {
  const g = document.createRange(); g.selectNodeContents(el);
  return new Set([...g.getClientRects()].filter((r) => r.width > 2).map((r) => Math.round(r.top))).size;
}
// Uwaga: prostokąty elementu <a> i tekstu w nim mogą mieć górne krawędzie różniące się o ułamek piksela — zaokrąglanie
// do pełnych pikseli potrafi dać +1 linię. Przy wdrożeniu grupuj krawędzie z tolerancją ok. pół wysokości linii.
function wystajeSlowo(el) { return el.scrollWidth > el.clientWidth + 1; }

/* Wyniki prototypu (Plan zajęć, semestr zimowy, 253 osoby w komórkach „prowadzący”, 88 przedmiotów):
   okno | dziś: prowadzący / osoby > 2 linie | po krokach 1–2: prowadzący / osoby > 2 linie / słowa wystające
   1024 |  11 px / 253 z 253 (litera po literze) | 173 px / 0 / 0
   1180 |  98 px /   7 z 253                     | 260 px / 0 / 0
   1280 | 153 px /   3 z 253                     | 316 px / 0 / 0
   Nazwy przedmiotów (kolumna 220 px, bez zmian): przy 1920 px 7 z 88 ma 3 linie, żadna nie ma 4 — limit 3 linie spełniony.
   Kontakty (Szkoła doktorska, Matematyka) przy 1024 i 1180 px po krokach 1–2 i auto-fill 250 px: bez kolizji, nazwiska w 1 linii,
   najdłuższy e-mail (Justyna.Jedrzejewska-Idczak@uwr.edu.pl) w 2 liniach przed „@” — zob. 25-kontakty-dzis-i-zasada.jpg.
   Strony z tabelami i kolumnami (kontakty kierunków, Szkoła doktorska, Pracownicy, Granty, Konferencje, Władze) po kroku 1:
   0 problemów w pomiarze 24-pomiar-szerokosci.cjs przy 1024, 1180 i 1280 px. */
