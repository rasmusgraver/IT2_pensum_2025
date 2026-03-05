from geometri import Rektangel, Kvadrat

rekt1 = Rektangel(2,5)
rekt2 = Rektangel(3,4)

if 10 != rekt1.areal():
    print("FEIL!! Rektangelet skal ha 10 i areal")
if 14 != rekt1.omkrets():
    print("FEIL!! Rektangelet skal ha 14 i omkrets")

if rekt1.farge == "blå":
    print("Fargetest 1 suksess")
else:
    print("FEIL: Første rektangel skal ha farge blå")
if rekt2.farge == "rød":
    print("Fargetest 2 suksess")
else:
    print("FEIL: Andre rektangel skal ha farge rød")


kvd1 = Kvadrat(3)
if 9 != kvd1.areal():
    print("FEIL!! Kvadratet skal ha 9 i areal")
if 12 != kvd1.omkrets():
    print("FEIL!! Kvadratet skal ha 12 i omkrets")

if kvd1.farge == "grønn":
    print("Fargetest 3 suksess")
else:
    print("FEIL: Tredje Rektangel skal ha farge grønn")

kvd2 = Kvadrat(4)
if kvd2.farge == "blå":
    print("Fargetest 4 suksess")
else:
    print("FEIL: Fjerde Rektangel skal ha farge blå")
    print(kvd2.farge)




