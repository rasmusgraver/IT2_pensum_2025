

class Instrument:

    def __init__(self, typeInstrument):
        self.typeInstrument = typeInstrument

 
    def spillLyd(self):
        if self.typeInstrument == "Gitar":
            print("PlingPlong")
        elif self.typeInstrument == "Tromme":
            print("BomBom")
        else:
            print("Generell musikklyd...")
    
    def visInfo(self):
        print(f"Jeg er et instrument, av typen {self.typeInstrument}")

piano = Instrument("Piano")
tromme = Instrument("Tromme")

piano.visInfo()
tromme.visInfo()


piano.spillLyd()
tromme.spillLyd()

print(type(piano))
print(type(tromme))

if type(piano) == Instrument:
    print("Piano er et instrument")

# MERK: Denne er ikke så informativ... Viser bare noe slikt
# <__main__.Instrument object at 0x000001B3EA666A50>
# print(piano)
