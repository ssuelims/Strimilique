# importe o streamlit - baby step -1

# Entre com o numero

# verifique se o numero e positivo,negativo ou nulo - baby step -3

import streamlit as st
numero = st.number_input("Digite o numero:")
if numero>0:
    st.balloons()
    st.write(f"o numero e positivo:{numero}")
elif numero<0:
    st.snow()
    st.write(f"o numero e negativo:{numero}")
else:
    st.write(f"o numero e zero")
    
    
    

