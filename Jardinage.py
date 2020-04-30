#coding : utf-8
#Ewan GRIGNOUX LEVERT
#Avril 2020
import sys
import csv
from tkinter import *
from PIL import Image, ImageTk # pour les images
from tkinter import ttk
from tkinter.messagebox import*
from datetime import *

# MISSION 1 : Lecture du fichier CSV


def lireFichierCSV(nomFichier):
    tableau =[]
    with open (nomFichier, newline = '', encoding = 'utf-8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter=',')
        for element in lecteur:
            tableau.append(element)
    return tableau

plantations = lireFichierCSV('Classeur.csv')
Plantes = lireFichierCSV('Semis.csv')


# MISSION 2 : Affichage des données enregistrées

def cliquer(n):
    return lambda: afficherInfos(n)

def indice_plante(plante,liste):
    indice = 0
    for indice in range(len(liste)):
        if liste[indice] == plante:
            return indice
    return 0
    


def afficherInfos(n):
    
    # Ouverture de la fenêtre d'affichage
    dialogue = Toplevel()
    dialogue.title(f'Parcelle n°{n+1}')
    
    liste_semis = []
    for i in range(19):
        liste_semis.append(Plantes[i]['Plante'])
    
    
    semis = ttk.Combobox(dialogue, values=liste_semis ,width=10)
    semis.current(indice_plante(plantations[n]['semis'],liste_semis))    
    txtsemis = Label(dialogue, text = 'Graines semmées: ', fg = 'yellow', bg = 'green')
    semis.grid(row=0, column = 1, padx=5, pady=5)
    txtsemis.grid(row=0, column = 0, padx=5, pady=5)
    
    levée = StringVar()
    
    récolte = StringVar()
    
    if plantations[n]['semis'] != 'vide':
        d = datetime.now()
        def CalculDateLevée(d):
            for i in range (0,19):
                if Plantes[i]['Plante'] == semis.get():
                    tps_levée = int(Plantes[i]['Levée'])
                
            d2 = d + timedelta(days=tps_levée)
            dfl = datetime(d2.year, d2.month, d2.day, d2.hour, d2.minute, d2.second)

            if plantations[n]['date_levée'] == '':
                with open('Classeur.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                    titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                    ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                    ecrivain.writeheader()
                    plantations[n]['date_levée'] = d2
                    for compartiment in plantations:
                        ecrivain.writerow(compartiment)

            return dfl

        def CalculDateRécolte(d):
            for i in range (0,19):
                if Plantes[i]['Plante'] == semis.get():
                    tps_récolte = int(Plantes[i]['Récolte'])
                
            d2 = d + timedelta(days=tps_récolte)

            if plantations[n]['date_récolte'] =='':
                with open('Classeur.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                    titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                    ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                    ecrivain.writeheader()
                    plantations[n]['date_récolte'] = d2
                    for compartiment in plantations:
                        ecrivain.writerow(compartiment)
                
            return d2

        CalculDateLevée(d)
        CalculDateRécolte(d)

        levée.set(plantations[n]['date_levée'])
        saisie_levée = Entry(dialogue, textvariable = levée, width = 17)
        txtlevée = Label(dialogue, text = 'Date de levée: ', fg = 'yellow', bg = 'green')
        saisie_levée.grid(row=2, column=1, padx=5, pady=5)
        txtlevée.grid(row=2, column =0, padx=5, pady=5)

        récolte.set(plantations[n]['date_récolte'])
        saisie_récolte = Entry(dialogue, textvariable = récolte, width = 17)
        txtrécolte = Label(dialogue, text = 'Date de récolte: ', fg = 'yellow', bg = 'green')        
        saisie_récolte.grid(row=3, column=1, padx=5, pady=5)
        txtrécolte.grid(row=3, column = 0, padx=5, pady=5)

    def crop_function():
        def function():
            for i in range (0,19):
                if Plantes[i]['Plante'] == semis.get():
                    type_plante = Plantes[i]['Types']
            with open('Classeur.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                    titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                    ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                    ecrivain.writeheader()
                    plantations[n]['type_avant'] = type_plante
                    plantations[n]['date_récolte'] = ''
                    plantations[n]['date_levée'] = ''
                    plantations[n]['date_semis'] = ''
                    plantations[n]['semis'] = 'vide'
                    plantations[n]['arroser'] = 'no'
                    for compartiment in plantations:
                        ecrivain.writerow(compartiment)
            dialogue.destroy()
            actualiser()
        
        
        now = str(datetime.now())
        if now > str(plantations[n]['date_récolte']):
            function()
        else:
            if askyesno('Attention', "Si vous récolté maintenant, vous ne récupéré rien! \n Voulez-vous tout de même récolter?"):
                function()
            else:
                dialogue.destroy()
                actualiser()

    def infos_function():
        for i in range (0,19):
            if Plantes[i]['Plante'] == plantations[n]['semis']:
                données_infos = Plantes[i]['Informations'] + "\n\n" + "Type: " + Plantes[i]['Types']
        Informations = Toplevel()
        Informations.title('Informations')
        Informations.geometry('250x300+500+350')
        Informations.config(bg = 'green')
        txt_infos = Label(Informations, text = données_infos, fg ='yellow', bg ='green', wraplength = 200)
        txt_infos.pack()
    
    
    def modifierInfos():
        if plantations[n]['arroser'] == 'yes':
            for i in range (0,19):
                if Plantes[i]['Plante'] == semis.get():
                    type_plante = Plantes[i]['Types']
        
            if type_plante != plantations[n]['type_avant']:
                with open('Classeur.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                    titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                    ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                    ecrivain.writeheader()
                    plantations[n]['date_récolte'] = récolte.get()
                    plantations[n]['date_levée'] = levée.get()
                    plantations[n]['semis'] = semis.get()
                    plantations[n]['type_avant'] = type_plante
                    for compartiment in plantations:
                        ecrivain.writerow(compartiment)
                actualiser()
                dialogue.destroy()    
            else:
                showinfo('Important', 'Vous ne pouvez pas planter le même type de plante sur la même parcelle deux fois de suite!')
        else:
            showinfo('Important','Vous devez arroser la parcelle avant de pouvoir planter.')

    def engrais_function():
        with open('Classeur.csv', 'w', newline='', encoding = 'utf-8')as fichier:
            titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
            ecrivain = csv.DictWriter(fichier, fieldnames=titres)
            ecrivain.writeheader()
            plantations[n]['type_avant'] = 'none'
            for compartiment in plantations:
                ecrivain.writerow(compartiment)
        showinfo('Information', "La parcelle a retrouvé tous ses nutriments, vous pouvez désormais planter n'importe quel type de plante.")

    def arroser_function():
        with open('Classeur.csv', 'w', newline='', encoding = 'utf-8')as fichier:
            titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
            ecrivain = csv.DictWriter(fichier, fieldnames=titres)
            ecrivain.writeheader()
            plantations[n]['arroser'] = 'yes'
            for compartiment in plantations:
                ecrivain.writerow(compartiment)
        actualiser()
        showinfo('Information', "La parcelle a été arroser.")

    close = Button(dialogue, text ="Fermer", fg = 'yellow', bg = 'green', command = dialogue.destroy)
    close.grid(row=4, column = 0, padx=5, pady=5)
    
    infos = Button(dialogue, text='Informations', fg = 'yellow', bg = 'green', command = infos_function)
    infos.grid(row=5, column = 0, padx=5, pady=5)
    
    if plantations[n]['arroser'] == 'no':
        arroser_button = Button(dialogue, text='Arroser', fg = 'yellow', bg = 'green', command =arroser_function)
        arroser_button.grid(row=5, column=1, padx=5, pady=5)

    if plantations[n]['semis'] == 'vide':
        save = Button(dialogue, text="Planter", fg = 'yellow', bg = 'green', command = modifierInfos)
        save.grid(row=4, column=1, padx=5, pady=5)

    if plantations[n]['semis'] == 'vide':
        engrais_button = Button(dialogue, text='Engrais', fg = 'yellow', bg = 'green', command = engrais_function)
        engrais_button.grid(row=4, column=2, padx=5, pady=5)
    
    if plantations[n]['semis'] != 'vide':
        crop = Button(dialogue, text="Récolter", fg = 'yellow', bg = 'green', command = crop_function)
        crop.grid(row=5, column=1, padx=5, pady=5)

    dialogue.geometry('400x250+450+300')
    dialogue.config(bg = 'green')

# La fenêtre principale
maFenetre = Tk()
# Réglage des paramètres
maFenetre.title("Champs")  # Le titre
maFenetre.geometry('420x420+400+200')  # La position
maFenetre.configure(bg = 'green')  # la couleur de fond

# Chargement des images
imgvide = Image.open("vide.png")
vide = ImageTk.PhotoImage(imgvide)

imgaubergine = Image.open("Aubergine.png")
Aubergine = ImageTk.PhotoImage(imgaubergine)

imgbetterave = Image.open("Betterave.png")
Betterave = ImageTk.PhotoImage(imgbetterave)

imgcarotte = Image.open("Carotte.png")
Carotte = ImageTk.PhotoImage(imgcarotte)

imgceleri = Image.open("Céleri.png")
Celeri = ImageTk.PhotoImage(imgceleri)

imgbrocoli = Image.open("Chou brocoli.png")
Brocoli = ImageTk.PhotoImage(imgbrocoli)

imgcdb = Image.open("Chou de Bruxelles.png")
CdB = ImageTk.PhotoImage(imgcdb)

imgcf = Image.open("Chou fleur.png")
Cf = ImageTk.PhotoImage(imgcf)

imgconcombre = Image.open("Concombre.png")
Concombre = ImageTk.PhotoImage(imgconcombre)

imgepinard = Image.open("Epinard.png")
Epinard = ImageTk.PhotoImage(imgepinard)

imghv = Image.open("Haricot vert.png")
Hv = ImageTk.PhotoImage(imghv)

imglaitue = Image.open("Laitue.png")
Laitue = ImageTk.PhotoImage(imglaitue)

imgva = Image.open("vide_arroser.png")
Va = ImageTk.PhotoImage(imgva)

imgmelon = Image.open("Melon.png")
Melon = ImageTk.PhotoImage(imgmelon)

imgnavet = Image.open("Navet.png")
Navet = ImageTk.PhotoImage(imgnavet)

imgpoireau = Image.open("Poireau.png")
Poireau = ImageTk.PhotoImage(imgpoireau)

imgpois = Image.open("Pois.png")
Pois = ImageTk.PhotoImage(imgpois)

imgradis = Image.open("Radis.png")
Radis = ImageTk.PhotoImage(imgradis)

imgetomate = Image.open("Tomate.png")
Tomate = ImageTk.PhotoImage(imgetomate)

def actualiser():
    carre = []# La variable qui va contenir la liste des boutons associés à chaque compartiment
    for numero in range(16):
        carre.append(Button(maFenetre))                      # On ajoute un bouton au carre  
        plante = plantations[numero]['semis']
        if plante == "Aubergine":
            carre[numero].configure(image = Aubergine)
        elif plante == "Betterave":
            carre[numero].configure(image = Betterave)
        elif plante == "Carotte":
            carre[numero].configure(image = Carotte)
        elif plante == "Céleri":
            carre[numero].configure(image = Celeri)
        elif plante == "Chou brocoli":
            carre[numero].configure(image = Brocoli)
        elif plante == "Chou de Bruxelles":
            carre[numero].configure(image = CdB)
        elif plante == "Chou fleur":
            carre[numero].configure(image = Cf)
        elif plante == "Concombre":
            carre[numero].configure(image = Concombre)
        elif plante == "Epinard":
            carre[numero].configure(image = Epinard)
        elif plante == "Haricot vert":
            carre[numero].configure(image = Hv)
        elif plante == "Laitue":
            carre[numero].configure(image = Laitue)
        elif plante == "Melon":
            carre[numero].configure(image = Melon)
        elif plante == "Navet":
            carre[numero].configure(image = Navet)
        elif plante == "Poireau":
            carre[numero].configure(image = Poireau)
        elif plante == "Pois":
            carre[numero].configure(image = Pois)
        elif plante == "Radis":
            carre[numero].configure(image = Radis)
        elif plante == "Tomate":
            carre[numero].configure(image = Tomate)
        elif plantations[numero]['arroser'] == 'yes':
            carre[numero].configure(image = Va)
        else:
            carre[numero].configure(image = vide)            # On affiche une image    
        carre[numero].configure(command = cliquer(numero))   # On associe le bouton à la fonction cliquer.    
        carre[numero].grid(row = numero//4, column=numero%4) # On place le bouton

actualiser()

maFenetre.mainloop()
sys.exit()