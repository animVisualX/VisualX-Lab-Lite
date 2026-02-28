import streamlit as _s
import streamlit.components.v1 as _c
import json as _j

_s.set_page_config(page_title="VisualX | Electronic Configuration", layout="wide")

_s.markdown("<style>header,footer,.stDeployButton,[data-testid='stToolbar'],[data-testid='stSidebar']{display:none !important;}body,[data-testid='stAppViewContainer']{background-color:#0d0d0d !important;color:#fff;font-family:'Inter',sans-serif;}.t_c{border-left:3px solid #00FFFF;padding-left:20px;margin:20px 0 20px 0;}.m_t{font-family:'Courier New',monospace;font-size:2.2rem;letter-spacing:2px;text-transform:uppercase;color:#fff;}.stSelectbox label{color:#ccc !important;font-family:'Courier New',monospace;text-transform:uppercase;font-size:0.9rem !important;}div[data-baseweb='select']{background-color:rgba(255,255,255,0.05);color:white;} /* Custom VisualX Button CSS */ .stFormSubmitButton button{width:100%;background-color:transparent !important;color:#00FFFF !important;border:1px solid #00FFFF !important;font-family:'Courier New',monospace;letter-spacing:2px;transition:0.3s;padding:10px;margin-top:28px;}.stFormSubmitButton button:hover{background-color:#00FFFF !important;color:#0d0d0d !important;box-shadow:0 0 15px #00FFFF;}</style><div class='t_c'><h1 class='m_t'>ELECTRONIC CONFIGURATION</h1></div>", unsafe_allow_html=True)

_e="Hydrogen,Helium,Lithium,Beryllium,Boron,Carbon,Nitrogen,Oxygen,Fluorine,Neon,Sodium,Magnesium,Aluminum,Silicon,Phosphorus,Sulfur,Chlorine,Argon,Potassium,Calcium,Scandium,Titanium,Vanadium,Chromium*,Manganese,Iron,Cobalt,Nickel,Copper*,Zinc,Gallium,Germanium,Arsenic,Selenium,Bromine,Krypton,Rubidium,Strontium,Yttrium,Zirconium,Niobium*,Molybdenum*,Technetium,Ruthenium*,Rhodium*,Palladium*,Silver*,Cadmium,Indium,Tin,Antimony,Tellurium,Iodine,Xenon,Cesium,Barium,Lanthanum*,Cerium*,Praseodymium,Neodymium,Promethium,Samarium,Europium,Gadolinium*,Terbium,Dysprosium,Holmium,Erbium,Thulium,Ytterbium,Lutetium,Hafnium,Tantalum,Tungsten,Rhenium,Osmium,Iridium,Platinum*,Gold*,Mercury,Thallium,Lead,Bismuth,Polonium,Astatine,Radon,Francium,Radium,Actinium*,Thorium*,Protactinium*,Uranium*,Neptunium*,Plutonium,Americium,Curium*,Berkelium,Californium,Einsteinium,Fermium,Mendelevium,Nobelium,Lawrencium*,Rutherfordium,Dubnium,Seaborgium,Bohrium,Hassium,Meitnerium,Darmstadtium,Roentgenium*,Copernicium,Nihonium,Flerovium,Moscovium,Livermorium,Tennessine,Oganesson".split(",")
_el=[f"{i+1}: {n}" for i,n in enumerate(_e)]

with _s.form("v_form"):
    _c1, _c2 = _s.columns([3,1])
    with _c1:
        _sel=_s.selectbox("SELECT ELEMENT (Z = 1 to 118)",_el,index=5)
    with _c2:
        _sub=_s.form_submit_button("RENDER ENGINE")

_z=int(_sel.split(":")[0])

def _g(z):
    _o=[("1s",2),("2s",2),("2p",6),("3s",2),("3p",6),("4s",2),("3d",10),("4p",6),("5s",2),("4d",10),("5p",6),("6s",2),("4f",14),("5d",10),("6p",6),("7s",2),("5f",14),("6d",10),("7p",6)]
    _c={}
    _r=z
    for n,c in _o:
        if _r==0:break
        f=min(_r,c)
        _c[n]=f
        _r-=f
    
    _ex={24:{"4s":1,"3d":5},29:{"4s":1,"3d":10},41:{"5s":1,"4d":4},42:{"5s":1,"4d":5},44:{"5s":1,"4d":7},45:{"5s":1,"4d":8},46:{"5s":0,"4d":10},47:{"5s":1,"4d":10},57:{"4f":0,"5d":1},58:{"4f":1,"5d":1},64:{"4f":7,"5d":1},78:{"6s":1,"5d":9},79:{"6s":1,"5d":10},89:{"5f":0,"6d":1},90:{"5f":0,"6d":2},91:{"5f":2,"6d":1},92:{"5f":3,"6d":1},93:{"5f":4,"6d":1},96:{"5f":7,"6d":1},103:{"6d":0,"7p":1},111:{"7s":1,"6d":10}}
    
    if z in _ex:
        _c.update(_ex[z])
        _c={k:v for k,v in _c.items() if v>0}
        _ok=[k for k,v in _o]
        _c={k:_c[k] for k in _ok if k in _c}
    return _c

_jc=_j.dumps(_g(_z))

_js="<div id='w' style='width:100%;height:75vh;overflow-y:auto;overflow-x:hidden;position:relative;background:#0d0d0d;'><canvas id='q'></canvas></div><script>const cv=document.getElementById('q'),cx=cv.getContext('2d'),wr=document.getElementById('w');let W=wr.offsetWidth,H=0,cE=0,mE=0;const cfg=V_JC,si={'s':{l:0,b:1},'p':{l:1,b:3},'d':{l:2,b:5},'f':{l:3,b:7}};for(let k in cfg)mE+=cfg[k];function gG(c,x,y,w,h){let g=c.createLinearGradient(x,y,x+w,y);g.addColorStop(0,'#78ffd6');g.addColorStop(0.33,'#4a00e0');g.addColorStop(0.66,'#c70039');g.addColorStop(1,'#ffb6c1');return g;}function cH(){let sx=50,c_x=sx,cy=100,bs=45,m=50;for(let[s,e]of Object.entries(cfg)){let t=s.slice(-1),nb=si[t].b,bw=nb*bs;if(c_x+bw>W-50){c_x=sx;cy+=130;}c_x+=bw+m;}return cy+300;}function rR(){W=wr.offsetWidth;H=Math.max(wr.offsetHeight,cH());let d=window.devicePixelRatio||1;cv.width=W*d;cv.height=H*d;cv.style.width=W+'px';cv.style.height=H+'px';cx.scale(d,d);}window.addEventListener('resize',rR);function dA(x,y,u){cx.beginPath();cx.strokeStyle='#FF007F';cx.lineWidth=2.5;cx.shadowBlur=8;cx.shadowColor='#FF007F';let l=22,sy=u?y+l/2:y-l/2,ey=u?y-l/2:y+l/2;cx.moveTo(x,sy);cx.lineTo(x,ey);let ho=u?6:-6;cx.moveTo(x-5,ey+ho);cx.lineTo(x,ey);cx.lineTo(x+5,ey+ho);cx.stroke();cx.shadowBlur=0;}function r(){cx.fillStyle='#0d0d0d';cx.fillRect(0,0,W,H);cx.font='bold 6vw Courier New';cx.fillStyle='rgba(255,255,255,0.02)';cx.textAlign='center';cx.textBaseline='middle';cx.fillText('@anim.VisualX',W/2,H/2);let sx=50,c_x=sx,cy=100,bs=45,m=50,gE=0,dL=Math.floor(cE);cx.textAlign='center';for(let[s,e]of Object.entries(cfg)){let t=s.slice(-1),i=si[t],nb=i.b,bw=nb*bs;if(c_x+bw>W-50){c_x=sx;cy+=130;}cx.shadowBlur=0;cx.fillStyle='#fff';cx.font='16px monospace';cx.fillText(s+' ('+e+'e⁻)',c_x+bw/2,cy+bs+25);for(let j=0;j<nb;j++){let bx=c_x+j*bs,by=cy;cx.beginPath();cx.strokeStyle='#00FFFF';cx.lineWidth=2;cx.shadowBlur=10;cx.shadowColor='#00FFFF';cx.rect(bx,by,bs,bs);cx.stroke();let ml=j-i.l;cx.shadowBlur=0;cx.fillStyle='#ccc';cx.font='12px monospace';cx.fillText((ml>0?'+':'')+ml,bx+bs/2,by-10);}for(let j=1;j<=e;j++){gE++;if(gE>dL)continue;let bI=(j<=nb)?(j-1):(j-1-nb),u=(j<=nb),bx=c_x+bI*bs,by=cy;if(u)dA(bx+bs/2-6,by+bs/2,true);else dA(bx+bs/2+6,by+bs/2,false);}c_x+=bw+m;}cx.fillStyle=gG(cx,0,cy+100,W,4);cx.fillRect(50,cy+90,W-100,4);}function A(){r();if(cE<mE)cE+=0.4;requestAnimationFrame(A);}setTimeout(()=>{rR();A();},100);</script>"

_h = _js.replace("V_JC", _jc)

_c.html(_h, height=850)
