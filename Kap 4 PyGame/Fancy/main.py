import pygame as pg
from constants import *
from MainCharacters.NinjaFrog.ninja import NinjaFrog


pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Ninja Frog!")
clock = pg.time.Clock()


# our main guy:
ninja = NinjaFrog(100, 100)


def main():
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(WHITE)
        
        # Sjekker hvilke taster som er trykket:
        keys = pg.key.get_pressed()

        ninja.update(keys)
        ninja.draw(vindu)

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


# Kjør programmet vårt:
main()

