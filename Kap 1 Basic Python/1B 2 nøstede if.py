# NOTE: Når vi tester programmene våre er det 
# enklest å bare angi tallene, ikke bruk input()
tall1 = 2
tall2 = 2.2

# MERK: Vi kan fint å if setninger inni if-setninger
# Dette gjelder også for for- og while-løkker: Kan fint
# ha dem innover i flere "lag i dybden": MEN: Det kan bli vanskelig 
# å lese om det blir for mange lag innover! Vi kommer til å bruke funksjoner
# for å unngå dette. 
if (tall1 != tall2):
    if (tall1 > tall2):
        print("Tall 1 er størst.")
    else:
        print("Tall 2 er størst.")
else:
    print("Tallene er like.")


# Alternativ løsning:
if (tall1 == tall2):
  print("Tallene er like.")
elif (tall1 > tall2):
    print("Tall 1 er størst.")
else:
    print("Tall 2 er størst.")

