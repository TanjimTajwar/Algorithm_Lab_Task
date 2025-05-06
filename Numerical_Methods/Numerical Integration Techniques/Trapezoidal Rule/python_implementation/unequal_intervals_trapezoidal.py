import numpy as np

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

if __name__ == "__main__":
    # Example usage
    x_unequal = np.array([0, 0.1, 0.3, 0.6, 1.0])
    y_unequal = x_unequal**2
    result = unequal_intervals_trapezoidal_rule(x_unequal, y_unequal)
    print(f"Unequal Intervals result: {result}") 