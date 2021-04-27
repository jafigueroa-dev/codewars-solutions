def find_short(s):
    l = s.split()
    return len(min(l, key=len))