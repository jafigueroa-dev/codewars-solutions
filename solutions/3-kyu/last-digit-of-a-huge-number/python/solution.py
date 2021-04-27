def last_digit(l):
    p = 1
    for i in range(len(l) - 1, -1, -1):
        if p == 0:
            p = 1
        elif p == 1:
            p = l[i]
        else:
            p = l[i]**(p % 4 + 4)
    return p % 10