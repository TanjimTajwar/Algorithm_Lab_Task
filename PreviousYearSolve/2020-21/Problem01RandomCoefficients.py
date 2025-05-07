np.random.seed(0)  # for reproducibility
A_rand = np.random.randint(-10, 10, (4, 4))
B_rand = np.random.randint(-10, 10, 4)

print("Random Coefficient Matrix A:\n", A_rand)
print("Random RHS Vector B:\n", B_rand)

try:
    solution_rand = np.linalg.solve(A_rand, B_rand)
    print("Random solution:", solution_rand)
except np.linalg.LinAlgError:
    print("Matrix is singular, cannot solve.")
