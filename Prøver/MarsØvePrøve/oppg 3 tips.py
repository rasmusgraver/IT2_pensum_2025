# Jeg lærte følgende triks når jeg jobbet med oppgave 3d:
#
#    # SE LENGER NED HER I PRAKSIS hvordan gjøre det:
#    # Lagrer radene i en liste:
#    rader = list(filinnhold)
#
# Dette gjør at man kan gå igjennom radene flere ganger - noe man
# sliter med på "den andre måten"
#    for rad in filinnhold:
#        ...


from pathlib import Path
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "studenter_i_hoyere_utdanning.csv"

# Vanlige formater:
#   windows-1252
#   utf-8-sig
#   iso-8859-1
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
