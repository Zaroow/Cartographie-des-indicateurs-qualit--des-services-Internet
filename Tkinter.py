import os
from tkinter import *
import pandas as pd
import numpy as np

window=Tk()
window.geometry("400x550")
window.title("Projet 8")

def CleaningData():
    os.system('python Clean_Data.py')
#def ML():
#    os.system('python Clean_Data.py')
def Carte():
    os.system('python Carte.py')

label1=Label(window, text="APP", font=("arial", 16, "bold"))
label1.pack()

button1=Button(window, text="Clean Data", command=CleaningData)
button1.place(x=175, y=100)
#button2=Button(window, text="ML Processing", command=ML)
#button2.place(x=175, y=250)
button3=Button(window, text="Map Maker", command=Carte)
button3.place(x=175, y=400)

window.mainloop()