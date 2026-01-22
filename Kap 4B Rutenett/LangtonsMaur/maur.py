import pygame as pg
from constants import *
from pathlib import Path

class Maur:
    IMAGE_DIR = Path(__file__).parent

    def __init__(self, rutenett, rad, kolonne) -> None:
        self.rutenett = rutenett
        self.rad = rad
        self.kolonne = kolonne
        self.bilde = pg.image.load(self.IMAGE_DIR / "maur.png")

    def draw(self, vindu):
        x = self.kolonne * CELLE_STR
        y = self.rad * CELLE_STR
        vindu.blit(self.bilde, (x,y) )

    def flytt(self):
        pass
