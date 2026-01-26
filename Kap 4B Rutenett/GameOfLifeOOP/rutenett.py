import pygame as pg
from constants import *
import random


class Rute:
    def __init__(self, rad, kol) -> None:
        self.rad = rad
        self.kol = kol
        self.levende = False
        self.nextState = False
        self.naboer:list[Rute] = []

    def settNaboer(self, brett, ant_rader, ant_kolonner):
        # Fyll listen self.naboer med de rutene som er naboer til denne cellen:
        for r in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                # Ikke tell med deg selv:
                if not (r == 0 and k == 0):
                    if 0 <= self.rad + r < ant_rader and 0 <= self.kol + k < ant_kolonner:
                        self.naboer.append(brett[self.rad + r][self.kol + k])


    def klikk(self):
        # Bytt fra levende til død, og omvendt:
        self.levende = not self.levende

    def draw(self, vindu):
      # Tegner fyllt firkant med farge ut i fra levende/død
      farge = BLACK if self.levende else WHITE
      pg.draw.rect(vindu, farge, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR))
      # Tegner en grå boks rundt (bredde 1) (kjekt når fargen er hvit...)
      pg.draw.rect(vindu, GREY, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR), 1)

    def animer(self):
        # Setter "next state" ut i fra antallet naboer, ut if fra spillereglene:
        naboer = self.antallLevendeNaboer()
        self.nextState = False
        if self.levende:
            # For a space that is populated:
            # Each cell with one or no neighbors dies, as if by solitude.
            # Trengs ikke, next state False er "default"
            # if naboer < 2:
            #    self.nextState = False

            # Each cell with four or more neighbors dies, as if by overpopulation.
            # Trengs ikke, next state False er "default"
            # if naboer >= 4:
            #    self.nextState = False

            # Each cell with two or three neighbors survives.
            if naboer == 2 or naboer == 3:
                self.nextState = True

        else:
            # For a space that is empty or unpopulated:
            # Each cell with three neighbors becomes populated.
            if naboer == 3:
                self.nextState = True

    def next(self):
        # Sett levende ut i fra hva "next state" er
        self.levende = self.nextState

    def antallLevendeNaboer(self):
        antLevende = 0
        for nabo in self.naboer:
            if nabo.levende == True:
                antLevende += 1
        return antLevende


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

    def draw(self, vindu):
        # Kaller på draw metoden til hver Rute:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].draw(vindu)

    def oppdater(self):
        # Kaller på animer metoden til hver Rute:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].animer()

        # Og sett levende ut ifra "next state":
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].next()
