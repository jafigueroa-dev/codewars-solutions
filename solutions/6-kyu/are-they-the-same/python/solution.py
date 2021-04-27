def comp(array1, array2):
    return False if array1 == None or array2 == None else sorted([x**2 for x in array1]) == sorted(array2)
    