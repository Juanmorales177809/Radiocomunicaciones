
from numpy import log10

class ModeloPerdidas:
    def __init__(self,frecuencia,distancia):
        self.frecuencia= frecuencia
        self.distancia= distancia

class Path(ModeloPerdidas):

    def calcular(self):
        lfs= 92.44+20*log10(self.frecuencia)+20*log10(self.distancia)
        return lfs

class Okumura(ModeloPerdidas):
    def __init__(self,hte=1,hre=1,ciudadGrande=True,subUrbano=True):
        self.hte= hte
        self.hre= hre
        self.ciudadGrande= ciudadGrande
        self.subUrbano= subUrbano
    
    def calcularA(self):
        if self.ciudadGrande:
            if self.frecuencia <= 200*10**6:
                a = 8.29*(log10(1.54*self.hre))**2-1.1
            else: 
                a= 3.2*log10(11.75*self.hre)**2-4.97
        else:
            a= (1.1*log10(self.frecuencia-0.7))*self.hre-(1.56*log10(self.frecuencia-0.8))
        return a
    def calcularLb(self):
        if self.subUrbano:
            lb = self.calcular()-2*(log10(self.frecuencia/28))**2-5.4
            return lb
    def calcular(self):
        lp= 69.55+26.16*log10(self.frecuencia)-13.82*log10(self.hte)-self.calcularA()
        +(44.9-6.55*log10(self.hte))*log10(self.distancia)
        return lp

class Cost(Okumura):

    def __init__(self,frecuencia,distancia,hte=1,hre=1,ciudadGrande=True,subUrbano=True):
        ModeloPerdidas.__init__(ModeloPerdidas, frecuencia, distancia)
        Okumura.__init__(Okumura,hte=1,hre=1,ciudadGrande=True,subUrbano=True)
    def calcular(self,c):
        correction = {"Ciudad densa": 0, "Ciudad":-5,"Barrios campestres": -10, "Rural":-17}
        lp= 46.3+33.9*log10(self.frecuencia)-13.82*log10(self.hte)
        -self.calcularA()*self.hre+(44.9-6.55*log10(self.hte))*log10(self.distancia)+correction[c]
        return lp

if __name__ == "__main__":
    modelo= Cost(2.4,10,2,4)
    print(modelo.calcular("Ciudad densa"))
    
    


    
                






