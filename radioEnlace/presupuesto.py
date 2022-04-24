
from math import log10, sqrt


class Presupuesto:
    def __init__(self,frecuencia,distancia,disponibilidad,factor,propabilidad,anchoBanda,cm,sn,lf,lb,gtx,grx,lfs,tk=290):
        self.k=1.380*10**-23 # Constante de Boltzman
        self.tk=tk #Temperatura en kelvin
        self.f= frecuencia #frecuencia en ghz
        self.distancia= distancia #Distancia en kilometros
        self.c= 3*10**8 #Velocidad de la luz
        self.disponibilidad=disponibilidad #Disponibilidad del sistema en porcentaje
        self.probabilidad= propabilidad # Factor de probabilidad
        self.factor= factor #Factor de rugosidad
        self.anchoBanda= anchoBanda #Ancho de banda del sistema
        self.cm= cm #Sensibilidad del sistema
        self.sn= sn #Relación señal a ruido
        self.lf= lf#Perdidas por el cable
        self.lb= lb #Perdidas por acople
        self.gtx=gtx#Ganancia antena transmisora
        self.lfs= lfs #Modelo de perdidas
        self.grx=grx #Ganancia antena receptora

    def longitudOnda(self):
        return self.c/self.f
        
    def factorRugo(self):
        if self.factor == "Agua o terreno liso":
            A = 4.0
        elif self.factor == "Sembrados densos, arenales":
            A= 3.0
        elif self.factor == "Bosques":
            A = 2.0
        elif self.factor == "Terreno normal":
            A = 1.0
        elif self.factor == "Aspero y montañoso":
            A = 0.25
        else:
            print("error")
        return A
    def factorProba(self):
        if self.probabilidad == "Area marina":
            B = 1
        elif self.probabilidad == "Area caliente o humeda":
            B = 0.5
        elif self.probabilidad ==  "Area Mediterranea":
            B = 0.25
        elif self.probabilidad == "Clima seco y fresco":
            B = 0.125
        return B
    #Calculo de disponibilidad
    def r(self):
        return self.disponibilidad/100
            
    #Margen de desvanecimiento (decibeles)
    def desvanecimiento(self):
        A= self.factorRugo()
        B= self.factorProba()
        R= self.r()
        return 30*log10(self.distancia)+10*log10(6*A*B*self.f)-10*log10(1-R)-70
    #Ecuación de Friss, solo recibe valores en decibeles
    #Potencia de ruido
    def potenciaRuido(self):
        #return '{:.2f}'.format( 10*log10(self.k*self.tk*self.anchoBanda))
        return -174+10*log10(self.anchoBanda)
    
    #sensibilidad del sistema
    def cmin(self):
        return -1*(-self.potenciaRuido()-self.sn)
    #Calculo de potencia de radio
    def gananciaSistema(self):
        return self.desvanecimiento()+self.lfs+self.lb-self.gtx-self.grx
    def rtxs(self,Fm,Lp,Lf,Lb,At,Ar):
        return Fm+Lp+Lf+Lb-At-Ar
    def rtx(self):
        return self.gananciaSistema
    #Calculod el PIRE
    def ptx(self):
      return self.gananciaSistema()+self.cmin()
    def PIRE(self):
        return self.ptx()+self.gtx-self.lf-self.lb 
    #Calculo del Friis  
    def friis(self):
        return self.PIRE()+self.gtx-self.lfs
    def potenciaRecibida(self):
      return self.friis()-self.lf-self.lb
    #Pérdida por ramificación
    # def lf(self):
    #     if self.f== 1.8:
    #         self.lf= 5.4
    #         self.lbs= 2
    #     elif self.f==7.4:
    #         self.lf= 4.7
    #         self.lbs=2
    #     elif self.f ==  8.0:
    #         pass
        
    # #Altura de la antena
    # def rn(self,d1,d2,f):
    #     return '{:.2f}'.format(sqrt((self.longitudOnda()*d1*d2)/(d1+d2)))
    # #Zona uno de fresnel 
    # def zonaUno(self,f,D):
    #     return 17.32*sqrt(D/(4*f))
  


if __name__ == "__main__":
    altura = Presupuesto()
    