import random

# Challenge: 
# Kast 2 terninger til summen blir 12
# Gjør dette tusen ganger! Hva er totalt kast? 
# Hva blir snittet: Hvor mange ganger må du forvente å kaste før du får 2 seksere?


# Vi skal snart lære om funksjoner... Lager en funksjon for dette:
def kastTilSum12():
    """ Kaster 2 terninger inntil summen er 12.
        Returnerer hvor mange ganger vi måtte kaste (int) """
    antall = 0 # Antall kast det tok før vi fikk 12
    t1 = t2 = 0
    while (t1 + t2) != 12:
        t1 = random.randint(1,6)
        t2 = random.randint(1,6)
        antall += 1 # Øker antallet kast det tok med 1

    return antall

# Eksempel på bruk av funksjonen vår:
ant = kastTilSum12()
print(f"Det tok {ant} ganger")
ant = kastTilSum12()
print(f"Denne gangen tok det {ant} ganger")


# Så: Over til oppgaven: Gjør dette tusen, eller ti tusen, ganger
ANT_KAST = 10000 # Bruker denne flere steder, så lager en variabel, eller egentlig KONSTANT av den
tot_kast = 0 # Antall kast vi har brukt alt i alt totalt
for _ in range(ANT_KAST): # HUSK: Bruker _ for å markere at vi ikke bryr oss om "i" telleren
    tot_kast += kastTilSum12() # Kan gjøre det så enkelt: Legge til total summen vår

print(f"{ANT_KAST} ganger tok {tot_kast} kast")
print(f"Det vil si at snittet var {tot_kast/ANT_KAST:.2f}")
