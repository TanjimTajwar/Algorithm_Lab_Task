import numpy as np

def density(x):
    """Function to calculate ρ(x) = 1 + x^2"""
    return 1 + x**2

def x_density(x):
    """Function to calculate x * ρ(x) for center of mass"""
    return x * density(x)

def simpsons_rule(a, b, n, is_x_density=False):
    """
    Implementation of Simpson's 1/3 Rule
    
    Parameters:
    a : float - Lower limit of integration
    b : float - Upper limit of integration
    n : int - Number of intervals (must be even)
    is_x_density : bool - Whether to use x_density function
    
    Returns:
    float - Approximate value of the integral
    """
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even")
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = x_density(x) if is_x_density else density(x)
    
    # Apply Simpson's 1/3 rule formula
    result = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))
    return result

def main():
    try:
        # Fixed values for this problem
        a = 0.0
        b = 2.0
        n = 6
        
        # Calculate total mass
        total_mass = simpsons_rule(a, b, n)
        
        # Calculate first moment
        first_moment = simpsons_rule(a, b, n, is_x_density=True)
        
        # Calculate center of mass
        center_of_mass = first_moment / total_mass
        
        # Exact value of center of mass
        # For ρ(x) = 1 + x^2, the exact center of mass is at x = 1.5
        exact_value = 1.5
        
        # Calculate error
        error = abs(center_of_mass - exact_value)
        
        # Print results
        print("Center of Mass Calculation using Simpson's 1/3 Rule:")
        print("------------------------------------------------")
        print(f"Number of intervals (n): {n}")
        print(f"Total mass: {total_mass:.10f}")
        print(f"First moment: {first_moment:.10f}")
        print(f"Approximate center of mass: {center_of_mass:.10f}")
        print(f"Exact center of mass: {exact_value:.10f}")
        print(f"Absolute error: {error:.10f}")
        print(f"Relative error: {(error/exact_value)*100:.10f}%")
        
        # Show how accuracy changes with different values of n
        print("\nAccuracy Analysis with Different n Values:")
        print("----------------------------------------")
        for i in range(2, 21, 2):
            mass = simpsons_rule(a, b, i)
            moment = simpsons_rule(a, b, i, is_x_density=True)
            approx = moment / mass
            err = abs(approx - exact_value)
            print(f"n = {i:2d}: Error = {err:.10f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 