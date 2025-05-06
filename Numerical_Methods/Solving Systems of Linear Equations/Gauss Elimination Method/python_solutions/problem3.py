import numpy as np

def solve_system(A, b):
    # Combine A and b into augmented matrix
    augmented = np.column_stack((A, b))
    n = len(A)
    
    # Forward elimination
    for i in range(n):
        # Find pivot
        max_row = i
        for j in range(i + 1, n):
            if abs(augmented[j, i]) > abs(augmented[max_row, i]):
                max_row = j
        
        # Swap rows
        augmented[i], augmented[max_row] = augmented[max_row].copy(), augmented[i].copy()
        
        # Eliminate
        for j in range(i + 1, n):
            factor = augmented[j, i] / augmented[i, i]
            augmented[j] -= factor * augmented[i]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented[i, -1] - np.dot(augmented[i, i+1:n], x[i+1:])) / augmented[i, i]
    
    return x

def print_solution(A, b):
    print("Problem 3:")
    print("Coefficient Matrix A:")
    print(A)
    print("\nVector b:")
    print(b)
    solution = solve_system(A, b)
    print("\nSolution:")
    for i, val in enumerate(solution):
        print(f"x{i+1} = {val:.4f}")

# Problem 3
A = np.array([[4, 3, 2],
              [-2, 2, 3],
              [3, -5, 2]], dtype=float)
b = np.array([25, -10, -4], dtype=float)
print_solution(A, b) 