import streamlit as st
import requests

st.title("Informações do País")

nome = st.text_input("Digite o nome de um país:")

buscar = st.button("Buscar")

if buscar:
    data = requests.get(f'https://restcountries.com/v3.1/name/{nome}?fullText=true').json() # Faz requisição GET para api RestCountries e recebe um json com os dados do país
    official_name = data[0]['name']['official'] # Acessa nome oficial do país
    borders = data[0]['borders'] # Lista com países que faz fronteira
    borders_str = ', '.join(borders) # String com países que faz fronteira
    flag = data[0]['flags']['png'] # Imagem da bandeira
    coat_of_arms = data[0]['coatOfArms']['png'] # Imagem coat of arms
    latidude = data[0]['capitalInfo']['latlng'][0] # Acessa latitude
    longitude = data[0]['capitalInfo']['latlng'][1] # Acessa longitude
    with st.expander("Resultados", expanded=False): # Cria expander que inicia fechado
        col1, col2 = st.columns([0.33,0.67]) # Cria duas colunas dentro do expander, uma de 1/3 e outra de 2/3
        with col1:
            st.write(f'Nome Oficial: {official_name}')
            st.write(f'Países com Fronteira: {borders_str}')
            st.write(f'Latitude:{latidude}, Longitude:{longitude}')

        with col2:
            try:
                st.image(coat_of_arms, width=400) # Imagem com 400px de largura
            except:
                st.write("Não possui coat of arms")

        st.image(flag, use_column_width=True) # Imagem da bandeira com largura da tela