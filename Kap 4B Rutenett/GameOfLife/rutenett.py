import pygame as pg
from constants import *
import random


class Rute:
    def __init__(self, rad, kol) -> None:
        self.rad = rad
        self.kol = kol
        self.levende = False
        self.nextLevende = False
        self.naboer:list[Rute] = []

    def antallLevendeNaboer(self) -> int:
        antallLevende = 0
        for rute in self.naboer:
            if rute.levende:
                antallLevende += 1
        return antallLevende
    
    def nextStep(self):
        levendeNaboer = self.antallLevendeNaboer()
        # Game of Life Rules
        # For a space that is alive:
        if self.levende:

            # Each cell with one or no neighbors dies, as if by solitude.
            if levendeNaboer <= 1:
                self.nextLevende = False

            # Each cell with four or more neighbors dies, as if by overpopulation.
            elif levendeNaboer >= 4:
                self.nextLevende = False

            # Each cell with two or three neighbors survives.
            else:
                self.nextLevende = True

        # For a space that is empty or unpopulated:
        else:
            # Each cell with three neighbors becomes populated.
            if levendeNaboer == 3:
                self.nextLevende = True

    def nextFrame(self):
        self.levende = self.nextLevende

    def klikk(self):
        self.levende = not self.levende

    def draw(self, vindu):
      # Tegner fyllt firkant med farge (SORT/HVIT):
      farge = BLACK if self.levende else WHITE
      pg.draw.rect(vindu, farge, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR))
      # Tegner en grå boks rundt (bredde 1) (kjekt når fargen er hvit...)
      pg.draw.rect(vindu, GREY, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR), 1)



class Rutenett:


    def __init__(self, ant_rader, ant_kolonner) -> None:
        self.ant_rader = ant_rader
        self.ant_kolonner = ant_kolonner
        # Lager 2D matrise (liste med lister) der hver verdi er et Rute objekt:
        self.brett: list[list[Rute]] = [[Rute(r,k) for k in range(self.ant_kolonner)] for r in range(self.ant_rader)]

    def getWindowSize(self) -> tuple:
        return ( self.ant_kolonner*CELLE_STR, self.ant_rader*CELLE_STR )

    def klikk(self, rad, kolonne):
        self.brett[rad][kolonne].klikk()

    def draw(self, vindu):
        # Kaller på draw metoden til hver Rute:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].draw(vindu)

    def gameOfLife(self):
        # Finn ut om ruten er levende/død neste frame:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].nextStep()

        # Oppdater status til "nextLevende":
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].nextFrame()
