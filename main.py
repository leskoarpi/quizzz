import streamlit as st 
import streamlit_authenticator as stauth 

st.title("Welcome, Human!")

data = st.text_input("data")

if 'lista' not in st.session_state:
    st.session_state.lista = []

if st.button('hozzaad'):
    st.session_state.lista.append(data)

if st.session_state.lista:
    for i in range(len(st.session_state.lista)):
        st.write(st.session_state.lista[i])