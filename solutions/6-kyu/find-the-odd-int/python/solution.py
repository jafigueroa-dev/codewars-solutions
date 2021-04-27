from collections import Counter 

def find_it(seq):
    cnt = Counter(seq)
    return next(i for i in cnt if cnt[i] % 2)
