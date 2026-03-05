
def tilListe(tall:int) -> list[int]:
    liste = []
    tekst = str(tall)
    for c in tekst:
        liste.append(int(c))
    return liste




def fraListe(liste:list[int]) -> int:
    tall = 1000*liste[0] + 100*liste[1] + 10*liste[2] + liste[3]
    return tall








"""
tallliste = tilListe(3142)
if tallliste != [3,1,4,2]:
    print("NEI! Det ble feil:", tallliste)
else:
    print("YES - bra jobb!")

"""


def tallspill(tall:int):
    forrigeTall = 0
    while tall != forrigeTall:
        forrigeTall = tall
        synkende = tilListe(tall)
        stigende = list(synkende) # OBS: Lager en kopi av listen!
        stigende.sort() # OBS: Sorterer "in place" (selve listen)
        synkende.sort(reverse=True)
        # Alternativ løsning ville vært å bruke sorted(liste)
        liteTall = fraListe(stigende)
        stortTall = fraListe(synkende)
        tall = stortTall - liteTall
        print(forrigeTall, "->", stortTall, "-", liteTall, "=", tall)


tallspill(3142)

