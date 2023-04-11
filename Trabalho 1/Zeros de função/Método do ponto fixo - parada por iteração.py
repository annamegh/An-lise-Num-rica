import math

def ponto_fixo(f, x0, lista):
    n = max(lista)
    for i in range(n):
        x = f(x0)
        if (i+1) in lista:
            print(f"{x},")
        x0 = x

    return

func = lambda x: math.sqrt((x + 3) / (pow(x, 2) + 2))
x0 = 1.6635
iterations = [1, 2, 3, 4, 5, 6, 7, 8]
ponto_fixo(func, x0, iterations)