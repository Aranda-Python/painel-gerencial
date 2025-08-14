import streamlit as st
from streamlit_option_menu import option_menu
import painel
import equipes_bomba 
import especialista_setor
import new_especialista_setor
import RAC
import municipios_visitados

 # --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Painel Gerencial - RSJCA",
    page_icon="📊",
    layout="wide",
)

# 🎨 CSS para deixar o menu mais bonito
st.markdown("""
    <style>
    .nav-link {
        font-size: 16px !important;
        font-weight: 500 !important;
        color: #4B5563 !important;
        transition: all 0.2s ease-in-out;
    }
    .nav-link:hover {
        color: #2563EB !important;
        transform: scale(1.05);
    }
    .nav-link.active {
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Menu horizontal no topo
escolha = option_menu(
    menu_title=None,
    options=["Home", "Painel Gerencial", "Equipes Bomba", "Especialista / Setor", "RAC", "Municipios Visitados"],
    icons=["house", "pie-chart", "droplet-fill", "gear", "clipboard-data", "geo-alt-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Menu na barra lateral
#with st.sidebar:
#    escolha = option_menu(
#        menu_title="📌 Menu Principal",
#        options=["Home", "Relatórios", "Dashboard", "Configurações"],
#        icons=["house", "bar-chart", "pie-chart", "gear"],
#        menu_icon="cast",
#        default_index=0,
#    )

# Lógica para carregar páginas
if escolha == "Home":
    st.title("🏠 Página Inicial")
    st.write("Bem-vindo ao sistema!")
    st.write('Utilize o menu acima.')
elif escolha == "Painel Gerencial":
    painel.app()
elif escolha == "Equipes Bomba":
    st.title("⛽ Equipes Bomba")
    st.write("Informações sobre as equipes de bombas medidoras...")
    # Aqui você pode adicionar mais conteúdo ou funcionalidades relacionadas às equipes bomba
    equipes_bomba.app()    
elif escolha == "Especialista / Setor":
    st.title("⚙️ Especialistas Setor")
    st.write("Informações sobre especialistas por setor...")
    especialista_setor.app()
    #new_especialista_setor.app()
elif escolha == "RAC":
    st.title("📈 RAC")
    st.write("Informações sobre RAC...")
    RAC.app()
elif escolha == "Municipios Visitados":
    st.title("🌍 Municípios Visitados")
    st.write("Informações sobre os municípios visitados...")
    municipios_visitados.app()    



