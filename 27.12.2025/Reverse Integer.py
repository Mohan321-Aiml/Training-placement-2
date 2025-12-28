def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = int(str(x)[::-1])
    return sign * reversed_x if reversed_x <= 2**31 - 1 else 0
