import numpy as np

def euler_method(h, x0, y0, target_x):
    x = x0
    y = y0
    
    print("Euler's Method Solution for Problem 10")
    print("y' = 2y - x, y(0) = 1")
    print(f"Step size (h) = {h}")
    print("\nx\t\ty\t\tExact\t\tError")
    print("----------------------------------------")
    
    while x <= target_x:
        # Calculate exact solution: y = (x/2 + 1/4) + (3/4)e^(2x)
        exact = (x/2 + 0.25) + 0.75 * np.exp(2*x)
        error = abs(exact - y)
        
        print(f"{x:.4f}\t\t{y:.4f}\t\t{exact:.4f}\t\t{error:.4f}")
        
        if x == target_x:
            break
            
        # Calculate next y using Euler's method
        slope = 2*y - x  # f(x,y) = 2y - x
        y = y + h * slope
        x = x + h

if __name__ == "__main__":
    h = 0.1      # Step size
    x0 = 0.0     # Initial x
    y0 = 1.0     # Initial y
    target_x = 0.4  # Target x value
    
    euler_method(h, x0, y0, target_x) 