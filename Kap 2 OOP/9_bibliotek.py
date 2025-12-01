class Bok:
    def __init__(self, tittel:str, forfatter:str) -> None:
        self.tittel = tittel
        self.forfatter = forfatter
        self.utlånt:Låner|None = None


class Låner:
    def __init__(self, lånerID:int) -> None:
        self.lånerID = lånerID
        self.lånteBøker:list[Bok] = []
