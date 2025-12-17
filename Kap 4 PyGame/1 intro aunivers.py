import pygame as pg

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

print(type(vindu))

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen hvit
    vindu.fill((255, 255, 255))

    # Tegner en sirkel
    pg.draw.circle(vindu, (255, 0, 0), (100, 250), 50)
    # Tegner et rektangel
    pg.draw.rect(vindu, (0, 255, 0), (200, 250, 70, 90))
    # Tegner en ellipse
    pg.draw.ellipse(vindu, (0, 0, 255), (300, 250, 90, 60))
    # Tegner en linje
    pg.draw.line(vindu, color=(200, 0, 200), start_pos=(400, 100), end_pos=(420, 400), width=5)

    # Lager en tekst i form av et bilde og legger til bildet i vinduet
    bilde = font.render("Heisann!", True, (50, 50, 50))
    vindu.blit(bilde, (400, 20))

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()