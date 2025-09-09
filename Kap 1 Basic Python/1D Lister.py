liste = [1,True, 2, "A"]

# Print ut første element
print(liste[0])
# Print ut siste element
print(liste[-1])

# Endre element: F.eks. endre True til False
liste[1] = False

print("-"*40) # Lager en strek
# for løkke som printer ut alle elementene
for elm in liste:
    print(elm)

print("-"*40) # Lager en strek
# Kan også gjøre det med en for i in range:
for i in range(len(liste)):
    print(liste[i])

# MERK: len angir lengden til listen: ant elementer
print("len:", len(liste)) # len: 4

# IndexError: print(liste[len(liste)])
try:
    a = liste[7] # får en IndexError
    print("Alt gikk bra:", a)
except IndexError as e:
    print("Vi fikk en index error:", e)

# Sub-lister: Hente ut en del av en liste:
print("Sublister")
liste = [0,1,2,3,4,5,6,7]
print(liste[1:3]) # Henter ut en liste fra index 1 til 3
# MERK: Er fra og med, og til (ikke til og med)
# liste[1:3] er [1,2]

print(liste[1:7:2]) # Henter ut annenhvert tall
# printer [1,3,5]


# Kan også ha pluss og ganging med lister
liste1 = [1,2,3]
liste2 = ["a", "b", "c"]
# Kan legge de sammen:
print(liste1 + liste2)
# printer  [1, 2, 3, 'a', 'b', 'c']
# kan gange:
print(liste1*3)
# printer [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Vi kikket også på 2-dimensjonale lister:
tabell = [
  ["A", "B", "C"],
  ["D", "E", "F"],
  ["G", "H", "I"]
]

print(tabell[0][0]) # Printer ut "A"
print(tabell[1][0]) # Printer ut "D"
print(tabell[2][1]) # Printer ut "H"

