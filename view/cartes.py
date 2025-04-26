# view/cartes.py

import streamlit as st
from game.card import cartes_personnages

def page_voir_cartes():
    st.title("🃏 Aperçu des cartes du jeu")
    for carte in cartes_personnages:
        st.subheader(carte.nom)
        st.image(str(carte.image_path), width=200)
        st.write(f"**Compétence :** {carte.description}")
        st.write(f"**Points de Vie :** {carte.pv}")
        st.write(f"**Attaque :** {carte.attaque}")
        st.write(f"**Défense :** {carte.defense}")
        st.write(f"**Influence :** {carte.influence} (1 pièce d'or par point)")
        st.markdown("---")
