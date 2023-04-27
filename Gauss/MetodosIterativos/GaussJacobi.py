def GaussJacobi(Matriz,Resultados,VectorInicial=None,Error=1,VueltasMinimas=100,VueltasMaximas=50):
    n=len(Matriz)
    if VectorInicial==None or len(VectorInicial)!=n:
        VectorInicial=[0]*len(Matriz)
    VectorX=VectorInicial
    contadorVueltas=0
    while True:
        contadorError=0
        contadorVueltas+=1
        for i in range(n):
            suma=Resultados[i]
            for j in range(len(Matriz[i])):
                if i!=j:
                    suma-=Matriz[i][j]*VectorInicial[j]
            VectorInicial[i]=VectorX[i]
            VectorX[i]=suma/Matriz[i][i]
            try:
                if -Error<(((VectorX[i]-VectorInicial[i])/VectorX[i])*100)<Error and contadorVueltas>=VueltasMinimas:
                    contadorError+=1
            except:
                pass
        if contadorError==n or contadorVueltas>VueltasMaximas:
            break
    # Prueba=[0]*n
    # for i in range(n):
        
    # if contadorVueltas>VueltasMaximas:
    #     print("La matriz no converge por el metodo de gauss seidel")
    #     return None
    # else:
    #     return VectorX

    return VectorX

# Matriz=[[3,-0.1,-0.2],
#         [0.1,7,-0.3],
#         [0.3,-0.2,10]]
# Resultados=[7.85,-19.3,71.4]
# print(GaussJacobi(Matriz,Resultados))