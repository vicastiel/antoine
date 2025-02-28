import requests

# URL de ton API Flask
url = "http://127.0.0.1:5000/locations"

# Liste des œuvres fictives avec leurs coordonnées GPS et descriptions
locations = [
    {"latitude": 48.8566, "longitude": 2.3522, "description": "Street Art à Châtelet"},
    {"latitude": 48.8606, "longitude": 2.3376, "description": "Fresque murale près du Louvre"},
    {"latitude": 48.853, "longitude": 2.3499, "description": "Installation moderne à Notre-Dame"},
    {"latitude": 48.875, "longitude": 2.295, "description": "Sculpture sur l’Avenue Montaigne"},
    {"latitude": 48.8656, "longitude": 2.3216, "description": "Peinture murale à Saint-Honoré"},
]

# Envoi des emplacements à l'API Flask
for location in locations:
    response = requests.post(url, json=location)
    if response.status_code == 201:
        print(f"✅ Emplacement ajouté : {response.json()}")
    else:
        print(f"❌ Erreur {response.status_code} : {response.text}")
