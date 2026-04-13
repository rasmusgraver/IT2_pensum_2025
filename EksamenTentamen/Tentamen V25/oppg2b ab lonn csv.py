import csv
import matplotlib.pyplot as plt
from pprint import pprint

filnavn = "DataFiler/manedslonn.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # Skipper første linje:
    # next(filinnhold)

    # Bekrefter at kolonne 12 (11) er 2024:
    aarstall = next(filinnhold)
    print(aarstall[11]) # 2024 

    # Bygger opp en liste med dataene vi trenger: (2024)
    lonn_2024 = []
    for rad in filinnhold:
        kjonn = rad[1]
        if kjonn == "Kvinner":
            # Tar vare på yrket og kvinnelønn, for å fylle inn i dict senere:
            yrke = rad[0]
            kvinnelonn = int(rad[11])
        if kjonn == "Menn":
            # Lager en dict med yrke og lønn for menn og kvinner:
            manne_lonn = int(rad[11])
            yrke_dict = {
                "yrke": yrke,
                "Menn": manne_lonn,
                "Kvinner": kvinnelonn,
                "Prosent": round((kvinnelonn / manne_lonn) * 100, 1)
            }
            lonn_2024.append(yrke_dict)

# pprint(lonn_2024)

# Printer det ut som en tabell:
print(f'{"Yrke":20} | {"Menn":10} | {"Kvinner":10} | {"Prosent":10}')
print("-"*60)
for lonn in lonn_2024:
    print(f'{lonn["yrke"]:20} | {lonn["Menn"]:10} | {lonn["Kvinner"]:10} | {lonn["Prosent"]:10}')

