from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox as MessageBox
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

#Chagement d'image
imag=ImageTk.PhotoImage(Image.open("C:\\Users\\Paule\\PycharmProjects\\pythonProject\\pythonProject\\pngo.png"))
x=Label(image=imag, font=("Arial",60))
x.pack()

ib2 =Listbox(fenetre, bg="light gray")
ib2.place(x=0, y=10, width=200, height=640)



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


ib2 =Listbox(fenetre, bg="gray")
ib2.place(x=200, y=10, width=1070, height=600)


ib2 =Listbox(fenetre, bg="WHITE")
ib2.place(x=200, y=150, width=800, height=300)

# cadre des sanction
ib2 =Listbox(fenetre, bg="WHITE")
ib2.place(x=460, y=10, width=600, height=100)


# Ajouter de titre

lbltitre=Label(fenetre, borderwidth=0, relief=SUNKEN, text="GESTION SANCTION"
               , font=("Arial", 20), background="white", fg="black")
lbltitre.place(x=600, y=20)


"""idAdherent=Label(fenetre, text="ID ADHERENT:", font=("Arial", 14), bg="#F67B0A", fg="black")
idAdherent.place(x=48, y=150)
textidAdherent=Entry(fenetre, bd=4, font=("Arial", 13))
textidAdherent.place(x=230, y=150,  width=300, height=35)"""

idSanction=Label(fenetre, text="ID SANCTION:", font=("Arial", 14), bg="WHITE", fg="BLACK")
idSanction.place(x=210, y=200)
textidSanction=Entry(fenetre, bd=4, font=("Arial", 13))
textidSanction.place(x=450, y=200,  width=300, height=35)


idBibliothecaire=Label(fenetre,text="ID BIBLIOTHECAIRE:", font=("Arial", 14), bg="WHITE", fg="BLACK")
idBibliothecaire.place(x=210, y=270)
textidBibliothecaire=Entry(fenetre, bd=4, font=("Arial", 13))
textidBibliothecaire.place(x=450, y=270,  width=300, height=35)

idAdherent=Label(fenetre, text="ID ADHERENT:", font=("Arial",14), bg="WHITE", fg="BLACK")
idAdherent.place(x=210, y=340)
textidAdherent=Entry(fenetre, bd=4, font=("Arial", 14))
textidAdherent.place(x=450, y=340, width=300, height=35)

"""dateAchat=Label(fenetre, text="DATE  D'ACHAT:", font=("Arial",14), bg="#F67B0A", fg="black")
dateAchat.place(x=20, y=350,  width=200, height=30)
textDatedAchat=Entry(fenetre, bd=4, font=("Arial", 14))
textDatedAchat.place(x=230, y=350, width=300, height=35)"""

montant=Label(fenetre, text="MONTANT:", font=("Arial",14), bg="WHITE", fg="BLACK")
montant.place(x=210, y=400)
textmontant=Entry(fenetre, bd=4, font=("Arial", 14))
textmontant.place(x=450, y=400, width=300, height=35)


ib2 = Listbox(fenetre, bg="GRAY")
ib2.place(x=910, y=150, width=280, height=280)
ajouter=customtkinter.CTkButton(fenetre, text="AJOUTER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="light green", border_width=1, corner_radius=1 )

ajouter.place(x=970, y=210, width=150, height=30)

modifier=customtkinter.CTkButton(fenetre, text="MODIFIER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="ROYAL BLUE", border_width=1, corner_radius=1 )

modifier.place(x=970, y=295, width=150, height=30)
annuler=customtkinter.CTkButton(fenetre, text="ANNULER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="RED", border_width=1, corner_radius=1 )

annuler.place(x=970, y=380, width=150, height=30)

retour= Button(fenetre, text="<<RETOUR", font= ("Arial",16), bg="white",fg="black", command=Retour)
retour.place(x=48, y=0)


"""ib3 = Listbox(fenetre, bg="#FFFFFF")
ib3.place(x=20, y=450, width=1210, height=230)

id2= Button(fenetre, text="ID", font= ("Arial",16), bg="#F67B0A",fg="black")"""

# Table
table = ttk.Treeview(fenetre, columns = (1, 2, 3,4,5), height = 2, show = "headings")
table.place(x =200,y = 450, width = 1070, height = 200)

#Entete
table.heading(1 , text = "ID ACHAT")
table.heading(2 , text = "ID ADHERENT")
table.heading(3 , text = "ID LIVRE")
table.heading(4, text= "DATE ACHAT")
table.heading(5, text="MONTANT")
#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 60)
table.column(3,width = 70)
table.column(4, width=80)
table.column(5, width=90)






fenetre.mainloop()
