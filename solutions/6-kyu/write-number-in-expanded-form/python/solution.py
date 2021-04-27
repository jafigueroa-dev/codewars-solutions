def expanded_form(num):
    return ' + '.join(x[1] + '0' * (x[0] - 1) for x in zip(range(len(str(num)), -1, -1), str(num)) if int(x[1]) != 0)