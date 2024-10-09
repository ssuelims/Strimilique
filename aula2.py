import streamlit as st
import pandas as pd
st.title("carregue o seu Dataset")

uploader = st.file_uploader("escolha o arquivo",type="csv")
if uploader is not None:
    df = pd.read_csv(uploader)
    st.dataframe(df)
                     
    