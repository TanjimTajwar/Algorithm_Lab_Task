import numpy as np

def f(x):
    """Function to calculate f(x) = x^2"""
    return x**2

def simpsons_rule(a, b, n):
    """
    Implementation of Simpson's 1/3 Rule
    
    Parameters:
    a : float - Lower limit of integration
    b : float - Upper limit of integration
    n : int - Number of intervals (must be even)
    
    Returns:
    float - Approximate value of the integral
    """
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even")
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    # Apply Simpson's 1/3 rule formula
    result = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))
    return result

def main():
    try:
        # Fixed values for this problem
        a = 0.0
        b = 1.0
        n = 4
        
        # Calculate using Simpson's 1/3 rule
        result = simpsons_rule(a, b, n)
        
        # Exact value of ∫x^2 dx from 0 to 1 is 1/3
        exact_value = 1/3
        
        # Calculate error
        error = abs(result - exact_value)
        
        # Print results
        print("Simpson's 1/3 Rule Results:")
        print("---------------------------")
        print(f"Number of intervals (n): {n}")
        print(f"Approximate value: {result:.10f}")
        print(f"Exact value: {exact_value:.10f}")
        print(f"Absolute error: {error:.10f}")
        print(f"Relative error: {(error/exact_value)*100:.10f}%")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 