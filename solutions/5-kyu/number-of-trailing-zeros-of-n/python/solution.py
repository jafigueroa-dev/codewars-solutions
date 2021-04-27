def zeros(n):
    x = 0
    y = 5
    while (n / y >= 1): 
        x += int(n / y) 
        y *= 5
    return int(x)