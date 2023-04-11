import math

def newton(f,df,x0,lista):
    n = max(lista)
    raiz = x0
    for i in range(n):
        if df(raiz) != 0: # se a derivada for zero sai    
            raiz=raiz-f(raiz)/df(raiz)
        if (i + 1) in lista:
            print(f"{raiz},")
#        if(raiz == 0):
#          print(f"Encontrei uma raiz em x_{i + 1}={raiz}");
    return 

# teste :

func = lambda x:  math.exp(x)-2*x**2+x-1.5
x_0 = 0.14612
df= lambda x: math.exp(x) -4*x + 1
iterations = [1, 3, 5]
newton(func,df, x_0, iterations)