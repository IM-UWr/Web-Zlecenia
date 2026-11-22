(function(){
  var hdr=document.querySelector('.hdr'); if(!hdr) return;
  var MQ=matchMedia('(max-width: 760px)');
  var okl=document.querySelector('.z-okladka'), baner=document.querySelector('.z-nagl'), stopka=document.querySelector('.z-stopka');
  var panel=document.getElementById((hdr.querySelector('[data-z-menu-otworz]')||{getAttribute:function(){return ''}}).getAttribute('aria-controls')||'');
  var pod=function(el,h){ if(!el) return false; var r=el.getBoundingClientRect(); return r.top<=h && r.bottom>h; };
  function ustaw(){
    if(!MQ.matches) return;
    var h=hdr.offsetHeight, y=window.scrollY, ciemny, przew;
    if(okl){ ciemny=pod(okl,h); przew=false; }
    else if(baner){ ciemny=pod(baner,h)||pod(stopka,h); przew=y>h; }
    else { przew=y>2; ciemny=!przew||pod(stopka,h); hdr.classList.add('bez-rozmycia'); }
    hdr.classList.toggle('przewiniety',przew);
    hdr.classList.toggle('jasny',!ciemny);
    if(panel) panel.classList.toggle('z-menu-jasny',!ciemny);
  }
  var rama=0;
  addEventListener('scroll',function(){cancelAnimationFrame(rama);rama=requestAnimationFrame(ustaw)},{passive:true});
  addEventListener('resize',ustaw);
  ustaw(); window.__ustawPasek=ustaw;
})();
