import numpy as np

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

if __name__ == "__main__":
    # Example usage
    x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    y = x**2
    result = table_data_trapezoidal_rule(x, y)
    print(f"Table Data result: {result}") 