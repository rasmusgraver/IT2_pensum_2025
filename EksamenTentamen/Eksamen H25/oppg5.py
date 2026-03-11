

class Tallviser:
    def __init__(self, verdi:int, maks_verdi:int) -> None:
        self.verdi = verdi
        self.maks_verdi = maks_verdi

    def set_verdi(self, v) -> None:
        if v > self.maks_verdi:
            raise ValueError("For høy verdi!")
        if v < 0:
            raise ValueError("Kan ikke ha negativ verdi!")
        # Har sjekket verdien, og den er fin:
        self.verdi = v

    def oek(self) -> None:
        self.verdi += 1
        if self.verdi > self.maks_verdi:
            # Reset tilbake til start:
            self.verdi = 0

    def vis_verdi(self) -> str:
        if self.verdi < 10:
            return "0" + str(self.verdi)
        else:
            return str(self.verdi)


class DigitalKlokke:

    def __init__(self) -> None:
        self.timer = Tallviser(0, 23)
        self.minutter = Tallviser(0, 59)

    def set_tid(self, t, m):
        self.timer.set_verdi(t)
        self.minutter.set_verdi(m)

    def tid_gaar(self) -> None:
        self.minutter.oek()
        # Sjekker om vi har "gått rundt":
        if self.minutter.verdi == 0:
            self.timer.oek()

    def vis_tid(self) -> str:
        return self.timer.vis_verdi() + ":" + self.minutter.vis_verdi()


# TESTER KODEN:
# ================================
# Lager en DigitalKlokke:
klokke = DigitalKlokke()
klokke.set_tid(10, 40)
# Tikk et par hakk fremover:
klokke.tid_gaar()
klokke.tid_gaar()
# Sjekk at klokka nå er 10:42
if klokke.vis_tid() == "10:42":
    print("YES, Jeg er god!")
else:
    print("NEI! Jobbe mer!", klokke.vis_tid() )

# Vanskeligere test: Over 60 min:
klokke.set_tid(10, 58)
# Tikk fremover, og test hver gang:

klokke.tid_gaar()
# Sjekk at klokka nå er 10:59
if klokke.vis_tid() == "10:59":
    print("YES, 10:59")
else:
    print("NEI! Jobbe mer!", klokke.vis_tid() )

klokke.tid_gaar()
# Sjekk at klokka nå er 11:00
if klokke.vis_tid() == "11:00":
    print("YES, 11:00")
else:
    print("NEI! Jobbe mer!", klokke.vis_tid() )

klokke.tid_gaar()
# Sjekk at klokka nå er 11:01
if klokke.vis_tid() == "11:01":
    print("YES, 11:01")
else:
    print("NEI! Jobbe mer!", klokke.vis_tid() )

