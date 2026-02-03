import pygame as pg
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

KNAPP_HOYDE = 50
KNAPP_BREDDE = 150
knapp1 = pg.Rect(20, 100, KNAPP_BREDDE, KNAPP_HOYDE)
knapp2 = pg.Rect(20, 100 + KNAPP_HOYDE + 20, KNAPP_BREDDE, KNAPP_HOYDE)

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mx, my = event.pos  # posisjon for klikket
            # Det finnes en annen måte å få muse-posisjon på:


    vindu.fill(WHITE)

    # Hover effekt:
    x,y = pg.mouse.get_pos()
    if knapp1.collidepoint( (x,y) ):
        pg.draw.rect(vindu, GREEN, knapp1)
    else:
        pg.draw.rect(vindu, GREEN_DARK, knapp1)


    pg.draw.rect(vindu, BLUE, knapp2)


    # Disse har vi alltid til slutt:
    pg.display.flip()
    clock.tick(FPS)


# Til slutt, når main loopen (while running) er ferdig:
pg.quit()
