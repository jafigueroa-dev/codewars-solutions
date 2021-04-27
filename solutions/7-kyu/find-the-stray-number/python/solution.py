def stray(arr):
    return next(i for i in set(arr) if arr.count(i) == 1)