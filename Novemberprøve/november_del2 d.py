import csv
from pprint import pprint

filnavn = "DataFiler/regnskap.csv"
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # NOTE! Denne er nice!
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*30)

    # Bruker tallene 1,2,3 for jan, feb, mars:
    totBok = {
        "mat": {
            1: 0,
            2: 0,
            3: 0,
        },
        "strøm": {
            1: 0,
            2: 0,
            3: 0,
        }
    }

    for rad in filinnhold: 
        # Henter mnd nr rett ut fra datoen:
        mnd = int(rad[0][4])
        totBok[rad[1]][mnd] += int(rad[2])
        

    pprint(totBok)