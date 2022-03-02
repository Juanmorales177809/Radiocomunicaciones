from ast import Lambda
from tkinter import *
from tkinter import ttk



v = Tk()
v.geometry('500x500')
v.config(background='white')
v.iconbitmap("./assets/antena.ico")
v.title("Calculo de Radio Enlace")
canva = Canvas(v,width=150, height=500, bg='white',borderwidth=10)
canva.grid(row=0, column=0,padx=0.1,pady=0.1)
canva1 = Canvas(v,width=350, height=500, bg='white',borderwidth=5)
canva1.grid(row=0, column=1)
Label(canva, text="Bienvenido",font=('Arial'),bg='white').grid(row=0, column= 0)
def radioEnlace():
    canva1 = Canvas(v,width=350, height=500, bg='blue',borderwidth=5)
    canva1.grid(row=0, column=0)
    ent = Entry(canva1,width=20,borderwidth=2)
    ent.grid(row=0,column=1)
    comboDe= ttk.Combobox(canva1,values=["dB","dBm","W","mW","dBd","dBi","metros","Kilometros"],width=7,foreground='grey')
    comboDe.grid(row=0, column=2,padx=5, pady=5)
    Label(canva1,text="=", background='white', font='Courier').grid(row=0,column=3)
    ent1 = Entry(canva1,width=20,borderwidth=2)
    ent1.grid(row=0,column=4)
    comboTo= ttk.Combobox(canva1,values=["dB","dBm","W","mW","dBd","dBi","metros","Kilometros"],width=7,foreground='grey')
    comboTo.grid(row=0, column=5,padx=5, pady=5)
    
    textUnit = Entry(canva1,width=10,borderwidth=2)#Caja de texto con el valor convertido
    textUnit.grid(row=3,column=2,padx=5, pady=5)
    textConv =Entry(canva1,borderwidth=2,width=20)#Caja de texto con las unidades convertidas
    textConv.grid(row=3,column=1,padx=5, pady=5)
def tokio():
    canva1 = Canvas(v,width=350, height=500, bg='red',borderwidth=5)
    canva1.grid(row=0, column=1)
def tokio2():
    canva1 = Canvas(v,width=350, height=500, bg='green',borderwidth=5)
    canva1.grid(row=0, column=1)
Button(canva, text="Calcular Lfs", background='blue',width=20,fg='white',command= lambda : radioEnlace()).grid(row =1, column =0,padx=5, pady=5)
Button(canva, text="Calcular ", background='blue',width=20,fg='white',command=lambda: tokio()).grid(row =2, column =0,padx=5, pady=5)
Button(canva, text="Calcular ", background='blue',width=20,fg='white',command=lambda:tokio2()).grid(row =3, column =0,padx=5, pady=5)


mainloop()