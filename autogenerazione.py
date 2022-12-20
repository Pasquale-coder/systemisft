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


n=10

#Defining the row and column
i=3

#Iterating over the numbers till n and
#creating the button
for j in range(n):
   mybutton= Button(w1, text=j)
   mybutton.grid(row=i, column=j)



w1.mainloop()