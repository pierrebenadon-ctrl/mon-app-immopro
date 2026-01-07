import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="ImmoPro - Mémorandum Expert", layout="wide")

class ImmoProMemorandum(FPDF):
    def header(self):
        # Bandeau Bleu Nuit
        self.set_fill_color(0, 35, 75) 
        self.rect(0, 0, 210, 45, 'F')
        self.set_font('Arial', 'B', 24)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 12)
        self.cell(0, 10, 'IMMOPRO', 0, 0, 'L')
        self.set_font('Arial', '', 10)
        self.set_xy(10, 24)
        self.cell(0, 10, 'STRATEGIE & DEVELOPPEMENT FONCIER', 0, 0, 'L')
        self.set_xy(140, 15)
        self.set_font('Arial', 'I', 9)
        self.cell(60, 10, f'Dossier Expertise - {datetime.datetime.now().strftime("%d/%m/%Y")}', 0, 0, 'R')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, 'Ce document constitue une analyse pre-operationnelle confidentielle.', 0, 0, 'L')
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'R')

    def section_header(self, title):
        self.ln(5)
        self.set_font('Arial', 'B', 13)
        self.set_text_color(0, 35, 75)
        self.set_fill_color(240, 243, 246)
        self.cell(0, 10, f"  {title}", 0, 1, 'L', fill=True)
        self.ln(3)

def generate_full_pdf(data):
    pdf = ImmoProMemorandum()
    pdf.add_page()
    pdf.ln(40)

    # --- TITRE ---
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(0, 168, 107) # Vert Emeraude
    pdf.cell(0, 15, data['adresse'].upper(), 0, 1, 'L')
    pdf.set_draw_color(0, 168, 107)
    pdf.line(10, 72, 90, 72)
    pdf.ln(8)

    # --- SECTION 1 : CARACTERISTIQUES ---
    pdf.section_header("1. SYNTHESE DE L'EMPLACEMENT ET URBANISME")
    pdf.set_font('Arial', '', 11)
    pdf.set_text_color(0, 0, 0)
    
    pdf.cell(100, 8, f"Surface de la parcelle : {data['surface']} m2", 0, 0)
    pdf.cell(0, 8, f"Zonage PLU : {data['zonage']}", 0, 1)
    pdf.cell(100, 8, f"Emprise au sol (CES) : {data['ces']} %", 0, 0)
    pdf.cell(0, 8, f"Surface de Plancher (SDP) Max : {data['sdp']:.0f} m2", 0, 1)
    pdf.cell(100, 8, f"Prix de vente FAI : {data['prix_fai']:,} euros", 0, 1)
    
    # --- SECTION 2 : BILAN FINANCIER ---
    pdf.section_header("2. BILAN D'OPERATION PREVISIONNEL")
    pdf.set_font('Arial', 'B', 10)
    pdf.set_fill_color(245, 245, 245)
    pdf.cell(110, 10, "Postes de depenses et recettes", 1, 0, 'L', fill=True)
    pdf.cell(80, 10, "Valeurs estimees", 1, 1, 'C', fill=True)
    
    pdf.set_font('Arial', '', 10)
    pdf.cell(110, 9, "Chiffre d'Affaires total (Revente)", 1)
    pdf.cell(80, 9, f"{data['ca']:,.0f} euros", 1, 1, 'R')
    pdf.cell(110, 9, "Prix d'acquisition (FAI)", 1)
    pdf.cell(80, 9, f"- {data['prix_fai']:,.0f} euros", 1, 1, 'R')
    pdf.cell(110, 9, "Cout de construction estime (VRD inclus)", 1)
    pdf.cell(80, 9, f"- {data['travaux']:,.0f} euros", 1, 1, 'R')
    pdf.cell(110, 9, "Fiscalite (Taxe Amenagement + RAP)", 1)
    pdf.cell(80, 9, f"- {data['taxe']:,.0f} euros", 1, 1, 'R')
    pdf.cell(110, 9, "Frais de portage et divers (estim. 8%)", 1)
    pdf.cell(80, 9, f"- {data['frais_divers']:,.0f} euros", 1, 1, 'R')
    
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(0, 168, 107)
    pdf.cell(110, 12, "MARGE BRUTE PREVISIONNELLE", 1)
    pdf.cell(80, 12, f"{data['marge']:,.0f} euros ({data['marge_p']:.1f}%)", 1, 1, 'R')

    # --- SECTION 3 : ANALYSE SWOT ---
    pdf.section_header("3. ANALYSE STRATEGIQUE (SWOT)")
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(0, 35, 75)
    
    # On cree une petite grille SWOT
    pdf.cell(95, 8, "FORCES (+)", 1, 0, 'L', fill=True)
    pdf.cell(95, 8, "FAIBLESSES (-)", 1, 1, 'L', fill=True)
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(95, 6, "- Surface terrain rare\n- Centre-bourg accessible\n- Plat et bien expose", 1, 'L')
    pdf.set_xy(105, pdf.get_y() - 18) # On remonte pour la 2eme colonne
    pdf.multi_cell(95, 6, "- Delais ABF possibles\n- Etude de sol G1 a prevoir\n- Marche local specifique", 1, 'L')
    
    pdf.ln(2)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(0, 35, 75)
    pdf.cell(95, 8, "OPPORTUNITES", 1, 0, 'L', fill=True)
    pdf.cell(95, 8, "MENACES", 1, 1, 'L', fill=True)
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(95, 6, "- Division en 4 ou 5 lots\n- Forte demande en T4/T5\n- Valorisation architecturale", 1, 'L')
    pdf.set_xy(105, pdf.get_y() - 18)
    pdf.multi_cell(95, 6, "- Evolution reglement PLU\n- Cout materiaux fluctuant\n- Recours des tiers", 1, 'L')

    # --- SECTION 4 : NOTE DE L'EXPERT ---
    pdf.section_header("4. AVIS DE L'EXPERT")
    pdf.set_font('Arial', 'I', 11)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 7, data['note'])

    return pdf.output()

# --- INTERFACE STREAMLIT ---
st.title("💎 IMMOPRO | Business Case Generator")

col1, col2 = st.columns(2)
with col1:
    st.subheader("📍 Terrain & Prix")
    adresse = st.text_input("Adresse", "15 Le Bourg, 33420 Jugazan")
    surface = st.number_input("Surface Terrain (m²)", value=3124)
    prix_fai = st.number_input("Prix FAI (€)", value=163500)
    zonage = st.text_input("Zonage PLU", "Zone U (Urbaine)")

with col2:
    st.subheader("🏗️ Hypotheses Construction")
    ces = st.slider("Emprise au sol (CES %)", 5, 100, 30)
    prix_m2 = st.number_input("Prix Revente Neuf (€/m²)", value=2800)
    tx_frais = st.slider("Frais de portage/divers (%)", 0, 15, 8)

note_expert = st.text_area("Analyse stratégique finale :", "L'operation presente un ratio foncier/CA tres favorable. Jugazan beneficie d'un attrait croissant. Le projet de division parcellaire est a privilegier pour maximiser la rentabilite.")

# --- CALCULS ---
sdp = surface * (ces/100)
ca = sdp * prix_m2
taxe = (sdp * 1050 * 0.08) # Estimation TA+RAP
travaux = sdp * 1750 # Hypothese construction
frais_divers = ca * (tx_frais/100)
marge = ca - (prix_fai + travaux + taxe + frais_divers)
marge_p = (marge/ca)*100 if ca > 0 else 0

# --- INDICATEURS ---
st.write("---")
m1, m2, m3 = st.columns(3)
m1.metric("CA Estimé", f"{ca:,.0f} €")
m2.metric("Marge Brute", f"{marge:,.0f} €", f"{marge_p:.1f}%")
m3.metric("Taxe Aménagement est.", f"{taxe:,.0f} €")

# --- BOUTON ---
if st.button("🔥 GENERER LE MEMORANDUM COMPLET"):
    data_pdf = {
        "adresse": adresse, "surface": surface, "prix_fai": prix_fai, "ces": ces,
        "zonage": zonage, "ca": ca, "marge": marge, "marge_p": marge_p, 
        "taxe": taxe, "note": note_expert, "travaux": travaux, 
        "sdp": sdp, "frais_divers": frais_divers
    }
    output = generate_full_pdf(data_pdf)
    st.download_button(
        label="📥 TELECHARGER LE DOSSIER EXPERT",
        data=bytes(output),
        file_name=f"Memorandum_ImmoPro_{adresse.replace(' ', '_')}.pdf",
        mime="application/pdf"
    )
