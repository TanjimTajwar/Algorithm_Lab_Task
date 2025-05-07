import numpy as np

def simplex(c, A, b):
   

    m, n = A.shape  # m = number of constraints, n = number of variables

    # Add slack variables to convert inequalities to equalities
    A = np.concatenate((A, np.eye(m)), axis=1)
    c = np.concatenate((c, np.zeros(m)), axis=0)

    # Initial basic feasible solution (assuming no constraints are <= 0)
    x = np.zeros(n + m)

    # Add a small positive value to the objective function to ensure maximization
    c = c + 1e-6

    # Simplex Algorithm
    iteration = 0
    while True:
        iteration += 1

        # Find entering variable (most negative coefficient in the objective row)
        entering_var = np.argmin(c[n:])

        if entering_var == -1:
            break  # Optimal solution found

        # Find leaving variable (minimum ratio test)
        ratios = []
        for i in range(m):
            if A[i, entering_var] > 0:
                ratios.append((b[i] / A[i, entering_var]))
            else:
                ratios.append(np.inf) # Avoid division by zero or negative ratios

        min_ratio = np.min(ratios)
        leaving_var = np.argmin(ratios)

        # Check for unboundedness
        if np.isinf(min_ratio):
            print("Problem is unbounded.")
            return None, None

        # Pivot
        pivot_element = A[leaving_var, entering_var]
        A[leaving_var, :] = A[leaving_var, :] / pivot_element
        c = c / pivot_element
        b = b / pivot_element

        # Update basis
        basis = [leaving_var] + list(range(n, n+m))

    # Extract optimal solution
    x = np.zeros(n + m)
    for i in range(n + m):
        if i in basis:
            x[i] = b[i]

    return x, c[n:]


if __name__ == '__main__':
    # Example usage:
    # Maximize: 3x1 + 2x2
    # Subject to:
    #   x1 + x2 <= 4
    #   2x1 + x2 <= 8
    #   x1, x2 >= 0

    c = np.array([3, 2])
    A = np.array([[1, 1], [2, 1]])
    b = np.array([4, 8])

    x, optimal_value = simplex(c, A, b)

    if x is not None and optimal_value is not None:
        print("Optimal solution:", x)
        print("Optimal value:", optimal_value)
    else:
        print("No solution found.")
