def print_matriz(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=",")
    return

A= [[-0.2222222222222222, -1.25, 4.0], [3.0, -0.7142857142857143, 0.5555555555555556], [0.14285714285714285, 0.875, -1.2], [-0.25, 0.7777777777777778, -1.8]]


temp = A[0]
A[0] = A[3]
A[3] = temp

for i in range(len(A[0])):
    A[0][i] = (-2)*A[0][i]

for i in range(len(A[0])):
    A[1][i] = (5/3)*A[3][i] + A[1][i]

temp = A[0]
A[0] = A[2]
A[2] = temp

for i in range(len(A[0])):
    A[3][i] = (-3/4)*A[1][i] + A[3][i]

for i in range(len(A[0])):
    A[2][i] = (-6)*A[2][i]

print_matriz(A)