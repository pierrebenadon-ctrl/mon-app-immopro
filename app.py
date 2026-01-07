import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURATION DE LA PAGE STREAMLIT ---
st.set_page_config(page_title="ImmoPro Premium", layout="wide")

# --- CLASSE DESIGN DU PDF ---
class ImmoProDesign(FPDF):
    def header(self):
        # Bandeau de tête Bleu Nuit
        self.set_fill_color(0, 35, 75) 
        self.rect(0, 0, 210, 40, 'F')
        
        # Texte du Header
        self.set_font('Arial', 'B', 22)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 15)
        self.cell(0, 10, 'IMMOPRO', 0, 0, 'L')
        
        self.set_font('Arial', '', 10)
        self.set_xy(10, 25)
        self.cell(0, 10, 'EXPERTISE & STRATEGIE FONCIERE', 0, 0, 'L')
        
        self.set_xy(150, 15)
        self.set_font('Arial', 'I', 9)
        self.cell(50, 10, f'Edite le {datetime.datetime.now().strftime("%d/%m/%Y")}', 0, 0, 'R')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, 'Document confidentiel genere par ImmoPro v2.0', 0, 0, 'L')
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'R')

    def section_title(self, label):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 35, 75)
        self.set_fill_color(230, 235, 240)
        self.cell(0, 10, f"  {label}", 0, 1, 'L', fill=True)
        self.ln(4)

def generate_premium_pdf(data):
    pdf = ImmoProDesign()
    pdf.add_page()
    pdf.ln(40)

    # TITRE DU PROJET
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(0, 168, 107) # Vert Émeraude
    pdf.cell(0, 15, data['adresse'].upper(), 0, 1, 'L')
    pdf.set_draw_color(0, 168, 107)
    pdf.line(10, 70, 80, 70)
    pdf.ln(10)

    # SYNTHESE
    pdf.section_title("1. SYNTHESE DE L'OPPORTUNITE")
    pdf.set_font('Arial', '', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(95, 8, f"Surface terrain : {data['surface']} m2", 0, 0)
    pdf.cell(95, 8, f"Emprise au sol (CES) : {data['ces']} %", 0, 1)
    pdf.cell(95, 8, f"Zonage : {data['zonage']}", 0, 0)
    pdf.cell(95, 8, f"Prix Net Vendeur : {data['prix_v']:,} euros", 0, 1)
    pdf.ln(8)

    # TABLEAU FINANCIER
    pdf.section_title("2. BILAN FINANCIER PREVISIONNEL")
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(100, 10, "Poste", 1, 0, 'C', fill=True)
    pdf.cell(80, 10, "Montant", 1, 1, 'C', fill=True)
    
    pdf.set_font('Arial', '', 10)
    items = [
        ("Chiffre d'Affaires total", f"{data['ca']:,.0f} euros"),
        ("Construction & Amenagements", f"{data['travaux']:,.0f} euros"),
        ("Taxes (TA + RAP)", f"{data['taxe']:,.0f} euros"),
        ("Honoraires de conseil", f"{data['honoraires']:,.0f} euros")
    ]
    for item in items:
        pdf.cell(100, 10, item[0], 1)
        pdf.cell(80, 10, item[1], 1, 1, 'R')
    
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(0, 16
