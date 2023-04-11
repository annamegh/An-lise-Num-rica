import math

def pos_falsa(f, a, b, lista):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
        n = max(lista)
        for k in range(n):
            x1 = (a*f(b) - b*f(a)) / (f(b) - f(a))

            if (k+1) in lista:
                print(f"{x1},")
            if f(a)*f(x1) < 0:
                a, b = a, x1
            if f(x1)*f(b) < 0:
                a, b = x1, b
    return 


func = lambda x: x*math.cos(x)-3*x**2+4*x-1
a = 0.0541
b = 0.839
iterations = [1, 2, 4, 6, 7, 8, 12, 14, 15, 19]
pos_falsa(func, a, b, iterations)