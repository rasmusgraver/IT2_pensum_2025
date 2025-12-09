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

    def __init__(self, x, y, radius, farge, vx, vy) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vx = vx # Fart i x-retning
        self.vy = vy # Fart i y-retning

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
        pg.draw.circle(vindu, color=self.farge, center=(self.x, self.y), radius=self.radius)



def main():
    ball1 = Ball(x=100, y=100, radius=40, farge=BLUE, vx=5, vy=3)
    ball2 = Ball(x=20, y=100, radius=10, farge=RED, vx=5, vy=30)
    ball3 = Ball(x=100, y=25, radius=20, farge=GREEN, vx=15, vy=3)

    baller = [ball1, ball2, ball3]

    # Om du vil ha flere baller kan du også legge dem til direkte slik:
    # baller.append(Ball(x=23,y=34.....))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(WHITE)

        for ball in baller:
            ball.oppdater()
            ball.tegn(vindu)


        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()