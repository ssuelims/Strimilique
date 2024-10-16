import streamlit as st
import pandas as pd
import requests

st.title("DASHBORD DE VENDAS: shopping_trolley:")
url= "https://labdados.com/produtos?regiao=norte&ano=2022"
response = requests.get(url)

if uploader is not None:
    df = pd.read_csv(uploader)
    st.dataframe(df)
                     
    st.metric('receita',df['preco'].sum())
    st.metric('quantidade de vendas(linhas)',df.shape[0])
    st.metric('quantidade de variaveis(colunas)',df.shape[1])
    st.dataframe(df)
    st.snow()
else:
    st.write('clique no botao todos')