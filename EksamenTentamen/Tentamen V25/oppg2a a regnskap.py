import csv
import matplotlib.pyplot as plt
from pprint import pprint

filnavn = "DataFiler/utgifter.csv"

# Summerer opp for mat og strøm hver for seg:
mat = 0
strøm = 0

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # Skipper første linje:
    next(filinnhold)

    for rad in filinnhold:
        # print(rad) # Debugging
        # Kjører gjennom hver rad i filen:
        # print(f"Rad: {rad}") # Debugging

        # Summerer opp for mat og strøm hver for seg:
        # Rad 0 er dato, rad 1 er type, rad 2 er beløp:
        if rad[1] == "mat":
            mat += int(rad[2])
        elif rad[1] == "strøm":
            strøm += int(rad[2])

# Skriver ut resultatet:
print(f"Mat: {mat} kr")
print(f"Strøm: {strøm} kr")
print(f"Totalt: {mat + strøm} kr")
