class Gjenstand:
    def __init__(self, navn: str, vekt: int) -> None:
        self.navn = navn
        self.vekt = vekt

    def __repr__(self) -> str:
        return f"{self.navn} ({self.vekt})"

class SpiseligGjenstand(Gjenstand):
    def __init__(self, navn: str, vekt: int, antall: int) -> None:
        super().__init__(navn, vekt)
        self.antall = antall

    def __repr__(self) -> str:
        return "*" + super().__repr__() + f" ant: {self.antall}"


stein = Gjenstand("Stein", 5)
lue = Gjenstand("Lue", 1)
kopp = Gjenstand("Kopp", 2)
print(kopp)
sjokolade = SpiseligGjenstand("Sjokolade", 1, 10)

gjenstander = [stein, lue, kopp, sjokolade]

gjenstander.append(Gjenstand("Sitteunderlag", 1))
print(gjenstander)


class Ryggsekk():
    """
    En ryggsekk som kan holde på Gjenstander
    """


    def __init__(self, kapasitet: int) -> None:
        self.kapasitet = kapasitet
        # MERK: Se måten man kan angi at dette er en liste av Gjenstander:
        self.gjenstander: list[Gjenstand] = []

    def leggTilGjenstand(self, gjenstand: Gjenstand):
        totalVekt = 0
        for g in self.gjenstander:
            totalVekt += g.vekt
        if totalVekt + gjenstand.vekt > self.kapasitet:
            print(f"Det er ikke plass til denne gjenstanden: {gjenstand} (Brukt {totalVekt} av {self.kapasitet})!")
        else:
            self.gjenstander.append(gjenstand)

    def spisMat(self) -> None:
        """ Går igjennom Gjenstander, og hvis de er spiselige
            så reduser antall med 1  """
        for g in self.gjenstander:
            if type(g) == SpiseligGjenstand:
                if g.antall > 0:
                    g.antall -= 1


sekk1 = Ryggsekk(20)
sekk2 = Ryggsekk(100)


for g in gjenstander:
    sekk1.leggTilGjenstand(g)

sekk1.leggTilGjenstand(Gjenstand("Mellom Stein", 10))
sekk1.leggTilGjenstand(Gjenstand("Liten fjær", 1))
