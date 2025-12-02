class Bok:
    def __init__(self, tittel:str, forfatter:str) -> None:
        self.tittel = tittel
        self.forfatter = forfatter
        self.utlånt:Låner|None = None

    def visInfo(self):
        if self.utlånt:
            utlåntStr = self.utlånt.lånerID
        else:
            utlåntStr = "Ingen"
        print(f"Bok med tittel {self.tittel} av {self.forfatter}. Utlånt av {utlåntStr}")


class Låner:
    def __init__(self, lånerID:int) -> None:
        self.lånerID = lånerID
        self.lånteBøker:list[Bok] = []
