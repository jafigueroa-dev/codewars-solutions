from itertools import product

def valid_solution(board):
    DIGITS = set(range(1, 10))
    THREES = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    
    def correct(groups):
        return all(set(group) == DIGITS for group in groups)
    
    rows = board
    columns = zip(*board)
    squares3x3 = [[board[r][c] for r, c in product(row_block, col_block)]
                  for row_block, col_block in product(THREES, THREES)]
    
    return correct(rows) and correct(columns) and correct(squares3x3)
    