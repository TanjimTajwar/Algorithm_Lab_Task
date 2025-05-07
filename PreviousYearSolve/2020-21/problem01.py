import numpy as np

# Coefficient matrix A and right-hand side vector B
A = np.array([
    [3, -4, 1, 5],
    [1, 3, -2, 5],
    [-2, -3, 2, 2],
    [-1, 5, 3, 4]
])

B = np.array([7, 12, 2, 17])

# Solving the system
solution = np.linalg.solve(A, B)

a, b, c, d = solution
print(f"a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, d = {d:.4f}")
