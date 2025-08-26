# https://projecteuler.net/problem=3 

"""
The prime factors of 13195 are 5,7,13 and 29.
What is the largest prime factor of the number 600851475143?
"""

import math
x = 600851475143
storst = 1

"""
Vår løsning på problemet: Del på de tallene små tallene først.
Ta vare på det nye tallet etter at vi har delt på et lite tall.
Prøv å del på tallet igjen, og prøv deg videre oppover slik, til
du har funnet største faktoren
"""

# Kan stoppe på sqrt av tallet - behøver ikke lete lenger da: Kommer ikke flere etter det
for i in range(2,math.floor(math.sqrt(x))):
    if x % i == 0:
        x = x//i
        storst = i # Ta vare på den største vi har funnet
        print(storst, x)
        i -= 1 # Gå et skritt tilbake: Kanskje det neste tallet også er delelig på denne

print(f"Største faktor {storst}")





""" 
Var noe litt rart i koden over: Burde egentlig ha stoppet løkka
tidligere enn sqrt av x: Må oppdatere den når vi har funnet "ny x".
Prøver på ny løsning her:
"""


x = 600851475143
storst = 1
fortsett = True

while fortsett:

    fortsett = False
    # Kan stoppe på sqrt av tallet - behøver ikke lete lenger da: Kommer ikke flere etter det
    for i in range(2,math.floor(math.sqrt(x))):
        if x % i == 0:
            x = x//i
            storst = i # Ta vare på den største vi har funnet
            print(storst,x)
            fortsett = True # Vi må fortsette litt til :)
            break # Bryter ut av denne forløkka

    # MERK! Når vi har kommet hit: Det vi "har igjen" er også en faktor!
    if x > storst:
        storst = x # x er den største faktoren i tallet


print(f"Største faktor {storst}")