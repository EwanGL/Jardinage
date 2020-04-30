#coding : utf-8
#Ewan GRIGNOUX LEVERT
#Avril 2020
from PIL import Image, ImageTk
import csv

def ChargementImage(ListeNom):
    ListeImages = {}
    for nom in ListeNom:
        img = Image.open(f"{nom}.png")
        ListeImages[nom] = ImageTk.PhotoImage(img)

    return ListeImages

def lireFichierCSV(nomFichier):
        tableau =[]
        with open (nomFichier, newline = '', encoding = 'utf-8') as fichier:
            lecteur = csv.DictReader(fichier, delimiter=',')
            for element in lecteur:
                tableau.append(element)
        return tableau