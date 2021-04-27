def order(s):
    split_string = s.split()
    result = ['' for i in range(len(split_string))]
    for word in split_string:
        position = next(int(i) for i in word if i.isdigit())
        result[position-1] = word
    return ' '.join(result)