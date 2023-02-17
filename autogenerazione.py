from tkinter import *
import Funzioni
def autogenerazione(mydb,id):
    w1 = Tk()
    w1.title("dispositivi")
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT COUNT(id_stampante) from fotocopiatori where Cliente="+str(id))
    risultato =mycursor.fetchone()
    risultato=int(''.join(map(str, risultato)))
    if(risultato>=1):
        for j in range(risultato):
            mybutton=Button(w1, text=nome(mydb,id,j),command=lambda k=j:test(mydb,id,k))
            mybutton.grid(row=j,column=1)
    elif(risultato==1):
        print("")
    w1.mainloop()
def nome(mydb,id,j):
    id=id+j
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT modello,seriale from fotocopiatori where id_stampante="+str(id))
    ris = str(mycursor.fetchall())
    return ris

def test(mydb,id,k):
    id = id + k
    mycursor = mydb.cursor(mydb)
    mycursor.execute("SELECT modello,seriale from fotocopiatori where id_stampante=" + str(id))
    ris = str(mycursor.fetchall())
    print(ris)

