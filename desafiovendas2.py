import streamlit as st
import requests
import pandas as pd

st.title("DASHBOARD DE VENDAS :shopping_trolley:")

# Obter dados
url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())

# Calcular receita e número de linhas
preco_total = df["Preço"].sum()
num_linhas = df.shape[0]

# Formatar receita
if preco_total < 1000:
    receita_formatada = f"{preco_total}"
elif preco_total < 1000000:
    receita_formatada = f"{preco_total / 1000:.1f} mil"
else:
    receita_formatada = f"{preco_total / 1000000:.1f} milhão"

# Formatar número de linhas
if num_linhas < 1000:
    linhas_formatadas = f"{num_linhas}"
elif num_linhas < 1000000:
    linhas_formatadas = f"{num_linhas / 1000:.1f} mil"
else:
    linhas_formatadas = f"{num_linhas / 1000000:.1f} milhão"

# Botão para mostrar os números
if st.button("Todos os números da receita"):
    st.balloons()
    st.metric("Receita", receita_formatada)
    st.metric("Vendas (linhas)", linhas_formatadas)
    st.metric("Variáveis (colunas)", df.shape[1])
    st.snow()
    st.dataframe(df)