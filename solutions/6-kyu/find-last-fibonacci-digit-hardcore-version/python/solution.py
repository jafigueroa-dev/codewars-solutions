def last_fib_digit(n):
    return [int(((1 + (5 ** 0.5)) / 2) ** i / (5 ** 0.5) + 0.5) % 10 for i in range(1, 61)][n % 60 - 1]