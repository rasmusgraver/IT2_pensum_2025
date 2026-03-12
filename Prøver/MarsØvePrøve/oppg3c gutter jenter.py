from pathlib import Path
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "studenter_i_hoyere_utdanning.csv"

# Bare lagrer denne for lesbarhet
INDEKS_2023 = 26

# Våre 3 lister (som skal bli være lange)
alleFagfelt = []
antallGutter = []
antallJenter = []

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*20)

    for rad in filinnhold:
        if rad[1] == "Menn":
            # Vi benytter oss av at radene kommer i samme rekkefølge 2 ganger - først menn:
            alleFagfelt.append(rad[2])
            antallGutter.append(int(rad[INDEKS_2023]))
        else:
            # Vi benytter oss av at fagfeltet allerede er lagt inn i sin liste
            antallJenter.append(int(rad[INDEKS_2023]))
            


fig, ax = plt.subplots(figsize=(10, 5))    # Angir dimensjoner for figure-objektet

y = np.arange(len(alleFagfelt))

ax.barh(y+0.2, antallJenter, height=0.4, label="Jenter", color="pink")  # Lager stolpediagram jenter
ax.barh(y-0.2, antallGutter, height=0.4, label="Gutter", color="blue")  # Lager stolpediagram gutter
ax.set_yticks(y, alleFagfelt)                             # Legger til akseverdier
ax.legend()                                               # Legger til beskrivelse

fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.show()         # Viser diagrammet
