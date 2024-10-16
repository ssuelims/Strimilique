import streamlit as st



#  (1)Crei um Algoritimo que descubra um numero secreto!
#  (2)crie um numero secreto
numero_secreto = 9
# (3)titulo de aplicaço
st.title("numero secreto")

# (4) Dar uma mensagem de boas vindas
st.write("boas vindas")

# (5)receber o chute do usuário
numero = st.number_input("digite o numero secreto",step=1,min_value=0,max_value=10 )

# (6) Verificar o chute com o numero secreto
if st.button('conferir'):
    if numero == numero_secreto:
        st.snow()
        
# (7) Mostrar uma mensagem personalizada
        st.success(" 🦔voce acertou🦔")
        st.write("acertou")
        st.balloons()
    else:
        st.write("Errou o numero")




