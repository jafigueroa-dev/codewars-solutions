def find_missing_letter(c):
    return next(chr(j+1) for i, j in enumerate([ord(i) for i in c]) if ord(c[i+1]) != j + 1)

