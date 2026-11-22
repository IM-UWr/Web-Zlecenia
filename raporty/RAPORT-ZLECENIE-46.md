# Raport: zlecenie 46, zajawka nie pokazuje się na stronie wpisu aktualności (18.11.2026)

**Status:** zrobione lokalnie, **nic nie wypchnięte**. Czeka na „push” razem ze zleceniami 47 i 48 (jedno STOP na końcu serii). Zmiana tylko w Web-Core. Repozytoria treści i `.pages.yml` są bez zmian, więc ochrona zmian redaktorów tego zlecenia nie dotyczy.

| Repozytorium | Gałąź lokalna | Commit | Baza |
|---|---|---|---|
| Web-Core (worktree `Web-Core-B`) | `praca/46-zajawka` (od gałęzi 48) | `309dd78c` | `3cde30e0` (origin/main) + 47 `1e479c91` + 48 `61d6e683` |

## Co jest zrobione
- `src/lib/widoki/aktualnosc.ts`: nowa wartość `zajawkaNaStronie`, czyli zajawka tylko wtedy, gdy wpis nie ma w tym języku żadnego tekstu. Treść liczy się jako pusta, gdy po usunięciu komentarzy `<!-- … -->` nic nie zostaje. Na stronie EN: jeśli jest Treść EN, liczy się ona; jeśli jej nie ma, liczy się treść polska, bo to ją strona EN wtedy pokazuje. W pozostałych przypadkach wartość jest pusta.
- `src/views/Aktualnosc.astro`: akapit `p.wst` pokazuje `zajawkaNaStronie`, więc pod linią „Rodzaj · Opublikowano … · Dla: …” jest od razu karta albo tekst wpisu. Dotyczy wszystkich rodzajów (ogłoszenie, wydarzenie, sukces, kariera) i obu języków.
- Bez zmian: `opis={zajawka}` w `<Podstrona>` (`<meta name="description">`, og:description), zajawka w bloku wydarzenia (`.ics`, Kalendarz), na listach i na stronie głównej, `AktualnoscZamianaDni.astro`, „Warto wiedzieć”, obrony; CSS `.wst` zostaje (używają go inne widoki).
- Komentarz na początku `Aktualnosc.astro`: usunięte „zajawka jako pierwszy akapit (p.wst)”, dopisany akapit o zleceniu 46 (zajawka nie jest pokazywana na stronie wpisu, wyjątek: pusta treść, decyzja 18.11.2026).
- **Dokumentacja dla redaktorów:** ani `dok/sciagawka-edytora.md`, ani `dok/jawny-markdown.md`, ani PDF-y w Web-Podglad `dla-redaktorow/` (`Mapa-CMS-IM-UWr.pdf`, `Czat-AI-formatowanie-tresci.pdf`, przeszukane przez `pdftotext`) nie piszą, że zajawka jest pierwszym akapitem wpisu. **PDF-ów do poprawy: brak.** Do ściągawki dopisałem jedno zdanie w sekcji „Aktualności”: gdzie zajawka się pokazuje, że na stronie wpisu jej nie ma (więc może powtarzać pierwsze zdanie treści), wyjątek dla wpisu bez treści i jak działa wersja EN. Etykieta pola w CMS zostaje bez zmian.

## Odstępstwa od zlecenia i powody
1. **Siatka bezpieczeństwa po angielsku**, dokładniej niż w zleceniu („pusta `tresc_en` i pusta treść PL”): sprawdzam treść, którą strona EN naprawdę pokazuje. Gdyby Treść EN miała same komentarze, strona EN pokazałaby właśnie ją (pustą), nie tekst polski, więc wtedy też pokazuję zajawkę. Dziś takich wpisów jest 0, więc wynik jest ten sam.
2. **Wpis Gdesza** ma w zleceniu dopisek „z kartą bez zdjęcia”, ale w danych nie ma ani zdjęcia, ani terminu, więc karty nie ma — przed zmianą i po niej. Zrzut i tak pokazuje to, o co chodziło: zdublowanego zdania już nie ma.

## Pytania do właściciela
Brak.

## Odbiór lokalny
Budowy: „przed” = wynik 48 (`tresci-B/z48-po`), „po” = `tresci-B/z46-po` (te same klony treści), „siatka” = `tresci-B/z46-siatka` (po + tymczasowa kopia wpisu z zajawką PL i EN i treścią złożoną z samego komentarza; kopia usunięta, nakładka przywrócona). Skrypty: `tresci-B/z46-budowy.sh`, `raport-zrzuty/z46-skrypt/porownaj46.py` (log `tresci-B/z46-porownaj.log`), `zrzuty46.mjs`.

**Dane (stan 18.11):** 167 wpisów, 165 z zajawką. Wpisy z pustą treścią: PL 0, EN 0. Treść EN z samymi komentarzami: 0. Siatka dziś nic nie zmienia.

**Porównanie HTML przed i po (`porownaj46.py`): 0 problemów.**
- Te same pliki w obu budowach (5012, bez Pagefind).
- 330 stron wpisów (165 PL + 165 EN, w tym oferty Kariery) różni się wyłącznie brakiem `p.wst`. Po jego usunięciu zostaje jedna spacja odstępu, dlatego porównanie zwija białe znaki. Po zmianie żadna strona wpisu nie ma `p.wst`.
- `<meta name="description">` i og:description bez zmian na wszystkich 330 stronach (wszystkie niepuste).
- Innych różnic: 0. Lista i EN lista Aktualności, Kariera, strona główna, Kalendarz, Studia: bez zmian. Strony „zamiany dni” (osobny widok) też bez zmian. 112 plików różni się tylko znacznikiem czasu (`DTSTAMP` w `.ics`, „wygenerowano” w `powiadomienia.json`). Pagefind: indeks inny, bo zniknął tekst zajawek ze stron wpisów (różnica dozwolona przez zlecenie).

**Siatka bezpieczeństwa:** kopia z pustą treścią pokazuje zajawkę w `p.wst` na stronie PL („Zajawka testowa…”) i EN („Test teaser…”). Inne wpisy w tej budowie dalej są bez `p.wst`.

**Zrzuty** (`raport-zrzuty/z46-zrzuty/`, 13 plików, tryb jasny): wpis Gdesza, wpis wydarzenia z kartą (wykład prof. Uwe Franza, ze zdjęciem i blokiem „Kiedy / Gdzie”) i oferta Kariery (korepetytor); 1920×1080 i 390×844; PL i EN. Do tego `z46-gdesz-pl-1920-PRZED.png` dla porównania (przed: zajawka i zaraz pod nią to samo zdanie w treści). Konsola czysta, na żadnej stronie wpisu nie ma `p.wst`.

**Kontrole:** `astro check` 0 błędów, 0 ostrzeżeń (4 podpowiedzi, jak przed zmianą); `npm run test:jawne` 76/76; `sprawdz_tresci.py` OK — 597 plików, 1 ostrzeżenie (Rolski „xxxx”, ze zlecenia 47).

## Kryteria odbioru
- Na stronie wpisu aktualności (PL i EN, wszystkie rodzaje) nie ma akapitu zajawki — spełnione.
- Zajawka bez zmian na listach, na stronie głównej, w Kalendarzu i w `<meta name="description">` — spełnione.
- Wpis z pustą treścią dalej pokazuje zajawkę — spełnione (test na kopii).
- Porównanie HTML przed i po: tylko opisane różnice — spełnione.
- Komentarz w `Aktualnosc.astro` i ściągawka zgodne z nowym działaniem; lista PDF-ów do poprawy: pusta — spełnione.

## Test w CMS (po pushu, z właścicielem)
Niepotrzebny: formularz się nie zmienia. Wystarczy obejrzeć na stronie publicznej (po budowie) wpis Gdesza i dowolny wpis z kartą: pod linią z rodzajem i datą od razu tekst albo karta.

## Push (zrobię po „push”)
Razem z 47 i 48: rebase serii na `origin/main` (dziś `origin/main` = `3cde30e0`, więc wystarczy przewinięcie), push `main` w Web-Core.

## Push (18.11.2026, po „push” właściciela)
Web-Core `3cde30e0..4e1d4c62` (w serii z 47 i 48, przewinięcie). Repozytoria treści bez zmian.
