import streamlit as st

# -------------------------------------------------------sidebar

st.sidebar.title("Calculadora IMC")

st.sidebar.title("IMC(Indice de massa corporasl=Será que seu peso )")

# ------------------------------------------------------principal
st.title("CALCULADORA IMC")
nome=st.text_input("Digite seu nome de Usuario: ")
altura=st.text_input("Digite sua altura: ")
peso=st.text_input("Digiie seu peso: ")

imc = peso / (altura ** 2) 

if  imc <=18.5 :
    peso("Abaixo do Peso!!")
elif imc <=24.9:
    peso("Peso normal")
elif imc >=29.9:
    peso("Sobrepeso")
elif imc >=34.9:
    peso("Obesidade Grau I")
elif imc >= 39.9 :
    peso("Obesidade Grau II")
elif imc >=40.0 :
    peso("Obesidade Grau III (mórbida)")

if st.button("Calcular"):
   imc= peso / (altura ** 2) 
    
st.warning(f"O seu imc é{imc}")
