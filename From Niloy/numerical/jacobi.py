import numpy as np
'''jacobi'''

def jacobi(a, b, x0=None, tol=1e-10, max_iterations=1000):
    """
    Solve the system of linear equations Ax = b using the Jacobi iterative method.

    Parameters:
    a (numpy.ndarray): Coefficient matrix.
    b (numpy.ndarray): Constant terms vector.
    x0 (numpy.ndarray, optional): Initial guess for the solution. If None, a zero vector is used.
    tol (float): Tolerance for convergence.
    max_iterations (int): Maximum number of iterations.

    Returns:
    numpy.ndarray: Solution vector x.
    """
    n = len(b)
    
    if x0 is None:
        x0 = np.zeros(n)
    
    x = np.copy(x0)
    
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        
        for i in range(n):
            sum_ax = np.dot(a[i], x) - a[i, i] * x[i]
            x_new[i] = (b[i] - sum_ax) / a[i, i]
        
        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        
        x = x_new
    
    raise ValueError("Jacobi method did not converge within the maximum number of iterations.")