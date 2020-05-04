#coding : utf-8
#Ewan GRIGNOUX LEVERT
#Avril 2020
import sys
import csv
from tkinter import *
from tkinter.messagebox import *

def Marché(player, new):

    Marche_win = Toplevel()
    Marche_win.title("Marché")
    frame = Frame(Marche_win, bg='green')
    frame.pack(expand = YES)

    def lireFichierCSV(nomFichier):
            tableau =[]
            with open (nomFichier, newline = '', encoding = 'utf-8') as fichier:
                lecteur = csv.DictReader(fichier, delimiter=',')
                for element in lecteur:
                    tableau.append(element)
            return tableau

    def Vendre_function():
        prix = 
        
        if askyesno('Vendre',f'Voulez-vous vendre {Quantite.get()}, pour {prix} €?')

    
    if new == False:
        semis = lireFichierCSV(f'Inventaire_{player}')
    else:
        semis = lireFichierCSV('Semis.csv')

    dict_produits = {}
    for i in range(20):
        if int(Plantes[i]['Quantite']) != 0:
            dict_produit[Plantes[i]['Plante']] = Plantes[i]['Quantite']

    liste_produits = []
    for cle in liste_inventaire.keys():
    liste_produits.append(cle)
    
    produit = ttk.Combobox(frame, values=liste_produit ,width=15, fg='yellow',bg='green', font=('Candara', 20))
    produit.pack(padx=5,pady=5)

    prod = produit.get
    max = dict_produits[prod]

    Quantite = Spinbox(frame, from_=0, to=max)
    Quantite.pack(padx=5,pady=5)

    vendre_button = Button(frame, text='Vendre', command = Vendre_function, fg='yellow',bg='green', font=('Candara', 20)))

    Marche_win.mainloop()
    sys.exit()