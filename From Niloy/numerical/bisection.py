import math

def bisection(func, a, b, tolerance=1e-6, max_iterations=100):
  """
  Implements the bisection method to find a root of a function.

  Args:
    func: The function to find the root of.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    tolerance: The desired accuracy of the root.
    max_iterations: The maximum number of iterations to perform.

  Returns:
    The approximate root of the function, or None if no root is found within
    the specified tolerance and maximum iterations.
  """

  if func(a) * func(b) >= 0:
    print("Function values at endpoints do not have opposite signs.  Bisection method may not converge.")
    return None

  for i in range(max_iterations):
    c = (a + b) / 2
    if abs(func(c)) < tolerance:
      return c
    elif func(a) * func(c) < 0:
      b = c
    else:
      a = c
    if abs(func(c)) < tolerance:
      return c

  print("Bisection method did not converge within the specified tolerance and maximum iterations.")
  return None


# Example usage with trigonometric functions:

def my_function_sin(x):
  return math.sin(x)

def my_function_cos(x):
  return math.cos(x)

# Find the root of sin(x) = 0 in the interval [0, 1]
root_sin = bisection(my_function_sin, .1, .9)

if root_sin is not None:
  print("Approximate root of sin(x) = 0:", root_sin)
else:
  print("Root not found.")

# Find the root of cos(x) = 0 in the interval [0, 1]
root_cos = bisection(my_function_cos, 0, 1)

if root_cos is not None:
  print("Approximate root of cos(x) = 0:", root_cos)
else:
  print("Root not found.")
