
import numpy as np
import calculos

class Presupuesto:
    def __init__(self):
        self.k=1.380*10**-23
        self.tk=290
        
    #Perdidas en trayectoria por espacio libre (adimensional)
    def lfsW(self,f,D):
        return ((4*np.pi*D)/self.wavLegh)**2
    #Perdidas en trayectoria por espacio libre (Frecuencia en Ghz y distancia en Km)
    def lfs(self,f,D):
        return 92.4 +20*np.log10(f)+20*np.log10(D)
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
    #Potencia de ruido
    def potenciaRuido(self,B):
        return '{:.2f}'.format( 10*np.log10(self.k*self.tk*B))
    #Calculo del Friis
    def friis(self):
        return self.Ptx+self.Gitx+self.Girx-self.lfs

    #Calculo de potencia de radio
    def gananciaSistema(self,Rtx,cmin):
        return Rtx - cmin
    def rtxs(self,Fm,Lp,Lf,Lb,At,Ar):
        return Fm+Lp+Lf+Lb-At-Ar
    def rtx(self,cmin):
        return self.gananciaSistema + cmin
    #Calculod el PIRE
    def PIRE(self,Rtx,pc,Gtx):
        return Rtx-pc+Gtx
    def cmin(self,gananciaSistema):
        self.ptx-gananciaSistema
    #Pérdida por ramificación
    def lf(self):
        if self.f== 1.8:
            self.lf= 5.4
            self.lbs= 2
        elif self.f==7.4:
            self.lf= 4.7
            self.lbs=2
        elif self.f ==  8.0:
            pass
        
    #Altura de la antena
    def rn(self,d1,d2,f):
        return '{:.2f}'.format(np.sqrt((calculos.wavLegh(f)*d1*d2)/(d1+d2)))
    #Zona uno de fresnel 
    def zonaUno(self,f,D):
        return 17.32*np.sqrt(D/(4*f))
    #Horizonte de radio
    
    
if __name__ == "__main__":
    #lost = Presupuesto(1.8,40)
    #d = lost.desvanecimiento("Agua o terreno liso","Areas calientes o humedas")
    #print(d, "dB")
    altura = Presupuesto()
    print(altura.potenciaRuido(10*10**6))
    print(altura.rn(9751,9751,915*10**6))