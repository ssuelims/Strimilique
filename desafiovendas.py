import streamlit as st


import requests
import pandas as pd
import plotly.express as px



st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())


preco_total = df["Preço"].sum()
linhas_total = df.shape[0]


# Formatando valores maiores
def formatar_valor(valor):
    if valor >= 1_000_000:
        return f"{valor / 1_000_000:.1f} milhão"
    elif valor >= 1_000:
        return f"{valor / 1_000:.1f} mil"
    else:
        return str(valor)


st.write(df.shape)
preco =df["Preço"].sum()
linhas = df.shape[0]

if preco / 1000 < 0.0:
    resposta = df["Preço"].sum()  
else:
    if preco / 1000000 < 0.0:
        valor = df["Preço"].sum()
        valor = str(valor)
        
        
        resposta = f"{valor[0]}mil"
    else:
        valor = df["Preço"].sum()
        valor = str(valor)
        resposta = f"{valor[0]} milhao"
   
if linhas / 1000 < 0.0:
    respostalinha = df.shape[0]  
else:
    if preco / 1000000< 0.0:
        linha = df.shape[0]
        linha = str(linha)
        respostalinha = f"{linha[0]}mil"
    else:
        linha = df.shape[0]
        linha = str(linha)
        respostalinha = f"{linha[0]} milhao"   
<<<<<<< HEAD
=======
        
   # valores de preços e Linhas
   
resposta = formatar_valor(preco_total)
respostalinha = formatar_valor(linhas_total)


>>>>>>> d45021802548a0f48849f8dd1b9d51d5b482eb05
        
if st.button("todos os numeros da receita"):
    st.balloons()
    st.metric("Receita",resposta)
    st.metric("vendas(linhas)",respostalinha)
    st.metric("variaveis(coluna)",df.shape[1])
    st.snow()
    st.dataframe(df)
else:
    st.write("clique no botao para todos")

    


        
        
  
    
    
    
    
    
    