import numpy as np

def f(x, y):
    return x + y*y  # y' = x + y^2

def rk4(x0, y0, h, target_x):
    x = x0
    y = y0
    
    while x < target_x:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
    
    return y

def main():
    x0 = 0
    y0 = 1
    h = 0.1
    target_x = 0.3
    
    result = rk4(x0, y0, h, target_x)
    print(f"Solution at x = {target_x:.1f}: y = {result:.6f}")
    
    # Note: This problem doesn't have a simple exact solution
    print("Note: This problem doesn't have a simple exact solution")

if __name__ == "__main__":
    main() 