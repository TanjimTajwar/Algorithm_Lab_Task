import numpy as np

def f(x):
    return x**3 + 2*x**2 + 3*x + 4

def weddles_rule(f, a, b, n):
    if n % 6 != 0:
        raise ValueError("Number of intervals must be divisible by 6")
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    # Weddle's Rule formula
    sum1 = y[0] + y[-1]  # First and last terms
    sum2 = 5 * np.sum(y[1:-1:6])  # Terms at positions 1,7,13,...
    sum3 = y[2:-1:6] + y[4:-1:6]  # Terms at positions 2,8,14,... and 4,10,16,...
    sum4 = 6 * np.sum(y[3:-1:6])  # Terms at positions 3,9,15,...
    sum5 = 5 * np.sum(y[5:-1:6])  # Terms at positions 5,11,17,...
    
    integral = (3*h/10) * (sum1 + sum2 + np.sum(sum3) + sum4 + sum5)
    return integral

def main():
    a = -2  # Lower limit
    b = 2   # Upper limit
    n = 24  # Number of intervals
    
    result = weddles_rule(f, a, b, n)
    exact_value = (b**4/4 + 2*b**3/3 + 3*b**2/2 + 4*b) - (a**4/4 + 2*a**3/3 + 3*a**2/2 + 4*a)
    error = abs(result - exact_value)
    
    print(f"Approximate value using Weddle's Rule: {result:.6f}")
    print(f"Exact value: {exact_value:.6f}")
    print(f"Absolute error: {error:.6f}")

if __name__ == "__main__":
    main() 