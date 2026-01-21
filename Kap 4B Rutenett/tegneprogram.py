import pygame as pg
from constants import *


CELLE_STR = 40
ANT_RADER = 10
ANT_KOLONNER = 15
PALETT_STR = 60

# Litt fancy måte å skrive det på, men vi bare godtar at det funker :)
rutenett = [[WHITE for k in range(ANT_KOLONNER)] for r in range(ANT_RADER)]

pg.init()
VINDU_BREDDE = CELLE_STR*ANT_KOLONNER
VINDU_HOYDE = CELLE_STR*ANT_RADER + PALETT_STR
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

# Vi bare manuelt legger til svart som farge også :)
FARGER.append(BLACK)

valgtFarge = BLACK
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mx, my = event.pos
            # Sjekk om vi treffer paletten:
            if my > (VINDU_HOYDE - PALETT_STR):
                # På paletten (høyden er rett i hvert fall): Finn ny valgt farge
                if mx < PALETT_STR*len(FARGER):
                    valgtFarge = FARGER[mx // PALETT_STR]
                else:
                    # Til høyre for paletten, sett valgt farge til hvit:
                    valgtFarge = WHITE
            else:
                # Ikke på paletten: Fargelegg ruten med valgt farge:
                kolonne = mx // CELLE_STR
                rad = my // CELLE_STR
                rutenett[rad][kolonne] = valgtFarge

    vindu.fill(WHITE)

    # Tegn rutene:
    for rad in range(ANT_RADER):
        for kolonne in range(ANT_KOLONNER):
            pg.draw.rect(vindu, rutenett[rad][kolonne], (kolonne*CELLE_STR, rad*CELLE_STR, CELLE_STR, CELLE_STR))
            pg.draw.rect(vindu, GREY, (kolonne*CELLE_STR, rad*CELLE_STR, CELLE_STR, CELLE_STR), 2)

    # Tegn paletten:
    i = 0
    for farge in FARGER:
        pg.draw.rect(vindu, farge, (i*PALETT_STR, VINDU_HOYDE-PALETT_STR,PALETT_STR, PALETT_STR))
        i += 1

    # Boka gjorde det på denne måten (med i som teller i løkka):
    # for i in range(len(FARGER)):
    #    pg.draw.rect(vindu, FARGER[i], (i*PALETT_STR, VINDU_HOYDE-PALETT_STR,PALETT_STR, PALETT_STR))


    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame:
pg.quit()
