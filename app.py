import streamlit as st
import pandas as pd
import os

# 1. Configuração da página
st.set_page_config(
    page_title="Data Pipeline 2026 | Otávio",
    page_icon="📊",
    layout="wide"
)

# 2. Estilização CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #374151;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Caminho dos dados
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_atual, 'data', 'vendas_limpo.csv')

# 4. Cabeçalho
st.title("🛡️ Pipeline de Inteligência de Vendas")
st.markdown(f"**Status:** ✅ Operacional | **Data:** {pd.Timestamp.now().strftime('%d/%m/%Y')}")
st.divider()

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    
    # 5. Métricas (Corrigido: Chaves fechadas corretamente)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Faturamento Total", f"R$ {df['valor'].sum():,.2f}")
    with col2:
        st.metric("Ticket Médio", f"R$ {df['valor'].mean():,.2f}")
    with col3:
        st.metric("Volume de Pedidos", len(df))

    # 6. Gráficos
    st.write("") 
    col_graph1, col_graph2 = st.columns([2, 1])
    with col_graph1:
        st.subheader("Análise por Categoria")
        st.bar_chart(df.groupby('categoria')['valor'].sum(), color="#00d4ff")
    with col_graph2:
        st.subheader("Destaque")
        st.info(f"Maior categoria: **{df.groupby('categoria')['valor'].sum().idxmax()}**")

    # 7. Tabela
    st.divider()
    st.subheader("🔍 Dados Processados")
    st.dataframe(df, width=2000) 
else:
    st.error("Arquivo de dados não encontrado.")