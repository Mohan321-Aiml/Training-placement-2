def is_binary(num):
    while num > 0:
        digit = num % 10
        if digit not in [0, 1]:
            return False
        num = num // 10
    return True
num = int(input("Please enter a number: "))
if is_binary(num):
    print("The number is binary.")
else:
    print("The number is not binary.")
