#!/usr/bin/env python2
# -*- coding: utf8 -*-

import binascii
from PIL import Image
import sys

def usage():
	print "Utilisation du programme ./recumsg.py image.bmp fichier_de_sortie.txt"
	exit()

######################----MAIN------#############################

if len(sys.argv) < 3 or sys.argv[1]=="-h" or sys.argv[1]=="h" or sys.argv[1] == "help" :
        usage()

img = sys.argv[1]
imgsrc = Image.open(img)
largeur, hauteur = imgsrc.size
msgbin=''
msglenn=''

o=0
i=0
msglen=1
z=0

for y in range ( hauteur ) :#hauteur
        for x in range ( largeur ) :#largeur
                pix = imgsrc.load()
                r, g, b = (pix[x, y])
		verif=0
		#on recupére les 20 premier pixel qui vont nous donner la taille de notre message
		if o < 20:
			msglenn=msglenn +bin(r)[-1]
			msglenn=msglenn +bin(g)[-1]
			msglenn=msglenn +bin(b)[-1]
			o = o +1

		#quand on a nos 20 bits on les converti en décimal
		if o == 20 and z == 0:
			msglenn=int(msglenn)
			msglen=int('%i' % msglenn, 2)
			z=1
			verif=1
		#on récupere ensuite les bit de notre message
		if msglen > i and z==1 and verif==0:				
			msgbin=msgbin + bin(r)[-1]
			i = i + 1
		if msglen > i and z==1 and verif==0:
			msgbin=msgbin + bin(g)[-1]
			i = i + 1
		if msglen > i and z==1 and verif==0:
			msgbin=msgbin + bin(b)[-1]

			i = i + 1
		if msglen == i:
			break

t=int(msgbin, 2)
msg=binascii.unhexlify('%x' % t)
f = open(sys.argv[2], "a")
f.write(msg)
f.close()

