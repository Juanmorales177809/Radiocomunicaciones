from pickle import READONLY_BUFFER
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from turtle import st
import Util




v = Tk()
v.geometry('500x500')
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

