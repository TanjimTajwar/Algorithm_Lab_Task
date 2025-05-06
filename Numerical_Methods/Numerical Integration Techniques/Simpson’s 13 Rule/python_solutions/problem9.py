import numpy as np

def density(x):
    """Function to calculate ρ(x) = x^2"""
    return x**2

def x_squared_density(x):
    """Function to calculate x^2 * ρ(x) for moment of inertia"""
    return x**2 * density(x)

def simpsons_rule(a, b, n, is_x_squared_density=False):
    """
    Implementation of Simpson's 1/3 Rule
    
    Parameters:
    a : float - Lower limit of integration
    b : float - Upper limit of integration
    n : int - Number of intervals (must be even)
    is_x_squared_density : bool - Whether to use x_squared_density function
    
    Returns:
    float - Approximate value of the integral
    """
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even")
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = x_squared_density(x) if is_x_squared_density else density(x)
    
    # Apply Simpson's 1/3 rule formula
    result = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))
    return result

def main():
    try:
        # Fixed values for this problem
        a = 0.0
        b = 1.0
        n = 6
        
        # Calculate total mass
        total_mass = simpsons_rule(a, b, n)
        
        # Calculate moment of inertia
        moment_of_inertia = simpsons_rule(a, b, n, is_x_squared_density=True)
        
        # Exact value of moment of inertia
        # For ρ(x) = x^2, the exact moment of inertia is 1/6
        exact_value = 1/6
        
        # Calculate error
        error = abs(moment_of_inertia - exact_value)
        
        # Print results
        print("Moment of Inertia Calculation using Simpson's 1/3 Rule:")
        print("----------------------------------------------------")
        print(f"Number of intervals (n): {n}")
        print(f"Total mass: {total_mass:.10f}")
        print(f"Approximate moment of inertia: {moment_of_inertia:.10f}")
        print(f"Exact moment of inertia: {exact_value:.10f}")
        print(f"Absolute error: {error:.10f}")
        print(f"Relative error: {(error/exact_value)*100:.10f}%")
        
        # Show how accuracy changes with different values of n
        print("\nAccuracy Analysis with Different n Values:")
        print("----------------------------------------")
        for i in range(2, 21, 2):
            approx = simpsons_rule(a, b, i, is_x_squared_density=True)
            err = abs(approx - exact_value)
            print(f"n = {i:2d}: Error = {err:.10f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 