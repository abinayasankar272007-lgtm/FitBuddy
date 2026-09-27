from fpdf import FPDF
from pathlib import Path
import requests, tempfile, os
from datetime import datetime

class ComicPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'ComicCraft - AI Comic Story', 0, 1, 'C')
        self.ln(2)

def save_pdf(layout, title="Comic"):
    pdf = ComicPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    for panel in layout:
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Panel {panel['panel']}: {panel['title']}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)
        img_path = None
        try:
            if panel.get("image_url"):
                resp = requests.get(panel["image_url"], timeout=25)
                if resp.status_code == 200:
                    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
                    tmp.write(resp.content)
                    tmp.close()
                    img_path = tmp.name
                    pdf.image(img_path, x=15, w=180)
                    pdf.ln(5)
        except Exception as e:
            print(e)
        pdf.set_font("Arial", "I", 11)
        pdf.multi_cell(0, 8, f"Scene: {panel['scene_description']}")
        pdf.ln(2)
        pdf.set_font("Arial", "", 12)
        safe = panel.get("story","").encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 8, safe)
        if img_path and os.path.exists(img_path):
            try: os.remove(img_path)
            except: pass
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    filename = f"comic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = output_dir / filename
    pdf.output(str(filepath))
    return str(filepath)