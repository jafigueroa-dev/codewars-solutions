def first_non_repeated(s):
    letters = {}
    for i in s:
        keys = letters.keys()
        if i in keys:
            letters[i] += 1
        else:
            letters[i] = 1
    for l in s:
        if l in letters and 1 == letters[l]:
            return l
    return None