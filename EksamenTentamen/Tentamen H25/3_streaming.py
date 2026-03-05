import json
from pprint import pprint 
import matplotlib.pyplot as plt


filnavn = "DataFiler/streaming.json"

with open(filnavn, encoding="utf-8") as f:
    data = json.load(f)


pprint(data)

tjenester = {}
for rad in data:
    tjenesteNavn = rad["tjeneste"]
    if tjenesteNavn in tjenester:
        tjenester[tjenesteNavn] += 1
    else:
        tjenester[tjenesteNavn] = 1


pprint(tjenester)

colors = ["blue", "purple", "red", "lightblue"]
plt.bar(list(tjenester.keys()), list(tjenester.values()), color=colors)

plt.show()
