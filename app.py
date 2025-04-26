import streamlit as st

# Titre de la page
st.title("Bienvenue sur mon premier site Streamlit 🎈")

# Un petit texte
st.write("Hello tout le monde ! Ceci est mon tout premier site Streamlit en ligne.")

# Un input utilisateur
name = st.text_input("Quel est ton prénom ?")

# Afficher une réponse
if name:
    st.write(f"Enchanté, {name} ! 👋")

# Un bouton
if st.button("Clique ici"):
    st.success("Tu as cliqué sur le bouton ! 🎉")