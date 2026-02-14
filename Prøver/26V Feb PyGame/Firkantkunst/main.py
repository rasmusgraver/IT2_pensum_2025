import pygame as pg
from firkant import Firkant
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

# Her lagrer vi de permantene firkant objektene våre (etterhvert som vi tegner dem)
firkanter:list[Firkant] = []


# Må lagre hvor brukeren startet trykket
x_start = 0
y_start = 0

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Lagre start-posisjon for firkanten
            x_start, y_start = event.pos
        elif event.type == pg.MOUSEBUTTONUP:
            # Slutt-posisjon for firkanten:
            x, y = event.pos
            # Finn hva som er minst av start og stop posisjon:
            x1 = min(x, x_start)
            x2 = max(x, x_start)
            y1 = min(y, y_start)
            y2 = max(y, y_start)
            if x2-x1 > 5 and y2-y1 > 5:
                # "Stor nok": Lag ny firkant:
                firkanter.append(Firkant(x1, y1, x2, y2))
            else:
                # Bare et "mini-trykk" (kunne kanksje her også bare sagt at om x1 == x2 or y1 == y2)
                # fjern den øverste (siste i lista) firkanten vi klikket på:
                # (Legg merke til at vi reverserer lista vi itererer over):
                for firkant in firkanter[::-1]:
                    if firkant.rect.collidepoint(x1,y1):
                        firkanter.remove(firkant)
                        # Skal bare fjerne den øverst, så break her:
                        break
            # Set disse til null igjen, så vi slutter å tegne midlertidige firkanter:
            # (og er klare for et nytt trykk, med nye start-posisjoner):
            x_start, y_start = 0,0


    vindu.fill(WHITE)

    for firkant in firkanter:
        # Trengs ikke i dag... firkant.oppdater()
        firkant.tegn(vindu)


    # Tegn en midlertidig firkant så lenge vi har fått mousebuttondown og ikke up enda:
    if x_start and y_start:
        x,y = pg.mouse.get_pos()
        x1 = min(x, x_start)
        x2 = max(x, x_start)
        y1 = min(y, y_start)
        y2 = max(y, y_start)
        # Lager et midlertidig rect objekt (trengs egentlig ikke, men koden blir penere):
        rect = pg.Rect(x1, y1, (x2-x1), (y2-y1))
        pg.draw.rect(vindu, BLACK, rect, width=2)



    # Har alltid med disse til slutt:
    pg.display.update()
    clock.tick(FPS)


# While running er false - avslutt pygame på en ryddig måte (lukk vinduet osv):
pg.quit()
