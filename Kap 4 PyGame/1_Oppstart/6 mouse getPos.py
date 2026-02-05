import pygame as pg
from ball_gravitasjon import BallGravitasjon
from constants import *
import random

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 20)

def main():
    baller = []
    # baller.append( Ball(x=100, y=100, radius=40, farge=BLUE, vx=5, vy=3) )

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # venstre museknapp
                    mx, my = event.pos  # posisjon for klikket
                    # Oppretter en ny ball på museposisjonen
                    farge = random.choice(FARGER)
                    baller.append(BallGravitasjon(x=mx, y=my, radius=30, farge=farge, vx=0, vy=0))

        vindu.fill(WHITE)

        if len(baller) == 0:
            tekst = font.render("Trykk på skjermen for å legge til baller!", True, GREEN_DARK)
            vindu.blit(tekst, (20, VINDU_HOYDE/2))

        for ball in baller:
            ball.oppdater(VINDU_BREDDE, VINDU_HOYDE)
            ball.tegn(vindu)


        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()