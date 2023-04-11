def seidel(a, b, x0, lista):
    m = len(b)
    n = max(lista)
    for k in range(n):
        for i in range(m):
            xi = b[i]
            for j in range(m):
                if i != j:
                    xi -= a[i][j] * x0[j]
            xi /= a[i][i]
            x0[i] =xi
        if (k + 1) in lista:
            for o in range(m):
                print(f'{x0[o]},')

A = [[7.46, 1.19, -4.47, -0.0], [2.58, 7.66, -2.86, -0.43], [-2.07, 0.53, 6.37, 1.97], [-0.95, -0.38, 0.49, 3.62]]
B = [-4.98, 3.05, -2.05, 2.06]
chute = [-1.51, -4.34, 0.46, -3.86]
iterations = [7, 9, 11, 12, 17, 18, 19, 22, 24, 26, 27, 29]
seidel(A, B, chute, iterations)