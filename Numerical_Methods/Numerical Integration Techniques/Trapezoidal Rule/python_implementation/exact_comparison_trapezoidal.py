import numpy as np
from basic_trapezoidal_rule import basic_trapezoidal_rule

def compare_with_exact(f, exact_integral: float, a: float, b: float, n: int) -> tuple:
    """
    Compares trapezoidal rule result with exact integral value.
    
    Args:
        f: Function to integrate
        exact_integral: Exact value of the integral
        a: Lower limit
        b: Upper limit
        n: Number of intervals
    
    Returns:
        Tuple of (approximate value, absolute error, relative error)
    """
    approx_value = basic_trapezoidal_rule(f, a, b, n)
    abs_error = abs(exact_integral - approx_value)
    rel_error = abs_error / abs(exact_integral)
    return approx_value, abs_error, rel_error

if __name__ == "__main__":
    # Example usage
    def f(x): return x**2
    exact = 1/3  # Exact integral of x^2 from 0 to 1
    result, abs_err, rel_err = compare_with_exact(f, exact, 0, 1, 100)
    print(f"Approximate value: {result}")
    print(f"Absolute error: {abs_err}")
    print(f"Relative error: {rel_err}") 