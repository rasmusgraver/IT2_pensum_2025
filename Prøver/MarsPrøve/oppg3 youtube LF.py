from pathlib import Path
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "YouTubeStats.csv"

# Vanlige formater:
#   windows-1252
#   utf-8-sig
#   iso-8859-1
with open(filnavn, encoding="windows-1252") as fil:
    filinnhold = csv.reader(fil, delimiter=",")
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("Antall overskrifter:", len(overskrifter))

    # Lagrer radene i en liste:
    rader = list(filinnhold)

print("Jeg har nå", len(rader), "rader å jobbe med")
print("Antall kolonner i første rad:", len(rader[0]))
print("Første entries i første rad:", rader[0][0], "|" , rader[0][1], "|" , rader[0][2])



# Oppgave a) Print ut de 4 YouTuberne fra Sverige:
print()
print("***** Oppgave a) *********")
for rad in rader:
    if rad[7] == "Sweden":
        print(f"- {rad[1]} med {int(rad[2])/1E6} millioner subscribers")



# Oppgave b) Finn de 5 landene med flest youtubere:
print()
print("***** Oppgave b) *********")
land_dict = {}
for rad in rader:
    land = rad[7]
    if not land in land_dict.keys():
        land_dict[land] = 0
    # Oppgave a: Spør bare om antall oppføringer
    land_dict[land] += 1

# Fjern "nan"
land_dict.pop("nan")

# pprint(land_dict)

sortertList = sorted(land_dict.items(), key=lambda item: item[1], reverse=True)
# print(sortertList)

# Bare 5 første:
fem_storste = sortertList[0:5]
#print(fem_storste)
for k, v in fem_storste:
    print(f"{k:20} med {v} YouTubere")



