def Simpson1_3Multiple(a:int,b:int,*args:float):
    I=b-a
    sum=args[0]+args[-1]
    sumtemp=0
    for i in range(1,len(args)-1,2):
        sumtemp+=args[i]
    sum+=4*sumtemp
    sumtemp=0
    for j in range(2,len(args)-1,2):
        sumtemp+=args[j]
    sum+=2*sumtemp
    sum=sum/(3*len(args))
    I=I*sum
    return I

if __name__=="__main__":
    resultado=Simpson1_3Multiple(-1,1,1,0.5625,0.25,0.0625,0,0.0625,0.25,0.5625,1)
    print(resultado)
    