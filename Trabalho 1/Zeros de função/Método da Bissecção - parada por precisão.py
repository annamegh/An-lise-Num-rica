import math
def bisection(f, a, b, n, tol):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
#        n = max(lista)
        for k in range(n):
            m = 0.5 * (a + b)
#            if (k + 1) in lista:
#                print(f"{m},")
            fm = f(m)
            if abs(fm) < tol:
                print(f"Encontrei uma raiz em x_{k + 1}={m}")
                return
            if fa * fm < 0:
                b = m
            else:
                a = m
                fa = fm

func = lambda x: math.exp(3*x)-5
a = -0.847802
b = 2.147284
tol = 3.87187e-08
n = 100
bisection(func, a, b, n, tol)
