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



# """Ejercicio 3"""
# """
# f(x)=x**2+10*math.cos(x)=0
# x**2=10*math.cos(x)
# x=(10*math.cos(x))**(1/2)=g(x)
# """
# def g(x):
#     return (10*math.cos(x))**(1/2)

# """
# g'(x)=-((5*math.sin(x)/((10*math.cos(x))**1/2)))
# """
# def gPrima(x):
#     return -((5*math.sin(x)/((10*math.cos(x))**1/2)))

# x0=1.5
# xant=1.2
# E=10*math.exp(-7)
# print(Newton.NewtonRaphson(g,gPrima,x0,xant,E))
# print(gPrima(2.5820099129931218))
# # print(PuntoFijo.PuntoFijo(g,gPrima,x0,E))
# print(Secante.Secante(g,x0,E))
