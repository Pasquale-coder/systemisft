from tkinter import *
import tkinter as tk
import tkinter.messagebox
def nome(mydb,id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT Nome_CLiente FROM Clienti where ID_Cliente=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    risultato = str(risultato)[2:-2]
    return (risultato)
def E_cliente(mydb, id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT Nome_CLiente FROM Clienti where ID_Cliente=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    risultato = str(risultato)[2:-2]
    return (risultato)


def E_dataconsegna(mydb, id, colore):
    mycursor = mydb.cursor(mydb)
    if colore == "ciano":
        mycursor.execute("SELECT DATE_FORMAT(C_DataConsegna,'%d/%m/%Y') FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[2:-2]
    elif colore == "giallo":
        mycursor.execute("SELECT DATE_FORMAT(Y_DataConsegna,'%d/%m/%Y') FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[2:-2]
    elif colore == "nero":
        mycursor.execute("SELECT DATE_FORMAT(K_DataConsegna,'%d/%m/%Y') FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[2:-2]
    elif colore == "magenta":
        mycursor.execute("SELECT DATE_FORMAT(M_DataConsegna,'%d/%m/%Y') FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[2:-2]
    return (risultato)


def E_contatore(mydb, id, colore):
    mycursor = mydb.cursor(mydb)
    if colore == "ciano":
        mycursor.execute("SELECT C_Contatore FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "giallo":
        mycursor.execute("SELECT Y_Contatore FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "nero":
        mycursor.execute("SELECT K_Contatore FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "magenta":
        mycursor.execute("SELECT M_Contatore FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    return (risultato)


def E_previsione(mydb, id, colore):
    mycursor = mydb.cursor(mydb)
    if colore == "ciano":
        mycursor.execute("SELECT C_Previsione FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "giallo":
        mycursor.execute("SELECT Y_Previsione FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "nero":
        mycursor.execute("SELECT K_Previsione FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "magenta":
        mycursor.execute("SELECT M_Previsione FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    return (risultato)


def E_datascorta(mydb, id, colore):
    mycursor = mydb.cursor(mydb)
    if colore == "ciano":
        mycursor.execute("SELECT DATE_FORMAT(C_DataScorta,'%d/%m/%Y') FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[2:-2]
    elif colore == "giallo":
        mycursor.execute("SELECT DATE_FORMAT(Y_DataScorta,'%d/%m/%Y') FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[2:-2]
    elif colore == "nero":
        mycursor.execute("SELECT DATE_FORMAT(K_DataScorta,'%d/%m/%Y') FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[2:-2]
    elif colore == "magenta":
        mycursor.execute("SELECT DATE_FORMAT(M_DataScorta,'%d/%m/%Y') FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[2:-2]
    return (risultato)


def E_scorta(mydb, id, colore):
    mycursor = mydb.cursor(mydb)
    if colore == "ciano":
        mycursor.execute("SELECT C_Scorta FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "giallo":
        mycursor.execute("SELECT Y_Scorta FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "nero":
        mycursor.execute("SELECT K_Scorta FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "magenta":
        mycursor.execute("SELECT M_Scorta FROM fotocopiatori where id_stampante=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    return (risultato)


def EV_datacambio(mydb, id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT DATE_FORMAT(V_DataCambio,'%d/%m/%Y) FROM fotocopiatori where id_stampante=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    return (risultato)


def EV_scorta(mydb, id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT V_Scorta FROM fotocopiatori where id_stampante=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    return (risultato)


def E_modello(mydb, id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT Modello FROM fotocopiatori where id_stampante=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    return (risultato)


def E_seriale(mydb, id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT Seriale FROM fotocopiatori where id_stampante=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    return (risultato)


def informazioni(mydb,id,id_stampante):
    w2 = Toplevel()
    w2.title(E_cliente(mydb, id))
    w2.geometry("1000x1000")
    colori=["ciano","magenta","giallo","nero"]
    list=[]
    list2= []
    for i in colori:
        Ltoner=Label(w2,text=i)
        Ltoner.pack()
        Ldataconsegnat = Label(w2, text="data consegna")
        Ldataconsegnat.pack()
        Edataconsegnat= tk.Entry(w2, width=20)
        Edataconsegnat.pack()
        Edataconsegnat.insert(0, E_dataconsegna(mydb, id_stampante, i))
        list.append(Edataconsegnat.get())
        list2.append(Edataconsegnat)

        # label ed entry contatore
        Lcontatoret = Label(w2, text="Contatore")
        Lcontatoret.pack()
        Econtatoret = tk.Entry(w2, width=20)
        Econtatoret.pack()
        Econtatoret.insert(0, E_contatore(mydb, id_stampante, i))
        list.append(Econtatoret.get())
        list2.append(Econtatoret)
        # label ed entry previsione
        Lprevisionet = Label(w2, text=("Previsione"))
        Lprevisionet.pack()
        Eprevisionet = tk.Entry(w2, width=20)
        Eprevisionet.pack()
        Eprevisionet.insert(0, E_previsione(mydb, id_stampante, i))
        list.append(Eprevisionet.get())
        list2.append(Eprevisionet)
        # label ed entry data scorta
        Ldatascortat = Label(w2, text=("Data Scorta"))
        Ldatascortat.pack()
        Edatascortat = tk.Entry(w2, width=20)
        Edatascortat.pack()
        Edatascortat.insert(0, E_datascorta(mydb, id_stampante, i))
        list.append(Edatascortat.get())
        list2.append(Edatascortat)

        # label ed entry scorta
        Lscortat = Label(w2, text=("Scorta"))
        Lscortat.pack()
        Escortat = tk.Entry(w2, width=20)
        Escortat.pack()
        Escortat.insert(0, E_scorta(mydb, id_stampante, i))
        list.append(Escortat.get())
        list2.append(Escortat)


    def aggiornadb():
        messaggio=tkinter.messagebox.askquestion("Confirm","Are you sure?")

    aggiorna=Button(w2,text="aggiorna database",command=lambda: aggiornadb())
    aggiorna.pack()
    w2.mainloop()





