# view/accueil.py

import streamlit as st

def page_accueil():
    st.title("🎴 Oriflamme - Accueil 🎴")
    st.markdown("""
    Oriflamme est un jeu de cartes de **bluff, de stratégie et de gestion d'influence**.

    Chaque joueur pose des cartes face cachée sur une ligne commune.

    Ensuite, les cartes sont révélées et leurs effets sont appliqués dans l'ordre de pose.

    Le but est d'accumuler le plus d'influence en usant de stratégie, de bluff et de prise de risques.
    """)

    st.subheader("Que voulez-vous faire ?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Créer une Partie"):
            st.info("Fonction de création de partie en construction... 🏗️")

    with col2:
        if st.button("🔍 Rechercher une Partie"):
            st.info("Fonction de recherche de partie en construction... 🔍")
