def gauss_seidel():
    # System of equations:
    # 5x + 2y - z = 10
    # 2x + 6y + z = 12
    # -x + y + 4z = 8
    
    x = y = z = 0.0  # Initial values
    tolerance = 0.0001
    iteration = 0
    converged = False

    print("Gauss-Seidel Iteration Method - Problem 3")
    print(f"Initial values: x = {x}, y = {y}, z = {z}")
    print(f"Tolerance: {tolerance}")
    print("\nIterations:")

    while not converged:
        iteration += 1
        
        # Calculate new values using Gauss-Seidel formula
        x_new = (10 - 2*y + z) / 5
        y_new = (12 - 2*x_new - z) / 6
        z_new = (8 + x_new - y_new) / 4

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