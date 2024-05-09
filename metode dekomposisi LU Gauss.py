def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for j in range(n):
        L[j][j] = 1.0

        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1

        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            if U[j][j] == 0:
                return None, None  # Menangani kasus matriks tidak bisa dipecahkan
            L[i][j] = (A[i][j] - s2) / U[j][j]

    return L, U

def solve_lu(A, b):
    L, U = lu_decomposition(A)
    if L is None or U is None:
        return None  # Matriks tidak bisa dipecahkan

    n = len(A)
    y = [0.0] * n
    x = [0.0] * n

    # Solve Ly = b using forward substitution
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    # Solve Ux = y using backward substitution
    for i in range(n-1, -1, -1):
        if U[i][i] == 0:
            return None  # Menangani kasus matriks tidak bisa dipecahkan
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]

    return x

# Contoh penggunaan:
A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
b = [1, 0, 1]

print("Matrix A:")
for row in A:
    print(row)
print("Vector b:")
print(b)

solution = solve_lu(A, b)
if solution is None:
    print("Matriks tidak bisa dipecahkan.")
else:
    print("Solusi:", solution)
