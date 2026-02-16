from __future__ import annotations
import pygame as pg
from constants import *
from dataclasses import dataclass

# Dataclass med slots=True gjør at vi må spesifisere helt i starten av
# klassen alle attributter denne klassen har (for å unngå skrivefeil og andre bugs...)
@dataclass(slots=True)
class Rute:
    rad: int
    kol: int
    # Trenger to statuser for å få animasjonen til å fungere:
    # Hva er status i "denne framen", og i "neste frame"
    levende: bool = False
    nextLevende: bool = False

    def __init__(self, rad: int, kol: int) -> None:
        self.rad = rad
        self.kol = kol
    
    def nextStep(self, brett:list[list[Rute]], ant_kol:int) -> None:
        # Finner ut hva "next state" er (nextLevende)
        # Starter med å anta samme som sist:
        self.nextLevende = self.levende
        # Sjekker om nabo til venstre er levende, i så fall skal jeg bli det:
        if self.kol > 0 and brett[self.rad][self.kol - 1].levende:
            self.nextLevende = True

        # Sjekk om vi har kommet til slutten:
        if self.levende and self.kol == ant_kol-1:
            # Nullstill hele raden:
            for k in range(ant_kol):
                brett[self.rad][k].levende = False
                brett[self.rad][k].nextLevende = False

    def nextFrame(self):
        self.levende = self.nextLevende

    def klikk(self):
        self.levende = not self.levende

    def draw(self, vindu:pg.Surface) -> None:
      # Tegner fyllt firkant med farge (SORT/HVIT):
      farge = BLACK if self.levende else WHITE
      x_pos = self.kol * CELLE_STR
      y_pos = self.rad * CELLE_STR
      pg.draw.rect(vindu, farge, (x_pos, y_pos, CELLE_STR, CELLE_STR))
      # Tegner en grå boks rundt (bredde 1) (kjekt når fargen er hvit...)
      pg.draw.rect(vindu, GREY, (x_pos, y_pos, CELLE_STR, CELLE_STR), width=1)



class Rutenett:

    def __init__(self, ant_rader:int, ant_kolonner:int) -> None:
        self.ant_rader = ant_rader
        self.ant_kolonner = ant_kolonner
        # Lager 2D matrise (liste med lister) der hver verdi er et Rute objekt:
        # MERK: Denne linjen er ganske magisk - det er OK å ikke skjønne den helt...
        self.brett: list[list[Rute]] = [[Rute(r,k) for k in range(self.ant_kolonner)] for r in range(self.ant_rader)]
        # Sett naboene til rutene: Trengs ikke her!

    def getWindowSize(self) -> tuple[int,int]:
        return ( self.ant_kolonner*CELLE_STR, self.ant_rader*CELLE_STR )

    def klikk(self, rad:int, kolonne:int) -> None:
        self.brett[rad][kolonne].klikk()

    def draw(self, vindu:pg.Surface) -> None:
        # Kaller på draw metoden til hver Rute:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].draw(vindu)

    def vandring(self):
        # Finn ut om ruten er levende/død neste frame:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].nextStep(self.brett, self.ant_kolonner)

        # Oppdater status til "nextLevende":
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].nextFrame()
