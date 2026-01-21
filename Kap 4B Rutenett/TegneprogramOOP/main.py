import pygame as pg
from constants import *
from rutenett import Rutenett
import random


pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

# Setter opp rutenettet vårt:
rutenett = Rutenett()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    vindu.fill(WHITE)
    rutenett.draw(vindu)


    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame:
pg.quit()
