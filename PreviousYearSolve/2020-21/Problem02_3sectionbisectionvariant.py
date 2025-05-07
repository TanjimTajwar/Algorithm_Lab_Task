import numpy as np

def f1(x):
    return x * np.sin(x)**2 - np.exp(x) + 5

def f2(x):
    return x**2 * np.cos(x) - x**3 + 5

def trisection_method(f, a, b, tol=1e-4, max_iter=100):
    for i in range(max_iter):
        p1 = a + (b - a) / 3
        p2 = a + 2 * (b - a) / 3

        if f(p1) * f(p2) < 0:
            a, b = p1, p2
        elif f(a) * f(p1) < 0:
            b = p1
        else:
            a = p2

        if abs(b - a) < tol:
            return (a + b) / 2, i + 1
    return None, max_iter

root1, steps1 = trisection_method(f1, -2, 3)
root2, steps2 = trisection_method(f2, -1, 3)

print(f"Root of f1 ≈ {root1:.4f} in {steps1} steps")
print(f"Root of f2 ≈ {root2:.4f} in {steps2} steps")
