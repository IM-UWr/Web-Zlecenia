(function(){
  if(!matchMedia('(hover: none) and (pointer: coarse)').matches) return;
  var okl=document.querySelector('.z-okladka'), ob=document.getElementById('szybki-dostep'), H=document.documentElement, hdr=document.querySelector('.hdr');
  if(!okl||!ob) return;
  var CISZA=400, ost=-1e9, palec=false, schowana=false, t=0;
  var Y1=function(){return Math.round(ob.getBoundingClientRect().top+scrollY-(hdr?hdr.offsetHeight:0))};
  function schowaj(){var d=Y1();if(d<=0)return;var y=scrollY;H.classList.add('bez-okladki');scrollTo({top:Math.max(0,y-d),behavior:'instant'});schowana=true;window.__chow=(window.__chow||0)+1}
  function pokaz(){var y=scrollY;H.classList.remove('bez-okladki');schowana=false;scrollTo({top:y+Y1(),behavior:'instant'});window.__pok=(window.__pok||0)+1}
  function spokoj(){if(palec||schowana)return;if(scrollY>=Y1()-1)schowaj()}
  function pozniej(){clearTimeout(t);t=setTimeout(spokoj,150)}
  addEventListener('touchstart',function(){palec=true;clearTimeout(t);if(schowana&&scrollY<=1&&performance.now()-ost>=CISZA)pokaz()},{passive:true});
  function pusc(){palec=false;pozniej()}
  addEventListener('touchend',pusc,{passive:true});addEventListener('touchcancel',pusc,{passive:true});
  addEventListener('scroll',function(){ost=performance.now();pozniej()},{passive:true});
  addEventListener('pageshow',pozniej);pozniej();
})();
