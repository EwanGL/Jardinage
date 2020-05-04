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
from Champs import Champs
from Inventaire import Inventaire
from Magasin import Magasin
import Chargement

root = Tk()
root.title('Jardinage')
root.geometry("1920x1080")
root.configure(bg = 'green')

frame = Frame(root, bg='green')
frame.pack()

def new_game_function():

    def retour_function():
            Name.destroy()
            Nametxt.destroy()
            retour.destroy()
            lancer.destroy()
            acceuil()
    def menu_function():
        player = str(Name.get())
        if player != '':
            with open ('infos.txt', 'a') as txt:
                msg = (f"{player},")
                txt.write(msg)
            
            plantations_pro = Chargement.lireFichierCSV('Classeur1.csv')
            with open(f'Classeur_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                titres = ['num','semis','date_semis','date_levée','date_récolte','type_avant','arroser']
                ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                ecrivain.writeheader()
                plantations_pro[2]['arroser'] = "no"
                for compartiment in plantations_pro:
                    ecrivain.writerow(compartiment)
            
            semis_pro = Chargement.lireFichierCSV('Modèle_inventaire.csv')
            with open(f'Inventaire_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                titres = ['Num','Plante','Quantite']
                ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                ecrivain.writeheader()
                semis_pro[16]['Quantite'] = '2'
                semis_pro[20]['Quantite'] = '20'
                semis_pro[18]['Quantite'] = '2'
                for compartiment in semis_pro:
                    ecrivain.writerow(compartiment)
            
            def Champs_function():
                Champs(player)
                showinfo('Champs',"Voici ton champs, c'est ici que tu vas pouvoir produire tes fruits et légumes.")
            def Inventaire_function():
                Inventaire(player)
            def Magasin_function():
                Magasin(player)
            def Quitter():
                Jardin.destroy()
                Champs_button.destroy()
                Inventaire_button.destroy()
                Magasin_button.destroy()
                acceuil()
                Exit.destroy()
            
            Name.destroy()
            Nametxt.destroy()
            lancer.destroy()
            retour.destroy()
            showinfo('Histoire',f"Bienvenue jeune fermier, {player}, dans le menu prncipal. D'ici, tu peux aller voir ton champs, aller au marché pour y vendre ta production, au magasin pour acheter ce dont tu as besoin, et enfin voir ce que tu possède dans ton inventaire; ")
            Jardin = Label(frame, text='Jardinage', fg='yellow', bg='green', font=('Candara', 50))
            Jardin.pack(padx=5, pady=5)
            Champs_button = Button(frame, text='Champs', fg='yellow', bg='green', command=Champs_function, font=('Candara', 20))
            Champs_button.pack(padx=5, pady=5)
            Inventaire_button = Button(frame, text='Inventaire', fg='yellow', bg='green', command=Inventaire_function, font=('Candara', 20))
            Inventaire_button.pack(padx=5, pady=5)
            Magasin_button = Button(frame, text='Magasin', fg='yellow', bg='green', command=Magasin_function, font=('Candara', 20))
            Magasin_button.pack(padx=5, pady=5)
            Exit = Button(frame,text='Quitter la partie', fg='yellow', bg='green', command=Quitter, font=('Candara', 20))
            Exit.pack(padx=5, pady=5)
        else:
            showerror('Important', 'Vous devez nommer cette partie.')
    
    new_game.pack_forget()
    continue_game.pack_forget()
    Nametxt = Label(frame, text='Nom du joueur:', fg='yellow', bg = 'green', font=('Candara', 20))
    Nametxt.pack(padx=5, pady=5)
    Name = Entry(frame, textvariable='Nom du joueur', width = 17, font=('Candara', 20))
    Name.pack(padx=5, pady=5)
    lancer = Button(frame, text='Jouer', fg='yellow',bg='green', command=menu_function, font=('Candara', 20))
    lancer.pack(padx=5, pady=5)
    retour = Button(frame, text='Retour', fg='yellow',bg='green', command=retour_function, font=('Candara', 20) )
    retour.pack(padx=5, pady=5)

def continue_game_function():

    def retour_function():
        lancer.destroy()
        partytxt.destroy()
        party.destroy()
        retour.destroy()
        acceuil()
    def menu_function():
        def Champs_function():
            Champs(player)
        def Inventaire_function():
            Inventaire(player)
        def Magasin_function():
            Magasin(player)
        def Quitter():
                Jardin.destroy()
                Champs_button.destroy()
                Inventaire_button.destroy()
                Magasin_button.destroy()
                acceuil()
                Exit.destroy()
        
        player = party.get()
        party.destroy()
        partytxt.destroy()
        lancer.destroy()
        retour.destroy()
        Jardin = Label(frame, text='Jardinage', fg='yellow', bg='green', font=('Candara', 50))
        Jardin.pack(padx=5, pady=5)
        Champs_button = Button(frame, text='Champs', fg='yellow', bg='green', command=Champs_function, font=('Candara', 20))
        Champs_button.pack(padx=5, pady=5)
        Inventaire_button = Button(frame, text='Inventaire', fg='yellow', bg='green', command=Inventaire_function, font=('Candara', 20))
        Inventaire_button.pack(padx=5, pady=5)
        Magasin_button = Button(frame, text='Magasin', fg='yellow', bg='green', command=Magasin_function, font=('Candara', 20))
        Magasin_button.pack(padx=5, pady=5)
        Exit = Button(frame,text='Quitter la partie', fg='yellow', bg='green', command=Quitter, font=('Candara', 20))
        Exit.pack(padx=5, pady=5)
    new_game.pack_forget()
    continue_game.pack_forget()
    liste_party=[]
    with open ('infos.txt','r') as r:
        d = r.read()
    liste_party = d.split(',')
    partytxt = Label(frame, text='Partie:', fg='yellow',bg='green', font=('Candara', 50))
    partytxt.pack(padx=5, pady=5)
    party = ttk.Combobox(frame, values=liste_party ,width=10)
    party.pack(padx=5, pady=5)
    lancer = Button(frame, text='Jouer', fg='yellow',bg='green', command=menu_function, font=('Candara', 20))
    lancer.pack(padx=5, pady=5)
    retour = Button(frame, text='Retour', fg='yellow',bg='green', command=retour_function, font=('Candara', 20) )
    retour.pack(padx=5, pady=5)

new_game = Button(frame, text='Nouvelle Partie', bg='green', fg='yellow', command=new_game_function, font=('Candara', 20))
continue_game = Button(frame, text='Continuer', bg='green', fg='yellow', command=continue_game_function, font=('Candara', 20))

def acceuil():
    new_game.pack(padx=5, pady=5)
    continue_game.pack(padx=5, pady=5)

acceuil()
frame.pack(expand=YES)
root.mainloop()
sys.exit()