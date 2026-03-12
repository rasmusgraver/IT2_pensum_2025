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

# Vanlige formater:
#   windows-1252
#   utf-8-sig
#   iso-8859-1
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    for i in range(3, INDEKS_2023+1):
        xer.append(overskrifter[i])

    # Lagrer radene i en liste:
    rader = list(filinnhold)



kjonn = "Kvinner"
valg = input("Vil du se stats for kvinner eller menn? Svar med k eller m: ")
if valg[0] == "m" or valg[0] == "M":
    kjonn = "Menn"

print("Viser stats for", kjonn)

alleFagfelt = []
i = 0
for rad in rader:
    if rad[1] == "Menn":
        # Kommer dobbelt - viser bare for mennene
        fagfelt = rad[2]
        alleFagfelt.append(fagfelt)
        i += 1
        print(f"{i}: {fagfelt}")

valg = int(input("Skriv tallet til fagfeltet du vil vise fra listen over: "))
valgtFag = alleFagfelt[valg - 1]

for rad in rader:
    fagfelt = rad[2]
    if rad[1] == kjonn and fagfelt == valgtFag:
        for i in range(3, INDEKS_2023+1):
            yer.append(int(rad[i]))


plt.plot(xer, yer)
plt.xticks(rotation=50, fontsize=8 )
plt.ylim([0, max(yer) + 2000])
plt.grid(axis='y')  # Legger til gridlinjer for y-aksen
plt.title(f"{kjonn} på {valgtFag}")
plt.show()
