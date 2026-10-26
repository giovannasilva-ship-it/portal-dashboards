import streamlit as st
import json

st.set_page_config(page_title="Portal de Dashboards", layout="centered")

# Injeção de CSS para estilizar os botões
st.markdown("""
<style>
    .corporate-btn {
        display: block;
        background-color: #ffffff;
        color: #0f172a !important;
        padding: 20px;
        margin-bottom: 15px;
        text-align: center;
        text-decoration: none;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px;
        font-weight: 600;
        border-radius: 8px;
        border-left: 6px solid #2563eb;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    .corporate-btn:hover {
        background-color: #2563eb;
        color: #ffffff !important;
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        transform: translateY(-3px);
    }
    .support-btn {
        border-left: 6px solid #475569;
        font-size: 14px;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Portal de Dashboards")
st.write("Selecione um relatório abaixo para visualizar os dados atualizados.")
st.write("---")

# Carregamento do JSON
try:
    with open('dashboards.json', 'r', encoding='utf-8') as f:
        dashboards = json.load(f)
except FileNotFoundError:
    st.error("Ficheiro dashboards.json não encontrado.")
    dashboards = []

# Geração dos botões com HTML/CSS
for dash in dashboards:
    html_btn = f"""<a href="{dash['url']}" target="_blank" class="corporate-btn">{dash['nome']}</a>"""
    st.markdown(html_btn, unsafe_allow_html=True)

st.write("---")

# Botão de suporte estilizado
suporte_btn = """<a href="https://forms.google.com/" target="_blank" class="corporate-btn support-btn">💬 Reportar Problema ou Sugestão</a>"""
st.markdown(suporte_btn, unsafe_allow_html=True)