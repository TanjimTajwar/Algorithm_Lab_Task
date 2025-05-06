import numpy as np

def euler_method(h, x0, y0, target_x):
    x = x0
    y = y0
    
    print("Euler's Method Solution for Problem 6")
    print("y' = x^2 + y^2, y(0) = 0")
    print(f"Step size (h) = {h}")
    print("\nx\t\ty")
    print("----------------------------------------")
    
    while x <= target_x:
        # Note: This problem doesn't have a simple exact solution
        # We'll just show the numerical solution
        print(f"{x:.4f}\t\t{y:.4f}")
        
        if x == target_x:
            break
            
        # Calculate next y using Euler's method
        slope = x**2 + y**2  # f(x,y) = x^2 + y^2
        y = y + h * slope
        x = x + h

if __name__ == "__main__":
    h = 0.1      # Step size
    x0 = 0.0     # Initial x
    y0 = 0.0     # Initial y
    target_x = 0.3  # Target x value
    
    euler_method(h, x0, y0, target_x) 