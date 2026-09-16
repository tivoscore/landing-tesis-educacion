import streamlit as st
import base64
from io import BytesIO
import pandas as pd
from datetime import datetime

# ============================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================
st.set_page_config(
    page_title="Angela Gutiérrez - Asesoría Metodológica para Tesis",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# OCULTAR ELEMENTOS DE STREAMLIT (BARRA LATERAL, MENÚ, DEPLOY)
# ============================================
st.markdown("""
<style>
    /* Tipografías de marca: Fraunces (titulares) + Work Sans (cuerpo) */
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Work+Sans:wght@400;500;600;700&display=swap');

    [data-testid="stSidebar"] { display: none !important; }
    #MainMenu { visibility: hidden !important; }
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    .stDeployButton { display: none !important; }
    .main > div {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 1000px !important;
        margin: 0 auto !important;
    }
    .stApp > footer { display: none !important; }

    /* Fondo general — Papel Cátedra */
    .stApp { background-color: #F6F1E7; }

    .main-title {
        font-family: 'Fraunces', serif;
        font-size: 2.6rem;
        font-weight: 700;
        color: #3B2247;
        line-height: 1.2;
    }
    .main-title .highlight { color: #B8562F; }

    .subtitle {
        font-family: 'Work Sans', sans-serif;
        font-size: 1.2rem;
        color: #241B2E;
        margin-top: 0.8rem;
        line-height: 1.6;
    }

    .badge {
        background-color: #3B2247;
        color: #F6F1E7;
        padding: 0.3rem 1.2rem;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        display: inline-block;
    }

    .benefit-box {
        background-color: #FFFFFF;
        padding: 1.5rem 1.2rem;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(59, 34, 71, 0.08);
        margin: 0.8rem 0;
        border-left: 4px solid #B8562F;
        transition: transform 0.2s ease;
    }
    .benefit-box:hover { transform: translateY(-2px); }
    .benefit-box h4 {
        color: #3B2247;
        font-family: 'Fraunces', serif;
        font-weight: 600;
        font-size: 1.05rem;
        margin-bottom: 0.3rem;
    }
    .benefit-box p {
        color: #241B2E;
        font-family: 'Work Sans', sans-serif;
        font-size: 0.92rem;
        margin: 0;
        line-height: 1.5;
    }
    .benefit-box .icon {
        font-size: 1.3rem;
        margin-right: 0.5rem;
        color: #B8562F;
    }

    .divider {
        border: none;
        height: 2px;
        background: linear-gradient(to right, transparent, #C9A227, transparent);
        margin: 2.5rem 0;
        opacity: 0.6;
    }

    .hero-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1.5rem;
    }

    .btn-whatsapp {
        background-color: #25D366;
        color: #FFFFFF;
        font-family: 'Work Sans', sans-serif;
        font-size: 1.05rem;
        font-weight: 600;
        padding: 0.85rem 2rem;
        border-radius: 50px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 4px 14px rgba(37, 211, 102, 0.3);
    }
    .btn-whatsapp:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
    }

    .btn-secondary {
        background-color: #FFFFFF;
        color: #3B2247;
        font-family: 'Work Sans', sans-serif;
        font-size: 1.05rem;
        font-weight: 600;
        padding: 0.85rem 2rem;
        border-radius: 50px;
        border: 2px solid #B8562F;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
    }
    .btn-secondary:hover {
        background-color: #B8562F;
        color: #FFFFFF;
        transform: scale(1.02);
    }

    .guia-section {
        background-color: #3B2247;
        padding: 2.5rem 2rem;
        border-radius: 16px;
        margin: 2.5rem 0 1rem 0;
        text-align: center;
    }
    .guia-section h3 {
        font-family: 'Fraunces', serif;
        font-size: 1.6rem;
        font-weight: 600;
        color: #F6F1E7;
        margin-bottom: 0.5rem;
    }
    .guia-section p {
        font-family: 'Work Sans', sans-serif;
        font-size: 1.05rem;
        color: #E9D9A8;
        max-width: 600px;
        margin: 0 auto 1.5rem auto;
        line-height: 1.6;
    }

    .btn-guia {
        background-color: #C9A227;
        color: #3B2247;
        font-family: 'Work Sans', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        padding: 0.85rem 2.5rem;
        border-radius: 50px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 4px 14px rgba(201, 162, 39, 0.3);
    }
    .btn-guia:hover {
        background-color: #B8912A;
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(201, 162, 39, 0.4);
    }

    .foto-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .foto-container img {
        border-radius: 50%;
        border: 4px solid #B8562F;
        box-shadow: 0 8px 30px rgba(59, 34, 71, 0.2);
        width: 180px;
        height: 180px;
        object-fit: cover;
        transition: transform 0.3s ease;
    }
    .foto-container img:hover { transform: scale(1.02); }

    .foto-placeholder {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: linear-gradient(135deg, #3B2247, #B8562F);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #F6F1E7;
        font-family: 'Fraunces', serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0 auto;
        border: 4px solid #B8562F;
        box-shadow: 0 8px 30px rgba(59, 34, 71, 0.2);
    }

    .cta-wrapper { text-align: center; padding: 1rem 0 0.5rem 0; }
    .cta-title {
        font-family: 'Fraunces', serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #3B2247;
        margin-bottom: 0.5rem;
    }
    .cta-sub {
        font-family: 'Work Sans', sans-serif;
        font-size: 1.05rem;
        color: #241B2E;
        max-width: 550px;
        margin: 0 auto 1rem auto;
    }

    .footer {
        text-align: center;
        font-family: 'Work Sans', sans-serif;
        color: #7A6E63;
        font-size: 0.8rem;
        padding: 2rem 0;
        border-top: 1px solid rgba(59, 34, 71, 0.15);
        margin-top: 2.5rem;
    }
    .footer a {
        color: #B8562F;
        text-decoration: none;
        font-weight: 500;
    }
    .footer a:hover { text-decoration: underline; }

    @media (max-width: 768px) {
        .main-title { font-size: 2rem; }
        .hero-buttons { flex-direction: column; align-items: stretch; }
        .btn-whatsapp, .btn-secondary { justify-content: center; }
        .foto-container img { width: 140px; height: 140px; }
        .guia-section h3 { font-size: 1.3rem; }
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# ENCABEZADO CON FOTO
# ============================================
col1, col2 = st.columns([1, 2.2])

with col1:
    try:
        st.markdown('<div class="foto-container">', unsafe_allow_html=True)
        st.image("assets/tu_foto.jpg",
                 caption=None,
                 width=180,
                 use_container_width=False,
                 output_format="JPEG")
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.markdown("""
        <div class="foto-placeholder">
            AG
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="padding-top: 0.3rem;">
        <span class="badge">Asesora metodológica para investigación en Educación</span>
        <h1 class="main-title">
            ¿Tu tesis de educación<br>
            <span class="highlight">se estanca en los números?</span>
        </h1>
        <p class="subtitle">
            Soy <strong>Angela Gutiérrez</strong>, economista.
            Te ayudo a que tu análisis estadístico sea <strong>aprobado por tu asesor</strong>
            sin que tengas que aprender SPSS desde cero.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# BOTONES DE ACCIÓN EN EL HERO
# ============================================
st.markdown("""
<div class="hero-buttons">
    <a href="https://wa.me/584247474381?text=Hola%20%C3%81ngela%2C%20quiero%20solicitar%20el%20diagn%C3%B3stico%20gratuito%20de%2010%20minutos%20para%20mi%20tesis." target="_blank">
        <button class="btn-whatsapp">
            📲 Solicitar diagnóstico de 10 min por WhatsApp
        </button>
    </a>
    <a href="/descarga" target="_self">
        <button class="btn-secondary">
            📄 Descargar guías gratis (5 Errores + Caso Resuelto)
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# ============================================
# SEPARADOR
# ============================================
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ============================================
# BENEFICIOS (3 COLUMNAS)
# ============================================
st.markdown("""
<div style="text-align: center; margin-bottom: 1.5rem;">
    <h3 style="font-family: 'Fraunces', serif; color: #3B2247; font-weight: 600; font-size: 1.4rem;">
        Acompañamiento estadístico para tu tesis
    </h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="benefit-box">
        <h4><span class="icon">▸</span> Validez y Confiabilidad</h4>
        <p>Calculo la V de Aiken con juicio de expertos y el Alfa de Cronbach. Tu instrumento quedará impecable.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="benefit-box">
        <h4><span class="icon">▸</span> Estadística completa</h4>
        <p>Pruebas paramétricas y no paramétricas, tamaño del efecto, análisis de supuestos. Todo justificado.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="benefit-box">
        <h4><span class="icon">▸</span> Documentación profesional</h4>
        <p>Entrego un documento redactado con tablas, resultados e interpretación, listo para que tu asesor lo revise paso a paso.</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECCIÓN DE GUÍA GRATUITA EN EL CUERPO
# ============================================
st.markdown("""
<div class="guia-section">
    <h3>¿Aún no estás listo para contratar?</h3>
    <p>
        Descarga gratis <strong>"5 Errores Estadísticos"</strong> y el <strong>"Caso Resuelto en APA 7"</strong> —
        revísalos antes de tu próxima entrega.
    </p>
    <a href="/descarga" target="_self">
        <button class="btn-guia">
            📄 Descargar Guías Gratis
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# ============================================
# LLAMADA A LA ACCIÓN FINAL
# ============================================
st.markdown("""
<div class="cta-wrapper">
    <h2 class="cta-title">
        ¿Listo para resolver la estadística de tu tesis?
    </h2>
    <p class="cta-sub">
        Escríbeme por WhatsApp y recibe un diagnóstico metodológico preliminar de 10 minutos sin costo.
    </p>
    <a href="https://wa.me/584247474381?text=Hola%20%C3%81ngela%2C%20quiero%20solicitar%20el%20diagn%C3%B3stico%20gratuito%20para%20mi%20tesis." target="_blank">
        <button class="btn-whatsapp" style="background-color: #25D366; font-size: 1.1rem; padding: 1rem 2.5rem;">
            📲 Quiero mi diagnóstico gratuito
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div class="footer">
    <p>
        <strong>Angela Gutiérrez</strong> · Economista, Universidad de Los Andes (2003) · Asesora metodológica para investigación en Educación<br>
        <a href="https://wa.me/584247474381" target="_blank">+58 424 747 4381</a>
    </p>
</div>
""", unsafe_allow_html=True)