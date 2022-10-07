from tkinter import *
from subprocess import call
from tkinter import messagebox

import customtkinter


def deconnection():
    mbox = messagebox.askquestion("Deconnecter","Voulez-vous vraiment vous deconnecter?")
    if(mbox=='yes'):
        fenetre.destroy()
        call(["python", "connectPage.py"])

def Accueil():
    fenetre.destroy()
    call(["python", "Chambre3.py"])

def Livre():
    fenetre.destroy()
    call(["python", "Chambre4.py"])
def Adherent():
    fenetre.destroy()
    call(["python", "Chambre5.py"])

def Emprunt():
    fenetre.destroy()
    call(["python", "Chambre6.py"])

def Sanction():
    fenetre.destroy()
    call(["python", "Chambre8.py"])

def Achat():
    fenetre.destroy()
    call(["python", "Chambre7.py"])


"""def Rdv():
    fenetre.destroy()
    call(["python", "rendez_vous.py"])"""
fenetre = Tk()


#parametre:
fenetre.geometry("1300x700")
fenetre.title("Accueil")
#fenetre.resizable(False,False)
fenetre.configure(background="light gray")

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="MY BIBLIOTHEQUE",font=("Sans Serif bold",26),
                   background="#ADD8E6",foreground="#4062DD")
labelTitre.place(x=0,y=0,width=1270,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=30)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE D'ACCUEIL",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=1270,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="MY BIBLIOTHEQUE DEVEL@P BY TEAM 3 ODC",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1270,height=30)

#FRAME
frame1 = Frame(fenetre,background="#ADD8E6")
frame1.place(x=0,y=90,width=200,height=480)

#BOUTONS
accueil = customtkinter.CTkButton(fenetre, text='ACCUEIL ', text_font=("BLACK", 15),text_color="black", bg="BLACK",fg_color="#0052CC",border_width=1,corner_radius=1, hover=True,hover_color="#0052CC", command=Accueil)
accueil.place(x=10,y=140,width=180, height=25)
livre = customtkinter.CTkButton(fenetre, text='LIVRES ', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Livre)
livre.place(x=10,y=190,width=180, height=25)
achats = customtkinter.CTkButton(fenetre, text='ACHATS ', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Achat)
achats.place(x=10,y=240,width=180, height=25)
adherents = customtkinter.CTkButton(fenetre, text='ADHERENTS ', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Adherent)
adherents.place(x=10,y=290,width=180, height=25)
livre = customtkinter.CTkButton(fenetre, text='LIVRES ', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Emprunt)
emprunt = customtkinter.CTkButton(fenetre, text='EMPRUNTS ', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Sanction)

emprunt.place(x=10,y=340,width=180, height=25)
sanction=Button(frame1,text="SANCTION",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Sanction)
"""btnComptabilite.place(x=10,y=310,width=180)
btnRdv=Button(dash,text="Rendez-vous",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Rdv)
btnRdv.place(x=10,y=360,width=180)"""

deconnection = customtkinter.CTkButton(fenetre, text='DECONNECTION ', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=deconnection)

deconnection.place(x=10,y=480,width=180, height=25)

#LOGO
img = PhotoImage(file="C:\\Users\\Paule\\PycharmProjects\\pythonProject\\pythonProject\\My logo.png")

# Create a Label Widget to display the text or Image
label = Label(fenetre, image = img)
label.place(x=550,y=90)

fenetre.mainloop()






