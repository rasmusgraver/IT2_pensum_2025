import pygame as pg

# Kall pg init her også, for sikkerhetsskyld (Kan fint kalle på denne flere ganger i et PyGame spill)
pg.init()

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 40, bold=False)

def skriv_tekst(screen, x, y, tekst, farge, bakgrunnsfarge=None):
    """ Skriver en tekst til skjermen. Kan angi en bakgrunnsfarge om du vil.
        - tekst er teksten som skrives
        - x,y er koordinatene der du vil ha teksten på skjermen
        - farge er tekst-fargen
        - bakgrunnsfarge er bakrunnsfargen på teksten, optional
    """
    if bakgrunnsfarge == None:
        tekst_surface = font.render(tekst, True, farge)
        screen.blit(tekst_surface, (x, y))
    else:
        # Lager en tekst-surface:
        tekst_surface = font.render(tekst, True, farge)
        # Lager en bakgrunns-surface:
        back_surface = pg.Surface(tekst_surface.get_size())
        back_surface.fill(bakgrunnsfarge)
        # Putter teksten på bakgrunnen:
        back_surface.blit(tekst_surface, (0, 0))
        # Tegner bakgrunnen på skjermen:
        screen.blit(back_surface, (x, y))


