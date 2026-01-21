import pygame as pg
from constants import *
import random


class Rute:
    def __init__(self, rad, kol) -> None:
        self.rad = rad
        self.kol = kol
        self.farge:tuple = WHITE # random.choice(FARGER)

    def draw(self, vindu):
      # Tegner fyllt firkant med self farge:
      pg.draw.rect(vindu, self.farge, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR))
      # Tegner en grå boks rundt (bredde 1) (kjekt når fargen er hvit...)
      pg.draw.rect(vindu, GREY, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR), 1)



class Rutenett:


    def __init__(self) -> None:
        # Lager 2D matrise (liste med lister) der hver verdi er et Rute objekt:
        self.brett: list[list[Rute]] = [[Rute(r,k) for k in range(ANT_KOLONNER)] for r in range(ANT_RADER)]


    def draw(self, vindu):
        # Kaller på draw metoden til hver Rute:
        for rad in range(ANT_RADER):
            for kol in range(ANT_KOLONNER):
                self.brett[rad][kol].draw(vindu)

