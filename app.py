import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="ImmoPro App", layout="wide")

class ImmoProPDF(FPDF):
    def header(self):
        self.set_fill_color(0, 35, 75)
        self.rect(0, 0, 210, 35, 'F')
        self.set_font('Arial', 'B', 15)
        self.set_text_color(255, 255, 255)
        self.set_y(12)
        self.cell(0, 10, 'IMMOPRO - DOSSIER EXPERT', 0, 1, 'C')

def generate_pdf(data):
    pdf = ImmoProPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.ln(40)
    pdf.cell(0, 10, f"PROJET : {data['adresse']}", 0, 1)
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Surface : {data['surface']} m2", 0, 1)
    pdf.cell(0, 10, f"Marge estimee : {data['marge']:,} euros", 0, 1)
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Note de l'expert : {data['note']}")
    # Correction ici pour la compatibilité totale
    return pdf.output()

# --- INTERFACE ---
st.title("🚀 Mon Application ImmoPro")

adresse = st.text_input("Adresse", "15 Le Bourg, Jugazan")
surface = st.number_input("Surface (m2)", value=3124)
prix = st.number_input("Prix", value=150000)
note = st.text_area("Note", "Opportunite exceptionnelle...")

# Calcul simple
marge = (surface * 0.3 * 2800) - prix - (surface * 0.3 * 1750)

if st.button("GÉNÉRER LE PDF"):
    data = {"adresse": adresse, "surface": surface, "marge": marge, "note": note}
    pdf_out = generate_pdf(data)
    
    # Utilisation de bytes() pour s'assurer que Streamlit accepte le flux
    st.download_button(
        label="📥 TELECHARGER MAINTENANT",
        data=bytes(pdf_out),
        file_name="Dossier_ImmoPro.pdf",
        mime="application/pdf"
    )
