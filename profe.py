
import tkinter as tk
from tkinter import ttk, messagebox
    
   
class GUI(ttk.Frame):
       
    def __init__(self, main_GUI):
        super().__init__(main_GUI)
        main_GUI.title("Instituto Tecnológico Metropolitano ITM")
        main_GUI.configure(width=600, height=200)
        self.place(relwidth=1, relheight=1)
        self.entry_ = ttk.Entry(self)
        self.entry_.insert(tk.END
        self.entry_.place(x=20, y=30)
        self.combo = ttk.Combobox(self)\n",
        self.combo.place(x=20, y=50)\n",
        self.combo(values = ["Path Loos","Okumura-Hata","Cost 231","Longley-Rice"]
        self.combo.bind(\"<<ComboboxSelected>>\", self.selection_1)
    "     
    "# ----------------------------------------------------------------------------------------------  \n",
    "#                                   Botones\n",
    "# ----------------------------------------------------------------------------------------------\n",
    "        self.button_1 = ttk.Button(self, text=\"Ptx en dBm\",command = self.button_1)\n",
    "        self.button_1.place(x=260, y=40, width=100, height=30)\n",
    "        \n",
    "# ----------------------------------------------------------------------------------------------\n",
    "#                                 Ingreso de datos\n",
    "# ----------------------------------------------------------------------------------------------\n",
    "        \n",
    "        self.entry = ttk.Entry(self)\n",
    "        self.entry.place(x=370, y=40, width=100, height=30)\n",
    " \n",
    "#         messagebox.showinfo(\"Error\")\n",
    "\n",
    "        \n",
    "    def button_1(self):\n",
    "        print(\"Potencia en dBm:\", eval(self.entry.get()))\n",
    "    \n",
    "    def selection_1(self, event):\n",
    "        print(\"Modelo seleccionado:\", self.combo.get())\n",
    "    \n",
    "        \n",
    "Ngui = tk.Tk()\n",
    "app = GUI(Ngui)\n",
    "app.mainloop()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Insertar imagenes y gráficos "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "\n",
    "class Aplicacion:\n",
    "    def __init__(self):\n",
    "        self.ventana1=tk.Tk()\n",
    "        self.canvas1=tk.Canvas(self.ventana1, width=400, height=400, background=\"black\")\n",
    "        self.canvas1.grid(column=0, row=0)\n",
    "        archi1=tk.PhotoImage(file=\"ITM.png\")\n",
    "        self.canvas1.create_image(30, 100, image=archi1, anchor=\"nw\")\n",
    "        self.ventana1.mainloop()\n",
    "        \n",
    "aplicacion1=Aplicacion()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from pandas import DataFrame\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg\n",
    "\n",
    "data1 = {'Country': ['US','CA','GER','UK','FR'],\n",
    "         'GDP_Per_Capita': [45000,42000,52000,49000,47000]\n",
    "        }\n",
    "df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])\n",
    "\n",
    "\n",
    "data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],\n",
    "         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]\n",
    "        }\n",
    "df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])\n",
    "\n",
    "\n",
    "data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],\n",
    "         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]\n",
    "        }  \n",
    "df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])\n",
    " \n",
    "\n",
    "root= tk.Tk() \n",
    "  \n",
    "figure1 = plt.Figure(figsize=(6,5), dpi=100)\n",
    "ax1 = figure1.add_subplot(111)\n",
    "bar1 = FigureCanvasTkAgg(figure1, root)\n",
    "bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)\n",
    "df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()\n",
    "df1.plot(kind='bar', legend=True, ax=ax1)\n",
    "ax1.set_title('Country Vs. GDP Per Capita')\n",
    "\n",
    "figure2 = plt.Figure(figsize=(5,4), dpi=100)\n",
    "ax2 = figure2.add_subplot(111)\n",
    "line2 = FigureCanvasTkAgg(figure2, root)\n",
    "line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)\n",
    "df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()\n",
    "df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)\n",
    "ax2.set_title('Year Vs. Unemployment Rate')\n",
    "\n",
    "figure3 = plt.Figure(figsize=(5,4), dpi=100)\n",
    "ax3 = figure3.add_subplot(111)\n",
    "ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')\n",
    "scatter3 = FigureCanvasTkAgg(figure3, root) \n",
    "scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)\n",
    "ax3.legend(['Stock_Index_Price']) \n",
    "ax3.set_xlabel('Interest Rate')\n",
    "ax3.set_title('Interest Rate Vs. Stock Index Price')\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import * \n",
    "from matplotlib.figure import Figure\n",
    "from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)\n",
    "  \n",
    "# plot function is created for \n",
    "# plotting the graph in \n",
    "# tkinter window\n",
    "def plot():\n",
    "  \n",
    "    # the figure that will contain the plot\n",
    "    fig = Figure(figsize = (5, 5),\n",
    "                 dpi = 100)\n",
    "  \n",
    "    # list of squares\n",
    "    y = [i**2 for i in range(101)]\n",
    "  \n",
    "    # adding the subplot\n",
    "    plot1 = fig.add_subplot(111)\n",
    "  \n",
    "    # plotting the graph\n",
    "    plot1.plot(y)\n",
    "  \n",
    "    # creating the Tkinter canvas\n",
    "    # containing the Matplotlib figure\n",
    "    canvas = FigureCanvasTkAgg(fig,\n",
    "                               master = window)  \n",
    "    canvas.draw()\n",
    "  \n",
    "    # placing the canvas on the Tkinter window\n",
    "    canvas.get_tk_widget().pack()\n",
    "  \n",
    "    # creating the Matplotlib toolbar\n",
    "    toolbar = NavigationToolbar2Tk(canvas,\n",
    "                                   window)\n",
    "    toolbar.update()\n",
    "  \n",
    "    # placing the toolbar on the Tkinter window\n",
    "    canvas.get_tk_widget().pack()\n",
    "  \n",
    "# the main Tkinter window\n",
    "window = Tk()\n",
    "  \n",
    "# setting the title \n",
    "window.title('Plotting in Tkinter')\n",
    "  \n",
    "# dimensions of the main window\n",
    "window.geometry(\"500x500\")\n",
    "  \n",
    "# button that displays the plot\n",
    "plot_button = Button(master = window, \n",
    "                     command = plot,\n",
    "                     height = 2, \n",
    "                     width = 10,\n",
    "                     text = \"Plot\")\n",
    "  \n",
    "# place the button \n",
    "# in main window\n",
    "plot_button.pack()\n",
    "\n",
    "# run the gui\n",
    "window.mainloop()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Google Maps Services\n",
    "\n",
    "https://github.com/googlemaps/google-maps-services-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install -U googlemaps\n",
    "# !pip install --upgrade pip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import googlemaps\n",
    "from datetime import datetime\n",
    "\n",
    "gmaps = googlemaps.Client(key='Add Your Key here')\n",
    "\n",
    "# Geocoding an address\n",
    "geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')\n",
    "\n",
    "# Look up an address with reverse geocoding\n",
    "reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
