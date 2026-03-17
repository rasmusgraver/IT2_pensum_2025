from pathlib import Path
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "studenter_i_hoyere_utdanning.csv"

# Bare lagrer denne for lesbarhet
INDEKS_2023 = 26

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("Antall overskrifter:", len(overskrifter))

    # Lagrer radene i en liste:
    rader = list(filinnhold)

print("Jeg har nå", len(rader), "rader å jobbe med")
print("Antall kolonner i første rad:", len(rader[0]))
print("Første entries i første rad:", rader[0][0], "|" , rader[0][1], "|" , rader[0][2])

verdier = {}
aarstall = overskrifter[3:]

for rad in rader:
    studie = rad[2]
    if not studie in verdier.keys():
        # Start med en 0-liste for verdiene:
        verdier[studie] = [0 for i in range(INDEKS_2023-2)]
    # øk verdiene (enten det er kvinner eller menn):
    for i in range(INDEKS_2023-2):
        verdier[studie][i] += int(rad[i+3])

pprint(verdier)

print("Antall årstall:", len(aarstall))
for k, v in verdier.items():
    print(k, "med antall:", len(v))

