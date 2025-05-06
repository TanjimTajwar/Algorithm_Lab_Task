import numpy as np

def solve_system(A, b):
    n = len(A)
    # Combine A and b into augmented matrix
    aug = np.column_stack((A, b))
    
    # Forward elimination
    for i in range(n):
        # Find pivot
        max_row = i
        for j in range(i + 1, n):
            if abs(aug[j][i]) > abs(aug[max_row][i]):
                max_row = j
        
        # Swap rows
        aug[i], aug[max_row] = aug[max_row].copy(), aug[i].copy()
        
        # Eliminate
        for j in range(i + 1, n):
            factor = aug[j][i] / aug[i][i]
            aug[j] -= factor * aug[i]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (aug[i][-1] - np.dot(aug[i][i+1:n], x[i+1:])) / aug[i][i]
    
    return x

def print_solution(A, b):
    print("Problem 10:")
    print("\nCoefficient Matrix A:")
    print(A)
    print("\nVector b:")
    print(b)
    
    solution = solve_system(A, b)
    print("\nSolution:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x:.4f}")

# Problem 10
A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]], dtype=float)
b = np.array([10, -2, -1], dtype=float)

print_solution(A, b) 