import json
from pprint import pprint

filnavn = "DataFiler/norgeFrekvens.json"

# DISSE LINJENE MÅ DERE KUNNE! (Eller altså "ha i verktøykassa")
with open(filnavn, encoding="utf-8") as fil:
  bokstavDict:dict = json.load(fil)

pprint(bokstavDict)
print(f"Antall keys: {len(bokstavDict)}")

# OPPGAVE:
# Sorter etter antall forekomster, og hent ut top 10
# ... og plot dem som søylediagram! 

# Denne trengte vi ikke i denne oppgaven: (Men nyttig å vite om...)
# Sorterer på keys: sortertDict = dict(sorted(bokstavDict.items()))

# Sorterer på values: (Den er jo ganske "gresk", men nå har vi den i verktøykassa vår)
sortertDict = dict(sorted(bokstavDict.items(), key=lambda item: item[1], reverse=True))

# NB!!: MERK!!! pprint sorterer dict på keys av seg selv! Så her må vi bruke "vanlig print"!!
# print(sortertDict)

# Kan bruke mer fancy google stuff:
# from itertools import islice
# top10 = dict(islice(sortertDict.items(), 10))

# ELLER: Konverter til en liste og så ta de 10 første:
bokstavListe = list(sortertDict.items())
top10 = dict(bokstavListe[:10])

print("TOP 10 - Antall: ", len(top10))
print("="*20)
print(top10)


# Konverter til relativ frekvens: Må hente ut total forekomst av alle bokstaver:
totalForekomst = 0
for value in bokstavDict.values():
  totalForekomst += value

print(f"Total bokstav forekomst: {totalForekomst}")

# Gjør om vår top 10 til relativ frekvens:
for key in top10:
  antall = top10[key]
  relativForekomst = antall/totalForekomst
  # Lagrer ny verdi på denne nøkkelen:
  top10[key] = round(relativForekomst*100, 1) # Ganger med hundre for prosent


print("TOP 10 - med relativ prosent forekomst")
print("="*20)
print(top10)


# Og plotter bar-diagram av det:
import matplotlib.pyplot as plt

# plt.bar(top10.keys(), top10.values(), color="green")
# Legg til verdien på stolpene:
# for i, v in enumerate(top10.values()):
#    plt.text(i, v - 1, str(v) + " %", ha='center', va='bottom', color="white", fontsize=6)
# plt.xlabel("bokstav")
# plt.ylabel("Relativ frekvens i %")

# Litt større vindu:
plt.figure(figsize=(10, 6))  # bredde=10, høyde=6 tommer

# Penere å plotte liste i omvendt rekkefølge:
bokstaver = list(reversed(top10.keys()))
prosenter = list(reversed(top10.values()))

# Horisontalt søylediagram
plt.barh(bokstaver, prosenter, color="green", edgecolor="black")

# Legg til verdien på stolpene:
for i, v in enumerate(prosenter):
            plt.text(v - 0.5, i, f"{v} %", ha='center', va='center', color='white', fontsize=8)

plt.ylabel("bokstav")
plt.xlabel("Relativ frekvens i %")
plt.title("Frekvensanalyse norske bokstaver")
# Se om trengs: plt.tight_layout()
plt.show()
