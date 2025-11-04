
# Åpne filen for lesing
with open('DataFiler/tall_liste.txt', 'r') as fil:
    # Les fila - EN LINJE av gangen
    for linje in fil:
        # linje = linje.strip()
        tallene = linje.split("-")

        print("Tallene:", tallene)

        total = 0
        for s in tallene:
            t = int(s)
            total += t


        # Skriv ut resultatet
        print("Totalsum:", total)
        print(f"Gjennomsnitt: {total/len(tallene):.2f}")

