from matplotlib.ticker import MultipleLocator
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

filnavn = "DataFiler/regnskap.csv"
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # NOTE! Denne er nice!
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*30)

    # Putter inn for jan, feb, mars i en liste med 3 tall (som starter som 0)
    totBok = {
        "mat":   [0]*3,
        "strøm": [0]*3
    }

    for rad in filinnhold: 
        # Henter mnd nr rett ut fra datoen (posisjon 4 i strengen):
        mnd = int(rad[0][4]) - 1 # Trekker fra 1 for å bruke som liste-index
        totBok[rad[1]][mnd] += int(rad[2])
        

    pprint(totBok)

    # Fra fancy gutt/jente plott fra boka:

    
fig, ax = plt.subplots(figsize=(7, 5))    # Angir dimensjoner for figure-objektet

mnder = ["jan", "feb", "mars"]

x = np.arange(len(mnder))

ax.bar(0.6+x-0.15, totBok["mat"], width=0.25, label="Mat", zorder=2)  # Lager stolpediagram Mat
ax.bar(0.6+x+0.15, totBok["strøm"], width=0.25, label="Strøm", zorder=2)  # Lager stolpediagram Strøm
ax.set_xticks(0.6+x, mnder, zorder=1)
ax.set_xlabel("Måned", fontsize=12)
ax.set_ylabel("Beløp", fontsize=12)
ax.legend(loc="center right")                           # Legger til beskrivelse
ax.set_title("Familien Olsens utgifter 2024", fontsize=16, fontweight="normal")

fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

plt.ylim(0, 10_000)
plt.xlim(0,3.5)
ax.grid(axis="y")  # Legger til rutenett (bare horisontale linjer)
ax.yaxis.set_major_locator(MultipleLocator(1000))  # Viser ticks på hver tusen
plt.tight_layout() # Prøver denne for å få den pen
plt.show()         # Viser diagrammet