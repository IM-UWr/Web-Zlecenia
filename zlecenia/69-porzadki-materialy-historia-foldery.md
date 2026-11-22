# Zlecenie 69 (23.11.2026): porządki – stare materiały dla redaktorów, historia zleceń na GitHubie, foldery w Github – WYKONANE

> Zapis po fakcie (changelog). Claude Code, 23.11.2026, ok. 0:00–1:00. Numer 68 zajęła równoległa sesja (minione referaty według lat).

**Decyzje właściciela:**
- „W folderze github mamy strasznie dużo folderów… Czy możemy pousuwać wszystkie, które nie są nam już potrzebne”, a potem „Wszystkie niepotrzebne foldery usuń”.
- „I wszystkie mapy dla redaktorów, artefakty przeszłości nieaktualne out. Żeby się nie mieszały”.
- „Usuwaj wszystko oprócz historii zleceń. Ta ma zostać. I ma być i lokalnie, i na GitHubie. Jako taki changelog”.
- „Czy da się zrobić, żeby zlecenia lądowały na GitHubie od razu i stąd Code je pobierał… Żeby to domyślnie zapamiętać”. Potem: „Web-Zlecenia możesz zmienić na publiczne”.
- „Innych projektów nie ruszamy. Tylko rzeczy dotyczące strony”. O IM-Website-test: „Wywalić”.
- „Chodzi mi przede wszystkim o usunięcie folderów w głównym widoku. Dokładne sprzątanie odłożymy na później”. O `tresci`, `tresci-B` i `tresci-C`: „Usuń na stałe”.

## Stare materiały dla redaktorów (usunięte)
- **claude.ai** (usunięte na stałe):
  - dokument „Mapa CMS — strona IM UWr” z 6.11 (gałąź `wyglad/zlecenie-16`, 21 repozytoriów, bez Tutornii);
  - „Teksty z czatu AI na stronę IM” z 19.11 (stare ścieżki `/pliki/…`, Tutornia w Stronach).
- **Web-Podglad da0d563 [skip ci]:** `dla-redaktorow/Czat-AI-formatowanie-tresci.pdf` z 7.11 (stary format z „Blokami”).
- **Web-Core `Claude outputs/`:** `Czat-AI-formatowanie-tresci.pdf` i `prompt-czat.txt` poszły do Kosza, a pusty folder został usunięty.
- Zostały tylko dwa PDF-y ze zlecenia 67, pod stałymi adresami.

## Historia zleceń w repozytorium Web-Zlecenia
- Nowe repozytorium https://github.com/IM-UWr/Web-Zlecenia. Najpierw było prywatne, a tego samego dnia stało się publiczne na polecenie właściciela. Jego treść nie trafia na stronę.
- Folder `Web-Core/.przekazanie/` jest jego klonem. Zawiera:
  - zlecenia 01–67 z załącznikami;
  - dziennik;
  - raporty: 60 plików `RAPORT-*.md` i `PYTANIA.md`, przeniesionych z katalogu głównego Web-Core do `raporty/`;
  - prototypy i dokumenty startowe;
  - stare zlecenia agentów, rozpakowane do `zlecenia/agentow-i-czesciowe/`.
- Przed upublicznieniem całość została przeszukana pod kątem tokenów, kluczy, haseł, prywatnego e-maila i telefonów. Nic nie znaleziono.
- Zasada: na początku pracy `git -C .przekazanie pull`, a po każdym zapisie commit i push.
  - Zapisana w `zlecenia/zasady.md`, w README repozytorium, w `CLAUDE.md` w Web-Core i w pamięci Claude Code.
  - Web-Core f647f6f7 i 9f62de8d [skip ci]: `CLAUDE.md` oraz `/.przekazanie/` w `.gitignore`.
- Repozytorium jest publiczne, więc nie zapisuje się w nim haseł, tokenów ani prywatnych danych.
- Zlecenie 68 (równoległa sesja) przeszło już tą drogą.

## Usunięte pliki robocze (do Kosza)
- `.przekazanie/robocze/` (368 MB: archiwa drzewa z 31.10–6.11, kopie nakładki, bundle'e).
- `web-core-lokalne-commity.bundle`, `web-core-nakladka-i-prototypy.tar.gz`, `zlecenia-agentow-i-czesciowe.tar.gz`.
- Przed usunięciem sprawdzone, że commity z bundle'i są w `main` na GitHubie.
- `Web-Core/raport-zrzuty/` (1,5 GB zrzutów z testów). Od teraz zrzutów się nie przechowuje: robi się je w katalogu tymczasowym, a w raporcie opisuje wynik.

## Foldery w Documents\Github
- **Do Kosza:**
  - `_stare`, `podglad-z33`, `tresci-z31`, `tresci-z33`, `tresci-z39`, `tresci-z40`.
  - `Web-Core-B`: drzewo robocze Web-Core na gałęzi `praca/52-sylwetki-baner`. Po usunięciu `git worktree prune`; 3 stashe zostały w Web-Core.
  - `IM-Website-test` (953 MB): pierwsza próba strony z 24.10–2.11. Repozytorium `Avean/IM-Website-test` zostało na GitHubie.
- **Na stałe** (ścieżki za długie dla Kosza): `tresci`, `tresci-B`, `tresci-C`.
  - Przepadły tylko commit „Aktualność 2026-11-16: usunięty pusty załącznik” z 18.11 i stash z kopią kierunku testowego.
  - Commity zlecenia 40 z tych kopii są w `main` pod innymi numerami.
- **Zostało:** 19 plików w `tresci-B` i `tresci-C` (zbudowane kopie strony z testów zleceń 44–59). Należą do konta piaskownicy Codex (`CodexSandboxOffline`), a konto właściciela nie ma do nich praw. Właściciel usuwa je sam w PowerShellu uruchomionym jako administrator (przejęcie własności).
- **Nietknięte:** Web-Core i inne projekty właściciela (HeidelbergResearch, Reaction-Diffusion-Laboratory, SourceDensity, TestXIV, XIVFPDEv2).

## Na później (dokładne sprzątanie)
- Drzewa robocze Web-Core poza folderem Github (odłączone HEAD): `C:\Users\Szymek\source\wc28` i `C:\Users\Szymek\source\Web-Core-porzadki`.
- Repozytorium `Avean/IM-Website-test` na GitHubie. Może je usunąć tylko właściciel; Claude Code nie ma uprawnienia `delete_repo`.
