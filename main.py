import gui
import sys
import pygame
import csv
import random
from messages import polish as messages
from logic import Board

pygame.init()


def get_new_board():
    with open('sudoku.csv', newline='') as f:
        quizzes = list(csv.reader(f, delimiter=','))
        quiz = quizzes[random.randint(0, len(quizzes)-1)]
        board = []
        for x in range(0, 73, 9):
            row = []
            for y in range(0, 9):
                row += [int(quiz[0][x+y])]
            board += [row]
    return board


SIZE = WIDTH, HEIGHT = 594, 594
TILE_SIZE = TILE_WIDTH, TILE_HEIGHT = (WIDTH-54)/9, (HEIGHT-54)/9
WHITE = 255, 255, 255
LIGHT_GREY = 216, 216, 216
GREY = 156, 156, 156
DARK_GREY = 128, 128, 128
BLACK = 0, 0, 0
FONT = pygame.font.SysFont('arial', 20)
selected_tile = False
message = messages['welcome']

SCREEN = pygame.display.set_mode(SIZE)


board = Board(get_new_board())
board.lock_tiles()
start_new_game = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = int(event.pos[0]//(TILE_WIDTH+6))
            y = int(event.pos[1]//(TILE_HEIGHT+6))
            selected_tile = False if selected_tile == (x, y) else (x, y)
        if event.type == pygame.KEYDOWN:
            if event.unicode == '\r':
                message = False
            elif event.unicode == '\x1b':
                if board.check_solution():
                    message = messages['success']
                    start_new_game = True
                else:
                    message = messages['fail']
                    start_new_game = True
            else:
                if selected_tile:
                    x, y = selected_tile
                    try:
                        key = int(event.unicode)
                        if key in [n for n in range(1, 10)] and not board.check_if_tile_locked(x, y):
                            board.tiles[x][y] = key
                    except ValueError:
                        message = messages['wrong_key']
    gui.draw_board(board, SCREEN, FONT,
                   TILE_SIZE, selected_tile, WHITE, LIGHT_GREY, BLACK, GREY, DARK_GREY)
    if message:
        gui.draw_center_message(message, WHITE, FONT, BLACK,
                                SCREEN)
    pygame.display.update()
    if start_new_game:
        board.new_board(get_new_board())
        start_new_game = False
