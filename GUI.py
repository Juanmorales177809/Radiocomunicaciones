from ast import Try
from pickle import READONLY_BUFFER
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from turtle import st
from matplotlib.pyplot import text
import Util
from modelos import ModeloPerdidas,Path,Okumura,Cost
import convertir




v = Tk()
#v.geometry('500x500')
v.config(background='white')
v.iconbitmap("./assets/antena.ico")
v.title("Calculo de Radio Enlace Terrestre")
v.configure(bg='beige')

note = ttk.Notebook(v)
note.pack(pady=10, expand=True)
note.grid(row=0,column=0)
webLabel = ttk.Label(note,text="Hello")
frame1 = Frame(note,width=500,height=500,bg='#d7f3bc')
frame2 = Frame(note,width=500,height=500, bg='#B0F9FE')
frame1.pack(fill='both',expand=True)
frame2.pack(fill='both',expand=True)
frame3 = Frame(note,width=500,height=500,bg='#D9B5FE')
frame3.pack(fill='both',expand=True)
imageForum= tk.PhotoImage(file="./assets/antenna.png")
imageForum1= tk.PhotoImage(file="./assets/convertir.png")
imageForum2= tk.PhotoImage(file="./assets/maps.png")
imageForum3= tk.PhotoImage(file="./assets/Guardar.png")
#note.add(frame2,text='Radioenlace',image=imageForum,compound=tk.RIGHT,padding=20)
note.add(frame1,image=imageForum,state=NORMAL)
note.add(frame2,image=imageForum1)
note.add(frame3,image=imageForum2)




#Modelo de perdidas
#Label(frame1, text="Modelo de Perdidas", font=(16),background='#B0F9FE')
Label(frame1,text= "Elija el modelo de perdidas",bg="#d7f3bc", font=(14)).place(x=150, y=150)
modelo= ttk.Combobox(frame1,width=30,values=["Path Loss", "Okumura-Hata", "Cost 231","Longley-Rice"])
modelo.place(x=150, y=200)
Button(frame1,text="ACEPTAR",background='#2A4014',width=20,fg='white',
        command=lambda: buton()).place(x=175,y=250)

def buton():
    if modelo.get()== "Path Loss":
        path()
    elif modelo.get()==  "Okumura-Hata":
        oku()
    elif modelo.get()=="Cost 231":
        cos()

#radioenlace
Label(frame2, text="Radio Enlace", font=(16),background='#d7f3bc').grid(row=0,column=0,sticky=W)
#Distancia
Label(frame2,text="Distancia :",font=(10),background='#d7f3bc').grid(row=1,column=0,sticky=E)
entD= Entry(frame2,width=10,borderwidth=3)
entD.grid(row=1,column=1)
combo= ttk.Combobox(frame2,values=["m","Km","Milles"],width=7)
combo.grid(row=1,column=2,padx=5,pady=5,sticky=W)

#Frecuencia
Label(frame2, text="Frecuencia :",font=(10),background='#d7f3bc').grid(row=2,column=0,sticky=E)
entF = Entry(frame2,width=10,borderwidth=3)
entF.grid(row=2,column=1)
combo1= ttk.Combobox(frame2,values=["Hz","Mhz","Khz","Ghz"],width=7)
combo1.grid(row=2, column=2,padx=5,pady=5,sticky=W)

#Factor de rugosidad
Label(frame2, text="Factor de rugosidad de terreno :",font=(10),background='#d7f3bc').grid(row=3,column=0,sticky=E)
comboFr= ttk.Combobox(frame2,values=["Agua o terreno liso","Sembrados densos, arenales","Bosques","Terreno normal","Aspero, motañoso"],width=25)
comboFr.grid(row=3, column=1,padx=5,pady=5,columnspan=2)

#Factor de Analisis climatico
Label(frame2, text="Factor de Analisis climatico :",font=(10),background='#d7f3bc').grid(row=4,column=0,sticky=E)
comboFC= ttk.Combobox(frame2,values=["Area marina","Area caliente o humeda","Area Mediterranea","Clima seco y fresco"],width=25)
comboFC.grid(row=4, column=1,padx=5,pady=5,columnspan=2)

#Confiabilidad del sistema
Label(frame2, text="Fiabilidad requerida :",font=(10),background='#d7f3bc').grid(row=5,column=0,sticky=E)
entR = Entry(frame2,width=10,borderwidth=3)
entR.grid(row=5,column=1)
Label(frame2, text="%",font=(10),background='#d7f3bc').grid(row=5,column=2,pady=5,sticky=W)

#Ganancia antena transmisora
Label(frame2, text="Ganancia de la antena Tx :",font=(10),background='#d7f3bc').grid(row=6,column=0,sticky=E)
entGtx = Entry(frame2,width=10,borderwidth=3)
entGtx.grid(row=6,column=1)
combo2= ttk.Combobox(frame2,values=["dBm","dBi"],width=7)
combo2.grid(row=6, column=2,padx=5,pady=5,sticky=W)

#Ganancia antena receptora
Label(frame2, text="Ganancia de la antena Rx :",font=(10),background='#d7f3bc').grid(row=7,column=0,sticky=E)
entGrx = Entry(frame2,width=10,borderwidth=3)
entGrx.grid(row=7,column=1)
combo3= ttk.Combobox(frame2,values=["dBb","dBi"],width=7)
combo3.grid(row=7, column=2,padx=5,pady=5,sticky=W)

#Perdidas por cable
Label(frame2, text="Perdidas por cable Lf :",font=(10),background='#d7f3bc').grid(row=8,column=0,sticky=E)
entLf = Entry(frame2,width=10,borderwidth=3)
entLf.grid(row=8,column=1,pady=5)
Label(frame2, text="dB",font=(10),background='#d7f3bc').grid(row=8,column=2,sticky=W)

#Perdidas por acople
Label(frame2, text="Perdidas por acople Lb :",font=(10),background='#d7f3bc').grid(row=9,column=0,sticky=E)
entLb = Entry(frame2,width=10,borderwidth=3)
entLb.grid(row=9,column=1,pady=5)
Label(frame2, text="dB",font=(10),background='#d7f3bc').grid(row=9,column=2,sticky=W)


#Sensibilidad receptora
Label(frame2, text="Sensibilidad Rx :",font=(10),background='#d7f3bc').grid(row=10,column=0,sticky=E)
entSe = Entry(frame2,width=10,borderwidth=3)
entSe.grid(row=10,column=1)
combo4= ttk.Combobox(frame2,values=["dBm","μV"],width=7,state=READONLY_BUFFER)
combo4.grid(row=10, column=2,padx=5,pady=5,sticky=W)

#Ancho de banda
Label(frame2, text="BW :",font=(10),background='#d7f3bc').grid(row=11,column=0,sticky=E)
entBw = Entry(frame2,width=10,borderwidth=3)
entBw.grid(row=11,column=1,pady=5)
Label(frame2, text="Mhz",font=(10),background='#d7f3bc').grid(row=11,column=2,sticky=W)

#Relación señal a ruido
Label(frame2, text="C/N :",font=(10),background='#d7f3bc').grid(row=12,column=0,sticky=E)
entCN = Entry(frame2,width=10,borderwidth=3)
entCN.grid(row=12,column=1,pady=5)
Label(frame2, text="dBm",font=(10),background='#d7f3bc').grid(row=12,column=2,sticky=W)

#Modelo de perdidas

class SelecOkamura:
    
    def ventana(self):
        self.ciudad=False
        ventana = Tk()
        ventana.geometry("350x300")
        ventana.resizable(0,0)
        ventana.config(bg='#d7f3bc')
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Okumura-Hata")
        self.radioValor=IntVar()
        Label(ventana,text="Distancia ",background='#d7f3bc').grid(row=0,column=0)
        self.entCo= Entry(ventana,width=17,borderwidth=3)
        self.entCo.grid(row=0,column=1,pady=5)
        self.combo= ttk.Combobox(ventana, values=["m","Km","Milles"],width=7)
        self.combo.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        Label(ventana,text="frecuencia ",background='#d7f3bc').grid(row=1,column=0)
        self.entCo1= Entry(ventana,width=17,borderwidth=3)
        self.entCo1.grid(row=1,column=1,pady=5)
        self.combo1= ttk.Combobox(ventana, values=["KHz","MHz","GHz"],width=7)
        self.combo1.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        Label(ventana,text="Altura efectiva antena Tx",background='#d7f3bc').grid(row=2,column=0)
        self.entPe= Entry(ventana,width=17,borderwidth=3)
        self.entPe.grid(row=2,column=1,pady=5)
        Label(ventana,text='m',background='#d7f3bc').grid(row=2, column=2,sticky=W)
        Label(ventana,text="Altura efectiva antena Rx",background='#d7f3bc').grid(row=3,column=0)
        self.entPe1= Entry(ventana,width=17,borderwidth=3)
        self.entPe1.grid(row=3,column=1,pady=5)
        Label(ventana,text='m',background='#d7f3bc').grid(row=3, column=2,sticky=W)
        radioPe= Radiobutton(ventana,text="Ciudad Grande",variable=self.radioValor,value=0,background='#d7f3bc')
        radioPe.grid(row=4,column=1,sticky=W)
        radioPe1= Radiobutton(ventana,text="Ciudad pequeña",variable=self.radioValor,value=1,background='#d7f3bc')
        radioPe1.grid(row=5,column=1,sticky=W)
        Label(ventana,textvariable=self.radioValor).grid(row=5,column=2)
        self.checkValue= BooleanVar()
        self.checkValue.set(True)
        check= Checkbutton(ventana,text="Zona Suburbana",var=self.checkValue,background='#d7f3bc')
        check.grid(row=6,column=1)
        buto= Button(ventana,text="CALCULAR",background='#2A4014',width=30,fg='white',
                    command=lambda: self.calcular())
        buto.grid(row=7,column=0,columnspan=2)
        Label(ventana,text="Lp ",background='#d7f3bc').grid(row=8, column=0)
        self.result= Entry(ventana,borderwidth=3)
        self.result.grid(row=8, column=1,pady=5,padx=5)
        Label(ventana,text="dB ",background='#d7f3bc').grid(row=8, column=2,sticky=W)
        def radio():
            if self.radioValor==0:
                self.ciudad=False
            elif self.radioValor==1
        self.sub = False

    
    
    
    def calcular(self):
        # try: 
        if self.combo.get()=='m':
            d= float(self.entCo.get())
            d= convertir.meToKm(d)
        elif self.combo.get()=='Milles':
            d= float(self.entCo.get())
            d= convertir.millasToKm(d)
        else:
            d= float(self.entCo.get())
        if self.entCo1.get()== 'MHz':
            f= float(self.entCo1.get())
            f= convertir.MhztoHz(f)
        elif self.entCo1.get()== 'KHz':
            f= float(self.entCo1.get())
            f= convertir.KhztoHz(f)
        elif self.entCo1.get()== 'GHz':
            f= float(self.entCo1.get())
            f= convertir.GhztoHz()
        else:
            f= float(self.entCo1.get())
            #messagebox.showwarning("Alerta", "Datos no validos")
    


        hte= float(self.entPe.get())
        hre= float(self.entPe1.get())
        modelo= Okumura(f,d,hte,hre,self.ciudad,self.sub)
        if self.checkValue:
            lp = modelo.calcular()
        else:
            lp= modelo.calcularLb()
        
        print(self.ciudad)
        self.result.configure(state=NORMAL)
        self.result.delete(0, END)
        self.result.insert(0,"{:.3f}".format(lp))
        self.result.configure(state=DISABLED)
        # except:
        #     messagebox.showwarning( "Warning","Datos no validos")
class SeleCost(Okumura):
    
    def ventana(self):
        ventana = Tk()
        ventana.geometry("300x200")
        ventana.resizable(0,0)
        ventana.config(bg='#d7f3bc')
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("COST 231")
        radioValCo= IntVar()
        Label(ventana,text="Altura efectiva antena Tx",background='#d7f3bc').grid(row=0,column=0)
        entCo= Entry(ventana,width=17,borderwidth=3)
        entCo.grid(row=0,column=1,pady=5)
        Label(ventana,text='m',background='#d7f3bc').grid(row=0, column=2,sticky=W)
        Label(ventana,text="Altura efectiva antena Rx",background='#d7f3bc').grid(row=1,column=0)
        entCo1= Entry(ventana,width=17,borderwidth=3)
        entCo1.grid(row=1,column=1,pady=5)
        Label(ventana,text='m',background='#d7f3bc').grid(row=1, column=2,sticky=W)
        Label(ventana,text="Factor de Corrección",background='#d7f3bc').grid(row=2,column=0)
        radioCo= Radiobutton(ventana,text="Ciudad densa",variable=radioValCo,value=0,background='#d7f3bc')
        radioCo.grid(row=2, column=1,sticky=W)
        radioCo1= Radiobutton(ventana,text="Ciudad",variable=radioValCo,value=-5,background='#d7f3bc')
        radioCo1.grid(row=3, column=1,sticky=W)
        radioCo2= Radiobutton(ventana,text="Barrios campestres",variable=radioValCo,value=-10,background='#d7f3bc')
        radioCo2.grid(row=4, column=1,sticky=W)
        radioCo3= Radiobutton(ventana,text="Rural",variable=radioValCo,value=-17,background='#d7f3bc')
        radioCo3.grid(row=5, column=1,sticky=W)
        Button(ventana,text="ACEPTAR",background='#2A4014',width=30,fg='white',
            command=lambda: self.guardar(ventana,entCo.get(),entCo1.get(),radioValCo)).grid(row=6,column=0,columnspan=2)

class PathLoss:
    def resultados(self):
        ventana = Tk()
        ventana.geometry("250x150")
        ventana.resizable(0,0)
        ventana.config(bg='#d7f3bc')
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Path Loss")
        radioValCo= IntVar()
        Label(ventana,text="Distancia ",background='#d7f3bc').grid(row=0,column=0)
        self.entCo= Entry(ventana,width=17,borderwidth=3)
        self.entCo.grid(row=0,column=1,pady=5)
        self.combo= ttk.Combobox(ventana, values=["m","Km","Milles"],width=7)
        self.combo.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        Label(ventana,text="frecuencia ",background='#d7f3bc').grid(row=1,column=0)
        self.entCo1= Entry(ventana,width=17,borderwidth=3)
        self.entCo1.grid(row=1,column=1,pady=5)
        self.combo1= ttk.Combobox(ventana, values=["KHz","MHz","GHz"],width=7)
        self.combo1.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        Button(ventana,text="Calcular",background='#2A4014',width=20,fg='white',
            command=lambda: self.calcular()).grid(row=3,column=0,columnspan=3)
        Label(ventana,text="Lfs ").grid(row=4, column=0)
        self.result= Entry(ventana,borderwidth=3)
        self.result.grid(row=4, column=1,columnspan=3,pady=5,padx=5)
    def calcular(self):
        if self.combo.get()=='m':
            d= float(self.entCo.get())
            d= convertir.meToKm(d)
        elif self.combo.get()=='Milles':
            d= float(self.entCo.get())
            d= convertir.millasToKm(d)
        else:
            d= float(self.entCo.get())
        if self.entCo1.get()== 'MHz':
            f= float(self.entCo1.get())
            f= convertir.megGig(f)
        elif self.entCo1.get()== 'KHz':
            f= float(self.entCo1.get())
            f= convertir.khzToGhz(f)
        else:
            f= float(self.entCo1.get())
        modelo= Path(d,f)
        lfs= modelo.calcular()
        self.result.configure(state=NORMAL)
        self.result.delete(0, END)
        self.result.insert(0,"{:.3f}".format(lfs))
        self.result.configure(state=DISABLED)
        
        


def path():
    loss= PathLoss()
    loss.resultados()

def oku():
    okumura= SelecOkamura()
    okumura.ventana()
def cos():
    cost= SeleCost()
    cost.ventana()
def results():
    presupuesto= PathLoss(
        entD.get(),entF.get(),
        comboFr.get(),comboFC.get(),entR.get(),entGtx.get(),
        entGrx.get(),entLf.get(),entLb.get(),entSe.get(),
        entBw.get(),entCN.get())
     
#Button(frame2,image= imageForum3, command=lambda: ventana.destroy()).grid(row=18,column=0)
radioValue= IntVar()
Label(frame2, text="Modelo de perdidas ",font=(10),background='#d7f3bc').grid(row=13,column=0,sticky=E)
radio1= Radiobutton(frame2,text="Path Loss", variable=radioValue,value=0,background='#d7f3bc')
radio1.grid(row=13,column=1,sticky=W)
radio2= Radiobutton(frame2,text="Okumura-Hata", variable=radioValue,value=1,background='#d7f3bc',command=lambda: oku())
radio2.grid(row=14,column=1,sticky=W)
radio3= Radiobutton(frame2,text="Cost 321", variable=radioValue,value=2,background='#d7f3bc',command=lambda: cos())
radio3.grid(row=15,column=1,sticky=W)


#Perdidas por espacio libre
Label(frame2, text="Lp :",font=(10),background='#d7f3bc').grid(row=16,column=0,sticky=E)
ent8 = Entry(frame2,width=10,borderwidth=3,state=DISABLED)
ent8.grid(row=16,column=1,pady=5)
Label(frame2, text="dB",font=(10),background='#d7f3bc').grid(row=16,column=2,sticky=W)

def calcular():
    pass
# def resultados():
#     result = Result()
#     result.resultados()
# #Calcular
Button(frame2,text="CALCULAR",background='#2A4014',width=30,fg='white',command=lambda: resultados()).grid(row=17,column=1,columnspan=2)




v.mainloop()