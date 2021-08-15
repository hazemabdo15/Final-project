import pygame
screen_height = 500
screen_width = screen_height
MAP_size = 7
tile_size = int(screen_width / MAP_size)
pygame.init()
win = pygame.display.set_mode((screen_width, screen_height))
print(win)


MAP = (
    '#######'
    '#     #'
    '#  c  #'
    '#     b'
    '#     #'
    '#m    #'
    '#######'
)
def draw_map():
    for rows in range(7):
        for columns in range(7):
            #calculate square index
            square = rows * MAP_size + columns
            #draw map in game window
            pygame.draw.rect(
                win,
                ((0, 89, 179) if MAP[square] == "#" else (255, 255, 255)),
                (columns * tile_size, rows * tile_size, tile_size - 2, tile_size - 2)
            )
            if MAP[square] == "b":
                pygame.draw.rect(win, (0, 128, 0), (columns * tile_size, rows * tile_size, tile_size - 2, tile_size - 2))
            if MAP[square] == "c":
                pygame.draw.rect(win, (255, 0, 255),
                                 (columns * tile_size, rows * tile_size, tile_size - 2, tile_size - 2))
            if MAP[square] == "m":
                pygame.draw.rect(win, (160, 160, 160),
                                 (columns * tile_size, rows * tile_size, tile_size - 2, tile_size - 2))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        draw_map()
        pygame.display.update()
