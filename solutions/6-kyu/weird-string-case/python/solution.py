def to_weird_case(string):
    res = []
    for i in string.split():
        res.append(''.join(k.upper() if j % 2 == 0 else k.lower() for j, k in enumerate(i)))
    return ' '.join(res)