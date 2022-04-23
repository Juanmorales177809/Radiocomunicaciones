import math

hre= 4
hte= 100
frecuencia= 870
distancia= 2
ciudad= 'Ciudad media-grande'
urbano= True
lpn= 115

#Calcular A
if hte>=30 and hte<200 and hre >= 1 and hre <= 10:
    if ciudad =='Ciudad media-grande':
        if frecuencia <= 200:
            a= 8.29*(math.log10(1.54*hre))**2-1.1
        else:
            a= 3.2*(math.log10(11.75*hre))**2-4.97
    elif ciudad =='Ciudad media-pequeña':
        a=(1.1*math.log10(frecuencia-0.7))*hre-(1.56*math.log10(frecuencia-0.8))

#Calcular Lp
lp0= 69.55+(26.16*math.log10(frecuencia))-(13.82*math.log10(hte))-a
lp1=(44.9-(6.55*math.log10(hte)))*math.log10(distancia)
lp= lp0+lp1
if urbano:
    lb= lpn-2*(math.log10(frecuencia/28))**2-5.4
        
#Calcular distancia para Lp=115

DdB0= 69.55+(26.16*math.log10(frecuencia))-(13.82*math.log10(hte))-a
DdB1= 44.9-6.55*math.log10(hte)
DdB= (lpn-DdB0)/DdB1
D= 10**DdB
        
#Area hexagonal
ace=(3*math.sqrt(3)/2)*D
print(lp,D,ace)      