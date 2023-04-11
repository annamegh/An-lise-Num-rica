def jacobi(a, b, x0, lista):
    m = len(b)
    n = max(lista)
    for k in range(n):
        X = []
        for i in range(m):
            xi = b[i]
            for j in range(m):
                if i != j:
                    xi -= a[i][j] * x0[j]
            xi /= a[i][i]
            X.append(xi)
        if (k + 1) in lista:
            for o in range(m):
                print(f'{X[o]},')
        x0 = X

A = [[9.25, 4.99, -0.09, 2.46], [-1.87, 5.67, -2.06, -0.03], [-2.13, -4.6, 8.67, -0.23], [-2.01, -0.22, 0.46, 4.4]]
B = [0.41, 1.52, -1.96, 4.03]
chute = [3.86, -3.04, 4.04, 2.42]
iterations = [3, 6, 7, 10, 13, 15, 16, 18, 20, 21, 26, 28]
jacobi(A, B, chute, iterations)

