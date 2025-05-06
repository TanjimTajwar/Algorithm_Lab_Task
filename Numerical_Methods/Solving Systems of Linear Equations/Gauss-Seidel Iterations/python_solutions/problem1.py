def gauss_seidel():
    # System of equations:
    # 4x + y + z = 7
    # x + 5y + z = 8
    # x + y + 6z = 9
    
    x = y = z = 0.0  # Initial values
    tolerance = 0.0001
    iteration = 0
    converged = False

    print("Gauss-Seidel Iteration Method - Problem 1")
    print(f"Initial values: x = {x}, y = {y}, z = {z}")
    print(f"Tolerance: {tolerance}")
    print("\nIterations:")

    while not converged:
        iteration += 1
        
        # Calculate new values using Gauss-Seidel formula
        x_new = (7 - y - z) / 4
        y_new = (8 - x_new - z) / 5
        z_new = (9 - x_new - y_new) / 6

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