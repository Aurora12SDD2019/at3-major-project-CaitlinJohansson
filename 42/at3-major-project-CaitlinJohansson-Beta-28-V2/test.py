import pygame as P
from mods import *

block_grp = P.sprite.Group()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color_array = [RED, GREEN, BLUE,RED, GREEN, BLUE, RED, GREEN, BLUE]
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 900, 550  # sets size of screen/window
Screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen

for c in color_array:
    b = Block(Screen, c)
    block_grp.add(b)

block2 = Block(Screen, YELLOW)

collide_list = P.sprite.spritecollide(block2, block_grp, False)
print(block2.x, block2.y)
for b in collide_list:
    print(b.x, b.y, b.rect.height)
    print(P.sprite.collide_rect(b, block2))
    print(b.rect.height)
          


