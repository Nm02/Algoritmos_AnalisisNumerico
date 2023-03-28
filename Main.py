import Funciones as Funciones

import MetodosCerrados.RegulaFalsiParo as RegulaFalsi
import MetodosCerrados.Biseccion as Biseccion

import MetodosAbiertos.PuntoFijo as PuntoFijo
import MetodosAbiertos.NewtonRaphson as Newton
import MetodosAbiertos.SecanteParo as Secante

# a=float(input("ingrese el primer numero del intervalo:"))
# b=float(input("ingrese el segundo numero del intervalo:"))
# Funcion=input("Ingrese la funcion (La variable debe ser x):")
print(RegulaFalsi.RegulaFalsi(Funciones.f,-10,10))
# print(Biseccion.Biseccion(Funcion,a,b))
# x=float(input("ingrese el x inicial:"))
# print(PuntoFijo.PuntoFijo(Funciones.f,Funciones.gPrima,x))
# print(Newton.NewtonRaphson(Funciones.g,Funciones.gPrima,x))
# print(Secante.Secante(Funciones.f,x))

