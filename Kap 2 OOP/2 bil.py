class Bil:
    def __init__(self, bilmerke = "Ford", aarsmodell = 2022, farge = "Svart"):
        self.bilmerke = bilmerke
        self.aarsmodell = aarsmodell
        self.farge = farge

    def visInfo(self):
        print(f"Jeg er en {self.farge} {self.bilmerke} fra {self.aarsmodell}")

ford = Bil("Ford", 2010)
ford.visInfo()

