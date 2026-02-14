import pygame as pg
import random
from constants import *

class Firkant:

    def __init__(self, x_start, y_start, x_stop, y_stop) -> None:
        # Alt vi trenger er en rect og en tilfeldig farge:
        self.rect = pg.Rect(x_start, y_start, (x_stop-x_start), (y_stop-y_start))
        self.farge = random.choice(FARGER)

    def oppdater(self):
        # Trenger ikke denne i dag...
        pass

    def tegn(self, vindu):
        # Super easy når vi har en self.rect:
        pg.draw.rect(vindu, self.farge, self.rect)
