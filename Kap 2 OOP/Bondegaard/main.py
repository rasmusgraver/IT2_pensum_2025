from bondegaard import Bondegård
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
# Merk den fancy liste splicing med [start:stop:step] - returnerer en ny liste
# - i dette tilfellet dagene (fra start til slutt), men bare annenhver av dem
plt.xticks(dager[::2])

# Skap en alternativ y-akse: (merk: gca betyr "get current axis")
ax1 = plt.gca()
ax1.set_ylabel("Egg")
# Litt fancy syntax for å si at vi vil ha heltall y-ticks:
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
# Trenger vanligivs ikke det her, men bare for å vise at man kan:
ax1.set_ylim(min(egg) - 1, max(egg) + 1)

# Hent en alternativ axe (tvilling-y-akse)
ax2 = ax1.twinx()
ax2.plot(dager, melk, color='orange', label="melk")
ax2.set_ylabel("Melk (liter)", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.spines['right'].set_color('orange')
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))

# Hent labels fra begge aksene
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.show()

