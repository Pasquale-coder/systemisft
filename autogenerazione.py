from tkinter import *
import tkinter as tk
import mysql.connector
mydb = mysql.connector.connect(
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
i=3

def nome(j):
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT modello from fotocopiatori where cliente="+str(9+j))
    ris=mycursor.fetchone()
    return ris

#Iterating over the numbers till n and
#creating the button
for j in range (num):
   mybutton= Button(w1, text= nome(j))
   mybutton.grid(row=i, column=j)




w1.mainloop()
