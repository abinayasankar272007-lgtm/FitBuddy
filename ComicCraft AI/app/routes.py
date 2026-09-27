from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import random, os

router = APIRouter()

class ComicRequest(BaseModel):
    story: str
    character: str
    setting: str
    tone: str
    artstyle: str

def make_image(panel_no):
    # Stable matching images - college network la kooda block aagathu!
    images = {
        1: "https://images.unsplash.com/photo-1481627834876-b7833e8f5570", # library laptop
        2: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3", # shocked laptop
        3: "https://images.unsplash.com/photo-1523240795612-9a054b0db644", # confused
        4: "https://images.unsplash.com/photo-1515879218367-8466d910aaa4", # typing
        5: "https://images.unsplash.com/photo-1529156069898-49953e39b3ac" # happy friends
    }
    base = images.get(panel_no, images[1])
    return f"{base}?auto=format&fit=crop&w=900&q=80&sig={random.randint(1,99999)}"

def ensure_files():
    base = os.path.dirname(__file__)
    home_path = os.path.join(base, "home.html")
    comic_path = os.path.join(base, "comic.html")
    with open(home_path, "w", encoding="utf-8") as f:
        f.write("""<html><head><title>ComicCraft AI</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',Arial}
body{min-height:100vh;background:linear-gradient(135deg,#667eea 0%,#764ba2 25%,#f093fb 50%,#f5576c 75%,#4facfe 100%);background-size:400% 400%;animation:grad 12s ease infinite;display:flex;justify-content:center;align-items:center;padding:20px}
@keyframes grad{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.card{width:100%;max-width:620px;background:rgba(255,255,255,0.95);backdrop-filter:blur(20px);border-radius:28px;padding:38px 32px;box-shadow:0 20px 60px rgba(0,0,0,0.3);animation:pop 0.6s}
@keyframes pop{0%{transform:scale(0.9) translateY(30px);opacity:0}100%{transform:scale(1) translateY(0);opacity:1}}
.header{text-align:center;margin-bottom:28px}.logo{font-size:46px}
.header h1{font-size:32px;font-weight:800;background:linear-gradient(135deg,#667eea,#764ba2);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.tag{font-size:13px;color:#6b7280;margin-top:4px;font-weight:600}
.team{background:linear-gradient(135deg,#f3f0ff,#fce7f3);border:1px dashed #c4b5fd;border-radius:12px;padding:10px 14px;margin-top:14px;font-size:11.5px;color:#6d28d9;font-weight:700;text-align:center}
label{font-size:12px;font-weight:700;color:#374151;margin-top:18px;display:flex;align-items:center;gap:6px;text-transform:uppercase}
input,select,textarea{width:100%;padding:13px 15px;border-radius:14px;border:2px solid #e5e7eb;margin-top:7px;font-size:14px;background:#f9fafb;outline:none}
input:focus,select:focus,textarea:focus{border-color:#8b5cf6;background:white;box-shadow:0 0 0 4px rgba(139,92,246,0.15)}
.row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.btn{width:100%;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:16px;border:none;border-radius:14px;margin-top:26px;font-weight:800;font-size:16px;cursor:pointer;box-shadow:0 8px 20px rgba(102,126,234,0.4)}
.btn:hover{transform:translateY(-2px)}
</style></head><body>
<div class="card">
<div class="header"><div class="logo">🎨📚✨</div><h1>ComicCraft AI</h1><div class="tag">Turn Your Story Into 5 Panel Magic Comic</div>
<div class="team">👩‍💻 Team: Abinaya | Kaviya T | Kaviya B | Vasumithra</div></div>
<label>📝 Story Plot</label><textarea id="story" rows="3">a girl finds a computer that shows tomorrow news</textarea>
<label>🦸 Character Name</label><input id="character" value="Anu">
<div class="row"><div><label>🏫 Setting</label><select id="setting"><option>College</option><option>School</option><option>Home</option><option>City Library</option><option>Space Lab</option></select></div>
<div><label>🎭 Tone</label><select id="tone"><option>Funny</option><option selected>Mystery</option><option>Adventure</option><option>Emotional</option></select></div></div>
<label>🎨 Art Style</label><select id="artstyle"><option selected>Anime</option><option>HD Realistic</option><option>Cartoon</option><option>Comic Book</option></select>
<button class="btn" onclick="generate()">🚀 Generate 5 Panel Comic</button></div>
<script>
function generate(){
var s=document.getElementById('story').value;var c=document.getElementById('character').value;var se=document.getElementById('setting').value;var t=document.getElementById('tone').value;var a=document.getElementById('artstyle').value;
localStorage.setItem('comic_data', JSON.stringify({story:s,character:c,setting:se,tone:t,artstyle:a}));window.location.href='/comic';
}
</script></body></html>""")
    with open(comic_path, "w", encoding="utf-8") as f:
        f.write("""<html><head><title>Your Comic</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*{font-family:'Poppins',Arial}body{background:#0a0a0f;color:white;margin:0;padding:0}
.container{max-width:880px;margin:0 auto;padding:24px}
.top{text-align:center;padding:20px 0}.top h1{font-size:28px;background:linear-gradient(135deg,#f093fb,#f5576c);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.panel{margin-top:28px;background:#16161e;border-radius:20px;overflow:hidden;border:1px solid #2a2a3a}
.panel img{width:100%;height:540px;object-fit:cover;background:#1e1e2a;display:block}
.title{color:#fbbf24;padding:16px 18px 0 18px;font-weight:700;font-size:18px}
.char{background:#000;padding:16px 18px;font-size:14.5px;line-height:1.8}
.btns{text-align:center;margin:36px}.btns button{padding:13px 30px;border-radius:12px;border:none;font-weight:700;cursor:pointer;margin:6px}
.yellow{background:#fbbf24;color:#000}.white{background:white;color:#000}
</style></head><body>
<div class="container">
<div class="top"><h1>🎉 Your Comic is Ready da! 🎉</h1><p style="color:#888;font-size:13px">Tanglish dialogues + matching images</p></div>
<div id="result"><h3 style="text-align:center;margin-top:70px;color:#aaa">✨ Creating magic... 3 sec da...</h3></div>
</div>
<script>
async function load(){
var info=JSON.parse(localStorage.getItem('comic_data'));
var res=await fetch('/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(info)});
var result=await res.json();
var html='';
for(var i=0;i<result.panels.length;i++){
var p=result.panels[i];
html+='<div class="panel"><div class="title">Panel '+(i+1)+': '+p.title+'</div><img src="'+p.image+'"><div class="char"><b>🦸 '+info.character+' - </b>'+p.dialogue+'<br><span style="color:#9ca3af">📖 '+p.narration+'</span></div></div>';
}
html+='<div class="btns"><button class="yellow" onclick="window.print()">📄 Download PDF</button><button class="white" onclick="window.location.href=&quot;/&quot;">🏠 Back to Home</button></div>';
document.getElementById('result').innerHTML=html;
}
load();
</script></body></html>""")

ensure_files()

@router.get("/", response_class=HTMLResponse)
def home():
    path = os.path.join(os.path.dirname(__file__), "home.html")
    with open(path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@router.get("/comic", response_class=HTMLResponse)
def comic_page():
    path = os.path.join(os.path.dirname(__file__), "comic.html")
    with open(path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@router.post("/generate")
def generate(data: ComicRequest):
    char = data.character or "Anu"
    setting = data.setting or "College"
    tone = data.tone or "Mystery"

    # TANGLISH DIALOGUES - ipo sema local ah irukkum!
    panels = [
        {
            "title": "The Discovery",
            "dialogue": f"{char}: Dei! Enna da ithu? {setting} library la oru pudhusa laptop irukku! Yaarachum maranthutangala? Naan eduthu paakava?",
            "narration": f"{setting} la {char} oru mysterious laptop ah paarkura. Athu tomorrow news kaamikuthu nu therila."
        },
        {
            "title": "The Shock",
            "dialogue": f"{char}: Ayyo kadavule! Enna ithu! Nalaiku nadakura news ellam ipo-ve kaamikuthu! Exam cancel, function cancel nu varuthu! Bayama irukku da!",
            "narration": f"{char} laptop ah open pannathum, naalaiku nadakura visayangal ellam shock ah varuthu."
        },
        {
            "title": "The Confusion",
            "dialogue": f"{char}: Ipo enna panrathu? Miss kitta sollava? Illa friends kitta sollava? Yaarum namba matanga da... Enna panna?",
            "narration": f"{char} romba confuse aagura, yaar kitta sollanum nu therila."
        },
        {
            "title": "The Decision",
            "dialogue": f"{char}: Illa da, summa irukka koodathu! Naan intha future ah maathanum! En friends ah, {setting} ah naan dhaan kaapathanum!",
            "narration": f"{char} thairiyama future ah maatha mudivu panra."
        },
        {
            "title": "The Happy Ending",
            "dialogue": f"{char}: Yes da! Panniten! Future ah maathiten! Ipo ellarum happy da! Naan dhaan heroine da! Semma happy!",
            "narration": f"Happy {tone} ending - {char} future ah maathi ellarayum happy aakkura in {setting}."
        }
    ]
    result=[]
    for i,p in enumerate(panels,1):
        result.append({"panel":i,"title":p["title"],"dialogue":p["dialogue"],"narration":p["narration"],"image":make_image(i)})
    return {"panels":result}