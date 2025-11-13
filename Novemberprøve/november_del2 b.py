import matplotlib.pyplot as plt
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

total = totMat + totStrom
print("Totalt")
print("="*20)
print(f"Mat:    {totMat}")
print(f"Strøm:  {totStrom}")
print(f"Totalt: {total}")

# Fra Kap 3 Plotting filene:
# partiforkortelser = ["AP", "FrP", "H", "KrF", "MDG", "R", "Sp", "SV", "V", "PF"]
# representanter = [48, 21, 36, 3, 3, 8, 28, 13, 8, 1]
# plt.pie(representanter, labels=partiforkortelser)

labels = ["Strøm", "Mat"]
verdier = [totStrom, totMat]
# plt.pie(verdier, labels=labels)

# Bedre: Fancy pie:

fig, ax = plt.subplots(figsize=(8, 6))

farger = ["#004281", "#25a23c"]

ax.pie(
    verdier,
    labels=labels,
    colors=farger,
    # autopct='%1.1f%%',
    # Få inn verdien også:
    autopct=lambda pct: f"{pct:.1f}%\n({int(round(pct/100*total))})",
    startangle=90,
    labeldistance=1.15,
    wedgeprops={"linewidth": 1, "edgecolor": "white"},
    textprops={"color": "white"}  # setter fargen på autopct teksten
)

# Legg til legend hvis du vil ha samleforklaring ved siden av
ax.legend(labels, title="Utgift", loc="lower right" )

plt.title("Utgifter til strøm og mat", fontsize=14)
plt.tight_layout()


plt.show()
