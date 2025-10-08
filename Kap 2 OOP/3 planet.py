import math

class Planet:


    def __init__(self, navn, solavstand, radius):
        """
        Parametere:
            - navn (str): Navnet på planeten
            - solavstand (float): avstand i millioner km
            - radius (int): radius til planeten i km
        """
        if type(radius) != int:
            raise ValueError("Radius må være en int!")

        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius

    def volum(self):
        """
        Returnerer volumet til planeten i kubikk km (int)
        """
        return int((4/3) * math.pi * (self.radius**3))

    def overflateAreal(self):
        pass

    def solavstandMinutter(self):
        """
        Returnerer int: Hvor mange minutter bruker 
        lyset fra sola til planeten
        """
        solAvstandKm = self.solavstand * 1e6
        return int( round ( ( solAvstandKm / 300e3 ) / 60 ) )


"""
Jorden
Gjennomsnittlig avstand fra solen: 149,6 millioner km
Radius: 6 371 km
"""
jorden = Planet("Jorden", 149.6, 6371)
"""
Jupiter
Gjennomsnittlig avstand fra solen: 778,5 millioner km
Radius: 69 911 km
"""
jupiter = Planet("Jupiter", 778.5, 69911)

jordensVolum = jorden.volum()
jupitersVolum = jupiter.volum()

print(f"Jordas volum er {jordensVolum}")
print(f"Jupiters volum er {jupitersVolum}")
print(f"Det betyr at det er plass til {round(jupitersVolum/jordensVolum)} jordkloder i jupiter")


print(f"Lyset bruker {jorden.solavstandMinutter()} minutter til jorda")
print(f"Lyset bruker {jupiter.solavstandMinutter()} minutter til jupiter")
