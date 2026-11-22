# Web-Zlecenia — historia zleceń strony IM UWr

Changelog pracy nad stroną Instytutu Matematycznego UWr: zlecenia, dziennik i raporty. Repozytorium jest publiczne, ale jego treść
**nie trafia na stronę**. Kod strony jest w [IM-UWr/Web-Core](https://github.com/IM-UWr/Web-Core). Nie zapisuj tu haseł, tokenów ani prywatnych danych.

## Co tu jest
- `zlecenia/NN-*.md` — zlecenia w kolejności numerów. Wykonane mają w tytule „WYKONANE”. `zasady.md` to wspólne zasady; `NN-zalaczniki/` to załączniki;
  `agentow-i-czesciowe/` to zlecenia agentów z 1–5.11 i częściowa praca nad trybem ciemnym.
- `dziennik.md` — wpis po każdym zleceniu (co zrobiono, commity, sprawdzenie).
- `raporty/` — raporty zleceń (`RAPORT-*.md`, `PYTANIA.md`). Dawne zrzuty z testów nie są przechowywane.
- `prototypy/` — prototypy z rozmowy w claude.ai (HTML, skrypty, obrazy), do których odwołują się zlecenia.
- `START-*.md`, `PODSUMOWANIE-*.md`, `przekazanie-im-uwr.md`, `pola-do-cms.md`, `podglad.yml` — dokumenty przekazania i stanu projektu.

## Jak z tym pracować
To repozytorium jest sklonowane do folderu `.przekazanie/` wewnątrz Web-Core (Web-Core go ignoruje, wpis w `.gitignore`):

```
git clone https://github.com/IM-UWr/Web-Zlecenia.git .przekazanie
```

- **Na początku pracy:** `git -C .przekazanie pull --ff-only`. Nowe zlecenie może przyjść prosto na GitHub
  (np. „Add file → Upload files” do `zlecenia/` w przeglądarce, z dowolnego komputera).
- **Po zapisaniu** zlecenia, wpisu w dzienniku albo raportu: commit i push w `.przekazanie`, od razu.
- Nic z tego repozytorium nie trafia do Web-Core ani na stronę.
