import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="CADASTRO PRODUTO", page_icon="🛒")
st.image("imagem.png")
st.title("CADASTRO DE PRODUTOS")
st.divider()

#inserindo os produtos
lista = st.subheader("Anote os itens da compra")

caneta = st.checkbox("Caneta")
if caneta:
    nr_caneta = st.number_input("Quantidade: ", placeholder="digitar",
                                step=1, value=None)
else:
     nr_caneta = 0

lapis = st.checkbox("Lápis")
if lapis:
    nr_lapis = st.number_input("Quantidade: ", placeholder="digitar", key="nr_lapis",
                                step=1, value=None)
else:
     nr_lapis = 0

borracha = st.checkbox("Borracha")
if borracha:
    nr_borracha = st.number_input("Quantidade: ", placeholder="digitar", key="nr_borracha",
                                step=1, value=None)
else:
     nr_borracha = 0

caderno = st.checkbox("Caderno")
if caderno:
    nr_caderno = st.number_input("Quantidade: ", placeholder="digitar", key="nr_caderno",
                                step=1, value=None)
else:
     nr_caderno = 0

regua = st.checkbox("Régua")
if regua:
    nr_regua = st.number_input("Quantidade: ", placeholder="digitar", key="nr_regua",
                                step=1, value=None)
else:
     nr_regua = 0


botao2 = st.button("Clique aqui para cadastrar", key="clk_botao2")

if botao2:
    with open("produtos.csv", "a", encoding="utf-8") as file:
            file.write(f"{nr_caneta},{nr_lapis},{nr_borracha},{nr_caderno},{nr_regua}\n")
            st.success("Cadastro concluido com sucesso!", icon="😁")
     

