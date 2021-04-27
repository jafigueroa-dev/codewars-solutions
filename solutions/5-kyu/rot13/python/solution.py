def rot13(m):
    return ''.join(chr((ord(i) + 13 - 97) % 26 + 97) if i.islower() else chr((ord(i) + 13 - 65) % 26 + 65) if i.isupper() else i for i in m)
