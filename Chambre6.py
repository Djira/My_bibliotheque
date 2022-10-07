from subprocess import call
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
from PIL import Image, ImageTk

import customtkinter


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

def enregistrer():
    idEmprunt = textidEmprunt.get()
    idLivre= textidLivre.get()
    idAdherent= textidAdherent.get()
    DateDebutEmprunt=textDateDebutEmprunt.get()
    DateFinEmprunt=textDateFinEmprunt.get()
    montant=textmontant.get()

    if(idEmprunt=="" or idLivre=="" or idAdherent=="" or DateDebutEmprunt=="" or DateFinEmprunt=="" or montant==""):
        MessageBox.showinfo("Modification", "Tout les champs sont réquises")
    """else:
        con = pymysql.connect(host="localhost", user="root",password="", database="my_biliotheque")
        cursor = con.cursor()
        cursor.execute("update appli set nom='"+ nom+"',numero='"+ numero +"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_nom.delete(0, 'end')
        e_numero.delete(0, 'end')
        MessageBox.showinfo("Modifications ", "Modifier avec succès")
        con.close()"""


# ma fenetre
fenetre: Tk = Tk()
fenetre.title("My bibliothèque")
fenetre.geometry("1300x700")
#fenetre.resizable(False, False)
fenetre.configure(background="#F67B0A")



imag=ImageTk.PhotoImage(Image.open("C:\\Users\\Paule\\PycharmProjects\\pythonProject\\pythonProject\\pngo.png"))
x=Label(image=imag, font=("Arial",60))
x.pack()

ib2 =Listbox(fenetre, bg="light gray")
ib2.place(x=0, y=10, width=200, height=640)


"""label = Label(fenetre, text='My bibliotheque/Dévél@ppé par groupe3 ODC', font=("Arial", 14), bg="gray")
label.place(x=260 ,y=600, height=60)"""
menu=Label(fenetre, text="Menu", font=("Arial", 14), bg="light blue")
menu.place(x=0, y=280, width=140, height=40)
livre = customtkinter.CTkButton(fenetre, text='LIVRES ', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Livre)
livre.place(x=00, y=320, width=140, height=60)


achat= customtkinter.CTkButton(fenetre, text='ACHATS', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Achat)
achat.place(x=00, y=380, width=140, height=60)

adherent = customtkinter.CTkButton(fenetre, text='ADHERENTS', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Adherent)
adherent.place(x=00, y=440, width=140, height=60)

emprunt = customtkinter.CTkButton(fenetre, text='EMPRUNTS ',text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Emprunt)
emprunt.place(x=00, y=500, width=140, height=60)

sanction = customtkinter.CTkButton(fenetre, text='SANCTIONS', text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="#0052CC",border_width=1,corner_radius=1, command=Sanction)
sanction.place(x=00, y=560, width=140, height=60)

"""ib2 =Listbox(fenetre, bg="GRAY")
ib2.place(x=450, y=60, width=700, height=130)"""


ib2 =Listbox(fenetre, bg="gray")
ib2.place(x=200, y=10, width=1070, height=600)
ib2 =Listbox(fenetre, bg="WHITE")
ib2.place(x=200, y=150, width=800, height=300)


# Ajouter de titre
lbltitre=Label(fenetre, borderwidth=0, relief=SUNKEN, text="EMPRUMTS"
               , font=("Arial", 20), background="white", fg="black")
lbltitre.place(x=500, y=0)
idAdherent=Label(fenetre, text="ID ADHERENT:", font=("Arial", 14), bg="white", fg="BLACK")
idAdherent.place(x=210, y=150)

textidAdherent=Entry(fenetre, bd=4, font=("Arial", 13))
textidAdherent.place(x=460, y=150,  width=300, height=35)

idEmprunt=Label(fenetre, text="ID D'EMPRUNT:", font=("Arial", 14), bg="white", fg="BLACK")
idEmprunt.place(x=210, y=200)
textidEmprunt=Entry(fenetre, bd=4, font=("Arial", 13))
textidEmprunt.place(x=460, y=200,  width=300, height=35)

idLivre=Label(fenetre,text="ID LIVRE:", font=("Arial", 14), bg="white", fg="BLACK")
idLivre.place(x=210, y=250)
textidLivre=Entry(fenetre, bd=4, font=("Arial", 13))
textidLivre.place(x=460, y=250,  width=300, height=35)

DateDebutEmprunt=Label(fenetre, text="DATE DEBUT D'EMPRUNT:", font=("Arial",14), bg="white", fg="BLACK")
DateDebutEmprunt.place(x=210, y=300)
textDateDebutEmprunt=Entry(fenetre, bd=4, font=("Arial", 14))
textDateDebutEmprunt.place(x=460, y=300, width=300, height=35)

DateFinEmprunt=Label(fenetre, text="DATE FIN D'EMPREUNT:", font=("Arial",14), bg="white", fg="BLACK")
DateFinEmprunt.place(x=210, y=350)
textDateFinEmprunt=Entry(fenetre, bd=4, font=("Arial", 14))
textDateFinEmprunt.place(x=460, y=350, width=300, height=35)

montant=Label(fenetre, text="MONTANT:", font=("Arial",14), bg="white", fg="BLACK")
montant.place(x=210, y=400)
textmontant=Entry(fenetre, bd=4, font=("Arial", 14))
textmontant.place(x=460, y=400, width=300, height=35)

"""ib1 = Listbox(fenetre, bg="grey")
ib1.place(x=410, y=200, width=800, height=230)"""


ib2 = Listbox(fenetre, bg="gray")
ib2.place(x=950, y=150, width=280, height=280)

ajouter=customtkinter.CTkButton(fenetre, text="AJOUTER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="light green", border_width=1, corner_radius=1 )

ajouter.place(x=1040, y=210, width=150, height=30)

modifier=customtkinter.CTkButton(fenetre, text="MODIFIER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="ROYAL BLUE", border_width=1, corner_radius=1 )

modifier.place(x=1040, y=295, width=150, height=30)
annuler=customtkinter.CTkButton(fenetre, text="ANNULER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="RED", border_width=1, corner_radius=1 )

annuler.place(x=1040, y=380, width=150, height=30)

retour= Button(fenetre, text="RETOUR", font= ("Arial",16), bg="gray",fg="white", command=Retour)
retour.place(x=0, y=0)


"""ib3 = Listbox(fenetre, bg="#FFFFFF")
ib3.place(x=20, y=450, width=1210, height=230)

id2= Button(fenetre, text="ID", font= ("Arial",16), bg="#F67B0A",fg="black")"""

# Table
table = ttk.Treeview(fenetre, columns = (1, 2, 3,4,5), height = 2, show = "headings")
table.place(x =200,y = 450, width = 1070, height = 200)

#Entete
table.heading(1 , text = "ID_EMPRUNT")
table.heading(2 , text = "ID_LIVRE")
table.heading(3 , text = "ID_ADHERENT")
table.heading(4, text= "DATE DEBUT D'EMPRUNT")
table.heading(5, text="DATE FIN D'EMPRUNT")
#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 60)
table.column(3,width = 70)
table.column(4, width=80)






fenetre.mainloop()
