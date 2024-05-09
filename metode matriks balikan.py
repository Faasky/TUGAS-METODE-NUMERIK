# Definisikan matriks A dan vektor B
A = [[2, 3], [1, -2]]
B = [7, 1]

# Menghitung determinan matriks A
det_A = A[0][0] * A[1][1] - A[0][1] * A[1][0]

# Menghitung matriks kofaktor A
cofactor_A = [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]

# Menghitung matriks adjoint A
adjoint_A = [[cofactor_A[0][0], cofactor_A[1][0]], [cofactor_A[0][1], cofactor_A[1][1]]]

# Menghitung matriks balikan A
A_inv = [[adjoint_A[0][0] / det_A, adjoint_A[0][1] / det_A],
         [adjoint_A[1][0] / det_A, adjoint_A[1][1] / det_A]]

# Menghitung solusi x = A_inv * B
x = [A_inv[0][0] * B[0] + A_inv[0][1] * B[1], A_inv[1][0] * B[0] + A_inv[1][1] * B[1]]

# Cetak matriks A, vektor B, dan solusi x
print("Matriks A:")
for row in A:
    print(row)

print("\nVektor B:")
print(B)

print("\nSolusi x:")
print(x)
