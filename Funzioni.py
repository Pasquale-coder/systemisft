from tkinter import *
import tkinter as tk
import tkinter.messagebox
import datetime

"""
creazione funzione per la generazione delle pagine
def finestra_clienti():
  clienti=TK()
  clienti.geometry("1000*1000")
  clienti.title("Clienti")
  
  b1=Button(w1,text="A & L Assistenza elettrodomestici Lombardia SNC",command=lambda:dati(mydb,1)).pack(pady=10)
  w1.mainloop()

def dati(mydb,id):
   w2 = Toplevel()
   w2.title(Funzioni.EC_cliente(mydb,id))
   w2.geometry("1000x1000")
   
   #generazione label ed entry dei toner
   toner(mydb,id,"nero")
   toner(mydb,id,"ciano")
   toner(mydb,id,"magenta")
   toner(mydb,id,"giallo")
   
def toner(mydb,id,colore):
  if colore=="nero":
   
  elif colore=="ciano":
  
  elif colore=="magenta":
  
  elif colore=="giallo":
   
   
  
"""
def E_cliente(mydb,id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT Nome_CLiente FROM Clienti where ID_Cliente="+str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    risultato = str(risultato)[2:-2]
    return (risultato)

def E_dataconsegna(mydb,id,colore):
    mycursor = mydb.cursor(mydb)
    if colore=="ciano":
        mycursor.execute("SELECT DATE_FORMAT(C_DataConsegna,'%d/%m/%Y') FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[15:-2]
    elif colore=="giallo":
        mycursor.execute("SELECT DATE_FORMAT(Y_DataConsegna,'%d/%m/%Y') FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[15:-2]
    elif colore=="nero":
        mycursor.execute("SELECT DATE_FORMAT(K_DataConsegna,'%d/%m/%Y') FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[15:-2]
    elif colore=="magenta":
        mycursor.execute("SELECT DATE_FORMAT(M_DataConsegna,'%d/%m/%Y') FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[15:-2]
    return (risultato)


def E_contatore(mydb,id,colore):
    mycursor = mydb.cursor(mydb)
    if colore=="ciano":
        mycursor.execute("SELECT C_Contatore FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore=="giallo":
        mycursor.execute("SELECT Y_Contatore FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore=="nero":
        mycursor.execute("SELECT K_Contatore FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore=="magenta":
        mycursor.execute("SELECT M_Contatore FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    return (risultato)

def E_previsione(mydb,id,colore):
    mycursor = mydb.cursor(mydb)
    if colore=="ciano":
        mycursor.execute("SELECT C_Previsione FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore=="giallo":
        mycursor.execute("SELECT Y_Previsione FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore=="nero":
        mycursor.execute("SELECT K_Previsione FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore=="magenta":
        mycursor.execute("SELECT M_Previsione FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    return (risultato)



def E_datascorta(mydb,id,colore):
    mycursor = mydb.cursor(mydb)
    if colore == "ciano":
        mycursor.execute("SELECT DATE_FORMAT(C_DataScorta,'%d/%m/%Y') FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "giallo":
        mycursor.execute("SELECT DATE_FORMAT(Y_DataScorta,'%d/%m/%Y') FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "nero":
        mycursor.execute("SELECT DATE_FORMAT(K_DataScorta,'%d/%m/%Y') FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "magenta":
        mycursor.execute("SELECT DATE_FORMAT(M_DataScorta,'%d/%m/%Y') FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    return (risultato)

def E_scorta(mydb,id,colore):
    mycursor = mydb.cursor(mydb)
    if colore == "ciano":
        mycursor.execute("SELECT C_Scorta FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "giallo":
        mycursor.execute("SELECT Y_Scorta FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "nero":
        mycursor.execute("SELECT K_Scorta FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    elif colore == "magenta":
        mycursor.execute("SELECT M_Scorta FROM fotocopiatori where Cliente=" + str(id))
        risultato = []
        for i in mycursor.fetchall():
            risultato.extend(i)
        risultato = str(risultato)[1:-1]
    return (risultato)


def EV_datacambio(mydb,id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT DATE_FORMAT(V_DataCambio,'%d/%m/%Y) FROM fotocopiatori where Cliente=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
       risultato.extend(i)
    return (risultato)

def EV_scorta(mydb,id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT V_Scorta FROM fotocopiatori where Cliente=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    return (risultato)

def E_modello(mydb,id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT Modello FROM fotocopiatori where Cliente=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    return (risultato)

def E_seriale(mydb,id):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT Seriale FROM fotocopiatori where Cliente=" + str(id))
    risultato = []
    for i in mycursor.fetchall():
        risultato.extend(i)
    return (risultato)














def aggiorna_database(mydb,id,cliente,dataconsegna,contatore,previsione,datascorta,scorta):
    fcliente,fdataconsegna,fcontatore,fprevisione,fdatascorta,fscorta=(True,)*6
    #fcliente=True
    """
    conferma=tk.messagebox.askquestion('conferma','stai per aggiornare i seguenti campi, sei sicuro?',icon='warning')
    if conferma=='yes':
        print(confermato)
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')
    """

    #nessun campo è stato cambiato
    """if cliente==EC_cliente(mydb,id) and dataconsegna==EC_dataconsegna(mydb,id) and contatore==EC_contatore(mydb,id) and previsione==EC_previsione(mydb,id) and datascorta==EC_datascorta(mydb,id) and scorta==EC_scorta(mydb,id):
        tk.messagebox.showinfo('conferma', 'non è stato modificato alcun campo',icon='warning')
    #il campo cliente è stato cambiato
    elif cliente!=EC_cliente(mydb,id) and dataconsegna==EC_dataconsegna(mydb,id) and contatore==EC_contatore(mydb,id) and previsione==EC_previsione(mydb,id) and datascorta==EC_datascorta(mydb,id) and scorta==EC_scorta(mydb,id):
        print("#il campo cliente è stato cambiato")
    #il campo data consegna è stato cambiato
    elif cliente==EC_cliente(mydb,id) and dataconsegna!=EC_dataconsegna(mydb,id) and contatore==EC_contatore(mydb,id) and previsione==EC_previsione(mydb,id) and datascorta==EC_datascorta(mydb,id) and scorta==EC_scorta(mydb,id):
        print("#il campo data consegna è stato cambiato")
    #il campo data consegna è stato cambiato
    elif cliente!=EC_cliente(mydb,id) and dataconsegna==EC_dataconsegna(mydb,id) and contatore==EC_contatore(mydb,id) and previsione==EC_previsione(mydb,id) and datascorta==EC_datascorta(mydb,id) and scorta==EC_scorta(mydb,id):
        print("#il campo data consegna è stato cambiato")
    # il campo data consegna è stato cambiato
    elif cliente!=EC_cliente(mydb,id) and dataconsegna==EC_dataconsegna(mydb,id) and contatore==EC_contatore(mydb,id) and previsione==EC_previsione(mydb,id) and datascorta==EC_datascorta(mydb,id) and scorta==EC_scorta(mydb,id):
        print("# il campo data consegna è stato cambiato")
    # il campo data consegna è stato cambiato
    elif cliente!=EC_cliente(mydb,id) and dataconsegna==EC_dataconsegna(mydb,id) and contatore==EC_contatore(mydb,id) and previsione==EC_previsione(mydb,id) and datascorta==EC_datascorta(mydb,id) and scorta==EC_scorta(mydb,id):
        print(" # il campo data consegna è stato cambiato")
    """