from tekst_utils import forekomstAvBokstav

# Tester med ulike inputs:
ant = forekomstAvBokstav("Hei", "e")
if ant != 1:
    print(f"Testen feilet med 'Hei' og 'e'. Den svarte med {ant}")
# Kan bruke assert slik (om du vil):
# MERK: Til vårt formål holder det fint med if og print
# assert ant == 1, f"Testen feilet med 'Hei' og 'e'. Den svarte med {ant}"

ant = forekomstAvBokstav("", "e")
if ant != 0:
    print(f"Testen feilet med '' og 'e'. Den svarte med {ant}")

ant = forekomstAvBokstav("pluto", "e")
if ant != 0:
    print(f"Testen feilet med 'pluto' og 'e'. Den svarte med {ant}")

ant = forekomstAvBokstav("lorem ipsum doloret", "o")
if ant != 3:
    print(f"Testen feilet med 'lorem' og 'o'. Den svarte med {ant}")
