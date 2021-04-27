def find_missing_number(n):
    return ((len(n) + 1)*(len(n) + 2) / 2) - sum(n)