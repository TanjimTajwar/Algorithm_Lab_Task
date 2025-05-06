import numpy as np

def f(x, y):
    return np.exp(x) - y  # y' = e^x - y

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
    y0 = 1
    h = 0.2
    target_x = 0.6
    
    result = rk3(x0, y0, h, target_x)
    print(f"Solution at x = {target_x:.1f}: y = {result:.6f}")
    
    # Exact solution: y = (x*e^x + y0)
    exact = target_x*np.exp(target_x) + y0
    print(f"Exact solution: y = {exact:.6f}")
    print(f"Error: {abs(result - exact):.6f}")

if __name__ == "__main__":
    main() 