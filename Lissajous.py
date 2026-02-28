import streamlit as _s
import streamlit.components.v1 as _c

_s.set_page_config(page_title="VisualX Lab | Lissajous", layout="wide")

_s.markdown("<style>[data-testid='stHeader'],header,footer,[data-testid='stSidebar']{display:none !important;}.stApp,body,html{background-color:#050505 !important;color:#fff;}.block-container{padding:0 30px !important;margin:0 !important;}.l_t{font-family:'Courier New',monospace;color:#fff;font-size:1.2rem;padding:15px 0;border-left:3px solid #00FFFF;padding-left:15px;margin:20px 0 15px 0;letter-spacing:2px;}.stSlider label{color:#ccc !important;font-family:sans-serif;text-transform:uppercase;font-size:0.8rem !important;}.c_p{background:rgba(255,255,255,0.01);border:1px solid #1a1a1a;padding:15px 25px;border-radius:8px;margin:0;}.f_f{position:fixed;bottom:12px;right:25px;color:#666;font-family:monospace;font-size:0.9rem;pointer-events:none;z-index:9999;letter-spacing:1px;}</style><div class='l_t'>LISSAJOUS KINEMATICS</div><div class='f_f'>@anim.VisualX</div>", unsafe_allow_html=True)

with _s.container():
    _s.markdown("<div class='c_p'>", unsafe_allow_html=True)
    _c1, _c2 = _s.columns(2)
    with _c1: _a = _s.slider("FREQUENCY X (a)", 1, 10, 3)
    with _c2: _b = _s.slider("FREQUENCY Y (b)", 1, 10, 2)
    _s.markdown("</div>", unsafe_allow_html=True)

_js = "<div id='w' style='width:100%;height:65vh;background:#050505;overflow:hidden;margin-top:15px;border-radius:8px;'><canvas id='c' style='width:100%;height:100%;display:block;'></canvas></div><script>const c=document.getElementById('c'),x=c.getContext('2d');let w,h,t=0;function r(){const e=document.getElementById('w');w=c.width=e.offsetWidth;h=c.height=e.offsetHeight;}function l(){x.clearRect(0,0,w,h);x.strokeStyle='#111';x.lineWidth=1;for(let i=0;i<w;i+=w/20){x.beginPath();x.moveTo(i,0);x.lineTo(i,h);x.stroke();}for(let j=0;j<h;j+=h/10){x.beginPath();x.moveTo(0,j);x.lineTo(w,j);x.stroke();}x.strokeStyle='#00FFFF';x.lineWidth=2;x.shadowBlur=0;x.beginPath();const a=V_A,b=V_B,s=Math.min(w,h)*0.4,cx=w/2,cy=h/2;for(let th=0;th<=Math.PI*2;th+=0.01){let px=cx+Math.sin(a*th+t)*s,py=cy+Math.sin(b*th)*s;if(th===0)x.moveTo(px,py);else x.lineTo(px,py);}let ex=cx+Math.sin(a*Math.PI*2+t)*s,ey=cy+Math.sin(b*Math.PI*2)*s;x.lineTo(ex,ey);x.closePath();x.stroke();let tx=cx+Math.sin(t*a+t)*s,ty=cy+Math.sin(t*b)*s;x.beginPath();x.arc(tx,ty,6,0,2*Math.PI);x.fillStyle='#FF007F';x.shadowBlur=0;x.fill();t-=0.006;requestAnimationFrame(l);}window.addEventListener('resize',r);r();l();</script>"

_h = _js.replace("V_A", str(_a)).replace("V_B", str(_b))

_c.html(_h, height=600)
