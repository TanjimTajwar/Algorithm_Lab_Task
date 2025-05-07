import numpy as np
def gauss(a,b):
    """
    Perform Gaussian elimination to solve the system of equations represented by the augmented matrix [A|b].
    
    Parameters:
    a (numpy.ndarray): Coefficient matrix.
    b (numpy.ndarray): Constant terms vector.
    
    Returns:
    numpy.ndarray: Solution vector x.
    """
    n = len(b)
    
    # Forward elimination
    for i in range(n):
        # Pivoting
        max_row = np.argmax(np.abs(a[i:, i])) + i
        if a[max_row, i] == 0:
            raise ValueError("Matrix is singular or nearly singular")
        a[[i, max_row]] = a[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
        
        # Elimination
        for j in range(i + 1, n):
            factor = a[j, i] / a[i, i]
            a[j, i:] -= factor * a[i, i:]
            b[j] -= factor * b[i]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
    
    return x


# Example usage
if __name__ == "__main__":
    A = np.array([[3, 2, -4], [2, 3, 3], [5, -3, 1]], dtype=float)
    b = np.array([3, 15, 14], dtype=float)
    
    solution = gauss(A, b)
    print("Solution:", solution)