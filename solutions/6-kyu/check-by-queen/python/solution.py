def check(board):
    q = [(i, k) for i, j in enumerate(board) for k, h in enumerate(j) if h == 'q'][0]
    k = [(i, k) for i, j in enumerate(board) for k, h in enumerate(j) if h == 'k'][0]
    return q[0] == k[0] or q[1] == k[1] or abs(q[0] - k[0]) == abs(q[1] - k[1])
