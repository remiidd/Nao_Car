#!/usr/bin/env python3

from Tkinter import *
import ttk
from PIL import Image, ImageTk
import time, sys
from random import randrange
nbr = randrange(1,5)
nbrB = randrange(1,5)


fenetre = Tk()
fenetre.title("Espagnol")

if(nbr == 1):
    txt = Label(fenetre, text="Mythe et hero")
    txt.grid(row=1, column=1)
if(nbr == 2):
    txt = Label(fenetre, text="Espace et echange")
    txt.grid(row=1, column=1)
if(nbr == 3):
    txt = Label(fenetre, text="lieu et forme de pouvoir")
    txt.grid(row=1, column=1)
if(nbr == 4):
    txt = Label(fenetre, text="idee de progres")
    txt.grid(row=1, column=1)
    
    
if(nbrB == 1):
    txtA = Label(fenetre, text="Intro")
    txtA.grid(row=2, column=1)
if(nbrB == 2):
    txtA = Label(fenetre, text="Partie 1")
    txtA.grid(row=2, column=1)
if(nbrB == 3):
    txtA = Label(fenetre, text="Partie 2")
    txtA.grid(row=2, column=1)
if(nbrB == 4):
    txtA = Label(fenetre, text="Conclusion")
    txtA.grid(row=2, column=1)
    

fenetre.mainloop()