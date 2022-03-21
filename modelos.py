from math import dist
from numpy import log10

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
        if ciudad ==0:
            if self.frecuencia <= 200*10**6:
                return 8.29*(log10(1.54*self.hre))**2-1.1
            else:
                return 3.2*log10(11.75*self.hre)**2-4.97
        else:
            return (1.1*log10(self.frecuencia-0.7))*self.hre-(1.56*log10(self.frecuencia-0.8))
        
    def calcular(self,ciudad,urbano):
        lp= 69.55+26.16*log10(self.frecuencia)-13.82*log10(self.hte)-self.calcularA(ciudad)
        +(44.9-6.55*log10(self.hte))*log10(self.distancia)
        if urbano:
            return lp-2*(log10(self.frecuencia/28))**2-5.4
        else:
            return lp
        

class Cost(Okumura):

    def __init__(self,frecuencia,distancia,hte=1,hre=1,ciudadGrande=True,subUrbano=True):
        ModeloPerdidas.__init__(ModeloPerdidas, frecuencia, distancia)#Importar contructor de clase madre
        Okumura.__init__(Okumura,frecuencia,distancia ,hte=1,hre=1,ciudadGrande=True,subUrbano=True)#Importar constructor clase hija
    def calcular(self,c):
        correction = {"Ciudad densa": 0, "Ciudad":-5,"Barrios campestres": -10, "Rural":-17}
        lp= 46.3+33.9*log10(self.frecuencia)-13.82*log10(self.hte)
        -self.calcularA()*self.hre+(44.9-6.55*log10(self.hte))*log10(self.distancia)+correction[c]
        return lp

# if __name__ == "__main__":
#     modelo= Cost(2.4,10)
#     print(modelo.calcular("Ciudad densa"))
#     model1 = Okumura(2.4,10,4,4,False,True)
#     print(model1.calcularLb())
    
    


    
                






