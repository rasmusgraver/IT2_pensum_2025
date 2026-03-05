
"""
Del 1 - Oppg 1 a)

class A:
    def __init__(self, farge):
        self.farge = farge

class B(A):
    def __init__(self, farge, lengde):
        self.farge = farge
        self.lengde = lengde


Svar: Det er rart/feil at B "lager sin egen self.farge". Den arver fra A,
så da skal den kalle på A sin init-funksjon, slik: 
    super().__init__(farge)

"""



class Kjoretoy:
    def __init__(self, aarsmodell):
        self.aarsmodell = aarsmodell

class Sykkel(Kjoretoy):
    def __init__(self, aarsmodell, ant_gir):
        super().__init__(aarsmodell)
        self.ant_gir = ant_gir
    
class Bil(Kjoretoy):
    def __init__(self, aarsmodell, drivstoff):
        super().__init__(aarsmodell)
        self.drivstoff = drivstoff


"""
Oppgave 1 b) Opprette sykkel og bil objekter:
"""
dbs = Sykkel(2020, 21)
ford = Bil(2022, "Bensin")

print(dbs)
print(ford)

"""
Oppgave 1 c) 

UPDATE 2025: Legg på __repr__(self) i stedet for __str__
Snakk med AI om hvorfor dette er bedre. 

2024 svar: Må legge på str funksjon for at print skal bli pent:
    def __str__(self):
        return f"Sykkel fra {self.aarsmodell} med {self.ant_gir} gir"
"""
