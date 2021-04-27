def solution(s):
    return [i + j for i, j in zip(s[0::2], s[1::2] + '_')]