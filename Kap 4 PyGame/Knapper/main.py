import pygame as pg
from constants import *
from spill1 import spill1

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

font = pg.font.SysFont("Arial", 24)
KNAPP_HEIGHT = 40
KNAPP_WIDTH = 100 
knapp1 = pg.Rect(20, 20, KNAPP_WIDTH, KNAPP_HEIGHT)
knapp2 = pg.Rect(20, 20 + (KNAPP_HEIGHT+20), KNAPP_WIDTH, KNAPP_HEIGHT)
knapp3 = pg.Rect(20, 20 + (KNAPP_HEIGHT+20)*2, KNAPP_WIDTH, KNAPP_HEIGHT)


running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if knapp1.collidepoint(event.pos):
                print("Spill 1")
                spill1(vindu, clock)
                
            if knapp2.collidepoint(event.pos):
                print("Spill 2")

            if knapp3.collidepoint(event.pos):
                print("Spill 3")


    vindu.fill(BLACK)



    pg.draw.rect(vindu, WHITE, knapp1)
    bilde = font.render("Knapp 1", True, BLUE).convert_alpha()
    vindu.blit(bilde, (knapp1.x, knapp1.y))

    pg.draw.rect(vindu, YELLOW, knapp2)
    bilde = font.render("Knapp 2", True, BLUE).convert_alpha()
    vindu.blit(bilde, (knapp2.x, knapp2.y))

    pg.draw.rect(vindu, WHITE, knapp3)
    bilde = font.render("Knapp 3", True, BLUE).convert_alpha()
    vindu.blit(bilde, (knapp3.x, knapp3.y))


    # Disse har vi alltid til slutt:
    pg.display.flip()
    clock.tick(FPS)




# Til slutt, når main loopen (while running) er ferdig:
pg.quit()
