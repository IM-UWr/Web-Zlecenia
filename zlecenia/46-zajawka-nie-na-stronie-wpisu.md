# Zlecenie 46: zajawka nie pokazuje się na stronie wpisu aktualności (18.11.2026)

**Skąd to zlecenie.** Na stronie wpisu „Stypendium im. Steinhausa dla Dominika Gdesza” (`Web-Aktualnosci/src/content/aktualnosci/2026-11-11-stypendium-im-steinhausa-dla-dominika-gdesza.md`) to samo zdanie stoi dwa razy:
- najpierw zajawka jako pierwszy, wyróżniony akapit (`p.wst`),
- zaraz pod nią pierwsze zdanie treści.

Redaktorzy wpisują jako zajawkę pierwsze zdanie treści, bo etykieta pola mówi „Zajawka (1–2 zdania na listę i stronę główną)”. Nie wiedzą, że zajawka pokazuje się też nad treścią wpisu. Zgrubne sprawdzenie 18.11 (pierwsze 40 znaków zajawki w pierwszym akapicie): tak jest w ok. 28 ze 165 wpisów z zajawką, także w nowym wpisie o wykładzie MISiU (`2026-11-18-wyklad-popularnonaukowy-z-cyklu-misiu.md`).

**Decyzja właściciela (18.11, 19:01):** „Po prostu w opisie wydarzenia nie pokazujmy zajawki”. Dotyczy strony każdego wpisu aktualności, wszystkich rodzajów (ogłoszenie, wydarzenie, sukces, kariera). Zajawka zostaje tam, gdzie jest skrótem wpisu: na listach i na stronie głównej.

**Zasady pracy:**
- Jak w `.przekazanie\zlecenia\zasady.md`: lokalna gałąź robocza, push dopiero po „push” właściciela.
- Raport `RAPORT-ZLECENIE-46.md`, zrzuty `raport-zrzuty/z46-*`. Bez subagentów.
- Zmiana tylko w Web-Core. Repozytoria treści i `.pages.yml` bez zmian, więc sekcja „Ochrona zmian redaktorów” nie dotyczy tego zlecenia.

## Stan dziś
- `src/views/Aktualnosc.astro`, linia 71: `{zajawka && <p class="wst" lang={langPola(d, 'zajawka', lang)}>{zajawka}</p>}` (PL i EN, `zajawka` z `daneAktualnosci`, `src/lib/widoki/aktualnosc.ts`, linia 14).
- Ta sama zmienna idzie też do `opis={zajawka}` w `<Podstrona …>` (linia 66): to opis strony w `<meta>` i podglądach linków.
- Klasa `.wst` jest używana także w innych widokach (m.in. `WartoWiedziecWpis.astro`, `RokAkademicki.astro`, `Zaklad.astro`), więc CSS zostaje.

## Docelowo
1. **Strona wpisu** (`/aktualnosci/<wpis>` i `/en/aktualnosci/<wpis>`): bez akapitu zajawki pod linią „Rodzaj · Opublikowano … · Dla: …”. Pod tą linią od razu karta albo tekst wpisu.
2. **Bez zmian:**
   - `opis={zajawka}` w `<Podstrona>`, czyli `<meta name="description">` i podglądy linków (og:description);
   - zajawka na listach (Aktualności, Sukcesy, Kariera, listy działów), na stronie głównej, w Kalendarzu i wszędzie poza stroną wpisu;
   - `AktualnoscZamianaDni.astro` (zajawka tam idzie tylko do `opis`);
   - Warto wiedzieć (`WartoWiedziecWpis.astro`) i obrony doktorskie.
3. **Siatka bezpieczeństwa** (strona bezobsługowa): jeśli treść wpisu w danym języku jest pusta (bez komentarzy `<!-- … -->`; dla EN: pusta `tresc_en` i pusta treść PL), zajawka pokazuje się jak dotąd, żeby strona wpisu nie została bez tekstu. Stan 18.11: takich wpisów jest 0, więc dziś to nic nie zmienia.
4. **Komentarz na początku `Aktualnosc.astro`:** popraw opis („zajawka jako pierwszy akapit (p.wst)” → zajawka nie jest pokazywana na stronie wpisu, wyjątek: pusta treść; decyzja 18.11.2026).
5. **Dokumentacja dla redaktorów:** sprawdź, czy `dok/sciagawka-edytora.md`, `dok/jawny-markdown.md` albo PDF-y w Web-Podglad `dla-redaktorow/` piszą, że zajawka jest pierwszym akapitem wpisu. Jeśli tak, popraw ściągawkę; PDF-y do poprawy wypisz w raporcie. Etykieta pola w CMS („Zajawka (1–2 zdania na listę i stronę główną)”) zostaje, bo teraz jest zgodna z prawdą.

## Odbiór lokalny
- **Porównanie HTML przed/po** (PL i EN, te same klony treści). Dozwolona różnica: brak `p.wst` na stronach `/aktualnosci/*` i `/en/aktualnosci/*`, w tym wpisy Kariery, oraz wynikające z tego zmiany indeksu wyszukiwarki (Pagefind). Każdą inną różnicę zgłoś.
- `<meta name="description">` na stronach wpisów bez zmian.
- Test siatki bezpieczeństwa: tymczasowa kopia wpisu z zajawką i pustą treścią (sam komentarz) pokazuje zajawkę. Kopię potem usuń.
- **Zrzuty:** wpis Gdesza (z kartą bez zdjęcia), wpis wydarzenia z kartą (np. `2026-09-10-wyklad-prof-uwe-franza.md`) i oferta Kariery; 1920×1080 i 390 px, PL i EN.
- **Kontrole:** `astro check` bez nowych błędów, `sprawdz_tresci.py` OK, konsola czysta.
- **Stop:** raport i czekanie na „push”.

## Kryteria odbioru
- [ ] Na stronie wpisu aktualności (PL i EN, wszystkie rodzaje) nie ma akapitu zajawki.
- [ ] Zajawka bez zmian na listach, na stronie głównej, w Kalendarzu i w `<meta name="description">`.
- [ ] Wpis z pustą treścią dalej pokazuje zajawkę.
- [ ] Porównanie HTML przed/po: tylko opisane różnice.
- [ ] Komentarz w `Aktualnosc.astro` i ściągawka zgodne z nowym działaniem; lista PDF-ów do poprawy w raporcie.

## Do wiadomości właściciela (nie do zrobienia w tym zleceniu)
- 18.11 (19:02, commit `abf23d3`) właściciel zmienił w Configuration etykietę w Web-Aktualnosci (`.pages.yml`) na „Termin wydarzenia (tylko spotkania, konferencje itp, ogólna informacja zostaw puste)”. Pages CMS nie pokazuje `description` przy polach-listach (z przyciskiem „Add an item”), więc wskazówka musi być w etykiecie. Etykieta z „: ” w środku musi być w apostrofach, inaczej YAML się nie wczyta i formularz Aktualności się wywala (tak było przez kilka minut 18.11, 19:00).
- Ten sam brak opisu dotyczy „Termin zgłoszeń” (Kariera, zlecenie 44); jego etykieta mówi jednak najważniejsze.
