# Svar på oppgave 2 "Esport" her i denne fila
# MERK: Du trenger ikke å fjerne noe fra fila - bare legg til din
# kode under hver oppgave under her. 

from pathlib import Path
import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "esport_spillere.json"

# Les inn JSON-filen
with open(filnavn, 'r', encoding='utf-8') as fil:
    spillere = json.load(fil)

# ==========================================
# DEL 1: GRUNNLEGGENDE
# ==========================================

print("Hentet inn", len(spillere))

# Oppgave 1.1
print("--- Oppgave 1.1 ---")
# Print navn og antall poeng om den første spiller i lista:
# Din kode her
print("Spiller:", spillere[0]["navn"])
print("Poeng:  ", spillere[0]["poeng"])


# Oppgave 1.2
print("\n--- Oppgave 1.2 ---")
# Print ut alle som kommer fra Norge: 
# Din kode her
print("Spillere fra Norge:")
for spiller in spillere:
    if spiller["land"] == "Norge":
        print(spiller["navn"])


# Oppgave 1.3
print("\n--- Oppgave 1.3 ---")
# Tell, og skriv ut, hvor mange som er 20 år eller yngre:
# Din kode her
antall = 0
for spiller in spillere:
    if spiller["alder"] <= 20:
        antall += 1
print("Det er ", antall, "spillere som er 20 år eller yngre")




# ==========================================
# DEL 2: FINNE EKSTREMVERDIER
# ==========================================

# Oppgave 2.1
print("\n--- Oppgave 2.1 ---")
# Finn den spilleren som har flest poeng:
# Din kode her
maksSpiller = spillere[0]
maksPoeng = 0
for spiller in spillere:
    if spiller["poeng"] > maksPoeng:
        maksPoeng = spiller["poeng"]
        maksSpiller = spiller
print("Spilleren som har flest poeng:", maksSpiller["navn"], "med", maksSpiller["poeng"])



# ==========================================
# DEL 3: PLOTTING
# ==========================================

# Oppgave 3.1 - Stolpediagram
#Lag et stolpediagram som viser poengene til hver spiller.
# Din kode her
xer = []
yer = []
for spiller in spillere:
    xer.append(spiller["navn"])
    yer.append(spiller["poeng"])

farger = ["blue", "green"]
plt.bar(xer, yer, color=farger)
plt.xticks(rotation=80, fontsize=8)
# plt.xlabel("Spillere")
plt.ylabel("Poeng")
plt.title("Esport-spillere med poeng")
plt.tight_layout()

plt.show()
