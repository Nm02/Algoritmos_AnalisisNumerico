import Gauss.MetodosDirectos.GaussSimple as GaussSimple
import Gauss.MetodosDirectos.GaussJordan as GaussJordan
import Gauss.MetodosIterativos.GaussSeidel as GaussSeidel
import Gauss.MetodosIterativos.GaussJacobi as GaussJacobi

#Ejercicio 1
#a)
#GaussSimple
Matriz=[[8,8,1],
        [2,1,4],
        [2,4,1]]
Resultados=[2,1,4]
print(GaussSimple.GaussSimple(Matriz,Resultados))
#GaussJacob
Matriz=[[8,8,1],
        [2,1,4],
        [2,4,1]]
Resultados=[2,1,4]
print(GaussJordan.GaussJordan(Matriz,Resultados))