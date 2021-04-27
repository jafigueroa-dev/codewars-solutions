def high(x):
    return max(x.split(), key=lambda i:sum(ord(j) - 96 for j in i))