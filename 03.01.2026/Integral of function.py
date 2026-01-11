import sympy as sp

x = sp.Symbol('x')
f = x**2 + 3*x + 1  # Define the function
integral = sp.integrate(f, x)  # Compute the integral

print("Function:", f)
print("Integral:", integral, "+ C")  # Add constant of integration
