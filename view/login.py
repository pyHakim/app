# view/login.py

import streamlit as st
from auth.users import charger_utilisateurs, charger_noms_utilisateurs, verifier_identifiants

# Charger utilisateurs une fois ici pour toute la session
utilisateurs = charger_utilisateurs()
noms_utilisateurs = charger_noms_utilisateurs()

def afficher_login():
    st.title("🔐 Connexion Joueur")

    username = st.selectbox("Nom d'utilisateur :", noms_utilisateurs)
    password = st.text_input("Mot de passe :", type="password")

    if st.button("Se connecter"):
        if verifier_identifiants(username, password, utilisateurs):
            st.success(f"Bienvenue {username} !")
            st.session_state.logged_in = True
            st.session_state.joueur = username
            st.experimental_rerun()
        else:
            st.error("Identifiants incorrects. Réessayez.")
