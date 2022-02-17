
import numpy as np

class Presupuesto:
    def __init__(self,f,D,ptx,gitx,girx,lfs,prx,cminrec):
        self.c = 3*10**8
        self.f = f
        self.wavLegh = self.f/self.c
        self.D = D
        self.A = 0
        self.B = 0
        self.R = 0
        self.Ptx = 0
        self.Gitx = 0
        self.Girx = 0
        self.Prx = 0
        self.fm = 0
        self.tm =365*24*60
        self.cminrec=cminrec
        
    #Perdidas en trayectoria por espacio libre (adimensional)
    def lfsW(self,D):
        return ((4*np.pi*D)/self.wavLegh)**2
    #Perdidas en trayectoria por espacio libre (Frecuencia en Ghz y distancia en Km)
    def lfs(self,D):
        return 92.4 +20*np.log10(self.f)+20*np.log10(D)
    #Perdidas en trayectoria por espacio libre (Frecuencia en Mhz y distancia en Km)
    def perdidasEspacioLibre(self):
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
    #Calculo de disponibilidad
        def r(self,tiempo):
            return (tiempo*100)/self.tm
            
    #Margen de desvanecimiento (decibeles)
    def desvanecimiento(self,val,prob):
        self.factorRugo(val)
        self.factorProba(prob)
        return 30*np.log10(self.D)+10*np.log10(6*self.A*self.B*self.f)-10*np.log10(1-self.R)-70
    #>Ecuación de Friss, solo recibe valores en decibeles
    
    #Calculo del Friis
    def friis(self):
        return self.Ptx+self.Gitx+self.Girx-self.lfs

    #Calculo de potencia de radio
    def gananciaSistema(self):
        pass
    def ptx(self):
        return self.gananciaSistema - cmin
    def PIRE(self):
        pass
    def cmin(self,gananciaSistema):
        self.ptx-gananciaSistema
    #Pérdida por ramificación
    def lf(self):
        pass
if __name__ == "__main__":
    lost = Presupuesto(1.8,40)
    d = lost.desvanecimiento("Agua o terreno liso","Areas calientes o humedas")
    print(d, "dB")
        