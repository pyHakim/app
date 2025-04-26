# auth/users.py


import yaml
import bcrypt
from conf import USERS_FILE

def charger_utilisateurs(filepath=USERS_FILE):
    """Charge la liste des utilisateurs et mots de passe."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return {user["username"]: user["password"] for user in data["users"]}

def charger_noms_utilisateurs(filepath=USERS_FILE):
    """Charge uniquement les noms des utilisateurs."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return [user["username"] for user in data["users"]]

def verifier_identifiants(username, password, utilisateurs):
    """Vérifie si le username existe et si le password correspond."""
    hashed_password = utilisateurs.get(username)
    if hashed_password:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
    return False
