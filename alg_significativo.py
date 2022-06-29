from math import floor, log10

def ar(x,n): #x= número a ser arredondado, n= número de algarismos significativos
    a = floor(log10(abs(x)))
    if a > 1:
        return round(x,-(a-n+1))
    elif a < 1:
        return round(x*10**(-a), n-1)*10**a
    else:
        return round(x,n-1)