from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
#import  customtkinter



# Fonction connecter
def Seconnecter():

    nomUtilisateur=txtNomUtilisateur.get()
    MoDePasse=textMoDePasse.get()
    if (nomUtilisateur=="" or  MoDePasse==""):

        MessageBox.showinfo("Echec", "Veillez rentrer les données")
    else:
        fenetre.destroy()
        call(["python", "Chambre3.py"])
        #MoDePasse.delete("0", "end")
    """elif (nomUtilisateur=="admin" and MoDePasse=="admin"):
        MessageBox.showinfo("", "Bienvenue")
        MoDePasse.delete("0", "end")
        fenetre.destroy()
        call(["python", "Chambre2.py"])

    else:
        MessageBox.showwarning("", "Erreur de Connexion")
        MoDePasse.delete("0", "end")
        nomUtilisateur.delete("0", "end")"""
def CreerCompte():
    fenetre.destroy()
    call(["python", "Chambre2biblio.py"])



# ma fenetre
fenetre: Tk = Tk()
fenetre.title("My bibliothèque")
fenetre.geometry("1300x700")

#fenetre.resizable(False, False)
#fenetre.configure(background="#F67B0A")


imag=ImageTk.PhotoImage(Image.open("C:\\Users\\Paule\\PycharmProjects\\pythonProject\\pythonProject\\livre.png"))
x=Label(image=imag, font=("Arial",60))
x.pack()

ib2 =Listbox(fenetre, bg="light gray")
ib2.place(x=300, y=100, width=700, height=400)


# Ajouter de titre
lbltitre=Label(fenetre, borderwidth=0, relief=SUNKEN, text="My bibliothèque"
               , font=("Arial", 30), background="white", fg="black")
lbltitre.place(x=400, y=0, width=500, height=50)

"""connexion=Label(fenetre, text="CONNEXION :", font=("Arial", 14), fg="black")
connexion.place(x=200, y=150, width=150, height=50)"""


nomUtilisateur=Label(fenetre, text="Nom Utilisateur :", font=("Arial", 14), fg="black")
nomUtilisateur.place(x=320, y=200, width=150, height=40)
txtNomUtilisateur=Entry(fenetre, bd=4, font=("Arial", 13))
txtNomUtilisateur.place(x=500, y=200, width=400, height=40)

MoDePasse=Label(fenetre, text="Mot de passe", font=("Arial",14),  fg="black")
MoDePasse.place(x=320, y=270, width=150, height=40)
textMoDePasse= Entry(fenetre, show="*", bd=4, font="Arial, 13")
textMoDePasse.place(x=500, y=270, width=400, height=40)

# Bouton connecter
btconnnecter=Button(fenetre, text="Connecter", font=("Arial",16), fg="black", bg="orange"
                    , command=Seconnecter)
btconnnecter.place(x=600, y=330, width=200)

btCreeCompte=Button(fenetre, text="Veuillez vous créer un compte?", font=("Arial", 16), bg="sky blue"
                    ,fg="black", command=CreerCompte)
btCreeCompte.place(x=550, y=400, width=300)


fenetre.mainloop()
