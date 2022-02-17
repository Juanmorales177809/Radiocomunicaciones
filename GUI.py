from cProfile import label
from msilib.schema import ComboBox
from tkinter import *
from tkinter import font
from turtle import back, color
from matplotlib.colorbar import Colorbar
from tkinter import messagebox
from matplotlib.pyplot import colorbar
from pyparsing import col
import convertir
from tkinter import ttk

v = Tk()
v.iconbitmap("./assets/antena.ico")
v.title("Radiocomunicaciones by Carlos")
v.minsize(700,600)
v.configure(background='white')
frame= Frame(width=600, height=100, bg='white', background='white' )
frame.pack()
canvas = Canvas(width=600, height=100, bg='white')
canvas.pack(expand=NO, fill=BOTH)
frameP= Frame(width=700, height=100, bg='white', background='white' )
frameP.pack()
frameF= Frame(width=700, height=100, bg='white', background='white' )
frameF.pack()
canvas2 = Canvas(width=700, height=300, bg='white')
canvas2.pack(expand=YES,fill=BOTH)
Label(frame,text='RADIOCOMUNICACIONES',background='white', font=("Courier", 25)).grid(row=0,column=0)
Label(canvas,text="Conversor",background='white',font=('Courier',13)).grid(row=0,column=0)
Label(canvas,text="Ingrese valor",background='white', font=('Courier',11)).grid(row=1,column=0)
comboDe= ttk.Combobox(canvas,values=["dB","dBm","W","mW"],width=7,foreground='grey')
comboDe.grid(row=1, column=2,padx=5, pady=5)
Label(canvas,text="=", background='white', font='Courier').grid(row=1,column=4)
comboTo= ttk.Combobox(canvas,values=["dB","dBm","W","mW"],width=7,foreground='grey')
comboTo.grid(row=1, column=5,padx=5, pady=5)
ent1 = Entry(canvas,width=20,borderwidth=2)
ent1.grid(row=1,column=1)
textUnit = Entry(canvas,width=10,borderwidth=2)#Caja de texto con el valor convertido
textUnit.grid(row=3,column=2,padx=5, pady=5)
textConv =Entry(canvas,borderwidth=2,width=20)#Caja de texto con las unidades convertidas
textConv.grid(row=3,column=1,padx=5, pady=5)

#Perdidas por espacio libre
Label(frameP,text="Perdidas en el espacio libre",font=("Courier",15),bg='white').grid(row=0,column=0)
Label(canvas2,text='Lfs =').grid(row=0, column=0)
potenciaT= Entry(canvas2,width=10,borderwidth=2)
potenciaT.grid(row=0, column=1)
potenciaT.insert(0, 'constante' )
Label(canvas2,text=' + ', font=('Courier',15),bg='white').grid(row=0,column=3)
gananciaT= Entry(canvas2,width=10,borderwidth=2)
gananciaT.grid(row=0,column=4)
combo1= ttk.Combobox(canvas2,values=["Hz","Mhz","Khz","Ghz"],width=7,foreground='grey')
combo1.grid(row=0,column=5)
Label(canvas2,text=' + ', font=('Courier',15),bg='white').grid(row=0,column=6)
gananciaR= Entry(canvas2,width=10,borderwidth=2)
gananciaR.grid(row=0,column=7)
combo2= ttk.Combobox(canvas2,values=["cm","m","Km","millas"],width=7,foreground='grey')
combo2.grid(row=0,column=8)
Label(canvas2,text=' = ',font=('Courier',15),bg='white').grid(row=0,column=9)
resultado = Entry(canvas2,width=10,borderwidth=2)
resultado.grid(row=0,column=10)



#Friis
Label(frameF,text="Relacion senal/ruido",font=("Courier",15),bg='white').grid(row=0,column=0)
Label(canvas2,text='Friis =').grid(row=1, column=0)
potenciaT= Entry(canvas2,width=10,borderwidth=2)
potenciaT.grid(row=1, column=1)
combo1= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo1.grid(row=1,column=2)
Label(canvas2,text=' + ', font=('Courier',15),bg='white').grid(row=1,column=3)
gananciaT= Entry(canvas2,width=10,borderwidth=2)
gananciaT.grid(row=1,column=4)
combo2= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo2.grid(row=1,column=5)
Label(canvas2,text=' + ', font=('Courier',15),bg='white').grid(row=1,column=6)
gananciaR= Entry(canvas2,width=10,borderwidth=2)
gananciaR.grid(row=1,column=7)
combo3= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo3.grid(row=1,column=8)
Label(canvas2,text=' - ', font=('Courier',15),bg='white').grid(row=1,column=9)
lfs= Entry(canvas2,width=10,borderwidth=2)
lfs.grid(row=1,column=10)
combo4= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo4.grid(row=1,column=11)

def insertar(caja,combo):
    caja.configure(state=NORMAL)
    caja.delete(0,END)
    caja.insert(0,combo)
    caja.configure(state=DISABLED)

def agregar():
    num = float(ent1.get())
    if comboDe.get() == "W":
        if comboTo.get() == "W":
            messagebox.showerror("Error", message='No puede elegir las mismas unidades')
            insertar(textConv,num)
            insertar(textUnit,'W')
        elif comboTo.get() == "mW":
            conv= convertir.watsMwats(num)
            insertar(textConv,conv)
            insertar(textUnit,'mW')    
        elif comboTo.get()=="dB":
            conv= convertir.todB(num)
            insertar(textConv,conv)
            insertar(textUnit,'dB')
        elif comboTo.get()=="dBm":
            conv= convertir.todB(num)
            conv= convertir.dBDBm(conv)
            insertar(textConv,conv)
            insertar(textUnit,'dBm')
    elif comboDe.get() == "mW":
        if comboTo.get() == "W":
            conv= convertir.mWatsWats(num)
            insertar(textConv,conv)
            insertar(textUnit,'W')
        elif comboTo.get() == "mW":
            messagebox.showerror("No puede elegir las mismas unidades")
            insertar(textConv,conv)
            insertar(textUnit,'mW')    
        elif comboTo.get()=="dBm":
            conv= convertir.todBm(num)
            insertar(textConv,conv)
            insertar(textUnit,'dBm')
        elif comboTo.get()=="dB":
            conv= convertir.todBm(num)
            conv= convertir.dBmDB(conv)
            insertar(textConv,conv)
            insertar(textUnit,'dB')
    elif comboDe.get() == "dB":
        if comboTo.get() == "W":
            conv= convertir.toWats(num)
            insertar(textConv,conv)
            insertar(textUnit,'W')
        elif comboTo.get() == "dB":
            messagebox.showerror("No puede elegir las mismas unidades")
            insertar(textConv,conv)
            insertar(textUnit,'dB')    
        elif comboTo.get()=="dBm":
            conv= convertir.dBDBm(num)
            insertar(textConv,conv)
            insertar(textUnit,'dBm')
        elif comboTo.get()=="mW":
            conv= convertir.dBDBm(num)
            conv= convertir.tomWats(conv)
            insertar(textConv,conv)
            insertar(textUnit,'mW')
    elif comboDe.get() == "mW":
        if comboTo.get() == "W":
            conv= convertir.mWatsWats(num)
            insertar(textConv,conv)
            insertar(textUnit,'W')
        elif comboTo.get() == "mW":
            messagebox.showerror("No puede elegir las mismas unidades")
            insertar(textConv,conv)
            insertar(textUnit,'mW')    
        elif comboTo.get()=="dBm":
            conv= convertir.todBm(num)
            insertar(textConv,conv)
            insertar(textUnit,'dBm')
        elif comboTo.get()=="dB":
            conv= convertir.mWatsWats
            conv= convertir.todB(num)
            insertar(textConv,conv)
            insertar(textUnit,'dB')
    
    
    
    
photo = PhotoImage(file=r"./assets/convertir.png")    
    


Button(canvas, text="Convertir", background='blue',width=20,fg='white',command= lambda: agregar()).grid(row =3, column = 0,padx=5, pady=5)

mainloop()
