import pygame


def draw_number(n, font, color, screen, position):
    if n == 0:
        n = ''
    surface = font.render(str(n), True, color)
    screen.blit(surface, position)


def draw_board(board, screen, font, tile_size, selected_tile, background_color, tile_color, font_color, selected_tile_color, locked_tile_color):
    screen.fill(background_color)
    for x in range(9):
        for y in range(9):
            if board.check_if_tile_locked(x, y):
                pygame.draw.rect(screen, locked_tile_color, (tile_size[0]*x+6*(x+1)-3,
                                                             tile_size[1]*y+6*(y+1)-3, tile_size[0], tile_size[1]))
            elif selected_tile == (x, y):
                pygame.draw.rect(screen, selected_tile_color, (tile_size[0]*x+6*(x+1)-3,
                                                               tile_size[1]*y+6*(y+1)-3, tile_size[0], tile_size[1]))
            else:
                pygame.draw.rect(screen, tile_color, (tile_size[0]*x+6*(x+1)-3,
                                                      tile_size[1]*y+6*(y+1)-3, tile_size[0], tile_size[1]))
            num = board.tiles[x][y]
            draw_number(num, font, font_color, screen, (tile_size[0]*x+6*(x+1)-3+(tile_size[0]-font.size(str(num))[0])/2,
                                                        tile_size[1]*y+6*(y+1)-3+(tile_size[1]-font.size(str(num))[1])/2))
    for x in range(4):
        pygame.draw.line(
            screen, font_color, (0, x*3*tile_size[1]+x*18-1), (screen.get_width(), x*3*tile_size[1]+x*18-1), 2)
    for y in range(4):
        pygame.draw.line(
            screen, font_color, (y*3*tile_size[1]+y*18-1, 0), (y*3*tile_size[1]+y*18-1, screen.get_height()), 2)


def draw_center_message(message, background_color, font, font_color, screen):
    width = 0
    height = 0
    for i, line in enumerate(message):
        size = font.size(line)
        width = size[0] if size[0] > width else width
        height += size[1]
    screen_size = screen.get_size()
    position = ((screen_size[0]-width)//2-20, (screen_size[1]-height)//2-20)
    pygame.draw.rect(screen, background_color,
                     (position[0], position[1], width+40, height+40))
    for i, line in enumerate(message):
        size = font.size(line)
        position = ((screen_size[0]-size[0])//2,
                    (screen_size[1]-size[1]*len(message))//2+size[1]*i)
        surface = font.render(line, True, font_color)
        screen.blit(surface, position)
