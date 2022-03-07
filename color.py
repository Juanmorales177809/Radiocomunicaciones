from tkinter import ttk
from tkinter import *


root = Tk()
root.geometry("600x200")

s = ttk.Style()
s.theme_use('clam')

s.configure(
    "custom.Horizontal.TProgressbar",
    troughcolor='#5A504E',
    background='#BF00FF',
    darkcolor="#390439",
    lightcolor="#ED28F0",
    bordercolor="black",
    )

bar = ttk.Progressbar(
    root,
    style="custom.Horizontal.TProgressbar",
    orient="horizontal",
    length=500,
    mode="determinate",
    maximum=4,
    value=1)

bar.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()