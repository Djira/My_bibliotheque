from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk


# Fonction connecter
def Sinscrire():
    prenom=textprenom.get()
    nom=textprenom.get()
    nomDUtilisateur=textnomDUtilisateur.get()
    email=textEmail.get()
    MotDepasse=textMotDePasse.get()
    ConfimationMotDePasse=textConfirmationMotDePasse.get()


    if (prenom=="" or  nom=="" or nomDUtilisateur=="" or email=="" or MotDepasse=="" or
            ConfimationMotDePasse==""):
        MessageBox.showinfo("Echec", "Veuillez remplir les conditions demandé ")
def Annuler():
    fenetre.destroy()
    call(["python", "Chambre1biblio.py"])
def Retour():
    fenetre.destroy()
    call(["python", "Chambre1biblio.py"])


# ma fenetre
fenetre: Tk = Tk()
fenetre.title("My bibliothèque")
fenetre.geometry("1300x700")

#Chagement d'image
imag=ImageTk.PhotoImage(Image.open("C:\\Users\\Paule\\PycharmProjects\\pythonProject\\pythonProject\\pngo.png"))
x=Label(image=imag, font=("Arial",60))
x.pack()

ib2 =Listbox(fenetre, bg="gray")
ib2.place(x=300, y=150, width=700, height=500)



# Ajouter de titre
lbltitre=Label(fenetre, borderwidth=0, relief=SUNKEN, text="S'inscrire"
               , font=("Arial", 20),bg="#091821", fg="white")
lbltitre.place(x=164, y=0)

prenom=Label(fenetre, text="Prénom:", font=("Arial", 14), bg="gray", fg="white")
prenom.place(x=300, y=200)
textprenom=Entry(fenetre, bd=4, font=("Arial", 13))
textprenom.place(x=600, y=200,  width=300, height=40)

nom=Label(fenetre,text="Nom:", font=("Arial", 14), bg="gray", fg="white")
nom.place(x=300, y=250)
textnom=Entry(fenetre, bd=4, font=("Arial", 13))
textnom.place(x=600, y=250,  width=300, height=40)

nomDUtilisateur=Label(fenetre, text="Nom d'utilisateur:", font=("Arial",14), bg="gray", fg="white")
nomDUtilisateur.place(x=300, y=300,   height=30)
textnomDUtilisateur=Entry(fenetre, bd=4, font=("Arial", 14))
textnomDUtilisateur.place(x=600, y=300, width=300, height=40)

email=Label(fenetre, text="Email:", font=("Arial",14),bg="gray", fg="white")
email.place(x=300, y=350,  height=30)
textEmail=Entry(fenetre, bd=4, font=("Arial", 14))
textEmail.place(x=600, y=350, width=300, height=40)


MotDepasse=Label(fenetre, text="Mot de passe:", font=("Arial",14),bg="gray",  fg="white")
MotDepasse.place(x=300, y=400,  height=40)
textMotDePasse=Entry(fenetre, bd=4, font=("Arial", 14))
textMotDePasse.place(x=600, y=400, width=300, height=40)

ConfimationMotDePasse=Label(fenetre, text="CONFIRMER MOT DE PASSE:", font=("Arial", 14), bg="gray", fg="white")
ConfimationMotDePasse.place(x=300, y=450,   height=40)
textConfirmationMotDePasse=Entry(fenetre, bd=4, font=("Arial", 14))
textConfirmationMotDePasse.place(x=600, y=450, width=300, height=40)

annule= Button(fenetre, text="Annuler", font=("Arial", 16), bg="gray", fg="red", command=Annuler)
annule.place(x=910, y=600)

retour= Button(fenetre, text="RETOUR", font= ("Arial",16),bg="gray", fg="green", command=Retour)
retour.place(x=300, y=600)

inscrire= Button(fenetre, text="S'inscrire", font= ("Arial",16),bg="gray", fg="yellow", command=Sinscrire)
inscrire.place(x=605, y=600)


fenetre.mainloop()
