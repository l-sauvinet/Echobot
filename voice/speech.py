import pyttsx3

def parler(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
