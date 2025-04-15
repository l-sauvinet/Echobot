import speech_recognition as sr

def reconnaissance_vocale():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Echobot: Écoute en cours...")
        audio = recognizer.listen(source)
        
        try:
            texte = recognizer.recognize_google(audio, language="fr-FR")
            print(f"Vous avez dit : {texte}")
            return texte
        except sr.UnknownValueError:
            print("Echobot: Désolé, je n'ai pas compris.")
            return None
        except sr.RequestError:
            print("Echobot: Erreur de connexion avec le service Google.")
            return None
