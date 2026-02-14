import pygame as pg
from constants import *
from pathlib import Path
from rutenett import Rutenett

class Maur:
    IMAGE_DIR = Path(__file__).parent
    # Retningene med tilsvarende fart i x og y retning:
    RETNINGER = ["HØYRE", "NED", "VENSTRE", "OPP"]
    VX_VY = [(1,0), (0,1), (-1,0), (0,-1)]

    def __init__(self, rutenett: Rutenett, rad, kolonne) -> None:
        self.rutenett = rutenett
        self.rad = rad
        self.retningsIndex = 0
        self.kolonne = kolonne
        self.bilde = pg.image.load(self.IMAGE_DIR / "maur.png")

    def draw(self, vindu):
        x = self.kolonne * CELLE_STR
        y = self.rad * CELLE_STR
        # Roter bilde til å peke rett vei
        bilde = pg.transform.rotate(self.bilde, -(90*self.retningsIndex))
        vindu.blit(bilde, (x,y) )

    def flytt(self):
        if self.rutenett.brett[self.rad][self.kolonne].farge == WHITE:
            self.rutenett.brett[self.rad][self.kolonne].farge = BLACK
            self.retningsIndex += 1
        else:
            self.rutenett.brett[self.rad][self.kolonne].farge = WHITE
            self.retningsIndex -= 1
        # pass på at vi holder oss innafor 0 til 3 på indeksen:
        self.retningsIndex %= 4
        # Flytt mauren i rett rettning:
        vx, vy = self.VX_VY[self.retningsIndex]
        print("Mauren har nå retning", self.RETNINGER[self.retningsIndex])
        self.kolonne += vx
        self.rad += vy
