#!/usr/bin/env python3
import cv2, numpy as np, math
#setup de l'image avec le filtre
img = cv2.imread("C:/Users/remi/Nao/sol.png") #sol_b.png ou sol.png

SOBEL = cv2.Sobel(img, -1, 1, 0)

cv2.imwrite("C:/Users/remi/Nao/sobel.png", SOBEL)

print("filtre applique !")

#creation des points
#X = [x,y]
a = [0,0]
b = [0,0]
c = [1903,1067]

img = cv2.imread("C:/Users/remi/Nao/sobel.png")
blanc = cv2.imread("C:/Users/remi/Nao/white.png")

px_w = blanc[0,0]

print("RGB blanc=",px_w)

x=0
while(x<1903):
    px = img[0,x]
    if((px[0] == px_w[0]) and (px[1] == px_w[1]) and (px[2] == px_w[2])):
        print("x=",x)
        a = [x,0]
        break
    x = x+1
    
while(x<1903):
    px = img[1067,x]
    if((px[0] == px_w[0]) and (px[1] == px_w[1]) and (px[2] == px_w[2])):
        print("x=",x)
        b = [x,1067]
        break
    x = x+1
    
print(a)
print(b)
print(c)

#calculs des coordonnes de vecteurs
x_ba = a[0] - b[0]
y_ba = a[1] - b[1]
ba = [x_ba,y_ba]
print("vecteur ba =", ba)
x_bc = c[0] - b[0]
y_bc = c[1] - b[1]
bc = [x_bc,y_bc]
print("vecteur bc =", bc)

#calculs de l'angle
#formule :    cos(ABC) = (Vba.Vbc)/(BA*BC)            //Vba = Vecteur BA

#numerateur
n = ba[0]*bc[0] + ba[1]*bc[1]
#denominateur
d = math.sqrt(pow(ba[0],2)+pow(ba[1],2)) * math.sqrt(pow(bc[0],2)+pow(bc[1],2))
#division
z = n/d
print("z =",z)
#calcul de l'angle
z = math.degrees(math.acos(z))
print("z =",z)

#determination de la direction a prendre
direction = 0 #0=TOUT DROIT | 1=DROITE | 2=GAUCHE
if(z<85):
    direction = 1
elif(z>84 and z<95):
    direction = 0
elif(z>94):
    direction = 2
else:
    direction = 0
    
if(direction == 0):
    print("tout droit !")
elif(direction == 1):
    print("a droite !")
elif(direction == 2):
    print("a gauche !")
else:
    print("erreur")
    
    
    