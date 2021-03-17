def exponant(x:float):
    if (x==0):
        return 0
    k=1.0
    j=x
    counter=1
    base=1
    while True: 
        if j<0:
            if (j*-1)/base<0.000000000001:
                break
        elif j/base<0.00000000001:
            break
        k=k+(j/base)
        j=j*x
        counter=counter+1
        base=base*counter
    return (k)


def ln(x:float):
    Epsilon=0.001
    yn=x-1
    eUp=exponant(yn)
    ynp=yn+2*((x-eUp)/(x+eUp))
    if(x<0):
        return 0
    while True:
        if(yn-ynp<Epsilon):
            break
        yn=ynp
        eUp=exponant(yn)
        ynp=yn+2*((x-eUp)/(x+eUp))
    return ynp


def XtimeY(x:float,y:float):
    return float('%0.6f' % exponant(y*ln(x)))
    
def sqrt(x:float,y:float):
    return XtimeY(y, (1/x))


def calculate(x:float):
    return exponant(x)*XtimeY(7,x)*XtimeY(x,-1)*sqrt(x,x)