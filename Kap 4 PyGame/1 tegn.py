import pygame as pg
import random
from constants import *


def tegnSirkel(vindu, radius = 20):
    tilf_x = random.randint(0 + radius, VINDU_BREDDE - radius)
    tilf_y = random.randint(0 + radius, VINDU_HOYDE - radius)
    farge = random.choice(FARGER)
    pg.draw.circle(vindu, farge, (tilf_x, tilf_y), radius)


def main():
    pg.init()
    vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
    clock = pg.time.Clock()

    # Gjør dette bare én gang i dag:
    vindu.fill(WHITE)

    frame_counter = 0
    running = True
    while running:
        frame_counter += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        # Dropper denne i dag (lar bare alle tegningene "overleve"): vindu.fill(WHITE)
        if frame_counter % FPS == 0:
            # Et helt sekund har gått
            tegnSirkel(vindu)

        # Vi trenger fortsatt update/flip, ellers ser vi ikke det vi har tegnet:
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


# Kjør programmet vårt:
main()