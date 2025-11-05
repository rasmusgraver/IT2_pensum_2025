# Kast en terning (virtuelt…) 100 ganger og plot som et stolpediagram antall 1,2,3,4,5,6ere. 
# Det finnes en «rett fram» enkel måte å gjøre dette på. 

# I fil 2:
# Utfordring: Etter du har gjort den enkle varianten: Kan du lagre alle kastene som en liste med 100 elementer i (hvert kast). Og så undersøke histogram plotting? (HINT: Lag 6 «bins») 

import random
import matplotlib.pyplot as plt

# Lagrer en liste som tar vare på antall
# 1,2,3,4,5,6ere (MERK: Lite "indeks problem")
# Vi teller antall 0,1,2,3,4,5ere...
results = [0]*6

# Alternativ løsning: Lag en ordbok der
# "kastet" er nøkkel, og verdien er antallet
# SE EGEN FIL FOR DETTE!

for i in range(100):
    kast = random.randint(0,5)
    results[kast] += 1


# Kjapp/Fancy måte å lage en liste med verdiene 1,2,3,4,5,6:
kastVerdier = list(range(1,7))

plt.bar(kastVerdier, results)
plt.show()
