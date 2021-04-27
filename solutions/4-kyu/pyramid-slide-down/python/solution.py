def longest_slide_down(pyramid):
    s = pyramid
    for a in reversed(pyramid):
        for i in range(0, len(a) - 1):
            x = len(s[i+1])
            y = len(s[i])
            diff = max(x, y)
            s[i+1].extend([0] * (diff - x))
            s[i].extend([0] * (diff - y))
    
    for i in range(len(s)-2, -1, -1): 
        for j in range(i+1): 
            if (s[i+1][j] > s[i+1][j+1]): 
                s[i][j] += s[i+1][j] 
            else: 
                s[i][j] += s[i+1][j+1] 
    
    return s[0][0]