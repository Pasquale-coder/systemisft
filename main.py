from tkinter import *
from tkinter import ttk
from Funzioni import nome

import Funzioni
import autogenerazione
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


mycursor = mydb.cursor(mydb)
mycursor.execute("SELECT COUNT(id_stampante) from fotocopiatori")
risultato =mycursor.fetchone()
risultato=int(''.join(map(str, risultato)))
for j in range(risultato):
    cliente=Button(w1,text=nome(mydb,j+1),command=lambda k=j:autogenerazione.autogenerazione(mydb,k+1))
    cliente.pack()

w1.mainloop()
