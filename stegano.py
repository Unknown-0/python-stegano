#!/usr/bin/env python2
# -*- coding: utf8 -*-

import binascii
from PIL import Image
import sys
import os

def dec2bin(d,nb=0):

    if d==0:
        b="0"
    else:
        b=""
        while d!=0:
            b="01"[d&1]+b
            d=d>>1
    return b.zfill(nb)

def usage():
		print "Utilisation du programme ./stegano.py imagesource.bmp imagedestination.bmp 'votre message a dissimuler'"
		exit()
#######################-----Main-----#######################
if len(sys.argv) < 3 or sys.argv[1]=="-h" or sys.argv[1]=="h" or sys.argv[1] == "help" :
	usage()
msgascii= sys.argv[3]
imgsource = sys.argv[1]
imgdestination = sys.argv[2]
#on traduit le message saisi en binaire
msgbin = bin(int(binascii.hexlify(msgascii), 16))[2:]

#On ouvre l'image source, on recupere sa taille et on crée l'image de destination de même taille
imgsrc = Image.open(imgsource)
largeur, hauteur = imgsrc.size
imgdst = Image.open(imgsource)
#On defini des compteur et des variables 
# msgbin = notre message passé en binaire
# msgbinlen = longueur de notre message  binaire
# msglen = longueur de notre message binaire en binaire
# f = nombre de bit reservé pour sotcker "msglen"
i=0
e=0
compteur=0
msgbinlen=len(msgbin)
f=60
msglen=dec2bin(msgbinlen,f)
#on parcours l'image pixel par pixel de haut en bas et de gauche a droite
for y in range ( hauteur ) :
	for x in range ( largeur ) :
		#on récupere les valeur RGB du pixel en cours
		pix = imgsrc.load()
		r, g, b = (pix[x, y])
		verif2=0
		if e < f :
                        rr = (bin(r))[2:]
                        rr = rr[:-1] + msglen[e]
                        r=int(rr,2)
                        e = e +1
               		gg = (bin(g))[2:]
                        gg = gg[:-1] + msglen[e]
                        g=int(gg,2)
                        e = e +1
                        bb = (bin(b))[2:]
                        bb = bb[:-1] + msglen[e]
                        b=int(bb,2)
			e = e +1
			verif2=1
		#On place les bits de notre message dans les bit de poid faible de la couleur rouge de chaue pixel	
		if i < msgbinlen and verif2==0:
			rr = (bin(r))[2:]
			rr = rr[:-1] + msgbin[i]
			r=int(rr,2)
			i = i +1
		if i < msgbinlen and verif2==0:
                        gg = (bin(g))[2:]
                        gg = gg[:-1] + msgbin[i]
                        g=int(gg,2)
			i = i +1
		if i < msgbinlen and verif2==0:
                        bb = (bin(b))[2:]
                        bb = bb[:-1] + msgbin[i]
                        b=int(bb,2)
			i = i + 1
		#on place notre valeur modifier dans le pixel de la nouvelle image		
		imgdst.putpixel((x, y), (r, g, b))
		if i == msgbinlen:
			 
			break
	if i == msgbinlen:
                        break
imgdst.save(imgdestination)
print "Votre message a bien était ajouté à l'image" 
