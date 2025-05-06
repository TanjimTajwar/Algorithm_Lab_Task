import numpy as np
import time
from basic_trapezoidal_rule import basic_trapezoidal_rule

def multiple_intervals_trapezoidal_rule(f, a: float, b: float, n: int = 10000) -> tuple:
    """
    Implements trapezoidal rule for large number of intervals with performance analysis.
    
    Args:
        f: Function to integrate
        a: Lower limit
        b: Upper limit
        n: Number of intervals (default: 10000)
    
    Returns:
        Tuple of (integral value, execution time)
    """
    start_time = time.time()
    result = basic_trapezoidal_rule(f, a, b, n)
    execution_time = time.time() - start_time
    return result, execution_time

if __name__ == "__main__":
    # Example usage
    def f(x): return x**2
    result, time_taken = multiple_intervals_trapezoidal_rule(f, 0, 1)
    print(f"Multiple Intervals result: {result}")
    print(f"Time taken: {time_taken:.6f} seconds") 