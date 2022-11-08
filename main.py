import tkinter as tk
from tkinter import *
from tkinter import Frame ,messagebox
import Funzioni
import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="systemisft"
    )

root = tk.Tk()

root.geometry('1000x1000')
root.resizable(False, False)
root.title('Label Widget Demo')


CCliente = tk.Canvas(root, width=400, height=300)
CCliente.pack()

#entry nome cliente
Cliente= tk.Entry(root,width=100)
Cliente.insert(0,Funzioni.customer(mydb))
Cliente.pack()

#label toner
LCiano= Label(root,text="ciano")
LCiano.pack()

#label data consegna ed entry
CLDataconsegnac= Label(root,text="data consegna")
CLDataconsegnac.pack()
CE_dataconsegna=tk.Entry(root,width=20)
CE_dataconsegna.pack()
CE_dataconsegna.insert(0,Funzioni.CL_dataconsegna(mydb))

#label ed entry contatore
LC_contatore= Label(root,text="Contatore")
LC_contatore.pack()
EC_contatore=tk.Entry(root,width=20)
EC_contatore.pack()
EC_contatore.insert(0,Funzioni.C_contatore(mydb))


#label ed entry previsione
LC_previsione=Label(root,text=("Previsione"))
LC_previsione.pack()
EC_rprevisione=tk.Entry(root,width=20)
EC_rprevisione.pack()
EC_rprevisione.insert(0,Funzioni.EC_previsione(mydb))

#label ed entry data scorta
LC_datascorta=Label(root,text=("Data Scorta"))
LC_datascorta.pack()
EC_datascorta=tk.Entry(root,width=20)
EC_datascorta.pack()
EC_datascorta.insert(0,Funzioni.EC_datascorta(mydb))

#label ed entry scorta
LC_scorta=Label(root,text=("Scorta"))
LC_scorta.pack()
EC_scorta=tk.Entry(root,width=20)
EC_scorta.pack()
EC_scorta.insert(0,Funzioni.EC_scorta(mydb))




BCliente = tk.Button(text='Update database', command=lambda: Funzioni.update(mydb,Cliente))
BCliente.pack()
CCliente.create_window(200, 180, window=BCliente)
CCliente.create_window(200, 140, window=Cliente)



root.mainloop()

