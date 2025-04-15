from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from brain.data import charger_donnees

vectorizer = CountVectorizer()
model = MultinomialNB()
X, y = [], []

def entrainer_modele():
    data = charger_donnees()
    global X, y
    X, y = [], []
    for question, reponses in data.items():
        for _ in reponses:
            X.append(question)
            y.append(question)
    if X:
        X_vect = vectorizer.fit_transform(X)
        model.fit(X_vect, y)

def predire_question(user_input):
    if not X:
        return None
    vect_input = vectorizer.transform([user_input])
    return model.predict(vect_input)[0]
