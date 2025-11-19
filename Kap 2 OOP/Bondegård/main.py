from bondegård import Bondegård
from dyr import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Opprett en bondegård: 
gården = Bondegård()

# Legg til noen kuer og høner på gården:
gården.leggTilDyr(Høne())
gården.leggTilDyr(Høne())
gården.leggTilDyr(Høne())
gården.leggTilDyr(Ku())
gården.leggTilDyr(Ku())
gården.leggTilDyr(Ku())

# Vis status for gården:
gården.visInfo()

# Melke kuene og hent egg fra hønene:
# Returner en ordbok(!) med tingene fra dyrene
# f.eks. 
"""
{
    "melk": 10,
    "egg": 3
}
"""

ting = []
for _ in range(20):
    ting.append(gården.samleTingFraDyrene())

# Lag en liste med tallene 1,2,3,4...20:
dager = list(range(1,21))
egg = []
melk = []

for ordbok in ting:
    egg.append(ordbok["egg"])
    melk.append(ordbok["melk"])

plt.plot(dager, egg, label="egg")

# Ta kontroll over x-aksen:
plt.xticks(dager[::2])

# Skap en alternativ y-akse: (merk: gca betyr "get current axis")
ax1 = plt.gca()
ax1.set_ylabel("Egg")
# Litt fancy syntax for å si at vi vil ha heltall y-ticks:
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))

# Hent en alternativ axe (tvilling-y-akse)
ax2 = ax1.twinx()
ax2.plot(dager, melk, color='orange', label="melk")
ax2.set_ylabel("Melk (liter)", color='black')
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))

plt.show()

