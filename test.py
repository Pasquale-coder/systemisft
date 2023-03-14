from tkinter import *
import mysql.connector
import autogenerazione
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="systemisft"
    )
w1 = Tk()
w1.title("dispositivi")
mycursor = mydb.cursor(mydb)
nome="Azienda Speciale Servizi Sanitari"
nome="\""+nome+"\""

mycursor.execute("select id_stampante,cliente from fotocopiatori join clienti on cliente=Id_cliente where Nome_Cliente="+nome)
risultato =mycursor.fetchall()
print(risultato)
for i in range (len(risultato)):
 print(risultato[i][0])
 print(risultato[i][1])


"""
for i in risultato:
    fotocopiatore=autogenerazione.nome(mydb,*i)
    mybutton=Button(w1,text=fotocopiatore)
    mybutton.pack()

w1.mainloop()
"""
"""
for i in risultato:
    print(*i)

for j in range(risultato):
    mybutton=Button(w1, text=nome(mydb,j+1),command=lambda k=j:informazioni(mydb,id,(id+k)))
    mybutton.grid(row=j,column=1)
w1.mainloop()

"""
