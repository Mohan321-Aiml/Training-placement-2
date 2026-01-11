import sympy as sp

x = sp.Symbol('x')
f = x**2 + 2*x  # Define the function
a, b = 1, 3  # Define limits

definite_integral = sp.integrate(f, (x, a, b))
print("Definite Integral from", a, "to", b, "is:", definite_integral)
