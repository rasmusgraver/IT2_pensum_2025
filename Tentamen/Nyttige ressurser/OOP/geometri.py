class Rektangel:

    farger = ["blå", "rød", "grønn"]
    farge_indeks = 0

    def __init__(self, bredde, hoyde):
        self.bredde = bredde
        self.hoyde = hoyde
        self.farge = Rektangel.farger[Rektangel.farge_indeks % 3]
        Rektangel.farge_indeks += 1
        # Evt, istedet for den % operatoren over, så kunne man gjort:
        if Rektangel.farge_indeks >= len(Rektangel.farger):
            Rektangel.farge_indeks = 0

    def areal(self):
        return self.bredde * self.hoyde
    
    def omkrets(self):
        return self.bredde*2 + self.hoyde*2

class Kvadrat(Rektangel):

    def __init__(self, sidelengde):
        super().__init__(bredde=sidelengde, hoyde=sidelengde)
