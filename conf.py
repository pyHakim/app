# conf.py

from pathlib import Path

# ==== Chemins ====
ROOT_DIR = Path(__file__).resolve().parent
GAME_DIR = ROOT_DIR / "game"
ASSETS_DIR = ROOT_DIR / "assets"
AUTH_DIR = ROOT_DIR / "auth"           # <-- Nouveau

# ==== Fichiers YAML ====
CARTES_FILE = GAME_DIR / "cartes.yaml"
USERS_FILE = AUTH_DIR / "users.yaml"    # <-- Nouveau

# ==== Paramètres Globaux ====
JOUEURS_DISPONIBLES = ["Alice", "Bob", "Clara", "David"]
OR_PAR_POINT_INFLUENCE = 1
OR_INITIAL_PAR_JOUEUR = 5

# ==== Infos UI ====
APP_TITLE = "Oriflamme - Jeu de Cartes"
