def find(n):
    l, x, y, c = [0, 1, 2, 2], 5, 4, 3
    if n <= 3:
        return l[n]
    while c < n + 1:
        x += c * l[c]
        if x >= n:
            z = (x - n) // c
            return y + l[c] - (z + 1)
        y += l[c]
        if y < 70000:
            l += [c] * l[c]
        c += 1