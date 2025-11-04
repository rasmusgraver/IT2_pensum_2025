
# Åpne filen for lesing
with open('DataFiler/tall_liste.txt', 'r') as fil:
    # Les fila - EN LINJE av gangen
    for linje in fil:
        # linje = linje.strip()
        tallene = linje.strip().split("-")

        print("Tallene:", tallene)

        total = 0
        for s in tallene:
            # HUSK! Må gjøre om fra streng til tall!
            t = int(s)
            total += t


        # Skriv ut resultatet
        print("Totalsum:", total)
        print(f"Gjennomsnitt: {total/len(tallene):.2f}")

