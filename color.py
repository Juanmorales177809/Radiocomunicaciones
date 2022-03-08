from tkinter import ttk
from tkinter import *
import Util


v = Tk()
v.geometry('500x500')
v.config(background='white')
v.iconbitmap("./assets/antena.ico")
v.title("Calculo de Radio Enlace Terrestre")
v.configure(bg='beige')

notes=Util.agregarNotePad(v,0,0)


frame1 = Frame(notes,width=500,height=500,bg='#d7f3bc')
# frame2 = Frame(notes,width=500,height=500, bg='#B0F9FE')
frame1.pack(fill='both',expand=True)
# frame2.pack(fill='both',expand=True)
# frame3 = Frame(notes,width=500,height=500,bg='#D9B5FE')
# frame3.pack(fill='both',expand=True)
Util.agregarPestana(notes,frame1,"./assets/antenna.png")
# Util.agregarPestana(notes,frame2,"./assets/convertir.png")
# Util.agregarPestana(notes,frame3,"./assets/maps.png")



v.mainloop()