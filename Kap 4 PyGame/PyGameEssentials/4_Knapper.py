import pygame as pg
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

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
            mx, my = event.pos
            if knapp1.collidepoint( (mx,my) ):
                # Tenker oss at knapp 1 er "avslutt":
                running = False
            if knapp2.collidepoint( (mx,my) ):
                print("Du trykket på knapp 2")


    vindu.fill(WHITE)

    pg.draw.rect(vindu, GREEN, knapp1)
    pg.draw.rect(vindu, BLUE, knapp2)

    # Lager tekst til knappene våre
    knapp1_tekst = font.render("Avslutt", True, BLACK)
    vindu.blit(knapp1_tekst, (knapp1.x + 20 , knapp1.y + 10  )  )
    knapp2_tekst = font.render("Knapp 2", True, YELLOW)
    vindu.blit(knapp2_tekst, (knapp2.x + 20 , knapp2.y + 10  )  )

    # Disse har vi alltid til slutt:
    pg.display.flip()
    clock.tick(FPS)


# Til slutt, når main loopen (while running) er ferdig:
pg.quit()
