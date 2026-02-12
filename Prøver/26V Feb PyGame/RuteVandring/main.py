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
            # Nullstill frameCounter (Så man har tid til å klikke på flere før animasjonen fortsetter):
            framecounter = 1


    # Hvert sekund (eller oftere...):
    if framecounter % (FPS//2) == 0:
        rutenett.vandring()


    # Tegner objektene våre (på et blankt hvitt lerret):
    vindu.fill(WHITE)
    rutenett.draw(vindu)


    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame:
pg.quit()
