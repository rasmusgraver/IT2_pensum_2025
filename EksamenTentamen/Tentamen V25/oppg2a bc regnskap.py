from pathlib import Path
import csv
import matplotlib.pyplot as plt
from pprint import pprint

# La oss bruke denne måten nå, så funker det uansett hvor man står og kjører programmet:
CURRENT_DIR = Path(__file__).parent
filnavn = CURRENT_DIR / "utgifter.csv"


# Summerer opp for mat og strøm hver for seg, for hver av de tre månedene:
mat = [0, 0, 0]
strøm = [0, 0, 0]

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # Skipper første linje:
    next(filinnhold)

    for rad in filinnhold:
        # print(rad) # Debugging
        # Kjører gjennom hver rad i filen:
        # print(f"Rad: {rad}") # Debugging
        maaned = int(rad[0].split(".")[1]) - 1

        # Summerer opp for mat og strøm hver for seg:
        # Rad 0 er dato, rad 1 er type, rad 2 er beløp:
        if rad[1] == "mat":
            mat[maaned] += int(rad[2])
        elif rad[1] == "strøm":
            strøm[maaned] += int(rad[2])

# Skriver ut resultatet som en tabell:
maaneder = ["Januar", "Februar", "Mars"]
print(f'{"Måned":10} | {"Mat":10} | {"Strøm":10} | {"Totalt":10}')
print("-"*50)
for i in range(3):
    print(f'{maaneder[i]:10} | {mat[i]:10} | {strøm[i]:10} | {mat[i] + strøm[i]:10}')
print("-"*50)
print(f'{"Totalt":10} | {sum(mat):10} | {sum(strøm):10} | {sum(mat) + sum(strøm):10}')
print("-"*50)

# Lager et stolpediagram (stablet):
# (Dere trengte ikke lage stablet)
plt.bar(maaneder, mat, label="Mat", color="blue")
plt.bar(maaneder, strøm, label="Strøm", color="red", bottom=mat)
plt.title("Utgifter for mat og strøm")
# plt.xlabel("Måned")
plt.ylabel("Beløp (kr)")
plt.legend()
plt.show()
