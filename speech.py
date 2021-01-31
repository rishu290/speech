import speech_recognition as sr
import pyttsx3

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(t):
    engine.say(t)
    engine.runAndWait()
    
try:
    with sr.Microphone() as source:
        print("Start Speaking")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        talk(command)
except:
    pass
