def print_matrix(matrix):
    for row in matrix:
        print(row)
        
def crout_decomposition(A):
    n = len(A)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]
    
    for j in range(n):
        U[j][j] = 1
        
        for i in range(j, n):
            sum_val = sum(L[i][k] * U[k][j] for k in range(i))
            L[i][j] = A[i][j] - sum_val
            
        for i in range(j, n):
            sum_val = sum(L[j][k] * U[k][i] for k in range(j))
            U[j][i] = (A[j][i] - sum_val) / L[j][j]
            
    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = [0] * n
    
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
        
    return y

def backward_substitution(U, y):
    n = len(y)
    x = [0] * n
    
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
        
    return x

def crout_solver(A, b):
    L, U = crout_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x, L, U

# Contoh penggunaan
A = [[2, -1, 0],
     [-1, 2, -1],
     [0, -1, 2]]
b = [1, 0, 1]


solusi, L, U = crout_solver(A, b)

print("Matriks A:")
print_matrix(A)
print("Vektor b:")
print(b)

print("Matriks L:")
for row in L:
    print(row)
print("Matriks U:")
for row in U:
    print(row)
print("Vektor b:")
print(b)
print("Solusi:")
print(solusi)
