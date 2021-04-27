def find_uniq(a):
    return next(i for i in set(a) if a.count(i) == 1)