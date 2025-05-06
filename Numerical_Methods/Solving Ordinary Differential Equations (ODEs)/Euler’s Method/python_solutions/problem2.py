import numpy as np

def euler_method(h, x0, y0, target_x):
    x = x0
    y = y0
    
    print("Euler's Method Solution for Problem 2")
    print("y' = 2x - y, y(0) = 1")
    print(f"Step size (h) = {h}")
    print("\nx\t\ty\t\tExact\t\tError")
    print("----------------------------------------")
    
    while x <= target_x:
        # Calculate exact solution: y = 2x - 2 + 3e^(-x)
        exact = 2 * x - 2 + 3 * np.exp(-x)
        error = abs(exact - y)
        
        print(f"{x:.4f}\t\t{y:.4f}\t\t{exact:.4f}\t\t{error:.4f}")
        
        if x == target_x:
            break
            
        # Calculate next y using Euler's method
        slope = 2 * x - y  # f(x,y) = 2x - y
        y = y + h * slope
        x = x + h

if __name__ == "__main__":
    h = 0.2      # Step size
    x0 = 0.0     # Initial x
    y0 = 1.0     # Initial y
    target_x = 1.0  # Target x value
    
    euler_method(h, x0, y0, target_x) 