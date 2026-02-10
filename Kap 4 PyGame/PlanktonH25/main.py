import pygame as pg
from constants import *
from klasser import Bunndyr, Plankton
import random


pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

# Globale variable:
running = True
plankton_r_sannsynlighet = 0.02
plankton_g_sannsynlighet = 0.03

# Sett opp objektene våre:
bunndyr = Bunndyr()
planktonliste:list[Plankton] = []


def events():
    global running
    global plankton_g_sannsynlighet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
            plankton_g_sannsynlighet += 0.01
            # Max verdi:
            if plankton_g_sannsynlighet > 0.2:
                plankton_g_sannsynlighet = 0.2
        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            plankton_g_sannsynlighet -= 0.01
            # Minste verdi:
            if plankton_g_sannsynlighet < 0.01:
                plankton_g_sannsynlighet = 0.01


def random_plankton():
    # Legg til plankton tilfeldig:
    if random.random() < plankton_g_sannsynlighet:
        planktonliste.append(Plankton(G))
    if random.random() < plankton_r_sannsynlighet:
        planktonliste.append(Plankton(R))


def oppdater_objekter():
    for p in planktonliste[::]:
        if p.dod:
            # Fjern døde plankton:
            planktonliste.remove(p)
        else:
            p.oppdater()
            p.bunndyrKollisjon(bunndyr)


def tegn_objekter():
    bunndyr.tegn(vindu)
    for p in planktonliste:
        p.tegn(vindu)


def spill_slutt():
    global running

    # Sjekk om spillet er slutt:
    if bunndyr.rect.width < 50:
        print("Bunndyret døde av forgiftning")
        running = False
    if bunndyr.rect.width > VINDU_BREDDE:
        print("Bunndyret døde av forspisning")
        running = False


while running:
    events()
    random_plankton()

    # Tegn bakgrunn: (En slags "reset" av hele vinduet vårt)
    vindu.fill(BLACK)
    oppdater_objekter()
    tegn_objekter()
    spill_slutt()

    # Har alltid disse med til slutt:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()
