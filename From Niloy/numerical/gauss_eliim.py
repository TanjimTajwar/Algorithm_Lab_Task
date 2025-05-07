import numpy as np

# Step 1: Define the augmented matrix [A | b]
A = np.array([[10.0, 2.0, 1.0, 14.0],
              [1.0, 10.0, 1.0, 13.0],
              [2.0, 3.0, 10.0, 15.0]])

n = len(A)

# Step 2: Forward Elimination
for i in range(n):
    # Make the diagonal element 1 (pivot normalization is optional but useful)
    pivot = A[i][i]
    if pivot == 0:
        raise ValueError("Zero pivot encountered!")

    for j in range(i + 1, n):
        factor = A[j][i] / pivot  # Elimination factor
        for k in range(i, n + 1):   # Include RHS column
            A[j][k] = A[j][k] - factor * A[i][k]
        print(f"Eliminating row {j}, using row {i}:")
        print(A)

# Step 3: Back Substitution
x = np.zeros(n)

for i in range(n - 1, -1, -1):  # Start from last row to first
    s = sum(A[i][j] * x[j] for j in range(i + 1, n))  # Known values
    x[i] = (A[i][n] - s) / A[i][i]  # Solve for variable

# Final result
print("Solution:")
print(f"x = {x}")
