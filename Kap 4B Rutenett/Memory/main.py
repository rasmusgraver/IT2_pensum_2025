import pygame as pg
from constants import *
from rute import Rute
from pg_meny import Knapp, MENYFARGE
import random
import time

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

    for r in range(ANT_RAD):
        kolonner = []
        for k in range(ANT_KOL):
            rute = Rute(k,r, bokstaver.pop())
            kolonner.append(rute)
        brett.append(kolonner)

    return brett


brett:list[list[Rute]] = setup_brett()
running = True
# Antall ruter som er klikket på:
antall_aapne = 0
# De to rutene som er blitt klikket på:
rute1 = None
rute2 = None

while running:
    screen.fill(WHITE)

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_pos, y_pos = event.pos

            for knapp in knapper:
                if knapp.rektangel.collidepoint( (x_pos, y_pos) ):
                    print(f"Klikket på: {knapp.tekst}")
                    if knapp.tekst == "Avslutt":
                        running = False
                    if knapp.tekst == "Restart":
                        brett = setup_brett()
                        antall_aapne = 0
                        rute1 = None
                        rute2 = None

            k = x_pos // (RUTE_STR + GAP)
            r = y_pos // (RUTE_STR + GAP)
            if k < ANT_KOL and r < ANT_RAD:
                rute = brett[r][k]
                print("Du klikket på rute", rute)
                if antall_aapne < 2 and rute.vis == False:
                    rute.klikk()
                    # Lagrer ruten vi klikket på i rute1 og rute2:
                    if antall_aapne == 0:
                        rute1 = rute
                    else:
                        rute2 = rute
                    antall_aapne += 1

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




    # Må ha sjekken helt til slutt (Etter at vi har tegnet brettet):
    if rute1 and rute2:
        print("------------ Sjekker de to rutene")
        # Sjekk om de to er like:
        if rute1.bokstav == rute2.bokstav:
            print("De to er like")
            rute1.funnet = True
            rute2.funnet = True
        else:
            print("NEI!")

        # Vent 1 sec:
        time.sleep(1)
        # Lukk rutene igjen:
        rute1.vis = False
        rute2.vis = False
        antall_aapne = 0
        rute1 = None
        rute2 = None





# While running er slutt: Avslutt pygame:
pg.quit()

