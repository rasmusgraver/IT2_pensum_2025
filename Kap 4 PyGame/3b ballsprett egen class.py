import pygame as pg
from ball import Ball
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

def main():
    baller = []
    baller.append( Ball(x=100, y=VINDU_HOYDE, radius=40, farge=BLUE, vx=5, vy=3) )
    baller.append( Ball(x=20, y=100, radius=10, farge=RED, vx=5, vy=20) )
    baller.append( Ball(x=100, y=25, radius=20, farge=GREEN, vx=15, vy=3))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(WHITE)

        for ball in baller:
            ball.oppdater(VINDU_BREDDE, VINDU_HOYDE)
            ball.tegn(vindu)


        pg.display.update()
        clock.tick(FPS)

    pg.quit()



# Kjør programmet vårt:
main()

