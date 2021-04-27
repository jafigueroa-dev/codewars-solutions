def digital_root(n):
    x = str(n)
    while len(x) > 1:
        x = str(sum([int(i) for i in x]))
    return int(x)