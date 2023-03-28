import streamlit as st
from PIL import Image # Pour montrer l'image 
import exifread #  Pour extraction des données méta
# Création de deux colonnes. Une pour la photo et une pour les métadonnées.
col1,col2 = st.columns(2)
#Ouverture de l'image avec titre
with col1:
    st.write("#### Une image avec streamlit : ")
    img = Image.open("montre_gps.jpg")
    st.image(img, caption="une montre gps", width=300)

# Ouverture du fichier et récupération des tags Exif
chemin = "montre_gps.jpg"
fichier = open(chemin, "rb")
tags = exifread.process_file(fichier)
# Boucle For pour placer les données dans le formulaire Streamlit
with col2:
    with st.form("my_form"):
        st.write("#### Formulaire Méta EXIF")
        for clé, valeur in tags.items():
            if clé not in ("JPEGThumbnail", "TIFFThumbnail", "Filename", "EXIF MakerNote"):
                tags[clé] = st.text_input(clé, valeur)
        submit_button = st.form_submit_button(label="Submit")
