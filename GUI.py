from cProfile import label
from msilib.schema import ComboBox
from tkinter import *
from turtle import back, color
from matplotlib.colorbar import Colorbar
from tkinter import messagebox

from matplotlib.pyplot import colorbar
from pyparsing import col
import convertir
from tkinter import ttk

v = Tk()
v.iconbitmap("./assets/antena.ico")
v.title("Radiocomunicaciones")
v.minsize(600,600)
v.configure(background='white')
frame= Frame(width=600, height=100, bg='white', background='white' )
frame.pack()
canvas = Canvas(width=600, height=200, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas2 = Canvas(width=600, height=300, bg='#CCE5FF')
canvas2.pack(expand=YES,fill=BOTH)
Label(frame,text='RADIOCOMUNICACIONES',background='white', font=("Courier", 25)).grid(row=0,column=0)
Label(frame,text='by Carlos',background='white',font='Courier').grid(row=0,column=1)
Label(canvas,text="Conversor",background='white',font=('Courier',13)).grid(row=0,column=0)
Label(canvas,text="Ingrese valor",background='white', font=('Courier',11)).grid(row=1,column=0)
combo= ttk.Combobox(canvas,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo.grid(row=1, column=2,padx=5, pady=5)
Label(canvas,text="=", background='white', font='Courier').grid(row=1,column=4)
combo1= ttk.Combobox(canvas,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo1.grid(row=1, column=5,padx=5, pady=5)
ent1 = Entry(canvas,width=20,borderwidth=2)
ent1.grid(row=1,column=1)
text2 = Entry(canvas,width=10,borderwidth=2)
text2.grid(row=3,column=2,padx=5, pady=5)
text =Entry(canvas,borderwidth=2,width=20)
text.grid(row=3,column=1,padx=5, pady=5)
def insertar(caja,combo):
    caja.configure(state=NORMAL)
    caja.delete(0,END)
    caja.insert(0,combo.get())
    caja.configure(state=DISABLED)

def agregar():
    a = float(ent1.get())
    if combo1.get() == "W":
        if combo.get() == "mW":
            a= convertir.watsMwats(a)
            insertar(text2,combo)
        elif combo.get() == "W":
            messagebox.showerror("Error",message="No puede elegir las mismas unidades")
            insertar(text2,combo1)    
        elif combo.get()=="dB":
            a= convertir.todB(a)
            insertar(text2,combo)
        elif combo.get()=="dBm":
            a= convertir.todB(a)
            a= convertir.dBDBm(a)
            insertar(text2,combo)
        
    elif combo1.get() == "mW":
        if combo.get() == "W":
            a= convertir.mWatsWats(a)
            insertar(text2,combo1)
        elif combo.get() == "mW":
            messagebox.showerror("No puede elegir las mismas unidades")
            insertar(text2,combo)    
        elif combo.get()=="dBm":
            a= convertir.todBm(a)
            insertar(text2,combo1)
        elif combo.get()=="dB":
            a= convertir.todB(a)
            a= convertir.dBDBm(a)
    elif combo1.get() == "W":
        if combo.get() == "mW":
            a= convertir.watsMwats(a)
            insertar(text2,combo1)
        elif combo.get() == "W":
            messagebox.showerror("No puede elegir las mismas unidades")
            insertar(text2,combo)    
        elif combo.get()=="dB":
            a= convertir.todB(a)
        elif combo.get()=="dBm":
            a= convertir.todB(a)
            a= convertir.dBDBm(a)
    elif combo1.get() == "W":
        if combo.get() == "mW":
            a= convertir.watsMwats(a)
            insertar(text2,combo1)
        elif combo.get() == "W":
            messagebox.showerror("No puede elegir las mismas unidades")
            insertar(text2,combo)    
        elif combo.get()=="dB":
            a= convertir.todB(a)
        elif combo.get()=="dBm":
            a= convertir.todB(a)
            a= convertir.dBDBm(a)
    text.configure(state=NORMAL)
    text.delete(0,END)
    text.insert(0,a)
    text.configure(state=DISABLED)
    
    
    
photo = PhotoImage(file=r"./assets/convertir.png")    
    


Button(canvas, text="Convertir", background='blue',width=20,fg='white',command= lambda: agregar()).grid(row =3, column = 0,padx=5, pady=5)

mainloop()
