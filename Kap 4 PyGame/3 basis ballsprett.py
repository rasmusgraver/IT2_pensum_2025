import pygame as pg

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

VINDU_BREDDE = 500
VINDU_HOYDE = 500
FPS = 60

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

class Ball:

    def __init__(self, x, y, radius, farge) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vx = 5 # Fart i x-retning

    def oppdater(self):
        self.x += self.vx
        if self.x > VINDU_BREDDE:
            self.vx *= -1 # Snu farten (x-retning)
        if self.x < 0:
            self.vx *= -1 # Snu farten (x-retning)        
        

    def tegn(self, vindu):
        # Tegne objektet på skjermen
        pg.draw.circle(vindu, color=self.farge, center=(self.x, self.y), radius=self.radius)



def main():
    ball1 = Ball(100, 100, 40, RED)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(WHITE)
        ball1.oppdater()
        ball1.tegn(vindu)


        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()