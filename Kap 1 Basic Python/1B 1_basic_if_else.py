# Spør brukeren om et tall
tall = int(input("Gi meg et tall: "))

# Skriv ut om tallet er positivt, negativt eller 0
if tall == 0:
    print("Tallet er null")
elif tall < 0:
    print("Tallet er negativt")
else:
    print("Tallet er positivt")

# Sjekk om tallet er mindre enn 10, mellom 10 og 100,
# eller over 100
if tall < 10:
    print("Tallet er mindre enn 10")
elif tall > 100:
    print("Tallet er større enn 100")
else:
    print("Tallet er mellom 10 og 100")


# En annen løsning:
# MERK! Opp til deg å se hva du syns blir penest / enklest å lese
if tall < 10:
    print("Tallet er mindre enn 10")
elif tall >= 10 and tall <= 100:
    print("Tallet er mellom 10 og 100")
else:
    print("Tallet er større enn 100")

