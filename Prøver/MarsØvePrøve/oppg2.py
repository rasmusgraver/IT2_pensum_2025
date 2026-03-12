class Trener:
    def __init__(self, navn:str) -> None:
        self.navn = navn

    def __repr__(self) -> str:
        return self.navn

class Sal:
    def __init__(self, navn:str) -> None:
        self.navn = navn

    def __repr__(self) -> str:
        return self.navn


class Time:
    def __init__(self, navn:str, trener:Trener, sal:Sal, dag:str, tid:str) -> None:
        self.navn = navn
        self.trener = trener
        self.sal = sal
        self.dag = dag
        self.tid = tid
    
    def __repr__(self) -> str:
        return f"{self.navn} {self.dag} {self.tid} på Rom {self.sal} med {self.trener}"
    


trener = Trener("Ståle Spinner")
sal = Sal("Spinning")
time1 = Time("intervall 1", trener, sal, "Mandag", "06:15")
time2 = Time("intervall 2", trener, sal, "Mandag", "16:15")

print(time1)
print(time2)


