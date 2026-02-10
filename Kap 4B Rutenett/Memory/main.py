import pygame as pg
from constants import *
from rute import Rute
from pg_meny import Knapp, MENYFARGE
import random

# Start opp PyGame:
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))


# Her setter du opp objektene dine:
knapper = []
knapper.append(Knapp(MENY_XSTART, MENY_YSTART, "Avslutt"))
knapper.append(Knapp(MENY_XSTART, MENY_YSTART + MENY_YAVSTAND, "Restart"))


def setup_brett() -> list[list[Rute]]:
    # Setter opp bokstavene vi skal ha i brettet (dobbelt opp av dem):
    bokstaver = ["A", "B", "C", "D", "E", "F", "G", "H"]
    bokstaver = bokstaver*2
    # Og "shuffler" dem tilfeldig:
    random.shuffle(bokstaver)

    print(bokstaver)

    # Starter med et tomt brett (som vi appender til)
    brett:list[list[Rute]] = []

    for x in range(ANT_X):
        y_verdier = []
        for y in range(ANT_Y):
            rute = Rute(x,y, bokstaver.pop())
            y_verdier.append(rute)
        brett.append(y_verdier)


    print(brett[0][0]) # "Jeg er rute (0,0)"
    print(brett[3][2]) # "Jeg er rute (3,2)"

    return brett


brett = setup_brett()


running = True
while running:

    clock.tick(FPS)
    screen.fill(WHITE)

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # Tøm brettet:
                for rad in brett:
                    for rute in rad:
                        rute.vis = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_pos, y_pos = pg.mouse.get_pos()

            for knapp in knapper:
                if knapp.rektangel.collidepoint( (x_pos, y_pos) ):
                    print(f"Klikket på: {knapp.tekst}")
                    if knapp.tekst == "Avslutt":
                        running = False
                    if knapp.tekst == "Restart":
                        brett = setup_brett()

            x = x_pos // (RUTE_STR + GAP)
            y = y_pos // (RUTE_STR + GAP)
            if x < ANT_X and y < ANT_Y:
                rute = brett[x][y]
                print("Du klikket på rute", rute)
                rute.klikk()


    # Tegn brettet for hver "frame":
    for rad in brett:
        for rute in rad:
            rute.tegn(screen)
    
    # og knappene:
    for knapp in knapper:
        knapp.tegn(screen)




    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame:
pg.quit()

