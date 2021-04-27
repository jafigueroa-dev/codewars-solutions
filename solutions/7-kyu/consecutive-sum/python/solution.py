def consecutive_sum(n):
    x, y = 1, 1
    for i in range(2, int((2 * n)**0.5) + 1):
        x += i
        y += 1 if (n - x) % i == 0 else 0
    return y