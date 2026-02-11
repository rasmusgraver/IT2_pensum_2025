import pygame as pg
from constants import *
from tekst import skriv_tekst

class Rute:
    def __init__(self, x, y, bokstav):
        self.x = x
        self.y = y
        self.bokstav = bokstav
        self.vis = False
        self.funnet = False

    def __repr__(self):
        return f"Rute {self.x}, {self.y} med bokstav {self.bokstav}"

    def klikk(self):
        # Vis ruten:
        self.vis = True

    def tegn(self, screen):
        x_pos = self.x * (RUTE_STR + GAP)
        y_pos = self.y * (RUTE_STR + GAP)

        if self.vis:
            # Tegn bokstaven
            skriv_tekst(screen, x_pos + 16, y_pos + 8, self.bokstav, BLACK)
        elif self.funnet:
            # Tegn bokstaven med grønn bakgrunnsfarge:
            skriv_tekst(screen, x_pos + 16, y_pos + 8, self.bokstav, BLACK, GREEN)
        else:
            # Tegn en firkant
            pg.draw.rect(screen, GREEN, (x_pos, y_pos, RUTE_STR, RUTE_STR))

        # Tegn en ramme rundt:
        pg.draw.rect(screen, BLACK, (x_pos, y_pos, RUTE_STR, RUTE_STR), width=1)
