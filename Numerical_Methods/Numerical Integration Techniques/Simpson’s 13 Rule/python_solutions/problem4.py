import numpy as np

def f(x):
    """Function to calculate f(x) = π(1-x^2)"""
    return np.pi * (1 - x**2)

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
        a = -1.0
        b = 1.0
        n = 8
        
        # Calculate using Simpson's 1/3 rule
        result = simpsons_rule(a, b, n)
        
        # Exact value of volume of sphere with radius 1 is (4/3)π
        exact_value = (4/3) * np.pi
        
        # Calculate error
        error = abs(result - exact_value)
        
        # Print results
        print("Volume of Sphere using Simpson's 1/3 Rule:")
        print("----------------------------------------")
        print(f"Number of intervals (n): {n}")
        print(f"Approximate volume: {result:.10f}")
        print(f"Exact volume: {exact_value:.10f}")
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