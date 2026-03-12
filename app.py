import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Mercado Imobiliário",
    page_icon="🏢",
    layout="wide"
)

model = joblib.load("model.pkl")

st.sidebar.title("🏢 Mercado Imobiliário")
st.sidebar.markdown("Sistema inteligente de previsão imobiliária")
st.sidebar.markdown("---")
st.sidebar.info("Modelo baseado em Regressão Linear")

st.title("Dashboard de Avaliação Imobiliária")
st.markdown("### Simule o valor de mercado de um imóvel")

col1, col2, col3 = st.columns(3)

with col1:
    area = st.number_input("Área (m²)", min_value=10, step=10)

with col2:
    quartos = st.number_input("Quartos", min_value=1, step=1)

with col3:
    banheiros = st.number_input("Banheiros", min_value=1, step=1)

st.markdown("---")

if st.button("Calcular Valor de Mercado"):
    dados = np.array([[area, quartos, banheiros]])
    previsao = model.predict(dados)[0]

    st.success("Avaliação concluída com sucesso!")

    colA, colB = st.columns(2)

    with colA:
        st.metric("Valor estimado", f"R$ {previsao:,.2f}")

    with colB:
        st.metric("Preço por m²", f"R$ {previsao/area:,.2f}")