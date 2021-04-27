import itertools

def permutations(s):
    return set([''.join(i) for i in itertools.permutations(s)])