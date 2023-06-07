def Simpson1_3(a:float,b:float,fx0:float,fx1:float,fx2:float):
    I=b-a
    sum=fx0+4*fx1+fx2
    sum=sum/6
    I=I*sum
    return I

if __name__=="__main__":
    resultado=Simpson1_3(-1,1,1,0,1)
    print(resultado)
