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

if __name__=="__main__":
    Matriz=[[0.2,1.3,-4,1.25,5],
            [0.03,0.2,-0.6,0.19,0.75],
            [0.19,1.24,-3.82,0.19,4.77],
            [0.29,1.88,-5.78,1.81,7.23],
            [-0.06,-0.39,1.2,-0.38,-1.5]]
    Resultados=[8,-2.4,1.2,7.63,11.56]
    # GaussJordan(Matriz,Resultados)
    print(GaussJacobi(Matriz,Resultados))
    # print(Matriz)