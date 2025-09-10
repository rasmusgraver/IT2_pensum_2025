befolkning_2025 = {
    "Sverige": 10656633,
    "Nigeria": 237527782,
    "Japan": 123103479,
    "Norge": 5623071,
    "Indonesia": 285721236,
    "Egypt": 118365995,
    "Brasil": 212812405,
    "India": 1463865525,
    "Tyskland": 84075075,
    "Mexico": 131946900,
    "Kina": 1416096094,
    "Russland": 143997393,
    "Pakistan": 255219554,
    "Danmark": 6002507,
    "Bangladesh": 175686899,
    "USA": 347275807,
    "Filippinene": 116786962,
    "Etiopia": 135472051
}

# Skriv ut en oversikt med navnene til alle landene ved hjelp av en løkke.
for land in befolkning_2025.keys():
    print(land)
# Skriv ut en oversikt med bare innbyggertallene til alle landene.
for verdi in befolkning_2025.values():
    print(verdi)
# Skriv ut en tekst om hvert land på formen: «X har Y innbyggere».
for land, befolk in befolkning_2025.items():
    print(f"{land} har {befolk} innbyggere")
# Bruk sorted() for å skrive ut lista i oppgave b med landenes navn i alfabetisk rekkefølge. (Hint: sorted(land.keys()))
print(sorted(befolkning_2025.keys()))

# Gå gjennom alle landene og avslutt med en tekst på formen:
#  «X har flest innbyggere. Y har færrest innbyggere.»
flest = 0
land_flest = ""
for land, befolk in befolkning_2025.items():
    if befolk > flest:
        # Jeg har funnet en ny maks!
        flest = befolk
        land_flest = land

print(f"Det landet som har flest innbyggere er {land_flest} med {flest}")
