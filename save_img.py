#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
# Prendre une image depuis le NAO

import sys, time, Image
from naoqi import ALProxy


def saveNaoImage(IP, PORT):

  camProxy = ALProxy("ALVideoDevice", IP, PORT)
  resolution = 2    # VGA
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  t0 = time.time()

  # photo
  naoImage = camProxy.getImageRemote(videoClient)

  t1 = time.time()

  # temps du transfer de l'image.
  print "delais d'acquisition ", t1 - t0

  camProxy.unsubscribe(videoClient)

  # Donnees de l'image
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  # Creation de l'image PIL.
  im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

  # Sauvegarde de l'image.
  im.save("camImage.png", "PNG")

  im.show()



if __name__ == '__main__':
  IP = "nao.local"  # IP ET PORT DU NAO
  PORT = 9559

  if len(sys.argv) > 1:
    IP = sys.argv[1]

  naoImage = saveNaoImage(IP, PORT)

