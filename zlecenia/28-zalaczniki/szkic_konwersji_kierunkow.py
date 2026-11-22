#!/usr/bin/env python3
"""Szkic konwersji kierunków (zlecenie 28) — WZÓR, nie gotowy skrypt.

Czyta stary plik kierunku (src/content/kierunki/<id>.md, pola YAML) i wypisuje:
  1) nowy plik treści  (nazwa, nazwa_en, tresc_en we front matter + Treść PL jako body),
  2) plik banera       (nadtytuł, zdanie, hasło, liczby),
  3) przypomnienia     (pozycje „terminy” z przypomnienie: true),
  4) pozycję listy menu i kafelków (do Web-Ustawienia).

Pokazuje docelowy format Markdownu. Claude Code pisze właściwy skrypt sam (może w TS, żeby użyć
tytulyEn() z src/lib/osoby.ts) i sprawdza go porównaniem stron przed i po.

Uruchomienie:  python -I szkic_konwersji_kierunkow.py <stary-plik.md> <katalog-wyjściowy>
"""
import json
import re
import sys
from pathlib import Path

import yaml

TWARDE = '  \n'  # złamanie linii (Shift+Enter) — tak zapisuje je edytor Pages CMS (TipTap)


def val(o, pole, en):
    """Wartość w języku; po angielsku pusta → polska (jak wybierz() w src/lib/i18n.ts)."""
    if en:
        v = o.get(pole + '_en')
        if v not in (None, ''):
            return v
    return o.get(pole)


def tytuly_en(t):
    """Port tytulyEn() z src/lib/osoby.ts (do nazwisk w kontaktach po angielsku)."""
    przed = r'(^|[\s,;(])'
    t = re.sub(r'(?:prof\.\s*)?dr\s+hab\.(?:\s*inż\.)?\s+([^,;]+?),\s*prof\.\s*UWr', r'Prof. \1', t, flags=re.I)
    t = re.sub(r'dr\s+hab\.(?:\s*inż\.)?,\s*prof\.\s*UWr\s+', 'Prof. ', t, flags=re.I)
    t = re.sub(r'prof\.\s*dr\s+hab\.(?:\s*inż\.)?', 'Prof.', t, flags=re.I)
    t = re.sub(r',\s*prof\.\s*UWr', '', t, flags=re.I)
    t = re.sub(przed + r'prof\.\s+', r'\1Prof. ', t, flags=re.I)
    t = re.sub(r'dr\s+hab\.(?:\s*inż\.)?', 'Dr hab.', t, flags=re.I)
    t = re.sub(przed + r'dr\.?\s+inż\.\s+', r'\1Dr ', t, flags=re.I)
    t = re.sub(przed + r'dr\.?\s+', r'\1Dr ', t, flags=re.I)
    t = re.sub(przed + r'mgr\.?(?:\s+inż\.)?\s+', r'\1', t, flags=re.I)
    t = re.sub(przed + r'inż\.\s+', r'\1', t, flags=re.I)
    return t


def linia(s):
    """Tekst pola w jednej linii (pola „text” bywają wielolinijkowe)."""
    return re.sub(r'\s*\n\s*', ' ', str(s or '')).strip()


def komorka(s):
    return linia(s).replace('|', '\\|')


def punkt(prefiks, linie):
    """Punkt listy: pierwsza linia po prefiksie, kolejne po Shift+Enter, wcięte pod tekst punktu."""
    wciecie = ' ' * len(prefiks)
    linie = [l for l in linie if l]
    return prefiks + (TWARDE + wciecie).join(linie)


def link(nazwa, adres):
    return f'[{linia(nazwa)}]({adres})'


def tresc(d, en, body_pl):
    T = (lambda pl, ang: ang if en else pl)
    w = (lambda o, pole: val(o, pole, en))
    etapy = d.get('etapy') or []
    stopnie = {e.get('stopien') for e in etapy}
    doktorat = stopnie == {'III'}
    out = []

    def sekcja(h):
        out.append(f'## {h}\n')

    # O kierunku
    sekcja(T('O Kolegium Doktorskim', 'About the Doctoral College') if doktorat else T('O kierunku', 'About'))
    tekst = (d.get('tresc_en') if en and d.get('tresc_en') else body_pl).strip()
    out.append(tekst + '\n')

    # Strony szkoły doktorskiej (pole „przyciski” wyświetla się dziś tylko tam)
    if doktorat and d.get('przyciski'):
        sekcja(T('Strony szkoły doktorskiej', 'Doctoral school pages'))
        out.append('\n'.join('- ' + link(w(p, 'etykieta'), p['adres']) for p in d['przyciski']) + '\n')

    # Dlaczego warto → kafelki (pogrubiony początek punktu)
    if d.get('dlaczego'):
        sekcja(T('Dlaczego warto', 'Why join'))
        out.append('\n'.join(f"- **{linia(w(x, 'tytul'))}** — {linia(w(x, 'opis'))}" for x in d['dlaczego']) + '\n')

    # Przebieg → oś (lista numerowana, „Etykieta: Tytuł” pogrubione)
    if etapy:
        sekcja(T('Od rekrutacji do obrony', 'From admission to defence') if doktorat
               else T('Jak wyglądają studia', 'How the studies work'))
        sciezki = [('I', T('Studia I stopnia (licencjackie)', "Bachelor's studies")),
                   ('II', T('Studia II stopnia (magisterskie)', "Master's studies")),
                   ('III', T('Kształcenie w szkole doktorskiej', 'Doctoral training'))]
        for st, h in sciezki:
            lista = [e for e in etapy if e.get('stopien') == st]
            if not lista:
                continue
            if not doktorat:
                out.append(f'### {h}\n')
            pozycje = []
            for i, e in enumerate(lista, 1):
                pierwsza = f"**{linia(w(e, 'kiedy'))}: {linia(w(e, 'tytul'))}**"
                if e.get('opis'):
                    pierwsza += ' — ' + linia(w(e, 'opis'))
                reszta = []
                if e.get('termin'):
                    reszta.append(f"{T('Termin', 'Deadline')}: {linia(w(e, 'termin'))}")
                if e.get('formularz') and not e.get('formularz_adres'):
                    reszta.append(f"{T('Formularz', 'Form')}: {linia(w(e, 'formularz'))}")
                if e.get('formularz') and e.get('formularz_adres'):
                    reszta.append(link(w(e, 'formularz'), e['formularz_adres']))
                pozycje.append(punkt(f'{i}. ', [pierwsza] + reszta))
            out.append('\n'.join(pozycje) + '\n')
        if d.get('_id') == 'matematyka':  # dziś wpisane w kod (linkDyplom), teraz zwykłe zdanie edytora
            out.append(T('Szczegóły egzaminów i prac dyplomowych: ', 'Exams and theses in detail: ')
                       + link(T('Egzaminy i dyplom', 'Exams and diploma'), '/studia/egzaminy-i-dyplom') + '.\n')

    # Specjalności → sam nagłówek; kafelki wstawia strona (kotwica)
    if not doktorat:
        sekcja(T('Specjalności', 'Specialisations'))

    # Terminy → tabela
    if d.get('terminy'):
        sekcja(T('Terminy', 'Deadlines') if doktorat else T('Terminy i formularze', 'Deadlines and forms'))
        jest_form = any(x.get('formularz') for x in d['terminy'])
        nag = [T('Sprawa', 'What'), T('Kogo dotyczy', 'Who'), T('Termin', 'Deadline')] + ([T('Formularz', 'Form')] if jest_form else [])
        wiersze = ['| ' + ' | '.join(nag) + ' |', '|' + ' --- |' * len(nag)]
        for x in d['terminy']:
            r = [komorka(w(x, 'co')), komorka(w(x, 'kogo')), komorka(w(x, 'termin'))]
            if jest_form:
                f = w(x, 'formularz') or ''
                r.append(link(f, x['formularz_adres']) if f and x.get('formularz_adres') else komorka(f))
            wiersze.append('| ' + ' | '.join(r) + ' |')
        out.append('\n'.join(wiersze) + '\n')
        if not doktorat:
            out.append(T('Wszystkie formularze i zasady rejestracji: ', 'All forms and registration rules: ')
                       + link(T('Zajęcia i konsultacje', 'Classes and office hours'), '/studia/zajecia') + '.\n')

    # Program → kotwica: ### w tej sekcji to zakładki (bez wyboru roku — decyzja 7.11)
    if d.get('programy'):
        sekcja(T('Program kształcenia', 'Programme') if doktorat else T('Program studiów', 'Curriculum'))
        for p in d['programy']:
            if len(d['programy']) > 1:
                out.append(f"### {linia(w(p, 'nazwa'))}\n")
            if p.get('dotyczy'):
                out.append(linia(w(p, 'dotyczy')) + '\n')
            pozycje = []
            for x in p.get('dokumenty') or []:
                s = '- ' + link(w(x, 'nazwa'), x.get('wgraj') or x.get('plik'))
                if x.get('opis'):
                    s += ' — ' + linia(w(x, 'opis'))
                pozycje.append(s)
            out.append('\n'.join(pozycje) + '\n')

    # Praktyki
    if d.get('praktyki'):
        sekcja(T('Praktyki pedagogiczne', 'Teaching placements'))
        out.append(str(w(d, 'praktyki')).strip() + '\n')
        if d.get('praktyki_dokumenty'):
            out.append('\n'.join('- ' + link(w(x, 'nazwa'), x.get('wgraj') or x.get('plik')) for x in d['praktyki_dokumenty']) + '\n')

    # Po studiach
    if d.get('kariera'):
        sekcja(T('Po studiach', 'After graduation'))
        out.append(str(w(d, 'kariera')).strip() + '\n')

    # Pytania → ### pytanie zakończone „?”
    if d.get('faq'):
        sekcja(T('Najczęstsze pytania', 'Frequently asked questions') if doktorat else T('Pytania i odpowiedzi', 'FAQ'))
        for f in d['faq']:
            out.append(f"### {linia(w(f, 'pytanie'))}\n")
            out.append(str(w(f, 'odpowiedz')).strip() + '\n')

    # Kontakt → *rola*, **osoba**, pary
    if d.get('kontakt'):
        sekcja(T('Kontakt', 'Contact'))
        pozycje = []
        for k in d['kontakt']:
            osoba = linia(k.get('osoba'))
            if en:
                osoba = tytuly_en(osoba)
            linie = [f"*{linia(w(k, 'rola'))}*", f'**{osoba}**']
            if k.get('email'):
                linie.append(f"e-mail: [{k['email']}](mailto:{k['email']})")
            if k.get('telefon'):
                linie.append(f"{T('tel.', 'phone')}: {k['telefon']}")
            if k.get('pokoj'):
                linie.append(f"{T('pokój', 'room')}: {k['pokoj']}")
            pozycje.append(punkt('- ', linie))
        out.append('\n'.join(pozycje) + '\n')

    # Akty prawne → lista linków (pliki)
    if d.get('akty'):
        sekcja(T('Akty prawne i regulaminy', 'Regulations') if doktorat else T('Akty prawne', 'Regulations'))
        out.append('\n'.join('- ' + link(w(x, 'nazwa'), x.get('wgraj') or x.get('plik')) for x in d['akty']) + '\n')

    return '\n'.join(out).rstrip() + '\n'


def main(sciezka, cel):
    tekst = Path(sciezka).read_text(encoding='utf-8')
    _, fm, body = tekst.split('---', 2)
    d = yaml.safe_load(fm)
    d['_id'] = Path(sciezka).stem
    cel = Path(cel)
    cel.mkdir(parents=True, exist_ok=True)

    pl = tresc(d, False, body)
    en = tresc(d, True, body)
    front = {'nazwa': d['nazwa'], 'nazwa_en': d.get('nazwa_en'), 'tresc_en': en}
    (cel / f"{d['_id']}.md").write_text(
        '---\n' + yaml.safe_dump(front, allow_unicode=True, sort_keys=False, width=10**6) + '---\n\n' + pl,
        encoding='utf-8')

    baner = {k: d.get(k) for k in ('podtytul', 'podtytul_en', 'opis', 'opis_en', 'haslo', 'haslo_en') if d.get(k)}
    baner['liczby'] = d.get('fakty') or []
    (cel / f"{d['_id']}.baner.json").write_text(json.dumps(baner, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    przyp = [{'sprawa': t['co'], 'sprawa_en': t.get('co_en'), 'data': str(t['data']), 'co_roku': t.get('co_roku', True),
              'dni_przed': t.get('dni_przed', 14), 'adres': f"/studia/{d['_id']}#terminy"}
             for t in d.get('terminy') or [] if t.get('przypomnienie') and t.get('data')]
    menu = {k: d.get(k) for k in ('kolejnosc', 'w_menu', 'menu_etykieta', 'menu_etykieta_en', 'menu_opis', 'menu_opis_en',
                                   'na_stronie_glownej', 'kafelek_poziom', 'kafelek_poziom_en', 'kafelek_opis', 'kafelek_opis_en')
            if d.get(k) is not None}
    menu['adres'] = f"/studia/{d['_id']}"
    (cel / f"{d['_id']}.przypomnienia-i-menu.json").write_text(
        json.dumps({'przypomnienia': przyp, 'menu_i_kafelek': menu}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
