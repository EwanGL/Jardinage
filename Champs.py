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
import Chargement

def Champs(player):
    # MISSION 1 : Lecture du fichier CSV

    plantations = Chargement.lireFichierCSV(f'Classeur_{player}.csv')
    Plantes = Chargement.lireFichierCSV(f'Inventaire_{player}.csv')
    données_semis = Chargement.lireFichierCSV('Semis.csv')

    liste_semis = []
    for i in range(19):
        if Plantes[i]['Quantité'] != '0':
            liste_semis.append(Plantes[i]['Plante'])
    liste_semis.remove('Engrais')

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
                    if données_semis[i]['Plante'] == semis.get():
                        tps_levée = 2*int(données_semis[i]['Levée'])
                    
                d2 = d + timedelta(seconds=tps_levée)
                dfl = datetime(d2.year, d2.month, d2.day, d2.hour, d2.minute, d2.second)

                if plantations[n]['date_levée'] == '':
                    with open(f'Classeur_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                        titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                        ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                        ecrivain.writeheader()
                        plantations[n]['date_levée'] = d2
                        for compartiment in plantations:
                            ecrivain.writerow(compartiment)

                return dfl

            def CalculDateRécolte(d):
                for i in range (0,19):
                    if données_semis[i]['Plante'] == semis.get():
                        tps_récolte = 2*int(données_semis[i]['Récolte'])
                    
                d2 = d + timedelta(seconds=tps_récolte)

                if plantations[n]['date_récolte'] =='':
                    with open(f'Classeur_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
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
                    if Plantes[i]['Plante'] == plantations[n]['semis']:
                        a = i
                with open(f'Classeur_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
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
                with open(f'Inventaire_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                    titres = ['Num','Plante','Levée','Récolte','Types','Prix','Quantité','Informations']
                    ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                    ecrivain.writeheader()
                    Plantes[a]['Quantité'] = float(Plantes[a]['Quantité'])+ 5
                    for compartiment in Plantes:
                        ecrivain.writerow(compartiment)
                dialogue.destroy()
                actualiser(maFenetre)
            
            now = str(datetime.now())
            if now > str(plantations[n]['date_récolte']):
                function()
            else:
                if askyesno('Attention', "Si vous récoltez maintenant, vous ne récupérez rien! \n Voulez-vous tout de même récolter?"):
                    function()
                else:
                    dialogue.destroy()
                    actualiser(maFenetre)

        def infos_function():
            for i in range (0,19):
                if Plantes[i]['Plante'] == plantations[n]['semis']:
                    données = données_semis[i]['Informations'] + "\n\n" + "Type: " + Plantes[i]['Types']
            Informations = Toplevel()
            Informations.title('Informations')
            Informations.geometry('250x300+500+350')
            Informations.config(bg = 'green')
            txt_infos = Label(Informations, text = données, fg ='yellow', bg ='green', wraplength = 200)
            txt_infos.pack()
        
        
        def modifierInfos():
            if plantations[n]['arroser'] == 'yes':
                for i in range (0,19):
                    if données_semis[i]['Plante'] == semis.get():
                        type_plante = données_semis[i]['Types']
                        num = i
                
                if float(Plantes[num]['Quantité']) >= 1 :
                    if type_plante != plantations[n]['type_avant']:
                        with open(f'Classeur_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                            titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                            ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                            ecrivain.writeheader()
                            plantations[n]['date_récolte'] = récolte.get()
                            plantations[n]['date_semis'] = datetime.now()
                            plantations[n]['date_levée'] = levée.get()
                            plantations[n]['semis'] = semis.get()
                            plantations[n]['type_avant'] = type_plante
                            for compartiment in plantations:
                                ecrivain.writerow(compartiment)
                        
                        for i in range (0,19): 
                            if Plantes[i]['Plante'] == semis.get():
                                with open(f'Inventaire_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                                    titres = ['Num','Plante','Levée','Récolte','Types','Prix','Quantité','Informations']
                                    ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                                    ecrivain.writeheader()
                                    Plantes[i]['Quantité'] = float(Plantes[i]['Quantité']) -1
                                    for compartiment in Plantes:
                                        ecrivain.writerow(compartiment)

                        actualiser(maFenetre)
                        dialogue.destroy()    
                    else:
                        showinfo('Important', 'Vous ne pouvez pas planter le même type de plante sur la même parcelle deux fois de suite!')
                else:
                    showinfo('Important', 'Vous ne possédez pas de graines pour pouvoir planter.')
            else:
                showinfo('Important','Vous devez arroser la parcelle avant de pouvoir planter.')

        def engrais_function():
            with open(f'Classeur_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                ecrivain.writeheader()
                plantations[n]['type_avant'] = 'none'
                for compartiment in plantations:
                    ecrivain.writerow(compartiment)
            with open(f'Inventaire_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                        titres = ['Num','Plante','Levée','Récolte','Types','Prix','Quantité','Informations']
                        ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                        ecrivain.writeheader()
                        Plantes[20]['Quantité'] =float(Plantes[20]['Quantité'])-1
                        for compartiment in Plantes:
                            ecrivain.writerow(compartiment)
            showinfo('Information', "La parcelle a retrouvé tous ses nutriments, vous pouvez désormais planter n'importe quel type de plante.")

        def arroser_function():
            with open(f'Classeur_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                ecrivain.writeheader()
                plantations[n]['arroser'] = 'yes'
                for compartiment in plantations:
                    ecrivain.writerow(compartiment)
            actualiser(maFenetre)
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
    maFenetre = Toplevel()
    # Réglage des paramètres
    maFenetre.title("Champs")  # Le titre
    maFenetre.geometry('420x420+400+200')  # La position
    maFenetre.configure(bg = 'green')  # la couleur de fond

    # Chargement des images
    liste_semis_img = []
    for i in range(20):
        liste_semis_img.append(Plantes[i]['Plante'])
    liste_semis_img.append('vide_arroser')
    
    MesImages = Chargement.ChargementImage(liste_semis_img)

    def actualiser(root):
        carre = []# La variable qui va contenir la liste des boutons associés à chaque compartiment
        for numero in range(16):
            carre.append(Button(root))                      # On ajoute un bouton au carre  
            plante = plantations[numero]['semis']
            if plantations[numero]['arroser'] == 'yes' and plante == 'vide':
                carre[numero].configure(image = MesImages['vide_arroser'])
            else:
                carre[numero].configure(image = MesImages[plante])
            carre[numero].configure(command = cliquer(numero))   # On associe le bouton à la fonction cliquer.    
            carre[numero].grid(row = numero//4, column=numero%4) # On place le bouton

    actualiser(maFenetre)

    maFenetre.mainloop()
    sys.exit()