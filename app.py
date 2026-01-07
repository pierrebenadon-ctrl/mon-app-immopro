import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURATION STREAMLIT ---
st.set_page_config(page_title="ImmoPro Premium", layout="wide")

class ImmoProDesign(FPDF):
    def header(self):
        # Bandeau latéral ou supérieur décoratif
        self.set_fill_color(0, 35, 75)  # Bleu Nuit
        self.rect(0, 0, 210, 45, 'F')
        
        # Logo Texte (En attendant ton vrai logo)
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 15)
        self.cell(0, 10, 'IMMOPRO', 0, 0, 'L')
        
        self.set_font('Helvetica', '', 10)
        self.set_xy(10, 25)
        self.cell(0, 10, 'EXPERTISE & STRATÉGIE FONCIÈRE', 0, 0, 'L')
        
        # Date à droite
        self.set_xy(150, 15)
        self.set_font('Helvetica', 'I', 9)
        self.cell(50, 10, f'Dossier n° {datetime.datetime.now().strftime("%Y-%m")}-01', 0, 0, 'R')

    def footer(self):
        self.set_y(-20)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, 'Document strictement confidentiel - Reproduction interdite', 0, 0, 'L')
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'R')

    def section_title(self, label):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 35, 75)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 10, f"  {label}", 0, 1, 'L', fill=True)
        self.ln(4)

def create_premium_pdf(data):
    pdf = ImmoProDesign()
    pdf.add_page()
    pdf.ln(45)

    # --- TITRE DU PROJET ---
    pdf.set_font('Helvetica', 'B', 22)
    pdf.set_text_color(0, 168, 107) # Vert Émeraude
    pdf.cell(0, 15, data['adresse'].upper(), 0, 1, 'L')
    pdf.set_draw_color(0, 168, 107)
    pdf.line(11, 72, 60, 72)
    pdf.ln(10)

    # --- BLOC SYNTHÈSE ---
    pdf.section_title("SYNTHÈSE DE L'OPPORTUNITÉ")
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(50, 50, 50)
    
    col_width = 90
    pdf.cell(col_width, 8, f"Surface de la parcelle : {data['surface']} m2", 0, 0)
    pdf.cell(col_width, 8, f"Emprise au sol (CES) : {data['ces']} %", 0, 1)
    pdf.cell(col_width, 8, f"Prix de vente : {data['prix_v']:,} euros", 0, 0)
    pdf.cell(col_width, 8, f"Zonage : {data['zonage']}", 0, 1)
    pdf.ln(10)

    # --- BLOC FINANCIER (TABLEAU) ---
    pdf.section_title("BILAN FINANCIER PRÉVISIONNEL")
    pdf.set_fill_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    
    # En-tête tableau
    pdf.cell(100, 10, "Poste de dépense / Recette", 1, 0, 'L')
    pdf.cell(80, 10, "Montant estimé", 1, 1, 'C')
    
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(100, 10, "Chiffre d'Affaires (Revente)", 1, 0, 'L')
    pdf.cell(80, 10, f"{data['ca']:,.0f} euros", 1, 1, 'C')
    pdf.cell(100, 10, "Coûts de construction & VRD", 1, 0, 'L')
    pdf.cell(80, 10, f"{(data['ca'] - data['marge'] - data['prix_v']):,.0f} euros", 1, 1, 'C')
    pdf.cell(100, 10, "Taxes d'aménagement (TA/RAP)", 1, 0, 'L')
    pdf.cell(80, 10, f"{data['taxe']:,.0f} euros", 1, 1, 'C')
    
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(0, 168, 107)
    pdf.cell(100, 12, "MARGE BRUTE OPÉRATIONNELLE", 1, 0, 'L')
    pdf.cell(80, 12, f"{data['marge']:,.0f} euros ({data['marge_p']:.1f}%)", 1, 1, 'C')
    pdf.ln(10)

    # --- BLOC NOTE EXPERT ---
    pdf.section_title("OBSERVATIONS DE L'EXPERT")
    pdf.set_font('Helvetica', 'I', 11)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(0, 8, data['note'])

    return pdf.output()

# --- INTERFACE STREAMLIT ---
st.title("🚀 IMMOPRO PREMIUM")
# ... (Garde ta partie saisie de données ici) ...
# [Insère ici le formulaire de saisie du code précédent]

# Copie juste la partie bouton ci-dessous :
if st.button("💎 GÉNÉRER LE DOSSIER PREMIUM"):
    data_final = {
        "adresse": adresse, "surface": surface, "prix_v": prix_v, "ces": ces,
        "zonage": zonage_nom, "ca": ca_total, "marge": marge_brute, 
        "marge_p": marge_p, "taxe": taxe_estimee, "note": note_expert
    }
    pdf_bytes = create_premium_pdf(data_final)
    st.download_button("📥 Télécharger le Dossier Design", data=bytes(pdf_bytes), file_name="ImmoPro_Expert.pdf", mime="application/pdf")
