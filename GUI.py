from pickle import READONLY_BUFFER
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from turtle import st
import Util




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
#note.add(frame1,text='Radioenlace',image=imageForum,compound=tk.RIGHT,padding=20)
note.add(frame1,image=imageForum,state=NORMAL)
note.add(frame2,image=imageForum1)
note.add(frame3,image=imageForum2)



#Conversor de unidades
Label(frame2, text="Conversor de Unidades", font=(16),background='#B0F9FE').grid(row=0,column=0)
Label(frame1, text="Radio Enlace", font=(16),background='#d7f3bc').grid(row=0,column=0,sticky=W)


#radioenlace
#Distancia
Label(frame1,text="Distancia :",font=(10),background='#d7f3bc').grid(row=1,column=0,sticky=E)
ent1= Entry(frame1,width=10,borderwidth=3)
ent1.grid(row=1,column=1)
combo= ttk.Combobox(frame1,values=["m","Km","Milles"],width=7)
combo.grid(row=1,column=2,padx=5,pady=5,sticky=W)

#Frecuencia
Label(frame1, text="Frecuencia :",font=(10),background='#d7f3bc').grid(row=2,column=0,sticky=E)
ent = Entry(frame1,width=10,borderwidth=3)
ent.grid(row=2,column=1)
combo1= ttk.Combobox(frame1,values=["Hz","Mhz","Khz","Ghz"],width=7)
combo1.grid(row=2, column=2,padx=5,pady=5,sticky=W)

#Factor de rugosidad
Label(frame1, text="Factor de rugosidad de terreno :",font=(10),background='#d7f3bc').grid(row=3,column=0,sticky=E)
combo2= ttk.Combobox(frame1,values=["Agua o terreno liso","Sembrados densos, arenales","Bosques","Terreno normal","Aspero, motañoso"],width=25)
combo2.grid(row=3, column=1,padx=5,pady=5,columnspan=2)

#Factor de Analisis climatico
Label(frame1, text="Factor de Analisis climatico :",font=(10),background='#d7f3bc').grid(row=4,column=0,sticky=E)
combo3= ttk.Combobox(frame1,values=["Area marina","Area caliente o humeda","Area Mediterranea","Clima seco y fresco"],width=25)
combo3.grid(row=4, column=1,padx=5,pady=5,columnspan=2)

#Confiabilidad del sistema
Label(frame1, text="Fiabilidad requerida :",font=(10),background='#d7f3bc').grid(row=5,column=0,sticky=E)
ent1 = Entry(frame1,width=10,borderwidth=3)
ent1.grid(row=5,column=1)
Label(frame1, text="%",font=(10),background='#d7f3bc').grid(row=5,column=2,pady=5,sticky=W)

#Ganancia antena transmisora
Label(frame1, text="Ganancia de la antena Tx :",font=(10),background='#d7f3bc').grid(row=6,column=0,sticky=E)
ent2 = Entry(frame1,width=10,borderwidth=3)
ent2.grid(row=6,column=1)
combo4= ttk.Combobox(frame1,values=["dBm","dBi"],width=7)
combo4.grid(row=6, column=2,padx=5,pady=5,sticky=W)

#Ganancia antena receptora
Label(frame1, text="Ganancia de la antena Rx :",font=(10),background='#d7f3bc').grid(row=7,column=0,sticky=E)
ent3 = Entry(frame1,width=10,borderwidth=3)
ent3.grid(row=7,column=1)
combo5= ttk.Combobox(frame1,values=["dBb","dBi"],width=7)
combo5.grid(row=7, column=2,padx=5,pady=5,sticky=W)

#Perdidas por cable
Label(frame1, text="Perdidas por cable Lf :",font=(10),background='#d7f3bc').grid(row=8,column=0,sticky=E)
ent4 = Entry(frame1,width=10,borderwidth=3)
ent4.grid(row=8,column=1,pady=5)
Label(frame1, text="dB",font=(10),background='#d7f3bc').grid(row=8,column=2,sticky=W)

#Perdidas por acople
Label(frame1, text="Perdidas por acople Lb :",font=(10),background='#d7f3bc').grid(row=9,column=0,sticky=E)
ent5 = Entry(frame1,width=10,borderwidth=3)
ent5.grid(row=9,column=1,pady=5)
Label(frame1, text="dB",font=(10),background='#d7f3bc').grid(row=9,column=2,sticky=W)


#Sensibilidad receptora
Label(frame1, text="Sensibilidad Rx :",font=(10),background='#d7f3bc').grid(row=10,column=0,sticky=E)
ent6 = Entry(frame1,width=10,borderwidth=3)
ent6.grid(row=10,column=1)
combo6= ttk.Combobox(frame1,values=["dBm","μV"],width=7,state=READONLY_BUFFER)
combo6.grid(row=10, column=2,padx=5,pady=5,sticky=W)

#Ancho de banda
Label(frame1, text="BW :",font=(10),background='#d7f3bc').grid(row=11,column=0,sticky=E)
ent7 = Entry(frame1,width=10,borderwidth=3)
ent7.grid(row=11,column=1,pady=5)
Label(frame1, text="Mhz",font=(10),background='#d7f3bc').grid(row=11,column=2,sticky=W)

#Relación señal a ruido
Label(frame1, text="C/N :",font=(10),background='#d7f3bc').grid(row=12,column=0,sticky=E)
ent7 = Entry(frame1,width=10,borderwidth=3)
ent7.grid(row=12,column=1,pady=5)
Label(frame1, text="dBm",font=(10),background='#d7f3bc').grid(row=12,column=2,sticky=W)

#Modelo de perdidas
class SelecOkamura:
    def __init__(self):
        self.heTx=0
        self.heRx=0
        self.ciudad=0
        self.sub=False
    
    def guardar(self,ventana,heRk,heTx,radio):
        self.heRx= float(heRk)
        self.heTx= float(heTx)
        self.ciudad= radio
        ventana.destroy()
    
    def sumar(self):
        return str(self.heRx+self.heTx)

    def selecOkumura(self):
        ventana = Tk()
        ventana.geometry("275x175")
        ventana.resizable(0,0)
        ventana.config(bg='#d7f3bc')
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Okumura-Hata")
        radioValor=IntVar()
        Label(ventana,text="Altura efectiva antena Tx",background='#d7f3bc').grid(row=0,column=0)
        entPe= Entry(ventana,width=17,borderwidth=3)
        entPe.grid(row=0,column=1,pady=5)
        Label(ventana,text='m',background='#d7f3bc').grid(row=0, column=2,sticky=W)
        Label(ventana,text="Altura efectiva antena Rx",background='#d7f3bc').grid(row=1,column=0)
        entPe1= Entry(ventana,width=17,borderwidth=3)
        entPe1.grid(row=1,column=1,pady=5)
        Label(ventana,text='m',background='#d7f3bc').grid(row=1, column=2,sticky=W)
        radioPe= Radiobutton(ventana,text="Ciudad pequeña",variable=radioValor,value=0,background='#d7f3bc')
        radioPe.grid(row=2,column=1,sticky=W)
        radioPe1= Radiobutton(ventana,text="Ciudad pequeña",variable=radioValor,value=1,background='#d7f3bc')
        radioPe1.grid(row=3,column=1,sticky=W)
        checkValue= BooleanVar()
        checkValue.set(True)
        check= Checkbutton(ventana,text="Zona Suburbana",var=checkValue,background='#d7f3bc')
        check.grid(row=4,column=1)
        Button(ventana,text="ACEPTAR",background='#2A4014',width=30,fg='white',command=lambda: self.guardar(ventana,entPe.get(),entPe1.get(),radioValor)).grid(row=5,column=0,columnspan=2)
        
class Cost(SelecOkamura):
    def __init__(self):
        self.correcion= 0

    def cost(self):
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
        
    

class Result(SelecOkamura):
    def __init__(self):
        pass
    
    def resultados(self):
        ventana = Tk()
        ventana.geometry("300x500")
        ventana.resizable(0,0)
        ventana.config(bg='#d7f3bc')
        ventana.iconbitmap("./assets/antena.ico")
        ventana.title("Resultados")
        #frames= Frame(ventana,background='white',width=300, height=50)
        #frames.pack()
        #Button(frames,image= "Guardar.png", command=lambda: ventana.destroy()).grid(row=0,column=0)
        Label(ventana,text=sumar(),font=(10)).grid(row=0, column=0)
        entResult= Entry(ventana,width=10,borderwidth=3)
        entResult.grid(row=0, column=1)
        


def oku():
    okumura= SelecOkamura()
    okumura.selecOkumura()
def cos():
    cost= Cost()
    cost.cost()
    
#Button(frame1,image= imageForum3, command=lambda: ventana.destroy()).grid(row=18,column=0)
radioValue= IntVar()
Label(frame1, text="Modelo de perdidas ",font=(10),background='#d7f3bc').grid(row=13,column=0,sticky=E)
radio1= Radiobutton(frame1,text="Path Loss", variable=radioValue,value=0,background='#d7f3bc')
radio1.grid(row=13,column=1,sticky=W)
radio2= Radiobutton(frame1,text="Okumura-Hata", variable=radioValue,value=1,background='#d7f3bc',command=lambda: oku())
radio2.grid(row=14,column=1,sticky=W)
radio3= Radiobutton(frame1,text="Cost 321", variable=radioValue,value=2,background='#d7f3bc',command=lambda: cos())
radio3.grid(row=15,column=1,sticky=W)


#Perdidas por espacio libre
Label(frame1, text="Lp :",font=(10),background='#d7f3bc').grid(row=16,column=0,sticky=E)
ent8 = Entry(frame1,width=10,borderwidth=3,state=DISABLED)
ent8.grid(row=16,column=1,pady=5)
Label(frame1, text="dB",font=(10),background='#d7f3bc').grid(row=16,column=2,sticky=W)

def calcular():
    pass
def resultados():
    result = Result()
    result.resultados()
#Calcular
Button(frame1,text="CALCULAR",background='#2A4014',width=30,fg='white',command=lambda: resultados()).grid(row=17,column=1,columnspan=2)




v.mainloop()