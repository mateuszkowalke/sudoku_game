def check_if_possible(board, x, y, num):
    row = board[x]
    column = [board[row][y] for row in range(8)]
    grid = [board[row][col]
            for row in range(x//3*3, x//3*3+3) for col in range(y//3*3, y//3*3+3)]
    return num not in grid and num not in row and num not in column


def solve(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for num in range(1, 10):
                    if check_if_possible(board, x, y, num):
                        board[x][y] = num
                        solve(board)
                        board[x][y] = 0
                return
    print(board)
    return board


def check_solution(board):
    for x in range(9):
        for y in range(9):
            if not check_if_possible(board, x, y, board[x][y]):
                return False
    return True


example_board = [
    [0, 1, 3, 4, 2, 0, 0, 8, 6],
    [2, 0, 4, 6, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 1, 0, 3, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 0, 0],
    [0, 6, 2, 5, 0, 0, 0, 0, 3],
    [5, 0, 0, 7, 6, 4, 0, 9, 1],
    [7, 0, 0, 0, 4, 0, 8, 1, 0],
    [0, 4, 0, 8, 0, 0, 0, 6, 0],
    [0, 0, 1, 2, 5, 6, 0, 3, 7]
]

empty_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

solve(example_board)
