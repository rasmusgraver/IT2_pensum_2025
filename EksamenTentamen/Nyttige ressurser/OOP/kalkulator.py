class Kalkulator:

    def __init__(self):
        pass

    def pluss(self, a, b):
        return a + b
    
    def dele(self, a, b):
        return a / b
    

# Tester koden:
kalk = Kalkulator()

if kalk.pluss(2,5) == 7:
    print("Suksess med 2+5")
else:
    print(f"FEIL med 2+5. Returnerte {kalk.pluss(2,5)}")

    