WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREY = (170,170,170)
RED = (255, 0, 0)
GREEN = (0, 225, 0)
GREEN_DARK = (0, 100, 0)
BLUE = (0, 0, 255)
PURPLE = (200,0,200)
ORANGE = (255,200,0)
YELLOW = (230,220,0)

# Liste med alle fargene (uten hvit og svart)
FARGER = [RED, GREEN, GREEN_DARK, BLUE, PURPLE, ORANGE, YELLOW]

FPS = 60

# Definer andre konstanter som celle størrelser osv her:
RUTE_STR = 60
GAP = 10

ANT_X = 4
ANT_Y = 4

# Definerer størrelsen på pygame-vinduet:
GAME_WIDTH = ANT_X * (RUTE_STR + GAP)

WIDTH = GAME_WIDTH + 200 # Setter av plass til knappene
HEIGHT = ANT_Y * (RUTE_STR + GAP)

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = GAME_WIDTH + 50
MENY_YSTART = 50
MENY_YAVSTAND = 80  # y-avstand for hver knapp

