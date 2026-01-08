import pygame as pg
from constants import *
from pathlib import Path

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

IMAGE_DIR = Path(__file__).parent

class Emo:
    def __init__(self) -> None:
        self.bilde = pg.image.load(IMAGE_DIR / "emo.png")
        self.rect = self.bilde.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.speed = 5

    def move(self, keys):
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, vindu):
        vindu.blit(self.bilde, self.rect)


class Rektangel:
    def __init__(self, x, y, size=40) -> None:
        self.rect = pg.Rect(0, 0, size, size)
        self.rect.center = (x, y)

    def kollisjon(self, rekt:pg.Rect):
        if rekt.colliderect(self.rect):
            return True
        return False

    def draw(self, vindu):
        pg.draw.rect(vindu, RED, self.rect)


def main():

    emo = Emo()
    rektangler:list[Rektangel] = []
    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mx, my = event.pos  # posisjon for klikket
                rektangler.append(Rektangel(mx, my))

        vindu.fill(WHITE)


        keys = pg.key.get_pressed()
        emo.move(keys)
        emo.draw(vindu)

        for rekt in rektangler:
            if rekt.kollisjon(emo.rect):
                rektangler.remove(rekt)
            else:
                rekt.draw(vindu)


        # Disse har vi alltid til slutt:
        pg.display.flip()
        clock.tick(FPS)



# Kjør programmet vårt:
main()

# Til slutt, når main loopen (while running) er ferdig:
pg.quit()
