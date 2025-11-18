import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "DataFiler/baerum.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)

    print("-"*20)

    aarst = []
    bef = []

    for rad in filinnhold:
        # print(rad)
        aarst.append(int(rad[0]))
        bef.append(int(rad[1]))
 

plt.xlabel("Årstall")
plt.ylabel("Befolkning")
# ax.set_xticklabels(xticks, rotation = 50)
plt.ylim([0,140000])
plt.plot(aarst, bef)

plt.show()
