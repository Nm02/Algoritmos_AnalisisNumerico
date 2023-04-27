import math

import Gauss.MetodosDirectos.GaussSimple as GaussSimple
import Gauss.MetodosDirectos.GaussJordan as GaussJordan
import Gauss.MetodosIterativos.GaussSeidel as GaussSeidel
import Gauss.MetodosIterativos.GaussJacobi as GaussJacobi

#Ejercicio 1
#a)
"""print("a)gauss simple y gauss Jordan")
#Gauss Simple
Matriz=[[8,8,1],
        [2,1,4],
        [2,4,1]]
Resultados=[2,1,4]
print(GaussSimple.GaussSimple(Matriz,Resultados))
#Gauss Jordan
Matriz=[[8,8,1],
        [2,1,4],
        [2,4,1]]
Resultados=[2,1,4]
print(GaussJordan.GaussJordan(Matriz,Resultados))"""

#b)
"""print("b) gauss seidel y gauss Jacobi")
#Gauss Seidel
Matriz=[[10,3,1],
        [2,-10,3],
        [1,3,10]]
Resultados=[14,-5,14]
E=10*math.exp(-5)
print(GaussSeidel.GaussSeidel(Matriz,Resultados,[0,0,0],E,VueltasMaximas=20))
#Gauss Jacobi
Matriz=[[10,3,1],
        [2,-10,3],
        [1,3,10]]
Resultados=[14,-5,14]
E=10*math.exp(-5)
print(GaussJacobi.GaussJacobi(Matriz,Resultados,[0,0,0],E,VueltasMaximas=20))"""

#Ejercicio 2
"""def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)
print("Gauss Simple")
print("Redondeo")
Matriz=[[round(1/1,3),round(1/2,3),round(1/3,3),round(1/4,3)],
        [round(1/2,3),round(1/3,3),round(1/4,3),round(1/5,3)],
        [round(1/3,3),round(1/4,3),round(1/5,3),round(1/6,3)],
        [round(1/4,3),round(1/5,3),round(1/6,3),round(1/7,3)]]
Resultados=[round(25/12,3),round(77/60,3),round(57/60,3),round(319/420,3)]
print(GaussSimple.GaussSimple(Matriz,Resultados))
print("truncamiento")
Matriz=[[truncate(1/1,3),truncate(1/2,3),truncate(1/3,3),truncate(1/4,3)],
        [truncate(1/2,3),truncate(1/3,3),truncate(1/4,3),truncate(1/5,3)],
        [truncate(1/3,3),truncate(1/4,3),truncate(1/5,3),truncate(1/6,3)],
        [truncate(1/4,3),truncate(1/5,3),truncate(1/6,3),truncate(1/7,3)]]
Resultados=[truncate(25/12,3),truncate(77/60,3),truncate(57/60,3),truncate(319/420,3)]
print(GaussSimple.GaussSimple(Matriz,Resultados))

print("Gauss Jordan")
print("Redondeo")
Matriz=[[round(1/1,3),round(1/2,3),round(1/3,3),round(1/4,3)],
        [round(1/2,3),round(1/3,3),round(1/4,3),round(1/5,3)],
        [round(1/3,3),round(1/4,3),round(1/5,3),round(1/6,3)],
        [round(1/4,3),round(1/5,3),round(1/6,3),round(1/7,3)]]
Resultados=[round(25/12,3),round(77/60,3),round(57/60,3),round(319/420,3)]
print(GaussJordan.GaussJordan(Matriz,Resultados))
print("truncamiento")
Matriz=[[truncate(1/1,3),truncate(1/2,3),truncate(1/3,3),truncate(1/4,3)],
        [truncate(1/2,3),truncate(1/3,3),truncate(1/4,3),truncate(1/5,3)],
        [truncate(1/3,3),truncate(1/4,3),truncate(1/5,3),truncate(1/6,3)],
        [truncate(1/4,3),truncate(1/5,3),truncate(1/6,3),truncate(1/7,3)]]
Resultados=[truncate(25/12,3),truncate(77/60,3),truncate(57/60,3),truncate(319/420,3)]
print(GaussJordan.GaussJordan(Matriz,Resultados))

print("Gauss Seidel")
print("Redondeo")
Matriz=[[round(1/1,3),round(1/2,3),round(1/3,3),round(1/4,3)],
        [round(1/2,3),round(1/3,3),round(1/4,3),round(1/5,3)],
        [round(1/3,3),round(1/4,3),round(1/5,3),round(1/6,3)],
        [round(1/4,3),round(1/5,3),round(1/6,3),round(1/7,3)]]
Resultados=[round(25/12,3),round(77/60,3),round(57/60,3),round(319/420,3)]
E=10*math.exp(-5)
print(GaussSeidel.GaussSeidel(Matriz,Resultados,[0,0,0],E,VueltasMaximas=20))
print("truncamiento")
Matriz=[[truncate(1/1,3),truncate(1/2,3),truncate(1/3,3),truncate(1/4,3)],
        [truncate(1/2,3),truncate(1/3,3),truncate(1/4,3),truncate(1/5,3)],
        [truncate(1/3,3),truncate(1/4,3),truncate(1/5,3),truncate(1/6,3)],
        [truncate(1/4,3),truncate(1/5,3),truncate(1/6,3),truncate(1/7,3)]]
Resultados=[truncate(25/12,3),truncate(77/60,3),truncate(57/60,3),truncate(319/420,3)]
E=10*math.exp(-5)
print(GaussSeidel.GaussSeidel(Matriz,Resultados,[0,0,0],E,VueltasMaximas=20))

print("Gauss Jcobi")
print("Redondeo")
Matriz=[[round(1/1,3),round(1/2,3),round(1/3,3),round(1/4,3)],
        [round(1/2,3),round(1/3,3),round(1/4,3),round(1/5,3)],
        [round(1/3,3),round(1/4,3),round(1/5,3),round(1/6,3)],
        [round(1/4,3),round(1/5,3),round(1/6,3),round(1/7,3)]]
Resultados=[round(25/12,3),round(77/60,3),round(57/60,3),round(319/420,3)]
E=10*math.exp(-5)
print(GaussJacobi.GaussJacobi(Matriz,Resultados,[0,0,0],E,VueltasMaximas=20))
print("truncamiento")
Matriz=[[truncate(1/1,3),truncate(1/2,3),truncate(1/3,3),truncate(1/4,3)],
        [truncate(1/2,3),truncate(1/3,3),truncate(1/4,3),truncate(1/5,3)],
        [truncate(1/3,3),truncate(1/4,3),truncate(1/5,3),truncate(1/6,3)],
        [truncate(1/4,3),truncate(1/5,3),truncate(1/6,3),truncate(1/7,3)]]
Resultados=[truncate(25/12,3),truncate(77/60,3),truncate(57/60,3),truncate(319/420,3)]
E=10*math.exp(-5)
print(GaussJacobi.GaussJacobi(Matriz,Resultados,[0,0,0],E,VueltasMaximas=20))"""


#Ejercicio 3
#Gauss Simple
"""Matriz=[[5,3,4],
        [2,5,5],
        [5,3,6]]
Resultados=[45,44,58]
print(GaussSimple.GaussSimple(Matriz,Resultados))"""

#Ejercicio 4
#a)
"""print("a)")
print("la matriz del inciso a diverge para los metodos de Gauss Seidel y Gauss Jacobi")

#b
print("b)")
Matriz=[[3,1,-1],
        [1,2,1],
        [-2,0,1]]
Resultados=[0,1,3]

E=10*math.exp(-5)
print(GaussJacobi.GaussJacobi(Matriz,Resultados,Error=E))

#C
print("c)")
Matriz=[[22.2,0.5,-1.5,2-3],
        [1.5,23.5,1.0,5.9],
        [6.0,3.0,27.0,0],
        [0,0,-17.5,20.9]]
Resultados=[-1,2,6,-5]

E=10*math.exp(-5)
print(GaussJacobi.GaussJacobi(Matriz,Resultados,Error=E))

#D
print("d)")
Matriz=[[2.5,0.14,0,0],
        [-0.25,1.4,0.72,0],
        [0,0.44,3.2,-0.21],
        [0.85,0,0.11,1.8]]
Resultados=[3.4,-1.1,1-6,-2.2]

E=10*math.exp(-5)
print(GaussJacobi.GaussJacobi(Matriz,Resultados,Error=E))"""

#Ejercicio 5
print("Gauss Jacobi")
Matriz=[[22.2,0.5,1.3,2.3],
        [0.5,23.5,1.0,5.9],
        [6.0,3.0,27.0,0],
        [0,0,17.5,20.9]]
Resultados=[-1,2,6,-5]

E=10*math.exp(-7)
print(GaussJacobi.GaussJacobi(Matriz,Resultados,VectorInicial=[0.1,-0.1,0.1,-0.1],Error=E,VueltasMaximas=22))

print("Gauss Seidel")
Matriz=[[22.2,0.5,1.3,2.3],
        [0.5,23.5,1.0,5.9],
        [6.0,3.0,27.0,0],
        [0,0,17.5,20.9]]
Resultados=[-1,2,6,-5]

E=10*math.exp(-7)
print(GaussSeidel.GaussSeidel(Matriz,Resultados,VectorInicial=[0.1,-0.1,0.1,-0.1],Error=E,VueltasMaximas=22))