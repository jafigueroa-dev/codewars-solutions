def index_equals_value(arr):
    return index_search(arr, 0, len(arr) - 1)

def index_search(a, l, h):
    if (l > h):
        return -1
    m = int((h + l) / 2)
    if(a[m] == m):
        lv = index_search(a, l, m-1)
        return lv if (lv != -1 and lv < m) else m
    if(a[m] > m):
        return index_search(a, l, m-1)
    else:
        return index_search(a, m+1, h)
    return -1