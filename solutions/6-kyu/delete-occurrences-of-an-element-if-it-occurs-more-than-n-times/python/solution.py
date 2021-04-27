def delete_nth(o,e):
    cnt = {}
    res = []
    for i in set(o):
         cnt[i] = 0
    for i in o:
        if cnt[i] < e:
            res.append(i)
            cnt[i] += 1
    return res