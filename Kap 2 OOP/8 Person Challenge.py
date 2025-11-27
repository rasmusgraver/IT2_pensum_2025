# litt teknisk den her: Det er for å få til at man kan bruke Person i input parametere osv
from __future__ import annotations

from datetime import datetime


class Person:

    def __init__(self, navn:str, fdato:str="", mor:Person|None = None, far:Person|None = None) -> None:
        self.navn = navn
        self.mor:Person|None = None
        self.far:Person|None = None
        self.barn:list[Person] = []
        if fdato:
            self.fdato = datetime.strptime(fdato, "%d.%m.%Y")
        else:
            self.fdato = None
        if mor:
            self.setMor(mor)
        if far:
            self.setFar(far)

    def __repr__(self) -> str:
        datostr = self.fdato.strftime("%d.%m.%Y") if self.fdato else "-"
        return f"{self.navn} ({datostr})"
    
    # Enkleste måten å få barn.sort() til å fungere: Fortell hvordan to Personer sammenliknes med "<":
    def __lt__(self, p:Person):
        if not self.fdato:
            return 1
        if not p.fdato:
            return -1
        return self.fdato < p.fdato

    def setMor(self, mor:Person):
        self.mor = mor
        mor.leggTilBarn(self)

    def setFar(self, far:Person):
        self.far = far
        far.leggTilBarn(self)

    def leggTilBarn(self, b:Person) -> None:
        self.barn.append(b)
        # Hver gang vi legger til et barn sorterer vi barnelista, så de eldste kommer først:
        self.barn.sort()

    def søsken(self) -> list[Person]:
        if self.mor:
            barna = list(self.mor.barn) # NB!! LAG en kopi av lista først!
            barna.remove(self)
            return barna
        else:
            return []
        
    def eldsteBarn(self) -> Person|None:
        if self.barn:
            return self.barn[0]
        
# TODO legg fødselsdato på personene
# Sorter barna etter fødselsdato
# Lag funksjon "eldsteBarn()" på Person

mamma = Person("Mamma", "12.03.1968")
pappa = Person("Pappa", "20.11.1965")
ole = Person("Ole", "05.06.1992", mamma, pappa)
kari = Person("Kari", "17.09.1990", mamma, pappa)
tredjemann = Person("Tredjemann", "17.09.1997", mamma, pappa)
baby = Person("Baby", "22.05.2024", kari)


print(f"Ole: {ole}. Oles mor: {ole.mor} Oles far: {ole.far}")
print(f"mammas barn: {mamma.barn}")
print(f"Oles søsken: {ole.søsken()}")
print(f"mammas barn (2): {mamma.barn}")
print(f"Baby sin mor sin mor: {baby.mor.mor}")
