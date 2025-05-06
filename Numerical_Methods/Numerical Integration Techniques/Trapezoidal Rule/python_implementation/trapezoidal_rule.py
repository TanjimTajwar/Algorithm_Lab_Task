import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, List, Tuple
import time

def basic_trapezoidal_rule(f: Callable, a: float, b: float, n: int) -> float:
    """
    Basic implementation of trapezoidal rule for numerical integration.
    
    Args:
        f: Function to integrate
        a: Lower limit
        b: Upper limit
        n: Number of intervals
    
    Returns:
        Approximate integral value
    """
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

def table_data_trapezoidal_rule(x: np.ndarray, y: np.ndarray) -> float:
    """
    Implements trapezoidal rule using table data (x, y values).
    
    Args:
        x: Array of x values
        y: Array of y values
    
    Returns:
        Approximate integral value
    """
    h = x[1] - x[0]
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

def multiple_intervals_trapezoidal_rule(f: Callable, a: float, b: float, n: int = 10000) -> Tuple[float, float]:
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

def compare_with_exact(f: Callable, exact_integral: float, a: float, b: float, n: int) -> Tuple[float, float, float]:
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

def plot_function_and_trapezoids(f: Callable, a: float, b: float, n: int):
    """
    Visualizes the function and trapezoids under the curve.
    
    Args:
        f: Function to plot
        a: Lower limit
        b: Upper limit
        n: Number of intervals
    """
    x = np.linspace(a, b, 1000)
    y = f(x)
    
    # Plot the function
    plt.plot(x, y, 'b-', label='Function')
    
    # Plot trapezoids
    x_trap = np.linspace(a, b, n+1)
    y_trap = f(x_trap)
    
    for i in range(n):
        plt.fill([x_trap[i], x_trap[i], x_trap[i+1], x_trap[i+1]],
                [0, y_trap[i], y_trap[i+1], 0], 'g', alpha=0.3)
    
    plt.grid(True)
    plt.legend()
    plt.title('Trapezoidal Rule Visualization')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def unequal_intervals_trapezoidal_rule(x: np.ndarray, y: np.ndarray) -> float:
    """
    Implements trapezoidal rule for data with unequal x-intervals.
    
    Args:
        x: Array of x values
        y: Array of y values
    
    Returns:
        Approximate integral value
    """
    h = np.diff(x)
    return np.sum(h * (y[:-1] + y[1:]) / 2)

# Example usage
if __name__ == "__main__":
    # Example 1: Basic Trapezoidal Rule
    def f(x): return x**2
    result1 = basic_trapezoidal_rule(f, 0, 1, 100)
    print(f"Basic Trapezoidal Rule result: {result1}")
    
    # Example 2: Table Data
    x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    y = x**2
    result2 = table_data_trapezoidal_rule(x, y)
    print(f"Table Data result: {result2}")
    
    # Example 3: Multiple Intervals
    result3, time3 = multiple_intervals_trapezoidal_rule(f, 0, 1)
    print(f"Multiple Intervals result: {result3}, Time: {time3:.6f} seconds")
    
    # Example 4: Compare with Exact
    exact = 1/3  # Exact integral of x^2 from 0 to 1
    result4, abs_err, rel_err = compare_with_exact(f, exact, 0, 1, 100)
    print(f"Comparison with exact: {result4}")
    print(f"Absolute error: {abs_err}")
    print(f"Relative error: {rel_err}")
    
    # Example 5: Plot
    plot_function_and_trapezoids(f, 0, 1, 10)
    
    # Example 6: Unequal Intervals
    x_unequal = np.array([0, 0.1, 0.3, 0.6, 1.0])
    y_unequal = x_unequal**2
    result6 = unequal_intervals_trapezoidal_rule(x_unequal, y_unequal)
    print(f"Unequal Intervals result: {result6}") 