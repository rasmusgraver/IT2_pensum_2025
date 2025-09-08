# kast en terning og print resultatet:
import random

terning = random.randint(1,6)
# print(f"Du kastet {terning}")

# CHALLENGE: Kast 2 terninger inntil summen er 12
# Hvor mange kast tok det? 
total = 0
antall = 0
while total != 12:
    t1 = random.randint(1,6)
    t2 = random.randint(1,6)
    total = t1 + t2
    antall += 1
print(f"Du kastet {total}, det tok {antall} ganger")


