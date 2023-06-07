def InterpolacionLagrange(x:int,*args:list):
    resultado=0
    
    for i in range(len(args)):
        li=1
        for j in range(len(args)):
            if i!=j:
                temp=((x-args[j][0])/(args[i][0]-args[j][0]))
                li=li*temp
        temp=li*args[i][1]
        resultado+=temp
    return resultado





if __name__=="__main__":
    resultado=InterpolacionLagrange(2,[1,1],[3,3])
    print(resultado)