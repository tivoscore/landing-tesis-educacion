import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ============================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================
st.set_page_config(
    page_title="Descarga tus Guías Gratuitas",
    page_icon="📥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# OCULTAR ELEMENTOS DE STREAMLIT
# ============================================
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none !important;}
    #MainMenu {visibility: hidden !important;}
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    .stApp > footer {display: none !important;}
    .main > div {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 800px !important;
        margin: 0 auto !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# ESTILOS CSS PERSONALIZADOS
# ============================================
st.markdown("""
<style>
    .stApp {
        background-color: #F8F9FA;
    }
    
    .download-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #1A3C4A;
        text-align: center;
    }
    
    .download-subtitle {
        font-family: 'Open Sans', sans-serif;
        font-size: 1.1rem;
        color: #4A5568;
        text-align: center;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    .form-box {
        background-color: #FFFFFF;
        padding: 2.5rem 2.5rem 2rem 2.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 24px rgba(26, 60, 74, 0.08);
        max-width: 500px;
        margin: 1.5rem auto;
        border: 1px solid #E2E8F0;
    }
    
    .form-box label {
        font-weight: 600;
        color: #1A3C4A;
        font-family: 'Open Sans', sans-serif;
    }
    
    .success-box {
        background-color: #F0F7F0;
        border: 2px solid #B87333;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        max-width: 500px;
        margin: 1.5rem auto;
    }
    
    .success-box .icon-big {
        font-size: 2.8rem;
        color: #B87333;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .success-box h3 {
        font-family: 'Montserrat', sans-serif;
        color: #1A3C4A;
        margin: 0.5rem 0;
    }
    
    .success-box p {
        font-family: 'Open Sans', sans-serif;
        color: #4A5568;
        line-height: 1.6;
    }
    
    .guia-item {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        max-width: 500px;
        margin: 1rem auto;
        text-align: left;
    }
    
    .guia-item h4 {
        font-family: 'Montserrat', sans-serif;
        color: #1A3C4A;
        margin: 0 0 0.3rem 0;
        font-size: 1.05rem;
    }
    
    .guia-item p {
        font-family: 'Open Sans', sans-serif;
        color: #4A5568;
        font-size: 0.92rem;
        margin: 0 0 0.8rem 0;
        line-height: 1.5;
    }
    
    .footer {
        text-align: center;
        font-family: 'Open Sans', sans-serif;
        color: #A0AEC0;
        font-size: 0.8rem;
        padding: 2rem 0;
        border-top: 1px solid #E2E8F0;
        margin-top: 2.5rem;
    }
    
    .footer a {
        color: #B87333;
        text-decoration: none;
        font-weight: 500;
    }
    
    .footer a:hover {
        text-decoration: underline;
    }
    
    .back-link {
        text-align: center;
        margin-top: 1rem;
    }
    
    .back-link a {
        color: #B87333;
        text-decoration: none;
        font-family: 'Open Sans', sans-serif;
        font-weight: 500;
    }
    
    .back-link a:hover {
        text-decoration: underline;
    }
    
    .disclaimer {
        text-align: center;
        color: #A0AEC0;
        font-family: 'Open Sans', sans-serif;
        font-size: 0.8rem;
        margin-top: -0.5rem;
    }
    
    .stCheckbox label {
        font-family: 'Open Sans', sans-serif;
        color: #4A5568;
        font-size: 0.9rem;
    }
    
    .stAlert {
        border-radius: 8px;
        font-family: 'Open Sans', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# TÍTULO
# ============================================
st.markdown("""
<h1 class="download-title">Descarga tus 2 guías gratuitas</h1>
<p class="download-subtitle">
    <strong>"5 errores estadísticos que arruinan tu tesis de educación"</strong> +
    <strong>"Caso Resuelto: Capítulo de Resultados en APA 7"</strong><br>
    Identifica los fallos antes de que tu asesor los vea, y mira un ejemplo completo ya resuelto.
</p>
""", unsafe_allow_html=True)

# ============================================
# SISTEMA DE CAPTURA DE CORREOS
# ============================================

if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'email' not in st.session_state:
    st.session_state.email = ""
if 'nombre' not in st.session_state:
    st.session_state.nombre = ""

def guardar_email(nombre, email):
    st.session_state.submitted = True
    st.session_state.email = email
    st.session_state.nombre = nombre
    
    try:
        df = pd.DataFrame([[datetime.now(), nombre, email]], 
                         columns=['fecha', 'nombre', 'email'])
        if os.path.exists('leads.csv'):
            df_existente = pd.read_csv('leads.csv')
            df = pd.concat([df_existente, df], ignore_index=True)
        df.to_csv('leads.csv', index=False)
    except:
        pass

if not st.session_state.submitted:
    with st.container():
        st.markdown('<div class="form-box">', unsafe_allow_html=True)
        
        with st.form("form_descarga"):
            nombre = st.text_input("Tu nombre completo", placeholder="Ej: María Fernández")
            email = st.text_input("Tu correo electrónico", placeholder="Ej: maria@email.com")
            
            acepta = st.checkbox("Acepto recibir información sobre asesoría estadística y recursos para mi tesis. Puedo darme de baja en cualquier momento.")
            
            submitted = st.form_submit_button("Descargar guías ahora")
            
            if submitted:
                if not nombre or not email:
                    st.error("Por favor, completa todos los campos.")
                elif "@" not in email or "." not in email:
                    st.error("Por favor, ingresa un correo válido.")
                elif not acepta:
                    st.warning("Debes aceptar el consentimiento para continuar.")
                else:
                    guardar_email(nombre, email)
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <p class="disclaimer">
            Tus datos están seguros. No compartiré tu información con terceros.
        </p>
        """, unsafe_allow_html=True)

else:
    st.markdown(f"""
    <div class="success-box">
        <span class="icon-big">✓</span>
        <h3>¡Gracias, {st.session_state.nombre}!</h3>
        <p>
            Tus guías están listas. <strong>Descárgalas y revísalas antes de tu próxima entrega.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ---- Guía 1 ----
    st.markdown("""
    <div class="guia-item">
        <h4>📄 Guía 1: 5 errores estadísticos que arruinan tu tesis de educación</h4>
        <p>Identifica los errores más comunes antes de que tu asesor los vea.</p>
    </div>
    """, unsafe_allow_html=True)
    try:
        with open("guia.pdf", "rb") as f:
            st.download_button(
                label="Descargar Guía 1",
                data=f.read(),
                file_name="5_errores_estadisticos_tesis_educacion.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="download_guia1",
            )
    except FileNotFoundError:
        st.error("El archivo `guia.pdf` no se encuentra en la carpeta raíz del proyecto.")

    # ---- Guía 2 ----
    st.markdown("""
    <div class="guia-item">
        <h4>📄 Guía 2: Caso Resuelto — Capítulo de Resultados en APA 7</h4>
        <p>Un ejemplo completo, paso a paso: operacionalización, confiabilidad, niveles, prueba de normalidad e hipótesis, redactado como lo espera tu jurado.</p>
    </div>
    """, unsafe_allow_html=True)
    try:
        with open("guia2.pdf", "rb") as f:
            st.download_button(
                label="Descargar Guía 2",
                data=f.read(),
                file_name="caso_resuelto_tesis_educacion_apa7.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="download_guia2",
            )
    except FileNotFoundError:
        st.error("El archivo `guia2.pdf` no se encuentra en la carpeta raíz del proyecto.")

    st.markdown("""
    <div class="back-link">
        <a href="/" target="_self">← Volver a la página principal</a>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div class="footer">
    <p>
        <strong>Ángela Gutiérrez</strong> · Economista, Universidad de Los Andes (2003) · Especialista en Metodología Aplicada a Ciencias Sociales<br>
        <a href="https://wa.me/584247474381" target="_blank">+58 424 747 4381</a>
    </p>
</div>
""", unsafe_allow_html=True)
