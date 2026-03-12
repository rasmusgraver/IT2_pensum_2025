from pathlib import Path
import csv
from pprint import pprint

CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "studenter_i_hoyere_utdanning.csv"


# Bare lagrer denne for lesbarhet
INDEKS_2023 = 26

# Vanlige formater:
#   windows-1252
#   utf-8-sig
#   iso-8859-1
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("Er dette 2023?", overskrifter[INDEKS_2023])
    if int(overskrifter[INDEKS_2023]) != 2023:
        raise ValueError("FEIL INDEKS for 2023!")
    print("-"*20)

    ant_2023 = 0
    for rad in filinnhold:
        fagfelt = rad[2]
        if fagfelt == "Naturvitenskapelige fag, håndverksfag og tekniske fag":
            ant = int(rad[INDEKS_2023])
            ant_2023 += ant
            print("La til", ant)


print("Antall studenter på NatVitensk fag i 2023 er", ant_2023)

