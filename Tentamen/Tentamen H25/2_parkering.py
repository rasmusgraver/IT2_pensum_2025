class Bil:
    def __init__(self, farge:str, modell:str, registreringsnummer:str):
        self.farge = farge
        self.modell = modell
        self.registreringsnummer = registreringsnummer

    def __repr__(self):
        return f"Bil({self.registreringsnummer}, {self.modell}, {self.farge})"


class Parkeringshus:
    MAX_PLASSER = 5

    def __init__(self):
        # ordbok: registreringsnummer -> Bil
        self.parkerte = {}

    def parkerBil(self, bil:Bil):
        """
        Legger bilen i parkeringshuset.
        Returnerer True hvis parkert, False hvis allerede parkert eller fullt.
        """
        reg = bil.registreringsnummer
        if reg in self.parkerte:
            print("FEIL: Bilen er allerede parkert!")
            return False
        if len(self.parkerte) >= self.MAX_PLASSER:
            print("FEIL: Det er fullt!")
            return False
        self.parkerte[reg] = bil
        return True

    def hentUtBil(self, regNr:str):
        """
        Henter ut og returnerer bil med regNr, eller None hvis ikke funnet.
        """
        if regNr in self.parkerte:
            print("FEIL: Bilen er allerede parkert!")
            return False

        return self.parkerte.pop(regNr, None)

    def listFarger(self):
        """
        Returnerer en liste med fargene til alle parkerte biler (inkluderer duplikater).
        """
        return [bil.farge for bil in self.parkerte.values()]

