def bisection(f, a, b, n):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
        for k in range(n):
            m = 0.5 * (a + b)
            fm = f(m)
            if fm == 0:
                print(f"Encontrei uma raiz em x_{k + 1}={m}")
                return
            if fa * fm < 0:
                b = m
            else:
                a = m
                fa = fm
        print(f"{m},")
    return

R = 0.08205736608096
T = [450, 850, 1100]
p = [1,60,80]

a = [3.7617569, 21.3093503]
b = [0.05443, 0.1182]


n = 50
ac = 0.001
bc = 200

for i in range(len(T)):
    for j in range(len(p)):
        g = R*T[i]/p[j]
        print('g T = ',T[i],' p = ',p[j])
        print(g)
        for k in range(len(a)):
            vw = lambda v: R*T[i] - (p[j] + a[k]/v**2)*(v - b[k])
            print('vw T = ',T[i],' p = ',p[j], ' a = ', a[k])
            bisection(vw, ac, bc, n)

