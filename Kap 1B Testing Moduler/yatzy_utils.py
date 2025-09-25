from random import randint

def nyttKast():
    # Returner liste med 5 random tall
    # f.eks. [1,2,4,5,1]
    kast = []
    for i in range(5):
        kast.append(randint(1,6))
    return kast

def flestForekomster(kast):
    # returner det det er mest av i et kast
    # f.eks. om kast er [1,2,4,5,1] så returnerer den 1 (int)
    mest_av = 0
    mest_ant = 0
    for i in range(1,7):
        k = kast.count(i)
        if k > mest_ant:
            mest_ant = k
            mest_av = i
    return mest_av

def nullUt(kast, behold):
    # Null ut det som ikke er "behold"
    # f.eks. nullUt([1,2,4,5,1], 1)
    # returnerer [1,0,0,0,1]
    for i in range(len(kast)):
        if kast[i] != behold:
            kast[i] = 0 # Ikke det vi vil beholde: "null ut"
    return kast


def reKast(kast):
    for i in range(len(kast)):
        if kast[i] == 0:
            # Kast den på nytt
            kast[i] = randint(1,6)
    return kast
