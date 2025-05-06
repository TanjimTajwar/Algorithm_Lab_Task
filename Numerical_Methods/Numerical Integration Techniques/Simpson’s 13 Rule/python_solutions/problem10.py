import numpy as np

def f1(x):
    """Function to calculate f(x) = x^2"""
    return x**2

def f2(x):
    """Function to calculate g(x) = x^3"""
    return x**3

def difference(x):
    """Function to calculate |f1(x) - f2(x)|"""
    return np.abs(f1(x) - f2(x))

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
    y = difference(x)
    
    # Apply Simpson's 1/3 rule formula
    result = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))
    return result

def main():
    try:
        # Fixed values for this problem
        a = 0.0
        b = 1.0
        n = 8
        
        # Calculate using Simpson's 1/3 rule
        result = simpsons_rule(a, b, n)
        
        # Exact value of area between curves
        # For y = x^2 and y = x^3, the exact area is 1/12
        exact_value = 1/12
        
        # Calculate error
        error = abs(result - exact_value)
        
        # Print results
        print("Area Between Curves using Simpson's 1/3 Rule:")
        print("-------------------------------------------")
        print(f"Number of intervals (n): {n}")
        print(f"Approximate area: {result:.10f}")
        print(f"Exact area: {exact_value:.10f}")
        print(f"Absolute error: {error:.10f}")
        print(f"Relative error: {(error/exact_value)*100:.10f}%")
        
        # Show how accuracy changes with different values of n
        print("\nAccuracy Analysis with Different n Values:")
        print("----------------------------------------")
        for i in range(2, 21, 2):
            approx = simpsons_rule(a, b, i)
            err = abs(approx - exact_value)
            print(f"n = {i:2d}: Error = {err:.10f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 