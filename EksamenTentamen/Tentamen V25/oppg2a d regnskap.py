import csv
import matplotlib.pyplot as plt
from pprint import pprint

filnavn = "DataFiler/utgifter.csv"

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

# Skriver ut resultatet som et sektordiagram:
periode = ""
while periode not in ["1", "2", "3", "t"]:
    periode = input("Hvilken periode vil du se på? (1, 2, 3 eller t (total)): ")

if periode == "t":
    utgifter = [sum(mat), sum(strøm)]
else:
    periode = int(periode) - 1
    utgifter = [mat[periode], strøm[periode]]

labels = ["Mat", "Strøm"]
plt.pie(utgifter, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Utgifter for mat og strøm")
plt.show()

