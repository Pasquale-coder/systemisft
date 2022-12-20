from tkinter import *
import tkinter as tk
import Funzioni
import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="systemisft"
    )

w1 = Tk()
w1.geometry("1000x1000")
w1.title("Clienti")
def open(mydb,id):
    w2 = Toplevel()
    w2.title(Funzioni.E_cliente(mydb,id))
    w2.geometry("1000x1000")
    # entry nome cliente
    EC_cliente = tk.Entry(w2, width=100)
    EC_cliente.insert(0, Funzioni.E_cliente(mydb,1))
    EC_cliente.pack()


    # label toner
    LCiano = Label(w2, text="ciano")
    LCiano.pack()

    # label data consegna ed entry
    LCDataconsegnac = Label(w2, text="data consegna")
    LCDataconsegnac.pack()
    EC_dataconsegna = tk.Entry(w2, width=20)
    EC_dataconsegna.pack()
    EC_dataconsegna.insert(0, Funzioni.E_dataconsegna(mydb,1,"ciano"))

    # label ed entry contatore
    LC_contatore = Label(w2, text="Contatore")
    LC_contatore.pack()
    EC_contatore = tk.Entry(w2, width=20)
    EC_contatore.pack()
    EC_contatore.insert(0, Funzioni.E_contatore(mydb,1,"ciano"))

    # label ed entry previsione
    LC_previsione = Label(w2, text=("Previsione"))
    LC_previsione.pack()
    EC_rprevisione = tk.Entry(w2, width=20)
    EC_rprevisione.pack()
    EC_rprevisione.insert(0, Funzioni.E_previsione(mydb,1,"ciano"))

    # label ed entry data scorta
    LC_datascorta = Label(w2, text=("Data Scorta"))
    LC_datascorta.pack()
    EC_datascorta = tk.Entry(w2, width=20)
    EC_datascorta.pack()
    EC_datascorta.insert(0, Funzioni.E_datascorta(mydb,1,"ciano"))

    # label ed entry scorta
    LC_scorta = Label(w2, text=("Scorta"))
    LC_scorta.pack()
    EC_scorta = tk.Entry(w2, width=20)
    EC_scorta.pack()
    EC_scorta.insert(0, Funzioni.E_scorta(mydb,1,"ciano"))

    #bottone per l'aggiornamento dei dati del database
    BCliente = tk.Button(w2,text='Aggiorna database', command=lambda: Funzioni.aggiorna_database(mydb,1,E_cliente.get(),EC_dataconsegna.get(),EC_contatore.get(),EC_rprevisione.get(),EC_datascorta.get(),EC_scorta.get()))
    BCliente.pack()



b1=Button(w1,text="A & L Assistenza elettrodomestici Lombardia SNC",command=lambda:open(mydb,1)).pack(pady=10)
w1.mainloop()