import csv
import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import pywhatkit
import pyjokes
import pywhatsapp
import pywhatsapp_api
import pywhatsapp_api_client


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()     