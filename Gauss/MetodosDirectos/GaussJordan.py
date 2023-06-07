def GaussJordan(Matriz,Resultados):
    n=len(Resultados)
    if len(Matriz)==n and n==len(Matriz[0]):
        #Agregar los resultados a la matriz
        for i in range(n):
            Matriz[i].append(Resultados[i])
        
        #Elimincacion hacia adelante
        for i in range(n-1):
            for k in range(i+1,n):
                if Matriz[i][i]==0:
                    for j in range(i+1,n):
                        if Matriz[j][i]!=0:
                            temp=Matriz[i]
                            Matriz[i]=Matriz[j]
                            Matriz[j]=temp
                            break
                if Matriz[i][i]==0:
                    break
                else:
                    factor=Matriz[k][i]/Matriz[i][i]
                    for j in range(n+1):
                        Matriz[i][j]=Matriz[i][j]*factor
                    for j in range(n+1):
                        Matriz[k][j]=Matriz[k][j]-Matriz[i][j]

        #Eliminacion hacia atras
        for i in range(n-1,-1,-1):
            for k in range(i-1,-1,-1):
                if Matriz[i][i]==0:
                    for j in range(i+1,n):
                        if Matriz[j][i]!=0:
                            temp=Matriz[i]
                            Matriz[i]=Matriz[j]
                            Matriz[j]=temp
                            break
                if Matriz[i][i]==0:
                    break
                else:
                    factor=Matriz[k][i]/Matriz[i][i]
                    for j in range(n,-1,-1):
                        Matriz[i][j]=Matriz[i][j]*factor
                    for j in range(n,-1,-1):
                        Matriz[k][j]=Matriz[k][j]-Matriz[i][j]

        VectorResultadosDespejados=[0]*n
        # print(Matriz)

        #Metodo de gauss Jordan
        for i in range(n):
            if Matriz[i][i]!=0:
                VectorResultadosDespejados[i]=Matriz[i][n]/Matriz[i][i]
        return(VectorResultadosDespejados)    
    else:
        print("La matriz o los resultados ingresados no son validos para este metodo")
        return None


if __name__=="__main__":
    Matriz=[[0.2,1.3,-4,1.25,5],
            [-0.06,-0.39,1.2,-0.38,-1.5],
            [0.03,0.2,-0.6,0.19,0.75],
            [0.19,1.24,-3.82,0.19,4.77],
            [0.29,1.88,-5.78,1.81,7.23]
            ]
    Resultados=[8,-2.4,1.2,7.63,11.56]
    # GaussJordan(Matriz,Resultados)
    print(GaussJordan(Matriz,Resultados))
    # print(Matriz)
    for i in range(len(Matriz)):
        suma=0
        for j in range(len(Matriz)):
            suma=suma+Matriz[i][j]*Resultados[i]
        print(Resultados[i]-0.5<suma<Resultados[i]+0.5)
        print([Resultados[i]-0.5,suma,Resultados[i]+0.5])


