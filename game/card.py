# game/card.py

import yaml
from conf import CARTES_FILE
from pathlib import Path

class Card:
    def __init__(self, nom, image_path, description, pv, attaque, defense, influence):
        self.nom = nom
        self.image_path = Path(image_path)
        self.description = description
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.influence = influence

    def __repr__(self):
        return f"Card(nom={self.nom})"

def charger_cartes(filepath=CARTES_FILE):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data is None or "cartes" not in data:
            raise ValueError(f"Le fichier {filepath} ne contient pas 'cartes'.")
        cartes = []
        for item in data["cartes"]:
            carte = Card(
                nom=item["nom"],
                image_path=item["image_path"],
                description=item["description"],
                pv=item["pv"],
                attaque=item["attaque"],
                defense=item["defense"],
                influence=item["influence"]
            )
            cartes.append(carte)
        return cartes
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier {filepath} est introuvable.")
    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement des cartes : {e}")

# Chargement automatique
cartes_personnages = charger_cartes()
