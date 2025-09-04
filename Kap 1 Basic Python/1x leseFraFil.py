
total = 0

# Åpne filen for lesing
with open('DataFiler/tall.txt', 'r') as fil:
    # Les hele filinnholdet som en streng
    innhold = fil.read()
    
    # Del opp strengen ved hver komma
    streng_liste = innhold.split(',')

    # Gå gjennom hver streng i listen
    for streng in streng_liste:        
        # Konverter til heltall og legg til i summen
        tall_verdi = int(streng)
        total += tall_verdi

# Skriv ut resultatet
print("Totalsum:", total)