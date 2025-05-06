import math

def f(x):
    return math.cos(x) - x

def regular_falsi(a, b, tolerance):
    if f(a) * f(b) >= 0:
        print("Initial points must have opposite signs")
        return None
    
    iteration = 0
    while True:
        # Calculate new root using Regular Falsi formula
        c = a - (f(a) * (b - a)) / (f(b) - f(a))
        
        # Print current iteration details
        print(f"Iteration {iteration}:")
        print(f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}")
        print(f"f(a) = {f(a):.6f}, f(b) = {f(b):.6f}, f(c) = {f(c):.6f}")
        print("-" * 50)
        
        # Check if we've reached the desired accuracy
        if abs(f(c)) < tolerance:
            return c
        
        # Update interval
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
            
        iteration += 1

# Initial interval and tolerance
a = 0
b = math.pi/2
tolerance = 0.0001

# Solve the equation
root = regular_falsi(a, b, tolerance)

if root is not None:
    print(f"\nFinal root: {root:.6f}")
    print(f"f(root) = {f(root):.6f}") 