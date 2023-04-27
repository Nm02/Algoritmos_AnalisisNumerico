def GaussSimple(Matriz,Resultados):
    n=len(Resultados)
    if len(Matriz)==n and n==len(Matriz[0]):
        #Agregar los resultados a la matriz
        for i in range(n):
            Matriz[i].append(Resultados[i])
        
        #Elimincacion hacia adelante
        for i in range(n-1):
            for k in range(i+1,n):
                factor=Matriz[k][i]/Matriz[i][i]
                for j in range(n+1):
                    Matriz[i][j]=Matriz[i][j]*factor
                for j in range(n+1):
                    Matriz[k][j]=Matriz[k][j]-Matriz[i][j]
        VectorResultadosDespejados=[0]*n
        # VectorResultadosDespejados[n-1]=Matriz[n-1][n]/Matriz[n-1][n-1]
        # print(VectorResultadosDespejados)

        #Metodo de gauss simple
        for i in range(n-1,-1,-1):
            suma=Matriz[i][n]
            for j in range(n-1,-1,-1):
                if i==j:
                    suma=suma/Matriz[i][i]
                    break
                suma=suma-(Matriz[i][j]*VectorResultadosDespejados[j])
            VectorResultadosDespejados[i]=suma
        return(VectorResultadosDespejados)    
    else:
        print("La matriz o los resultados ingresados no son validos para este metodo")
        return None



# Matriz=[[4,2,5],
#         [2,5,8],
#         [5,4,3]]
# Resultados=[60,92,56]
# GussSimple(Matriz,Resultados)
# print(GussSimple(Matriz,Resultados))
# print(Matriz)