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

print("Hentet inn data med lengde:", len(spillere))

# Oppgave 1.1
print("--- Oppgave 1.1 ---")
# Print navn og antall poeng til den første spilleren i json-fila:
# Din kode her


# Oppgave 1.2
print("\n--- Oppgave 1.2 ---")
# Print ut navnet til alle som kommer fra Norge: 
# Din kode her



# Oppgave 1.3
print("\n--- Oppgave 1.3 ---")
# Tell, og skriv ut, hvor mange som er 20 år eller yngre:
# Din kode her



# ==========================================
# DEL 2: FINNE EKSTREMVERDIER
# ==========================================

# Oppgave 2.1
print("\n--- Oppgave 2.1 ---")
# Finn den spilleren som har flest poeng:
# Din kode her



# ==========================================
# DEL 3: PLOTTING
# ==========================================

# Oppgave 3.1 - Stolpediagram
# Lag et stolpediagram som viser poengene til hver spiller.
# Din kode her
