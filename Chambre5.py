from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
import customtkinter
import pymysql
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




def Retour():
    fenetre.destroy()
    call(["python", "Chambre3.py"])
def Ajouter():
    idAdherent = text_idAdherent.get()
    nonAcheteur= text.get()
    genreAherent= text_genreAdherent.get()
    TelAdherent=text_TelAdherent.get()
    DateEnreg=text_DateEnreg.get()

    if(idAdherent=="" or nomAdherent=="" or genreAherent=="" or TelAdherent=="" or DateEnreg==""):
        MessageBox.showinfo("Veuillez remplir les champs","Tout les champs ne peuvent pas etre vide")
    else:
        con = pymysql.connect(host="localhost", user="root",password="", database="my_bibliotheque")
        cursor = con.cursor()
        cursor.execute(" INSERT into adherent values('"+ idAdherent +"','"+ nomAdherent +"','"+ genreAherent +"', '"+ TelAdherent +"' , '"+ DateEnreg +"')")
        cursor.execute("commit")

        text_idAdherent.delete(0, 'end')
        textnomaDHERENT.delete(0, 'end')
        text_genreAdherent.delete(0, 'end')
        text_TelAdherent.delete(0, 'end')
        text_DateEnreg.delete(0, 'end')

        MessageBox.showinfo("Apprenant ajouter ", "Inserer avec succès")
        con.close()




# ma fenetre
fenetre: Tk = Tk()
fenetre.title("My bibliothèque")
fenetre.geometry("1300x700")
#fenetre.resizable(False, False)
fenetre.configure(background="midnight blue")
# Ajouter de titre

"""imag=ImageTk.PhotoImage(Image.open("C:\\Users\\Paule\\PycharmProjects\\pythonProject\\pythonProject\\pngo.png"))
x=Label(image=imag, font=("Arial",60))
x.pack()"""

ib2 =Listbox(fenetre, bg="light gray")
ib2.place(x=0, y=30, width=140, height=600)


"""label = Label(fenetre, text='My bibliotheque/Dévél@ppé par groupe3 ODC', font=("Arial", 14), bg="gray")
label.place(x=260 ,y=600, height=60)"""
menu=Label(fenetre, text="Menu", font=("Arial", 14), bg="light blue")
menu.place(x=0, y=280, width=140, height=40)
livre = customtkinter.CTkButton(fenetre, text='LIVRES ',text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Livre)
livre.place(x=00, y=320, width=140, height=60)


achat= customtkinter.CTkButton(fenetre, text='ACHATS', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Achat)
achat.place(x=00, y=380, width=140, height=60)

adherent = customtkinter.CTkButton(fenetre, text='ADHERENTS', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Adherent)
adherent.place(x=00, y=440, width=140, height=60)

emprunt = customtkinter.CTkButton(fenetre, text='EMPRUNTS ',text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Emprunt)
emprunt.place(x=00, y=500, width=140, height=60)

sanction = customtkinter.CTkButton(fenetre, text='SANCTIONS',text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1 , command=Sanction)
sanction.place(x=00, y=560, width=140, height=60)

quiter= Button(fenetre, text="<<QUITER", font= ("Arial",16), bg="light gray",fg="black", command=Retour)
quiter.place(x=0, y=560, width=140, height=60)



"""ib2 =Listbox(fenetre, bg="gray")
ib2.place(x=420, y=60, width=800, height=400)"""
"""ib1 = Listbox(fenetre, bg="white")
ib1.place(x=200, y=30, width=1050, height=600)"""

ib2 =Listbox(fenetre, bg="gray")
ib2.place(x=180, y=30, width=1070, height=600)


# cadre des sanction
ib2 =Listbox(fenetre, bg="WHITE")
ib2.place(x=460, y=80, width=600, height=100)

lbltitre=Label(fenetre, borderwidth=0, relief=SUNKEN, text="GESTION ADHERENTS"
               , font=("Arial", 20), background="white", fg="black")
lbltitre.place(x=600, y=100)


idAdherent=Label(fenetre, text="ID ADHERENTS:", font=("Arial", 14), bg="GRAY", fg="BLACK")
idAdherent.place(x=210, y=200)
text_idAdherent=Entry(fenetre, bd=4, font=("Arial", 13))
text_idAdherent.place(x=400, y=200,  width=300, height=35)

nonAcheteur=Label(fenetre,text="NOM D'ACHERTEUR:", font=("Arial", 14), bg="GRAY", fg="BLACK")
nonAcheteur.place(x=210, y=250)
textnomaDHERENT=Entry(fenetre, bd=4, font=("Arial", 13))
textnomaDHERENT.place(x=400, y=250,  width=300, height=35)

genreAherent=Label(fenetre, text="SEXE:", font=("Arial",14), bg="GRAY", fg="BLACK")
genreAherent.place(x=210, y=300)
text_genreAdherent=Entry(fenetre, bd=4, font=("Arial", 14))
text_genreAdherent.place(x=400, y=300, width=300, height=35)

PrenomAcheteur=Label(fenetre, text="PRENOM ACHETEUR :", font=("Arial",14), bg="GRAY", fg="BLACK")
PrenomAcheteur.place(x=210, y=350)
text_TelAdherent=Entry(fenetre, bd=4, font=("Arial", 14))
text_TelAdherent.place(x=400, y=350, width=300, height=35)

NumTelAcheteur=Label(fenetre, text="NUMERO DE L'ACHETEUR:", font=("Arial",14), bg="GRAY", fg="BLACK")
NumTelAcheteur.place(x=210, y=400)
textNumTelAcheteur=Entry(fenetre, bd=4, font=("Arial", 14))
textNumTelAcheteur.place(x=400, y=400, width=300, height=35)

email=Label(fenetre, text="EMAIL:", font=("Arial",14), bg="GRAY", fg="BLACK")
email.place(x=710, y=200)
textEmail=Entry(fenetre, bd=4, font=("Arial", 14))
textEmail.place(x=900, y=200, width=300, height=35)

tarif=Label(fenetre, text="TARIF:", font=("Arial",14), bg="GRAY", fg="BLACK")
tarif.place(x=710, y=250)
textTarif=Entry(fenetre, bd=4, font=("Arial", 14))
textTarif.place(x=900, y=250, width=300, height=35)

abonnement=Label(fenetre, text="ABONNEMENT:", font=("Arial",14), bg="GRAY", fg="BLACK")
abonnement.place(x=710, y=300)
textAbonnement=Entry(fenetre, bd=4, font=("Arial", 14))
textAbonnement.place(x=900, y=300, width=300, height=35)



"""ib1 = Listbox(fenetre, bg="grey")
ib1.place(x=410, y=200, width=800, height=230)"""


"""ib2 = Listbox(fenetre, bg="LIGHT GRAY")
ib2.place(x=910, y=200, width=280, height=230)"""
ajouter=customtkinter.CTkButton(fenetre, text="AJOUTER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="light green", border_width=1, corner_radius=1, command=Ajouter )

ajouter.place(x=710, y=400, width=100, height=30)

modifier=customtkinter.CTkButton(fenetre, text="MODIFIER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="ROYAL BLUE", border_width=1, corner_radius=1 )

modifier.place(x=830, y=400, width=100, height=30)
supprimer=customtkinter.CTkButton(fenetre, text="SUPPRIMER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="RED", border_width=1, corner_radius=1 )

supprimer.place(x=1110, y=400, width=140, height=30)

rechercher=customtkinter.CTkButton(fenetre, text="RECHERCHER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="RED", border_width=1, corner_radius=1 )

rechercher.place(x=950, y=400, width=140, height=30)



"""annuler=Button(fenetre, text="ANNULER", font= ("Arial",16), bg="orange",fg="black")
annuler.place(x=970, y=270, width=150, height=30)"""


"""retour= Button(fenetre, text="<<-RETOUR", font= ("Arial",16), bg="gray",fg="white", command=Retour)
retour.place(x=0, y=0)"""

# Table
table = ttk.Treeview(fenetre, columns = (1, 2, 3,4,5), height = 2, show = "headings")
table.place(x =180,y = 450, width = 1070, height = 190)

#Entete
table.heading(1 , text = "ID")
table.heading(2 , text = "NON ADHERENT")
table.heading(3 , text = "GENRE ADHERENT")
table.heading(4, text= "TEL ADHERENT")
table.heading(5, text="DATE ENREGISTREMENT")
#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 60)
table.column(3,width = 70)
table.column(4, width=80)





fenetre.mainloop()
