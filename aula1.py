
import streamlit as st

import requests
import pandas as pd

st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url = "https://labdados.com/produtos?regiao=norte&ano=2022"
response = requests.get(url)
# json
# Dicionario
# Dataframe
# verificar se a resposta foi bem sucedida


df = pd.DataFrame.from_dict(response.json())
if st.button("todos"):
    st.balloons()
    st.metric('receita',df['Preço'].sum())
    st.metric('quantidade de vendas(linhas)',df.shape[0])
    st.metric('quantidade de variaveis(colunas)',df.shape[1])
    st.dataframe(df)
    st.snow()
else:
    st.write('clique no botao todos')
