import pygame as pg


class Ball:

    def __init__(self, x, y, radius, farge, vx, vy) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vx = vx # Fart i x-retning
        self.vy = vy # Fart i y-retning

    def oppdater(self, bredde, hoyde):

        # Gravitasjon:
        self.vy += 0.4

        self.x += self.vx
        self.y += self.vy
        if self.x > bredde - self.radius:
            self.vx *= -1 # Snu farten (x-retning)
        if self.x < self.radius:
            self.vx *= -1 # Snu farten (x-retning)        
        if self.y > hoyde - self.radius:
            self.vy *= -1 # Snu farten (y-retning)
            self.y = hoyde - self.radius # Tving den ut fra kanten
        if self.y < self.radius:
            self.vy *= -1 # Snu farten (y-retning)        
        

    def tegn(self, vindu):
        # Tegne objektet på skjermen
        pg.draw.circle(vindu, color=self.farge, center=(self.x, self.y), radius=self.radius)
