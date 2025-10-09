class Elev:
    def __init__(self, navn, karakterer):
        self.navn = navn
        self.karakterer = karakterer  # liste med tall, f.eks. [5, 6, 4]

    def __repr__(self):
        """ En metode for å fortelle Python hvordan en elev skal vises
            når den blir printet.
            PRØV print(skole.elever) med og uten denne repr metoden!
        """
        return self.navn + f" ({self.snitt():.2f})"

    def __lt__(self, other):
        """ Sammenligner en elev med en annen elev.
            Hvordan!? Det er opp til oss! Her bruker vi snittet. 
            MERK: Dette avgjør hvordan sort() sorderer en liste med elever!
        """
        return self.snitt() < other.snitt()
        # Eller kunne gjort det med navn slik: return self.navn < other.navn

    def snitt(self):
        return sum(self.karakterer) / len(self.karakterer)


class Skole:
    def __init__(self, navn, elever):
        self.navn = navn
        self.elever = elever  # liste ev Elev objekter

    def leggTilElev(self, elev):
        self.elever.append(elev)

    def skrivUtAlleElever(self):
        print("Elever på skolen:")
        for elev in self.elever:
            print("-", elev) # MERK!!! Her brukes __repr__ funksjonen til å printe eleven!

    def snittKarakter(self):
        # finn totalt antall karakterer og summen av alle
        total_sum = 0
        total_antall = 0
        for elev in self.elever:
            total_sum += sum(elev.karakterer)
            total_antall += len(elev.karakterer)
        if total_antall == 0:
            return 0
        return total_sum / total_antall



e1 = Elev("Emma", [5, 6, 4])
e2 = Elev("Jonas", [3, 4, 5])
e3 = Elev("Sara", [6, 5, 6])

skole = Skole("Nadderud", [e1, e2, e3])

# kan også legge til flere:
skole.leggTilElev(Elev("Gunnar", [2,3,1]))

skole.skrivUtAlleElever()
print("Gjennomsnittskarakter for skolen:", round(skole.snittKarakter(), 2))


# Vi har implementer __lt__ (<) funksjonen. Vi kan da sammenligne med den:
if e1 < e2:
    print(f"{e1} har dårligere snitt enn {e2}")
else:
    print(f"{e1} har bedre snitt enn {e2}")

# OG! Nå kan vi også bruke sort(), fordi vi har definert __lt__:
skole.elever.sort()

print(skole.elever)
