#coding : utf-8
#Ewan GRIGNOUX LEVERT
#Avril 2020
import sys
import csv
from tkinter import *
from tkinter.messagebox import *
import Chargement

def Magasin(player):
    Magasin_win = Toplevel()
    Magasin_win.title("Magasin")
    Magasin_win.geometry('500x630+400+200')
    Magasin_win.configure(bg = 'green')

    semis = Chargement.lireFichierCSV(f'Inventaire_{player}.csv')
    données_semis = Chargement.lireFichierCSV('Semis.csv')
    
    liste_semis = []
    for i in range(20):
        liste_semis.append(semis[i]['Plante'])
    liste_semis.remove('vide')

    def argent(root,r,c):
                Votre_solde = Label(root, text=f"Votre solde: {semis[20]['Quantite']}€")
                Votre_solde.grid(row=r,column=c,padx=5,pady=5)

    argent(Magasin_win,4,3)

    # Chargement des images
    MesImages = Chargement.ChargementImage(liste_semis)

    def cliquer(n):
        return lambda: afficherInfos(n)

    def afficherInfos(n):
        if semis[n]['Plante'] == 'vide':
            tite_info = semis[n+1]['Informations']
            titre_text = semis[n+1]['Plante']
            a = semis[n+1]['Plante']
        else:
            tite_info = données_semis[n]['Informations']
            titre_text = semis[n]['Plante']
            a = semis[n]['Plante']
        
        infos = Toplevel()
        infos.title(f'{a}')
        infos.configure(bg = 'green')
        
        titre = Label(infos,  text=titre_text, fg='yellow',bg='green', font=('Candara', 30))
        titre.grid(row = 0, column=0,padx=5,pady=5)

        informations = Label(infos, text=tite_info, fg='yellow',bg='green', font=('Candara', 20),wraplength = 500)
        informations.grid(row=1, column=0, padx=5, pady=5)

        def achat():
            achat_win = Toplevel()
            achat_win.configure(bg = 'green')
            achat_win.geometry("460x130")
            nbr = Spinbox(achat_win, from_=0, to=10)
            nbr.grid(row=0, column=0,padx=5,pady=5)

            def acheter_function():
                nombre = float(nbr.get())
                p = nombre*float(données_semis[n]['Prix'])
                if float(semis[20]['Quantite']) >= p:
                    if askyesno('Achat',f"Voulez-vous acheter {nombre} de{semis[n]['Plante']}, pour {p}€ ?"):
                        with open(f'Inventaire_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                            titres = ['Num','Plante','Levée','Récolte','Types','Prix','Quantite','Informations']
                            ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                            ecrivain.writeheader()
                            semis[20]['Quantite'] = (float(semis[20]['Quantite']) - p)
                            semis[n]['Quantite'] = round((float (semis[n]['Quantite']) + nombre),2)
                            for compartiment in semis:
                                ecrivain.writerow(compartiment)
                        showinfo('Achat','Votre achat se trouve dans votre inventaire.')
                        achat_win.destroy()
                showerror('Achat',"Vous n'avez pas l'argent nécessaire pour cet achat")


            def vendre_function():
                nombre = float(nbr.get())
                if nombre <= float(semis[n]['Quantite']):
                    p = nombre*float(données_semis[n]['Prix'])
                    if askyesno('Vendre',f"Voulez-vous vendre {nombre} de {semis[n]['Plante']}, pour {p}€ ?"):
                        with open(f'Inventaire_{player}.csv', 'w', newline='', encoding = 'utf-8')as fichier:
                            titres = ['Num','Plante','Levée','Récolte','Types','Prix','Quantite','Informations']
                            ecrivain = csv.DictWriter(fichier, fieldnames=titres)
                            ecrivain.writeheader()
                            semis[20]['Quantite'] = (float(semis[20]['Quantite']) + p)
                            semis[n]['Quantite'] = round((float (semis[n]['Quantite']) - nombre),2)
                            for compartiment in semis:
                                ecrivain.writerow(compartiment)
                        showinfo('Vente','Vous avez vendu  ce(s) produit(s).')
                        achat_win.destroy()

                else:
                    showerror('Erreur',"Vous n'en possédez pas autant")


            acheter = Button(achat_win, text='Acheter', command=acheter_function ,fg='yellow',bg='green', font=('Candara', 20))
            acheter.grid(row=1,column=0,padx=5,pady=5)

            vendre = Button(achat_win, text='Vendre', command=vendre_function, fg='yellow',bg='green', font=('Candara', 20))
            vendre.grid(row=1,column=1,padx=5,pady=5)

            prix_unitaire = Label(achat_win, text=f"Prix unitaire: {données_semis[n]['Prix']}€", fg='yellow',bg='green', font=('Candara', 20))
            prix_unitaire.grid(row=0,column=1,padx=5,pady=5)
            
            argent(achat_win,2,0)

        achat_button = Button(infos, text='Acheter/Vendre', fg='yellow',bg='green', command = achat, font=('Candara', 20))
        achat_button.grid(row=2,column=0,padx=5,pady=5)

    
    
    carre = []
    for numero in range (len(liste_semis)):
        carre.append(Button(Magasin_win, image=MesImages[liste_semis[numero]], command = cliquer(numero), fg='yellow',bg='green', font=('Candara', 20)))
        carre[numero].grid(row = numero//4, column=numero%4,padx=5,pady=5)
    
    Magasin_win.mainloop()
    sys.exit()
