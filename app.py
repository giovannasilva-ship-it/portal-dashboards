import streamlit as st
import json

# Atualizado para ecrã mais largo para acomodar bem as duas colunas
st.set_page_config(page_title="Painel da Aprendizagem", layout="wide")

st.markdown("""
<style>
    a { text-decoration: none !important; }
    .corporate-btn {
        display: block;
        background-color: #f8fafc;
        color: #1e293b !important;
        padding: 18px;
        margin-bottom: 12px;
        text-align: center;
        text-decoration: none !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
        border-left: 6px solid #0056b3;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        transition: all 0.2s ease-in-out;
    }
    .corporate-btn:hover {
        background-color: #0056b3;
        color: #ffffff !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    .support-btn { border-left: 6px solid #475569; background-color: #ffffff; font-size: 14px; padding: 15px; }
    .support-btn:hover { background-color: #475569; }
</style>
""", unsafe_allow_html=True)

st.title("📊 Painel da Aprendizagem")
st.write("Selecione um relatório abaixo para visualizar os dados atualizados.")
st.write("---")

try:
    with open('dashboards.json', 'r', encoding='utf-8') as f:
        dashboards = json.load(f)
except FileNotFoundError:
    st.error("Ficheiro dashboards.json não encontrado.")
    dashboards = []

# Criação das duas colunas
col1, col2 = st.columns(2)

# Distribui os primeiros 5 na coluna 1 e os restantes na coluna 2
meio = 5
with col1:
    for dash in dashboards[:meio]:
        st.markdown(f'<a href="{dash["url"]}" target="_blank" class="corporate-btn">{dash["nome"]}</a>', unsafe_allow_html=True)

with col2:
    for dash in dashboards[meio:]:
        st.markdown(f'<a href="{dash["url"]}" target="_blank" class="corporate-btn">{dash["nome"]}</a>', unsafe_allow_html=True)

st.write("---")
st.markdown('<a href="https://forms.google.com/" target="_blank" class="corporate-btn support-btn">💬 Reportar Problema ou Sugestão</a>', unsafe_allow_html=True)
