import pygame as pg
from constants import *


CELLE_STR = 100
VINDU_BREDDE = 3*CELLE_STR
VINDU_HOYDE = 3*CELLE_STR

pg.init()
vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
clock = pg.time.Clock()

# Dette er brettet vårt. Fyller det med x og o når de blir klikket på:
brett = [
    ["","",""],
    ["","",""],
    ["","",""]
]

def tegnBrett(vindu, brett):
    for x in range(3):
        for y in range(3):
            farge = WHITE
            if brett[y][x] == "o":
                farge = RED
            elif brett[y][x] == "x":
                farge = BLUE
            # Tegn en celle i rett farge:
            pg.draw.rect(vindu, farge, (x*CELLE_STR, y*CELLE_STR, CELLE_STR, CELLE_STR))

            # Tegn grå boks rundt:
            pg.draw.rect(vindu, GREY, (x*CELLE_STR, y*CELLE_STR, CELLE_STR, CELLE_STR), width=1)


# Returnerer "running" true/false
def sjekkSeier(brett) -> bool:
    running = True
    for i in range(3):
        # sjekk den ene veien:
        if brett[0][i] != "" and brett[0][i] == brett[1][i] == brett[2][i]:
            print("3 på rad!")
            print(f"{brett[0][i]} vant")
            running = False
    for i in range(3):
        # og den andre veien:
        if brett[i][0] != "" and brett[i][0] == brett[i][1] == brett[i][2]:
            print("3 på rad!")
            print(f"{brett[i][0]} vant")
            running = False
    # og de 2 kryssene:
    if brett[0][0] != "" and brett[0][0] == brett[1][1] == brett[2][2]:
        print("3 på rad!")
        print(f"{brett[1][1]} vant")
        running = False
    if brett[2][0] != "" and brett[0][2] == brett[1][1] == brett[2][0]:
        print("3 på rad!")
        print(f"{brett[1][1]} vant")
        running = False

    return running


playerX = True
running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            # MERK: 2 ulike måter å hente museklikk sin posisjon på under her. 
            # mouse.get_pos() eller event.pos (Merk: Siste er ikke en funksjon...)
            # Begge fungerer fint:
            mx, my = pg.mouse.get_pos()
            x = mx // CELLE_STR
            y = my // CELLE_STR
            # print(f"du trykket på rute {y},{x}")
            # print(f"Den ruten er lik {brett[y][x]}")
            # Bare lov å skrive til tomme ruter:
            if brett[y][x] == "":
                if playerX == True:
                    brett[y][x] = "x"
                    playerX = False
                else:
                    brett[y][x] = "o"
                    playerX = True
                


    vindu.fill(WHITE)
    tegnBrett(vindu, brett)
    running = sjekkSeier(vindu)


    # Disse har vi alltid til slutt:
    pg.display.flip()
    clock.tick(FPS)




# Til slutt, når main loopen (while running) er ferdig:
pg.quit()
