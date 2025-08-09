import pyshorteners
import streamlit as st

#Función que usa el metodo tinyurl.short para acortar la URL
def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

#App web con stremamlit
st.set_page_config(page_title="URL Shortener", page_icon="✏️", layout="centered")
st.image("images/www.png", use_container_width=True)
st.title("URL Shortener")
url = st.text_input("Ingresa la URL")
if st.button("Genera la nueva URL"):
    st.write("URL recortada: ", shorten_url(url))
    #if url:
    #    shortened_url = shorten_url(url)
