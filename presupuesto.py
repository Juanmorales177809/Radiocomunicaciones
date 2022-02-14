
import numpy as np

class Presupuesto:
    def __init__(self,f,D):
        self.c = 3*10**8
        self.f = f
        self.wavLegh = self.f/self.c
        self.D = D
        self.A = 0
        self.B = 0
        self.R = 0.9999
        
    #Perdidas en trayectoria por espacio libre (adimensional)
    def lfsW(self,D):
        return ((4*np.pi*D)/self.wavLegh)**2
    #Perdidas en trayectoria por espacio libre (Frecuencia en Ghz y distancia en Km)
    def lfs(self,D):
        return 92.4 +20*np.log10(self.f)+20*np.log10(D)
    #Perdidas en trayectoria por espacio libre (Frecuencia en Mhz y distancia en Km)
    def lostFreemeg(self):
        return 32.4+20*np.log10(self.f)+20*np.log10(self.D)
    
    def factorRugo(self,val):
        if val == "Agua o terreno liso":
            self.A = 4
        elif val == "Terreno Promedio":
            self.A = 1
        elif val == "Aspero y montanoso":
            self.A = 0.25
    def factorProba(self,prob):
        if prob == "Anual a mensual":
            self.B = 1
        elif prob == "Areas calientes o humedas":
            self.B = 0.5
        elif prob ==  "Areas continentales promedio":
            self.B = 0.25
        elif prob == "Areas muy secas o montanosas":
            self.B = 0.125
    #Margen de desvanecimiento (decibeles)
    def desvanecimiento(self,val,prob):
        self.factorRugo(val)
        self.factorProba(prob)
        return 30*np.log10(self.D)+10*np.log10(6*self.A*self.B*self.f)-10*np.log10(1-self.R)-70
    #>Ecuación de Friss, solo recibe valores en decibeles
    def friss(self,ptx,gitx,girx,lfs):
        return ptx+gitx+girx-lfs
class Friis(Presupuesto):
    def __init__(self,Ptx,Gitx,Girx,Prx):
        self.Ptx = Ptx
        self.Gitx = Gitx
        self.Girx = Girx
        self.Prx = Prx
    def friis(self):
        return self.Ptx+self.Gitx+self.Girx-self.lfs

   
if __name__ == "__main__":
    lost = Presupuesto(1.8,40)
    d = lost.desvanecimiento("Agua o terreno liso","Areas calientes o humedas")
    print(d, "dB")
        