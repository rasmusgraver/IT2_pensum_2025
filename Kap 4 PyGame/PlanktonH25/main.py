import pygame as pg
from constants import *
from klasser import Bunndyr, Plankton
import random

plankton_r_sannsynlighet = 0.01
plankton_g_sannsynlighet = 0.03


pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

bunndyr = Bunndyr()
planktonliste:list[Plankton] = []


running = True
while running:
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

    # Legg til plankton tilfeldig:
    if random.random() < plankton_g_sannsynlighet:
        planktonliste.append(Plankton(G))
    if random.random() < plankton_r_sannsynlighet:
        planktonliste.append(Plankton(R))


    # Tegn bakgrunn: (En slags "reset" av hele vinduet vårt)
    vindu.fill(BLACK)

    # Oppdater objektene våre:
    for p in planktonliste:
        p.oppdater()
        # Sjekk for kollisjon med bunndyret:
        if p.rect.colliderect(bunndyr.rect):
            # Planktonet dør:
            p.dod = True
            if p.type == G:
                bunndyr.voks()
            else:
                bunndyr.krymp()

    # Tegn objektene våre:
    bunndyr.tegn(vindu)
    for p in planktonliste:
        p.tegn(vindu)

    # Fjern døde plankton:
    for p in planktonliste:
        if p.dod:
            planktonliste.remove(p)

    # Sjekk om spillet er slutt:
    if bunndyr.rect.width < 50:
        print("Bunndyret døde av forgiftning")
        running = False
    if bunndyr.rect.width > VINDU_BREDDE:
        print("Bunndyret døde av forspisning")
        running = False


    # Har alltid disse med til slutt:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()
