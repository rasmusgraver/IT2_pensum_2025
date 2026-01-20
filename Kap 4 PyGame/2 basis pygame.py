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


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    vindu.fill(WHITE)
    pg.draw.circle(vindu, RED, (100, 250), 50)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()

