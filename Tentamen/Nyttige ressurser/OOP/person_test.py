from person import Person

p1 = Person("Ola")
p2 = Person("Rasmus")

if p1.personNr == 1:
    print("Suksess 1")
else:
    print("Feil: Person 1 skal ha nr 1")

if p2.personNr == 2:
    print("Suksess 2")
else:
    print("Feil: Person 2 skal ha nr 2")
