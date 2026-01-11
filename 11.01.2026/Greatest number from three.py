n1 = int(input("Please enter the first number (n1): "))
n2 = int(input("Please enter the second number (n2): "))
n3 = int(input("Please enter the third number (n3): "))
if n1 >= n2 and n1 >= n3:
    print("n1 is the greatest")
elif n2 >= n1 and n2 >= n3:
    print("n2 is the greatest")
else:
    print("n3 is the greatest")
