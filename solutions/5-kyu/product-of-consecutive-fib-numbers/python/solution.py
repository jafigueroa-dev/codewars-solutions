def productFib(prod):
    a, b = 1, 1
    for i in range(prod):
        if a * b == prod:
            return [a, b, True]
        if a * b > prod:
            return [a, b, False]
        a, b = b, a+b
    if prod == 0:
        return [0, 1, True]
    pass