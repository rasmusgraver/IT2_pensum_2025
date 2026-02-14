import pygame as pg
from constants import *
from rutenett import Rutenett

# Setter opp rutenettet vårt:
rutenett = Rutenett(30, 40)
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


    vindu.fill(WHITE)
    rutenett.draw(vindu)

    # 5 ganger per sekund:
    if framecounter % (FPS//5) == 0:
        rutenett.skogbrann()


    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame:
pg.quit()
