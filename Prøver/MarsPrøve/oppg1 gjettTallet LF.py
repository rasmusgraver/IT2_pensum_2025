import random

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
else:
    print(f"Nei! Du klarte det ikke på 10 forsøk. Tallet var {hemmeligTall}")

