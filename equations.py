def exponent(x:float):
    k=1.0
    j=x
    counter=1
    base=1
    while True: 
        if j<0:
            if (-j)/base<0.00000001:
                break
        elif j/base<0.00000001:
            break
        k=k+(j/base)
        j=j*x
        counter=counter+1
        base=base*counter
    return (k)


def Ln(x:float):
    Epsilon=0.001
    yn=x-1
    eUp=exponent(yn)
    ynp=yn+2*((x-eUp)/(x+eUp))
    if(x<=0):
        return 0.0
    while True:
        if(yn-ynp<Epsilon):
            break
        yn=ynp
        eUp=exponent(yn)
        ynp=yn+2*((x-eUp)/(x+eUp))
    return ynp


def XtimesY(x:float,y:float):
    return float('%0.6f' % exponent(y*Ln(x)))
    
def sqrt(x:float,y:float):
    if(x==0):
        return 0
    return XtimesY(y, (1/x))


def calculate(x:float):
    if(x==0):
        return 0.0
    return float('%0.4f' % (exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)))