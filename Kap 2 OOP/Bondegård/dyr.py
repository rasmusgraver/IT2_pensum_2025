import random

class Dyr:
    def __init__(self) -> None:
        pass
    def __repr__(self) -> str:
        return f"Dyr"

class Ku(Dyr):
    def __init__(self) -> None:
        super().__init__()
    def __repr__(self) -> str:
        return f"Ku"

    def giMelk(self) -> int:
        return 10
    
class Høne(Dyr):
    def __init__(self) -> None:
        super().__init__()
    def __repr__(self) -> str:
        return f"Høne"

    # Returnerer 1,2 eller 3 egg
    def leggEgg(self) -> int:
        return random.randint(1,3)
    
