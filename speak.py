from cgitb import text
import pyttsx3

def speak(audio):

    print("     ")
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    print(voices[1].id)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',175)
    print("     ")
    print(f"FRIDAY :{audio}")
    engine.say(text=audio)
    engine.runAndWait()
    print("     ")



