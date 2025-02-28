import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autorise les requêtes depuis le frontend

# Fichier pour stocker les emplacements
DATA_FILE = "locations.json"

def load_locations():
    """Charge les emplacements depuis le fichier JSON."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_locations(locations):
    """Sauvegarde les emplacements dans le fichier JSON."""
    with open(DATA_FILE, "w") as file:
        json.dump(locations, file, indent=4)

# Charger les emplacements au démarrage
locations = load_locations()

@app.route('/')
def home():
    return "Bienvenue sur l'API ArtMap ! Essayez /locations pour voir les emplacements."

@app.route('/locations', methods=['GET'])
def get_locations():
    """Renvoie la liste des emplacements."""
    return jsonify(locations)

@app.route('/locations', methods=['POST'])
def add_location():
    """Ajoute un nouvel emplacement."""
    data = request.json
    new_location = {
        "id": len(locations) + 1,
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "description": data.get("description", "")
    }
    locations.append(new_location)
    save_locations(locations)  # Sauvegarde dans le fichier
    return jsonify(new_location), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)

