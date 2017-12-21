#!/usr/bin/env python

from Tkinter import *
import ttk
from PIL import Image, ImageTk
import time, sys

fenetre = Tk()
fenetre.title("NAO driver panel v0.5 - Remi Debray")

def showCalcs():
    if(var_check_1.get() == 0):
        calcs.grid_forget()
    elif(var_check_1.get() == 1):
        calcs.grid(row=7, column=1)

def showTraj():
    if(var_check_2.get() == 0):
        zone.coords(item_2, 0,0,0,0)
        zone.coords(item_3, 0,0,0,0)
        zone.coords(item_4, 0,0,0,0)
    elif(var_check_2.get() == 1):
        zone.coords(item_2, 60,0,160,240)
        zone.coords(item_3, 160,240,320,240)
        zone.coords(item_4, 80,180,240,360)
        zone.itemconfig(item_4, extent=108) #112 - [4]
    else:
        zone.coords(item_2, 0,0,0,0)
        zone.coords(item_3, 0,0,0,0)
        zone.coords(item_4, 0,0,0,0)

def getImage():
    if(var_choix.get() == 0):
        zone.itemconfig(item_1, image=img_clean)
    elif(var_choix.get() == 1):
        zone.itemconfig(item_1, image=img_filtre)
    else:
        zone.itemconfig(item_1, image=img_clean)
        
def flux():
    time.sleep(0.01)      
    img_clean = ImageTk.PhotoImage(Image.open("F:/Programs_Files/camImage.png"))
    img_filtre = ImageTk.PhotoImage(Image.open("F:/Programs_Files/sobel.png"))
    if(var_choix.get() == 0):
        zone.itemconfig(item_1, image=img_clean)
        zone.image = img_clean
    elif(var_choix.get() == 1):
        zone.itemconfig(item_1, image=img_filtre)
        zone.image = img_filtre
    else:
        zone.itemconfig(item_1, image=img_clean)
        zone.image = img_clean

titre_menu = Label(fenetre, text="Configuration")


var_choix = IntVar()
choix_im = Radiobutton(fenetre, text="Vue du Nao", variable=var_choix, value=0, command = lambda : getImage())
choix_sobel = Radiobutton(fenetre, text="Vue du filtre", variable=var_choix, value=1, command = lambda : getImage())
var_check_1 = IntVar()
var_check_2 = IntVar()
case_1 = Checkbutton(fenetre, text="Afficher les calculs de trajectoire", variable=var_check_1, command=showCalcs)
case_2 = Checkbutton(fenetre, text="Afficher la visualisation de la trajectoire", variable=var_check_2, command=showTraj)

calcs = Label(fenetre, text="n/d = z degrees")

im_c = Image.open("F:/Programs_Files/camImage.png")
im_f = Image.open("F:/Programs_Files/sobel.png")
img_clean = ImageTk.PhotoImage(im_c)
img_filtre = ImageTk.PhotoImage(im_f)

zone = Canvas(fenetre, width=320, height=240)
item_1 = zone.create_image(0,0, anchor = NW, image=img_clean)
item_2 = zone.create_line(0,0,0,0, width=4, fill="green")
item_3 = zone.create_line(0,0,0,0, width=4, fill="blue")
item_4 = zone.create_arc(0,0,0,0, style=ARC, width=4, outline="red", fill="blue")

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