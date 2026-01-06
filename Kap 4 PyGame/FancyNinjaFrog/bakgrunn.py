from pathlib import Path
import pygame as pg
import os
from constants import *

class Bakgrunn:
    IMAGE_DIR = Path(__file__).parent / "Items" / "Boxes" / "Box1"

    def __init__(self, x, y):
        self.image = pg.image.load(self.IMAGE_DIR / "Idle.png")

        # Typisk i PyGame: Bruker en "rect" for å plassere bildet på rett sted på skjermen (se draw metoden)        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, keys=None):
        pass
    
    def draw(self, surface):        
        surface.blit(self.image, self.rect)
    
