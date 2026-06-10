import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ── Configuração da página ──────────────────────────────────────────
st.set_page_config(
    page_title="Sistema EKT — Formulário de Viabilidade",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove margens padrão do Streamlit para o formulário ficar 100%
st.markdown("""
<style>
    /* Remove padding padrão do Streamlit */
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header[data-testid="stHeader"] { display: none; }
    .stDeployButton { display: none; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    /* Sem barra de scroll lateral no body */
    html, body { overflow-x: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Carrega o HTML do formulário ────────────────────────────────────
html_path = Path(__file__).parent / "index.html"

if not html_path.exists():
    st.error("❌ Arquivo index.html não encontrado na pasta do projeto.")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

# ── Renderiza o formulário em iframe de altura total ─────────────────
# height=0 + scrolling=True + CSS de expansão = ocupa 100vh
components.html(
    html_content,
    height=1100,   # ajuste se quiser mais ou menos altura inicial
    scrolling=True,
)
