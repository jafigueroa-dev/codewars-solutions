def minimum_sum(values, n):
    return sum(x for x in sorted(values)[:n]) if n != 0 else 0

def maximum_sum(values, n):
    return sum(x for x in sorted(values)[-n:]) if n != 0 else 0