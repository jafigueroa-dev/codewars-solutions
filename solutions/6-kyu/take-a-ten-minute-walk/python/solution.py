def is_valid_walk(walk):
    iswalk = False
    n, s, e, w = walk.count('n'), walk.count('s'), walk.count('e'), walk.count('w')
    
    if len(walk) == 10 and n == s and e == w:
        iswalk = True
        
    return iswalk
    pass