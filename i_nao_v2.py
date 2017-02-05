#!/usr/bin/env python

#version : 1
#Le Nao peux prendre une image, la sauvegarde. Ensuite il traite l'image pour determiner la direction a prendre

import sys, time, cv2, math
import numpy as np
from naoqi import ALProxy
from PIL import Image

def saveNaoImage(IP, PORT):

  camProxy = ALProxy("ALVideoDevice", IP, PORT)
  resolution = 1    # VGA
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  t0 = time.time()

  # photo
  naoImage = camProxy.getImageRemote(videoClient)

  t1 = time.time()

  # temps du transfer de l'image.
  #print "delais d'acquisition ", t1 - t0

  camProxy.unsubscribe(videoClient)

  # Donnees de l'image
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  # Creation de l'image PIL.
  im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

  # Sauvegarde de l'image.
  im.save("C:/Users/remi/camImage.png", "PNG")
  
def trajectoire():
	img = cv2.imread("C:/Users/remi/camImage.png")
		
	SOBEL = cv2.Sobel(img, -1, 1, 0)

	cv2.imwrite("C:/Users/remi/sobel.png", SOBEL)

	#print("filtre applique !")

	#creation des points
	#X = [x,y]
	a = [0,0]
	b = [0,0]
	c = [319 ,239]
	   
	img = cv2.imread("C:/Users/remi/sobel.png")
	blanc = cv2.imread("C:/Users/remi/Nao/white.png")

	px_w = blanc[0,0]

	#print("RGB blanc=",px_w[0])
	#print("RGB blanc=",px_w[1])
	#print("RGB blanc=",px_w[2])

	x=0
	while(x<319):
		px = img[5,x]
		if((px[0] > 130) and (px[1] > 130) and (px[2] > 130)):
			#print("x=",x)
			a = [x,0]
			break
		x = x+1
		
	xb=0
	while(xb<319):
		px = img[230,xb]
		if((px[0] > 130) and (px[1] > 130) and (px[2] > 130)):
			#print("x=",xb)
			b = [xb,239]
			break
		xb = xb+1
	 
	#print(a)
	#print(b)
	#print(c)
	   
	#calculs des coordonnes de vecteurs
	x_ba = a[0] - b[0]
	y_ba = a[1] - b[1]
	ba = [x_ba,y_ba]
	#print("vecteur ba =", ba)
	x_bc = c[0] - b[0]
	y_bc = c[1] - b[1]
	bc = [x_bc,y_bc]
	#print("vecteur bc =", bc)

	#numerateur
	n = ba[0]*bc[0] + ba[1]*bc[1]
	#denominateur
	d = math.sqrt(pow(ba[0],2)+pow(ba[1],2)) * math.sqrt(pow(bc[0],2)+pow(bc[1],2))
	#division
	z = n/d
	#print("z =",z)
	#calcul de l'angle
	z = math.degrees(math.acos(z))
	#print("z =",z)
		
	#determination de la direction a prendre
	direction = 0 #0=TOUT DROIT | 1=DROITE | 2=GAUCHE
	if(z<85):
		return(1)
	elif(z>84 and z<95):
		return(0)
	elif(z>94):
		return(2)
	else:
		return(0)
#DEBUT
if __name__ == '__main__':
  IP = "192.168.43.31"  # IP ET PORT DU NAO
  PORT = 9559
  
  if len(sys.argv) > 1:
    IP = sys.argv[1]

while(1):
  
  t0 = time.time()
  
  saveNaoImage(IP, PORT)

  if(trajectoire() == 0):
    print("tout droit !")
  elif(trajectoire() == 1):
    print("a droite !")
  elif(trajectoire() == 2):
    print("a gauche !")
  else:
    print("erreur")
  t1 = time.time()
  print "delais d'acquisition ", t1 - t0
    
