def GussSimple(Matriz,Resultados):
    n=len(Resultados)
    if len(Matriz)==n and n==len(Matriz[0]):
        for i in range(n):
            Matriz[i].append(Resultados[i])
        
        for i in range(n-1):
            for k in range(i+1,n):
                factor=Matriz[k][i]/Matriz[i][i]
                for j in range(n+1):
                    Matriz[i][j]=Matriz[i][j]*factor
                for j in range(n):
                    Matriz[k][j]=Matriz[k][j]-Matriz[i][j]
        x=[0]*n
        x[n-1]=Matriz[n-1][n]/Matriz[n-1][n-1]
        for i in range(len(Matriz)-2,-1,-1):
            suma=0
            for i in range(n-1):
                



        for i in range(len(Matriz)):
            print(Matriz[i])
                

    else:
        print("La matriz ingresada no es valida para este metodo")
        return None



# eliminación hacia adelante
# for i in range(0,n-1,1):
#     pivote   = AB[i,i]
#     adelante = i + 1
#     for k in range(adelante,n,1):
#         factor  = AB[k,i]/pivote
#         AB[k,:] = AB[k,:] - AB[i,:]*factor


Matriz=[[4,2,5],
        [2,5,8],
        [5,4,3]]
Resultados=[60.70,92.90,56.30]
GussSimple(Matriz,Resultados)