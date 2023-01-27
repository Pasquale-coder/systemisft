from tkinter import *

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
b1=Button(w1,text="A & L Assistenza elettrodomestici Lombardia SNC",command=lambda:autogenerazione.autogenerazione(mydb,1))
b1.pack()
w1.mainloop()