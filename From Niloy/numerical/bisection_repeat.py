import numpy as np

def f(x):
    return x**3 - x - 2  # Example function

def bisection_until_convergence(a, b):
    if f(a) * f(b) >= 0:
        print("Invalid interval: f(a) and f(b) must have opposite signs.")
        return None

    c_old = None
    iteration = 1
    while True:
        c = (a + b) / 2
        print(f"Iteration {iteration}: c = {c:.10f}")
        
        if c == c_old:
            print("Converged: two successive c values are equal.")
            print(iteration)
            return c
        
        if f(c) == 0:
            print("Exact root found.")
            print(iteration)
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c
        iteration += 1

# Example usage
root = bisection_until_convergence(1, 2)
print("Root:", root)
