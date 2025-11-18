import json
from pprint import pprint 
import matplotlib.pyplot as plt

"""
Felter i dataene:
    model - navn på bilen
    mpg Miles/(US) gallon
    cyl Number of cylinders
    disp Displacement (cu.in.)
    hp Gross horsepower
    drat Rear axle ratio
    wt Weight (1000 lbs)
    qsec 1/4 mile time
    vs Engine (0 = V-shaped, 1 = straight)
    am Transmission (0 = automatic, 1 = manual)
    gear Number of forward gears
    carb Number of carburetors
"""

filnavn = "DataFiler/mtcars.json"

with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)

biler = []
ant_cyl = {}
for bil in data:
    if int(bil["hp"]) > 200:
        print( "HP: " + str(bil["hp"]) + ": " + bil["model"] )
        biler.append(bil)
    # Legger til i ant_cyl (for alle biler):
    # Hvis vi har en ny "antall cylindre", så opprett den i ant_cyl ordboka:
    if not bil["cyl"] in ant_cyl:
        ant_cyl[bil["cyl"]] = 0
    # Øk antall for den aktuelle "antall cylindre": (nå som vi vet at den finnes i ordboka)
    ant_cyl[bil["cyl"]] += 1


# Bruker denne til sorted funksjonen under:
def sort_key(b):
	return b["hp"]

# NB: Lær dette! Se så elegant det er! :)
biler_sortert = sorted(biler, key=sort_key, reverse=False)

print("SORTED")
print("="*30)
for bil in biler_sortert:
    print("HP: " + str(bil["hp"]) + ": " + bil["model"] )


# ============================================
# over til antall cylindere og sektor-diagram:
# ============================================

# Returnerer den første verdien i tuple (som er antall sylindre):
def sort_key_cyl(cyl):
    return cyl[0]

# Sorter ant_cyl (ut i fra den første verdien - altså antall sylindre):
# (Merk bruken av dict(sorted(...)) for å lage en ny ordbok med sorterte verdier)
ant_cyl_sortert = dict(sorted(ant_cyl.items(), key=sort_key_cyl, reverse=False))

# Lager et sektordiakgram/kakediagram med antall cylindre:
plt.pie(ant_cyl_sortert.values(), labels=ant_cyl_sortert.keys(), autopct='%1.1f%%', startangle=90, counterclock=False)
plt.title("Antall sylindre")
plt.show()

