import pygame as pg
from constants import *
import random

class Bunndyr:

    def __init__(self) -> None:
        width = 100
        height = 30
        left = (VINDU_BREDDE-width) // 2
        self.rect = pg.Rect(left, VINDU_HOYDE-height, width, height)

    def voks(self):
        self.rect.width += 40
        self.rect.x -= 20

    def krymp(self):
        self.rect.width -= 40
        self.rect.x += 20

    def tegn(self, vindu):
        pg.draw.rect(vindu, GREY, self.rect)

    
class Plankton:

    def __init__(self, type) -> None:
        size = 18
        left = random.randint(0, VINDU_BREDDE-size)
        self.rect = pg.Rect(left, 0, size, size)
        self.type = type
        self.dod = False

    def oppdater(self):
        self.rect.y += 2
        if self.rect.top > VINDU_HOYDE:
            self.dod = True

    def bunndyrKollisjon(self, bunndyr:Bunndyr):
        # Sjekk for kollisjon med bunndyret:
        if self.rect.colliderect(bunndyr.rect):
            # Planktonet dør:
            self.dod = True
            if self.type == G:
                bunndyr.voks()
            else:
                bunndyr.krymp()

    def tegn(self, vindu):
        farge = RED if self.type == R else GREEN
        pg.draw.rect(vindu, farge, self.rect)
