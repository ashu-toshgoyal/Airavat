import pyttsx3, os, tkinter, spacy,plyer
import speech_recognition as sr
# from ttkbootstrap import *
# from ttkbootstrap.widgets import *
# from ttkbootstrap.constants import *
# from tkinter import *
import datetime
import random
import pywhatkit
import time
import webbrowser
# import tkinter as tk
import time
import os
import wikipedia

splash_text = """
############################################
#                                          #
#         MADE BY ASHU AND MANYA           #
#                                          #
#         WELCOME TO PROJECT ARIA          #
#                                          #
############################################
"""
Introduction = '''Hello, I’m Aria — a smart virtual assistant developed with care by Ashu and Manya. I’m designed to make your digital life easier, faster, and a bit more fun. From answering your questions and searching the internet, to opening apps, reading things out loud, or reminding you about your day — I can do a lot. I’m still learning and evolving, but I’m always ready to assist you with whatever you need. Just say the word, and I’ll be there.'''

r = sr.Recognizer()
def Ytopen_Search():
    webbrowser.open("https://www.youtube.com/")

def Wikipedia_search(order_wiki,sentencenumber):
    wikipedia.search(order_wiki,sentencenumber)

# def Time(da):
#     nows = datetime.datetime.now()
#     date = datetime.date.today()
#     if da == 1:




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
    "System online. All functions operational, awaiting your command.",
    "Initializing neural core... complete. Aria is now active.",
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

def aria_speak_listen():#main working function
    while True:

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = r.listen(source)

            try:
                query = r.recognize_google(audio)
                print(f"User said: {query}")
                query = query.lower()

                if any(phrase in query for phrase in [
                    "aria shutdown", "exit program", "go to sleep", 
                    "terminate the core", "power off yourself", "bye aria", "fuck off"]):
                    
                    shutdown_lines = [
                        "Acknowledged. Powering down systems.",
                        "Command received. Going offline.",
                        "Shutting down. As per your command.",
                        "Logging out. No further activity expected.",
                        "System disengaged. Awaiting further orders.",
                        "Understood. Session terminated.",
                        "All operations suspended. Goodbye.",
                        "Offline protocols initiated. See you on the next directive.",
                        "Exiting all active states. Signing off.",
                        "Mission aborted. Going silent."
                    ]
                    
                    speak_aria(random.choice(shutdown_lines))
                    break

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
                elif ("search" in query and "youtube" in query) or ("search" in query and "youtube" in query):
                    search_term = query.replace("search", "").replace("on youtube", "").strip()
                    url = f"https://www.youtube.com/results?search_query={search_term.replace(' ', '+')}"
                    webbrowser.open(url)
                elif ("introduce" in query and "yourself" in query):
                    print(splash_text)
                    speak_aria(Introduction)

                elif "open" in query and "youtube" in query:
                    speak_aria("Openning Youtube")
                    Ytopen_Search()
                elif "what's the date" in query or "what is the date" in query or "today's date" in query or "tell me the date" in query or "date today" in query or "can you tell the date" in query or "which date is it" in query or "current date" in query:
                    from datetime import datetime
                    date_today = datetime.now().strftime("%A, %d %B %Y")
                    speak_aria(f"Today is {date_today}")
                elif "what's the time" in query or "what is the time" in query or "today's time" in query or "tell me the time" in query or "time today" in query or "can you tell the time" in query or "which time is it" in query or "current time" in query:
                    from datetime import datetime
                    time_today = datetime.now().strftime("%I:%M %p")
                    speak_aria(f"It's {time_today}")
                




                elif "are you from hogwarts" in query or "do you know hogwarts" in query or "are you a wizard" in query or "potter" in query or "lumos" in query :
                    responses = [
                        "I'm not from Hogwarts, but I did take a few online classes from Dumbledore.",
                        "I solemnly swear that I am up to no good.",
                        "10 points to Gryffindor for asking!",
                    ]
                    speak_aria(random.choice(responses))


            except sr.UnknownValueError:
                print("Please try again")
                speak_aria("Sorry, I didn't catch that.")
            except sr.RequestError:
                print("Speech service error.")
                speak_aria("There was an issue with the speech service.")



greet()
aria_speak_listen()

     


##########      #        #          ###########   
#               #        #               #   
#               #        #               #   
#   ####        #        #               #  
#      #        #        #               #
########        ##########          ############    




