import math

def newton(f,df,x0,n):
    raiz = x0
    for i in range(n):
        if df(raiz) != 0: # se a derivada for zero sai    
            raiz=raiz-f(raiz)/df(raiz)
    print(f"{raiz},")
    return 


R = 0.08205736608096
T = [700, 850, 1850]
p = [10,20,70]

a = [7.9242335, 40.9583965]
b = [0.09044, 0.213]


n = 20
x0 = 80

for i in range(len(T)):
    for j in range(len(p)):
        g = R*T[i]/p[j]
        print('g T = ',T[i],' p = ',p[j])
        print(g)
        for k in range(len(a)):
            vw = lambda v: R*T[i] - (p[j] + a[k]/v**2)*(v - b[k])
            df = lambda v: -p[j] + a[k]/(v**2) - 2*a[k]*b[k]/(v*v**2)
            print('vw T = ',T[i],' p = ',p[j], ' a = ', a[k])
            newton(vw, df, x0, n)