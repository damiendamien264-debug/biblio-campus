import json
import os

DATA_FILE = os.path.join("data", "library.json")

def charger_donnees():
    if not os.path.exists(DATA_FILE):
        return {"livres": [], "emprunts": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_donnees(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)