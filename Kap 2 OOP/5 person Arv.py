class Person:
    def __init__(self, navn: str, alder: int) -> None:
        self.navn = navn
        self.alder = alder

    def __repr__(self) -> str:
        """ Alltid lurt å implementere! Lar deg printe personer og lister av personer osv """
        return f"{self.navn} ({self.alder})"
    
    def siHei(self) -> None:
        print(f"Hei, jeg er en Person som heter {self.navn}")


class Elev(Person):

    def __init__(self, navn: str, alder: int) -> None:
        super().__init__(navn, alder)
        self.karakterer = []

    def leggTilKarakter(self, karakter: int):
        self.karakterer.append(karakter)


class Laerer(Person):
    # TODO: Kan legge på mer info om en Lærer her
    pass 


# Oppretter Objekter av klassen Person/Elev
rasmus = Person("Rasmus", 47)
ola = Elev("Ola", 18)

print(ola)
ola.leggTilKarakter(5)

# MERK! Fungerer ikke! Rasmus er en Person, ikke en Elev
# rasmus.leggTilKarakter(4)

# MEN! En elev ER en person!
ola.siHei()
