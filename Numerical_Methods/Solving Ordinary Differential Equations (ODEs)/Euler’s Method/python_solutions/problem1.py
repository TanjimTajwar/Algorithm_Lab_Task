import numpy as np

def euler_method(h, x0, y0, target_x):
    x = x0
    y = y0
    
    print("Euler's Method Solution for Problem 1")
    print("y' = x + y, y(0) = 1")
    print(f"Step size (h) = {h}")
    print("\nx\t\ty\t\tExact\t\tError")
    print("----------------------------------------")
    
    while x <= target_x:
        # Calculate exact solution: y = 2e^x - x - 1
        exact = 2 * np.exp(x) - x - 1
        error = abs(exact - y)
        
        print(f"{x:.4f}\t\t{y:.4f}\t\t{exact:.4f}\t\t{error:.4f}")
        
        if x == target_x:
            break
            
        # Calculate next y using Euler's method
        slope = x + y  # f(x,y) = x + y
        y = y + h * slope
        x = x + h

if __name__ == "__main__":
    h = 0.1      # Step size
    x0 = 0.0     # Initial x
    y0 = 1.0     # Initial y
    target_x = 0.5  # Target x value
    
    euler_method(h, x0, y0, target_x) 