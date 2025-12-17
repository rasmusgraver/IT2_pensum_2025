import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "DataFiler/temp.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=",")

    overskrifter = next(filinnhold)
    print(overskrifter)

    print("-"*20)

    dager = []
    temps = []

    for rad in filinnhold:
        # print(rad)
        dager.append(str(rad[0]))
        temps.append(int(rad[1]))
 

plt.xlabel("Dag")
plt.ylabel("Temperatur")
# ax.set_xticklabels(xticks, rotation = 50)
# plt.ylim([0,140000])
plt.plot(dager, temps)
# farger = ["red", "orange", "yellow", "green", "blue"]
# plt.bar(dager, temps, color=farger)

plt.show()
