import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "DataFiler/friluftsaktiviteter.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*20)

    for rad in filinnhold:
        print("Rad:", rad[4])

    xer = []
    yer = []

    plt.scatter(xer, yer)
    plt.show()
    