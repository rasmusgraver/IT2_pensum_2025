
total = 0

# Åpne filen for lesing
with open('DataFiler/tall.txt', 'r') as fil:
    # Les hele filinnholdet som en streng
    innhold = fil.read()
    print("Innholdet av fila er:", innhold, "slutt")

    # Strip fjerner "luft" foran og bak strengen:
    innhold = innhold.strip()
    # Split: Returnerer en liste: (MERK at vi kan si hva vi splitter på)
    tallene = innhold.split(",")

    print("Tallene:", tallene)

    for streng in tallene:
        t = int(streng)
        total += t


# Skriv ut resultatet
print("Totalsum:", total)
print(f"Gjennomsnitt: {total/len(tallene):.2f}")

# Skriv resultatet til fil:
with open('DataFiler/tall_output.txt', 'w') as fil:
    fil.write(f"Totalsum: {total}\n")
    fil.write(f"Gjennomsnitt: {total/len(tallene):.2f}\n")
