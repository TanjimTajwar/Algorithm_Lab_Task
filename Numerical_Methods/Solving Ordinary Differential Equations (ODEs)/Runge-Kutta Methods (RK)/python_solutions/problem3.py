import numpy as np

def f(x, y):
    return y - x*x  # y' = y - x^2

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
    y0 = 0.5
    h = 0.1
    target_x = 0.3
    
    result = rk4(x0, y0, h, target_x)
    print(f"Solution at x = {target_x:.1f}: y = {result:.6f}")
    
    # Exact solution: y = x^2 + 2x + 2 + (y0-2)e^x
    exact = target_x*target_x + 2*target_x + 2 + (y0-2)*np.exp(target_x)
    print(f"Exact solution: y = {exact:.6f}")
    print(f"Error: {abs(result - exact):.6f}")

if __name__ == "__main__":
    main() 