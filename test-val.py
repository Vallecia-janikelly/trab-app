import streamlit as st

col1, col2, col3 = st.columns([1, 2, 3])

with col2:
  st.image("Instagram_icon.png", width=300, link="https://www.instagram.com/")

st.title("Nome: Vallécia Janikelly")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  st.image("foto.jpg", width=300)
 
with col2:
  st.header("Sobre Mim:")
  st.write(" Sou aluna do curso técnico integrado em informática - campus Itabaiana ")

st.write("")
 
st.link_button("Acessar Site", "https://sites.google.com/academico.ifpb.edu.br/discentevallecia/in%C3%ADcio")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 3])

with col2:
  st.image("whats.jpg", width=100, link="https://wa.me/+5583987061523")
