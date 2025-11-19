from bondegård import Bondegård
from dyr import *
import matplotlib.pyplot as plt

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
dager = list(range(20))
egg = []
melk = []

for ordbok in ting:
    egg.append(ordbok["egg"])
    melk.append(ordbok["melk"])

plt.plot(dager, egg)
plt.plot(dager, melk)
plt.show()

