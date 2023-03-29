"""Importo librerias para funciones matematicas"""
import math
"""Importo mis Librerias para el Ejercicio 2"""
import MetodosCerrados.BiseccionParoError as biseccion
import MetodosCerrados.RegulaFalsiParoError as RegulaFalsi
"""Importo mis Librerias para el Ejercicio 3"""
import MetodosAbiertos.NewtonRaphsonParoError as Newton
import MetodosAbiertos.PuntoFijoParoError as PuntoFijo
import MetodosAbiertos.SecanteParoError as Secante

"""Ejercicio 2"""
# def f(x):
#     return math.cos(4*x-2)+math.exp(1-x)

# a=0.8
# b=1.2
# E=10*math.exp(-4)
# print(biseccion.Biseccion(f,a,b,E))
# print(RegulaFalsi.RegulaFalsi(f,a,b,E))



"""Ejercicio 3"""
def F(x):
    return x**2+10*math.cos(x)

def FPrima(x):
    return 2*x-10*math.sin(x)
"""
f(x)=x**2+10*math.cos(x)=0
g(x)=acos(-(x**2)/10)
"""
def g(x):
    return math.acos(-(x**2)/10)

"""
g'(x)=
"""
def gPrima(x):
    return -((2*x)/(math.sqrt(100-x**4)))

x0=1.5
xant=1.2
E=10*math.exp(-7)
print(Newton.NewtonRaphson(F,FPrima,x0,xant,E))
print(PuntoFijo.PuntoFijo(g,gPrima,x0,E))
print(Secante.Secante(F,x0,xant,E))
