import random
from brain.data import charger_donnees, sauvegarder_donnees
from brain.nlp import predire_question

memoire = charger_donnees()

def repondre(message):
    question = predire_question(message)
    if question in memoire:
        return random.choice(memoire[question])
    return None

def apprendre(question, reponse):
    if question not in memoire:
        memoire[question] = []
    if reponse not in memoire[question]:
        memoire[question].append(reponse)
        sauvegarder_donnees(memoire)
