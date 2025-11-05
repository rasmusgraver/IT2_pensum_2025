class Person:

    # NB!! Ikke kall denne det samme som "self.personNr"!
    personNrTeller = 1

    def __init__(self, navn):
        self.navn = navn
        self.personNr = Person.personNrTeller
        Person.personNrTeller += 1

