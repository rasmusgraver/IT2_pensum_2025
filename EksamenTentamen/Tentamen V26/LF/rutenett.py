import pygame as pg
from constants import *


class Rute:
    def __init__(self, rad, kol) -> None:
        self.rad = rad
        self.kol = kol
        self.farge = WHITE
        self.originalFarge = WHITE
        self.naboer:list[Rute] = []
        

    def settNaboer(self, brett, ant_rader, ant_kolonner):
        if self.rad != 0:
            self.naboer.append(brett[self.rad - 1][self.kol])
        if self.rad != ant_rader - 1:
            self.naboer.append(brett[self.rad + 1][self.kol])


    def klikk(self):
        if self.farge == WHITE:
            self.farge = self.originalFarge
        elif self.farge == BLACK:
            self.farge = WHITE
        else:
            self.farge = BLACK

    def draw(self, vindu):
      x_start = self.kol * CELLE_STR
      y_start = self.rad * CELLE_STR
      # Tegner fyllt firkant med fargen til cellen:
      pg.draw.rect(vindu, self.farge, (x_start, y_start, CELLE_STR, CELLE_STR))
      # Tegner en grå boks rundt (bredde 1) (kjekt når fargen er hvit...)
      pg.draw.rect(vindu, GREY, (x_start, y_start, CELLE_STR, CELLE_STR), 1)



class Rutenett:

    def __init__(self, ant_rader, ant_kolonner) -> None:
        self.ant_rader = ant_rader
        self.ant_kolonner = ant_kolonner
        # Lager 2D matrise (liste med lister) der hver verdi er et Rute objekt:
        self.brett: list[list[Rute]] = [[Rute(r,k) for k in range(self.ant_kolonner)] for r in range(self.ant_rader)]
        # Og sett naboene til hver rute:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].settNaboer(self.brett, self.ant_rader, self.ant_kolonner)


    def getWindowSize(self) -> tuple:
        return ( self.ant_kolonner*CELLE_STR, self.ant_rader*CELLE_STR )

    def klikk(self, rad, kolonne):
        # Pass på at vi er innafor rutenettet:
        if 0 <= rad < self.ant_rader and 0 <= kolonne < self.ant_kolonner:
            self.brett[rad][kolonne].klikk()
            # OG: Klikk på naboene også!
            for nabo in self.brett[rad][kolonne].naboer:                
                nabo.klikk()


    def settFarger(self):
        indeks = 0
        antFarger = len(FARGER)
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                farge = FARGER[indeks % antFarger]
                self.brett[rad][kol].farge = farge
                self.brett[rad][kol].originalFarge = farge
                indeks += 1

    def draw(self, vindu):
        # Kaller på draw metoden til hver Rute:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].draw(vindu)

    def oppdater(self):
        # Trengs ikke her:
        pass
