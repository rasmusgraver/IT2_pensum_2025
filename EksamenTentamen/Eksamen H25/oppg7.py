from pathlib import Path
import csv
from pprint import pprint

CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "Elever-fag.csv"

# Jeg vil bygge opp en slik struktur:
"""
fagomraader = {
 "Dansefag":
    {
        "2022-23": 232,
        "2023-24": 121,
        "2024-25": 141
    }
}
"""
fagomraader = {}

# En liten hjelpemetode
def tilTall(tekst:str) -> int:
    tekst = tekst.replace(" ", "")
    if tekst:
        return int(tekst)
    else:
        return 0


# Vanlige formater: 
#   windows-1252
#   utf-8-sig
#   iso-8859-1
# MERK! På denne eksamensoppgaven var fila rett og slett lagret feil, så norske tegn fungerer ikke :( 
with open(filnavn, encoding="windows-1252") as fil:
    filinnhold = csv.reader(fil, delimiter=",")
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*20)

    # Les en linje om gangen, hent ut verdiene, og oppdater ordboka:
    for rad in filinnhold:
        fagomraade = rad[1]
        ant_22_23 = tilTall(rad[3])
        ant_23_24 = tilTall(rad[4])
        ant_24_25 = tilTall(rad[5])
        if fagomraade in fagomraader.keys():
            # Øk de eksisterende verdiene:
            fagomraader[fagomraade]["2022-23"] += ant_22_23
            fagomraader[fagomraade]["2023-24"] += ant_23_24
            fagomraader[fagomraade]["2024-25"] += ant_24_25
        else:
            # Insert i ordboka:
            fagomraader[fagomraade] = {
                "2022-23": ant_22_23,
                "2023-24": ant_23_24,
                "2024-25": ant_24_25
            }



# pprint(fagomraader)

# Print "tabell-lignende"
print(f"{'Fagområde':40} |  22-23 |  23-24 |  24-25")
print("-"*70)
for fagomraade in fagomraader.keys():
    ant_22_23 = fagomraader[fagomraade]["2022-23"]
    ant_23_24 = fagomraader[fagomraade]["2023-24"]
    ant_24_25 = fagomraader[fagomraade]["2024-25"]
    tekst = fagomraade if len(fagomraade) <= 40 else fagomraade[:37] + "..."
    print(f"{tekst:40} | {ant_22_23:6} | {ant_23_24:6} | {ant_24_25:6}")

