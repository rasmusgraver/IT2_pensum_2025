
import csv

filnavn = "DataFiler/regnskap.csv"
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # NOTE! Denne er nice!
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*30)

    totMat = 0
    totStrom = 0
    for rad in filinnhold:
        if rad[1] == "mat":
            totMat += int(rad[2])
        else:
            totStrom += int(rad[2])

print("Totalt")
print("="*20)
print(f"Mat:    {totMat}")
print(f"Strøm:  {totStrom}")
print(f"Totalt: {totMat+totStrom}")
