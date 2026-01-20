import pygame as pg
from constants import *


pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

rutenett = [
    [WHITE, WHITE, BLACK], 
    [BLACK, WHITE, GREEN], 
    [WHITE, RED, BLUE], 
]
CELLE_STR = 40
ANT_RADER = 3
ANT_KOLONNER = 3


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    vindu.fill(WHITE)

    for rad in range(ANT_RADER):
        for kolonne in range(ANT_KOLONNER):
            pg.draw.rect(vindu, rutenett[rad][kolonne], (kolonne*CELLE_STR, rad*CELLE_STR, CELLE_STR, CELLE_STR))
            pg.draw.rect(vindu, GREY, (kolonne*CELLE_STR, rad*CELLE_STR, CELLE_STR, CELLE_STR), 2)


    pg.display.flip()
    clock.tick(FPS)

pg.quit()

