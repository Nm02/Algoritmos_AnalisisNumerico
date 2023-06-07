def IntegracionNewton_Cortez(a:float,b:float,*args:float):
    n=len(args)
    h=(b-a)/n
    sum=0
    for i in range(1,n-1):
        sum+=args[i]
    # print(sum)
    sum=sum*2
    # print(sum)
    sum+=args[0]
    # print(sum)
    sum+=args[-1]
    # print(sum)
    sum=sum*(h/2)
    # print(h)
    return sum

if __name__=="__main__":
    resultado=IntegracionNewton_Cortez(-1,1,1,0,1)
    print(resultado)


