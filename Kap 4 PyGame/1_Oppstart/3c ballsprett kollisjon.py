from __future__ import annotations
import pygame as pg
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

class Ball:

    def __init__(self, x, y, radius, farge, vx, vy) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vx = vx # Fart i x-retning
        self.vy = vy # Fart i y-retning
        self.kollidert = False

    def oppdater(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > VINDU_BREDDE - self.radius:
            self.vx *= -1 # Snu farten (x-retning)
        if self.x < self.radius:
            self.vx *= -1 # Snu farten (x-retning)        
        if self.y > VINDU_HOYDE - self.radius:
            self.vy *= -1 # Snu farten (y-retning)
        if self.y < self.radius:
            self.vy *= -1 # Snu farten (y-retning)        
        

    def tegn(self, vindu):
        # Tegne objektet på skjermen
        farge = self.farge
        if self.kollidert:
            farge = BLACK
        pg.draw.circle(vindu, color=farge, center=(self.x, self.y), radius=self.radius)

    def kollisjon(self, ball:Ball):
        samletRadius = self.radius + ball.radius
        x_diff = abs(self.x - ball.x)
        y_diff = abs(self.y - ball.y)
        if x_diff > samletRadius:
            # Quick check: x'ene er for langt unna hverandre til å kollidere
            return
        if y_diff > samletRadius:
            # Quick check: y'ene er for langt unna hverandre til å kollidere
            return        
        hyp = (x_diff**2 + y_diff**2)**0.5 # NOTE: Kan opphøye i 0.5 for sqrt
        if hyp < samletRadius:
            self.kollidert = True
            ball.kollidert = True


def main():
    ball1 = Ball(x=100, y=100, radius=40, farge=BLUE, vx=3, vy=2)
    ball2 = Ball(x=20, y=100, radius=10, farge=RED, vx=3, vy=8)
    ball3 = Ball(x=100, y=25, radius=20, farge=GREEN, vx=7, vy=2)

    baller = [ball1, ball2, ball3]

    # Om du vil ha flere baller kan du også legge dem til direkte slik:
    baller.append(Ball(x=200, y=125, radius=10, farge=PURPLE, vx=7, vy=3))
    baller.append(Ball(x=170, y=175, radius=20, farge=ORANGE, vx=5, vy=4))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(WHITE)

        # Kollisjonsdeteksjon først, så fargene blir rett
        # Først sett alle til å ikke være kollidert, før de settes til kollidert om avstanden er liten nok
        for ball in baller:
            ball.kollidert = False

        for i in range(len(baller)):
            ball1 = baller[i]
            for j in range(i+1, len(baller)):
                ball2 = baller[j]
                ball1.kollisjon(ball2)

        for ball in baller:
            ball.oppdater()
            ball.tegn(vindu)


        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()