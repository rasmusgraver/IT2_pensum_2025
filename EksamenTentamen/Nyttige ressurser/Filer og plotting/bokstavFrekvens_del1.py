from pathlib import Path
from pprint import pprint
import json

CURRENT_DIR = Path(__file__).parent
txtFilNavn = CURRENT_DIR / "norge.txt"
jsonFilNavn = CURRENT_DIR / "norgeFrekvens.json"

# Starter med en tom dictionary:
bokstavDict = {}

with open(txtFilNavn, encoding="utf-8") as fil:
  innhold = fil.read()
  for bokstav in innhold:
    # Sjekker at det er en bokstav (isalpha) (og ikke et tegn eller mellomrom eller tall)
    if bokstav.isalpha():
      # Gjør om til liten:
      b = bokstav.lower()
      # Hvis den ikke finnes i dict, så legger vi den til:
      if not b in bokstavDict:
        bokstavDict[b] = 0
      # og øker forekomsten med 1:
      bokstavDict[b] += 1

# MERK: pprint sorterer dict på keys!!
pprint(bokstavDict)
print(f"Antall keys: {len(bokstavDict)}")

# Lagre resultatet til en json fil:
json_object = json.dumps(bokstavDict, indent=4)
with open(jsonFilNavn, "w") as outfile:
    outfile.write(json_object)

# MERK: Denne json fila bruker vi videre i neste oppgave: "leseJSON"