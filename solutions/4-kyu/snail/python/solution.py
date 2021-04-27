def snail(snail_map):
    result = []
    while(len(snail_map) > 0):
        for x in snail_map[0]:
            result.append(x)
        snail_map.pop(0)
        if snail_map:
            for x in snail_map:
                result.append(x[-1])
                del x[-1]
        if snail_map:
            for x in reversed(snail_map[-1]):
                result.append(x)
            snail_map.pop(-1)
        if snail_map:
            for x in reversed(snail_map):
                result.append(x[0])
                del x[0]
    return result
    pass