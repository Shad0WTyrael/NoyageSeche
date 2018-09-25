'Import de toutes les fonctions Tkinter'
from tkinter import *

'Commande bouton Résultat'
def Resultats():
    'Récupération des sasies dans la fenetre'
    Jours = int(recupj.get())
    Mois = int(recupm.get())
    annee = recupa.get()

    if Mois < 11 and int(annee) <= 1582 or int(annee) < 1582 or int(annee) > 2199 or Mois < 1 or Mois > 12:
        'Affichage Fenetre en cas erreur'
        errorsaisie = Tk()
        errorsaisie.geometry("230x130")
        errorsaisie.title("Erreur")
        Erreur= Label(errorsaisie, text='Saisir une date valide comprise entre\n\nle 1/11/1582 et le 12/12/2199.')
        Erreur.place(x=30, y=15)
        Erreurbt = Button(errorsaisie, text='Ok', command=errorsaisie.quit)
        Erreurbt.place(x=100, y=80)
        errorsaisie.mainloop()

    'Consiqnes'

    'On garde les deux derniers chiffres '
    annee1 = annee[2:4]

    'On ajoute 1/4 '
    annee1 = int(annee1)
    date = (annee1 + annee1//4)

    'On ajoute la journée '
    date = date + Jours

    'Selon le mois on ajoute diférents valeurs'
    if 2 <= Mois <= 3 or Mois == 11: date = date + 3
    elif Mois == 4 or Mois == 7: date = date + 6
    elif Mois == 9 or Mois == 12: date = date + 5
    elif Mois == 5: date = date + 1
    elif Mois == 6: date = date + 4
    elif Mois == 8: date = date + 2
    else: date = date + 0

    'Si l''année est bissextile & mois =  janvier ou février, on fait - 1'
    if int(annee)%400==0 or (int(annee)%4==0 and int(annee)%100!=0) and Mois == 1 or Mois == 2:
        date = date - 1

    'Selon le siècle, on ajoute'
    annee2 = annee[0:2]
    annee2 = int(annee2)
    if annee2 == 16 or annee2 == 20: date = date + 6
    elif annee2 == 17 or annee2 == 21: date = date + 4
    elif annee2 == 18: date = date + 2

    ' divise par 7 garde le reste'
    date = date % 7

    'Le reste représente le jour '
    semaine = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']
    i = 0
    for i, jr in enumerate(semaine):
        if date == i: date1.set(jr)




'Configuration interface graphique Tkinder'
intgraph1 = Tk()
intgraph1.geometry("400x300")
intgraph1.title("Exo1 Noyade Séche")


'Les différents label dans "fnt"'
Titre = Label(intgraph1, text='Exo 1 : Jour Calendrier', font='arial 8 bold')
Titre.place(x=110, y=25)

Indic = Label(intgraph1, text='Veuillez indiquer une date :', font='arial 8')
Indic.place(x=50, y=150)

date1=StringVar()

Result1= Label(intgraph1, textvariable=date1)
Result1.place(x=220, y=80)

Result2= Label(intgraph1, text="La recheche indique que le jour est un : ",font='arial 8 ')
Result2.place(x=20, y=80)

'saisie pour la date'
recupj = StringVar()
jour = Entry(intgraph1, textvariable=recupj, justify='center')
jour.place(x=200, y=150, width=20)
recupm = StringVar()
mois = Entry(intgraph1, textvariable=recupm, justify='center')
mois.place(x=240, y=150, width=20)
recupa = StringVar()
annee = Entry(intgraph1, textvariable=recupa, justify='center')
annee.place(x=280, y=150, width=30)

'Le bouton appelant la fonction resulat'
Resultbt= Button(intgraph1, text='Résultat', command=Resultats)
Resultbt.place(x=170, y=200)

'Bouton Quitter'
quitbtn = Button(intgraph1, text ='Quitter', command = intgraph1.destroy)
quitbtn.place(x=170, y=250)

intgraph1.mainloop()


