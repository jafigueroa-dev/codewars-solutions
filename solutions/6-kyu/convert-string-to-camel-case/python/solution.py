def to_camel_case(t):
    if t:
        lst = t.replace('-',' ').replace('_',' ').split()
        return lst[0] + ''.join(i.title() for i in lst[1:])
    return t