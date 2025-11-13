import csv
from pprint import pprint

filnavn = "DataFiler/regnskap.csv"
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # NOTE! Denne er nice!
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*30)

    totBok = {
        "mat": 0,
        "strøm": 0
    }

    for rad in filinnhold: 
        totBok[rad[1]] += int(rad[2])
        

    pprint(totBok)