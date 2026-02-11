import pygame as pg
import random
from klasser import Bunndyr, Plankton
from constants import *

class Simulering:
    def __init__(self) -> None:
        self.running = True
        self.plankton_r_sannsynlighet = 0.02
        self.plankton_g_sannsynlighet = 0.03
        # Sett opp objektene våre:
        self.bunndyr = Bunndyr()
        self.planktonliste:list[Plankton] = []

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
                self.plankton_g_sannsynlighet += 0.01
                # Max verdi:
                if self.plankton_g_sannsynlighet > 0.2:
                    self.plankton_g_sannsynlighet = 0.2
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self.plankton_g_sannsynlighet -= 0.01
                # Minste verdi:
                if self.plankton_g_sannsynlighet < 0.01:
                    self.plankton_g_sannsynlighet = 0.01

            # Litt debugg info til terminal (uansett hvilken tast man trykker ned):
            if event.type == pg.KEYDOWN:
                print(f"Sannsynlighet for grønn er nå {self.plankton_g_sannsynlighet}.")
                print(f"Antallet plankton i lista er {len(self.planktonliste)}")


    def random_plankton(self):
        # Legg til plankton tilfeldig:
        if random.random() < self.plankton_g_sannsynlighet:
            self.planktonliste.append(Plankton(G))
        if random.random() < self.plankton_r_sannsynlighet:
            self.planktonliste.append(Plankton(R))


    def oppdater_objekter(self):
        for p in self.planktonliste[::]:
            if p.dod:
                # Fjern døde plankton:
                self.planktonliste.remove(p)
            else:
                p.oppdater()
                p.bunndyrKollisjon(self.bunndyr)


    def tegn(self, vindu):
        vindu.fill(BLACK)
        self.bunndyr.tegn(vindu)
        for p in self.planktonliste:
            p.tegn(vindu)


    def spill_slutt(self):
        # Sjekk om spillet er slutt:
        if self.bunndyr.rect.width < 50:
            print("Bunndyret døde av forgiftning")
            self.running = False
        if self.bunndyr.rect.width > VINDU_BREDDE:
            print("Bunndyret døde av forspisning")
            self.running = False

