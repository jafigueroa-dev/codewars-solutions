from collections import Counter

def scramble(s1, s2):
    s1_data = Counter(s1)
    s2_data = Counter(s2)
    for i in set(s2):
        if s1_data[i] < s2_data[i]:
            return False
        if i not in s1:
            return False
    return True