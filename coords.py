#!/usr/bin/env python

import math, numpy as np

a = [60,0]
b = [160,240]
c = [320,240]

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
z = math.degrees(math.acos(n/d))

print(z)