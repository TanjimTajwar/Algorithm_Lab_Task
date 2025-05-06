import numpy as np

def gauss_seidel():
    # System of equations:
    # 6x + y + z = 10
    # x + 5y + z = 11
    # x + y + 4z = 12
    
    # Initial values
    x = np.array([0.0, 0.0, 0.0])
    tolerance = 0.0001
    iteration = 0
    converged = False

    # Coefficient matrix A and constant vector b
    A = np.array([[6, 1, 1],
                  [1, 5, 1],
                  [1, 1, 4]])
    b = np.array([10, 11, 12])

    print("Gauss-Seidel Iteration Method - Problem 9")
    print(f"Initial values: x = {x[0]}, y = {x[1]}, z = {x[2]}")
    print(f"Tolerance: {tolerance}")
    print("\nIterations:")

    while not converged:
        iteration += 1
        x_old = x.copy()
        
        # Calculate new values using Gauss-Seidel formula
        for i in range(len(x)):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x_old[i+1:])) / A[i, i]

        # Check for convergence
        if np.all(np.abs(x - x_old) < tolerance):
            converged = True

        # Print current iteration
        print(f"Iteration {iteration}: x = {x[0]:.6f}, y = {x[1]:.6f}, z = {x[2]:.6f}")

    print(f"\nSolution converged after {iteration} iterations:")
    print(f"x = {x[0]:.6f}")
    print(f"y = {x[1]:.6f}")
    print(f"z = {x[2]:.6f}")

if __name__ == "__main__":
    gauss_seidel() 