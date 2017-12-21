#!/usr/bin/env python

#version : 8
#Le programme est fonctionnelle

import sys, time, cv2, math                                  #Importation des differents modules
import numpy as np											 
from math import radians		                             #Ou des fonctions specifiques
from naoqi import ALProxy                                    #contenue dans des modules
from PIL import Image


def saveNaoImage(IP, PORT):                                  #Fonction pour prise d'images

	camProxy = ALProxy("ALVideoDevice", IP, PORT)              #definition du peripherique video
	resolution = 1                                             #definition de la resolution(320*240)
	colorSpace = 11   # RGB                                    #definition de l'oganisation des couleurs (RBG)

	videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5) #connexion au peripherique

    # photo
	naoImage = camProxy.getImageRemote(videoClient)            #prise de l'image

	camProxy.unsubscribe(videoClient)                          #deconnexion du peripherique

	imageWidth = naoImage[0]                                   # Donnees de l'image (Hauteur, largeur, densitee de pixel)
	imageHeight = naoImage[1]
	array = naoImage[6]

	im = Image.fromstring("RGB", (imageWidth, imageHeight), array) # Creation de l'image (PIL).

	im.save("F:/Programs_Files/camImage.png", "PNG")               # Sauvegarde de l'image sur le PC

def trajectoire():
	img = cv2.imread("F:/Programs_Files/camImage.png")           #Lecture de l'image
		
	SOBEL = cv2.Sobel(img, -1, 1, 0)                         #Modification de l'image pour appliquer un filtre de Sobel

	cv2.imwrite("F:/Programs_Files/sobel.png", SOBEL)            #Sauvegarde de la nouvelle image


	a = [0,0]                                                 #creation des points
	b = [0,0]                                                 #X = [x,y]
	c = [319 ,239]
	   
	img = cv2.imread("F:/Programs_Files/sobel.png")               #lecture de l'image avec le filtre

	#print("RGB blanc=",px_w[0])
	#print("RGB blanc=",px_w[1])
	#print("RGB blanc=",px_w[2])

	x=0															#pointeur mis a 0
	skip = 0													#initalisation de la variable skip a 0. Cette varible sert a passer 
																#une partie du programme quand il n'y a pas de lignes
	while(x<319):											   #temps que x est inferieur a la longueur total de l'image
		px = img[5,x]										   #couleur du pixel a la colonne x de la 5eme ligne
		if((px[0] > 150) and (px[1] > 150) and (px[2] > 150)): #si la couleur RGB se rapproche d'un gris clair/blanc
			#print("x=",x)
			a = [x,0]                                          #alors on enregistre cette colonne dans le point A
			break                                              #puis on sort de la boucle
		x = x+1                                                #sinon on passe on verifie la colonne suivante
	else:
		x=0
		while(x<319):											   #temps que x est inferieur a la longueur total de l'image
			px = img[40,x]										   #couleur du pixel a la colonne x de la 40eme ligne
			if((px[0] > 150) and (px[1] > 150) and (px[2] > 150)): #si la couleur RGB se rapproche d'un gris clair/blanc
				#print("x=",x)
				a = [x,0]                                          #alors on enregistre cette colonne dans le point A
				break                                              #puis on sort de la boucle
			x = x+1
		else:
			x=0
			while(x<319):											   #temps que x est inferieur a la longueur total de l'image
				px = img[80,x]										   #couleur du pixel a la colonne x de la 80eme ligne
				if((px[0] > 130) and (px[1] > 130) and (px[2] > 130)): #si la couleur RGB se rapproche d'un gris clair/blanc						#print("x=",x)
					a = [x,0]                                          #alors on enregistre cette colonne dans le point A
					break                                              #puis on sort de la boucle
				x = x+1
			else:
				skip = 1										#si aucune ligne a ete trouve, on passe les calculs et on va tout droit
		
	xb=0                                                       #meme chose pour le point B mais a la ligne B
	while(xb<319):
		px = img[130,xb]
		if((px[0] > 130) and (px[1] > 130) and (px[2] > 130)):
			#print("x=",xb)
			b = [xb,239]
			break
		xb = xb+1
	else:
		skip = 1

	#print(a)
	#print(b)
	#print(c)
	   
	x_ba = a[0] - b[0]                 #calculs des coordonnes de vecteurs
	y_ba = a[1] - b[1]
	ba = [x_ba,y_ba]
	#print("vecteur ba =", ba)
	x_bc = c[0] - b[0]
	y_bc = c[1] - b[1]
	bc = [x_bc,y_bc]
	#print("vecteur bc =", bc)

	#numerateur
	n = ba[0]*bc[0] + ba[1]*bc[1]     #multiblication des vecteurs
	#denominateur
	d = math.sqrt(pow(ba[0],2)+pow(ba[1],2)) * math.sqrt(pow(bc[0],2)+pow(bc[1],2)) #module des vecteurs
	#division
	if(skip==0):								#si une ligne a ete trouver on fait les calculs, sinon, on passe
		z = n/d
		#print("z =",z)
		z = math.degrees(math.acos(z))        #calcul de l'angle
		#print("z =",z)
		
	#determination de la direction a prendre
	direction = 0
	if(skip == 0):
		print(z)
		if(z>100):
			return(0)
		elif(z>95 and z<=100):
			return(3)
		elif(z<=95 and z>=85):
			return(2)
		elif(z<85 and z>=80):
			return(1)
		elif(z<80):
			return(4)
		else:
			return(2)
	else:
		return(0)
		skip = 0
	
def gauche(robotIP):
    PORT = 9559

    motionProxy = ALProxy("ALMotion", robotIP, PORT)                      #connexion aux moteurs
    motionProxy.setStiffnesses("RShoulderPitch", 1.0)                     #Mise en fonctionnement des moteurs
    motionProxy.setStiffnesses("RShoulderRoll", 1.0)                      #             |
    motionProxy.setStiffnesses("RElbowRoll", 1.0)                         #             |
    motionProxy.setStiffnesses("RElbowYaw", 1.0)                          #             |
    motionProxy.setStiffnesses("LShoulderPitch", 1.0)                     #             |
    motionProxy.setStiffnesses("LShoulderRoll", 1.0)                      #             |
    motionProxy.setStiffnesses("LElbowRoll", 1.0)                         #             |
    motionProxy.setStiffnesses("LElbowYaw", 1.0)                          #            \/
    motionProxy.setAngles("RShoulderPitch", radians(24.3), 0.2)           #Mouvement de chaques moteurs
    motionProxy.setAngles("RShoulderRoll", radians(6.6), 0.2)             #             |
    motionProxy.setAngles("RElbowRoll", radians(3.5), 0.6)                #             |
    motionProxy.setAngles("RElbowYaw", radians(93.9), 0.6)                #             |
    motionProxy.setAngles("LShoulderPitch", radians(84.6), 0.2)           #             |
    motionProxy.setAngles("LShoulderRoll", radians(-6.7), 0.2)            #             |
    motionProxy.setAngles("LElbowRoll", radians(-88.5), 0.6)              #             |
    motionProxy.setAngles("LElbowYaw", radians(-91.4), 0.6)               #            \/
    time.sleep(0.5)                                                       #temps d'attente pour les moteurs

def gauchemoitie(robotIP):
    PORT = 9559
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    motionProxy.setStiffnesses("RShoulderPitch", 1.0)
    motionProxy.setStiffnesses("RShoulderRoll", 1.0)
    motionProxy.setStiffnesses("RElbowRoll", 1.0)
    motionProxy.setStiffnesses("RElbowYaw", 1.0)
    motionProxy.setStiffnesses("LShoulderPitch", 1.0)
    motionProxy.setStiffnesses("LShoulderRoll", 1.0)
    motionProxy.setStiffnesses("LElbowRoll", 1.0)
    motionProxy.setStiffnesses("LElbowYaw", 1.0)
    motionProxy.setAngles("RShoulderPitch", radians(75), 0.2)
    motionProxy.setAngles("RShoulderRoll", radians(5.9), 0.2)
    motionProxy.setAngles("RElbowRoll", radians(70), 0.6)
    motionProxy.setAngles("RElbowYaw", radians(94), 0.6)
    motionProxy.setAngles("LShoulderPitch", radians(46), 0.2)
    motionProxy.setAngles("LShoulderRoll", radians(-6.5), 0.2)
    motionProxy.setAngles("LElbowRoll", radians(-30), 0.6)
    motionProxy.setAngles("LElbowYaw", radians(-93.4), 0.6)
    time.sleep(0.5)


def droite(robotIP):
    PORT = 9559
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    motionProxy.setStiffnesses("RShoulderPitch", 1.0)
    motionProxy.setStiffnesses("RShoulderRoll", 1.0)
    motionProxy.setStiffnesses("RElbowRoll", 1.0)
    motionProxy.setStiffnesses("RElbowYaw", 1.0)
    motionProxy.setStiffnesses("LShoulderPitch", 1.0)
    motionProxy.setStiffnesses("LShoulderRoll", 1.0)
    motionProxy.setStiffnesses("LElbowRoll", 1.0)
    motionProxy.setStiffnesses("LElbowYaw", 1.0)
    motionProxy.setAngles("RShoulderPitch", radians(85.5), 0.2)
    motionProxy.setAngles("RShoulderRoll", radians(5.9), 0.2)
    motionProxy.setAngles("RElbowRoll", radians(86), 0.6)
    motionProxy.setAngles("RElbowYaw", radians(94), 0.6)
    motionProxy.setAngles("LShoulderPitch", radians(28.1), 0.2)
    motionProxy.setAngles("LShoulderRoll", radians(-6.5), 0.2)
    motionProxy.setAngles("LElbowRoll", radians(-4.6), 0.6)
    motionProxy.setAngles("LElbowYaw", radians(-93.4), 0.6)
    time.sleep(0.5)
    
def droitemoitie(robotIP):
    PORT = 9559
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    motionProxy.setStiffnesses("RShoulderPitch", 1.0)
    motionProxy.setStiffnesses("RShoulderRoll", 1.0)
    motionProxy.setStiffnesses("RElbowRoll", 1.0)
    motionProxy.setStiffnesses("RElbowYaw", 1.0)
    motionProxy.setStiffnesses("LShoulderPitch", 1.0)
    motionProxy.setStiffnesses("LShoulderRoll", 1.0)
    motionProxy.setStiffnesses("LElbowRoll", 1.0)
    motionProxy.setStiffnesses("LElbowYaw", 1.0)
    motionProxy.setAngles("RShoulderPitch", radians(40), 0.2)
    motionProxy.setAngles("RShoulderRoll", radians(5.9), 0.2)
    motionProxy.setAngles("RElbowRoll", radians(32), 0.6)
    motionProxy.setAngles("RElbowYaw", radians(94), 0.6)
    motionProxy.setAngles("LShoulderPitch", radians(72), 0.2)
    motionProxy.setAngles("LShoulderRoll", radians(-6.5), 0.2)
    motionProxy.setAngles("LElbowRoll", radians(-72), 0.6)
    motionProxy.setAngles("LElbowYaw", radians(-93.4), 0.6)
    time.sleep(0.5)


def avant(robotIP):
    PORT = 9559
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    motionProxy.setStiffnesses("RShoulderPitch", 1.0)
    motionProxy.setStiffnesses("RShoulderRoll", 1.0)
    motionProxy.setStiffnesses("RElbowRoll", 1.0)
    motionProxy.setStiffnesses("RElbowYaw", 1.0)
    motionProxy.setStiffnesses("LShoulderPitch", 1.0)
    motionProxy.setStiffnesses("LShoulderRoll", 1.0)
    motionProxy.setStiffnesses("LElbowRoll", 1.0)
    motionProxy.setStiffnesses("LElbowYaw", 1.0)
    motionProxy.setAngles("RShoulderPitch", radians(54.9), 0.2)
    motionProxy.setAngles("RShoulderRoll", radians(6.6), 0.2)
    motionProxy.setAngles("RElbowRoll", radians(58.75), 0.6)
    motionProxy.setAngles("RElbowYaw", radians(93.9), 0.6)
    motionProxy.setAngles("LShoulderPitch", radians(56.35), 0.2)
    motionProxy.setAngles("LShoulderRoll", radians(-6.7), 0.2)
    motionProxy.setAngles("LElbowRoll", radians(-57.55), 0.6)
    motionProxy.setAngles("LElbowYaw", radians(-91.4), 0.6)
    time.sleep(0.5)

if __name__ == '__main__':                                                    #debut du programme
	IP = "192.168.43.31"                                                      # IP ET PORT DU NAO
	PORT = 9559

	if len(sys.argv) > 1:
	    IP = sys.argv[1]

while(1):                                                                    #boucle infinie
    t0 = time.time()                                                         #l'heure au point au au debut de la boucle

    saveNaoImage(IP, PORT)                                                   #lancement de la fonction pour la capture d'une image

    if(trajectoire() == 0):                                                  #determination des mouvement en fonction de la trajectoire
        gauche(IP)
        print("a gauche")
    elif(trajectoire() == 1):
        gauchemoitie(IP)
        print("a moitie a gauche")
    elif(trajectoire() == 2):
        avant(IP)
        print("tout droit")
    elif(trajectoire() == 3):
        droitemoitie(IP)
        print("a moitie a gauche")
    elif(trajectoire() == 4):
        droite(IP)
        print("a gauche")
    else:
        print("erreur")
    t1 = time.time()                                                          #l'heure a la fin de la boucle
    print "delais d'acquisition ", t1 - t0                                    #delta des heures pour avoir le delais et affichage du delais

