import pygame as pg
from constants import *
from spill1 import spill1

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

font = pg.font.SysFont("Arial", 24)
KNAPP_HEIGHT = 40
KNAPP_WIDTH = 100
PADDING_X = 10
PADDING_Y = 5
knapp1 = pg.Rect(20, 20, KNAPP_WIDTH, KNAPP_HEIGHT)
knapp2 = pg.Rect(20, 20 + (KNAPP_HEIGHT+20), KNAPP_WIDTH, KNAPP_HEIGHT)
knapp3 = pg.Rect(20, 20 + (KNAPP_HEIGHT+20)*2, KNAPP_WIDTH, KNAPP_HEIGHT)

def tegnKnapp(vindu, knapp:pg.Rect, tekst:str):
    pg.draw.rect(vindu, WHITE, knapp)
    tekstBilde = font.render(tekst, True, BLUE).convert_alpha()
    vindu.blit(tekstBilde, (knapp.x + PADDING_X, knapp.y + PADDING_Y))


running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            # MERK: 2 ulike måter å hente museklikk sin posisjon på under her. 
            # mouse.get_pos() eller event.pos (Merk: Siste er ikke en funksjon...)
            # Begge fungerer fint:
            mx, my = pg.mouse.get_pos()
            if knapp1.collidepoint( (mx,my) ):
                print("Spill 1")
                spill1(vindu, clock)
                
            if knapp2.collidepoint(event.pos):
                print("Spill 2")

            if knapp3.collidepoint(event.pos):
                print("Spill 3")

    vindu.fill(BLACK)

    tegnKnapp(vindu, knapp1, "Knapp 1")
    tegnKnapp(vindu, knapp2, "Knapp 2")
    tegnKnapp(vindu, knapp3, "Knapp 3")

    # Disse har vi alltid til slutt:
    pg.display.flip()
    clock.tick(FPS)




# Til slutt, når main loopen (while running) er ferdig:
pg.quit()
