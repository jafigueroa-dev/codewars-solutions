def dig_pow(n, p):
    dig_sum = sum(int(i)**j for j, i in enumerate(str(n), p)) / n
    return -1 if dig_sum % 1 != 0 else dig_sum