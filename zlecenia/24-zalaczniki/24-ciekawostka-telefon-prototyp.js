// Zlecenie 24, punkt 5 — PROTOTYP (wstrzyknięty w zbudowany podgląd, nie kod do skopiowania 1:1).
// Widok telefonu, nagłówek podstrony z ciekawostką: opis ciekawostki z lewej od symbolu, gdy się mieści; inaczej znika (symbol zostaje).
// Prototyp działał na kopii podglądu z progiem telefonu przesuniętym do 1023 px. W prototypie brakowało sprawdzenia wysokości
// (Organizatorzy przy 700 px: niski nagłówek bez liczb ucinał tekst od dołu) — przy wdrożeniu dołóż je (punkt 5 zlecenia).

/* CSS prototypu (w widoku telefonu, gdy nagłówek ma co najmniej ok. 560 px szerokości) */
const CSS = `@media (min-width: 560px) and (max-width: 1023px) {
 .z-nagl.z-nagl-pod .z-znak-opis { display: block; position: absolute; z-index: 1; right: 124px; top: calc(var(--hdr-h) + 16px); width: min(290px, 40%); margin: 0; text-align: right;
   font-size: 12.5px; line-height: 1.45; color: rgb(255 255 255 / .85); text-shadow: 0 1px 8px rgb(13 24 48 / .9); }
 .z-nagl.z-nagl-pod .z-znak-opis b { display: block; font-family: var(--f-display); font-style: italic; font-weight: 500; font-size: 14px; color: #fff; }
 .z-nagl.z-nagl-pod .z-znak-opis.z-brak-miejsca { display: none; }
}`;
// Symbol na telefonie: .z-znak { right: 6px; width: 104px } (zal-telefon.css) — stąd right: 124px opisu (104 + 6 + 14 odstępu).

/* „Jest miejsce?” — opis nie może dotykać (z odstępem 16 px) tytułu, ścieżki, hasła ani liczb. */
function miejsceNaCiekawostke() {
  const n = document.querySelector('.z-nagl-pod'), o = n && n.querySelector('.z-znak-opis');
  if (!o || getComputedStyle(o).display === 'none') return 'brak opisu';
  o.classList.remove('z-brak-miejsca');
  const R = o.getBoundingClientRect(), pola = [];
  n.querySelectorAll('h1, .z-haslo, .z-sciezka a, .z-slot li').forEach((e) => {
    const g = document.createRange(); g.selectNodeContents(e); pola.push(...g.getClientRects());
  });
  const kolizja = pola.some((r) => r.width && r.right + 16 > R.left && r.left < R.right && r.bottom > R.top && r.top < R.bottom);
  // DO DOŁOŻENIA przy wdrożeniu: wysokość — dół opisu nie niżej niż dół nagłówka minus jego dolny padding.
  if (kolizja) o.classList.add('z-brak-miejsca');
  return kolizja ? 'znika' : 'widać';
}
// Wywoływać: po wylosowaniu ciekawostki (skrypt CK w NaglowekZ.astro), po document.fonts.ready i przy zmianie rozmiaru okna (rAF).

/* Wynik prototypu (3 losowania na stronę; ● widać, ○ znika):
strona              600    700    800    900    980
sd                  ○○○    ○○○    ●●●    ●●●    ●●●
podyplomowe         ○○○    ○○○    ○○○    ●●●    ●●●
organizatorzy       ○○○    ●●●    ●●●    ●●●    ●●●   (przy 700 ucięty od dołu — brak sprawdzenia wysokości)
matematyka          ○○○    ●●●    ●●●    ●●●    ●●●
isim                ○○○    ○○○    ○○○    ○○○    ○○○
infrastruktura      ○○○    ○○○    ○○○    ○○○    ●●●
konferencje         ○○○    ●●●    ●●●    ●●●    ●●●
*/
