import matplotlib.pyplot as plt
import numpy as np

filnavn = "DataFiler/valgdeltagelse.txt"

aarstall = []
valgdelt = []

with open(filnavn) as fil:
  for linje in fil:
    print(linje.strip())
    (aar, delt) = linje.strip().split(";")
    aarstall.append(aar)
    valgdelt.append(float(delt.replace(",", ".")))

print(aarstall)
print(valgdelt)

#plt.barh(aarstall, valgdelt)

fig, ax = plt.subplots()    # Angir dimensjoner for figure-objektet

# ax.barh(aarstall, valgdelt, label="Valgdeltagelse")
ax.plot(aarstall, valgdelt)

# x = np.arange(70,10)
# ax.set_yticks( [70, 75, 80]) # , ["70", "75", "80"] )                       # Legger til akseverdier
# ax.legend()                                               # Legger til beskrivelse
ax.set_xticklabels(aarstall, rotation = 50)

# fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet


# ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.show()         # Viser diagrammet

