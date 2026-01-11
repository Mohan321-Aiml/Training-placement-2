def even_odd(num):
    if num % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"
# Taking input from the user
num = int(input("Enter a number: "))
print(even_odd(num))
