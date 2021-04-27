def triangle(row):
    p = {'BG':'R','RG':'B','BR':'G','GB':'R','GR':'B','RB':'G'}
    c = [i for i in row]
    while len(c) != 1:
        r = []
        for i in range(len(c) - 1):
            if c[i] is c[i+1]:
                r.append(c[i])
            else:
                r.append(p[c[i] + c[i+1]])
        c = r
    return c[0]