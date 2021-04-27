def row_sum_odd_numbers(n):
    return sum(x for x in range((n**2 - n) + 1, (n**2 + n) + 1, 2))