from calendar import c
from pickle import READONLY_BUFFER
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from matplotlib.pyplot import text
from numpy import imag
from pyparsing import col
from modelos import Path,Okumura,Cost
import convertir
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import unidades





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
#presupuesto= PhotoImage(file="./assets/cost231.jpg")


note.add(frame1,image=imageForum,state=NORMAL)

note.add(frame2,image=imageForum4)
note.add(frame3,image=imageForum1)

patloss= PhotoImage(file="./assets/pathsolo.png")
botonPath = Button(frame1 ,image=patloss, width=500, height=100,compound=tk.LEFT,command=lambda: path())
botonPath.pack()

okumura= PhotoImage(file="./assets/okumura.png")
botonPath2 = Button(frame1 ,image=okumura, width=500, height=100,compound=tk.LEFT,command=lambda: oku())
botonPath2.pack()

cost= PhotoImage(file="./assets/cost.png")
botonPath3 = Button(frame1 ,image=cost, width=500, height=100,compound=tk.LEFT,command=lambda: cos())
botonPath3.pack()

long= PhotoImage(file="./assets/long.png")
botonPath4 = Button(frame1 ,image=long, width=500, height=100,compound=tk.LEFT,command=lambda: lon())
botonPath4.pack()

google= PhotoImage(file="./assets/mapitas.png")
botonPath5 = Button(frame1 ,image=google, width=500, height=100,compound=tk.LEFT,command=lambda: lon())
botonPath5.pack()


    


#radioenlace
Label(frame2, text="Radio Enlace", font=(16)).grid(row=0,column=0,sticky=W)
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
comboFr= ttk.Combobox(frame2,values=["Agua o terreno liso","Sembrados densos, arenales","Bosques","Terreno normal","Aspero, motañoso"],width=25)
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
cn = Entry(frame2,width=10,borderwidth=3)
cn.grid(row=12,column=1,pady=5)
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
Button(frame2,image=mapas,background='white',fg='white',command=lambda: lon()).grid(row=18,column=3,pady=20,sticky=E)
Button(frame2,image=mapas,background='white',fg='white',command=lambda: limpiar()).grid(row=18,column=2,pady=20,sticky=E)
#Button(frame2,image=mapas,background='white',fg='white',command=lambda: listar1()).grid(row=18,column=1,pady=20,sticky=E)
Button(frame2,image=mapas,background='white',fg='white',command=lambda: listar()).grid(row=18,column=4,pady=20,sticky=E)


    

class Modelos:
    
    def enviar(self,lfs,f,d,uf,ud):
            perdidas.configure(state=NORMAL)
            perdidas.delete(0, END)
            perdidas.insert(0,"{:.3f}".format(lfs))
            perdidas.configure(state=DISABLED)
            distancia.configure(state=NORMAL)
            distancia.delete(0, END)
            distancia.insert(0,"{:.3f}".format(d))
            distancia.configure(state=DISABLED)
            frecuencia.configure(state=NORMAL)
            frecuencia.delete(0, END)
            frecuencia.insert(0,"{:.3f}".format(f))
            frecuencia.configure(state=DISABLED)
            combof.configure(state=NORMAL)
            combof.delete(0, END)
            combof.insert(0,uf)
            combof.configure(state=DISABLED)
            combod.configure(state=NORMAL)
            combod.delete(0, END)
            combod.insert(0,ud)
            combod.configure(state=DISABLED)
    def convertirUnidades(self,d,f,uf,ud):
        try:
        
            if ud=='Milles':
                d= convertir.millasToKm(d)
                d= convertir.kmToM(d)
            elif ud=="Km":
                d= convertir.kmToM(d)
            if uf== 'MHz':
                f= convertir.MhztoHz(f)
            elif uf== 'KHz':
                f= convertir.KhztoHz(f)
            elif uf== 'GHz':
                f= convertir.GhztoHz(f)
            
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
                command=lambda: self.enviar(self.lp,float(self.distancia.get()),float(self.frecuencia.get()),self.combof.get(),self.comboD.get())).grid(row=8,column=1,pady=30)
        Label(ventana,text="dB").grid(row=7, column=2,sticky=W)
        self.resultado= Entry(ventana,borderwidth=3,width=17)
        self.resultado.grid(row=7, column=1)
        mapas= Button(ventana,image=imageForum2,fg='white',command=lambda: lon())
        mapas.grid(row=9,column=0,padx=15,pady=15)
        
    
    def calcular(self):
        try:
            d= float(self.distancia.get()) 
            f= float(self.frecuencia.get())
            ud= self.comboD.get()
            uf= self.combof.get()
            d,f= self.convertirUnidades(d,f,uf,ud)
            
            hte= float(self.hte.get())
            hre= float(self.hre.get())

            modelo= Okumura(f,d,hte,hre)
            self.lp= modelo.calcular(self.ciudad.get(),self.sub.get())
            self.asignar(self.lp)
        except:
            messagebox.showwarning( "Warning","Datos no validos")

class Cost231(Modelos):
    def __init__(self):
        self.factor= BooleanVar()
        self.sub= BooleanVar()
        self.ciudad= IntVar()
    def ventana(self):
        
        ventana = Toplevel()
        ventana.geometry("350x380")
        ventana.resizable(0,0)
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Cost-231")
        Label(ventana,text="Distancia ").grid(row=0,column=0)
        self.distancia= Entry(ventana,width=17,borderwidth=3)
        self.distancia.grid(row=0,column=1,pady=5)
        self.comboD= ttk.Combobox(ventana, values=["m","Km","Milles"],width=7)
        self.comboD.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        Label(ventana,text="frecuencia ").grid(row=1,column=0)
        self.frecuencia= Entry(ventana,width=17,borderwidth=3)
        self.frecuencia.grid(row=1,column=1,pady=5)
        self.combof= ttk.Combobox(ventana, values=["KHz","MHz","GHz"],width=7)
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
        # check= Checkbutton(ventana,text="Zona Suburbana",var=self.sub,onvalue=True, offvalue=False)
        # check.grid(row=6,column=1,pady=10)
        self.combofactor= ttk.Combobox(ventana,values=["Ciudad densa","Ciudad","Barrios campestres","Rural"],width=15)
        self.combofactor.grid(row=6,column=1,pady=10)
        # self.combofactor.configure(state=DISABLED)
        # chackFac= Checkbutton(ventana,text='Aplicar factor de corrección', var=self.factor,onvalue=True, offvalue=False,command=lambda: self.activar())
        # chackFac.grid(row=7,column=1,columnspan=2,sticky=W)
        Label(ventana,text="Factor de corrección").grid(row=6,column=0)
        Button(ventana,text="Lp",background='#336DBA',width=15,fg='white',
                    command=lambda: self.calcular()).grid(row=7,column=0,padx=15)
        Button(ventana,text="Enviar",background='#336DBA',width=15,fg='white',
                command=lambda: self.enviar(self.lp,float(self.frecuencia.get()),float(self.distancia.get()),self.combof.get(),self.comboD.get())).grid(row=8,column=1,pady=15)
        Label(ventana,text="dB").grid(row=7, column=2,sticky=W)
        self.resultado= Entry(ventana,borderwidth=3,width=17)
        self.resultado.grid(row=7, column=1,pady=5)
        mapas= Button(ventana,image=imageForum2,fg='white',command=lambda: lon())
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
            c= self.combofactor.get()
            hte= float(self.hte.get())
            hre= float(self.hre.get())
            modelo= Cost(f,d,hte,hre)
            self.lp= modelo.calcular(c,self.ciudad.get())
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
            command=lambda: self.enviar(self.lfs,float(self.distancia.get()),float(self.frecuencia.get()),self.combof.get(),self.comboD.get())).grid(row=5,column=1,columnspan=2,pady=30)
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


class Resultado:
    def __init__(self,pire,friis,fc,ptx,gs,):
        self.pire = pire
        self.friis= friis
        self.fc = fc
        self.ptx = ptx
        self.gs = gs

    def ventana(self):
        ventana = Toplevel()
        ventana.geometry("400x350")
        ventana.resizable(0,0)
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Presupuesto de potencia")
        frames= Frame(ventana)
        frames.pack(anchor=CENTER,expand=True, fill=tk.X)
        frames.config(relief='groove')
        #Label(ventana,image=imageForum3).grid(row=4,column=1, columnspan=3)
        Label(frames,text="PIRE:").grid(row=1,column=0,pady=5,ipadx=10)
        self.pireE= Entry(frames,width=10)
        self.pireE.grid(row=1,column=1,pady=5)
        Label(frames,text="dB").grid(row=1,column=2)
        Label(frames,text="Friis:").grid(row=2,column=0,pady=5)
        self.friisE= Entry(frames,width=10)
        self.friisE.grid(row=2,column=1,pady=5)
        Label(frames,text="   dB   ").grid(row=2,column=2)
        Label(frames,text="Fc:").grid(row=3,column=0, pady=5)
        self.fcE= Entry(frames, width=10)
        self.fcE.grid(row=3,column=1,pady=5)
        Label(frames,text="   dB   ").grid(row=3,column=2)
        Label(frames,text="Ptx:").grid(row=4,column=0,pady=5)
        self.ptxE= Entry(frames,width=10)
        self.ptxE.grid(row=4,column=1,pady=5)
        Label(frames,text="   dBm   ").grid(row=4,column=2)
        Label(frames,text="             Ganancia del sitema:            ").grid(row=5,column=0,pady=5)
        self.gsE= Entry(frames,width=10)
        self.gsE.grid(row=5,column=1)
        Label(frames,text="   dB   ").grid(row=5,column=2)
        # Button(frames,image=abrir,background='white',fg='white',command=lambda: resultados()).grid(row=7,column=1, pady= 000)
        # Button(frames,image=guardar,background='white',fg='white',command=lambda: resultados()).grid(row=7,column=0,sticky=E,padx=2)
    
    
        self.pireE.configure(state=NORMAL)
        self.pireE.delete(0, END)
        self.pireE.insert(0,"{:.1f}".format(self.pire))
        self.pireE.configure(state=DISABLED)
        self.friisE.configure(state=NORMAL)
        self.friisE.delete(0, END)
        self.friisE.insert(0,"{:.1f}".format(self.friis))
        self.friisE.configure(state=DISABLED)
        self.fcE.configure(state=NORMAL)
        self.fcE.delete(0, END)
        self.fcE.insert(0,"{:.1f}".format(self.fc))
        self.fcE.configure(state=DISABLED)
        self.ptxE.configure(state=NORMAL)
        self.ptxE.delete(0, END)
        self.ptxE.insert(0,"{:.1f}".format(self.ptx))
        self.ptxE.configure(state=DISABLED)
        self.gsE.configure(state=NORMAL)
        self.gsE.delete(0, END)
        self.gsE.insert(0,"{:.1f}".format(self.gs))
        self.gsE.configure(state=DISABLED)
        

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
    cn.configure(state=NORMAL)
    cn.delete(0, END)
    perdidas.configure(state=NORMAL)
    perdidas.delete(0, END)
    comborx.configure(state=NORMAL)
    comborx.delete(0, END)
    combotx.configure(state=NORMAL)
    combotx.delete(0, END)
    
    

def resultados():
    resultados= Resultado(2.55,5.26,2.5,16.5,52)
    resultados.ventana()

def path():
    loss= PathLoss()
    loss.ventana()

def oku():
    okumura= SelecOkamura()
    okumura.ventana()
def cos():
    cost= Cost231()
    cost.ventana()





if __name__ == "__main__":
    conversor= Conversor()
    conversor.ventana()

v.mainloop()