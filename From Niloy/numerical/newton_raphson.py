import sympy as sp

x=sp.symbols('x')
X=sp.symbols('X')

f=x**3-x-2
f_prime=f.diff(x)
df=sp.lambdify(x,f_prime)

print(f_prime)