def simpson3_8(a:float,b:float,fx0:float,fx1:float,fx2:float,fx3:float):
    I=b-a
    sum=fx0+3*fx1+3*fx2+fx3
    sum=sum/8
    I=I*sum
    return I

if __name__=="__main__":
    resultado=simpson3_8(0,6,0,1,0,-1)
    print(resultado)
