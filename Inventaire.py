#coding : utf-8
#Ewan GRIGNOUX LEVERT
#Avril 2020
import sys
import csv
from tkinter import *
import Chargement

def Inventaire(player):
    
    Plantes = Chargement.lireFichierCSV(f'Inventaire_{player}.csv')

    Inventaire_win = Toplevel()
    Inventaire_win.title('Inventaire')
    Inventaire_win.configure(bg='green')
    Inventaire_win.geometry('200x220+400+200')
    
    liste_inventaire = {}
    for i in range(20):
        if float(Plantes[i]['Quantité']) != 0 and Plantes[i]['Plante'] != "vide":
            liste_inventaire[Plantes[i]['Plante']] = Plantes[i]['Quantité']

    liste1, liste2 = "", ""
    for cle in liste_inventaire.keys():
        liste1 += cle
        liste1 += "\n"

    for valeur in liste_inventaire.values():
        liste2 += valeur
        liste2 += "\n"

    a = Label(Inventaire_win, text=liste1, fg='yellow',bg='green', font=('Candara', 20) )
    a.grid(row = 0, column =0, padx=5,pady=5)
    b = Label(Inventaire_win, text=liste2, fg='yellow',bg='green', font=('Candara', 20) )
    b.grid(row = 0, column =1, padx=5,pady=5)
    
    Inventaire_win.mainloop()
    sys.exit()