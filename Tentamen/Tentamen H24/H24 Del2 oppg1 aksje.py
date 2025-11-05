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

import matplotlib.pyplot as plt
import csv
from datetime import datetime

filnavn = "DataFiler/aksjekurs.csv"
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # NB! MERK! Denne er nice!
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*30)

    # Listene vi skal plotte:
    datoer = []
    kurs_liste = []

    for rad in filinnhold:
        # NB!!! HUSK!!! Ikke bare append det som en string! Konverter til rett datatype!
        datoer.append(  datetime.strptime(rad[0], "%Y-%m-%d")  )
        kurs_liste.append(  float(rad[1])  )


# Oppg 1 c) Legg til rullerende gjennomsnitt: 
snitt_liste = []
lengde = len(kurs_liste)
for i in range(lengde):
    # Skal gå 5 skritt bakover, og 5 skritt frem i listen, MEN kan ikke gå
    # lenger bakover enn 0, eller lenger frem en lengden av kurs-listen:
    start = max(0, i-5)
    slutt = min(lengde, i+5)
    # MERK: Denne syntaxen med [:] er nice! Henter ut en subliste kjapt og enkelt!
    snitt = gjennomsnitt_av_liste(kurs_liste[start:slutt])
    snitt_liste.append(snitt)


plt.plot(datoer, kurs_liste, label="aksjekurs", color="skyblue")
plt.plot(datoer, snitt_liste, label="snittkurs 10 dager", color="purple")

plt.xlabel("Dato")
plt.ylabel("Kurs")
plt.legend(loc="upper left")

# Eventuelt: "zoom" litt inn (fjerner et par topper og bunner på kursen)
# plt.ylim(60, 140)

# Tight layout gjør at vi får plass til å se etikettene på x-aksen (datoene)
# Trengte det ikke nå lenger... Men: Kjekk kommando å ha i verktøykassa!
# plt.tight_layout()


plt.show()


"""
Kommentar: I 2024 brukte jeg manuelt xticks, med å legge til kun hver tiende dato
på denne måten (bare til info til de som er interessert...)

    # Det blir for trangt å printe alle datoer: 
    # Vi lagrer bare hver 10ende, og bruker det som "xticks"
    labels = []
    ticks = []

    # Inne i for løkka, der vi lagrer dato og kurs:

        # Lagrer hver 10ende til å bruke som "xticks":
        i = len(datoer)
        if i%10 == 0:
            labels.append(rad[0]) # MERK: Her la jeg det bare til som en string!
            ticks.append(i)


# Og så etter plt.plot:
plt.xticks(ticks=ticks, labels=labels, rotation=90)




# (Fancy forslag fra ChatGPT (finner ticks og labels "her og nå") (Med denne måten kunne jeg droppet all koden over her...) )
# plt.xticks(ticks=range(0, len(dato), 10), labels=dato[::10], rotation=90)

"""
