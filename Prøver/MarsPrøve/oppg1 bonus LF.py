import random

# Bonus-oppgaven til oppgave 1 - les highscore fra fil

FILNAVN = "highscore.txt"

def lesHighscore() -> int:
    try:
        with open(FILNAVN, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 999 # Bare en veldig dårlig highscore...

def skrivHighscore(highscore:int):
    with open(FILNAVN, "w", encoding="utf-8") as f:
        f.write(str(antallGjett))


hemmeligTall = random.randint(0,50)

gjett = -1
antallGjett = 0

while gjett != hemmeligTall and antallGjett < 10:
    antallGjett += 1
    gjett = int(input("Gjett tallet: "))
    if gjett < hemmeligTall:
        print("Du må gjette høyere!")
    if gjett > hemmeligTall:
        print("Du må gjette lavere!")    


if gjett == hemmeligTall:
    print(f"Gratulerer! Du klarte det på {antallGjett} forsøk")

    # Bonus-oppgaven: Sjekk highscore:
    highscore = lesHighscore()

    if antallGjett < highscore:
        print("Ny highscore!")
        skrivHighscore(highscore)
    else:
        print(f"Highscore er {highscore} forsøk. Prøv å slå den neste gang!")

else:
    print(f"Nei! Du klarte det ikke på 10 forsøk. Tallet var {hemmeligTall}")

