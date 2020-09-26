import pytest
from ..logic import Board, empty_board, example_board, solved_board


class TestBoard:

    def test_create_board(self):
        board = Board(example_board)
        assert board.tiles == example_board

    def test_solve_board(self):
        board = Board(example_board)
        board.solve()
        assert board.tiles == solved_board

    def test_check_if_possible(self):
        board = Board(example_board)
        assert board.check_if_possible(0, 0, 4) == False
        assert board.check_if_possible(0, 0, 9) == True

    def test_check_solution(self):
        board = Board(solved_board)
        assert board.check_solution()

    def test_new_board(self):
        board = Board(empty_board)
        board.new_board(example_board)
        assert board.tiles == example_board

    def test_lock_tiles(self):
        board = Board(example_board)
        board.lock_tiles()
        assert board.check_if_tile_locked(0, 1)
