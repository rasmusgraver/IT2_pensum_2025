"""
Siden vi kom så nærme det, så måtte vi ta en titt innom dette kjente
problemet: https://en.wikipedia.org/wiki/Knapsack_problem 

Oppgave: Fyll en ryggsekk med mest mulig verdifulle gjenstander, innenfor
kapasiteten til sekken
"""

import random

class Gjenstand:
    def __init__(self, navn: str, vekt: int, verdi: int) -> None:
        self.navn = navn
        self.vekt = vekt
        self.verdi = verdi

    def __repr__(self) -> str:
        return f"{self.navn} ({self.vekt})"
"""
items = [
    {"name": "Laptop", "weight": 3, "value": 2000},
    {"name": "Headphones", "weight": 1, "value": 250},
    {"name": "Coffee mug", "weight": 1, "value": 100},
    {"name": "Notepad", "weight": 2, "value": 300},
    {"name": "Camera", "weight": 2, "value": 1500},
]
capacity = 5 """
# Optimal løsning: Laptop (3,2000) + Camera (2,1500) = 3500
# Optimal value = 3500

items = [
    {"name": "Gold bar", "weight": 10, "value": 5000},
    {"name": "Silver bar", "weight": 5, "value": 1500},
    {"name": "Bronze bar", "weight": 3, "value": 900},
    {"name": "Diamond", "weight": 1, "value": 2000},
    {"name": "Emerald", "weight": 2, "value": 1800},
]
capacity = 10
# Optimal løsning: Gold bar (10,5000) alene gir 5000
# Men Diamond (1,2000) + Emerald (2,1800) + Silver (5,1500) + Bronze (2 igjen) = 5300 maks
# Men 1+2+5 = 8, vi kan legge til Bronze (3) da blir 11, for mye
# Bedre: Diamond (1,2000) + Emerald (2,1800) + Silver (5,1500) + Bronze (3,900) = 11 (for tungt)
# Så beste kombinasjon innen 10 er: Diamond (1,2000) + Emerald (2,1800) + Silver (5,1500) = weight 8, value 5300
# Optimal value = 5300

gjenstander: list[Gjenstand] = []
for item in items:
    gjenstander.append(Gjenstand(item["name"], item["weight"], item["value"]))

print(gjenstander)

class Ryggsekk():
    """
    En ryggsekk som kan holde på Gjenstander
    """

    def __init__(self, kapasitet: int) -> None:
        self.kapasitet = kapasitet
        # MERK: Se måten man kan angi at dette er en liste av Gjenstander:
        self.gjenstander: list[Gjenstand] = []

    def __repr__(self) -> str:
        retStr = f"Ryggsekk med"
        for g in self.gjenstander:
            retStr += f" {g.navn} ({g.vekt}, {g.verdi}) "
        retStr += f". Totalverdi: {self.totalVerdi()}"
        return retStr

    def totalVerdi(self) -> int:
        tot = 0
        for g in self.gjenstander:
            tot += g.verdi

        return tot

    def leggTilGjenstand(self, gjenstand: Gjenstand):
        totalVekt = 0
        for g in self.gjenstander:
            totalVekt += g.vekt
        if totalVekt + gjenstand.vekt > self.kapasitet:
            # Gjør det bare i stillhet...
            # print(f"Det er ikke plass til denne gjenstanden: {gjenstand} (Brukt {totalVekt} av {self.kapasitet})!")
            pass
        else:
            self.gjenstander.append(gjenstand)


sekk1 = Ryggsekk(capacity)

for g in gjenstander:
    sekk1.leggTilGjenstand(g)

# print(sekk1)

besteTotal = sekk1.totalVerdi()
besteStr = str(sekk1)

print("Bestetotal oppstart:", besteTotal)
print("Beste sekk oppstart:", besteStr)

# Prøver med hundre random forsøk, og ser om treffer optimalt:
for _ in range(100):
    sekk = Ryggsekk(capacity)
    # Må lage en kopi av gjenstandlista, fordi vi skal poppe fra den (ødellegge den)
    gjenstandListe = list(gjenstander)
    for i in range(len(gjenstander)):
        # Legger til en tilfeldig gjenstand i sekken (MERK: Om det ikke er plass, så blir det bare silently ignored)
        tilfIndex = random.randrange(len(gjenstandListe))
        sekk.leggTilGjenstand(gjenstandListe.pop(tilfIndex))

    # Sjekk om dette var en ny bestesekk:
    if sekk.totalVerdi() > besteTotal:
        besteTotal = sekk.totalVerdi()
        besteStr = str(sekk)


print("Bestetotal:", besteTotal)
print("Beste sekk:", besteStr)
