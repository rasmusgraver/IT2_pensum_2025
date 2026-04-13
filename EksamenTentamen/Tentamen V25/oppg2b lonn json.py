import json

filnavn = "DataFiler/manedslonn.json"

with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)

print(data)


# Bygger opp en liste med dataene vi trenger: (2024)
lonn_2024 = []

for yrke in data.keys():
  for kjonn in data[yrke].keys():
    for aar in data[yrke][kjonn].keys():
      print(f"{yrke} ({kjonn}) {aar}: {data[yrke][kjonn][aar]}")

      if aar == "2024":
        if kjonn == "Kvinner":
            # Tar kvinnelønn, for å fylle inn i dict senere:
            kvinnelonn = int(data[yrke][kjonn][aar])
        if kjonn == "Menn":
            manne_lonn = int(data[yrke][kjonn][aar])
            # Lager en dict med yrke og lønn for både menn og kvinner:
            yrke_dict = {
                "yrke": yrke,
                "Menn": manne_lonn,
                "Kvinner": kvinnelonn,
                "Prosent": round((kvinnelonn / manne_lonn) * 100, 1)
            }
            lonn_2024.append(yrke_dict)


# Printer det ut som en tabell:
print(f'{"Yrke":20} | {"Menn":10} | {"Kvinner":10} | {"Prosent":10}')
print("-"*60)
for lonn in lonn_2024:
    print(f'{lonn["yrke"]:20} | {lonn["Menn"]:10} | {lonn["Kvinner"]:10} | {lonn["Prosent"]:10}')

