import yatzy_utils as y

# MERK!! Se hvor ryddig struktur det er her! 
#   - yatzy_utils med funksjonene
#   - yatzy_test som tester at utils funker som det skal
# Nå er det bare å sy det sammen til et spill :)


def skaffYatzy():
    # Prøv å kast 3 ganger, og maksimer for å få 5 like
    # Returnerer True/False om den klarer det eller ikke
    kast = y.nyttKast()
    # print(f"---- Kast 1: {kast}")
    nr = 2
    for _ in range(2):
        # Prøv 2 ganger å maksimere for fem like:
        mestAv = y.flestForekomster(kast)
        kast = y.nullUt(kast, mestAv)
        # print(kast)
        kast = y.reKast(kast)
        # print(f"---- Kast {nr}: {kast}")
        nr += 1
    # Sjekk om vi fikk fem like / Yatzy:
    mestAv = y.flestForekomster(kast)
    return mestAv == 5 # Fancy måte å returnere True/False på

ant = 0
for i in range(100):
    if skaffYatzy():
        ant += 1

print(f"Vi fikk Yatzy {ant} ganger")





