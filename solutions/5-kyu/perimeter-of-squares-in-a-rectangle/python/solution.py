def perimeter(n):
    fibonacci_sum = 0
    count = 0
    x, y, z = 0, 1, 1
    while(n+1 > count):
        fibonacci_sum = fibonacci_sum + z
        z = x + y
        x = y
        y = z
        count += 1
    return 4 * fibonacci_sum