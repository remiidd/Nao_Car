#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk
import time, sys

fenetre = Tk()
fenetre.title("NAO driver panel v0.1")

def showCalcs():
    if(var_check_1.get() == 0):
        calcs.grid_forget()
    elif(var_check_1.get() == 1):
        calcs.grid(row=7, column=1)
    
def getScript():
    if(var_choix.get() == 0):
        zone.create_image(image=img_clean)
    elif(var_choix.get() == 1):
        zone.create_image(image=img_filtre)
    else:
        zone.create_image(image=img_clean)
        
def flux():
    img_clean = ImageTk.PhotoImage(Image.open("C:/Users/remi/camImage_f.png"))
    img_filtre = ImageTk.PhotoImage(Image.open("C:/Users/remi/sobel.png"))
    if(var_choix.get() == 0):
        im_nao.configure(image=img_clean)
        im_nao.image = img_clean
    elif(var_choix.get() == 1):
       im_nao.configure(image=img_filtre)
       im_nao.image = img_filtre
    else:
        im_nao.configure(image=img_clean)
        im_nao.image = img_clean

titre_menu = Label(fenetre, text="Configuration")


var_choix = IntVar()
choix_im = Radiobutton(fenetre, text="Vue du Nao", variable=var_choix, value=0, command = lambda : getScript())
choix_sobel = Radiobutton(fenetre, text="Vue du filtre", variable=var_choix, value=1, command = lambda : getScript())
var_check_1 = IntVar()
var_check_2 = IntVar()
case_1 = Checkbutton(fenetre, text="Afficher les calculs de trajectoire", variable=var_check_1, command=showCalcs)
case_2 = Checkbutton(fenetre, text="Afficher la visualisation de la trajectoire", variable=var_check_2)

calcs = Label(fenetre, text="n/d = z degrees")

im_c = Image.open("C:/Users/remi/camImage.png")
im_f = Image.open("C:/Users/remi/sobel.png")
img_clean = ImageTk.PhotoImage(im_c)
img_filtre = ImageTk.PhotoImage(im_f)

zone = Canvas(fenetre, width=320, height=240)
zone.create_image(0,0, anchor = NW, image=img_clean)
zone.create_line(0,0,200,200, fill="red")

refresh = Button(fenetre, text="refresh", command = lambda : flux())

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)

titre_menu.grid(row=1, column=1)
choix_im.grid(row=2, column=1, sticky=W)
choix_sobel.grid(row=3, column=1, sticky=W)
case_1.grid(row=5, column=1, sticky=W)
case_2.grid(row=6, column=1, sticky=W)
refresh.grid(row=8, column=1)
zone.grid(row=1, column=2, rowspan=10)
bouton_quitter.grid(row=10, column=1)

fenetre.mainloop()