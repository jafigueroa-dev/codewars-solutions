def next_smaller(number):
    number_to_string = str(number)
    for i in range(2, len(number_to_string) + 1):
        p = sorted(number_to_string[-i+1:])[::-1]
        for j in range(len(p)):
            if p[j] < number_to_string[-i]:
                s = number_to_string[:-i] + p[j]
                p.pop(j)
                p.append(number_to_string[-i])
                s += "".join(sorted(p)[::-1])
                if s[0] == "0":
                    return -1
                else:
                    return int(s)
    return -1