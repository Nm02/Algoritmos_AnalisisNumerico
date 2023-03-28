from sympy import *
import numpy as np

class CalculadoraAnalisisNumerico():
    x=Symbol("x")
    funcion=0
    def IngresarFuncion(self,y:str):
        x=Symbol("x")
        exec("self.funcion="+y)
        
    def EvaluarFuncion(self, Valor:int):
        return self.funcion.subs(self.x,Valor)
    
    def Derivada(self):
        return self.funcion.diff(self.x)

    def Biseccion(self,a:float,b:float):
        if b>a:
            temp=a
            a=b
            b=temp
        elif a==b:
            if self.funcion.subs(self.x,a)==0:
                return a
            else:
                print("No hay raices en el intervalo dado.")
                return None
        if (self.funcion.subs(self.x,a))*(self.funcion.subs(self.x,b))<0:
            xr=(a+b)/2
            if (self.funcion.subs(self.x,a))*(self.funcion.subs(self.x,xr))<0:
                b=xr
            elif (self.funcion.subs(self.x,xr))*(self.funcion.subs(self.x,b))<0:
                a=xr
            else:
                return xr
            while True:
                xrant=xr
                xr=(a+b)/2
                if -0.001<(((xrant-xr)/xr)*100)<0.001:
                    return xr
                if (self.funcion.subs(self.x,a))*(self.funcion.subs(self.x,xr))<0:
                    b=xr
                elif (self.funcion.subs(self.x,xr))*(self.funcion.subs(self.x,b))<0:
                    a=xr
                else:
                    return xr
        else:
            print("No se puede concluir si hay o no raices por el metodo de la biseccion")
            return None
    
    def RegulaFalsi(self,a,b):
        if b>a:
            temp=a
            a=b
            b=temp
        elif a==b:
            if (self.funcion.subs(self.x,a))==0:
                return a
            else:
                print("No hay raices en el intervalo dado.")
                return None
            
        if ((self.funcion.subs(self.x,a))*(self.funcion.subs(self.x,b))<0):
            mr=b-((self.funcion.subs(self.x,b))*(a-b)/((self.funcion.subs(self.x,a))-(self.funcion.subs(self.x,b))))
            if (((self.funcion.subs(self.x,a)))*(self.funcion.subs(self.x,mr)))<0:
                b=mr
            elif (self.funcion.subs(self.x,mr))*(self.funcion.subs(self.x,b))<0:
                a=mr
            else:
                return mr
            while True:
                mrant=mr
                mr=b-((self.funcion.subs(self.x,b))*(a-b)/((self.funcion.subs(self.x,a))-(self.funcion.subs(self.x,b))))
                if -0.001<(((mr-mrant)/mr)*100)<0.001:
                    return mr
                if ((self.funcion.subs(self.x,a))*(self.funcion.subs(self.x,mr))<0):
                    b=mr
                elif (self.funcion.subs(self.x,mr))*(self.funcion.subs(self.x,b))<0:
                    a=mr
                else:
                    return mr
        else:
            print("No se puede derterminar si hay raices en el intervalo con el metodo de regula falsi")
            return None

    def __str__(self):
        return self.funcion




# yprime = y.diff(x)
# print(y)
# print(yprime)

# x = Symbol('x')
# funcion=input("ingrese la funcion:")
# y=0
# exec("y="+funcion)
# print(type(y))
# print(y.subs(x,1))
a=CalculadoraAnalisisNumerico()
funcion="x**3+2*x**2+5"
a.IngresarFuncion(funcion)
print(a.RegulaFalsi(10,-10))