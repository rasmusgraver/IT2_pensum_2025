import pygame as pg
from constants import *

class BallGravitasjon:

    def __init__(self, x, y, radius, farge, vx, vy) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vx = vx # Fart i x-retning
        self.vy = vy # Fart i y-retning

    def oppdater(self, bredde, hoyde):
        # Stopper å simulere bevegelse når den har falt ut av bildet:
        if self.y <= hoyde + self.radius:
            # Gravitasjon:
            self.vy += GRAVITASJON
            # Oppdater x og y pos, utifra fartene:
            self.x += self.vx
            self.y += self.vy
            if self.x > bredde - self.radius:
                self.vx *= -1 # Snu farten (x-retning)
            if self.x < self.radius:
                self.vx *= -1 # Snu farten (x-retning)        
        

    def tegn(self, vindu):
        # Tegne objektet på skjermen
        pg.draw.circle(vindu, color=self.farge, center=(self.x, self.y), radius=self.radius)
