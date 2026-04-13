import csv
import matplotlib.pyplot as plt
from pprint import pprint

filnavn = "DataFiler/manedslonn.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # Skipper første linje:
    # next(filinnhold)

    # Bekrefter at kolonne 12 (11) er 2024:
    overskrift = next(filinnhold)
    aarstall = overskrift[2:12]

    # Bygger opp en dict med dataene vi trenger: 
    #   yrke, med en liste over prosentene for alle årene
    yrker = {}

    for rad in filinnhold:
        kjonn = rad[1]
        if kjonn == "Kvinner":
            # Tar vare på yrket. Og på kvinnelønnen, for å fylle inn i prosenter senere:
            yrke = rad[0]
            kvinnelonn = rad[2:12]
        if kjonn == "Menn":
            manne_lonn = rad[2:12]
            # Lager en liste med prosenter for dette yrket:
            prosenter = []
            for i in range(len(kvinnelonn)):
                forhold = int(kvinnelonn[i]) / int(manne_lonn[i])
                prosenter.append(round(forhold * 100, 1))

            # Lager en dict med yrke og lønn for menn og kvinner:
            yrker[yrke] = prosenter


# pprint(yrker)
# print(aarstall)

# Plotter det som et linjediagram:
for yrke, prosent in yrker.items():
    plt.plot(prosent, marker='o', label=yrke)

plt.title("Kvinners lønn i prosent av menns lønn")
plt.xlabel("År")
plt.ylabel("Lønn i prosent av menns lønn")
plt.xticks(range(len(aarstall)), aarstall, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.ylim(75, 105) # Skaper litt "luft" til legends nederst
# plt.tight_layout()
plt.show()
