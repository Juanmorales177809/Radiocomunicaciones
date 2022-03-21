
from pickle import READONLY_BUFFER
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

from matplotlib.pyplot import text
from modelos import ModeloPerdidas,Path,Okumura,Cost
import convertir




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
# frame= Frame(note,width=500,height=500)
# frame.pack(fill='both',expand=True) 
# frame4= Frame(note,width=500,height=500)
# frame4.pack(fill='both',expand=True) 
# frame5= Frame(note,width=500,height=500)
# frame5.pack(fill='both',expand=True) 
imageForum= tk.PhotoImage(file="./assets/ante4.png")
imageForum1= tk.PhotoImage(file="./assets/convertir.png")
imageForum2= tk.PhotoImage(file="./assets/maps.png")
imageForum3= tk.PhotoImage(file="./assets/Guardar.png")
okupe= tk.PhotoImage(file="./assets/okupeque.png")
costpe= tk.PhotoImage(file="./assets/costpeque.png")

#note.add(frame2,text='Radioenlace',image=imageForum,compound=tk.RIGHT,padding=20)
note.add(frame1,image=imageForum,state=NORMAL)
# note.add(frame,image=imageForum,state=NORMAL)
# note.add(frame4,image=imageForum,state=NORMAL)
# note.add(frame5,image=imageForum,state=NORMAL)
note.add(frame3,image=imageForum2)
note.add(frame2,image=imageForum1)





#Modelo de perdidas
#Label(frame1, text="Modelo de Perdidas", font=(16),background='#B0F9FE')
# Label(frame1,text= "Elija el modelo de perdidas",bg="#d7f3bc", font=(14)).place(x=150, y=150)
# modelo= ttk.Combobox(frame1,width=30,values=["Path Loss", "Okumura-Hata", "Cost 231","Longley-Rice"])
# modelo.place(x=150, y=200)
# Button(frame1,text="ACEPTAR",background='#2A4014',width=20,fg='white',
#         command=lambda: buton()).place(x=175,y=250)

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

def lon():
    messagebox.showinfo("Mantenimiento", "Esta sección está en construcción")
def limpiar():
    frame1.destroy()
    


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
entR = Entry(frame2,width=10,borderwidth=3)
entR.grid(row=5,column=1)
Label(frame2, text="%",font=(10)).grid(row=5,column=2,pady=5,sticky=W)

#Ganancia antena transmisora
Label(frame2, text="Ganancia de la antena Tx :",font=(10)).grid(row=6,column=0,sticky=E)
entGtx = Entry(frame2,width=10,borderwidth=3)
entGtx.grid(row=6,column=1)
combo2= ttk.Combobox(frame2,values=["dBm","dBi"],width=7)
combo2.grid(row=6, column=2,padx=5,pady=5,sticky=W)

#Ganancia antena receptora
Label(frame2, text="Ganancia de la antena Rx :",font=(10)).grid(row=7,column=0,sticky=E)
entGrx = Entry(frame2,width=10,borderwidth=3)
entGrx.grid(row=7,column=1)
combo3= ttk.Combobox(frame2,values=["dBb","dBi"],width=7)
combo3.grid(row=7, column=2,padx=5,pady=5,sticky=W)

#Perdidas por cable
Label(frame2, text="Perdidas por cable Lf :",font=(10)).grid(row=8,column=0,sticky=E)
entLf = Entry(frame2,width=10,borderwidth=3)
entLf.grid(row=8,column=1,pady=5)
Label(frame2, text="dB",font=(10)).grid(row=8,column=2,sticky=W)

#Perdidas por acople
Label(frame2, text="Perdidas por acople Lb :",font=(10)).grid(row=9,column=0,sticky=E)
entLb = Entry(frame2,width=10,borderwidth=3)
entLb.grid(row=9,column=1,pady=5)
Label(frame2, text="dB",font=(10)).grid(row=9,column=2,sticky=W)


#Sensibilidad receptora
Label(frame2, text="Sensibilidad Rx :",font=(10)).grid(row=10,column=0,sticky=E)
entSe = Entry(frame2,width=10,borderwidth=3)
entSe.grid(row=10,column=1)
combo4= ttk.Combobox(frame2,values=["dBm","μV"],width=7,state=READONLY_BUFFER)
combo4.grid(row=10, column=2,padx=5,pady=5,sticky=W)

#Ancho de banda
Label(frame2, text="BW :",font=(10)).grid(row=11,column=0,sticky=E)
entBw = Entry(frame2,width=10,borderwidth=3)
entBw.grid(row=11,column=1,pady=5)
Label(frame2, text="Mhz",font=(10)).grid(row=11,column=2,sticky=W)

#Relación señal a ruido
Label(frame2, text="C/N :",font=(10)).grid(row=12,column=0,sticky=E)
entCN = Entry(frame2,width=10,borderwidth=3)
entCN.grid(row=12,column=1,pady=5)
Label(frame2, text="dBm",font=(10)).grid(row=12,column=2,sticky=W)

#Modelo de perdidas
     
#Button(frame2,image= imageForum3, command=lambda: ventana.destroy()).grid(row=18,column=0)
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
if radioValue.get==0:
    perdida= "Lfs"
else:
    perdida= "Lp"
Label(frame2, text="Lp :",font=(10)).grid(row=17,column=0,sticky=E)
perdidas = Entry(frame2,width=10,borderwidth=3,state=DISABLED)
perdidas.grid(row=17,column=1,pady=5)
Label(frame2, text="dB",font=(10)).grid(row=17,column=2,sticky=W)
Button(frame2,text=perdida,background='#336DBA',width=30,fg='white',command=lambda: resultados()).grid(row=17,column=0)
def resultados():
    print(radioValue)
class SelecOkamura:

    def __init__(self):
        self.ciudad=IntVar(value=0)
        self.sub= BooleanVar()

    
    def ventana(self):
        
        ventana = Tk()
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
                command=lambda: self.calcular()).grid(row=8,column=1,pady=30)
        Label(ventana,text="dB").grid(row=7, column=2,sticky=W)
        self.resultado= Entry(ventana,borderwidth=3,width=17)
        self.resultado.grid(row=7, column=1)
        mapas= Button(ventana,text= "Mapa" ,background='#336DBA',fg='white',width=15,command=lambda: lon())
        mapas.grid(row=9,column=0,padx=15,pady=15)
        
    
    def calcular(self):
        # try:
        d= float(self.distancia.get()) 
        f= float(self.frecuencia.get())
        if self.comboD.get()=='Milles':
            d= convertir.millasToKm(d)
            d= convertir.kmToM(d)
        elif self.comboD.get()=="Km":
            d= convertir.kmToM(d)
        if self.combof.get()== 'MHz':
            f= convertir.MhztoHz(f)
        elif self.combof.get()== 'KHz':
            f= convertir.KhztoHz(f)
        elif self.combof.get()== 'GHz':
            f= convertir.GhztoHz(f)
        if self.ciudad.get()== 0:
            print("Ciudad Grande")
        elif self.ciudad.get()== 1:
            print("Ciudad Pequeña")


        hte= float(self.hte.get())
        hre= float(self.hre.get())
        
        modelo= Okumura(f,d,hte,hre)
        lp= modelo.calcular(self.ciudad.get(),self.sub.get())
        print(self.ciudad.get(), self.sub.get())
        
        self.resultado.configure(state=NORMAL)
        self.resultado.delete(0, END)
        self.resultado.insert(0,"{:.3f}".format(lp))
        self.resultado.configure(state=DISABLED)
        # except:
        #     messagebox.showwarning( "Warning","Datos no validos")
class Cost231:
    
    def ventana(self):
        self.ciudad=False
        ventana = Tk()
        ventana.geometry("350x350")
        ventana.resizable(0,0)
        # ventana.config(bg='#d7f3bc')
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Cost-231")
        self.radioValor=IntVar()
        Label(ventana,text="Distancia ").grid(row=0,column=0)
        self.entCo= Entry(ventana,width=17,borderwidth=3)
        self.entCo.grid(row=0,column=1,pady=5)
        self.combo= ttk.Combobox(ventana, values=["m","Km","Milles"],width=7)
        self.combo.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        Label(ventana,text="frecuencia ").grid(row=1,column=0)
        self.entCo1= Entry(ventana,width=17,borderwidth=3)
        self.entCo1.grid(row=1,column=1,pady=5)
        self.combo1= ttk.Combobox(ventana, values=["KHz","MHz","GHz"],width=7)
        self.combo1.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        Label(ventana,text="Altura efectiva antena Tx").grid(row=2,column=0)
        self.entPe= Entry(ventana,width=17,borderwidth=3)
        self.entPe.grid(row=2,column=1,pady=5)
        Label(ventana,text='m').grid(row=2, column=2,sticky=W)
        Label(ventana,text="Altura efectiva antena Rx").grid(row=3,column=0)
        self.entPe1= Entry(ventana,width=17,borderwidth=3)
        self.entPe1.grid(row=3,column=1,pady=5)
        Label(ventana,text='m').grid(row=3, column=2,sticky=W)
        radioPe= Radiobutton(ventana,text="Ciudad Grande",variable=self.radioValor,value=0)
        radioPe.grid(row=4,column=1,sticky=W)
        radioPe1= Radiobutton(ventana,text="Ciudad pequeña",variable=self.radioValor,value=1)
        radioPe1.grid(row=5,column=1,sticky=W)
        Label(ventana,textvariable=self.radioValor).grid(row=5,column=2)
        self.checkValue= BooleanVar()
        self.checkValue.set(True)
        check= Checkbutton(ventana,text="Zona Suburbana",var=self.checkValue)
        check.grid(row=6,column=1,pady=10)
        Label(ventana,text="Factor de corrección").grid(row=7,column=0)
        factor= ttk.Combobox(ventana,values=["Ciudad densa","Ciudad","Barrios campestres","Rural"],width=15)
        factor.grid(row=7,column=1,pady=10)
        Button(ventana,text="Lp",background='#336DBA',width=15,fg='white',
                    command=lambda: self.calcular()).grid(row=8,column=0,padx=15)
        Button(ventana,text="Enviar",background='#336DBA',width=15,fg='white',
                command=lambda: self.calcular()).grid(row=9,column=1,pady=15)
        Label(ventana,text="dB").grid(row=8, column=2,sticky=W)
        self.result= Entry(ventana,borderwidth=3,width=17)
        self.result.grid(row=8, column=1,pady=5)
    
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
        
        modelo= Okumura(f,d,hte,hre)
        lp= modelo.calcular(self.radioValor.get(),self.checkValue.get())
        print(self.radioValor.get(), self.checkValue.get())
        
        self.result.configure(state=NORMAL)
        self.result.delete(0, END)
        self.result.insert(0,"{:.3f}".format(lp))
        self.result.configure(state=DISABLED)
        # except:
        #     messagebox.showwarning( "Warning","Datos no validos")   
        
    
class PathLoss:
    def ventana(self):
        ventana = Tk()
        ventana.geometry("350x200")
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
            command=lambda: self.enviar()).grid(row=5,column=1,columnspan=2,pady=30)
        Label(ventana,text="dB").grid(row=3, column=3,sticky=W)
        self.result= Entry(ventana,borderwidth=3,width=17)
        self.result.grid(row=3, column=1,columnspan=2,pady=5,padx=5)
    
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
        lfs= modelo.calcular()
        self.result.configure(state=NORMAL)
        self.result.delete(0, END)
        self.result.insert(0,"{:.3f}".format(lfs))
        self.result.configure(state=DISABLED)
        
    def enviar(self):
            lfs= float(self.result.get())
            d= float(self.distancia.get())
            f= float(self.frecuencia.get())
            uf= self.combof.get()
            ud= self.comboD.get()
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
        


def path():
    loss= PathLoss()
    loss.ventana()

def oku():
    okumura= SelecOkamura()
    okumura.ventana()
def cos():
    cost= Cost231()
    cost.ventana()
def results():
    presupuesto= PathLoss(
        entD.get(),entF.get(),
        comboFr.get(),comboFC.get(),entR.get(),entGtx.get(),
        entGrx.get(),entLf.get(),entLb.get(),entSe.get(),
        entBw.get(),entCN.get())

def calcular():
    pass
# def resultados():
#     result = Result()
#     result.resultados()
# #Calcular





v.mainloop()