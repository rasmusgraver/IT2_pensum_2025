# MERK DERE DENNE!
#   Lagrer radene i en liste:
#   rader = list(filinnhold)
#
# Dette gjør at man kan gå igjennom radene flere ganger - noe man
# sliter med på "den andre måten"
#    for rad in filinnhold:
#        ...


from pathlib import Path
import csv
from pprint import pprint
# pprint er "handy" om man skal printe ut mye data, f eks en stor ordbok
import matplotlib.pyplot as plt
import numpy as np

# La oss bruke denne måten nå, så funker det uansett hvor man står og kjører programmet:
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
    # hopp over en ekstra rad før vi henter ut resten av innholdet:
    # next(filinnhold)

    # Lagrer radene i en liste:
    rader = list(filinnhold)


# Kast ut den siste raden:
# rader.pop()


print("Jeg har nå", len(rader), "rader å jobbe med")
print("Antall kolonner i første rad:", len(rader[0]))
print("Første entries i første rad:", rader[0][0], "|" , rader[0][1], "|" , rader[0][2])
ANT_KOL = len(overskrifter)
if len(rader[0]) != ANT_KOL:
    print("WARNING! Det er ulikt antall kolonner i overskrifter og første rad")

# Når du skal gå gjennom radene:
for rad in rader:
    # Første verdi i raden:
    kol1 = rad[0]
    # siste verdi i raden:
    sisteVerdi = rad[ANT_KOL-1]
    sisteOverskrift = overskrifter[ANT_KOL-1]
    # print(f"Første verdi: {kol1}. Siste: {sisteOverskrift}: {sisteVerdi}")
    # print("Her er en rad", rad)
    # print("og den første verdien i raden:", rad[0])

