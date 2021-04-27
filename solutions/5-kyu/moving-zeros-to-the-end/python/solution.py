def move_zeros(array):
    list1 = []
    list2 = []
    for value in array:
        if isinstance(value, bool) is True:
            list1.append(value)
        elif (isinstance(value, int) or isinstance(value, float)) is True and (value == 0):
            list2.append(value)
        else:
            list1.append(value)
    result = list1 + list2
    return result