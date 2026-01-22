import pygame as pg
from constants import *
from rutenett import Rutenett
import random

# Setter opp rutenettet vårt:
rutenett = Rutenett(10,20)
bredde,hoyde = rutenett.getWindowSize()

pg.init()
vindu = pg.display.set_mode( (bredde, hoyde) )
clock = pg.time.Clock()


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
