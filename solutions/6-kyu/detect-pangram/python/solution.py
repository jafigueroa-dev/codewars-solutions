import string

def is_pangram(s):
    a = set('abcdefghijklmnopqrstuvwxyz')
    return set(''.join(filter(a.__contains__, s.lower()))) >= a