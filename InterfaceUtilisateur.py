import os
import webbrowser
from tkinter import *
import pandas as pd
import numpy as np

##1) Creates the app window
window=Tk()
window.geometry("400x550")
window.title("Projet 8")

##2) Defines the python code calls
def CleaningData():
    os.system('python Clean_Data.py')
def Carte():
    os.system('python Carte2.py')
def AfficherMap():
    webbrowser.open('maCarte3.html')

##3) Creates the Title
label1=Label(window, text="APP", font=("arial", 16, "bold"))
label1.pack()

##4) Creating the buttons that calls definitions
button1=Button(window, text="Clean Data", command=CleaningData)
button1.place(x=175, y=100)
button3=Button(window, text="Map Updater", command=Carte)
button3.place(x=175, y=200)
button3=Button(window, text="Display map", command=AfficherMap)
button3.place(x=175, y=400)
window.mainloop()
