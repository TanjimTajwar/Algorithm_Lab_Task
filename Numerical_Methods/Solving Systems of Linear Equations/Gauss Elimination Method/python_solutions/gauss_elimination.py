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

def print_solution(problem_num, A, b):
    print(f"\nProblem {problem_num}:")
    print("Coefficient Matrix A:")
    print(A)
    print("\nVector b:")
    print(b)
    solution = solve_system(A, b)
    print("\nSolution:")
    for i, val in enumerate(solution):
        print(f"x{i+1} = {val:.4f}")

# Problem 1
A1 = np.array([[2, 1, -1],
               [-3, -1, 2],
               [-2, 1, 2]], dtype=float)
b1 = np.array([8, -11, -3], dtype=float)
print_solution(1, A1, b1)

# Problem 2
A2 = np.array([[1, 2, 3],
               [2, 5, 2],
               [3, 1, 5]], dtype=float)
b2 = np.array([14, 18, 20], dtype=float)
print_solution(2, A2, b2)

# Problem 3
A3 = np.array([[4, 3, 2],
               [-2, 2, 3],
               [3, -5, 2]], dtype=float)
b3 = np.array([25, -10, -4], dtype=float)
print_solution(3, A3, b3)

# Problem 4
A4 = np.array([[2, -1, 3],
               [1, 1, 1],
               [1, -1, 1]], dtype=float)
b4 = np.array([9, 6, 2], dtype=float)
print_solution(4, A4, b4)

# Problem 5
A5 = np.array([[3, 2, -1],
               [2, -2, 4],
               [-1, 0.5, -1]], dtype=float)
b5 = np.array([10, -2, -1], dtype=float)
print_solution(5, A5, b5)

# Problem 6
A6 = np.array([[1, 1, 1],
               [2, 3, 4],
               [3, 4, 5]], dtype=float)
b6 = np.array([6, 20, 30], dtype=float)
print_solution(6, A6, b6)

# Problem 7
A7 = np.array([[2, 3, -1],
               [4, 4, -3],
               [-2, 3, -1]], dtype=float)
b7 = np.array([5, 3, 1], dtype=float)
print_solution(7, A7, b7)

# Problem 8
A8 = np.array([[1, 2, 3],
               [2, 5, 2],
               [6, -3, 1]], dtype=float)
b8 = np.array([6, 4, 2], dtype=float)
print_solution(8, A8, b8)

# Problem 9
A9 = np.array([[2, -1, 3],
               [3, 1, 2],
               [1, -3, 2]], dtype=float)
b9 = np.array([9, 11, 5], dtype=float)
print_solution(9, A9, b9)

# Problem 10
A10 = np.array([[1, 1, 1],
                [2, 3, 1],
                [3, 5, 2]], dtype=float)
b10 = np.array([3, 6, 11], dtype=float)
print_solution(10, A10, b10) 