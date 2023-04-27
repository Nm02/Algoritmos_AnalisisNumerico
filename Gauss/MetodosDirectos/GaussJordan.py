def GaussJordan(Matriz,Resultados):
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

        #Eliminacion hacia atras
        for i in range(n-1,-1,-1):
            for k in range(i-1,-1,-1):
                factor=Matriz[k][i]/Matriz[i][i]
                for j in range(n,-1,-1):
                    Matriz[i][j]=Matriz[i][j]*factor
                for j in range(n,-1,-1):
                    Matriz[k][j]=Matriz[k][j]-Matriz[i][j]

        VectorResultadosDespejados=[0]*n
        # print(Matriz)

        #Metodo de gauss Jordan
        for i in range(n):
            VectorResultadosDespejados[i]=Matriz[i][n]/Matriz[i][i]
        return(VectorResultadosDespejados)    
    else:
        print("La matriz o los resultados ingresados no son validos para este metodo")
        return None



# Matriz=[[4,2,5],
#         [2,5,8],
#         [5,4,3]]
# Resultados=[60,92,56]
# # GussJordan(Matriz,Resultados)
# print(GussJordan(Matriz,Resultados))
# print(Matriz)