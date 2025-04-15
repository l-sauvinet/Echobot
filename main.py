from flask import Flask, render_template, request, jsonify
import wikipedia
from deep_translator import GoogleTranslator
import difflib
from langdetect import detect
import json
import random
import wikipedia

app = Flask(__name__)

# Fonction pour charger les données à partir de data.json
def charger_donnees():
    with open('data/data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Fonction pour répondre en fonction de la question
def repondre(question, donnees):
    question = question.lower().strip()  # Met en minuscule pour éviter les soucis de casse
    if question in donnees:
        return random.choice(donnees[question])
    else:
        return wikipedia_summary(question)

# Fonction pour récupérer un résumé de Wikipedia
def wikipedia_summary(question):
    try:
        # Traduire la question en anglais pour la recherche
        question_en = GoogleTranslator(source='fr', target='en').translate(question)
        wikipedia.set_lang("en")

        # Essayer de récupérer un résumé direct
        summary = wikipedia.summary(question_en, sentences=2)
        return GoogleTranslator(source='en', target='fr').translate(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        # Trouver la meilleure correspondance parmi les choix
        best_match = difflib.get_close_matches(question_en, e.options, n=1, cutoff=0.2)
        if best_match:
            try:
                summary = wikipedia.summary(best_match[0], sentences=2)
                return GoogleTranslator(source='en', target='fr').translate(summary)
            except:
                pass

        # Si aucune correspondance fiable, essayer manuellement le mot avec "country"
        try:
            alt_query = f"{question_en} (country)"
            summary = wikipedia.summary(alt_query, sentences=2)
            return GoogleTranslator(source='en', target='fr').translate(summary)
        except:
            pass

        return "Il y a plusieurs significations possibles. Essayez d'être plus précis."

    except wikipedia.exceptions.PageError:
        return "Désolé, je n'ai pas trouvé de page correspondant à cette question."

    except Exception as e:
        return f"Une erreur est survenue : {str(e)}"
# Route pour l'index
@app.route('/')
def index():
    return render_template('index.html')

# Route pour gérer la question du chatbot
@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    if question:
        donnees = charger_donnees()
        reponse = repondre(question, donnees)
    else:
        reponse = "Veuillez poser une question."
    return jsonify({"reponse": reponse})

# Démarre le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
