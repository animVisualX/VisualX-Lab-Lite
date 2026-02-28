import streamlit as _s
import streamlit.components.v1 as _c

_s.set_page_config(page_title="VisualX | Double Pendulum", layout="wide")

_s.markdown("<style>header,footer,.stDeployButton,[data-testid='stToolbar'],[data-testid='stSidebar']{display:none !important;}body,[data-testid='stAppViewContainer']{background-color:#050505 !important;color:#fff;font-family:'Inter',sans-serif;}.t_c{border-left:3px solid #00FFFF;padding-left:20px;margin:20px 0 30px 0;}.m_t{font-family:'Courier New',monospace;font-size:2.2rem;letter-spacing:2px;text-transform:uppercase;color:#fff;}.stSlider label{color:#ccc !important;font-family:'Courier New',monospace;text-transform:uppercase;font-size:0.75rem;}.w_m{position:fixed;bottom:20px;right:20px;font-family:'Courier New',monospace;color:#666;font-size:0.9rem;z-index:9999;pointer-events:none;}</style><div class='w_m'>@anim.VisualX</div><div class='t_c'><h1 class='m_t'>Double Pendulum</h1></div>", unsafe_allow_html=True)

_c1, _c2, _c3 = _s.columns(3)
with _c1:
    _m1 = _s.slider("Mass Upper (m1)", 5.0, 50.0, 20.0, 1.0)
    _m2 = _s.slider("Mass Lower (m2)", 5.0, 50.0, 20.0, 1.0)
with _c2:
    _l1 = _s.slider("Length Upper (l1)", 50.0, 250.0, 200.0, 1.0)
    _l2 = _s.slider("Length Lower (l2)", 50.0, 250.0, 200.0, 1.0)
with _c3:
    _g = _s.slider("Gravity", 0.1, 2.5, 1.2, 0.01)
    _tr = _s.slider("Trace History", 100, 3000, 1500, 50)

_js = "<div id='wC' style='width:100%;height:85vh;overflow:hidden;position:relative;background:#050505;'><canvas id='pC'></canvas></div><script>const c=document.getElementById('pC'),x=c.getContext('2d');let w,h,r1=V_L1,r2=V_L2,m1=V_M1,m2=V_M2,g=V_G,a1=Math.PI/2.2,a2=Math.PI/2.5,v1=0,v2=0,p=[],mp=V_TR;function r(){const e=document.getElementById('wC');w=c.width=e.offsetWidth;h=c.height=e.offsetHeight;}window.addEventListener('resize',r);r();function A(){for(let i=0;i<3;i++){let n1=-g*(2*m1+m2)*Math.sin(a1),n2=-m2*g*Math.sin(a1-2*a2),n3=-2*Math.sin(a1-a2)*m2,n4=v2*v2*r2+v1*v1*r1*Math.cos(a1-a2),d=r1*(2*m1+m2-m2*Math.cos(2*a1-2*a2)),A1=(n1+n2+n3*n4)/d;n1=2*Math.sin(a1-a2);n2=(v1*v1*r1*(m1+m2));n3=g*(m1+m2)*Math.cos(a1);n4=v2*v2*r2*m2*Math.cos(a1-a2);d=r2*(2*m1+m2-m2*Math.cos(2*a1-2*a2));let A2=(n1*(n2+n3+n4))/d;v1+=A1*0.2;v2+=A2*0.2;a1+=v1;a2+=v2;}let x1=r1*Math.sin(a1),y1=r1*Math.cos(a1),x2=x1+r2*Math.sin(a2),y2=y1+r2*Math.cos(a2);p.push({x:x2,y:y2});if(p.length>mp)p.shift();x.fillStyle='#050505';x.fillRect(0,0,w,h);const tl=r1+r2,pd=120,ah=h-pd*2,sc=Math.min(1.0,ah/(tl*2));x.save();x.translate(w/2,h/2-20);x.scale(sc,sc);x.beginPath();x.lineWidth=1.5/sc;x.strokeStyle='#00FFFF';for(let i=1;i<p.length;i++){x.moveTo(p[i-1].x,p[i-1].y);x.lineTo(p[i].x,p[i].y);}x.stroke();x.strokeStyle='#FFFFFF';x.lineWidth=3/sc;x.lineCap='round';x.beginPath();x.moveTo(0,0);x.lineTo(x1,y1);x.lineTo(x2,y2);x.stroke();x.beginPath();x.arc(0,0,8/sc,0,Math.PI*2);x.fillStyle='#444444';x.fill();x.beginPath();x.arc(0,0,4/sc,0,Math.PI*2);x.fillStyle='#FFFFFF';x.fill();x.fillStyle='#FF007F';x.beginPath();x.arc(x1,y1,8/sc,0,Math.PI*2);x.fill();x.beginPath();x.arc(x2,y2,10/sc,0,Math.PI*2);x.fill();x.restore();requestAnimationFrame(A);}A();</script><style>body{margin:0;overflow:hidden;}</style>"

_h = _js.replace("V_L1", str(_l1)).replace("V_L2", str(_l2)).replace("V_M1", str(_m1)).replace("V_M2", str(_m2)).replace("V_G", str(_g)).replace("V_TR", str(_tr))

_c.html(_h, height=800)
