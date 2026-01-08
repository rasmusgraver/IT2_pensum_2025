import pygame as pg
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

class Rektangel:
    def __init__(self, x, y, size=40) -> None:
        self.rect = pg.Rect(0, 0, size, size)
        self.rect.center = (x, y)

    def draw(self, vindu):
        pg.draw.rect(vindu, RED, self.rect)


def main():

    objects:list[Rektangel] = []
    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mx, my = event.pos  # posisjon for klikket
                objects.append(Rektangel(mx, my))


        vindu.fill(WHITE)
        for rekt in objects:
            rekt.draw(vindu)


        # Disse har vi alltid til slutt:
        pg.display.flip()
        clock.tick(FPS)



# Kjør programmet vårt:
main()

# Til slutt, når main loopen (while running) er ferdig:
pg.quit()
