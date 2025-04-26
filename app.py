# app.py

import os
import sys
from pathlib import Path

# === Setup PYTHONPATH ===
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

# === Debug infos ===
print(f"[DEBUG] Répertoire courant (pwd) : {os.getcwd()}")
print(f"[DEBUG] sys.path : {sys.path}")

# === Imports internes ===
import streamlit as st
from conf import APP_TITLE
from view.accueil import page_accueil
from view.cartes import page_voir_cartes
from view.login import afficher_login

# === Streamlit config ===
st.set_page_config(page_title=APP_TITLE, page_icon="🎴", layout="centered")

# ---------------------- MAIN ----------------------

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "joueur" not in st.session_state:
        st.session_state.joueur = None

    # === Authentification ===
    if not st.session_state.logged_in:
        afficher_login()
        return

    # === Sidebar Navigation ===
    st.sidebar.title(f"Bienvenue {st.session_state.joueur} 👑")
    
    # MENU vertical
    page = st.sidebar.radio(
        "Navigation",
        ["Accueil", "Voir les Cartes"],
        index=0
    )

    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Déconnexion"):
        st.session_state.logged_in = False
        st.session_state.joueur = None
        st.experimental_rerun()

    # === Routage ===
    if page == "Accueil":
        page_accueil()
    elif page == "Voir les Cartes":
        page_voir_cartes()


if __name__ == "__main__":
    main()
