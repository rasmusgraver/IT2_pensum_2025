import pygame as pg
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

def main():
    running = True
    while running:

        # Den ene måten å motta keyboard input på:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_a:
                print("Du trykket på a knappen")


        # Den andre måten å motta keyboard input på:
        keys = pg.key.get_pressed()
        if keys[pg.K_b]:
            print("Du trykket på b knappen")


        vindu.fill(WHITE)
        pg.draw.circle(vindu, RED, (100, 250), 50)


        # Disse har vi alltid til slutt:
        pg.display.flip()
        clock.tick(FPS)



# Kjør programmet vårt:
main()

# Til slutt, når main loopen (while running) er ferdig:
pg.quit()
