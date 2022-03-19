import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Panel de pestañas en Tcl/Tk")
        main_window.config(background='white')
        main_window.iconbitmap("./assets/antena.ico")
        main_window.title("Calculo de Radio Enlace Terrestre")
        main_window.configure(bg='beige')
        
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self)
        #Crear el contenido de cada una de las pestañas.
        
        self.frame1 = tk.Frame(self.notebook,width=500,height=500,bg='#B0F9FE')
        self.frame2 =tk.Frame(self.notebook,width=500,height=500, bg='#d7f3bc')
        self.frame1.pack(fill='both',expand=True)
        self.frame2.pack(fill='both',expand=True)
        self.frame3 = tk.Frame(self.notebook,width=500,height=500,bg='#D9B5FE')
        self.frame3.pack(fill='both',expand=True)
        self.imageForum1= tk.PhotoImage(file="./assets/antenna.png")
        self.imageForum= tk.PhotoImage(file="./assets/convertir.png")
        self.imageForum2= tk.PhotoImage(file="./assets/maps.png")
        
        self.notebook.add(self.frame1,image=self.imageForum)
        self.notebook.add(self.frame2,image=self.imageForum1)
        self.notebook.add(self.frame3,image=self.imageForum2)
        
        ttk.Label(self.frame1,text="Modelos de Perdidas",font=(14),background='#B0F9FE').pack()
        self.notebook.pack(padx=10, pady=10)
        self.pack()
    
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()