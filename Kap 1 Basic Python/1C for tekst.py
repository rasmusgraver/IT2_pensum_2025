# Kan også bruke en for løkke gjennom en tekst
minTekst = "Python er bra"

# Finnes 2 måter:
for i in range(len(minTekst)):
    print(minTekst[i], end=".")
print() # Må ha et linjeskift til slutt

# Enklere og kortere og tydeligere:
for bokstav in minTekst:
    print(bokstav, end=",")
print() # Må ha et linjeskift til slutt

# Få tak i den siste bokstaven:
print(minTekst[-1])
# Eller nest siste:
print(minTekst[-2])


# CHALLENGE: Skriv ut teksten baklengs
# Uten noen ekstra mellomrom
for i in range(len(minTekst)-1, -1, -1):
    print(minTekst[i], end="")
print() # Må ha et linjeskift til slutt


