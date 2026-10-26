import streamlit as st
import json

st.set_page_config(page_title="Painel da Aprendizagem", layout="wide")

# CSS para cores do CIEE, alinhamento central e animações
st.markdown("""
<style>
    a { text-decoration: none !important; }
    
    .header-container {
        text-align: center;
        margin-bottom: 25px;
    }
    
    .corporate-btn {
        display: block;
        background: linear-gradient(135deg, #0056b3 0%, #0080ff 100%);
        color: #ffffff !important;
        padding: 16px;
        margin-bottom: 15px;
        text-align: center;
        text-decoration: none !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 16px;
        font-weight: 600;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .corporate-btn:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 15px rgba(0, 128, 255, 0.3);
        color: #ffffff !important;
    }
    .support-btn { 
        background: linear-gradient(135deg, #ffc107 0%, #ff9800 100%);
        color: #000000 !important;
    }
    .support-btn:hover { 
        transform: scale(1.03);
        box-shadow: 0 8px 15px rgba(255, 152, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Bloco Centralizado: 3 colunas onde colocamos o logo no meio exato
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

# Título e descrição centralizados
st.markdown("""
<div class="header-container">
    <h1 style="margin-top: 10px; color: #1e293b;">📊 Painel da Aprendizagem</h1>
    <p style="font-size: 16px; color: #64748b;">Selecione um relatório abaixo para visualizar os dados atualizados.</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Carregamento dos links
try:
    with open('dashboards.json', 'r', encoding='utf-8') as f:
        dashboards = json.load(f)
except FileNotFoundError:
    st.error("Ficheiro dashboards.json não encontrado.")
    dashboards = []

# Distribuição 5 e 5 nas colunas
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
