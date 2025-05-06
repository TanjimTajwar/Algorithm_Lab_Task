def gauss_seidel():
    # System of equations:
    # 3x - y + z = 4
    # -x + 4y + 2z = 5
    # x + 2y + 5z = 6
    
    x = y = z = 1.0  # Initial values
    tolerance = 0.001
    iteration = 0
    converged = False

    print("Gauss-Seidel Iteration Method - Problem 2")
    print(f"Initial values: x = {x}, y = {y}, z = {z}")
    print(f"Tolerance: {tolerance}")
    print("\nIterations:")

    while not converged:
        iteration += 1
        
        # Calculate new values using Gauss-Seidel formula
        x_new = (4 + y - z) / 3
        y_new = (5 + x_new - 2*z) / 4
        z_new = (6 - x_new - 2*y_new) / 5

        # Check for convergence
        if (abs(x_new - x) < tolerance and
            abs(y_new - y) < tolerance and
            abs(z_new - z) < tolerance):
            converged = True

        # Update values
        x, y, z = x_new, y_new, z_new

        # Print current iteration
        print(f"Iteration {iteration}: x = {x:.6f}, y = {y:.6f}, z = {z:.6f}")

    print(f"\nSolution converged after {iteration} iterations:")
    print(f"x = {x:.6f}")
    print(f"y = {y:.6f}")
    print(f"z = {z:.6f}")

if __name__ == "__main__":
    gauss_seidel() 