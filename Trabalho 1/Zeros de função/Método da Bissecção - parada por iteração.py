def bisection(f, a, b, lista):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
        n = max(lista)
        for k in range(n):
            m = 0.5 * (a + b)
            if (k + 1) in lista:
                print(f"{m},")
            fm = f(m)
            if fm == 0:
                print(f"Encontrei uma raiz em x_{k + 1}={m}")
                return
            if fa * fm < 0:
                b = m
            else:
                a = m
                fa = fm
                
func = lambda x: x**2-3
a = -2.12556
b = -0.57758
iterations = [1, 4, 7]
bisection(func, a, b, iterations)