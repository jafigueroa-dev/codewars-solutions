def iq_test(n):
    e_o = ['1' for i in n.split() if int(i) % 2 != 0]
    return int(''.join(str(i) if len(e_o) == 1 and int(j) % 2 != 0 else str(i) if len(e_o) > 1 and int(j) % 2 == 0 else '' for i, j in enumerate(n.split(), 1)))