def capitalize(s):
    return [''.join(c[1].upper() if c[0] % 2 == 0 else c[1] for c in enumerate(s)), ''.join(c[1].upper() if c[0] % 2 != 0 else c[1] for c in enumerate(s))]