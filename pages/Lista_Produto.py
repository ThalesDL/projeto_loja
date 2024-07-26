import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Listagem de Produtos", page_icon="📙")

st.title("PRODUTOS CADASTRADOS")
st.divider()

dados2 = pd.read_csv("produtos.csv")
dados2.set_index("nr_caneta" , inplace=True)
st.dataframe(dados2)
