from dyr import *

class Bondegård:

    def __init__(self) -> None:
        self.dyr:list[Dyr] = []

    def leggTilDyr(self, dyr:Dyr):
        self.dyr.append(dyr)

    def visInfo(self):
        print(f"En bondegård med følgende dyr: {self.dyr}")

    def samleTingFraDyrene(self) -> dict:
        ordbok = {
            "melk": 0,
            "egg": 0
        }
        for d in self.dyr:
            if type(d) == Høne:
                ordbok["egg"] += d.leggEgg()
            if type(d) == Ku:
                ordbok["melk"] += d.giMelk()

        return ordbok