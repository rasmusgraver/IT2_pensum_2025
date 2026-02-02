import pygame as pg
from constants import *
import random


class Rute:
    def __init__(self, rad, kol) -> None:
        self.rad = rad
        self.kol = kol
        self.status = TOM
        self.nextStatus = TOM
        self.naboer:list[Rute] = []


    def settNaboer(self, brett, antall_rader, antall_kolonner):
        for r in [-1,0,1]:
            for k in [-1,0,1]:
                if not (r==0 and k==0):
                    # Er vi innafor brettet?
                    if 0 <= self.rad + r < antall_rader and 0 <= self.kol + k < antall_kolonner:
                        self.naboer.append(brett[self.rad + r][self.kol + k])

    
    def nextStep(self, brannPågår):
        # Finner ut hva "nextStatus" er
        # tenker det er tryggest å starte med at nextStatus er samme som status:
        self.nextStatus = self.status
        # Voks - bare hvis det ikke brenner:
        if self.status == TOM and brannPågår == False:
            # Med 0,3% sjanse så skal nextStatus bli TRE:
            if random.random() < (0.3/100):
                self.nextStatus = TRE

        elif self.status == TRE:
            # Med 0,03% sjanse set NEXT status til BRANN
            if random.random() < (0.03/100):
                self.nextStatus = BRANN
            # OG: Sjekk alle naboer: Om en av de brenner, så begynner du å brenne
            for nabo in self.naboer:
                if nabo.status == BRANN:
                    self.nextStatus = BRANN
        
        elif self.status == BRANN:
            # Slutt å brenn
            self.nextStatus = TOM

    def nextFrame(self):
        self.status = self.nextStatus

    def draw(self, vindu):
        # Tegner fyllt firkant med farge (HVIT/GRØNN/RØD):
        farge = WHITE
        if self.status == TRE:
            farge = GREEN_DARK
        elif self.status == BRANN:
            farge = RED
        pg.draw.rect(vindu, farge, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR))
        # Tegner en grå boks rundt (bredde 1) (kjekt når fargen er hvit...)
        pg.draw.rect(vindu, GREY, (self.kol * CELLE_STR, self.rad * CELLE_STR, CELLE_STR, CELLE_STR), width=1)


class Rutenett:


    def __init__(self, ant_rader, ant_kolonner) -> None:
        self.ant_rader = ant_rader
        self.ant_kolonner = ant_kolonner
        self.brannPågår = False
        # Lager 2D matrise (liste med lister) der hver verdi er et Rute objekt:
        self.brett: list[list[Rute]] = [[Rute(r,k) for k in range(self.ant_kolonner)] for r in range(self.ant_rader)]
        # Sett naboene til rutene:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].settNaboer(self.brett, self.ant_rader, self.ant_kolonner)


    def getWindowSize(self) -> tuple:
        return ( self.ant_kolonner*CELLE_STR, self.ant_rader*CELLE_STR )


    def draw(self, vindu):
        # Kaller på draw metoden til hver Rute:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].draw(vindu)

    def skogbrann(self):
        # Finn ut "nextStatus" til hver rute:
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].nextStep(self.brannPågår)

        # Oppdater status til "nextStatus":
        self.brannPågår = False
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.brett[rad][kol].nextFrame()
                if self.brett[rad][kol].status == BRANN:
                    self.brannPågår = True
