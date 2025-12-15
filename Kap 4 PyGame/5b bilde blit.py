import pygame as pg
from constants import *
import os

VINDU_BREDDE = 800
VINDU_HOYDE = 600

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Eevee Demo")
clock = pg.time.Clock()

# Finn mappen der Python-filen ligger
current_dir = os.path.dirname(__file__)

def main():
    running = True

    # Last inn og forbered bildet ÉN gang før løkka
    bildesti = os.path.join(current_dir, "bilder", "eevee.png")
    try:
        original = pg.image.load(bildesti).convert_alpha()
    except Exception as e:
        print(f"Feil ved innlasting av bilde: {e}")
        return

    # Skaler bildet til ønsket bredde med bevart aspect ratio
    # target_width = 200
    ow, oh = original.get_size()
    # scale_factor = target_width / ow
    scale_factor = 0.15
    new_size = (int(ow * scale_factor), int(oh * scale_factor))
    bilde = pg.transform.smoothscale(original, new_size)  # smoothscale for bedre kvalitet

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(WHITE)
        vindu.blit(bilde, (20, 20))
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()