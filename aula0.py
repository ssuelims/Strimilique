import streamlit as st
st.write("Alo mundo")

"""
# Estamos iniciando o streamlit
# Ele nos ajudara no projeto final
# Em sua instalaçao vem incluido o pandas e outras libs.
"""
idade = st.number_input("Digite sua idade:",min_value=14, max_value=120)
if idade>=18:
    st.write(f" Alo mundo - voçe e maior de idade:{idade}")
else:
    st.write(f"Alo mundo - voçe e menor de idade:{idade}")
    
    

        