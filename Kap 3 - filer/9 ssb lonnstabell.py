import json
import matplotlib.pyplot as plt
import numpy as np

filnavn = "DataFiler/lonnstabell.json"

with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)

# print(data)

aarstall = list(data["dataset"]["dimension"]["Tid"]["category"]["label"].keys())

lonninger = data["dataset"]["value"]

lonningerMenn = lonninger[0:6]
lonningerKvinner = lonninger[6:]
print(aarstall)

print(lonningerMenn)
print(lonningerKvinner)

plt.plot(aarstall, lonningerMenn, label = "Menn")
plt.plot(aarstall, lonningerKvinner, label = "Kvinner")
plt.legend()
plt.ylabel("Månedslønn")
plt.xlabel("Årstall")

plt.show()

