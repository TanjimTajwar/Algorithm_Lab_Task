import numpy as np

def f(x, y):
    return x*x + y*y  # y' = x^2 + y^2

def rk2(x0, y0, h, target_x):
    x = x0
    y = y0
    
    while x < target_x:
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        
        y = y + (k1 + k2) / 2
        x = x + h
    
    return y

def main():
    x0 = 0
    y0 = 1
    h = 0.2
    target_x = 0.8
    
    result = rk2(x0, y0, h, target_x)
    print(f"Solution at x = {target_x:.1f}: y = {result:.6f}")
    
    # Note: This problem doesn't have a simple exact solution
    print("Note: This problem doesn't have a simple exact solution")

if __name__ == "__main__":
    main() 