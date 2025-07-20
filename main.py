import pyttsx3, os, tkinter,spacy
import speech_recognition as sr
from tkinter import * 
# import tkinter as tk


win = Tk()
win.title("Airavat")
win.geometry("600x400")

opt = StringVar(win)



opt.set("Select Voice")
Voices_GUI = ["voice1","voice2","voice3"]
Voption = OptionMenu(win, opt , *Voices_GUI)
Voption.pack()

win.mainloop()