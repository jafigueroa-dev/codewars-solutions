def next_bigger(n):
    s = [int(x) for x in str(n)]
    print(n)
    if n in range(10):
        return -1
    for k in range(len(s)-1,0,-1): 
         if s[k] > s[k-1]: 
             break
    if s[k] <= s[k-1]: 
         return -1
    i = max(i for i in range(1, len(s)) if s[i - 1] < s[i])
    j = max(j for j in range(i, len(s)) if s[j] > s[i - 1])
    s[j], s[i - 1] = s[i - 1], s[j]
    s[i:] = reversed(s[i:])
    return int(''.join(str(t) for t in s))