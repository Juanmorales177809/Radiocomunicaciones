from pickle import READONLY_BUFFER
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from modelos import Path,Okumura,Cost
import convertir
from presupuesto import Presupuesto
import unidades
import convertir
import mapaspyQt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets 
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import os
from mapaspyQt import Ui_Dialog





v = Tk()
#v.geometry('500x500')
v.config(background='white')
v.iconbitmap("./assets/antena.ico")
v.title("Calculo de Radio Enlace Terrestre v.1.0")
v.configure(bg='beige')

note = ttk.Notebook(v)
note.pack(pady=10, expand=True)
note.grid(row=0,column=0)
webLabel = ttk.Label(note,text="Hello")
frame1 = Frame(note,width=500,height=500)

frame2 = Frame(note,width=500,height=500)
frame1.pack(fill='both',expand=True)

frame2.pack(fill='both',expand=True)
frame3 = Frame(note,width=500,height=500)
frame3.pack(fill='both',expand=True)
frame4= Frame(frame3,borderwidth=5,border=10)
frame4.grid(row=0,column=0,columnspan=3,pady=30,padx=15)
frame4.config(relief='groove')



imageForum= tk.PhotoImage(file="./assets/ante4.png")
imageForum1= tk.PhotoImage(file="./assets/convertir.png")
imageForum2= tk.PhotoImage(file="./assets/maps.png")
guardar= tk.PhotoImage(file="./assets/Guardar.png")
okupe= tk.PhotoImage(file="./assets/okupeque.png")
costpe= tk.PhotoImage(file="./assets/costpeque.png")
imageForum4= tk.PhotoImage(file="./assets/polar.png")
mapas= PhotoImage(file="./assets/maps.png")
abrir= PhotoImage(file="./assets/abrir.png")
salir= PhotoImage(file="./assets/salir.png")
cancelar= PhotoImage(file="./assets/cancela.png")
listar= PhotoImage(file="./assets/listar.png")



note.add(frame2,image=imageForum)

note.add(frame3,image=imageForum1,state=NORMAL)
note.add(frame1,image=imageForum4,state=NORMAL)


modelosImage= PhotoImage(file="./assets/modelosdeperdidas.png")
botonPath = Button(frame1 ,image=modelosImage, width=500, height=100,compound=tk.LEFT,command=lambda: hello_world())



patloss= PhotoImage(file="./assets/pathsolo.png")
botonPath1 = Button(frame1 ,image=patloss, width=500, height=100,compound=tk.LEFT,command=lambda: path())

okumura= PhotoImage(file="./assets/okumura.png")
botonPath2 = Button(frame1 ,image=okumura, width=500, height=100,compound=tk.LEFT,command=lambda: oku())

cost= PhotoImage(file="./assets/cost.png")
botonPath3 = Button(frame1 ,image=cost, width=500, height=100,compound=tk.LEFT,command=lambda: cos())

long= PhotoImage(file="./assets/long.png")
botonPath4 = Button(frame1 ,image=long, width=500, height=100,compound=tk.LEFT,command=lambda: lon())

radio= PhotoImage(file="./assets/radio.png")
radioenlace = PhotoImage(file="./assets/radioenlace.png")
botonPath5 = Button(frame1 ,image=radioenlace, width=500, height=100,compound=tk.LEFT,command=lambda: lon())

# modelosImage= PhotoImage(file="./assets/modelosdeperdidas.png")
# imagenModelos= Label(frame1, image=modelosImage)

botonPath5.pack()
botonPath.pack()
# imagenModelos.pack()




# google= PhotoImage(file="./assets/mapitas.png")
# botonPath5 = Button(frame1 ,image=google, width=500, height=100,compound=tk.LEFT,command=lambda: lon())
# botonPath5.pack()


def goodbye_world():
    botonPath.configure(command=hello_world)
    botonPath1.destroy()
    botonPath2.destroy()
    botonPath3.destroy()
    botonPath4.destroy()

def hello_world():
    botonPath.configure(command=goodbye_world)
    botonPath1.pack()
    botonPath2.pack()
    botonPath3.pack()
    botonPath4.pack()


#radioenlace
Label(frame2, image=radio, font=(16)).grid(row=0,column=0,sticky=W, columnspan=5)
#Distancia
Label(frame2,text="Distancia :",font=(10)).grid(row=1,column=0,sticky=E)
distancia= Entry(frame2,width=10,borderwidth=3)
distancia.grid(row=1,column=1)
combod= ttk.Combobox(frame2,values=["m","Km","Milles"],width=7)
combod.grid(row=1,column=2,padx=5,pady=5,sticky=W)

#Frecuencia
Label(frame2, text="Frecuencia :",font=(10)).grid(row=2,column=0,sticky=E)
frecuencia = Entry(frame2,width=10,borderwidth=3)
frecuencia.grid(row=2,column=1)
combof= ttk.Combobox(frame2,values=["Hz","Mhz","Khz","Ghz"],width=7)
combof.grid(row=2, column=2,padx=5,pady=5,sticky=W)

#Factor de rugosidad
Label(frame2, text="Factor de rugosidad de terreno :",font=(10)).grid(row=3,column=0,sticky=E)
comboFr= ttk.Combobox(frame2,values=["Agua o terreno liso","Sembrados densos, arenales","Bosques","Terreno normal","Aspero y montañoso"],width=25)
comboFr.grid(row=3, column=1,padx=5,pady=5,columnspan=2)

#Factor de Analisis climatico
Label(frame2, text="Factor de Analisis climatico :",font=(10)).grid(row=4,column=0,sticky=E)
comboFC= ttk.Combobox(frame2,values=["Area marina","Area caliente o humeda","Area Mediterranea","Clima seco y fresco"],width=25)
comboFC.grid(row=4, column=1,padx=5,pady=5,columnspan=2)

#Confiabilidad del sistema
Label(frame2, text="Fiabilidad requerida :",font=(10)).grid(row=5,column=0,sticky=E)
confiabilidad = Entry(frame2,width=10,borderwidth=3)
confiabilidad.grid(row=5,column=1)
Label(frame2, text="%",font=(10)).grid(row=5,column=2,pady=5,sticky=W)

#Ganancia antena transmisora
Label(frame2, text="Ganancia de la antena Tx :",font=(10)).grid(row=6,column=0,sticky=E)
gananciatx = Entry(frame2,width=10,borderwidth=3)
gananciatx.grid(row=6,column=1)
combotx= ttk.Combobox(frame2,values=["dBm","dBi"],width=7)
combotx.grid(row=6, column=2,padx=5,pady=5,sticky=W)

#Ganancia antena receptora
Label(frame2, text="Ganancia de la antena Rx :",font=(10)).grid(row=7,column=0,sticky=E)
gananciarx = Entry(frame2,width=10,borderwidth=3)
gananciarx.grid(row=7,column=1)
comborx= ttk.Combobox(frame2,values=["dBb","dBi"],width=7)
comborx.grid(row=7, column=2,padx=5,pady=5,sticky=W)

#Perdidas por cable
Label(frame2, text="Perdidas por cable Lf :",font=(10)).grid(row=8,column=0,sticky=E)
perdidasCable = Entry(frame2,width=10,borderwidth=3)
perdidasCable.grid(row=8,column=1,pady=5)
Label(frame2, text="dB",font=(10)).grid(row=8,column=2,sticky=W)

#Perdidas por acople
Label(frame2, text="Perdidas por acople Lb :",font=(10)).grid(row=9,column=0,sticky=E)
perdidasAcople = Entry(frame2,width=10,borderwidth=3)
perdidasAcople.grid(row=9,column=1,pady=5)
Label(frame2, text="dB",font=(10)).grid(row=9,column=2,sticky=W)


#Sensibilidad receptora
Label(frame2, text="Sensibilidad Rx :",font=(10)).grid(row=10,column=0,sticky=E)
sensibilidad = Entry(frame2,width=10,borderwidth=3)
sensibilidad.grid(row=10,column=1)
combo4= ttk.Combobox(frame2,values=["dBm","μV"],width=7,state=READONLY_BUFFER)
combo4.grid(row=10, column=2,padx=5,pady=5,sticky=W)

#Ancho de banda
Label(frame2, text="BW :",font=(10)).grid(row=11,column=0,sticky=E)
bw = Entry(frame2,width=10,borderwidth=3)
bw.grid(row=11,column=1,pady=5)
Label(frame2, text="Mhz",font=(10)).grid(row=11,column=2,sticky=W)

#Relación señal a ruido
Label(frame2, text="C/N :",font=(10)).grid(row=12,column=0,sticky=E)
Sn = Entry(frame2,width=10,borderwidth=3)
Sn.grid(row=12,column=1,pady=5)
Label(frame2, text="dBm",font=(10)).grid(row=12,column=2,sticky=W)

#Modelo de perdidas
    

radioValue= IntVar()
Label(frame2, text="Modelo de perdidas ",font=(10)).grid(row=13,column=0,sticky=E)
radio1= Radiobutton(frame2,text="Path Loss", variable=radioValue,value=0,command=lambda: path())
radio1.grid(row=13,column=1,sticky=W)
radio2= Radiobutton(frame2,text="Okumura-Hata", variable=radioValue,value=1,command=lambda: oku())
radio2.grid(row=14,column=1,sticky=W)
radio3= Radiobutton(frame2,text="Cost-231",variable=radioValue,value=2,command=lambda: cos())
radio3.grid(row=15,column=1,sticky=W)
radio4= Radiobutton(frame2,text="Longley-Rice", variable=radioValue,value=3,command=lambda: lon())
radio4.grid(row=16,column=1,sticky=W)


#Perdidas por espacio libre


Label(frame2, text="Lp :",font=(10)).grid(row=17,column=0,sticky=E)
perdidas = Entry(frame2,width=10,borderwidth=3,state=DISABLED)
perdidas.grid(row=17,column=1,pady=5)
Label(frame2, text="dB",font=(10)).grid(row=17,column=2,sticky=W)
Button(frame2,text="Calcular",background='#336DBA',width=15,fg='white',command=lambda: resultados()).grid(row=17,column=0)
Button(frame2,image=listar,background='white',fg='white',command=lambda: lon()).grid(row=18,column=2,pady=20,sticky=E)
Button(frame2,image=cancelar,background='white',fg='white',command=lambda: limpiar()).grid(row=18,column=2,pady=20,sticky=W)
Button(frame2,image=mapas,background='white',fg='white',command=lambda: googmaps()).grid(row=18,column=0,pady=20,sticky=W,padx=20)
Button(frame2,image=guardar,background='white',fg='white',command=lambda: v.destroy()).grid(row=18,column=3,pady=20,sticky=E)
Button(frame2,image=salir,background='white',fg='white',command=lambda: v.destroy()).grid(row=18,column=4,pady=20,sticky=E)

    

class Modelos:
    
    def enviar(self,lfs,f,d,uf,ud,ventana):
            perdidas.configure(state=NORMAL)
            perdidas.delete(0, END)
            perdidas.insert(0,"{:.3f}".format(lfs))
            perdidas.configure(state=DISABLED)
            distancia.configure(state=NORMAL)
            distancia.delete(0, END)
            distancia.insert(0,"{:.3f}".format(f))
            distancia.configure(state=DISABLED)
            frecuencia.configure(state=NORMAL)
            frecuencia.delete(0, END)
            frecuencia.insert(0,"{:.3f}".format(d))
            frecuencia.configure(state=DISABLED)
            combof.configure(state=NORMAL)
            combof.delete(0, END)
            combof.insert(0,uf)
            combof.configure(state=DISABLED)
            combod.configure(state=NORMAL)
            combod.delete(0, END)
            combod.insert(0,ud)
            combod.configure(state=DISABLED)
            ventana.destroy()
            

            messagebox.showinfo("Envio exitoso", "Los datos han sido enviados con exito")
    def convertirUnidades(self,d,f,uf,ud):
        try:
        
            if ud=='Milles':
                d= convertir.millasToKm(d)
            elif ud=="m":
                d= convertir.meToKm(d)
            if uf== 'Hz':
                f=convertir.HztoMhz(f)
            elif uf== 'KHz':
                f= convertir.KhztoMhz(f)
            elif uf== 'GHz':
                f= convertir.GhztoMhz(f)
            
            return d,f
        except:
            messagebox.showwarning( "Warning","Datos no validos")
    def asignar(self,lp):
        self.resultado.configure(state=NORMAL)
        self.resultado.delete(0, END)
        self.resultado.insert(0,"{:.3f}".format(lp))
        self.resultado.configure(state=DISABLED)

class SelecOkamura(Modelos):

    def __init__(self):
        self.ciudad=IntVar(value=0)
        self.sub= BooleanVar()

    def ventana(self):
        ventana = Toplevel()
        ventana.geometry("350x400")
        ventana.resizable(0,0)
        # ventana.config(bg='#d7f3bc')
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Okumura-Hata")
        self.radioValor=IntVar()
        Label(ventana,text="Distancia ").grid(row=0,column=0)
        self.distancia= Entry(ventana,width=17,borderwidth=3)
        self.distancia.grid(row=0,column=1,pady=5)
        self.comboD= ttk.Combobox(ventana, values=["m","Km","Milles"],width=7)
        self.comboD.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        Label(ventana,text="frecuencia ").grid(row=1,column=0)
        self.frecuencia= Entry(ventana,width=17,borderwidth=3)
        self.frecuencia.grid(row=1,column=1,pady=5)
        self.combof= ttk.Combobox(ventana, values=["Hz","KHz","MHz","GHz"],width=7)
        self.combof.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        Label(ventana,text="Altura efectiva antena Tx").grid(row=2,column=0)
        self.hte= Entry(ventana,width=17,borderwidth=3)
        self.hte.grid(row=2,column=1,pady=5)
        Label(ventana,text='m').grid(row=2, column=2,sticky=W)
        Label(ventana,text="Altura efectiva antena Rx").grid(row=3,column=0)
        self.hre= Entry(ventana,width=17,borderwidth=3)
        self.hre.grid(row=3,column=1,pady=5)
        Label(ventana,text='m').grid(row=3, column=2,sticky=W)
        grande= Radiobutton(ventana,text="Ciudad Grande",variable=self.ciudad,value=0)
        grande.grid(row=4,column=1,sticky=W)
        pequena= Radiobutton(ventana,text="Ciudad pequeña",variable=self.ciudad,value=1)
        pequena.grid(row=5,column=1,sticky=W)
        Label(ventana,textvariable=self.radioValor).grid(row=5,column=2)
        urbano= Checkbutton(ventana,text="Zona Suburbana",variable= self.sub,onvalue=True, offvalue=False)
        urbano.grid(row=6,column=1)
        Button(ventana,text="Lp",background='#336DBA',width=15,fg='white',
                    command=lambda: self.calcular()).grid(row=7,column=0,padx=15)
        Button(ventana,text="Enviar",background='#336DBA',width=15,fg='white',
                command=lambda: self.enviar(self.lp,float(self.distancia.get()),float(self.frecuencia.get()),self.combof.get(),self.comboD.get(),ventana)).grid(row=8,column=1,pady=30)
        Label(ventana,text="dB").grid(row=7, column=2,sticky=W)
        self.resultado= Entry(ventana,borderwidth=3,width=17)
        self.resultado.grid(row=7, column=1)
        mapas= Button(ventana,image=imageForum2,fg='white',command=lambda: lon())
        mapas.grid(row=9,column=0,padx=15,pady=15)
        
    
    def calcular(self):
        try:
            d= float(self.distancia.get())
            f= float(self.frecuencia.get())
            hte= float(self.hte.get())
            hre= float(self.hre.get())
            ud= self.comboD.get()
            uf= self.combof.get()
            d,f= self.convertirUnidades(d,f,uf,ud)
            
            modelo= Okumura(f,d,hte,hre)
            a= modelo.calcularA(self.ciudad.get())
            
            self.lp= modelo.calcular(self.sub.get(),a)
            print(a,self.sub.get(), self.ciudad.get())
            self.asignar(self.lp)
        except:
            messagebox.showwarning( "Warning","Datos no validos")

class Cost231(Modelos):
    def __init__(self):
        self.factor= BooleanVar()
        self.sub= BooleanVar()
        self.ciudad= IntVar()
    def ventanas(self):
        
        self.ventana = Toplevel()
        self.ventana.geometry("350x380")
        self.ventana.resizable(0,0)
        self.ventana.iconbitmap("./assets/antena.ico")
        self.ventana.title("Cost-231")
        Label(self.ventana,text="Distancia ").grid(row=0,column=0)
        self.distancia= Entry(self.ventana,width=17,borderwidth=3)
        self.distancia.grid(row=0,column=1,pady=5)
        self.comboD= ttk.Combobox(self.ventana, values=["m","Km","Milles"],width=7)
        self.comboD.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        Label(self.ventana,text="frecuencia ").grid(row=1,column=0)
        self.frecuencia= Entry(self.ventana,width=17,borderwidth=3)
        self.frecuencia.grid(row=1,column=1,pady=5)
        self.combof= ttk.Combobox(self.ventana, values=["KHz","MHz","GHz"],width=7)
        self.combof.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        Label(self.ventana,text="Altura efectiva antena Tx").grid(row=2,column=0)
        self.hte= Entry(self.ventana,width=17,borderwidth=3)
        self.hte.grid(row=2,column=1,pady=5)
        Label(self.ventana,text='m').grid(row=2, column=2,sticky=W)
        Label(self.ventana,text="Altura efectiva antena Rx").grid(row=3,column=0)
        self.hre= Entry(self.ventana,width=17,borderwidth=3)
        self.hre.grid(row=3,column=1,pady=5)
        Label(self.ventana,text='m').grid(row=3, column=2,sticky=W)
        grande= Radiobutton(self.ventana,text="Ciudad Grande",variable=self.ciudad,value=0)
        grande.grid(row=4,column=1,sticky=W)
        pequena= Radiobutton(self.ventana,text="Ciudad pequeña",variable=self.ciudad,value=1)
        pequena.grid(row=5,column=1,sticky=W)
        # check= Checkbutton(ventana,text="Zona Suburbana",var=self.sub,onvalue=True, offvalue=False)
        # check.grid(row=6,column=1,pady=10)
        self.combofactor= ttk.Combobox(self.ventana,values=["Ciudad densa","Ciudad","Barrios campestres","Rural"],width=15)
        self.combofactor.grid(row=6,column=1,pady=10)
        # self.combofactor.configure(state=DISABLED)
        # chackFac= Checkbutton(ventana,text='Aplicar factor de corrección', var=self.factor,onvalue=True, offvalue=False,command=lambda: self.activar())
        # chackFac.grid(row=7,column=1,columnspan=2,sticky=W)
        Label(self.ventana,text="Factor de corrección").grid(row=6,column=0)
        Button(self.ventana,text="Lp",background='#336DBA',width=15,fg='white',
                    command=lambda: self.calcular()).grid(row=7,column=0,padx=15)
        Button(self.ventana,text="Enviar",background='#336DBA',width=15,fg='white',
                command=lambda: self.enviar(self.lp,float(self.frecuencia.get()),float(self.distancia.get()),self.combof.get(),self.comboD.get(),self.ventana)).grid(row=8,column=1,pady=15)
        Label(self.ventana,text="dB").grid(row=7, column=2,sticky=W)
        self.resultado= Entry(self.ventana,borderwidth=3,width=17)
        self.resultado.grid(row=7, column=1,pady=5)
        mapas= Button(self.ventana,image=imageForum2,fg='white',command=lambda: lon())
        mapas.grid(row=9,column=0,padx=15,pady=15)

    def activar(self):
        if self.factor:
            self.combofactor.configure(state=NORMAL)
        else:
            self.combofactor.configure(state=DISABLED)
    def calcular(self):
        try:
            d= float(self.distancia.get())
            f= float(self.frecuencia.get())
            ud= self.comboD.get()
            uf= self.combof.get()
            d,f= self.convertirUnidades(d,f,uf,ud)
            print(f)
            c= self.combofactor.get()
            hte= float(self.hte.get())
            hre= float(self.hre.get())
            modelo= Cost(f,d,hte,hre)
            a= modelo.calcularA(self.ciudad.get())
            self.lp= modelo.calcular(c,a)
            if self.lp==False:
                messagebox.showerror("Ërror", "solo admite frecuencias entre 1.5Ghz y 2Ghz")
                self.ventana.destroy()
            print(self.lp)
            self.asignar(self.lp)
            
        except:
            messagebox.showwarning( "Warning","Datos no validos")
        
    
class PathLoss(Modelos):
    def ventana(self):
        ventana = Toplevel()
        ventana.geometry("350x250")
        ventana.resizable(0,0)
        # ventana.config(bg='#d7f3bc')
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Path Loss")
        radioValCo= IntVar()
        Label(ventana,text="  Distancia  ").grid(row=0,column=0)
        self.distancia= Entry(ventana,width=17,borderwidth=3)
        self.distancia.grid(row=0,column=1,pady=5,columnspan=2)
        self.comboD= ttk.Combobox(ventana, values=["m","Km","Milles"],width=7)
        self.comboD.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        Label(ventana,text="  Frecuencia  ").grid(row=1,column=0)
        self.frecuencia= Entry(ventana,width=17,borderwidth=3)
        self.frecuencia.grid(row=1,column=1,pady=5, columnspan=2)
        self.combof= ttk.Combobox(ventana, values=["KHz","MHz","GHz"],width=7)
        self.combof.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        Button(ventana,text="Lfs",background='#336DBA',width=15,fg='white',
            command=lambda: self.calcular()).grid(row=3,column=0,padx=15)
        Button(ventana,text="Enviar",background='#336DBA',width=15,fg='white',
            command=lambda: self.enviar(self.lfs,float(self.distancia.get()),float(self.frecuencia.get()),self.combof.get(),self.comboD.get(),ventana)).grid(row=5,column=1,columnspan=2,pady=30)
        Label(ventana,text="dB").grid(row=3, column=3,sticky=W)
        self.result= Entry(ventana,borderwidth=3,width=17)
        self.result.grid(row=3, column=1,columnspan=2,pady=5,padx=5)
        mapas= Button(ventana,image=imageForum2,fg='white',command=lambda: lon())
        mapas.grid(row=6,column=0,padx=15,pady=15)
    
    def calcular(self):
        if self.comboD.get()=='m':
            d= float(self.distancia.get())
            d= convertir.meToKm(d)
        elif self.comboD.get()=='Milles':
            d= float(self.distancia.get())
            d= convertir.millasToKm(d)
        else:
            d= float(self.distancia.get())
        if self.combof.get()== 'MHz':
            f= float(self.frecuencia.get())
            f= convertir.megGig(f)
        elif self.combof.get()== 'KHz':
            f= float(self.frecuencia.get())
            f= convertir.khzToGhz(f)
        else:
            f= float(self.frecuencia.get())
        modelo= Path(d,f)
        self.lfs= modelo.calcular()
        self.result.configure(state=NORMAL)
        self.result.delete(0, END)
        self.result.insert(0,"{:.3f}".format(self.lfs))
        self.result.configure(state=DISABLED)

class Conversor:
    
    def ventana(self):
        Label(frame4,text="Ingrese valor", font=(11)).grid(row=1,column=0, padx=15,pady=5)
        self.unidadesD= ttk.Combobox(frame4,values=["dB","dBm","W","mW","dBd","dBi","metros","Kilometros"],width=7,foreground='grey')
        self.unidadesD.grid(row=1, column=2,padx=5,pady=5)
        Label(frame4,text="=").grid(row=1,column=4)
        self.unidadesA= ttk.Combobox(frame4,values=["dB","dBm","W","mW","dBd","dBi","metros","Kilometros"],width=7,foreground='grey')
        self.unidadesA.grid(row=1, column=5,padx=5, pady=5,sticky=W)
        self.entrada = Entry(frame4,width=20,borderwidth=2)
        self.entrada.grid(row=1,column=1)
        self.unidad = Entry(frame4,width=10,borderwidth=2)#Caja de texto con el valor convertido
        self.unidad.grid(row=3,column=2,padx=5, pady=5)
        self.numeros =Entry(frame4,borderwidth=2,width=20)#Caja de texto con las unidades convertidas
        self.numeros.grid(row=3,column=1,padx=5, pady=5)
        Button(frame4,text="Convertir", background="#336DBA",fg='white',command=lambda: self.calcular()).grid(row=3,column=0,pady=5)
    
    def calcular(self):
        self.num, self.uni = unidades.agregar(float(self.entrada.get()),self.unidadesD.get(),self.unidadesA.get())
        self.asignar()
    def asignar(self):
        self.numeros.configure(state=NORMAL)
        self.numeros.delete(0, END)
        self.numeros.insert(0,"{:.1f}".format(self.num))
        self.numeros.configure(state=DISABLED)
        self.unidad.configure(state=NORMAL)
        self.unidad.delete(0, END)
        self.unidad.insert(0,self.uni)
        self.unidad.configure(state=DISABLED)


class Resultado():
    
    def ventana(self):
        self.ven = Toplevel()
        self.ven.geometry("300x350")
        self.ven.resizable(0,0)
        self.ven.iconbitmap("./assets/antena.ico")
        self.ven.title("Presupuesto de potencia")
        frames= Frame(self.ven)
        frames.pack(anchor=CENTER,expand=True, fill=tk.X)
        frames.config(relief='groove')
        #Label(ventana,image=imageForum3).grid(row=4,column=1, columnspan=3)
        Label(frames,text="Desvanecimiento: ").grid(row=1,column=0,pady=5,ipadx=10)
        self.desvanecimiento= Entry(frames,width=10)
        self.desvanecimiento.grid(row=1,column=1,pady=5)
        Label(frames,text="dB").grid(row=1,column=2)
        Label(frames,text="Gs: ").grid(row=2,column=0,pady=5)
        self.gananciaSistema= Entry(frames,width=10)
        self.gananciaSistema.grid(row=2,column=1,pady=5)
        Label(frames,text="dB").grid(row=2,column=2)
        Label(frames,text="Sensibilidad de Rtx: ").grid(row=3,column=0, pady=5)
        self.cmin= Entry(frames, width=10)
        self.cmin.grid(row=3,column=1,pady=5)
        Label(frames,text="dB").grid(row=3,column=2)
        Label(frames,text="Ptx: ").grid(row=4,column=0,pady=5)
        self.ptxE= Entry(frames,width=10)
        self.ptxE.grid(row=4,column=1,pady=5)
        Label(frames,text="dBm").grid(row=4,column=2)
        Label(frames,text="PIRE: ").grid(row=5,column=0,pady=5)
        self.pireR= Entry(frames,width=10)
        self.pireR.grid(row=5,column=1)
        Label(frames,text="dB").grid(row=5,column=2)
        Label(frames,text="Friis: ").grid(row=6,column=0,pady=5)
        self.friis= Entry(frames,width=10)
        self.friis.grid(row=6,column=1)
        Label(frames,text="dB").grid(row=6,column=2)
        Label(frames,text="Potencia recibida: ").grid(row=7,column=0,pady=5)
        self.potenciaRecibida= Entry(frames,width=10)
        self.potenciaRecibida.grid(row=7,column=1)
        Label(frames,text="dB").grid(row=7,column=2)
        Label(frames,text="Perdidas en el espacio libre: ").grid(row=8,column=0,pady=5)
        self.perdidasCalculadas= Entry(frames,width=10)
        self.perdidasCalculadas.grid(row=8,column=1)
        Label(frames,text="dB").grid(row=8,column=2)
        # Button(frames,image=abrir,background='white',fg='white',command=lambda: resultados()).grid(row=7,column=1, pady= 000)
        Button(frames,image=guardar,background='white',fg='white',command=lambda: resultados()).grid(row=9,column=2,sticky=E,pady=5,columnspan=2)
    
    def calcular(self):
        j,h,x= verificarDatos()
        if j and h and x:
            
            anchoB= convertir.MhztoHz(float(bw.get()))
            presupuesto = Presupuesto(float(frecuencia.get()),float(distancia.get()),float(confiabilidad.get()),comboFr.get(),
                        comboFC.get(),anchoB,float(sensibilidad.get()),float(Sn.get()),float(perdidasCable.get()),float(perdidasAcople.get()),
                        float(gananciatx.get()),float(gananciarx.get()),float(perdidas.get()))
            fc= presupuesto.desvanecimiento()
            Gs= presupuesto.gananciaSistema()
            cmin= presupuesto.cmin()
            ptx= presupuesto.ptx()
            pire= presupuesto.PIRE()
            friis= presupuesto.friis()
            Ptx= presupuesto.potenciaRecibida()
            lfs= float(perdidas.get())
            
            
            self.desvanecimiento.configure(state=NORMAL)
            self.desvanecimiento.delete(0, END)
            self.desvanecimiento.insert(0,"{:.1f}".format(fc))
            self.desvanecimiento.configure(state=DISABLED)

            self.gananciaSistema.configure(state=NORMAL)
            self.gananciaSistema.delete(0, END)
            self.gananciaSistema.insert(0,"{:.1f}".format(Gs))
            self.gananciaSistema.configure(state=DISABLED)

            self.cmin.configure(state=NORMAL)
            self.cmin.delete(0, END)
            self.cmin.insert(0,"{:.1f}".format(cmin))
            self.cmin.configure(state=DISABLED)

            self.ptxE.configure(state=NORMAL)
            self.ptxE.delete(0, END)
            self.ptxE.insert(0,"{:.1f}".format(ptx))
            self.ptxE.configure(state=DISABLED)

            self.pireR.configure(state=NORMAL)
            self.pireR.delete(0, END)
            self.pireR.insert(0,"{:.1f}".format(pire))
            self.pireR.configure(state=DISABLED)
            
            self.friis.configure(state=NORMAL)
            self.friis.delete(0, END)
            self.friis.insert(0,"{:.1f}".format(friis))
            self.friis.configure(state=DISABLED)
            
            self.potenciaRecibida.configure(state=NORMAL)
            self.potenciaRecibida.delete(0, END)
            self.potenciaRecibida.insert(0,"{:.1f}".format(Ptx))
            self.potenciaRecibida.configure(state=DISABLED)
        
            self.perdidasCalculadas.configure(state=NORMAL)
            self.perdidasCalculadas.delete(0, END)
            self.perdidasCalculadas.insert(0,"{:.1f}".format(lfs))
            self.perdidasCalculadas.configure(state=DISABLED)
        else:
            self.ven.destroy()
            messagebox.showerror("Error","Ingrese todos los valores")
        

def lon():
    messagebox.showinfo("Mantenimiento", "Esta sección está en construcción")
def limpiar():
    frecuencia.configure(state=NORMAL)
    frecuencia.delete(0, END)
    combof.configure(state=NORMAL)
    combof.delete(0, END)
    distancia.configure(state=NORMAL)
    distancia.delete(0, END)
    combod.configure(state=NORMAL)
    combod.delete(0, END)
    comboFr.configure(state=NORMAL)
    comboFr.delete(0, END)
    comboFC.configure(state=NORMAL)
    comboFC.delete(0, END)
    confiabilidad.configure(state=NORMAL)
    confiabilidad.delete(0, END)
    bw.configure(state=NORMAL)
    bw.delete(0, END)
    gananciarx.configure(state=NORMAL)
    gananciarx.delete(0, END)
    gananciatx.configure(state=NORMAL)
    gananciatx.delete(0, END)
    sensibilidad.configure(state=NORMAL)
    sensibilidad.delete(0, END)
    perdidasAcople.configure(state=NORMAL)
    perdidasAcople.delete(0, END)
    perdidasCable.configure(state=NORMAL)
    perdidasCable.delete(0, END)
    perdidas.configure(state=NORMAL)
    perdidas.delete(0, END)
    comborx.configure(state=NORMAL)
    comborx.delete(0, END)
    combotx.configure(state=NORMAL)
    combotx.delete(0, END)
    Sn.configure(state=NORMAL)
    Sn.delete(0, END)
    Sn.configure(state=NORMAL)
    Sn.delete(0, END)
def verificarDatos():
    vector= {1: distancia.get(),2: frecuencia.get(),5: confiabilidad.get(),6: gananciatx.get(),
            7: gananciarx.get(),8:perdidasCable.get(),9:perdidasAcople.get(),10:sensibilidad.get(),
            11:bw.get(),12:Sn.get(),17: perdidas.get()}
    vec= list(vector.items())
    vector1= {1: combod.get(), 2: combof.get(),6:combotx.get(),7:comborx.get(),10:combo4.get()}
    vec1= list(vector1.items())
    vector2= {3: comboFr.get(), 4: comboFC.get()}
    vec2= list(vector2.items())
    y= True
    h= True
    x= True
    for i in range(0,len(vec)):
        v= list(vec[i])
        
        if v[1]== '':
            g= v[0]
            Label(frame2, text="*", fg='red' ).grid(row=g,column=1,sticky=E)
            y= False
        elif v[1]!= '':
            g= v[0]
            Label(frame2, text="  ").grid(row=g,column=1,sticky=E)
    for i in range(0,len(vec1)):
        v1= list(vec1[i])
        if v1[1]=='':
            g1=v1[0]
            
            Label(frame2, text="*", fg='red' ).grid(row=g1,column=3,sticky=W)
            h= False
        elif v1 != '':
            g1=v1[0]
            Label(frame2, text="  ", fg='red' ).grid(row=g1,column=3,sticky=W) 
    for i in range(0,len(vec2)):
        v2= list(vec2[i])
        if v2[1]=='':
            g2=v2[0]
            
            Label(frame2, text="*", fg='red' ).grid(row=g2,column=3,sticky=W)
            x= False
        elif v2 != '':
            g2=v2[0]
            Label(frame2, text="  ", fg='red' ).grid(row=g2,column=3,sticky=W) 
    return y,h,x
def googmaps():
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())


def resultados():
    resultados= Resultado()
    resultados.ventana()
    resultados.calcular()

def path():
    loss= PathLoss()
    loss.ventana()

def oku():
    okumura= SelecOkamura()
    okumura.ventana()
def cos():
    cost= Cost231()
    cost.ventanas()





if __name__ == "__main__":
    conversor= Conversor()
    conversor.ventana()

v.mainloop()