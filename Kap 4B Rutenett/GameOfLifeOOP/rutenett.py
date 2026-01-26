import pygame as pg
from constants import *
import random


class Rute:
    def __init__(self, rad, kol) -> None:
        self.rad = rad
        self.kol = kol
        self.farge:tuple = WHITE # random.choice(FARGER)

    def klikk(self):
        if self.farge == WHITE:
            self.farge = BLUE
        elif self.farge == BLUE:
            self.farge = RED
        elif self.farge == RED:
            self.farge = WHITE

    def draw(self, vindu):
      # Tegner fyllt firkant med self farge:
      pg.draw.rect(vindu, self.farge, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR))
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

