import streamlit as st
# -------------------------------------------------------sidebar

st.sidebar.title("VelozRent")

st.sidebar.title("Aluguel de carros")

carros = ['BMW','Mercedes','Civic', "fox" , "clio"]

opcao = st.sidebar.selectbox("Escolha o carro que foi alugado", carros)




#------------------------------------------------------principal
st.title("Aluguel de Carros")

st.image(f'{opcao}.png')
st.markdown(f'## você alugou o modelo:{opcao}')
st.markdown('---')

dias = st.text_input(f"Por quantos dias o {opcao} foi alugado?")
km = st.text_input(f"quantos km você rodou com o {opcao}?")

if opcao == 'BMW':
    diaria = 600
elif opcao == "Civic":
    diaria = 550
elif opcao == "clio":
    diarias = 260
elif opcao == "fox":
    diaria = 355


if st.button("Calcular"):
    dias = int(dias)
    km = float(km)
    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f"Você alugou o {opcao} por {dias}dias e redou {km}km. O valor total a pagar é R${aluguel_total}")