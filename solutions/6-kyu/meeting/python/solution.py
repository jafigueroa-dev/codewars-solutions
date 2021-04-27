def meeting(s):
    return ''.join(sorted('(' + ', '.join(i.split(':')[::-1]) + ')' for i in s.upper().split(';')))
    