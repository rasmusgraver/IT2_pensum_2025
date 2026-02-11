import pygame as pg
from constants import *
from simulering import Simulering

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

sim = Simulering()
while sim.running:
    sim.events()
    sim.random_plankton()
    sim.oppdater_objekter()
    sim.tegn(vindu)
    sim.spill_slutt()

    # Har alltid disse med til slutt:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()
