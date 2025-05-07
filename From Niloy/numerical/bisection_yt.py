import math
from datetime import datetime
def f(x):
    return x**3 - 3*x + 5

a = float(input("Enter a: "))
b = float(input("Enter b: "))
z = float(input("Enter z: "))

tolerance = 10**(-z)
n = math.ceil(math.log(abs(b - a) / tolerance) / math.log(2))
t_i=datetime.now()
if f(a) * f(b) > 0:
    print("Invalid interval")
else:
    for i in range(10000):
        c = (a + b) / 2
        if abs(f(c)) < tolerance:  # Check if the function value is close enough to 0
            print(f"Root is {c} at iteration {i}")
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        i += 1  # Increment the iteration count
        print(f"Current approximation: {c} at iteration {i}")
        t_f=datetime.now()

        print(f"Time taken: {t_f - t_i}")
