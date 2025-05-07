import numpy as np

A = np.array([[10, 2, 1],
              [1, 10, 1],
              [2, 3, 10]])

b = np.array([14, 13, 15])
x = np.array([0.0, 0.0, 0.0])

max_iterations = 25
tolerance = 1e-4
n = len(b)

for iteration in range(max_iterations):
    x_new = np.zeros_like(x)

    for i in range(n):
        s = 0
        for j in range(n):
            if i != j:
                s += A[i][j] * x[j]
        x_new[i] = (b[i] - s) / A[i][i]

    print(f"Iteration {iteration + 1}: x = {x_new}")

    if np.allclose(x, x_new, atol=tolerance):
        print("Converged.")
        break

    x = x_new

print(f"Final solution: x = {x}")
