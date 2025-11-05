import matplotlib.pyplot as plt
import csv

# Oppg 1 a) Gjennomsnittsfunksjon:
def gjennomsnitt_av_liste(liste):    
    totalt = sum(liste)
    lengde = len(liste)
    return totalt / lengde

# Tester
print(gjennomsnitt_av_liste([1, 2, 3]))              # Skal printe 2.0
print(gjennomsnitt_av_liste([2, 2, 3]))              # Skal printe 2.333...
print(gjennomsnitt_av_liste([1, 2, 3, 3, 2, 7, 6]))  # Skal printe 3.42857..

# Oppg 1 b) Plotte aksjekurs:
filnavn = "DataFiler/aksjekurs.csv"
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)

    print("-"*30)

    # Listene vi skal plotte:
    datoer = []
    kurs_liste = []
    # Det blir for trangt å printe alle datoer: Vi lagrer bare hver 10ende, og bruker det som "xticks"
    labels = []
    ticks = []

    for rad in filinnhold:
        datoer.append(rad[0])
        kurs_liste.append(float(rad[1]))
        i = len(datoer)
        # Lagrer hver 10ende til å bruke som "xticks":
        if i%10 == 0:
            labels.append(rad[0])
            ticks.append(i)


# Oppg 1 c) Legg til rullerende gjennomsnitt: 
snitt_liste = []
lengde = len(kurs_liste)
for i in range(lengde):
    # Skal gå 5 skritt bakover, og 5 skritt frem i listen, MEN kan ikke gå
    # lenger bakover enn 0, eller lenger frem en lengden av kurs-listen:
    start = max(0, i-5)
    slutt = min(lengde, i+5)
    snitt = gjennomsnitt_av_liste(kurs_liste[start:slutt])
    snitt_liste.append(snitt)


plt.plot(datoer, kurs_liste, label="aksjekurs")
plt.plot(datoer, snitt_liste, label="snittkurs 10 dager")

plt.xlabel("Dato")
plt.ylabel("Kurs")
plt.legend(loc="upper left")

# Det blir for mange datoer: Bare vis hver 10ende:
plt.xticks(ticks=ticks, labels=labels, rotation=90)

# (Fancy forslag fra ChatGPT (finner ticks og labels "her og nå"):)
# plt.xticks(ticks=range(0, len(dato), 10), labels=dato[::10], rotation=90)

# Tight layout gjør at vi får plass til å se etikettene på x-aksen (datoene)
plt.tight_layout()

plt.show()

