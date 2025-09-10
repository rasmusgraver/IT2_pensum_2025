
# Oprette tom ordbok:
bok = {}

# Oprette ordbok med noen verdier fra start:
person1 = {
    "fornavn": "Rasmus",
    "etternavn": "Graver"
} # HUSK: Kolon og komma! 

# skriv ut hele ordboka:
print(person1)
# skriv ut én verdi:
print(person1["etternavn"])


# Legg til (eller endre!) en egenskap(verdi):
person1["etternavn"] = "Hansen"
person1["alder"] = 40

# MERK: Vi bruker alltid strings som keys! 
bok["tittel"] = "Programmering i IT2"
bok["forfatter"] = "Nils Markussen"

print(bok)

# MERK: Med f-strings:
print(f"Tittel på boka er {bok['tittel']}")

bok["forlag"] = "Gyldendal"

# Gå gjennom en ordbok:
for key in bok.keys():
    print(f"Nøkkel: {key} med verdi: {bok[key]}")

# Bare hente ut verdiene:
for verdi in bok.values():
    print(f"Verdi: {verdi}")

for key, value in bok.items():
    print(f"{key}: {value}")
    