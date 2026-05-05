import pygame as pg
import random
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Fallende Baller")
clock = pg.time.Clock()

# Ball egenskaper
BALL_RADIUS = 20
ball1_vx, ball1_vy, ball1_x, ball1_y = (0,0,0,0)
ball2_vx, ball2_vy, ball2_x, ball2_y = (0,0,0,0)

# Funksjon for å resette ball 1
def reset_ball1():
    global ball1_vx, ball1_vy, ball1_x, ball1_y
    ball1_x = BALL_RADIUS
    ball1_y = BALL_RADIUS
    ball1_vx = random.randint(1, 3)
    ball1_vy = random.randint(2, 5)

# Funksjon for å resette ball 2
def reset_ball2():
    global ball2_vx, ball2_vy, ball2_x, ball2_y
    ball2_x = VINDU_BREDDE - BALL_RADIUS
    ball2_y = BALL_RADIUS
    ball2_vx = random.randint(-5, 0)
    ball2_vy = random.randint(2, 5)

# Setter i gang ballene første gang:
reset_ball1()
reset_ball2()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    # La gravitasjonen jobbe:
    ball1_vy += GRAVITASJON
    ball2_vy += GRAVITASJON

    # Oppdater ball posisjoner
    ball1_x += ball1_vx
    ball1_y += ball1_vy
    ball2_x += ball2_vx
    ball2_y += ball2_vy

    # Reset baller når de når bunnen med nye tilfeldige hastigheter
    if ball1_y >= VINDU_HOYDE - BALL_RADIUS:
        reset_ball1()

    if ball2_y >= VINDU_HOYDE - BALL_RADIUS:
        reset_ball2()

    vindu.fill(WHITE)

    # Tegn ballene
    pg.draw.circle(vindu, RED, center=(int(ball1_x), int(ball1_y)), radius=BALL_RADIUS)
    pg.draw.circle(vindu, BLUE, center=(int(ball2_x), int(ball2_y)), radius=BALL_RADIUS)

    # Oppdater displayet
    pg.display.flip()
    clock.tick(FPS)

pg.quit()