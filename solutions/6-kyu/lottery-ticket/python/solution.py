def bingo(ticket, win):
    cnt = 0
    for i in ticket:
        for j in i[0]:
            if ord(j) == i[1]:
                cnt += 1
    return 'Winner!' if cnt >= win else 'Loser!'