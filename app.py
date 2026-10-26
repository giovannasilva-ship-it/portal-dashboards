import streamlit as st
import json

st.set_page_config(page_title="Painel da Aprendizagem", layout="wide")

# CSS para cores do CIEE e animações interativas
st.markdown("""
<style>
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
        transform: scale(1.03); /* Efeito de aumentar o botão */
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

# Layout do Cabeçalho com o Logótipo
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    try:
        # O Streamlit vai procurar este ficheiro no seu GitHub
        st.image("logo.png", width=150)
    except:
        st.write("*(Logo CIEE)*")

with col_titulo:
    st.title("📊 Painel da Aprendizagem")
    st.write("Selecione um relatório abaixo para visualizar os dados atualizados.")

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
