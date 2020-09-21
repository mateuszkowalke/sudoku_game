import copy
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


class Board():
    def __init__(self, tiles=empty_board):
        self.tiles = copy.deepcopy(tiles)
        self.locked_tiles = []

    def check_if_possible(self, x, y, num):
        row = self.tiles[x]
        column = [self.tiles[row][y] for row in range(8)]
        grid = [self.tiles[row][col]
                for row in range(x//3*3, x//3*3+3) for col in range(y//3*3, y//3*3+3)]
        return num not in grid and num not in row and num not in column

    def solve(self):
        for x in range(9):
            for y in range(9):
                if self.tiles[x][y] == 0:
                    for num in range(1, 10):
                        if self.check_if_possible(x, y, num):
                            self.tiles[x][y] = num
                            not_valid = self.solve()
                            if self.check_solution():
                                return
                            if not_valid:
                                self.tiles[x][y] = 0
                    return True

    def check_solution(self):
        for x in range(9):
            for y in range(9):
                num = self.tiles[x][y]
                if num == 0:
                    return False
                self.tiles[x][y] = 0
                if not self.check_if_possible(x, y, num):
                    return False
                self.tiles[x][y] = num
        return True

    def new_board(self, tiles=empty_board):
        self.tiles = copy.deepcopy(tiles)
        self.lock_tiles()

    def lock_tiles(self):
        self.locked_tiles = []
        for x in range(9):
            for y in range(9):
                if self.tiles[x][y] != 0:
                    self.locked_tiles += [(x, y)]

    def check_if_tile_locked(self, x, y):
        return (x, y) in self.locked_tiles


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

solved_board = [
    [9, 1, 3, 4, 2, 7, 5, 8, 6],
    [2, 5, 4, 6, 8, 3, 1, 7, 9],
    [6, 8, 7, 9, 1, 5, 3, 2, 4],
    [4, 7, 9, 1, 3, 2, 6, 5, 8],
    [1, 6, 2, 5, 9, 8, 7, 4, 3],
    [5, 3, 8, 7, 6, 4, 2, 9, 1],
    [7, 2, 6, 3, 4, 9, 8, 1, 5],
    [3, 4, 5, 8, 7, 1, 9, 6, 2],
    [8, 9, 1, 2, 5, 6, 4, 3, 7]
]

if __name__ == '__main__':
    res = Board(example_board)
    res.solve()
    print(res.tiles)
