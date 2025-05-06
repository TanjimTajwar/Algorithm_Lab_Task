import numpy as np
import matplotlib.pyplot as plt
from basic_trapezoidal_rule import basic_trapezoidal_rule

def plot_function_and_trapezoids(f, a: float, b: float, n: int):
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
    plt.title('ট্র্যাপিজয়েডাল রুল ভিজুয়ালাইজেশন')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

if __name__ == "__main__":
    # Example usage
    def f(x): return x**2
    plot_function_and_trapezoids(f, 0, 1, 10) 