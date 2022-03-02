from cProfile import label
from calendar import c
from msilib.schema import ComboBox
from tkinter import *
from tkinter import font
from turtle import back, color
from matplotlib.colorbar import Colorbar
from tkinter import messagebox
from matplotlib.pyplot import colorbar, text
from pyparsing import col
import convertir
from tkinter import ttk
import calculos
from presupuesto import Presupuesto


v = Tk()
v.iconbitmap("./assets/antena.ico")
v.title("Radiocomunicaciones by Carlos")
v.minsize(700,600)
v.configure(background='white')
canvas = Canvas(width=600, height=100, bg='white',borderwidth=5)
canvas.pack(expand=NO, fill=BOTH)



mainloop()