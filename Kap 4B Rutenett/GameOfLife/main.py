import pygame as pg
from constants import *
from rutenett import Rutenett

# Setter opp rutenettet vårt:
rutenett = Rutenett(10,20)
bredde,hoyde = rutenett.getWindowSize()

pg.init()
vindu = pg.display.set_mode( (bredde, hoyde) )
clock = pg.time.Clock()

framecounter = 0
running = True
while running:
    framecounter+=1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mx, my = event.pos
            kolonne = mx // CELLE_STR
            rad = my // CELLE_STR
            rutenett.klikk(rad, kolonne)
            # Nullstill frameCounter:
            framecounter = 1

    vindu.fill(WHITE)
    rutenett.draw(vindu)

    # Hvert sekund:
    if framecounter % FPS == 0:
        rutenett.gameOfLife()


    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame:
pg.quit()
