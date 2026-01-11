import sympy as sp

x = sp.Symbol('x')
f = x**3 + 2*x**2 + 5*x + 3  # Define the function
derivative = sp.diff(f, x)  # Compute the derivative

print("Function:", f)
print("Derivative:", derivative)
