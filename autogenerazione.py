from tkinter import *
import mysql.connector
import Funzioni
"""mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="systemisft"
    )

w1 = Tk()

w1.title("Clienti")


mycursor = mydb.cursor(mydb)
mycursor.execute("SELECT COUNT(cliente) from fotocopiatori where cliente=9;")
risultato=mycursor.fetchone()
num=risultato[0]
#Defining the row and column


def nome(j):
    id=9+j
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT modello,sede from fotocopiatori where id_stampante="+str(id))
    ris=str(mycursor.fetchall())
    return ris

#Iterating over the numbers till n and
#creating the button
for j in range (num):
   mybutton= Button(w1, text= nome(j))
   mybutton.grid(row=j, column=1)




w1.mainloop()
"""
def autogenerazione(mydb,id):
    w1 = Tk()
    w1.title("dispositivi")
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT * from fotocopiatori where Cliente="+str(id))
    if(mycursor.fetchall()):

    else:


    w1.mainloop()
