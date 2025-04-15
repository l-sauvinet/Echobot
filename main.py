import json
import random
import os
import requests
from bs4 import BeautifulSoup

# Fonction pour charger les données des réponses
def charger_donnees():
    if os.path.exists('data/data.json'):
        with open('data/data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# Fonction pour sauvegarder les données dans le fichier
def sauvegarder_donnees(donnees):
    with open('data/data.json', 'w', encoding='utf-8') as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)

# Fonction pour répondre à une question
def repondre(question, donnees):
    # Si la question existe déjà dans les données, répondre avec une réponse aléatoire
    if question in donnees:
        return random.choice(donnees[question])
    else:
        # Si la question n'est pas dans les données, chercher sur Wikipedia
        return obtenir_definition_wikipedia(question)

# Fonction pour obtenir une définition depuis Wikipedia
def obtenir_definition_wikipedia(terme):
    url = f"https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "titles": terme,
        "exchars": 300
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()), {})

    if 'extract' in page:
        # Nettoyer le texte HTML avec BeautifulSoup
        extrait_html = page['extract']
        extrait_texte = BeautifulSoup(extrait_html, 'html.parser').get_text()
        return extrait_texte
    else:
        return "Je n'ai pas trouvé de définition pour ce terme sur Wikipedia."

# Fonction pour apprendre une nouvelle réponse
def apprendre(question, nouvelle_reponse, donnees):
    if question not in donnees:
        donnees[question] = []
    
    # Ajouter la nouvelle réponse à la question
    if nouvelle_reponse not in donnees[question]:
        donnees[question].append(nouvelle_reponse)
        sauvegarder_donnees(donnees)
        print("Merci, j'ai appris quelque chose !")
    else:
        print("Cette réponse existe déjà.")

# Exemple d'utilisation
if __name__ == "__main__":
    donnees = charger_donnees()  # Charger les données existantes
    
    print("EchoBot est prêt. Tape une phrase (ou 'stop' pour quitter).")
    
    while True:
        # Demande à l'utilisateur de poser une question
        question = input("Toi : ")
        
        if question.lower() == 'stop':
            break
        
        # Obtenir une réponse
        reponse = repondre(question, donnees)
        print(f"EchoBot : {reponse}")
        
        # Si le chatbot ne sait pas répondre, demander ce qu'il doit dire
        if reponse == "Je n'ai pas trouvé de définition pour ce terme sur Wikipedia.":
            print("Je ne sais pas encore répondre à ça. Que dois-je dire ?")
            nouvelle_reponse = input("Ta réponse : ")
            apprendre(question, nouvelle_reponse, donnees)
