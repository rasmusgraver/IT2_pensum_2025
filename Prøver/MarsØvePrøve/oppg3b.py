from pathlib import Path
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "studenter_i_hoyere_utdanning.csv"

# Bare lagrer denne for lesbarhet
INDEKS_2023 = 26

xer = []
yer = []

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*20)
    # Lagrer årstallene som x-verdier:
    for i in range(3, INDEKS_2023+1):
        xer.append(overskrifter[i])

    # Lagrer antallet studenter som y-verdier:
    for rad in filinnhold:
        fagfelt = rad[2]
        if rad[1] == "Kvinner" and fagfelt == "Naturvitenskapelige fag, håndverksfag og tekniske fag":
            for i in range(3, INDEKS_2023+1):
                yer.append(int(rad[i]))


# Ready to plot!
plt.plot(xer, yer)
plt.xticks(rotation=50, fontsize=8 )
plt.ylim([0,25000])
plt.grid(axis='y')  # Legger til gridlinjer for y-aksen
plt.title("Kvinner på Naturvitenskapelige fag, håndverksfag og tekniske fag")
plt.show()
