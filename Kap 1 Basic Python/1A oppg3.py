# Fra blanda oppgaver bakerst i kap 1A 

"""
Oppgave 3
Lag teksten maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes". 
Lag et program som lar brukeren skrive inn et tall som representerer et månedsnummer. 
Programmet skal deretter hente ut og skrive ut riktig månedsforkortelse 
fra teksten maaneder.
"""

maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"
tall = int(input("Hvilken måned? "))
start = (tall - 1) * 3 # Litt vanskelig å tenke rett her - prøv med noen eksempler i hodet...
print(f"Månedsforkortelsen er {maaneder[start:start+3]}")
