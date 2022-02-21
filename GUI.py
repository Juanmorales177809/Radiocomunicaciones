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
import calculos
from presupuesto import Presupuesto

"""---------------------Head----------------------"""

v = Tk()
v.iconbitmap("./assets/antena.ico")
v.title("Radiocomunicaciones by Carlos")
v.minsize(700,600)
v.configure(background='white')
frame= Frame(width=600, height=100, bg='white', background='white' )
frame.pack()
canvas = Canvas(width=600, height=100, bg='white',borderwidth=5)
canvas.pack(expand=NO, fill=BOTH)
frameP= Frame(width=700, height=100, bg='white', background='white' )
frameP.pack()
frameF= Frame(width=700, height=100, bg='white', background='white' )
frameF.pack()
canvas2 = Canvas(width=700, height=300, bg='white',borderwidth=5)
canvas2.pack(expand=YES,fill=BOTH)
frameFres= Frame(width=700, height=100, bg='white', background='white' )
frameFres.pack()
canvas3 = Canvas(width=700, height=300, bg='white',borderwidth=5)
canvas3.pack(expand=YES,fill=BOTH)

"""---------------------Bodie----------------------"""

Label(frame,text='RADIOCOMUNICACIONES',background='white', font=("Courier", 25)).grid(row=0,column=0)
Label(canvas,text="Conversor",background='white',font=('Courier',13)).grid(row=0,column=0)
Label(canvas,text="Ingrese valor",background='white', font=('Courier',11)).grid(row=1,column=0)
comboDe= ttk.Combobox(canvas,values=["dB","dBm","W","mW","metros","Kilometros"],width=7,foreground='grey')
comboDe.grid(row=1, column=2,padx=5, pady=5)
Label(canvas,text="=", background='white', font='Courier').grid(row=1,column=4)
comboTo= ttk.Combobox(canvas,values=["dB","dBm","W","mW","metros","Kilometros"],width=7,foreground='grey')
comboTo.grid(row=1, column=5,padx=5, pady=5)
ent1 = Entry(canvas,width=20,borderwidth=2)
ent1.grid(row=1,column=1)
textUnit = Entry(canvas,width=10,borderwidth=2)#Caja de texto con el valor convertido
textUnit.grid(row=3,column=2,padx=5, pady=5)
textConv =Entry(canvas,borderwidth=2,width=20)#Caja de texto con las unidades convertidas
textConv.grid(row=3,column=1,padx=5, pady=5)

#Perdidas por espacio libre
Label(frameP,text="Perdidas en el espacio libre",font=("Courier",25),bg='white').grid(row=0,column=0)
Label(canvas2,text='Lfs =', font=('Courier',15),bg='white').grid(row=0,column=0)
frecuenciaT= Entry(canvas2,width=10,borderwidth=2)
frecuenciaT.grid(row=0,column=2)
Label(canvas2,text='f', font=('Courier',15),bg='white').grid(row=0,column=1)
combo1= ttk.Combobox(canvas2,values=["Hz","Mhz","Khz","Ghz"],width=7,foreground='grey')
combo1.grid(row=0,column=3)
Label(canvas2,text=' + D ', font=('Courier',15),bg='white').grid(row=0,column=4)
distancia= Entry(canvas2,width=10,borderwidth=2)
distancia.grid(row=0,column=5)
combo2= ttk.Combobox(canvas2,values=["cm","m","Km","millas"],width=7,foreground='grey')
combo2.grid(row=0,column=6)
Label(canvas2,text=' = ',font=('Courier',15),bg='white').grid(row=0,column=7)
resultado = Entry(canvas2,width=10,borderwidth=2)
resultado.grid(row=0,column=8)

def caLfs():
    f=frecuenciaT.get()
    D=distancia.get()
    if combo1.get()== "Hz":
        f= convertir.hzToGhz(f)
    elif combo1.get() == "Mhz":
        f= convertir.meToKm(f)
    elif combo1.get()=="Khz":
        f=convertir.khzToGhz(f)
    else:
        f=f
    if combo2.get()=="cm":
        D=convertir.cmToKm(D)
    elif combo2.get()=="m":
        D=convertir.meToKm
    elif combo2.get()=="millas":
        D=convertir.millasToKm(D)
    perdidas= Presupuesto() 
    lfs1= perdidas.lfs(float(f),float(D))
    resultado.insert(0,"{:.3f}".format(lfs1)) 
    lfs.insert(0,"{:.3f}".format(lfs1))
    unidad= "dB"
    Label(canvas2,text=unidad,font=('Courier',15),bg='white').grid(row=0,column=9)
    if lfs:
       lfs.config(state=DISABLED) 
    else:
        lfs.config(state=NORMAL)
Button(canvas2, text="Calcular Lfs", background='blue',width=20,fg='white',command= lambda: caLfs()).grid(row =0, column =10,padx=5, pady=5)

#Friis
Label(frameF,text="Relacion senal/ruido",font=("Courier",25),bg='white').grid(row=0,column=0)
Label(canvas2,text='Friis =', font=('Courier',15),bg='white').grid(row=2, column=0)
Ptx= Entry(canvas2,width=10,borderwidth=2)
Ptx.grid(row=2, column=1)
combo1= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo1.grid(row=2,column=2)
Label(canvas2,text=' + ', font=('Courier',15),bg='white').grid(row=2,column=3)
Gtx= Entry(canvas2,width=10,borderwidth=2)
Gtx.grid(row=2,column=4)
combo2= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo2.grid(row=2,column=5)
Label(canvas2,text=' + ', font=('Courier',15),bg='white').grid(row=2,column=6)
Grx= Entry(canvas2,width=10,borderwidth=2)
Grx.grid(row=2,column=7)
combo3= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo3.grid(row=2,column=8)
Label(canvas2,text=' - ', font=('Courier',15),bg='white').grid(row=2,column=9)
lfs= Entry(canvas2,width=10,borderwidth=2)
lfs.grid(row=2,column=10)

combo4= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
combo4.grid(row=2,column=11)

def insertar(caja,combo):
    caja.configure(state=NORMAL)
    caja.delete(0,END)
    caja.insert(0,combo)
    caja.configure(state=DISABLED)

#PIRE

Label(canvas2,text="PIRE= ",font=("Courier",15),bg="white").grid(row=1,column=0)
Label(canvas2,text="Gtx",font=("Courier",15),bg="white").grid(row=1,column=1)
gananciaTx= Entry(canvas2,width=10,borderwidth=2)
gananciaTx.grid(row=1,column=2)
comboGa= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
comboGa.grid(row=1,column=3)
Label(canvas2,text="Ptx",font=("Courier",15),bg='white').grid(row=1,column=4)
potenciaTx= Entry(canvas2,width=10,borderwidth=2)
potenciaTx.grid(row=1,column=5)
comboPo= ttk.Combobox(canvas2,values=["dB","dBm","W","mW"],width=7,foreground='grey')
comboPo.grid(row=1,column=6)
perCombo= ttk.Combobox(canvas2,values=['Incluir perdidas'],width=7)
perCombo.grid(row=1,column=7)




#Conversor de unidades


def agregar():
    try:
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
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
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
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
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
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
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
                conv= convertir.mWatsWats(num)
                conv= convertir.todB(conv)
                insertar(textConv,conv)
                insertar(textUnit,'dB')
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif comboDe.get() == "metros":
            if comboTo.get() == "Kilometros":
                conv= convertir.meToKm(num)
                insertar(textConv,conv)
                insertar(textUnit,'Kilometros')
            elif comboTo.get() == 'metros':
                insertar(textConv,num)
                insertar(textUnit,'metros')
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif comboDe.get() == "Kilometros":
            if comboTo.get() == "metros":
                conv= convertir.kmToM(num)
                insertar(textConv,conv)
                insertar(textUnit,'metros')
            elif comboTo.get() == 'Kilometros':
                insertar(textConv,num)
                insertar(textUnit,'Kilometros')
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
    except:
        messagebox.showerror("Error", message='Ingrese valores')
#Zonas de fresnel

Label(frameFres, text='Zonas de Fresnel y linea de Vista',background='white', font=("Courier", 25)).pack()
Label(canvas3,text="f=",background="white",font=("Courier")).grid(row=0,column=0)
lamb= Entry(canvas3,width=10,borderwidth=2)
lamb.grid(row=0,column=1)
comboF1= ttk.Combobox(canvas3,values=["Hz","Mhz","Khz","Ghz"],width=7,foreground='grey')
comboF1.grid(row=0,column=2)
Label(canvas3,text='D1=',background="white",font=("Courier")).grid(row=0,column=3)
d1= Entry(canvas3, width=10, borderwidth=2)
d1.grid(row=0,column=4)
Label(canvas3,text='D2=',background="white",font=("Courier")).grid(row=0,column=5)
d2= Entry(canvas3, width=10, borderwidth=2)
d2.grid(row=0,column=6)
Label(canvas3,text='Zona=',background="white",font=("Courier")).grid(row=0,column=7)
n= Entry(canvas3, width=10, borderwidth=2)
n.grid(row=0,column=8)
Label(canvas3,text='rn= ',background='white',font=("Courier")).grid(row=1,column=0)
altura= Entry(canvas3, width=10,borderwidth=2)
altura.grid(row=1,column=1)
def calcula():
    D1= d1.get()
    D2= d2.get()
    f= lamb.get()
    Fresnel = presupuesto.Presupuesto()
    Fr= Fresnel.fresnel(D1,D2,f)
    insertar(altura,Fr)
Button(canvas3, text="Calcular altura antena", background='blue',width=20,fg='white',command= lambda: calcula()).grid(row =0, column = 8,padx=5, pady=5)




    
    
photo = PhotoImage(file=r"./assets/convertir.png")    
    


Button(canvas, text="Convertir", background='blue',width=20,fg='white',command= lambda: agregar()).grid(row =3, column = 0,padx=5, pady=5)

mainloop()
