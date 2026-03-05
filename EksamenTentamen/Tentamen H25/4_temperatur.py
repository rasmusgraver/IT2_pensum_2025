import csv
import matplotlib.pyplot as plt
from datetime import datetime

filnavn = "DataFiler/temperatur.csv"

datoer = []
temperaturer = {
    "Oslo": [],
    "Bergen": [],
    "Trondheim": [],
}

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*20)
    for rad in filinnhold:
        # Bare sett inn én av datoene (den til Oslo)
        if rad[2] == "Oslo":
            datoer.append(datetime.strptime(rad[0], "%Y-%m-%d"))
        temperaturer[rad[2]].append(float(rad[1]))
 

byer = ["Oslo", "Bergen", "Trondheim"]
for by in byer:
    plt.plot(datoer, temperaturer[by], label=by)
plt.legend()

# sett etikett på y-aksen
plt.ylabel("Temperatur (°C)")

# roter x-etikettene 45 grader og unngå overlapping
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
