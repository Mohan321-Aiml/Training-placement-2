import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c  

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Two real roots:", root1, "and", root2)
elif D == 0:
    root = -b / (2*a)
    print("One real root:", root)
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(abs(D)) / (2*a)
    print("Complex roots:", real_part, "+", imag_part, "i and", real_part, "-", imag_part, "i")
