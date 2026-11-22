/* ===== Wspólny skrypt makiet: motyw, menu, wyszukiwarka, ograniczenie ruchu, nieaktywne linki ===== */
(function () {
  var R = document.documentElement;
  var KS = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg>';
  var SL = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var mq = window.matchMedia('(prefers-reduced-motion: reduce)');
  window.ustawRuch = function () {
    R.classList.toggle('rm', mq.matches || R.dataset.rm === '1');
    if (window.poRuchu) window.poRuchu();
  };
  if (mq.addEventListener) mq.addEventListener('change', window.ustawRuch);
  window.ustawRuch();
  window.ruchOgr = function () { return R.classList.contains('rm'); };

  function ikonaMotywu() {
    var d = R.dataset.theme === 'dark';
    document.querySelectorAll('[data-motyw]').forEach(function (b) {
      b.innerHTML = d ? SL : KS;
      b.setAttribute('aria-label', d ? 'Włącz tryb jasny' : 'Włącz tryb ciemny');
    });
  }
  ikonaMotywu();

  var menu = document.querySelector('.menu');
  var szukaj = document.querySelector('.szukaj');
  var ostatni = null;
  function menuOtworz(tak) {
    menu.classList.toggle('otwarte', tak);
    document.querySelectorAll('[data-menu]').forEach(function (b) { b.setAttribute('aria-expanded', tak ? 'true' : 'false'); });
    if (tak) { ostatni = document.activeElement; menu.querySelector('[data-zamknij]').focus(); }
    else if (ostatni) ostatni.focus();
  }
  function szukajOtworz(tak) {
    szukaj.classList.toggle('otwarte', tak);
    if (tak) { ostatni = document.activeElement; setTimeout(function () { szukaj.querySelector('input').focus({ preventScroll: true }); }, 30); }
    else if (ostatni) ostatni.focus();
  }
  var tid = 0;
  function toast(t) {
    var el = document.querySelector('.toast');
    el.textContent = t; el.classList.add('widac');
    clearTimeout(tid); tid = setTimeout(function () { el.classList.remove('widac'); }, 1600);
  }
  document.addEventListener('click', function (e) {
    var w = e.target.closest('.wiecej-row');
    if (w) {
      /* Jak zwykle przy „Pokaż więcej”: rozwinięcie jednej sekcji zwija pozostałe (jak „W tym dziale”), strona nie skacze.
         Przy rozwijaniu kotwicą jest ostatnia widoczna pozycja sekcji: nowe pozycje pojawiają się pod nią, a jeśli wyżej
         zwinęła się inna sekcja, przewinięcie to wyrównuje. Przy zwijaniu kotwicą jest przycisk. Fokus zostaje na przycisku. */
      var box = w.closest('.box'), tak = !box.classList.contains('rozw');
      var widoczne = box.querySelectorAll('.wyd:not(.nadmiar), .ak:not(.nadmiar), .sem:not(.nadmiar)');
      var kotwica = tak && widoczne.length ? widoczne[widoczne.length - 1] : w, y0 = kotwica.getBoundingClientRect().top;
      function ustaw(b, t) {
        b.classList.toggle('rozw', t);
        var p = b.querySelector('.wiecej-row');
        if (p) { p.setAttribute('aria-expanded', t ? 'true' : 'false'); p.querySelector('.wt').textContent = t ? 'Zwiń' : 'Zobacz więcej'; }
      }
      if (tak) document.querySelectorAll('.box.rozw').forEach(function (b) { if (b !== box) ustaw(b, false); });
      ustaw(box, tak);
      var d = kotwica.getBoundingClientRect().top - y0;
      if (Math.abs(d) > 0.5) window.scrollBy({ top: d, left: 0, behavior: 'instant' });
      if (document.activeElement !== w) w.focus({ preventScroll: true, focusVisible: false });
      return;
    }
  });
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-motyw],[data-menu],[data-szukaj],[data-zamknij],.menu-tlo,.szukaj,a');
    if (!el) return;
    if (el.matches('[data-motyw]')) { R.dataset.theme = R.dataset.theme === 'dark' ? 'light' : 'dark'; ikonaMotywu(); return; }
    if (el.matches('[data-menu]')) { menuOtworz(true); return; }
    if (el.matches('[data-szukaj]')) { szukajOtworz(true); return; }
    if (el.matches('[data-zamknij]')) { if (menu.classList.contains('otwarte')) menuOtworz(false); else szukajOtworz(false); return; }
    if (el.matches('.menu-tlo')) { menuOtworz(false); return; }
    if (el.matches('.szukaj') && e.target === el) { szukajOtworz(false); return; }
    if (el.matches('a')) {
      var h = el.getAttribute('href') || '';
      if (h.length > 1 && h.charAt(0) === '#' && document.querySelector(h)) return; /* kotwice obsługuje makieta */
      e.preventDefault();
      toast('Makieta: ' + (el.dataset.cel || 'link nieaktywny'));
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (menu.classList.contains('otwarte')) menuOtworz(false);
    else if (szukaj.classList.contains('otwarte')) szukajOtworz(false);
  });
  window.addEventListener('error', function (e) { console.error('Błąd makiety: ' + e.message); });
})();
