import numpy as np

def f(x, y):
    return y*y - x  # y' = y^2 - x

def rk3(x0, y0, h, target_x):
    x = x0
    y = y0
    
    while x < target_x:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h, y - k1 + 2*k2)
        
        y = y + (k1 + 4*k2 + k3) / 6
        x = x + h
    
    return y

def main():
    x0 = 0
    y0 = 0.5
    h = 0.2
    target_x = 0.6
    
    result = rk3(x0, y0, h, target_x)
    print(f"Solution at x = {target_x:.1f}: y = {result:.6f}")
    
    # Note: This problem doesn't have a simple exact solution
    print("Note: This problem doesn't have a simple exact solution")

if __name__ == "__main__":
    main() 