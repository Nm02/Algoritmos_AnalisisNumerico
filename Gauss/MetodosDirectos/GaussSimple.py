def GaussSimple(Matriz,Resultados):
    n=len(Resultados)
    if len(Matriz)==n and n==len(Matriz[0]):
        #Agregar los resultados a la matriz
        for i in range(n):
            Matriz[i].append(Resultados[i])
        
        #Elimincacion hacia adelante
        for i in range(n-1):
            for k in range(i+1,n):
                if Matriz[i][i]==0:
                    for i in range(k,len(Matriz)):
                        if Matriz[k][i]!=0:
                            Matriz[k][i],Matriz[i][i]=Matriz[i][i],Matriz[k][i]
                            break
                if Matriz[i][i]!=0:
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
                    if Matriz[i][i]!=0:
                        suma=suma/Matriz[i][i]
                    break
                suma=suma-(Matriz[i][j]*VectorResultadosDespejados[j])
            VectorResultadosDespejados[i]=suma
        return(VectorResultadosDespejados)    
    else:
        print("La matriz o los resultados ingresados no son validos para este metodo")
        return None


"""
resolver
0,2a+1.3b-4c+1.25d+5e=8
-0.06a-0.39b+1.2c-0.38d-1.5e=-2.4
0.03a+0.2b-0.6c+0.19d+0.75e=1.2
0.19a+1.24b-3.82c+1.19d+4.77e=7.63
0.29a+1.88b-5.78c+1.81d+7.23e=11-56
a = -9.04348
b = -5.78261
c = -4.78261
d = 5.04348
e = 1.30435
"""
if __name__=="__main__":
    Matriz=[[0.2,1.3,-4,1.25,5],
            [-0.06,-0.39,1.2,-0.38,-1.5],
            [0.03,0.2,-0.6,0.19,0.75],
            [0.19,1.24,-3.82,0.19,4.77],
            [0.29,1.88,-5.78,1.81,7.23]
            ]
    Resultados=[8,-2.4,1.2,7.63,11.56]
    # GaussSimple(Matriz,Resultados)
    Resultados2=[-9.04348,-5.78261,-4.78261,5.04348,1.30435]
    # print(Matriz)
    Matriz=[[0.2,1.3,-4,1.25,5],
            [0.03,0.2,-0.6,0.19,0.75],
            [0.19,1.24,-3.82,0.19,4.77],
            [0.29,1.88,-5.78,1.81,7.23],
            [-0.06,-0.39,1.2,-0.38,-1.5]]
    print(Resultados2)
    for i in range(len(Matriz)):
        suma=0
        for j in range(len(Matriz)):
            suma=suma+Matriz[i][j]*Resultados2[i]
        print(Resultados[i]-0.5<suma<Resultados[i]+0.5)
        print([Resultados[i]-0.5,suma,Resultados[i]+0.5])
