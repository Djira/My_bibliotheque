from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox as MessageBox
import  pymysql
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



"""def Ajouter() :
    idLivre = textidLivre.get()
    nomlivre= textnomlivre.get()
    edition= textnomlivre.get()
    nombre=text_nombre.get()
    auteur=textAuteur.get()
    prix=text_prix.get()
    dateEnregist=textDateEng.get()
    discipline=textDiscipline.get()

    if(idLivre=="" or nomlivre=="" or edition=="" or nombre=="" or auteur=="" or prix=="" or dateEnregist=="" or discipline==""):
        MessageBox.showinfo("Enregistrement","Tout les champs ne peuvent pas etre vide")
    else:
        con = pymysql.connect(host="localhost", user="root",password="", database="my_bibliotheque")
        cursor = con.cursor()
        cursor.execute(" insert into livre values('"+ idLivre +"','"+ nomlivre +"','"+ edition +"', '"+ nombre +"' , '"+ auteur +"' ,'"+ prix+"' ,'"+ dateEnregist+"' , '"+ discipline +"')")
        cursor.execute("commit")

        textidLivre.delete(0, 'end')
        textnomlivre.delete(0, 'end')
        text_edition.delete(0, 'end')
        text_nombre.delete(0, 'end')
        textAuteur.delete(0, 'end')
        text_prix.delete(0, 'end')
        textDateEng.delete(0, 'end')
        textDiscipline.delete(0, 'end')
        MessageBox.showinfo("Apprenant ajouter ", "Enregistrer avec succès")
        con.close()"""


def Modifier():
    idLivre = textidLivre.get()
    nomlivre= textnomlivre.get()
    edition= textnomlivre.get()
    nombre=text_nombre.get()
    auteur=textAuteur.get()
    prix=text_prix.get()
    dateEnregist=textDateEng.get()
    discipline=textDiscipline.get()

    if(idLivre=="" or nomlivre=="" or edition=="" or nombre=="" or auteur=="" or prix=="" or dateEnregist=="" or discipline==""):
        MessageBox.showinfo("Modification","Tout les champs ne peuvent pas etre vide")
    else:
        con = pymysql.connect(host="localhost", user="root",password="", database="my_bibliotheque")
        cursor = con.cursor()
        cursor.execute(" update into livre values('"+ idLivre +"','"+ nomlivre +"','"+ edition +"', '"+ nombre +"' , '"+ auteur +"' ,'"+ prix+"' ,'"+ dateEnregist+"' , '"+ discipline +"')")
        cursor.execute("commit")

        textidLivre.delete(0, 'end')
        textnomlivre.delete(0, 'end')
        text_edition.delete(0, 'end')
        text_nombre.delete(0, 'end')
        textAuteur.delete(0, 'end')
        text_prix.delete(0, 'end')
        textDateEng.delete(0, 'end')
        textDiscipline.delete(0, 'end')
        MessageBox.showinfo("Apprenant ajouter ", "Modifier avec succès")
        con.close()


def Ajouter():
    idLivre = textidLivre.get()
    nomlivre= textnomlivre.get()
    edition= textnomlivre.get()
    nombre=text_nombre.get()
    auteur=textAuteur.get()
    prix=text_prix.get()
    dateEnregist=textDateEng.get()
    discipline=textDiscipline.get()

    if(idLivre=="" or nomlivre=="" or edition=="" or nombre=="" or auteur=="" or prix=="" or dateEnregist=="" or discipline==""):
        MessageBox.showinfo("Veuillez remplir les champs","Tout les champs ne peuvent pas etre vide")
    else:
        con = pymysql.connect(host="localhost", user="root",password="", database="my_bibliotheque")
        cursor = con.cursor()
        cursor.execute(" INSERT into livre values('"+ idLivre +"','"+ nomlivre +"','"+ edition +"', '"+ nombre +"' , '"+ auteur +"' ,'"+ prix+"' ,'"+ dateEnregist+"' , '"+ discipline +"')")
        cursor.execute("commit")

        textidLivre.delete(0, 'end')
        textnomlivre.delete(0, 'end')
        text_edition.delete(0, 'end')
        text_nombre.delete(0, 'end')
        textAuteur.delete(0, 'end')
        text_prix.delete(0, 'end')
        textDateEng.delete(0, 'end')
        textDiscipline.delete(0, 'end')
        MessageBox.showinfo("Apprenant ajouter ", "Inserer avec succès")
        con.close()


def Supprimer():
    if(textidLivre.get() == ""):
        MessageBox.showinfo("Suppression ", "Spécifier ID du livre  à supprimer")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="my_bibliotheque")
        cursor = con.cursor()
        cursor.execute("delete from livre where idLivre ='"+ textidLivre.get() +"'")
        cursor.execute("commit")

        textidLivre.delete(0, 'end')
        textnomlivre.delete(0, 'end')
        text_edition.delete(0, 'end')
        text_nombre.delete(0, 'end')
        textAuteur.delete(0, 'end')
        text_prix.delete(0, 'end')
        textDateEng.delete(0, 'end')
        textDiscipline.delete(0, 'end')
        MessageBox.showinfo("Suppression ", "Supprimer avec succès")
        con.close()


def Afficher():
    con = pymysql.connect(host="localhost", user="root",password="", database="my_bibliotheque")
    cursor = con.cursor()
    cursor.execute("select * from livre")
    table.delete(*table.get_children())
    records=cursor.fetchall()
    for i, (idLivre, nomlivre, edition, nombre, auteur) in enumerate(records, start=1):
        table.insert("", "end", values=(idLivre, nomlivre, edition, nombre, auteur))
    con.close()



def Retour():
    fenetre.destroy()
    call(["python", "Chambre3.py"])


# ma fenetre
fenetre: Tk = Tk()
fenetre.title("My bibliothèque")
fenetre.geometry("1300x700")
#fenetre.resizable(False, False)
##fenetre.configure(background="#F67B0A")

#Chagement d'image
imag=ImageTk.PhotoImage(Image.open("C:\\Users\\Paule\\PycharmProjects\\pythonProject\\pythonProject\\pngo.png"))
x=Label(image=imag, font=("Arial",60))
x.pack()

"""ib2 = Listbox(fenetre, bg="black")
ib2.place(x=210, y=40, width=1000, height=150)"""


ib2 =Listbox(fenetre, bg="light gray")
ib2.place(x=0, y=10, width=200, height=640)


"""label = Label(fenetre, text='My bibliotheque/Dévél@ppé par groupe3 ODC', font=("Arial", 14), bg="gray")
label.place(x=260 ,y=600, height=60)"""
menu=Label(fenetre, text="Menu", font=("Arial", 14), bg="light blue")
menu.place(x=0, y=280, width=140, height=40)

quiter= Button(fenetre, text="<<QUITER", font= ("Arial",16), bg="light gray",fg="black", command=Retour)
quiter.place(x=0, y=560, width=140, height=60)


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

"""ib1 = Listbox(fenetre, bg="white")
ib1.place(x=200, y=10, width=1070, height=600)
"""
# Ajouter de titre
lbltitre=Label(fenetre, borderwidth=0, relief=SUNKEN, text="GESTION LIVRES"
               , font=("Arial", 20), background="white", fg="black")
lbltitre.place(x=500, y=0)

idLivre=Label(fenetre, text="ID LIVRE:", font=("Arial", 14), bg="gray", fg="BLACK")
idLivre.place(x=210, y=60)
textidLivre=Entry(fenetre, bd=4, font=("Arial", 13))
textidLivre.place(x=360, y=60,  width=200, height=35)

nomlivre=Label(fenetre,text="NOM DU LIVRE:", font=("Arial", 14), bg="gray", fg="BLACK")
nomlivre.place(x=210, y=120)
textnomlivre=Entry(fenetre, bd=4, font=("Arial", 13))
textnomlivre.place(x=360, y=120,  width=200, height=35)

edition=Label(fenetre, text="EDITION:", font=("Arial",14), bg="gray", fg="BLACK")
edition.place(x=210, y=180)
text_edition=Entry(fenetre, bd=4, font=("Arial", 14))
text_edition.place(x=360, y=180, width=200, height=35)

nombre=Label(fenetre, text="NOMBRE:", font=("Arial",14), bg="gray", fg="BLACK")
nombre.place(x=210, y=240)
text_nombre=Entry(fenetre, bd=4, font=("Arial", 14))
text_nombre.place(x=360, y=240, width=200, height=35)




auteur=Label(fenetre, text="AUTEUR:", font=("Arial",14), bg="gray", fg="BLACK")
auteur.place(x=210, y=300)
textAuteur=Entry(fenetre, bd=4, font=("Arial", 14))
textAuteur.place(x=360, y=300, width=200, height=35)


prix=Label(fenetre, text="PRIX:", font=("Arial", 14), bg="gray",fg="black")
prix.place(x=210, y=360)
text_prix=Entry(fenetre, bd=4, font=("Arial", 13))
text_prix.place(x=360, y=360,  width=200, height=40)

dateEnregist=Label(fenetre,text="DATE ENREGIST:", font=("Arial", 14), bg="gray",fg="black")
dateEnregist.place(x=580, y=60)
textDateEng=Entry(fenetre, bd=4, font=("Arial", 13))
textDateEng.place(x=800, y=60,  width=200, height=40)

discipline=Label(fenetre, text="DISCIPLINE:", font=("Arial",14),bg="gray" ,fg="black")
discipline.place(x=580, y=120,  width=200, height=30)
textDiscipline=Entry(fenetre, bd=4, font=("Arial", 14))
textDiscipline.place(x=800, y=120, width=200, height=40)

"""ib2 = Listbox(fenetre, bg="Light gray")
ib2.place(x=800, y=200, width=380, height=230)"""
ajouter=customtkinter.CTkButton(fenetre, text="AJOUTER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="light green", border_width=1, corner_radius=1,
                                command=Ajouter )

ajouter.place(x=580, y=400, width=150, height=30)


modifier=customtkinter.CTkButton(fenetre, text="MODIFIER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="ROYAL BLUE", border_width=1, corner_radius=1, command=Modifier )

modifier.place(x=740, y=400, width=150, height=30)

rechercher=customtkinter.CTkButton(fenetre, text="RECHERCHER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="sky blue", border_width=1, corner_radius=1 )


rechercher.place(x=900, y=400, width=150, height=30)

supprimer=customtkinter.CTkButton(fenetre, text="SUPPRIMER",text_font=("#000000", 15), text_color="black",bg="light gray",
                                fg_color="light gray", hover=True,hover_color="RED", border_width=1, corner_radius=1 , command=Supprimer)

supprimer.place(x=1060, y=400, width=150, height=30)

"""ib1 = Listbox(fenetre, bg="white")
ib1.place(x=600, y=250, width=500, height=100)

tapeIdLivre=Label(fenetre, text="Tape Id Livre", font=("Arial", 14), bg="light gray")
tapeIdLivre.place(x=750, y=290, width=150, height=40)
rechercher=Button(fenetre, text="RECHERCHER", font= ("Arial",16), bg="",fg="black")
rechercher.place(x=900, y=290, width=150)"""





"""ib3 = Listbox(fenetre, bg="#FFFFFF")
ib3.place(x=20, y=450, width=1210, height=230)

id2= Button(fenetre, text="ID", font= ("Arial",16), bg="#F67B0A",fg="black")"""

# Table
table = ttk.Treeview(fenetre, columns = (1, 2, 3,4,5, 6, 7, 8), height = 2, show = "headings")
table.place(x = 200,y = 450, width = 1070, height = 200)

#Entete
table.heading(1 , text = "ID")
table.heading(2 , text = "NON DU LIVRE")
table.heading(3 , text = "EDITION")
table.heading(4, text= "NOMBRE")
table.heading(5, text="AUTEUR")
table.heading(6, text="PRIX")
table.heading(7, text="DATE ENREGIST")
table.heading(8, text="DISCIPLINE")
#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 60)
table.column(3,width = 70)
table.column(4, width=80)
table.column(5, width=90)
table.column(6, width=100)
table.column(7, width=110)
table.column(8, width=120)

fenetre.mainloop()