from math import dist
from numpy import log10
from tkinter import messagebox
from tkinter import *

class ModeloPerdidas:
    def __init__(self,frecuencia,distancia):
        self.frecuencia= frecuencia
        self.distancia= distancia

class Path(ModeloPerdidas):

    def calcular(self):
        lfs= 92.44+20*log10(self.frecuencia)+20*log10(self.distancia)
        return lfs
    

class Okumura():
    def __init__(self,frecuencia,distancia,hte,hre):
        self.frecuencia= frecuencia
        self.distancia= distancia
        self.hte= hte
        self.hre= hre
    
    def calcularA(self,ciudad):
        if self.hte>=30 and self.hte<200 and self.hre >= 1 and self.hre <= 10:
            if ciudad ==0:
                if self.frecuencia <= 200*10**6:
                    return 8.29*(log10(1.54*self.hre))**2-1.1
                else:
                    return 3.2*log10(11.75*self.hre)**2-4.97
            else:
                return (1.1*log10(self.frecuencia-0.7))*self.hre-(1.56*log10(self.frecuencia-0.8))
        else:
            messagebox.showerror("Error","Este modelo de perdidas solo permite una altura en la transmisora entre 30 y 200 metros y de la receptora entre 1 y 10 metros")
    def calcular(self,ciudad,urbano):
        lp= 69.55+26.16*log10(self.frecuencia)-13.82*log10(self.hte)-self.calcularA(ciudad)
        +(44.9-6.55*log10(self.hte))*log10(self.distancia)
        if urbano:
            return lp-2*(log10(self.frecuencia/28))**2-5.4
        else:
            return lp
        
class Cost(Okumura):

    def __init__(self,frecuencia,distancia,hte=1,hre=1,ciudadGrande=True,subUrbano=True):
        self.frecuencia= frecuencia
        self.distancia= distancia
        self.hte= hte
        self.hre= hre
    def calcular(self,c,ciudad):
        if self.frecuencia >= 1.5*10**9 and self.frecuencia <= 2*10**9:
            correction = {"Ciudad densa": 0, "Ciudad":-5,"Barrios campestres": -10, "Rural":-17}
            lp= 46.3+33.9*log10(self.frecuencia)-13.82*log10(self.hte)
            -self.calcularA(ciudad)*self.hre+(44.9-6.55*log10(self.hte))*log10(self.distancia)+correction[c]
            return lp
        else:
            messagebox.showerror("Ërror", "solo admite frecuencias entre 1.5Ghz y 2Ghz") 

if __name__ == "__main__":
    modelo= Okumura(2.4*10**9,24000,4,4)
    print(modelo.calcular(0,True))
    # model1 = Okumura(2.4*10**9,10,4,4)
    # print(model1.calcularLb())
    
    


    
                






