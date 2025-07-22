import pyttsx3, os, tkinter, spacy,plyer
import speech_recognition as sr
from ttkbootstrap import *
from tkinter import *
import datetime
import random
import pywhatkit
import time
import webbrowser
import wikipedia

r = sr.Recognizer()
def Ytopen_Search(order):
    pywhatkit.playonyt(order)

def Wikipedia_search(order_wiki,sentencenumber):
    wikipedia.search(order_wiki,sentencenumber)


def ariavoice(): #voice function
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[150].id)
    return engine

def greet(): #greeting funtion
    engine = ariavoice()
    now = datetime.datetime.now()
    hours = now.hour

    greetings = [
    "Awaiting your command.",
    "Aria is now online and ready.",
    "Aria is synced and standing by.",
    ]


    chosen = random.choice(greetings)

    if 5 <= hours < 12:
        engine.say("Good morning sir.")
    elif 12 <= hours < 18:
        engine.say("Good afternoon sir.")
    else:
        engine.say("Good evening sir.")

    engine.say(chosen)
    engine.runAndWait()


def speak_aria(text): #Speak the text function
    try:
        engine = ariavoice()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"[ERROR] TTS Failed: {e}")

def aria_speak_listen(): #main working function
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print(f"User said: {query}")
            query = query.lower()


            if ("open" in query and "youtube" in query) or ("search" in query and "youtube" in query):
                search_term = query.replace("search", "").replace("on youtube", "").strip()
                url = f"https://www.youtube.com/results?search_query={search_term.replace(' ', '+')}"
                webbrowser.open(url)
        except:
            
            print("Please try again")
            speak_aria("Sorry, I didn't catch that.")


# greet()
# aria_speak_listen()



##########      #        #          ###########   
#               #        #               #   
#               #        #               #   
#   ####        #        #               #  
#      #        #        #               #
########        ##########          ############    
