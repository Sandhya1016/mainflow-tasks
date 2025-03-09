def is_valid_sudoku(board):
    def is_valid_unit(unit):
        unit = [num for num in unit if num != '.']
        return len(unit) == len(set(unit))
    def is_valid_row(board):
        for row in board:
            if not is_valid_unit(row):
                return False
        return True
    def is_valid_column(board):
        for col in zip(*board):
            if not is_valid_unit(col):
                return False
        return True
    def is_valid_subgrid(board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_unit(subgrid):
                    return False
        return True
    return is_valid_row(board) and is_valid_column(board) and is_valid_subgrid(board)
sudoku_board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

print(is_valid_sudoku(sudoku_board))
