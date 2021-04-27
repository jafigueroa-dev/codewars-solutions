def tribonacci(sig, n):
    a, b, c = sig
    output = []
    for i in range(n):
        output.append(a)
        a, b, c = b, c, a+b+c
    return output
    