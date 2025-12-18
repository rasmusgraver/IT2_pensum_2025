import pygame as pg
from constants import *
from ninjafrog import NinjaFrog

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Ninja Frog!")
clock = pg.time.Clock()


# our main guy:
ninja = NinjaFrog(100, 100)

def main():
    running = True

    while running:
        jumping = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
                jumping = True

        vindu.fill(WHITE)


        # Tegn en fylt rektangel, som viser bakken
        bakken = pg.Rect(0, BAKKE_HOYDE, VINDU_BREDDE, (VINDU_HOYDE-BAKKE_HOYDE))
        pg.draw.rect(vindu, GREEN_DARK, bakken)

        # Sjekker hvilke taster som er trykket:
        keys = pg.key.get_pressed()

        ninja.update(keys, jumping)
        ninja.draw(vindu)

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


# Kjør programmet vårt:
main()

