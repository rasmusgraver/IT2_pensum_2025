import pygame as pg
from constants import *


pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

plattformer = []
# Legg til 3 plattformer:
plattformer.append(  pg.Rect(300, 150, 100, 40)  )
plattformer.append(  pg.Rect(100, 280, 150, 40)  )
plattformer.append(  pg.Rect(300, 350, 150, 40)  )

# Mario klassen:
class Mario:

    def __init__(self, x, y) -> None:
        self.rect:pg.Rect = pg.Rect(x, y, 40, 60)
        # Flytt Mario opp, så han kommer på bakken:
        self.rect.bottom = y
        self.vy = 0

    def oppdater(self, keys):
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        if keys[pg.K_RIGHT]:
            self.rect.x += 5
        if keys[pg.K_UP]:
            self.vy = -10
        # La tyngdekraften jobbe:
        self.vy += 1
        # Flytt i y-retning med vy fart:
        self.rect.y += self.vy
        # Treffer bakken:
        if self.rect.bottom > BAKKEN:
           self.rect.bottom = BAKKEN 
           self.vy = 0

    def plattformKollisjon(self, plattformer:list[pg.Rect]):
        for p in plattformer:
            if self.rect.colliderect(p):
                # Dytt Mario opp på plattformen:
                self.rect.bottom = p.top
                self.vy = 0


    def tegn(self, vindu):
        pg.draw.rect(vindu, RED, self.rect)


mario = Mario(100, BAKKEN)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    vindu.fill(SKY_BLUE)
    # Tegn bakken:
    pg.draw.rect(vindu, GREEN_DARK, (0, BAKKEN, VINDU_BREDDE, (VINDU_HOYDE-BAKKEN) ) )

    # Tegn plattformer:
    for p in plattformer:
        pg.draw.rect(vindu, GREEN_DARK, p)

    # Flytt Mario:
    keys = pg.key.get_pressed()
    mario.oppdater(keys)
    mario.plattformKollisjon(plattformer)

    # Tegn Mario:
    mario.tegn(vindu)


    pg.display.flip()
    clock.tick(FPS)





pg.quit()

