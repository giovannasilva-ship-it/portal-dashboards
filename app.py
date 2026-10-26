import streamlit as st
import json

st.set_page_config(page_title="Painel da Aprendizagem", layout="wide")

# CSS para remover margens excessivas do topo e compactar o layout
st.markdown("""
<style>
    /* Remove o espaçamento padrão no topo do Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }
    
    a { text-decoration: none !important; }
    
    .header-container {
        text-align: center;
        margin-top: -10px;
        margin-bottom: 15px;
    }
    
    .corporate-btn {
        display: block;
        background: linear-gradient(135deg, #0056b3 0%, #0080ff 100%);
        color: #ffffff !important;
        padding: 15px;
        margin-bottom: 12px;
        text-align: center;
        text-decoration: none !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 15px;
        font-weight: 600;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .corporate-btn:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 12px rgba(0, 128, 255, 0.25);
        color: #ffffff !important;
    }
    .support-btn { 
        background: linear-gradient(135deg, #ffc107 0%, #ff9800 100%);
        color: #000000 !important;
    }
    .support-btn:hover { 
        transform: scale(1.02);
        box-shadow: 0 6px 12px rgba(255, 152, 0, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# Centralização do logo com margem superior reduzida
col_esq, col_centro, col_dir = st.columns([2.5, 1, 2.5])
with col_centro:
    try:
        st.image("logo.png", width=140)
    except:
        pass

# Título e subtítulo juntos, sem espaços vazios
st.markdown("""
<div class="header-container">
    <h2 style="margin: 0; color: #1e293b; font-weight: 700;">Painel da Aprendizagem</h2>
    <p style="margin: 5px 0 0 0; font-size: 15px; color: #64748b;">Selecione um relatório abaixo para visualizar os dados atualizados.</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Carregamento dos relatórios
try:
    with open('dashboards.json', 'r', encoding='utf-8') as f:
        dashboards = json.load(f)
except FileNotFoundError:
    st.error("Arquivo dashboards.json não encontrado.")
    dashboards = []

# Distribuição 5 e 5 em colunas
col1, col2 = st.columns(2)
meio = 5

with col1:
    for dash in dashboards[:meio]:
        st.markdown(f'<a href="{dash["url"]}" target="_blank" class="corporate-btn">{dash["nome"]}</a>', unsafe_allow_html=True)

with col2:
    for dash in dashboards[meio:]:
        st.markdown(f'<a href="{dash["url"]}" target="_blank" class="corporate-btn">{dash["nome"]}</a>', unsafe_allow_html=True)

st.write("---")
st.markdown('<a href="https://forms.google.com/" target="_blank" class="corporate-btn support-btn">💬 Reportar Problema ou Sugestão</a>', unsafe_allow_html=True)
